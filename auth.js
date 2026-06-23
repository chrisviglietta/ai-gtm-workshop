/* ══════════════════════════════════════════════════════════════════
   auth.js — soft access gate for the Workshop portal

   - Tabs/links pointing at gated pages (For You, Post-workshop) are
     locked until the visitor enters a valid access code on home.html.
   - Locked links show a padlock, are dimmed, and (on home) open the
     access modal instead of navigating.
   - Gated pages also carry an inline head-guard that bounces locked
     visitors back to home.html (see each page's <head>).

   ADMIN: the code CLAY-ADMIN unlocks the full attendee experience AND
   flags the visitor as admin (localStorage 'clay_ws_admin'). Admins can
   open the internal dashboard (cohort-progress.html), which is guarded
   so non-admins are bounced to home.html. A floating link lets admins
   jump to the dashboard (and back) from any page.

   State lives in localStorage: 'clay_ws_unlocked' (attendee) and
   'clay_ws_admin' (admin). This is a SOFT gate (matches the
   ACCESS-CODES.md threat model), not real auth.
   ══════════════════════════════════════════════════════════════════ */
(function () {
  var KEY = 'clay_ws_unlocked';
  var ADMIN_KEY = 'clay_ws_admin';
  var ADMIN_CODE = 'CLAY-ADMIN';
  var GATED = ['welcome.html', 'post-workshop.html'];
  var DASHBOARD = 'cohort-progress.html';

  var Auth = window.ClayAuth = {
    ADMIN_CODE: ADMIN_CODE,
    isUnlocked: function () {
      try { return localStorage.getItem(KEY) === '1'; } catch (e) { return false; }
    },
    isAdmin: function () {
      try { return localStorage.getItem(ADMIN_KEY) === '1'; } catch (e) { return false; }
    },
    unlock: function (code) {
      try {
        localStorage.setItem(KEY, '1');
        if (code) localStorage.setItem('clay_ws_code', String(code).toUpperCase());
        if (code && String(code).toUpperCase() === ADMIN_CODE) {
          localStorage.setItem(ADMIN_KEY, '1');
        }
      } catch (e) {}
    },
    lock: function () {
      try {
        localStorage.removeItem(KEY);
        localStorage.removeItem(ADMIN_KEY);
      } catch (e) {}
    }
  };

  function fileOf(href) {
    if (!href) return '';
    try {
      var a = document.createElement('a');
      a.href = href;
      return (a.pathname.split('/').pop() || '').toLowerCase();
    } catch (e) { return ''; }
  }

  function currentFile() {
    return (location.pathname.split('/').pop() || '').toLowerCase();
  }

  function injectStyle() {
    if (document.getElementById('clay-auth-style')) return;
    var s = document.createElement('style');
    s.id = 'clay-auth-style';
    s.textContent =
      '.is-locked{ opacity:.4 !important; cursor:not-allowed !important; }' +
      '.clay-lock{ font-size:.85em; margin-left:5px; opacity:.85; vertical-align:baseline; }' +
      '.clay-admin-bar{ position:fixed; right:16px; bottom:16px; z-index:9999; display:flex; gap:8px; align-items:center;' +
        ' background:#0E0D0B; color:#FEFDFB; border:1px solid rgba(254,253,251,.18); border-radius:999px;' +
        ' padding:8px 14px 8px 12px; font-family:var(--font-mono, monospace); font-size:12px; letter-spacing:.04em;' +
        ' box-shadow:0 8px 26px rgba(0,0,0,.28); text-decoration:none; }' +
      '.clay-admin-bar .dot{ width:7px; height:7px; border-radius:999px; background:#cbd810; box-shadow:0 0 0 3px rgba(203,216,16,.22); }' +
      '.clay-admin-bar a{ color:#FEFDFB; text-decoration:none; border-bottom:1px solid rgba(254,253,251,.35); padding-bottom:1px; }' +
      '.clay-admin-bar a:hover{ border-bottom-color:#cbd810; }' +
      '.clay-admin-bar .sep{ opacity:.4; }';
    (document.head || document.documentElement).appendChild(s);
  }

  function injectAdminBar() {
    if (!Auth.isAdmin()) return;
    if (document.getElementById('clay-admin-bar')) return;
    var here = currentFile();
    var bar = document.createElement('div');
    bar.id = 'clay-admin-bar';
    bar.className = 'clay-admin-bar';
    var jump = (here === DASHBOARD)
      ? '<a href="home.html">← Back to portal</a>'
      : '<a href="' + DASHBOARD + '">Dashboard</a>';
    bar.innerHTML =
      '<span class="dot" aria-hidden="true"></span>' +
      '<span>ADMIN</span>' +
      '<span class="sep">·</span>' +
      jump +
      '<span class="sep">·</span>' +
      '<a href="#" id="clay-admin-exit">Exit</a>';
    document.body.appendChild(bar);
    var exit = document.getElementById('clay-admin-exit');
    if (exit) exit.addEventListener('click', function (e) {
      e.preventDefault();
      Auth.lock();
      window.location.href = 'home.html';
    });
  }

  function wireNav() {
    injectStyle();
    injectAdminBar();
    var unlocked = Auth.isUnlocked();
    var links = document.querySelectorAll('a[href]');
    Array.prototype.forEach.call(links, function (a) {
      var name = fileOf(a.getAttribute('href'));
      if (GATED.indexOf(name) === -1) return;

      if (unlocked) {
        a.classList.remove('is-locked');
        a.removeAttribute('aria-disabled');
        var old = a.querySelector('.clay-lock');
        if (old) old.remove();
        return;
      }

      a.classList.add('is-locked');
      a.setAttribute('aria-disabled', 'true');
      a.setAttribute('title', 'Enter your access code to unlock');
      if (!a.querySelector('.clay-lock')) {
        var i = document.createElement('i');
        i.className = 'ph-bold ph-lock-simple clay-lock';
        a.appendChild(i);
      }
      a.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        if (typeof window.ClayOpenAccess === 'function') window.ClayOpenAccess();
        else window.location.href = 'home.html';
      }, true);
    });
  }

  if (document.readyState !== 'loading') wireNav();
  else document.addEventListener('DOMContentLoaded', wireNav);

  // re-assert lock state if the tab regains focus (e.g. after logging in elsewhere)
  window.addEventListener('pageshow', wireNav);
})();
