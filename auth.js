/* ══════════════════════════════════════════════════════════════════
   auth.js — soft access gate for the Workshop portal

   - Tabs/links pointing at gated pages (For You, Pre-flight, Post-workshop)
     are locked until the visitor enters a valid access code on home.html.
   - Locked links show a padlock, are dimmed, and (on home) open the access
     modal instead of navigating.
   - Gated pages also carry an inline head-guard that bounces locked
     visitors back to home.html (see each page's <head>).

   State lives in localStorage under 'clay_ws_unlocked'. This is a SOFT gate
   (matches ACCESS-CODES.md threat model), not real auth.
   ══════════════════════════════════════════════════════════════════ */
(function () {
  var KEY = 'clay_ws_unlocked';
  var GATED = ['welcome.html', 'post-workshop.html'];

  var Auth = window.ClayAuth = {
    isUnlocked: function () {
      try { return localStorage.getItem(KEY) === '1'; } catch (e) { return false; }
    },
    unlock: function (code) {
      try {
        localStorage.setItem(KEY, '1');
        if (code) localStorage.setItem('clay_ws_code', String(code).toUpperCase());
      } catch (e) {}
    },
    lock: function () {
      try { localStorage.removeItem(KEY); } catch (e) {}
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

  function injectStyle() {
    if (document.getElementById('clay-auth-style')) return;
    var s = document.createElement('style');
    s.id = 'clay-auth-style';
    s.textContent =
      '.is-locked{ opacity:.4 !important; cursor:not-allowed !important; }' +
      '.clay-lock{ font-size:.85em; margin-left:5px; opacity:.85; vertical-align:baseline; }';
    (document.head || document.documentElement).appendChild(s);
  }

  function wireNav() {
    injectStyle();
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
