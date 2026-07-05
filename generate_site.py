from pathlib import Path
from urllib.parse import quote
import html

ROOT = Path(__file__).resolve().parent
SHARED_FOLDER = "problems"

DEVELOPERS = [
    {
        "folder": "arham-dev",
        "name": "Arham",
        "initials": "AR",
        "focus": "Problem solving log",
        "accent": "#14b8a6",
        "soft": "#d8fbf4",
        "warm": "#ffedd5",
        "ring": "rgba(20, 184, 166, 0.2)",
    },
    {
        "folder": "huzaifa-dev",
        "name": "Huzaifa",
        "initials": "HZ",
        "focus": "Solution practice",
        "accent": "#3b82f6",
        "soft": "#dbeafe",
        "warm": "#fef3c7",
        "ring": "rgba(59, 130, 246, 0.2)",
    },
    {
        "folder": "ahmad-dev",
        "name": "Ahmad",
        "initials": "AH",
        "focus": "Code challenges",
        "accent": "#f97316",
        "soft": "#ffedd5",
        "warm": "#dcfce7",
        "ring": "rgba(249, 115, 22, 0.2)",
    },
]

DEVELOPER_FOLDERS = [developer["folder"] for developer in DEVELOPERS]
SUPPORTED_SUFFIXES = {
    ".c", ".cpp", ".cs", ".go", ".java", ".js", ".kt", ".md",
    ".php", ".py", ".rb", ".rs", ".swift", ".ts", ".txt",
}

LANGUAGE_BY_SUFFIX = {
    ".c": "C", ".cpp": "C++", ".cs": "C#", ".go": "Go",
    ".java": "Java", ".js": "JavaScript", ".kt": "Kotlin",
    ".md": "Markdown", ".php": "PHP", ".py": "Python",
    ".rb": "Ruby", ".rs": "Rust", ".swift": "Swift",
    ".ts": "TypeScript", ".txt": "Text",
}

