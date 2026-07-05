(function () {
  const root = document.documentElement;

  // --- Theme toggle ---------------------------------------------------------
  const themeToggle = document.querySelector("[data-theme-toggle]");
  if (themeToggle) {
    const applyLabel = () => {
      const isDark = root.getAttribute("data-theme") === "dark";
      themeToggle.setAttribute("aria-pressed", String(isDark));
      themeToggle.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
    };
    applyLabel();
    themeToggle.addEventListener("click", () => {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("stg-theme", next); } catch (e) {}
      applyLabel();
    });
  }

  // --- Copy code buttons ----------------------------------------------------
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    const wrap = btn.closest(".code-wrap");
    const code = wrap ? wrap.querySelector("code") : null;
    if (!code) {
      return;
    }
    btn.addEventListener("click", async () => {
      const text = code.innerText;
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          await navigator.clipboard.writeText(text);
        } else {
          const ta = document.createElement("textarea");
          ta.value = text;
          ta.style.position = "fixed";
          ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.select();
          document.execCommand("copy");
          document.body.removeChild(ta);
        }
        const original = btn.dataset.label || "Copy";
        btn.textContent = "Copied!";
        btn.classList.add("is-copied");
        window.setTimeout(() => {
          btn.textContent = original;
          btn.classList.remove("is-copied");
        }, 1400);
      } catch (e) {
        btn.textContent = "Copy failed";
        window.setTimeout(() => { btn.textContent = btn.dataset.label || "Copy"; }, 1400);
      }
    });
  });

  // --- Expand / collapse cards ---------------------------------------------
  const cardsAll = Array.from(document.querySelectorAll("[data-expand-card]"));

  function setCardOpen(card, open) {
    const toggle = card.querySelector("[data-expand-toggle]");
    const panel = card.querySelector("[data-expand-panel]");
    card.classList.toggle("is-open", open);
    if (toggle) toggle.setAttribute("aria-expanded", String(open));
    if (panel) panel.setAttribute("aria-hidden", String(!open));
  }

  cardsAll.forEach((card) => {
    const toggle = card.querySelector("[data-expand-toggle]");
    const panel = card.querySelector("[data-expand-panel]");
    if (!toggle || !panel) {
      return;
    }
    toggle.addEventListener("click", () => {
      setCardOpen(card, !card.classList.contains("is-open"));
    });
  });

  const expandAll = document.querySelector("[data-expand-all]");
  const collapseAll = document.querySelector("[data-collapse-all]");
  if (expandAll) {
    expandAll.addEventListener("click", () => {
      cardsAll.forEach((card) => { if (!card.hidden) setCardOpen(card, true); });
    });
  }
  if (collapseAll) {
    collapseAll.addEventListener("click", () => {
      cardsAll.forEach((card) => setCardOpen(card, false));
    });
  }

  // --- Search + language filter --------------------------------------------
  const searchInput = document.querySelector("[data-file-search]");
  const cards = Array.from(document.querySelectorAll("[data-search]"));
  const emptyState = document.querySelector("[data-empty-state]");
  const visibleCount = document.querySelector("[data-visible-count]");
  const chips = Array.from(document.querySelectorAll("[data-lang-filter]"));
  let activeLang = "all";

  function updateFileList() {
    if (cards.length === 0) {
      return;
    }
    const query = (searchInput ? searchInput.value : "").trim().toLowerCase();
    let visible = 0;

    cards.forEach((card) => {
      const matchesText = card.dataset.search.includes(query);
      const matchesLang = activeLang === "all" || card.dataset.lang === activeLang;
      const isMatch = matchesText && matchesLang;
      card.hidden = !isMatch;
      if (isMatch) {
        visible += 1;
      }
    });

    if (emptyState) {
      emptyState.hidden = visible !== 0;
    }
    if (visibleCount) {
      visibleCount.textContent = `${visible} file${visible === 1 ? "" : "s"} shown`;
    }
  }

  chips.forEach((chip) => {
    chip.addEventListener("click", () => {
      activeLang = chip.dataset.langFilter;
      chips.forEach((c) => {
        const on = c === chip;
        c.classList.toggle("is-active", on);
        c.setAttribute("aria-pressed", String(on));
      });
      updateFileList();
    });
  });

  if (searchInput) {
    searchInput.addEventListener("input", updateFileList);
  }
  if ((searchInput || chips.length > 0) && cards.length > 0) {
    updateFileList();
  }
})();
