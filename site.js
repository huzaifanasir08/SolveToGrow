(function () {
  const searchInput = document.querySelector("[data-file-search]");
  const cards = Array.from(document.querySelectorAll("[data-search]"));
  const emptyState = document.querySelector("[data-empty-state]");
  const visibleCount = document.querySelector("[data-visible-count]");
  const toggles = Array.from(document.querySelectorAll("[data-expand-toggle]"));

  function updateFileList() {
    if (!searchInput || cards.length === 0) {
      return;
    }

    const query = searchInput.value.trim().toLowerCase();
    let visible = 0;

    cards.forEach((card) => {
      const isMatch = card.dataset.search.includes(query);
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

  toggles.forEach((toggle) => {
    const card = toggle.closest("[data-expand-card]");
    const panel = card ? card.querySelector("[data-expand-panel]") : null;

    if (!card || !panel) {
      return;
    }

    toggle.addEventListener("click", () => {
      const isOpen = card.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(isOpen));
      panel.setAttribute("aria-hidden", String(!isOpen));
    });
  });

  if (searchInput && cards.length > 0) {
    searchInput.addEventListener("input", updateFileList);
    updateFileList();
  }
})();