SITE_CSS = """
:root {
  color-scheme: light;
  --ink: #071426;
  --muted: #5d6d84;
  --paper: rgba(255, 255, 255, 0.9);
  --paper-strong: #ffffff;
  --line: rgba(124, 144, 170, 0.28);
  --surface: #f4f8fb;
  --shadow: 0 24px 70px rgba(15, 23, 42, 0.15);
  --glow-teal: rgba(20, 184, 166, 0.34);
  --glow-blue: rgba(59, 130, 246, 0.2);
  --glow-warm: rgba(249, 115, 22, 0.22);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: Arial, Helvetica, sans-serif;
  background:
    linear-gradient(115deg, rgba(20, 184, 166, 0.12), transparent 34%),
    linear-gradient(245deg, rgba(59, 130, 246, 0.1), transparent 36%),
    linear-gradient(180deg, #fbfcff 0%, var(--surface) 48%, #f7f3f2 100%);
  color: var(--ink);
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(15, 23, 42, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(15, 23, 42, 0.04) 1px, transparent 1px);
  background-size: 38px 38px;
  mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.82), transparent 80%);
}

a {
  color: inherit;
}

.hero {
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--line);
  background:
    linear-gradient(135deg, rgba(255, 255, 255, 0.94), rgba(236, 253, 245, 0.76) 48%, rgba(255, 247, 237, 0.9)),
    #ffffff;
}

.hero::after {
  content: "";
  position: absolute;
  inset: auto 0 -1px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--glow-teal), var(--glow-warm), transparent);
  box-shadow: 0 0 24px var(--glow-teal);
}

.hero-inner,
.content,
.topbar {
  width: min(1120px, calc(100% - 40px));
  margin: 0 auto;
}

.hero-inner {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(320px, 0.92fr);
  gap: 42px;
  align-items: center;
  padding: 34px 0 32px;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 12px;
  color: var(--accent, #14b8a6);
  font-size: 0.86rem;
  font-weight: 800;
  letter-spacing: 0;
}

.eyebrow::before {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: currentColor;
  box-shadow: 0 0 18px currentColor;
}

h1,
h2,
h3,
p {
  overflow-wrap: anywhere;
}

h1 {
  margin: 0;
  max-width: 760px;
  font-size: 2.7rem;
  line-height: 1.07;
  letter-spacing: 0;
}

.hero-copy {
  min-width: 0;
}

.hero-copy > p:not(.eyebrow) {
  max-width: 650px;
  margin: 16px 0 0;
  color: var(--muted);
  font-size: 1.04rem;
  line-height: 1.7;
}

.stat-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 24px;
}

.stat {
  min-width: 132px;
  padding: 14px 15px;
  border: 1px solid rgba(255, 255, 255, 0.72);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.72);
  box-shadow: 0 14px 34px rgba(15, 23, 42, 0.09), inset 0 1px 0 rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(16px);
}

.stat strong {
  display: block;
  font-size: 1.5rem;
}

.stat span {
  display: block;
  margin-top: 3px;
  color: var(--muted);
  font-size: 0.9rem;
}

.code-board {
  position: relative;
  min-height: 250px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  border-radius: 8px;
  background: linear-gradient(145deg, #0e1728, #111827 52%, #07111f);
  box-shadow: 0 28px 70px rgba(15, 23, 42, 0.28), 0 0 38px rgba(20, 184, 166, 0.18);
  overflow: hidden;
}

.code-board::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(120deg, transparent 18%, rgba(255, 255, 255, 0.08), transparent 42%);
  transform: translateX(-55%);
  animation: board-sheen 6s ease-in-out infinite;
}

@keyframes board-sheen {
  0%, 55% { transform: translateX(-60%); }
  100% { transform: translateX(70%); }
}

.board-bar {
  display: flex;
  gap: 8px;
  padding: 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.board-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: var(--dot);
  box-shadow: 0 0 16px var(--dot);
}

.board-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  padding: 20px;
}

.code-lines {
  display: grid;
  gap: 10px;
}

.code-line {
  height: 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.16);
}

.code-line:nth-child(2) {
  width: 74%;
  background: rgba(45, 212, 191, 0.55);
  box-shadow: 0 0 18px rgba(45, 212, 191, 0.18);
}

.code-line:nth-child(3) {
  width: 88%;
}

.code-line:nth-child(4) {
  width: 62%;
  background: rgba(251, 146, 60, 0.54);
  box-shadow: 0 0 18px rgba(251, 146, 60, 0.16);
}

.visual-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 9px;
}

.visual-grid span {
  aspect-ratio: 1;
  border-radius: 8px;
  background: var(--tile);
  box-shadow: 0 14px 26px rgba(15, 23, 42, 0.16), 0 0 18px rgba(255, 255, 255, 0.08);
  opacity: 0.95;
}

.content {
  padding: 30px 0 64px;
}

.section-heading {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 18px;
}

.section-heading h2,
.file-section h2 {
  margin: 0;
  color: #071426;
}

.section-heading h2 {
  font-size: 1.5rem;
}

.section-heading p {
  margin: 6px 0 0;
  color: var(--muted);
}

.developer-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.developer-card,
.file-card {
  border: 1px solid rgba(255, 255, 255, 0.74);
  border-radius: 8px;
  background: var(--paper);
  box-shadow: 0 18px 46px rgba(15, 23, 42, 0.11), inset 0 1px 0 rgba(255, 255, 255, 0.82);
  backdrop-filter: blur(18px);
}

.developer-card {
  position: relative;
  display: flex;
  min-height: 240px;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  text-decoration: none;
  overflow: hidden;
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}

.developer-card::before,
.file-card::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.55), transparent 34%, var(--ring, rgba(20, 184, 166, 0.16)));
  opacity: 0.74;
}

.developer-card:hover {
  transform: translateY(-5px);
  border-color: var(--accent);
  box-shadow: var(--shadow), 0 0 34px var(--ring, rgba(20, 184, 166, 0.18));
}

.developer-card > * {
  position: relative;
}

.developer-top {
  display: flex;
  gap: 14px;
  align-items: center;
}

.avatar {
  display: grid;
  flex: 0 0 auto;
  width: 54px;
  height: 54px;
  place-items: center;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--soft), var(--warm));
  color: var(--accent);
  font-weight: 800;
  box-shadow: 0 0 28px var(--ring, rgba(20, 184, 166, 0.18));
}

.developer-name {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 800;
}

.developer-focus,
.latest,
.file-path,
.file-summary,
.meta-item {
  color: var(--muted);
}

.developer-focus {
  margin: 4px 0 0;
}

.latest {
  min-height: 44px;
  margin: 18px 0;
  line-height: 1.5;
}

.mini-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.mini-stat {
  padding: 12px;
  border: 1px solid rgba(255, 255, 255, 0.72);
  border-radius: 8px;
  background: rgba(248, 250, 252, 0.75);
}

.mini-stat strong {
  display: block;
  font-size: 1.25rem;
}

.mini-stat span {
  color: var(--muted);
  font-size: 0.85rem;
}

.card-action {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 18px;
  color: var(--accent);
  font-weight: 800;
}

.topbar {
  padding-top: 22px;
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--accent, #14b8a6);
  font-weight: 800;
  text-decoration: none;
}

.developer-hero .hero-inner {
  grid-template-columns: minmax(0, 1fr);
  padding-top: 24px;
}

.toolbar {
  display: grid;
  grid-template-columns: minmax(260px, 1fr) auto;
  gap: 14px;
  align-items: center;
  margin-bottom: 24px;
}

.search-box {
  display: block;
}

.search-box span {
  display: block;
  margin-bottom: 7px;
  color: var(--muted);
  font-size: 0.9rem;
  font-weight: 700;
}

.search-box input {
  width: 100%;
  min-height: 46px;
  border: 1px solid rgba(148, 163, 184, 0.34);
  border-radius: 8px;
  padding: 0 14px;
  background: rgba(255, 255, 255, 0.82);
  color: var(--ink);
  font: inherit;
  outline: none;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.07);
}

.search-box input:focus {
  border-color: var(--accent, #14b8a6);
  box-shadow: 0 0 0 4px var(--ring, rgba(20, 184, 166, 0.16)), 0 18px 44px rgba(15, 23, 42, 0.1);
}

.visible-count {
  align-self: end;
  margin: 0;
  color: var(--muted);
  font-weight: 700;
}

.file-section {
  margin-top: 26px;
}

.file-section h2 {
  margin-bottom: 14px;
  font-size: 1.28rem;
}

.file-grid {
  display: grid;
  gap: 14px;
}

.file-card {
  position: relative;
  overflow: hidden;
}

.file-card[open] {
  box-shadow: var(--shadow), 0 0 38px var(--ring, rgba(20, 184, 166, 0.18));
}

.file-card[open] .expand-mark {
  transform: rotate(45deg);
}

.file-card summary {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 16px;
  align-items: center;
  min-height: 92px;
  padding: 18px;
  cursor: pointer;
  list-style: none;
}

.file-card summary::-webkit-details-marker {
  display: none;
}

.file-card summary:focus-visible {
  outline: 3px solid var(--ring, rgba(20, 184, 166, 0.2));
  outline-offset: -4px;
}

.file-title {
  min-width: 0;
}

.file-title h3 {
  margin: 0 0 7px;
  font-size: 1.13rem;
  line-height: 1.2;
}

.file-summary {
  display: -webkit-box;
  margin: 0;
  overflow: hidden;
  line-height: 1.5;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.file-side {
  display: inline-flex;
  gap: 10px;
  align-items: center;
}

.type-badge {
  flex: 0 0 auto;
  border: 1px solid rgba(255, 255, 255, 0.78);
  border-radius: 999px;
  padding: 7px 11px;
  background: var(--soft, #d8fbf4);
  color: var(--accent, #14b8a6);
  font-size: 0.8rem;
  font-weight: 800;
  box-shadow: 0 0 20px var(--ring, rgba(20, 184, 166, 0.16));
}

.expand-mark {
  display: grid;
  width: 32px;
  height: 32px;
  place-items: center;
  border: 1px solid rgba(148, 163, 184, 0.3);
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.72);
  color: var(--accent, #14b8a6);
  font-size: 1.35rem;
  line-height: 1;
  transition: transform 0.18s ease;
}

.file-detail {
  position: relative;
  padding: 0 18px 18px;
}

.file-path {
  margin: 0 0 10px;
  font-size: 0.86rem;
}

pre {
  max-height: 430px;
  margin: 0;
  overflow: auto;
  border: 1px solid rgba(148, 163, 184, 0.24);
  border-radius: 8px;
  background: #0f172a;
  color: #e2e8f0;
  padding: 16px;
  line-height: 1.55;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
}

code {
  font-family: Consolas, "Courier New", monospace;
  font-size: 0.92rem;
}

.file-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-top: 14px;
}

.meta-item,
.file-link {
  border-radius: 999px;
  padding: 7px 10px;
  background: rgba(244, 247, 251, 0.82);
  font-size: 0.86rem;
  font-weight: 700;
}

.file-link {
  margin-left: auto;
  background: var(--soft, #d8fbf4);
  color: var(--accent, #14b8a6);
  text-decoration: none;
  box-shadow: 0 0 20px var(--ring, rgba(20, 184, 166, 0.16));
}

.empty-state {
  margin: 0;
  border: 1px dashed rgba(148, 163, 184, 0.42);
  border-radius: 8px;
  padding: 18px;
  background: rgba(255, 255, 255, 0.72);
  color: var(--muted);
}

[hidden] {
  display: none !important;
}

@media (max-width: 860px) {
  .hero-inner {
    grid-template-columns: 1fr;
  }

  .developer-grid {
    grid-template-columns: 1fr;
  }

  .toolbar {
    grid-template-columns: 1fr;
  }

  .visible-count {
    align-self: start;
  }
}

@media (max-width: 560px) {
  .hero-inner,
  .content,
  .topbar {
    width: min(100% - 28px, 1120px);
  }

  h1 {
    font-size: 2rem;
  }

  .board-body {
    grid-template-columns: 1fr;
  }

  .section-heading {
    align-items: start;
    flex-direction: column;
  }

  .file-card summary {
    grid-template-columns: 1fr;
  }

  .file-side {
    justify-content: space-between;
    width: 100%;
  }

  .file-meta {
    align-items: start;
    flex-direction: column;
  }

  .file-link {
    margin-left: 0;
  }
}
/* Modern glow theme overrides (dark is opt-in via [data-theme="dark"]) */
[data-theme="dark"] {
  color-scheme: dark;
  --ink: #eaf2ff;
  --muted: #9fb0ca;
  --paper: rgba(15, 23, 42, 0.74);
  --line: rgba(148, 163, 184, 0.22);
  --surface: #07111f;
  --shadow: 0 28px 80px rgba(0, 0, 0, 0.38);
  --glow-teal: rgba(20, 184, 166, 0.42);
  --glow-blue: rgba(59, 130, 246, 0.3);
  --glow-warm: rgba(249, 115, 22, 0.26);
}

[data-theme="dark"] body {
  background:
    radial-gradient(circle at 12% 12%, rgba(20, 184, 166, 0.34), transparent 28%),
    radial-gradient(circle at 86% 10%, rgba(59, 130, 246, 0.28), transparent 32%),
    radial-gradient(circle at 72% 88%, rgba(249, 115, 22, 0.2), transparent 34%),
    linear-gradient(135deg, #050914 0%, #07111f 42%, #111827 100%);
}

[data-theme="dark"] body::before {
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.045) 1px, transparent 1px);
}

[data-theme="dark"] .hero {
  background:
    linear-gradient(135deg, rgba(15, 23, 42, 0.88), rgba(17, 94, 89, 0.62) 48%, rgba(88, 28, 8, 0.42)),
    rgba(7, 17, 31, 0.94);
}

.section-heading h2,
.file-section h2 {
  color: var(--ink);
}

[data-theme="dark"] .stat,
[data-theme="dark"] .mini-stat,
[data-theme="dark"] .search-box input,
[data-theme="dark"] .empty-state,
[data-theme="dark"] .meta-item {
  border-color: rgba(255, 255, 255, 0.14);
  background: rgba(15, 23, 42, 0.68);
  box-shadow: 0 16px 38px rgba(0, 0, 0, 0.24), inset 0 1px 0 rgba(255, 255, 255, 0.12);
}

[data-theme="dark"] .developer-card,
[data-theme="dark"] .file-card {
  border-color: rgba(255, 255, 255, 0.14);
  background: rgba(15, 23, 42, 0.74);
  box-shadow: 0 22px 58px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.12);
}

[data-theme="dark"] .developer-card::before,
[data-theme="dark"] .file-card::before {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.12), transparent 34%, var(--ring, rgba(20, 184, 166, 0.16)));
  opacity: 0.88;
}

.file-card {
  transition: border-color 0.22s ease, box-shadow 0.22s ease, transform 0.22s ease;
}

.file-card.is-open {
  border-color: var(--accent, #14b8a6);
  box-shadow: var(--shadow), 0 0 42px var(--ring, rgba(20, 184, 166, 0.18));
}

.file-card.is-open .expand-mark {
  transform: rotate(45deg);
}

.file-toggle {
  position: relative;
  display: grid;
  width: 100%;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 16px;
  align-items: center;
  min-height: 92px;
  border: 0;
  padding: 18px;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font: inherit;
  text-align: left;
}

.file-toggle:focus-visible {
  outline: 3px solid var(--ring, rgba(20, 184, 166, 0.2));
  outline-offset: -4px;
}

.file-heading {
  display: block;
  margin: 0 0 7px;
  color: var(--ink);
  font-size: 1.13rem;
  font-weight: 800;
  line-height: 1.2;
}

.expand-mark {
  transition: transform 0.24s ease, border-color 0.24s ease, background 0.24s ease;
}

[data-theme="dark"] .expand-mark {
  background: rgba(15, 23, 42, 0.72);
}

.file-toggle,
.file-detail-shell {
  position: relative;
}

.file-detail-shell {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  overflow: hidden;
  visibility: hidden;
  transition: grid-template-rows 0.36s ease, opacity 0.24s ease, visibility 0s linear 0.36s;
}

.file-card.is-open .file-detail-shell {
  grid-template-rows: 1fr;
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

.file-detail {
  min-height: 0;
  overflow: hidden;
  padding: 0;
}

.file-detail-inner {
  padding: 0 18px 18px;
}

@media (max-width: 560px) {
  .file-toggle {
    grid-template-columns: 1fr;
  }
}

/* --- Interactive UI additions --- */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.ghost-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 8px 14px;
  background: var(--paper);
  color: var(--ink);
  font: inherit;
  font-weight: 700;
  font-size: 0.86rem;
  cursor: pointer;
  transition: border-color 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
}

.ghost-btn:hover {
  border-color: var(--accent, #14b8a6);
  transform: translateY(-1px);
  box-shadow: 0 0 22px var(--ring, rgba(20, 184, 166, 0.16));
}

.ghost-btn:focus-visible {
  outline: 3px solid var(--ring, rgba(20, 184, 166, 0.24));
  outline-offset: 2px;
}

.theme-toggle .theme-icon {
  font-size: 1rem;
  line-height: 1;
}

/* Show sun in dark mode (click for light), moon in light mode */
.theme-toggle .icon-dark { display: inline; }
.theme-toggle .icon-light { display: none; }
[data-theme="dark"] .theme-toggle .icon-dark { display: none; }
[data-theme="dark"] .theme-toggle .icon-light { display: inline; }

.toolbar-actions {
  display: inline-flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: end;
}

.filter-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0 0 18px;
}

.chip {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 6px 13px;
  background: var(--paper);
  color: var(--muted);
  font: inherit;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: border-color 0.16s ease, color 0.16s ease, background 0.16s ease;
}

.chip:hover {
  border-color: var(--accent, #14b8a6);
  color: var(--ink);
}

.chip.is-active {
  border-color: var(--accent, #14b8a6);
  background: var(--soft, #d8fbf4);
  color: var(--accent, #14b8a6);
  box-shadow: 0 0 18px var(--ring, rgba(20, 184, 166, 0.18));
}

.chip:focus-visible {
  outline: 3px solid var(--ring, rgba(20, 184, 166, 0.24));
  outline-offset: 2px;
}

.code-wrap {
  position: relative;
}

.copy-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 2;
  border: 1px solid rgba(148, 163, 184, 0.34);
  border-radius: 7px;
  padding: 6px 11px;
  background: rgba(15, 23, 42, 0.82);
  color: #e2e8f0;
  font: inherit;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.code-wrap:hover .copy-btn,
.copy-btn:focus-visible {
  opacity: 1;
}

.copy-btn:hover {
  border-color: var(--accent, #14b8a6);
}

.copy-btn.is-copied {
  border-color: #22c55e;
  color: #bbf7d0;
}

.copy-btn:focus-visible {
  outline: 3px solid var(--ring, rgba(20, 184, 166, 0.28));
  outline-offset: 2px;
}

.owner-tag {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 4px 10px;
  background: var(--soft, #d8fbf4);
  color: var(--accent, #14b8a6);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.file-heading-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  margin-bottom: 7px;
}

.file-heading-row .file-heading {
  margin: 0;
}

@media (max-width: 560px) {
  .topbar {
    flex-wrap: wrap;
  }

  .copy-btn {
    opacity: 1;
  }
}
"""

