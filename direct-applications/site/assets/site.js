(function () {
  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });
  }

  // Dropdown menus
  var items = document.querySelectorAll(".nav-item");
  function closeAll(except) {
    items.forEach(function (it) {
      if (it === except) return;
      var b = it.querySelector("button");
      b.setAttribute("aria-expanded", "false");
      it.querySelector(".menu").hidden = true;
    });
  }
  items.forEach(function (it) {
    var b = it.querySelector("button");
    var m = it.querySelector(".menu");
    b.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = b.getAttribute("aria-expanded") !== "true";
      closeAll(it);
      b.setAttribute("aria-expanded", open ? "true" : "false");
      m.hidden = !open;
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav-item")) closeAll();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeAll();
  });

  // Work filters
  var grid = document.querySelector("[data-work-grid]");
  if (grid) {
    var state = { solution: "all", process: "all" };
    var empty = document.querySelector("[data-work-empty]");
    function apply() {
      var shown = 0;
      grid.querySelectorAll(".work-card").forEach(function (c) {
        var ok = (state.solution === "all" || c.dataset.solution === state.solution) &&
                 (state.process === "all" || (" " + c.dataset.process + " ").indexOf(" " + state.process + " ") > -1);
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (empty) empty.hidden = shown > 0;
    }
    document.querySelectorAll("[data-filter]").forEach(function (chip) {
      chip.addEventListener("click", function () {
        var group = chip.dataset.filter;
        state[group] = chip.dataset.value;
        document.querySelectorAll('[data-filter="' + group + '"]').forEach(function (c) {
          c.setAttribute("aria-pressed", c === chip ? "true" : "false");
        });
        apply();
      });
    });
    var h = (location.hash || "").slice(1);
    var pre = h && document.querySelector('[data-filter="solution"][data-value="' + h + '"]');
    if (pre) pre.click();
  }

  // File drop zones
  function fmt(n) {
    if (n > 1e9) return (n / 1e9).toFixed(1) + " GB";
    if (n > 1e6) return (n / 1e6).toFixed(1) + " MB";
    return Math.max(1, Math.round(n / 1e3)) + " KB";
  }
  document.querySelectorAll(".drop").forEach(function (drop) {
    var input = drop.querySelector("input[type=file]");
    var list = document.getElementById(drop.dataset.list);
    ["dragenter", "dragover"].forEach(function (ev) { drop.addEventListener(ev, function () { drop.classList.add("over"); }); });
    ["dragleave", "drop"].forEach(function (ev) { drop.addEventListener(ev, function () { drop.classList.remove("over"); }); });
    input.addEventListener("change", function () {
      list.innerHTML = "";
      Array.prototype.forEach.call(input.files, function (f) {
        var li = document.createElement("li");
        var a = document.createElement("span"); a.textContent = f.name;
        var b = document.createElement("span"); b.textContent = fmt(f.size);
        li.appendChild(a); li.appendChild(b); list.appendChild(li);
      });
    });
  });

  // Preselect solution on the quote form from #anchor (e.g. quote.html#custom-acrylic)
  var sol = document.getElementById("q-solution");
  if (sol) {
    var hh = (location.hash || "").slice(1);
    if (hh && sol.querySelector('option[value="' + hh + '"]')) sol.value = hh;
  }

  // Forms: no backend is connected yet. Validate, then show a confirmation in place.
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var err = form.querySelector(".form-error");
      if (!form.checkValidity()) {
        if (err) { err.hidden = false; err.textContent = "Fill in the fields marked with * and check the email address, then send again."; }
        var bad = form.querySelector(":invalid");
        if (bad) bad.focus();
        return;
      }
      if (err) err.hidden = true;
      var status = form.querySelector(".form-status");
      var nameEl = form.querySelector("[name=name]");
      var first = nameEl && nameEl.value ? nameEl.value.trim().split(" ")[0] : "";
      status.hidden = false;
      status.innerHTML = "<b>Thanks" + (first ? ", " + first.replace(/[<>&"]/g, "") : "") + ".</b> " + form.dataset.thanks +
        ' <span class="tbd">Form not connected yet</span>';
      status.scrollIntoView({ block: "center", behavior: "smooth" });
    });
  });

  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