THEME_INIT_JS = """
(function () {
  try {
    var stored = localStorage.getItem("stg-theme");
    var theme = stored || (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    document.documentElement.setAttribute("data-theme", theme);
  } catch (e) {
    document.documentElement.setAttribute("data-theme", "dark");
  }
})();
"""

SITE_JS = """
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
"""

def is_supported_problem_file(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_SUFFIXES or path.suffix == ""


def get_problem_files(folder_name: str):
    folder = ROOT / folder_name
    if not folder.exists():
        return []

    files = [
        path
        for path in folder.rglob("*")
        if path.is_file()
        and is_supported_problem_file(path)
        and not any(part.startswith(".") for part in path.relative_to(folder).parts)
    ]
    return sorted(files, key=lambda path: path.relative_to(folder).as_posix().lower())


def read_problem_content(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return "No content available."


def get_line_count(content: str) -> int:
    return len(content.splitlines()) or 1


def format_file_size(path: Path) -> str:
    try:
        size = path.stat().st_size
    except OSError:
        return "Unknown size"

    if size < 1024:
        return f"{size} B"
    return f"{size / 1024:.1f} KB"


def get_language(path: Path) -> str:
    return LANGUAGE_BY_SUFFIX.get(path.suffix.lower(), "File")


def get_type_label(path: Path) -> str:
    if path.suffix:
        return path.suffix[1:].upper()
    return "FILE"


def get_preview_line(content: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped:
            if len(stripped) > 160:
                return stripped[:157].rstrip() + "..."
            return stripped
    return "No preview available yet."


def get_code_excerpt(content: str, max_lines: int = 80, max_chars: int = 12000) -> str:
    lines = content.splitlines() or ["No content available."]
    excerpt = "\n".join(lines[:max_lines])

    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars].rstrip() + "\n..."
    elif len(lines) > max_lines:
        excerpt += f"\n... {len(lines) - max_lines} more line(s)"

    return excerpt


def html_attr(value: str) -> str:
    return html.escape(" ".join(value.split()).lower(), quote=True)


def page_url(path: Path) -> str:
    return quote(path.relative_to(ROOT).as_posix())


def total_lines(files) -> int:
    return sum(get_line_count(read_problem_content(path)) for path in files)


def latest_text(files) -> str:
    if not files:
        return "Ready for the first solution."

    try:
        latest = max(files, key=lambda path: path.stat().st_mtime)
    except OSError:
        latest = files[-1]

    return f"Latest file: {latest.name}"


def write_static_assets():
    (ROOT / "styles.css").write_text(SITE_CSS.strip() + "\n", encoding="utf-8")
    (ROOT / "site.js").write_text(SITE_JS.strip() + "\n", encoding="utf-8")


def render_stat(value: int, label: str) -> str:
    return f"""
      <div class="stat">
        <strong>{value}</strong>
        <span>{html.escape(label)}</span>
      </div>
    """


def render_code_board() -> str:
    return """
      <div class="code-board" aria-hidden="true">
        <div class="board-bar">
          <span class="board-dot" style="--dot: #fb7185"></span>
          <span class="board-dot" style="--dot: #facc15"></span>
          <span class="board-dot" style="--dot: #34d399"></span>
        </div>
        <div class="board-body">
          <div class="code-lines">
            <span class="code-line"></span>
            <span class="code-line"></span>
            <span class="code-line"></span>
            <span class="code-line"></span>
            <span class="code-line"></span>
            <span class="code-line"></span>
          </div>
          <div class="visual-grid">
            <span style="--tile: #14b8a6"></span>
            <span style="--tile: #f97316"></span>
            <span style="--tile: #60a5fa"></span>
            <span style="--tile: #facc15"></span>
            <span style="--tile: #22c55e"></span>
            <span style="--tile: #fb7185"></span>
            <span style="--tile: #38bdf8"></span>
            <span style="--tile: #a3e635"></span>
            <span style="--tile: #fdba74"></span>
          </div>
        </div>
      </div>
    """


def render_theme_toggle() -> str:
    return """
      <button class="ghost-btn theme-toggle" type="button" data-theme-toggle aria-pressed="false" aria-label="Toggle theme">
        <span class="theme-icon" aria-hidden="true"><span class="icon-dark">&#9790;</span><span class="icon-light">&#9728;</span></span>
        <span>Theme</span>
      </button>
    """


def render_language_chips(files) -> str:
    languages = sorted({get_language(path) for path in files})
    if not languages:
        return ""

    chips = ['<button class="chip is-active" type="button" data-lang-filter="all" aria-pressed="true">All</button>']
    for language in languages:
        chips.append(
            f'<button class="chip" type="button" data-lang-filter="{html_attr(language)}" aria-pressed="false">{html.escape(language)}</button>'
        )

    return f'<div class="filter-chips" role="group" aria-label="Filter by language">{"".join(chips)}</div>'


def render_developer_card(developer) -> str:
    files = get_problem_files(developer["folder"])
    line_count = total_lines(files)
    label = f"{developer['name']} Dev"

    return f"""
      <a class="developer-card" href="{developer['folder']}.html" style="--accent: {developer['accent']}; --soft: {developer['soft']}; --warm: {developer['warm']}; --ring: {developer['ring']};">
        <div>
          <div class="developer-top">
            <div class="avatar">{html.escape(developer['initials'])}</div>
            <div>
              <p class="developer-name">{html.escape(label)}</p>
              <p class="developer-focus">{html.escape(developer['focus'])}</p>
            </div>
          </div>
          <p class="latest">{html.escape(latest_text(files))}</p>
          <div class="mini-stats">
            <div class="mini-stat">
              <strong>{len(files)}</strong>
              <span>Files</span>
            </div>
            <div class="mini-stat">
              <strong>{line_count}</strong>
              <span>Lines</span>
            </div>
          </div>
        </div>
        <span class="card-action">Open workspace <span aria-hidden="true">&rarr;</span></span>
      </a>
    """


def render_file_card(path: Path, developer, owner_label: str = "") -> str:
    content = read_problem_content(path)
    relative_path = path.relative_to(ROOT).as_posix()
    preview = get_preview_line(content)
    language = get_language(path)
    search_blob = f"{path.name} {relative_path} {language} {owner_label} {content[:1800]}"

    owner_tag = (
        f'<span class="owner-tag">{html.escape(owner_label)}</span>' if owner_label else ""
    )

    return f"""
      <article class="file-card" data-expand-card data-search="{html_attr(search_blob)}" data-lang="{html_attr(language)}" style="--accent: {developer['accent']}; --soft: {developer['soft']}; --ring: {developer['ring']};">
        <button class="file-toggle" type="button" aria-expanded="false" data-expand-toggle>
          <span class="file-title">
            <span class="file-heading-row">
              <span class="file-heading">{html.escape(path.name)}</span>
              {owner_tag}
            </span>
            <span class="file-summary">{html.escape(preview)}</span>
          </span>
          <span class="file-side">
            <span class="type-badge">{html.escape(get_type_label(path))}</span>
            <span class="expand-mark" aria-hidden="true">+</span>
          </span>
        </button>
        <div class="file-detail-shell" data-expand-panel aria-hidden="true">
          <div class="file-detail">
            <div class="file-detail-inner">
              <p class="file-path">{html.escape(relative_path)}</p>
              <div class="code-wrap">
                <button class="copy-btn" type="button" data-copy data-label="Copy">Copy</button>
                <pre><code>{html.escape(get_code_excerpt(content))}</code></pre>
              </div>
              <div class="file-meta">
                <span class="meta-item">{html.escape(language)}</span>
                <span class="meta-item">{get_line_count(content)} lines</span>
                <span class="meta-item">{html.escape(format_file_size(path))}</span>
                <a class="file-link" href="{page_url(path)}">Open raw file</a>
              </div>
            </div>
          </div>
        </div>
      </article>
    """

def render_file_section(title: str, files, empty_message: str, developer) -> str:
    if files:
        file_cards = "\n".join(render_file_card(path, developer) for path in files)
    else:
        file_cards = f'<p class="empty-state">{html.escape(empty_message)}</p>'

    return f"""
      <section class="file-section">
        <h2>{html.escape(title)}</h2>
        <div class="file-grid">
          {file_cards}
        </div>
      </section>
    """


SHARED_STYLE = {
    "accent": "#8b5cf6",
    "soft": "#ede9fe",
    "warm": "#e0e7ff",
    "ring": "rgba(139, 92, 246, 0.2)",
}


def collect_all_files():
    """Return (path, style, owner_label) for every developer + shared file."""
    entries = []
    for developer in DEVELOPERS:
        label = f"{developer['name']} Dev"
        for path in get_problem_files(developer["folder"]):
            entries.append((path, developer, label))
    for path in get_problem_files(SHARED_FOLDER):
        entries.append((path, SHARED_STYLE, "Shared"))
    return entries


def build_index_page():
    developer_cards = "\n".join(render_developer_card(developer) for developer in DEVELOPERS)
    developer_files = [path for folder in DEVELOPER_FOLDERS for path in get_problem_files(folder)]
    shared_files = get_problem_files(SHARED_FOLDER)
    all_entries = collect_all_files()
    all_files = [entry[0] for entry in all_entries]

    if all_entries:
        file_cards = "\n".join(
            render_file_card(path, style, owner_label) for path, style, owner_label in all_entries
        )
        library = f"""
    <section class="file-section" aria-label="All problem files">
      <div class="section-heading">
        <div>
          <h2>Problem Library</h2>
          <p>Search and filter every solution across the team.</p>
        </div>
        <div class="toolbar-actions">
          <button class="ghost-btn" type="button" data-expand-all>Expand all</button>
          <button class="ghost-btn" type="button" data-collapse-all>Collapse all</button>
        </div>
      </div>
      <section class="toolbar">
        <label class="search-box">
          <span>Search files</span>
          <input type="search" placeholder="Name, owner, language, or code text" data-file-search />
        </label>
        <p class="visible-count" data-visible-count>{len(all_entries)} files shown</p>
      </section>
      {render_language_chips(all_files)}
      <p class="empty-state" data-empty-state hidden>No matching files found.</p>
      <div class="file-grid">
        {file_cards}
      </div>
    </section>
        """
    else:
        library = ""

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SolveToGrow Developers</title>
  <script>{THEME_INIT_JS.strip()}</script>
  <link rel="stylesheet" href="styles.css" />
  <script src="site.js" defer></script>
</head>
<body>
  <header class="hero" style="--accent: #14b8a6;">
    <nav class="topbar">
      <p class="eyebrow">SolveToGrow</p>
      {render_theme_toggle()}
    </nav>
    <div class="hero-inner">
      <div class="hero-copy">
        <h1>Three developers growing through consistent problem solving.</h1>
        <p>A clean archive for daily practice, personal solutions, and shared challenges.</p>
        <div class="stat-row">
          {render_stat(len(DEVELOPERS), "Developers")}
          {render_stat(len(all_files), "Problem files")}
          {render_stat(total_lines(all_files), "Lines saved")}
          {render_stat(len(shared_files), "Shared files")}
        </div>
      </div>
      {render_code_board()}
    </div>
  </header>

  <main class="content">
    <div class="section-heading">
      <div>
        <h2>Developer Workspaces</h2>
        <p>Each workspace highlights solution files, previews, and file stats.</p>
      </div>
    </div>
    <section class="developer-grid" aria-label="Developer workspaces">
      {developer_cards}
    </section>
    {library}
  </main>
</body>
</html>
"""
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")


def build_developer_page(developer):
    folder_name = developer["folder"]
    label = f"{developer['name']} Dev"
    files = get_problem_files(folder_name)
    shared_files = get_problem_files(SHARED_FOLDER)
    all_visible_files = files + shared_files

    toolbar = ""
    if all_visible_files:
        toolbar = f"""
      <section class="toolbar">
        <label class="search-box">
          <span>Search files</span>
          <input type="search" placeholder="Name, language, or code text" data-file-search />
        </label>
        <div class="toolbar-actions">
          <button class="ghost-btn" type="button" data-expand-all>Expand all</button>
          <button class="ghost-btn" type="button" data-collapse-all>Collapse all</button>
          <p class="visible-count" data-visible-count>{len(all_visible_files)} files shown</p>
        </div>
      </section>
      {render_language_chips(all_visible_files)}
      <p class="empty-state" data-empty-state hidden>No matching files found.</p>
        """

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(label)} Problems</title>
  <script>{THEME_INIT_JS.strip()}</script>
  <link rel="stylesheet" href="styles.css" />
  <script src="site.js" defer></script>
</head>
<body>
  <header class="hero developer-hero" style="--accent: {developer['accent']}; --soft: {developer['soft']}; --warm: {developer['warm']}; --ring: {developer['ring']};">
    <nav class="topbar">
      <a class="back-link" href="index.html"><span aria-hidden="true">&larr;</span> Team overview</a>
      {render_theme_toggle()}
    </nav>
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">{html.escape(developer['focus'])}</p>
        <h1>{html.escape(label)} problem archive.</h1>
        <p>Click a file card to expand the solution preview only when you need it.</p>
        <div class="stat-row">
          {render_stat(len(files), "Developer files")}
          {render_stat(total_lines(files), "Developer lines")}
          {render_stat(len(shared_files), "Shared files")}
        </div>
      </div>
    </div>
  </header>

  <main class="content" style="--accent: {developer['accent']}; --soft: {developer['soft']}; --ring: {developer['ring']};">
    {toolbar}
    {render_file_section("Developer Files", files, "No problem files found in this workspace yet.", developer)}
    {render_file_section("Shared Problems", shared_files, "No shared problems found yet.", developer)}
  </main>
</body>
</html>
"""
    (ROOT / f"{folder_name}.html").write_text(page_html, encoding="utf-8")


if __name__ == "__main__":
    write_static_assets()
    build_index_page()
    for developer_config in DEVELOPERS:
        build_developer_page(developer_config)
    print("HTML pages generated successfully.")
