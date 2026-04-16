// Folio Assistant — Single-Page Application
// Fetches paper data from /api/* and renders a reading/QC interface.

(function () {
  "use strict";

  const $ = (s, p) => (p || document).querySelector(s);
  const $$ = (s, p) => [...(p || document).querySelectorAll(s)];
  const h = (tag, cls, html) => {
    const el = document.createElement(tag);
    if (cls) el.className = cls;
    if (html != null) el.innerHTML = html;
    return el;
  };

  // ── State ───────────────────────────────────────────────
  let folio = null;       // FolioEntry[]
  let paper = null;       // ResolvedPaper
  let mode = "read";      // "read" | "qc" | "diff"
  let blockIndex = {};    // label → ResolvedBlock (for cross-ref lookup)
  let currentUser = null; // { email, name, provider, role } or null
  let currentBranch = null;   // HEAD branch on server
  let selectedBranch = null;  // branch the user is viewing (null = current)
  let diffData = null;        // PaperDiff from /api/diff
  let diffAbort = null;       // AbortController for diff fetch

  const app = $("#app");
  const navLinks = $("#nav-links");
  const branchSelect = $("#c-br");
  const diffBtn = $("#c-diff");

  // ── Progressive rendering helpers ────────────────────────
  // Double-rAF guarantees the previous frame has painted before we continue.
  const yieldPaint = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  // Humanize a slug like "quantum-observable-universe" → "Quantum Observable Universe".
  function prettifyPaperId(id) {
    return String(id || "").split(/[-_]+/).map(w => w ? w[0].toUpperCase() + w.slice(1) : "").join(" ");
  }

  // ── Auth: fetch current user ──────────────────────────────
  async function fetchUser() {
    try {
      const r = await fetch("/auth/me");
      if (r.ok) {
        currentUser = await r.json();
      } else {
        currentUser = null;
      }
    } catch {
      // Local dev — no auth gateway, treat as owner
      currentUser = { email: "local", name: "Local Dev", provider: "github", role: "owner" };
    }
  }

  function userCan(minRole) {
    const levels = { viewer: 1, collaborator: 2, owner: 3 };
    if (!currentUser) return false;
    return (levels[currentUser.role] || 0) >= (levels[minRole] || 99);
  }

  // ── Theme / font / sidebar / wide toggles ────────────────
  $("#c-th").onclick = () => {
    const t = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = t;
    $("#c-th").textContent = t === "dark" ? "light" : "dark";
    localStorage.setItem("folio-theme", t);
  };
  $("#c-fn").onclick = () => {
    const f = document.body.dataset.font === "paper" ? "web" : "paper";
    document.body.dataset.font = f;
    $("#c-fn").textContent = f === "paper" ? "web" : "paper";
    localStorage.setItem("folio-font", f);
  };
  $("#c-sb").onclick = () => {
    document.body.classList.toggle("sb-hidden");
    localStorage.setItem("folio-sb", document.body.classList.contains("sb-hidden") ? "hidden" : "visible");
  };
  $("#c-wd").onclick = () => {
    document.body.classList.toggle("wide-mode");
    localStorage.setItem("folio-wide", document.body.classList.contains("wide-mode") ? "wide" : "normal");
  };
  // restore saved prefs
  const savedTheme = localStorage.getItem("folio-theme");
  if (savedTheme) {
    document.documentElement.dataset.theme = savedTheme;
    $("#c-th").textContent = savedTheme === "dark" ? "light" : "dark";
  }
  const savedFont = localStorage.getItem("folio-font");
  if (savedFont) {
    document.body.dataset.font = savedFont;
    $("#c-fn").textContent = savedFont === "paper" ? "web" : "paper";
  }
  if (localStorage.getItem("folio-sb") === "hidden") document.body.classList.add("sb-hidden");
  if (localStorage.getItem("folio-wide") === "wide") document.body.classList.add("wide-mode");

  // ── Branch switcher ─────────────────────────────────────
  async function loadBranches() {
    try {
      const data = await api("/api/branches");
      currentBranch = data.current;
      if (!selectedBranch) selectedBranch = currentBranch;
      branchSelect.innerHTML = "";
      for (const b of data.branches) {
        const opt = document.createElement("option");
        opt.value = b;
        opt.textContent = (b === data.current ? "\u25CF " : "  ") + b;
        if (b === selectedBranch) opt.selected = true;
        branchSelect.appendChild(opt);
      }
      updateDiffBtn();
    } catch { /* ignore if /api/branches not available */ }
  }

  branchSelect.onchange = () => {
    selectedBranch = branchSelect.value;
    updateDiffBtn();
    updateReadOnlyBanner();
    route(); // re-fetch with new branch
  };

  function updateDiffBtn() {
    const show = selectedBranch && selectedBranch !== "main" && selectedBranch !== "master";
    diffBtn.style.display = show ? "" : "none";
  }

  diffBtn.onclick = async () => {
    if (mode === "diff") {
      mode = "read";
      if (paper) renderPaper();
      return;
    }
    if (!paper) return;
    mode = "diff";
    await loadDiff();
  };

  function branchParam() {
    if (!selectedBranch || selectedBranch === currentBranch) return "";
    return `&branch=${encodeURIComponent(selectedBranch)}`;
  }

  function branchQuery(base) {
    const sep = base.includes("?") ? "&" : "?";
    if (!selectedBranch || selectedBranch === currentBranch) return base;
    return base + sep + `branch=${encodeURIComponent(selectedBranch)}`;
  }

  // ── Read-only banner ──────────────────────────────────────
  function updateReadOnlyBanner() {
    let banner = $("#readonly-banner");
    if (selectedBranch && selectedBranch !== currentBranch) {
      if (!banner) {
        banner = h("div", "readonly-banner");
        banner.id = "readonly-banner";
        document.body.insertBefore(banner, app);
      }
      banner.innerHTML = `Viewing <strong>${esc(selectedBranch)}</strong> (read-only)`;
      banner.style.display = "";
    } else if (banner) {
      banner.style.display = "none";
    }
  }

  // ── Branch polling (detect branch changes) ────────────────
  let pollTimer = null;
  function startBranchPolling() {
    if (pollTimer) return;
    pollTimer = setInterval(async () => {
      try {
        const data = await api("/api/branch");
        if (data.branch !== currentBranch) {
          const oldBranch = currentBranch;
          currentBranch = data.branch;
          await loadBranches();
          // Auto-refresh if viewing the old current branch
          if (selectedBranch === oldBranch) {
            selectedBranch = currentBranch;
            showToast(`Branch changed to ${currentBranch}`);
            route();
          }
        }
      } catch {}
    }, 5000);
  }

  function showToast(msg) {
    const t = h("div", "toast", esc(msg));
    document.body.appendChild(t);
    requestAnimationFrame(() => t.classList.add("show"));
    setTimeout(() => {
      t.classList.remove("show");
      setTimeout(() => t.remove(), 300);
    }, 3000);
  }

  // ── Router ──────────────────────────────────────────────
  const LABEL_RE = /^(def|thm|lem|prop|cor|conj|ex|rem|prf|eq|fig|sec|chap|prose|sim|app):/;

  function route() {
    const hash = location.hash || "#/";
    const raw = hash.slice(1); // remove #

    // Shorthand: #rem:foo → load default paper and scroll to block
    if (LABEL_RE.test(raw)) {
      pendingScrollLabel = raw;
      if (!currentPaperId) {
        // Load default paper then scroll
        api(branchQuery("/api/folio")).then(data => {
          const id = data.papers?.[0]?.id;
          if (id) loadPaper(id);
        }).catch(() => loadFolio());
      } else {
        scrollToBlock(raw);
      }
      return;
    }

    const parts = raw.replace(/^\//, "").split("/").filter(Boolean);

    if (parts[0] === "paper" && parts[1]) {
      // #/paper/id/label → load paper and scroll to label
      const label = parts[2] && LABEL_RE.test(parts[2]) ? parts[2] : null;
      if (label) pendingScrollLabel = label;
      loadPaper(parts[1]);
    } else if (parts[0] === "view" && parts[1]) {
      // #/view/id or #/view/id/label (compat with viewer URLs)
      const label = parts[2] && LABEL_RE.test(parts[2]) ? parts[2] : null;
      if (label) pendingScrollLabel = label;
      loadPaper(parts[1]);
    } else {
      loadFolio();
    }
  }

  let pendingScrollLabel = null;
  let currentPaperId = null;

  function scrollToBlock(label) {
    const el = document.getElementById(label);
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "start" });
      el.style.outline = "2px solid var(--ac, #47a)";
      setTimeout(() => { el.style.outline = ""; }, 2000);
      pendingScrollLabel = null;
    }
  }
  window.addEventListener("hashchange", route);

  // ── API helpers ─────────────────────────────────────────
  async function api(path, signal) {
    const r = await fetch(path, signal ? { signal } : undefined);
    if (!r.ok) throw new Error(`${r.status} ${r.statusText}`);
    return r.json();
  }

  // ── Folio (landing page) ────────────────────────────────
  async function loadFolio() {
    document.body.dataset.folioMode = "folio";
    navLinks.innerHTML = "";
    app.innerHTML = '<div class="loading">loading folio...</div>';
    try {
      const data = await api(branchQuery("/api/folio"));
      folio = data.papers || [];
      renderFolio(data.title, folio);
      updateReadOnlyBanner();
    } catch (e) {
      app.innerHTML = `<div class="err">${esc(e.message)}</div>`;
    }
  }

  function renderFolio(title, papers) {
    const land = h("div", "landing");
    land.appendChild(h("h1", null, esc(title || "Papers")));
    land.appendChild(h("p", "subtitle", `${papers.length} paper${papers.length !== 1 ? "s" : ""}`));
    const grid = h("div", "paper-grid");
    for (const p of papers) {
      const card = h("div", "paper-card");
      card.innerHTML = `
        <h2>${esc(p.title)}</h2>
        <div class="meta">${esc((p.authors || []).join(", "))}${p.date ? " &middot; " + esc(p.date) : ""}</div>
        ${p.description ? `<p style="font-size:.8rem;color:var(--fg-d);margin-top:.4rem">${esc(p.description)}</p>` : ""}
        <div class="stats">
          <span class="stat">${p.stats.chapters} ch</span>
          <span class="stat">${p.stats.blocks} blocks</span>
          <span class="stat proved">${p.stats.proved} proved</span>
          <span class="stat todo">${p.stats.todos} todos</span>
        </div>
        <div class="paper-actions">
          <button class="primary" data-go="read">Read</button>
          <button data-go="qc">QC Dashboard</button>
        </div>`;
      card.querySelectorAll("button").forEach(b => {
        b.onclick = (e) => {
          e.stopPropagation();
          mode = b.dataset.go || "read";
          location.hash = `#/paper/${p.id}`;
        };
      });
      card.onclick = () => { mode = "read"; location.hash = `#/paper/${p.id}`; };
      grid.appendChild(card);
    }
    land.appendChild(grid);
    app.innerHTML = "";
    app.appendChild(land);
  }

  // ── Paper view ──────────────────────────────────────────
  async function loadPaper(id) {
    // Instant placeholder paints before any network round-trip.
    const guessTitle = prettifyPaperId(id);
    app.innerHTML = `<div class="paper-layout"><div class="paper-content"><div class="paper-hdr"><h1 style="opacity:.55">${esc(guessTitle)}</h1><div class="au" style="color:var(--fg-d);font-size:.8rem">loading paper…</div></div></div></div>`;
    document.title = `${guessTitle} — Folio`;
    currentPaperId = id;

    // Phase 1 — lightweight outline for the real header + sidebar skeleton.
    // We fetch outline and full paper in parallel so the UI paints structure
    // quickly while full block content streams in behind it.
    const outlinePromise = api(branchQuery(`/api/paper/outline?id=${encodeURIComponent(id)}`)).catch(() => null);
    const fullPromise = api(branchQuery(`/api/paper?id=${encodeURIComponent(id)}`));

    try {
      const outline = await outlinePromise;
      if (outline && mode === "read") {
        renderPaperSkeleton(outline);
        await yieldPaint();
      }

      const data = await fullPromise;
      paper = data;
      katexMacros = buildKatexMacros(data.macros);
      buildBlockIndex();
      updateReadOnlyBanner();
      if (mode === "diff") await loadDiff();
      else if (mode === "qc") renderQC();
      else await renderPaper();
      // Scroll to pending label after render
      if (pendingScrollLabel) {
        requestAnimationFrame(() => setTimeout(() => scrollToBlock(pendingScrollLabel), 500));
      }
    } catch (e) {
      app.innerHTML = `<div class="err">${esc(e.message)}</div>`;
    }
  }

  // Paints header + sidebar chapter list from the outline (no block content)
  // so the user sees the paper's structure before the full fetch completes.
  function renderPaperSkeleton(outline) {
    document.body.dataset.folioMode = "read";
    const wrap = h("div", "paper-layout");
    const sb = h("aside", "sidebar");
    const sbHead = h("div", "sidebar-header", esc(outline.title));
    sb.appendChild(sbHead);
    for (const ch of outline.chapters || []) {
      const tabLbl = ch.tabLabel || (ch.number != null ? String(ch.number) : "");
      const chEl = h("div", "sb-ch", `<span class="sb-tab">${esc(tabLbl)}</span><span class="arrow">&#9654;</span> <span class="sb-ch-title">${esc(ch.title)}</span>`);
      sb.appendChild(chEl);
    }
    wrap.appendChild(sb);
    const content = h("div", "paper-content");
    const hdr = h("div", "paper-hdr");
    hdr.innerHTML = `
      <h1>${esc(outline.title)}</h1>
      <div class="au">${esc((outline.authors || []).join(", "))}</div>
      ${outline.date ? `<div class="dt">${esc(outline.date)}</div>` : ""}`;
    content.appendChild(hdr);
    const skel = h("div", "loading", "loading chapters…");
    skel.style.cssText = "color:var(--fg-d);font-size:.8rem;padding:1rem 0";
    content.appendChild(skel);
    wrap.appendChild(content);
    app.innerHTML = "";
    app.appendChild(wrap);
    document.title = `${outline.title} — Folio`;
  }

  function buildBlockIndex() {
    blockIndex = {};
    if (!paper) return;
    for (const ch of paper.chapters || []) {
      for (const sec of ch.sections || []) {
        for (const blk of sec.blocks || []) {
          if (blk.label) blockIndex[blk.label] = blk;
        }
      }
    }
  }

  // ── Nav links ───────────────────────────────────────────
  function updateNav() {
    navLinks.innerHTML = "";
    const home = h("a", "", "folio");
    home.href = "#/";
    navLinks.appendChild(home);

    if (paper) {
      const readLink = h("a", mode === "read" ? "active" : "", "read");
      readLink.href = "#";
      readLink.onclick = (e) => { e.preventDefault(); if (diffAbort) diffAbort.abort(); mode = "read"; renderPaper(); };
      navLinks.appendChild(readLink);

      const qcLink = h("a", mode === "qc" ? "active" : "", "qc");
      qcLink.href = "#";
      qcLink.onclick = (e) => { e.preventDefault(); mode = "qc"; renderQC(); };
      navLinks.appendChild(qcLink);

      const cpLink = h("a", mode === "critical-path" ? "active" : "", "critical path");
      cpLink.href = "#";
      cpLink.onclick = (e) => { e.preventDefault(); mode = "critical-path"; renderCriticalPath(); };
      navLinks.appendChild(cpLink);

      if (selectedBranch && selectedBranch !== "main" && selectedBranch !== "master") {
        const diffLink = h("a", mode === "diff" ? "active" : "", "diff");
        diffLink.href = "#";
        diffLink.onclick = async (e) => { e.preventDefault(); mode = "diff"; await loadDiff(); };
        navLinks.appendChild(diffLink);
      }
    }

    // User badge
    const navRight = $(".nav-right");
    const existingBadge = $(".user-badge", navRight);
    if (existingBadge) existingBadge.remove();
    if (currentUser) {
      const badge = h("span", "user-badge");
      const roleClass = currentUser.role === "owner" ? "role-owner"
        : currentUser.role === "collaborator" ? "role-collab" : "role-viewer";
      const nameSpan = h("span", "user-name");
      nameSpan.textContent = currentUser.name;
      const roleSpan = h("span", "user-role " + roleClass);
      roleSpan.textContent = currentUser.role;
      badge.appendChild(nameSpan);
      badge.appendChild(roleSpan);
      const logout = h("a", "user-logout", "logout");
      logout.href = "/auth/logout";
      badge.appendChild(logout);
      navRight.insertBefore(badge, navRight.firstChild);
    }
  }

  // ── Paper: read mode ────────────────────────────────────
  async function renderPaper() {
    document.body.dataset.folioMode = "read";
    updateNav();
    const wrap = h("div", "paper-layout");

    // sidebar
    const sb = h("aside", "sidebar");
    const sbHead = h("div", "sidebar-header", esc(paper.title));
    sb.appendChild(sbHead);
    for (const ch of paper.chapters || []) {
      const tabLbl = ch.tabLabel || (ch.number != null ? String(ch.number) : "");
      const chEl = h("div", "sb-ch", `<span class="sb-tab">${esc(tabLbl)}</span><span class="arrow">&#9654;</span> <span class="sb-ch-title">${esc(ch.title)}</span>`);
      const secList = h("div", "sb-secs");
      const secInner = h("div", "sb-secs-inner");
      for (const sec of ch.sections || []) {
        const secWrap = h("div", "sb-sec-wrap");
        const secEl = h("div", "sb-sec", `<span class="sb-sec-arrow">&#9654;</span> ${esc(sec.title)}`);
        if (sec.label) secEl.dataset.sbLabel = sec.label;

        const blkList = h("div", "sb-blks");
        const blkInner = h("div", "sb-blks-inner");

        // block-level labels under each section
        for (const blk of sec.blocks || []) {
          if (blk.kind === "prose" || !blk.label) continue;
          const blkEl = h("div", "sb-blk",
            `<span class="sb-bk">${kindAbbr(blk.kind)}</span> ${esc(blk.title || blk.label)}`);
          blkEl.dataset.sbLabel = blk.label;
          blkEl.onclick = (e) => {
            e.stopPropagation();
            const target = document.getElementById(blk.label);
            if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
          };
          blkInner.appendChild(blkEl);
        }
        blkList.appendChild(blkInner);

        secEl.onclick = (e) => {
          e.stopPropagation();
          secWrap.classList.toggle("open");
          const target = document.getElementById(sec.label || "");
          if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
        };

        secWrap.appendChild(secEl);
        secWrap.appendChild(blkList);
        secInner.appendChild(secWrap);
      }
      secList.appendChild(secInner);
      chEl.onclick = () => { chEl.classList.toggle("open"); };
      sb.appendChild(chEl);
      sb.appendChild(secList);
    }
    wrap.appendChild(sb);

    // content
    const content = h("div", "paper-content");

    // header
    const hdr = h("div", "paper-hdr");
    hdr.innerHTML = `
      <h1>${esc(paper.title)}</h1>
      <div class="au">${esc((paper.authors || []).join(", "))}</div>
      ${paper.date ? `<div class="dt">${esc(paper.date)}</div>` : ""}`;
    content.appendChild(hdr);

    // Mount header + sidebar immediately so the user sees structure;
    // chapters are appended incrementally below with rAF yields between them.
    wrap.appendChild(content);
    app.innerHTML = "";
    app.appendChild(wrap);
    document.title = `${paper.title} — Folio`;
    await yieldPaint();

    // Render chapters progressively — one per frame, with the surrounding
    // paint committed between each. Cheap chapters batch; huge chapters break
    // naturally on the yield boundary.
    const chapters = paper.chapters || [];
    for (let i = 0; i < chapters.length; i++) {
      const chEl = renderChapter(chapters[i]);
      content.appendChild(chEl);
      // Render math for this chapter only so KaTeX cost amortizes per frame.
      try { renderMath(chEl); } catch {}
      if (i + 1 < chapters.length) await yieldPaint();
    }

    // Final polish: listeners, copy buttons, cross-ref enhancement, sidebar
    // active-block tracking. Deferred to idle so they don't block first paint.
    const finalize = () => {
      try { attachPopupListeners(app); } catch {}
      try { addCopyButtons(app); } catch {}
      try { enhanceIndexLinks(app); } catch {}
      try { observeVisibleBlocks(sb); } catch {}
    };
    (window.requestIdleCallback || requestAnimationFrame)(finalize);
  }

  function renderChapter(ch) {
    const el = h("div", "ch");
    const numSpan = ch.number != null ? `<span class="n">${ch.number}.</span> ` : "";
    el.innerHTML = `<h2 class="ch-t">${numSpan}${esc(ch.title)}</h2>`;
    for (const sec of ch.sections || []) {
      el.appendChild(renderSection(sec));
    }
    return el;
  }

  function renderSection(sec) {
    const el = h("div", "sec");
    if (sec.label) el.id = sec.label;
    el.innerHTML = `<h3 class="sec-t">${esc(sec.title)}</h3>`;

    // section jump bar
    const envBlocks = (sec.blocks || []).filter(b => b.kind !== "prose");
    if (envBlocks.length > 3) {
      const jump = h("div", "sec-jump");
      for (const b of envBlocks) {
        const a = h("a", "", `${kindAbbr(b.kind)} ${esc(b.title || b.label || b.rootName)}`);
        a.href = "#";
        a.onclick = (e) => {
          e.preventDefault();
          const t = document.getElementById(b.label || b.rootName);
          if (t) t.scrollIntoView({ behavior: "smooth", block: "start" });
        };
        jump.appendChild(a);
      }
      el.appendChild(jump);
    }

    for (const blk of sec.blocks || []) {
      el.appendChild(renderBlock(blk));
    }
    return el;
  }

  function renderBlock(blk) {
    if (blk.kind === "prose") {
      const el = h("div", "blk");
      if (blk.label) el.id = blk.label;
      el.innerHTML = `<div class="bb">${mdToHtml(blk.md || "", blk.rendered)}</div>`;
      return el;
    }

    const el = h("div", `env ${blk.kind}`);
    if (blk.label) el.id = blk.label;

    // header
    const bh = h("div", "bh");
    const statusCls = blk.status || blk.lean?.validation || "";
    const statusLabel = blk.status || blk.lean?.validation || "";
    const leanBadge = blk.lean
      ? `<span class="bh-lean ${statusCls}" title="${esc(blk.lean.decl)}${statusLabel ? " (" + esc(statusLabel) + ")" : ""}">∀${statusLabel ? `<span class="bh-lean-status">${esc(statusLabel)}</span>` : ""}</span>`
      : "";
    const proofBadge = blk.kind === "proof"
      ? `<span class="bh-lean ${statusCls}" title="proof block${statusLabel ? " (" + esc(statusLabel) + ")" : ""}">∀${statusLabel ? `<span class="bh-lean-status">${esc(statusLabel)}</span>` : ""}</span>`
      : "";
    bh.innerHTML = `
      <span class="bk">${esc(blk.kind)}</span>
      ${blk.title ? `<span class="bt">${esc(blk.title)}</span>` : ""}
      ${blk.label ? `<span class="bl">${esc(blk.label)}</span>` : ""}
      ${leanBadge || proofBadge}`;
    el.appendChild(bh);

    // action bar (role-gated)
    const actions = h("div", "blk-actions");
    const srcBtn = h("button", "blk-act", "src");
    srcBtn.title = "Toggle source";
    actions.appendChild(srcBtn);
    // Feedback: any authenticated user (viewer+)
    if (currentUser) {
      const fbBtn = h("button", "blk-act", "fb");
      fbBtn.title = "Send feedback";
      fbBtn.onclick = () => openFeedback(blk);
      actions.appendChild(fbBtn);
    }
    // Edit: collaborator+ only
    if (userCan("collaborator")) {
      const editBtn = h("button", "blk-act blk-act-edit", "edit");
      editBtn.title = "Edit content (WYSIWYG)";
      editBtn.onclick = () => openEditor(blk);
      actions.appendChild(editBtn);
    }
    el.appendChild(actions);

    // body
    const bb = h("div", "bb", mdToHtml(blk.md || "", blk.rendered));
    el.appendChild(bb);

    // source panel
    const srcPanel = h("pre", "bsrc", esc(blk.md || ""));
    srcBtn.onclick = () => srcPanel.classList.toggle("vis");
    el.appendChild(srcPanel);

    // lean badge + source toggle
    if (blk.lean) {
      const cls = blk.status || blk.lean.validation || "";
      const lb = h("div", `lb ${cls}`);
      lb.innerHTML = `<span class="vi ${blk.lean.validation || ""}"></span> ${esc(blk.lean.decl)} ${cls ? `(${cls})` : ""}`;
      lb.style.cursor = "pointer";
      lb.title = "Show Lean source";
      const leanPanel = h("pre", "lean-src");
      if (blk.lean.source) {
        leanPanel.textContent = blk.lean.source;
      } else {
        leanPanel.textContent = `-- No Lean source available for ${blk.lean.decl}\n-- Status: ${blk.status || "unknown"}`;
        leanPanel.classList.add("lean-src-empty");
      }
      const toggleLean = () => leanPanel.classList.toggle("vis");
      lb.onclick = toggleLean;
      el.appendChild(lb);
      el.appendChild(leanPanel);

      // Wire ∀ badge in header to same toggle
      const forallBadge = bh.querySelector(".bh-lean");
      if (forallBadge) forallBadge.onclick = toggleLean;
    }

    // uses
    if (blk.uses && blk.uses.length) {
      const uses = h("div", "uses", "uses: ");
      for (const ref of blk.uses) {
        const a = h("a", "uref", esc(ref));
        a.href = `#${ref}`;
        a.onclick = (e) => {
          e.preventDefault();
          const t = document.getElementById(ref);
          if (t) t.scrollIntoView({ behavior: "smooth", block: "start" });
        };
        uses.appendChild(a);
        uses.appendChild(document.createTextNode(" "));
      }
      el.appendChild(uses);
    }

    // tags
    if (blk.tags && blk.tags.length) {
      const tags = h("div", "tags");
      for (const t of blk.tags) tags.appendChild(h("span", "tag", esc(t)));
      el.appendChild(tags);
    }

    // todos
    if (blk.todos && blk.todos.length) {
      const badge = h("span", "todo-badge",
        `${blk.todos.length} todo${blk.todos.length > 1 ? "s" : ""}`);
      const list = h("div", "todo-list");
      for (const td of blk.todos) list.appendChild(renderTodoItem(td, blk));
      badge.onclick = () => list.classList.toggle("open");
      el.appendChild(badge);
      el.appendChild(list);
    }

    return el;
  }

  function renderTodoItem(td, blk) {
    const el = h("div", "todo-item");
    el.innerHTML = `
      <div class="ti-head">
        <span class="ti-status ${td.status}">${esc(td.status)}</span>
        <span class="ti-summary">${esc(td.summary)}</span>
      </div>
      ${td.comment ? `<div class="ti-comment">${esc(td.comment)}</div>` : ""}
      <div class="ti-meta">
        ${td.author ? esc(td.author) + " &middot; " : ""}
        ${td.priority ? td.priority : ""}
        ${td.assignee ? " &middot; " + esc(td.assignee) : ""}
        ${td.createdAt ? " &middot; " + esc(td.createdAt.slice(0, 10)) : ""}
      </div>`;

    // Delete button: collaborator+ only
    if (userCan("collaborator") && td.id && blk && paper) {
      const del = h("button", "ti-delete", "\u00d7");
      del.title = "Delete this todo";
      del.onclick = async (e) => {
        e.stopPropagation();
        if (!confirm("Delete this feedback item?")) return;
        try {
          const res = await fetch("/api/feedback/delete", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ paperId: paper.id, rootName: blk.rootName, todoId: td.id }),
          });
          if (res.ok) el.remove();
          else alert("Failed to delete: " + (await res.json()).error);
        } catch (err) { alert("Failed: " + err.message); }
      };
      el.querySelector(".ti-head").appendChild(del);
    }

    // AI triage button
    if (blk && paper && td.id) {
      const triageBtn = h("button", "fb-triage-btn", "AI Triage");
      const triageArea = h("div", "");
      triageBtn.onclick = async (e) => {
        e.stopPropagation();
        triageBtn.disabled = true;
        triageBtn.textContent = "Triaging...";
        triageArea.innerHTML = "";
        try {
          const res = await fetch("/api/feedback/triage", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ paperId: paper.id, rootName: blk.rootName, todoId: td.id }),
          });
          const data = await res.json();
          if (data.error && !data.assessment) throw new Error(data.error);
          const result = h("div", "triage-result");
          result.innerHTML = `<div class="triage-assessment">${esc(data.assessment)}</div>`;
          if (data.error) result.innerHTML += `<div class="char-error">${esc(data.error)}</div>`;
          if (data.actionable && data.proposedEdit) {
            const action = h("div", "triage-action");
            action.innerHTML = `<span>${esc(data.proposedEdit.description)}</span>`;

            // Branch selector for where to apply
            const brSelect = h("select", "triage-branch-select");
            const optCurrent = h("option", "", currentBranch + " (current)");
            optCurrent.value = "__current__";
            brSelect.appendChild(optCurrent);
            const optNew = h("option", "", "New branch");
            optNew.value = "__new__";
            brSelect.appendChild(optNew);
            action.appendChild(brSelect);

            const applyBtn = h("button", "triage-action-btn", "Apply Edit");
            applyBtn.onclick = async (ev) => {
              ev.stopPropagation();
              applyBtn.disabled = true;
              applyBtn.textContent = "Applying...";
              try {
                const saveRes = await fetch("/api/block/save", {
                  method: "POST",
                  headers: { "Content-Type": "application/json" },
                  body: JSON.stringify({ paperId: paper.id, rootName: blk.rootName, md: data.proposedEdit.newMd }),
                });
                if (!saveRes.ok) throw new Error(`${saveRes.status}`);
                showToast("Edit applied to " + blk.rootName);
                // Reload paper to reflect changes
                const hash = location.hash;
                const parts = hash.slice(2).split("/").filter(Boolean);
                if (parts[0] === "paper" && parts[1]) loadPaper(parts[1]);
              } catch (err) {
                showToast("Failed: " + err.message);
              }
              applyBtn.textContent = "Apply Edit";
              applyBtn.disabled = false;
            };
            action.appendChild(applyBtn);
            result.appendChild(action);
          }
          triageArea.appendChild(result);
        } catch (err) {
          triageArea.innerHTML = `<div class="char-error">${esc(err.message)}</div>`;
        }
        triageBtn.textContent = "AI Triage";
        triageBtn.disabled = false;
      };
      el.querySelector(".ti-meta").appendChild(triageBtn);
      el.appendChild(triageArea);
    }

    return el;
  }

  // ── QC Dashboard ────────────────────────────────────────
  function renderQC() {
    document.body.dataset.folioMode = "qc";
    updateNav();
    const qc = h("div", "qc");
    qc.innerHTML = `<h1>QC Dashboard &mdash; ${esc(paper.title)}</h1>`;

    // gather stats
    let total = 0, proved = 0, sorry = 0, notStarted = 0, stubs = 0;
    const allBlocks = [];
    for (const ch of paper.chapters || []) {
      for (const sec of ch.sections || []) {
        for (const blk of sec.blocks || []) {
          if (blk.kind === "prose") continue;
          total++;
          allBlocks.push({ ...blk, chapter: ch.title });
          const s = blk.status || "";
          if (s === "proved" || s === "validated") proved++;
          else if (s === "has_sorry") sorry++;
          else if (s === "stub") stubs++;
          else notStarted++;
        }
      }
    }

    // stat cards
    const stats = h("div", "qc-stats");
    stats.innerHTML = `
      <div class="qc-stat blue"><div class="num">${total}</div><div class="lbl">total blocks</div></div>
      <div class="qc-stat green"><div class="num">${proved}</div><div class="lbl">proved</div></div>
      <div class="qc-stat yellow"><div class="num">${sorry}</div><div class="lbl">has sorry</div></div>
      <div class="qc-stat red"><div class="num">${stubs}</div><div class="lbl">stubs</div></div>
      <div class="qc-stat"><div class="num">${notStarted}</div><div class="lbl">not started</div></div>`;
    qc.appendChild(stats);

    // filter bar
    let activeFilter = "all";
    const filters = h("div", "qc-filters");
    for (const f of ["all", "definition", "theorem", "proposition", "lemma", "example", "remark"]) {
      const btn = h("button", `qc-filter${f === "all" ? " active" : ""}`, f);
      btn.onclick = () => {
        activeFilter = f;
        $$(".qc-filter", qc).forEach(b => b.classList.toggle("active", b.textContent === f));
        renderTable();
      };
      filters.appendChild(btn);
    }
    qc.appendChild(filters);

    // table
    const tableWrap = h("div");
    qc.appendChild(tableWrap);

    function renderTable() {
      const filtered = activeFilter === "all" ? allBlocks : allBlocks.filter(b => b.kind === activeFilter);
      const tbl = h("table", "qc-table");
      tbl.innerHTML = `<thead><tr>
        <th>kind</th><th>label</th><th>title</th><th>lean</th><th>status</th><th>chapter</th>
      </tr></thead>`;
      const tbody = h("tbody");
      for (const b of filtered) {
        const tr = h("tr");
        const st = b.status || "—";
        const stCls = st === "proved" || st === "validated" ? "color:var(--grn)"
          : st === "has_sorry" ? "color:var(--yel)"
          : st === "stub" ? "color:var(--red)" : "";
        tr.innerHTML = `
          <td><span class="bk">${esc(b.kind)}</span></td>
          <td style="font-family:var(--f-mono);font-size:.7rem"><a href="#${b.label || ""}" style="color:var(--ac)">${esc(b.label || "—")}</a></td>
          <td>${esc(b.title || "—")}</td>
          <td style="font-family:var(--f-mono);font-size:.65rem">${b.lean ? esc(b.lean.decl) : "—"}</td>
          <td style="${stCls};font-family:var(--f-mono);font-size:.65rem">${esc(st)}</td>
          <td style="font-size:.7rem;color:var(--fg-d)">${esc(b.chapter)}</td>`;
        tr.onclick = () => {
          mode = "read";
          renderPaper();
          setTimeout(() => {
            const t = document.getElementById(b.label || "");
            if (t) t.scrollIntoView({ behavior: "smooth", block: "start" });
          }, 100);
        };
        tr.style.cursor = "pointer";
        tbody.appendChild(tr);
      }
      tbl.appendChild(tbody);
      tableWrap.innerHTML = "";
      tableWrap.appendChild(tbl);
    }
    renderTable();

    app.innerHTML = "";
    app.appendChild(qc);
  }

  // ── Feedback panel ──────────────────────────────────────
  const fbOverlay = $("#feedback-overlay");
  const fbPanel = $("#feedback-panel");
  const fbTarget = $("#fb-target");
  const fbText = $("#fb-text");
  const fbPriority = $("#fb-priority");
  const fbAssignee = $("#fb-assignee");

  let fbBlock = null;

  function openFeedback(blk) {
    fbBlock = blk;
    fbTarget.textContent = blk.label || blk.rootName || "block";
    fbText.value = "";
    fbOverlay.classList.add("open");
    fbPanel.classList.add("open");
    fbText.focus();
  }

  function closeFeedback() {
    fbOverlay.classList.remove("open");
    fbPanel.classList.remove("open");
    fbBlock = null;
  }

  $("#fb-close").onclick = closeFeedback;
  fbOverlay.onclick = closeFeedback;

  $("#fb-submit").onclick = async () => {
    if (!fbBlock || !fbText.value.trim()) return;
    try {
      const res = await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          paperId: paper.id,
          chapterDir: "",
          rootName: fbBlock.rootName,
          summary: fbText.value.trim().slice(0, 80),
          comment: fbText.value.trim(),
          priority: fbPriority.value,
          assignee: fbAssignee.value
        })
      });
      if (!res.ok) throw new Error(`${res.status}`);
      const data = await res.json();
      // show in history
      if (data.todo) {
        const history = $("#fb-history");
        history.prepend(renderTodoItem(data.todo, fbBlock));
      }
      fbText.value = "";
      closeFeedback();
    } catch (e) {
      alert("Failed to submit: " + e.message);
    }
  };

  // ── Voice input (Web Speech API, if available) ──────────
  const voiceBtn = $("#fb-voice");
  if (voiceBtn && "webkitSpeechRecognition" in window) {
    let rec = null;
    voiceBtn.onclick = () => {
      if (rec) { rec.stop(); return; }
      rec = new webkitSpeechRecognition();
      rec.continuous = false;
      rec.interimResults = false;
      voiceBtn.classList.add("recording");
      rec.onresult = (e) => {
        fbText.value += e.results[0][0].transcript + " ";
      };
      rec.onend = () => {
        voiceBtn.classList.remove("recording");
        rec = null;
      };
      rec.start();
    };
  }

  // ── Diff view ──────────────────────────────────────────
  async function loadDiff() {
    // Cancel any in-progress diff fetch
    if (diffAbort) diffAbort.abort();
    diffAbort = new AbortController();
    document.body.dataset.folioMode = "diff";
    updateNav();
    app.innerHTML = '<div class="loading">computing diff...<br><button class="diff-cancel" style="margin-top:1rem">cancel</button></div>';
    const cancelBtn = app.querySelector(".diff-cancel");
    if (cancelBtn) cancelBtn.onclick = () => { diffAbort.abort(); mode = "read"; renderPaper(); };
    try {
      const base = "main";
      const head = selectedBranch || currentBranch;
      const data = await api(`/api/diff?id=${encodeURIComponent(paper.id)}&base=${encodeURIComponent(base)}&head=${encodeURIComponent(head)}`, diffAbort.signal);
      diffData = data;
      renderDiff();
    } catch (e) {
      if (e.name === "AbortError") return; // user cancelled
      app.innerHTML = `<div class="err">${esc(e.message)}</div>`;
    } finally {
      diffAbort = null;
    }
  }

  function renderDiff() {
    if (!diffData) return;
    const wrap = h("div", "paper-layout");

    // sidebar with change markers
    const sb = h("aside", "sidebar");
    const sbHead = h("div", "sidebar-header");
    sbHead.innerHTML = `Diff: <strong>${esc(diffData.base)}</strong> \u2192 <strong>${esc(diffData.head)}</strong>`;
    sb.appendChild(sbHead);

    const summary = h("div", "diff-summary");
    summary.innerHTML = `
      <span class="diff-stat added">+${diffData.summary.added} added</span>
      <span class="diff-stat removed">\u2212${diffData.summary.removed} removed</span>
      <span class="diff-stat changed">\u0394${diffData.summary.changed} changed</span>
      <span class="diff-stat unchanged">${diffData.summary.unchanged} unchanged</span>`;
    sb.appendChild(summary);

    // Block list in sidebar — only changed/added/removed, then collapsed unchanged
    const changedBlocks = diffData.blocks.filter(b => b.status !== "unchanged");
    const unchangedBlocks = diffData.blocks.filter(b => b.status === "unchanged");

    for (const blk of changedBlocks) {
      const el = h("div", `sb-blk diff-${blk.status}`);
      const icon = blk.status === "added" ? "+" : blk.status === "removed" ? "\u2212" : "\u0394";
      el.innerHTML = `<span class="diff-icon">${icon}</span> ${esc(blk.title || blk.label || blk.rootName)}`;
      el.onclick = () => {
        const target = document.getElementById(`diff-${blk.rootName}`);
        if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
      };
      sb.appendChild(el);
    }

    if (unchangedBlocks.length) {
      const toggle = h("div", "sb-collapse");
      toggle.innerHTML = `<span class="arrow">\u25B6</span> ${unchangedBlocks.length} unchanged`;
      toggle.onclick = () => toggle.classList.toggle("open");
      sb.appendChild(toggle);
      const list = h("div", "sb-collapsed-list");
      for (const blk of unchangedBlocks) {
        const el = h("div", "sb-blk diff-unchanged");
        el.textContent = blk.title || blk.label || blk.rootName;
        list.appendChild(el);
      }
      sb.appendChild(list);
    }

    wrap.appendChild(sb);

    // content
    const content = h("div", "paper-content");
    const hdr = h("div", "diff-header");
    const mbInfo = diffData.mergeBase ? `<div class="diff-merge-base">from merge-base <code>${esc(diffData.mergeBase.slice(0, 8))}</code></div>` : "";
    hdr.innerHTML = `
      <h1>Changes: ${esc(diffData.base)} \u2192 ${esc(diffData.head)}</h1>
      ${mbInfo}
      <div class="diff-stats-bar">
        <span class="added">+${diffData.summary.added}</span>
        <span class="removed">\u2212${diffData.summary.removed}</span>
        <span class="changed">\u0394${diffData.summary.changed}</span>
      </div>`;

    // AI characterize button + results area
    const charSection = h("div", "characterize-section");
    const charBtn = h("button", "char-btn", "Characterize with AI");
    const charResult = h("div", "char-result");
    charBtn.onclick = async () => {
      charBtn.disabled = true;
      charBtn.textContent = "Analyzing...";
      charResult.innerHTML = "";
      try {
        const data = await api(`/api/characterize?id=${encodeURIComponent(paper.id)}&base=${encodeURIComponent(diffData.base)}&head=${encodeURIComponent(diffData.head)}`);
        charResult.innerHTML = `
          <div class="char-title">${esc(data.title)}</div>
          <div class="char-summary">${esc(data.summary)}</div>
          <div class="char-meta">
            <span class="char-impact char-impact-${data.impact}">${esc(data.impact)}</span>
            ${(data.categories || []).map(c => `<span class="char-cat">${esc(c)}</span>`).join("")}
          </div>
          ${data.suggestions?.length ? `<div class="char-suggestions"><strong>Suggestions:</strong><ul>${data.suggestions.map(s => `<li>${esc(s)}</li>`).join("")}</ul></div>` : ""}
          ${data.error ? `<div class="char-error">${esc(data.error)}</div>` : ""}`;
      } catch (e) {
        charResult.innerHTML = `<div class="char-error">${esc(e.message)}</div>`;
      }
      charBtn.textContent = "Characterize with AI";
      charBtn.disabled = false;
    };
    charSection.appendChild(charBtn);
    charSection.appendChild(charResult);
    hdr.appendChild(charSection);

    content.appendChild(hdr);

    // Changed blocks first, then unchanged (collapsed)
    for (const blk of changedBlocks) {
      content.appendChild(renderDiffBlock(blk));
    }

    if (unchangedBlocks.length) {
      const collapsedSection = h("details", "diff-unchanged-section");
      const summ = h("summary", "", `${unchangedBlocks.length} unchanged blocks`);
      collapsedSection.appendChild(summ);
      for (const blk of unchangedBlocks) {
        const el = h("div", "env diff-unchanged-block");
        el.id = `diff-${blk.rootName}`;
        el.innerHTML = `<div class="bh"><span class="bk">${esc(blk.kind)}</span> ${blk.title ? `<span class="bt">${esc(blk.title)}</span>` : ""}</div>`;
        collapsedSection.appendChild(el);
      }
      content.appendChild(collapsedSection);
    }

    wrap.appendChild(content);
    app.innerHTML = "";
    app.appendChild(wrap);
    renderMath(app);
  }

  function renderDiffBlock(blk) {
    const el = h("div", `env diff-block diff-${blk.status}`);
    el.id = `diff-${blk.rootName}`;

    // header with diff status badge
    const statusIcon = blk.status === "added" ? "+" : blk.status === "removed" ? "\u2212" : "\u0394";
    const bh = h("div", "bh");
    bh.innerHTML = `
      <span class="diff-badge diff-badge-${blk.status}">${statusIcon} ${esc(blk.status)}</span>
      <span class="bk">${esc(blk.kind)}</span>
      ${blk.title ? `<span class="bt">${esc(blk.title)}</span>` : ""}
      ${blk.label ? `<span class="bl">${esc(blk.label)}</span>` : ""}`;
    el.appendChild(bh);

    // Status change indicator
    if (blk.statusDiff) {
      const sd = h("div", "diff-status-change");
      sd.innerHTML = `Status: <span class="diff-old">${esc(blk.statusDiff.base)}</span> \u2192 <span class="diff-new">${esc(blk.statusDiff.head)}</span>`;
      el.appendChild(sd);
    }

    // View toggle bar: Diff | Old | New | Source
    const hasContent = blk.mdDiff || blk.leanDiff;
    if (hasContent) {
      const toggleBar = h("div", "diff-toggle-bar");
      const views = ["diff", "old", "new", "source"];
      const labels = { diff: "Diff", old: "Old", "new": "New", source: "Source" };
      const panes = {};
      let activeView = "diff";

      for (const v of views) {
        if (v === "old" && blk.status === "added") continue;
        if (v === "new" && blk.status === "removed") continue;
        const btn = h("button", `diff-toggle-btn${v === "diff" ? " active" : ""}`, labels[v]);
        btn.dataset.view = v;
        btn.onclick = () => {
          toggleBar.querySelectorAll(".diff-toggle-btn").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          for (const [key, pane] of Object.entries(panes)) {
            pane.style.display = key === v ? "" : "none";
          }
          activeView = v;
          if (v === "old" || v === "new") renderMath(panes[v]);
        };
        toggleBar.appendChild(btn);
      }
      el.appendChild(toggleBar);

      // Diff pane (default)
      const diffPane = h("div", "diff-pane");
      if (blk.mdDiff) {
        const diffEl = h("div", "diff-content");
        diffEl.appendChild(renderLineDiff(blk.mdDiff.base, blk.mdDiff.head));
        diffPane.appendChild(diffEl);
      }
      if (blk.leanDiff) {
        const leanDiffEl = h("div", "diff-lean");
        leanDiffEl.appendChild(h("div", "diff-lean-header", "\u2200 Lean source"));
        leanDiffEl.appendChild(renderLineDiff(blk.leanDiff.base, blk.leanDiff.head));
        diffPane.appendChild(leanDiffEl);
      }
      panes.diff = diffPane;
      el.appendChild(diffPane);

      // Old pane (rendered base)
      if (blk.status !== "added") {
        const oldPane = h("div", "diff-pane diff-pane-old");
        oldPane.style.display = "none";
        if (blk.mdDiff) oldPane.appendChild(h("div", "bb diff-rendered", mdToHtml(blk.mdDiff.base || "")));
        if (blk.leanDiff && blk.leanDiff.base) {
          const le = h("div", "diff-lean");
          le.appendChild(h("div", "diff-lean-header", "\u2200 Lean source (old)"));
          le.appendChild(h("pre", "diff-lean-src", esc(blk.leanDiff.base)));
          oldPane.appendChild(le);
        }
        panes.old = oldPane;
        el.appendChild(oldPane);
      }

      // New pane (rendered head)
      if (blk.status !== "removed") {
        const newPane = h("div", "diff-pane diff-pane-new");
        newPane.style.display = "none";
        if (blk.mdDiff) newPane.appendChild(h("div", "bb diff-rendered", mdToHtml(blk.mdDiff.head || "")));
        if (blk.leanDiff && blk.leanDiff.head) {
          const le = h("div", "diff-lean");
          le.appendChild(h("div", "diff-lean-header", "\u2200 Lean source (new)"));
          le.appendChild(h("pre", "diff-lean-src", esc(blk.leanDiff.head)));
          newPane.appendChild(le);
        }
        panes["new"] = newPane;
        el.appendChild(newPane);
      }

      // Source pane (raw markdown side-by-side)
      const srcPane = h("div", "diff-pane diff-pane-source");
      srcPane.style.display = "none";
      if (blk.mdDiff) {
        const cols = h("div", "diff-source-columns");
        const oldCol = h("div", "diff-source-col");
        oldCol.appendChild(h("div", "diff-source-label", "Old source"));
        oldCol.appendChild(h("pre", "diff-source-pre", esc(blk.mdDiff.base || "")));
        cols.appendChild(oldCol);
        const newCol = h("div", "diff-source-col");
        newCol.appendChild(h("div", "diff-source-label", "New source"));
        newCol.appendChild(h("pre", "diff-source-pre", esc(blk.mdDiff.head || "")));
        cols.appendChild(newCol);
        srcPane.appendChild(cols);
      }
      if (blk.leanDiff) {
        const cols = h("div", "diff-source-columns");
        const oldCol = h("div", "diff-source-col");
        oldCol.appendChild(h("div", "diff-source-label", "\u2200 Old"));
        oldCol.appendChild(h("pre", "diff-source-pre", esc(blk.leanDiff.base || "")));
        cols.appendChild(oldCol);
        const newCol = h("div", "diff-source-col");
        newCol.appendChild(h("div", "diff-source-label", "\u2200 New"));
        newCol.appendChild(h("pre", "diff-source-pre", esc(blk.leanDiff.head || "")));
        cols.appendChild(newCol);
        srcPane.appendChild(cols);
      }
      panes.source = srcPane;
      el.appendChild(srcPane);
    }

    // Feedback: button + inline todo list with edit/delete
    const fbSection = h("div", "diff-fb-section");

    // "Add feedback" button — reuses the slide-in panel
    const fbBtn = h("button", "diff-fb-btn", "+ feedback");
    fbBtn.onclick = () => openFeedback(blk);
    fbSection.appendChild(fbBtn);

    // Inline existing todos
    if (blk.todos && blk.todos.length) {
      const todoList = h("div", "diff-todo-list");
      for (const td of blk.todos) {
        todoList.appendChild(renderDiffTodo(td, blk, todoList));
      }
      fbSection.appendChild(todoList);
    }
    el.appendChild(fbSection);

    return el;
  }

  /** Render a todo item inside a diff block with inline edit/delete controls. */
  function renderDiffTodo(td, blk, listEl) {
    const el = h("div", `diff-todo-item pri-${td.priority || "medium"}`);

    const head = h("div", "diff-todo-head");
    head.innerHTML = `
      <span class="diff-todo-status ${td.status || ""}">${esc(td.status || "open")}</span>
      <span class="diff-todo-summary">${esc(td.summary || "")}</span>`;
    el.appendChild(head);

    if (td.comment && td.comment !== td.summary) {
      el.appendChild(h("div", "diff-todo-comment", esc(td.comment)));
    }

    // Controls: priority selector + delete button
    const controls = h("div", "diff-todo-controls");

    // Priority selector
    const priSelect = h("select", "diff-todo-pri");
    for (const p of ["low", "medium", "high", "critical"]) {
      const opt = document.createElement("option");
      opt.value = p;
      opt.textContent = p;
      if (p === (td.priority || "medium")) opt.selected = true;
      priSelect.appendChild(opt);
    }
    priSelect.onchange = async () => {
      try {
        await fetch("/api/feedback/update", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paperId: paper.id, rootName: blk.rootName, todoId: td.id, priority: priSelect.value }),
        });
        td.priority = priSelect.value;
        el.className = `diff-todo-item pri-${priSelect.value}`;
        showToast("Priority updated");
      } catch (e) { showToast("Failed: " + e.message); }
    };
    controls.appendChild(priSelect);

    // Assignee label
    if (td.assignee) {
      controls.appendChild(h("span", "diff-todo-assignee", esc(td.assignee)));
    }

    // Date
    if (td.createdAt) {
      controls.appendChild(h("span", "diff-todo-date", esc(td.createdAt.slice(0, 10))));
    }

    // Delete button
    const delBtn = h("button", "diff-todo-del", "\u00d7");
    delBtn.title = "Delete feedback";
    delBtn.onclick = async () => {
      if (!confirm("Delete this feedback item?")) return;
      try {
        const res = await fetch("/api/feedback/delete", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paperId: paper.id, rootName: blk.rootName, todoId: td.id }),
        });
        if (!res.ok) throw new Error(`${res.status}`);
        el.remove();
        // Update blk.todos
        if (blk.todos) blk.todos = blk.todos.filter(t => t.id !== td.id);
        showToast("Feedback deleted");
      } catch (e) { showToast("Failed: " + e.message); }
    };
    controls.appendChild(delBtn);

    el.appendChild(controls);
    return el;
  }

  /** Simple line-by-line diff renderer. */
  function renderLineDiff(base, head) {
    const baseLines = (base || "").split("\n");
    const headLines = (head || "").split("\n");
    const el = h("div", "line-diff");

    // Simple LCS-based diff
    const lcs = computeLCS(baseLines, headLines);
    let bi = 0, hi = 0, li = 0;

    while (bi < baseLines.length || hi < headLines.length) {
      if (li < lcs.length && bi < baseLines.length && hi < headLines.length
          && baseLines[bi] === lcs[li] && headLines[hi] === lcs[li]) {
        // context line (same in both)
        const line = h("div", "diff-line ctx");
        line.innerHTML = `<span class="diff-gutter"> </span><span class="diff-text">${esc(baseLines[bi])}</span>`;
        el.appendChild(line);
        bi++; hi++; li++;
      } else {
        // removed lines from base
        while (bi < baseLines.length && (li >= lcs.length || baseLines[bi] !== lcs[li])) {
          const line = h("div", "diff-line del");
          line.innerHTML = `<span class="diff-gutter">\u2212</span><span class="diff-text">${esc(baseLines[bi])}</span>`;
          el.appendChild(line);
          bi++;
        }
        // added lines from head
        while (hi < headLines.length && (li >= lcs.length || headLines[hi] !== lcs[li])) {
          const line = h("div", "diff-line ins");
          line.innerHTML = `<span class="diff-gutter">+</span><span class="diff-text">${esc(headLines[hi])}</span>`;
          el.appendChild(line);
          hi++;
        }
      }
    }

    return el;
  }

  /** Compute longest common subsequence of two arrays. */
  function computeLCS(a, b) {
    const m = a.length, n = b.length;
    // For very large files, skip LCS and just show side-by-side
    if (m > 500 || n > 500) return [];
    const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
        dp[i][j] = a[i - 1] === b[j - 1] ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
    const result = [];
    let i = m, j = n;
    while (i > 0 && j > 0) {
      if (a[i - 1] === b[j - 1]) { result.unshift(a[i - 1]); i--; j--; }
      else if (dp[i - 1][j] > dp[i][j - 1]) i--;
      else j--;
    }
    return result;
  }

  // ── Markdown → HTML (minimal) ───────────────────────────
  function mdToHtml(md, rendered) {
    let out = md;
    // display math $$...$$
    out = out.replace(/\$\$([\s\S]*?)\$\$/g, (_, tex) =>
      `<span class="katex-display-raw" data-tex="${escAttr(tex.trim())}"></span>`);
    // inline math $...$
    out = out.replace(/\$([^\n$]+?)\$/g, (_, tex) =>
      `<span class="katex-inline-raw" data-tex="${escAttr(tex.trim())}"></span>`);
    // fenced code blocks — replace ```tex with rendered SVG if available
    let texBlockIdx = 0;
    out = out.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => {
      if (lang === "tex" || lang === "latex") {
        const idx = texBlockIdx++;
        const asset = rendered && rendered.find(r => r.blockIndex === idx);
        if (asset) {
          return `<div class="txb"><img src="${escAttr(asset.url)}" alt="diagram" class="txb-svg"></div>`;
        }
        // Try KaTeX for simple environments, show raw for complex (tikzcd)
        const trimmed = code.trim();
        if (/\\begin\{(align|equation|gather|cases)/.test(trimmed)) {
          // Strip \begin{env}...\end{env} wrapper for KaTeX
          const inner = trimmed.replace(/^\\begin\{[^}]+\}/, "").replace(/\\end\{[^}]+\}$/, "").trim();
          return `<span class="katex-display-raw" data-tex="${escAttr(inner)}"></span>`;
        }
        return `<div class="txb ph">${esc(trimmed)}</div>`;
      }
      return `<pre style="background:var(--bg-r);padding:.6rem;border-radius:4px;overflow-x:auto;font-size:.8rem"><code>${esc(code)}</code></pre>`;
    });
    // markdown tables
    out = out.replace(/((?:^\|.+\|$\n?)+)/gm, (tableBlock) => {
      const rows = tableBlock.trim().split("\n").filter(r => r.trim());
      if (rows.length < 2) return tableBlock;
      // Check if row 2 is a separator (|---|---|)
      const isSep = /^\|[\s:]*-+[\s:]*(\|[\s:]*-+[\s:]*)*\|?$/.test(rows[1]);
      let html = '<table class="md-table">';
      const dataRows = isSep ? [rows[0], ...rows.slice(2)] : rows;
      for (let i = 0; i < dataRows.length; i++) {
        const cells = dataRows[i].split("|").slice(1, -1);
        const tag = (i === 0 && isSep) ? "th" : "td";
        html += "<tr>" + cells.map(c => `<${tag}>${c.trim()}</${tag}>`).join("") + "</tr>";
      }
      html += "</table>";
      return html;
    });
    // headings (## and ###)
    out = out.replace(/^### (.+)$/gm, '<h4 class="md-h4">$1</h4>');
    out = out.replace(/^## (.+)$/gm, '<h3 class="md-h3">$1</h3>');
    // bold, italic (allow multiline spans)
    out = out.replace(/\*\*([\s\S]+?)\*\*/g, "<strong>$1</strong>");
    out = out.replace(/\*([^\n*][^*]*?)\*/g, "<em>$1</em>");
    // inline code
    out = out.replace(/`([^`]+)`/g, '<code style="background:var(--bg-r);padding:.1rem .3rem;border-radius:3px;font-size:.85em">$1</code>');
    // citations \cite{key} → [key]
    out = out.replace(/\\cite\{([^}]+)\}/g, '<span class="cite" title="$1">[$1]</span>');
    // en-dash and em-dash
    out = out.replace(/---/g, "\u2014");
    out = out.replace(/--/g, "\u2013");
    // cross-refs [text](#label)
    out = out.replace(/\[([^\]]+)\]\(#([^)]+)\)/g,
      '<a class="uref" href="#$2" onclick="event.preventDefault();document.getElementById(\'$2\')?.scrollIntoView({behavior:\'smooth\',block:\'start\'})">$1</a>');
    // markdown list items
    out = out.replace(/^(\d+)\.\s+(.+)$/gm, '<li class="md-li" value="$1">$2</li>');
    out = out.replace(/^[-*]\s+(.+)$/gm, '<li class="md-li">$1</li>');
    // paragraphs (but not after block elements)
    out = out.replace(/\n{2,}/g, "</p><p>");
    out = "<p>" + out + "</p>";
    // Clean up empty paragraphs around block elements
    out = out.replace(/<p>(<table|<h[34])/g, "$1");
    out = out.replace(/(<\/table>|<\/h[34]>)<\/p>/g, "$1");
    return out;
  }

  // ── KaTeX rendering ─────────────────────────────────────
  let katexMacros = {};
  function buildKatexMacros(paperMacros) {
    const m = {};
    if (paperMacros) {
      for (const [name, def] of Object.entries(paperMacros)) {
        m['\\' + name] = def.tex;
      }
    }
    return m;
  }
  function renderMath(root) {
    if (!window.katex) return;
    root.querySelectorAll(".katex-display-raw").forEach(el => {
      try {
        katex.render(el.dataset.tex, el, { displayMode: true, throwOnError: false, macros: katexMacros });
      } catch (_) { el.textContent = el.dataset.tex; }
    });
    root.querySelectorAll(".katex-inline-raw").forEach(el => {
      try {
        katex.render(el.dataset.tex, el, { displayMode: false, throwOnError: false, macros: katexMacros });
      } catch (_) { el.textContent = el.dataset.tex; }
    });
  }

  // ── Block preview popup (hover over cross-ref links) ────
  let popupEl = null;
  let popupTimer = null;
  let popupLabel = null;

  function createPopup() {
    if (popupEl) return popupEl;
    popupEl = h("div", "blk-popup");
    popupEl.innerHTML = `<div class="blk-popup-head"><span class="blk-popup-title"></span><button class="blk-popup-expand" title="Fullscreen">⛶</button><button class="blk-popup-close" title="Close">&times;</button></div><div class="blk-popup-body"></div>`;
    popupEl.onmouseenter = () => clearTimeout(popupTimer);
    popupEl.onmouseleave = () => hidePopup();
    popupEl.querySelector(".blk-popup-close").onclick = () => hidePopup(true);
    popupEl.querySelector(".blk-popup-expand").onclick = () => openBlockModal(popupLabel);
    document.body.appendChild(popupEl);
    return popupEl;
  }

  function showPopup(label, anchorEl) {
    const blk = blockIndex[label];
    if (!blk) return;
    clearTimeout(popupTimer);
    popupLabel = label;
    const popup = createPopup();
    popup.querySelector(".blk-popup-title").innerHTML =
      `<span class="bk">${esc(blk.kind)}</span> ${esc(blk.title || blk.label)}`;
    const body = popup.querySelector(".blk-popup-body");
    body.innerHTML = mdToHtml(blk.md || "", blk.rendered);
    popup.classList.add("vis");
    renderMath(body);
    // Position near anchor
    const rect = anchorEl.getBoundingClientRect();
    popup.style.top = Math.min(rect.bottom + 4, window.innerHeight - popup.offsetHeight - 8) + "px";
    popup.style.left = Math.max(8, Math.min(rect.left, window.innerWidth - popup.offsetWidth - 8)) + "px";
  }

  function hidePopup(immediate) {
    if (!popupEl) return;
    if (immediate) { popupEl.classList.remove("vis"); return; }
    popupTimer = setTimeout(() => popupEl.classList.remove("vis"), 200);
  }

  // ── Fullscreen block modal ─────────────────────────────
  function openBlockModal(label) {
    const blk = blockIndex[label];
    if (!blk) return;
    hidePopup(true);
    const overlay = h("div", "blk-modal-overlay");
    const modal = h("div", "blk-modal");
    // Render the block using the same renderBlock function
    const rendered = renderBlock(blk);
    rendered.style.margin = "0";
    rendered.style.border = "none";
    const head = h("div", "blk-modal-head");
    head.innerHTML = `<button class="blk-modal-close">&times;</button>`;
    modal.appendChild(head);
    modal.appendChild(rendered);
    renderMath(rendered);
    function close() { overlay.remove(); modal.remove(); }
    overlay.onclick = close;
    head.querySelector(".blk-modal-close").onclick = close;
    document.addEventListener("keydown", function esc(e) {
      if (e.key === "Escape") { close(); document.removeEventListener("keydown", esc); }
    });
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
  }

  // Attach hover listeners after render
  function attachPopupListeners(root) {
    for (const a of root.querySelectorAll("a.uref")) {
      const label = (a.getAttribute("href") || "").replace("#", "");
      if (!label || !blockIndex[label]) continue;
      a.addEventListener("mouseenter", () => showPopup(label, a));
      a.addEventListener("mouseleave", () => hidePopup());
    }
  }

  // ── Copy button for stubs ──────────────────────────────
  function addCopyButtons(root) {
    for (const envEl of root.querySelectorAll(".env")) {
      const label = envEl.id;
      if (!label) continue;
      const blk = blockIndex[label];
      if (!blk) continue;
      // Show copy button if: has sorry, not started, or stated (no proof)
      const status = blk.status || blk.lean?.validation || "";
      const isStub = status === "has_sorry" || status === "stated" || status === "not_started" ||
        (["definition","theorem","proposition","lemma","corollary"].includes(blk.kind) && (!blk.lean || !blk.lean.source));
      if (!isStub) continue;
      const copyBtn = h("button", "blk-copy", "📋");
      copyBtn.title = "Copy block content";
      copyBtn.onclick = (e) => {
        e.stopPropagation();
        const text = [
          `-- ${blk.kind}: ${blk.title || blk.label}`,
          `-- Label: ${blk.label}`,
          blk.lean?.decl ? `-- Lean: ${blk.lean.decl}` : "",
          "",
          blk.md || "",
          "",
          blk.lean?.source || (blk.lean?.decl ? `-- TODO: prove ${blk.lean.decl}\nsorry` : ""),
        ].filter(Boolean).join("\n");
        navigator.clipboard.writeText(text).then(() => {
          copyBtn.textContent = "✓";
          setTimeout(() => { copyBtn.textContent = "📋"; }, 1500);
        });
      };
      envEl.appendChild(copyBtn);
    }
  }

  // ── Index page: expand definitions inline ───────────────
  function enhanceIndexLinks(root) {
    // Find the index chapter (label = app:index-definitions)
    const indexEl = root.querySelector("#sec\\:definition-index");
    if (!indexEl) return;
    // Find all uref links in the index section's parent
    const indexSection = indexEl.closest(".sec") || indexEl.closest(".ch") || indexEl.parentElement;
    if (!indexSection) return;
    for (const a of indexSection.querySelectorAll("a.uref")) {
      const label = (a.getAttribute("href") || "").replace("#", "");
      if (!label || !blockIndex[label]) continue;
      // Replace scroll behavior with inline expand
      a.onclick = (e) => {
        e.preventDefault();
        const blk = blockIndex[label];
        if (!blk) return;
        // Toggle: if already expanded, collapse
        const existing = a.parentElement.querySelector(`.idx-expand[data-label="${CSS.escape(label)}"]`);
        if (existing) { existing.remove(); return; }
        // Create inline expansion
        const expand = h("div", "idx-expand");
        expand.dataset.label = label;
        const rendered = renderBlock(blk);
        rendered.style.margin = ".5rem 0";
        expand.appendChild(rendered);
        // Insert after the table row or after the link
        const td = a.closest("td");
        const tr = a.closest("tr");
        if (tr) {
          const expandRow = document.createElement("tr");
          const expandCell = document.createElement("td");
          expandCell.colSpan = 4;
          expandCell.appendChild(expand);
          expandRow.appendChild(expandCell);
          tr.after(expandRow);
        } else {
          a.after(expand);
        }
        renderMath(expand);
        attachPopupListeners(expand);
      };
    }
  }

  // ── Scroll-based sidebar highlighting ───────────────────
  function observeVisibleBlocks(sb) {
    const sidebarLinks = $$("[data-sb-label]", sb);
    if (!sidebarLinks.length) return;

    const io = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        const label = entry.target.id;
        if (!label) continue;
        const link = sb.querySelector(`[data-sb-label="${CSS.escape(label)}"]`);
        if (link) link.classList.toggle("active", entry.isIntersecting);
      }
    }, { rootMargin: "-40px 0px -40% 0px", threshold: 0 });

    for (const link of sidebarLinks) {
      const label = link.dataset.sbLabel;
      const target = document.getElementById(label);
      if (target) io.observe(target);
    }
  }

  // ── Helpers ─────────────────────────────────────────────
  function esc(s) {
    if (s == null) return "";
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function escAttr(s) {
    return esc(s).replace(/'/g, "&#39;");
  }
  function kindAbbr(k) {
    const m = { definition: "Def", theorem: "Thm", proposition: "Prop", lemma: "Lem",
      corollary: "Cor", example: "Ex", remark: "Rem", conjecture: "Conj" };
    return m[k] || k;
  }

  // ── WYSIWYG editor (collaborator+ only) ─────────────────
  function openEditor(blk) {
    if (!userCan("collaborator")) return;
    const overlay = h("div", "editor-overlay");
    const panel = h("div", "editor-panel");
    panel.innerHTML = `
      <div class="editor-head">
        <h3>Edit: ${esc(blk.title || blk.rootName)}</h3>
        <button class="editor-close">&times;</button>
      </div>`;
    const textarea = h("textarea", "editor-textarea");
    textarea.value = blk.md || "";
    textarea.rows = 20;
    panel.appendChild(textarea);

    const actions = h("div", "editor-actions");
    const saveBtn = h("button", "editor-save", "Save");
    const cancelBtn = h("button", "editor-cancel", "Cancel");
    actions.appendChild(cancelBtn);
    actions.appendChild(saveBtn);
    panel.appendChild(actions);

    function close() { overlay.remove(); panel.remove(); }
    overlay.onclick = close;
    panel.querySelector(".editor-close").onclick = close;
    cancelBtn.onclick = close;

    saveBtn.onclick = async () => {
      try {
        const res = await fetch("/api/block/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            paperId: paper.id,
            rootName: blk.rootName,
            md: textarea.value,
          }),
        });
        if (!res.ok) {
          const data = await res.json();
          alert("Save failed: " + (data.error || res.status));
          return;
        }
        blk.md = textarea.value;
        close();
        renderPaper();
      } catch (e) { alert("Save failed: " + e.message); }
    };

    document.body.appendChild(overlay);
    document.body.appendChild(panel);
    textarea.focus();
  }

  // ── Critical Path view ─────────────────────────────────
  function computeCriticalPath() {
    if (!paper) return [];
    // Build flat block list and dependency maps
    const allBlocks = [];
    const byLabel = {};
    for (const ch of paper.chapters || []) {
      for (const sec of ch.sections || []) {
        for (const blk of sec.blocks || []) {
          allBlocks.push({ ...blk, _chapter: ch.title, _chapterNum: ch.number, _section: sec.title });
          if (blk.label) byLabel[blk.label] = blk;
        }
      }
    }

    // Build reverse-dep map: which blocks are used BY other blocks
    const usedBy = {}; // label → Set of labels that use it
    for (const blk of allBlocks) {
      if (blk.uses) {
        for (const ref of blk.uses) {
          if (!usedBy[ref]) usedBy[ref] = new Set();
          usedBy[ref].add(blk.label);
        }
      }
    }

    // Provable block kinds (things that form the proof chain)
    const provableKinds = new Set(["theorem", "proposition", "lemma", "corollary"]);
    const defKinds = new Set(["definition"]);

    // Find "leaf" theorems: provable blocks not used by any other provable block
    const leafTheorems = allBlocks.filter(blk => {
      if (!provableKinds.has(blk.kind)) return false;
      if (!blk.label) return false;
      const consumers = usedBy[blk.label];
      if (!consumers) return true;
      // Check if any consumer is also provable
      for (const c of consumers) {
        const cb = byLabel[c];
        if (cb && provableKinds.has(cb.kind)) return false;
      }
      return true;
    });

    // BFS backwards from leaf theorems through uses to collect the full critical path
    const onPath = new Set();
    const queue = [...leafTheorems.map(b => b.label).filter(Boolean)];
    while (queue.length) {
      const label = queue.shift();
      if (onPath.has(label)) continue;
      onPath.add(label);
      const blk = byLabel[label];
      if (blk && blk.uses) {
        for (const ref of blk.uses) {
          if (!onPath.has(ref) && byLabel[ref]) queue.push(ref);
        }
      }
    }

    // Collect blocks in document order, preserving narrative flow
    const result = [];
    for (const blk of allBlocks) {
      if (!blk.label) continue;
      if (!onPath.has(blk.label)) continue;
      result.push(blk);
    }
    return result;
  }

  function renderCriticalPath() {
    document.body.dataset.folioMode = "critical-path";
    updateNav();
    const cpBlocks = computeCriticalPath();

    const wrap = h("div", "critical-path-layout");

    // Header with print controls
    const hdr = h("div", "cp-header");
    hdr.innerHTML = `
      <h1>Critical Path</h1>
      <p class="cp-subtitle">${esc(paper.title)} &mdash; ${cpBlocks.length} blocks on the critical proof chain</p>
      <div class="cp-actions">
        <button class="cp-btn" id="cp-print-browser" title="Print in browser">Print</button>
        <button class="cp-btn cp-btn-secondary" id="cp-export-latex" title="Export as LaTeX">Export LaTeX</button>
      </div>`;
    wrap.appendChild(hdr);

    // Render blocks as a cohesive narrative
    const content = h("div", "cp-content");
    let lastChapter = null;
    let lastSection = null;

    for (const blk of cpBlocks) {
      // Chapter heading
      if (blk._chapter !== lastChapter) {
        lastChapter = blk._chapter;
        lastSection = null;
        const ch = h("h2", "cp-chapter", `${blk._chapterNum ? blk._chapterNum + ". " : ""}${esc(blk._chapter)}`);
        content.appendChild(ch);
      }
      // Section heading
      if (blk._section !== lastSection) {
        lastSection = blk._section;
        content.appendChild(h("h3", "cp-section", esc(blk._section)));
      }
      // Block
      content.appendChild(renderCPBlock(blk));
    }

    if (!cpBlocks.length) {
      content.appendChild(h("div", "cp-empty", "No critical path blocks found. The paper may not have dependency chains (uses fields) set up yet."));
    }

    wrap.appendChild(content);
    app.innerHTML = "";
    app.appendChild(wrap);
    renderMath(app);

    // Wire up print buttons
    const printBtn = $("#cp-print-browser");
    const latexBtn = $("#cp-export-latex");
    if (printBtn) printBtn.onclick = () => printCriticalPath(cpBlocks);
    if (latexBtn) latexBtn.onclick = () => exportCriticalPathLatex(cpBlocks);
  }

  function renderCPBlock(blk) {
    const el = h("div", `cp-block cp-kind-${blk.kind}`);
    if (blk.label) el.id = `cp-${blk.label}`;

    const header = h("div", "cp-block-header");
    const statusCls = blk.status || "";
    header.innerHTML = `
      <span class="bk">${esc(blk.kind)}</span>
      ${blk.title ? `<span class="bt">${esc(blk.title)}</span>` : ""}
      ${blk.label ? `<span class="bl">${esc(blk.label)}</span>` : ""}
      ${blk.lean ? `<span class="bh-lean ${statusCls}" title="${esc(blk.lean.decl)}">∀${statusCls ? `<span class="bh-lean-status">${esc(statusCls)}</span>` : ""}</span>` : ""}`;
    el.appendChild(header);

    // Body content
    const body = h("div", "bb", mdToHtml(blk.md || ""));
    el.appendChild(body);

    // Uses links
    if (blk.uses && blk.uses.length) {
      const uses = h("div", "uses", "uses: ");
      for (const ref of blk.uses) {
        const a = h("a", "uref", esc(ref));
        a.href = `#cp-${ref}`;
        a.onclick = (e) => {
          e.preventDefault();
          const t = document.getElementById(`cp-${ref}`);
          if (t) t.scrollIntoView({ behavior: "smooth", block: "start" });
        };
        uses.appendChild(a);
        uses.appendChild(document.createTextNode(" "));
      }
      el.appendChild(uses);
    }

    return el;
  }

  function printCriticalPath(cpBlocks) {
    // Build a standalone print document
    const printWin = window.open("", "_blank");
    if (!printWin) { alert("Pop-up blocked. Please allow pop-ups for this site."); return; }

    const katexCss = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css";
    const katexJs = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js";

    let bodyHtml = `<h1>${esc(paper.title)}</h1>
      <p class="subtitle">Critical Path &mdash; ${cpBlocks.length} blocks</p>
      <p class="meta">${esc((paper.authors || []).join(", "))}${paper.date ? " &middot; " + esc(paper.date) : ""}</p>
      <hr>`;

    let lastChapter = null, lastSection = null;
    for (const blk of cpBlocks) {
      if (blk._chapter !== lastChapter) {
        lastChapter = blk._chapter;
        lastSection = null;
        bodyHtml += `<h2>${blk._chapterNum ? blk._chapterNum + ". " : ""}${esc(blk._chapter)}</h2>`;
      }
      if (blk._section !== lastSection) {
        lastSection = blk._section;
        bodyHtml += `<h3>${esc(blk._section)}</h3>`;
      }
      const kindLabel = blk.kind.charAt(0).toUpperCase() + blk.kind.slice(1);
      bodyHtml += `<div class="block ${blk.kind}">
        <div class="block-header"><strong>${esc(kindLabel)}</strong>${blk.title ? ` (${esc(blk.title)})` : ""}${blk.label ? ` <span class="label">[${esc(blk.label)}]</span>` : ""}</div>
        <div class="block-body">${mdToHtml(blk.md || "")}</div>
      </div>`;
    }

    printWin.document.write(`<!DOCTYPE html><html><head>
      <meta charset="utf-8">
      <title>Critical Path — ${esc(paper.title)}</title>
      <link rel="stylesheet" href="${katexCss}">
      <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
      <style>
        body { font-family: 'Crimson Pro', 'Georgia', serif; max-width: 700px; margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; font-size: 11pt; line-height: 1.6; }
        h1 { font-size: 1.6rem; margin-bottom: .2rem; }
        h2 { font-size: 1.2rem; margin-top: 2rem; border-bottom: 1px solid #ccc; padding-bottom: .3rem; }
        h3 { font-size: 1rem; color: #555; margin-top: 1.2rem; }
        .subtitle { color: #666; font-style: italic; margin: .2rem 0; }
        .meta { color: #888; font-size: .9rem; }
        hr { border: none; border-top: 1px solid #ccc; margin: 1rem 0; }
        .block { margin: 1rem 0; padding: .8rem; border-left: 3px solid #ddd; page-break-inside: avoid; }
        .block.definition { border-left-color: #4a90d9; }
        .block.theorem, .block.proposition { border-left-color: #d94a4a; }
        .block.lemma { border-left-color: #d9974a; }
        .block.corollary { border-left-color: #7b4ad9; }
        .block-header { font-variant: small-caps; margin-bottom: .4rem; }
        .label { font-family: monospace; font-size: .75rem; color: #999; }
        .block-body p { margin: .3rem 0; }
        @media print { body { margin: 0; max-width: 100%; } }
      </style>
      <script src="${katexJs}"><\/script>
    </head><body>${bodyHtml}
      <script>
        document.querySelectorAll('.katex-display-raw').forEach(function(el) {
          try { katex.render(el.dataset.tex, el, { displayMode: true, throwOnError: false, macros: ${JSON.stringify(katexMacros)} }); } catch(e) { el.textContent = el.dataset.tex; }
        });
        document.querySelectorAll('.katex-inline-raw').forEach(function(el) {
          try { katex.render(el.dataset.tex, el, { displayMode: false, throwOnError: false, macros: ${JSON.stringify(katexMacros)} }); } catch(e) { el.textContent = el.dataset.tex; }
        });
        setTimeout(function() { window.print(); }, 500);
      <\/script>
    </body></html>`);
    printWin.document.close();
  }

  function exportCriticalPathLatex(cpBlocks) {
    // Generate LaTeX document
    let tex = `\\documentclass[11pt]{article}
\\usepackage{amsmath,amssymb,amsthm}
\\usepackage[utf8]{inputenc}
\\usepackage{hyperref}

\\newtheorem{theorem}{Theorem}[section]
\\newtheorem{proposition}[theorem]{Proposition}
\\newtheorem{lemma}[theorem]{Lemma}
\\newtheorem{corollary}[theorem]{Corollary}
\\newtheorem{definition}[theorem]{Definition}
\\newtheorem{remark}[theorem]{Remark}
\\newtheorem{example}[theorem]{Example}
\\newtheorem{conjecture}[theorem]{Conjecture}

`;
    // Add paper macros if available
    if (paper.macros) {
      for (const [name, def] of Object.entries(paper.macros)) {
        const d = def;
        if (d.args) {
          tex += `\\newcommand{\\${name}}[${d.args}]{${d.tex}}\n`;
        } else {
          tex += `\\newcommand{\\${name}}{${d.tex}}\n`;
        }
      }
      tex += "\n";
    }

    tex += `\\title{${latexEsc(paper.title)} \\\\ {\\large Critical Path}}
\\author{${latexEsc((paper.authors || []).join(", "))}}
${paper.date ? `\\date{${latexEsc(paper.date)}}` : ""}

\\begin{document}
\\maketitle

`;

    let lastChapter = null, lastSection = null;
    for (const blk of cpBlocks) {
      if (blk._chapter !== lastChapter) {
        lastChapter = blk._chapter;
        lastSection = null;
        tex += `\\section{${latexEsc(blk._chapter)}}\n\n`;
      }
      if (blk._section !== lastSection) {
        lastSection = blk._section;
        tex += `\\subsection{${latexEsc(blk._section)}}\n\n`;
      }
      // Environment mapping
      const envMap = {
        definition: "definition", theorem: "theorem", proposition: "proposition",
        lemma: "lemma", corollary: "corollary", remark: "remark",
        example: "example", conjecture: "conjecture"
      };
      const env = envMap[blk.kind];
      if (env) {
        const titleOpt = blk.title ? `[${latexEsc(blk.title)}]` : "";
        const label = blk.label ? `\\label{${blk.label}}\n` : "";
        tex += `\\begin{${env}}${titleOpt}\n${label}${mdToLatex(blk.md || "")}\n\\end{${env}}\n\n`;
      } else {
        // prose or unknown kind
        tex += `${mdToLatex(blk.md || "")}\n\n`;
      }
    }

    tex += `\\end{document}\n`;

    // Download as .tex file
    const blob = new Blob([tex], { type: "text/x-tex" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `critical-path-${paper.id || "paper"}.tex`;
    a.click();
    URL.revokeObjectURL(url);
  }

  function latexEsc(s) {
    if (!s) return "";
    return s.replace(/\\/g, "\\textbackslash{}")
      .replace(/[&%$#_{}~^]/g, m => "\\" + m);
  }

  function mdToLatex(md) {
    if (!md) return "";
    let out = md;
    // Display math $$...$$ → \[...\]
    out = out.replace(/\$\$([\s\S]*?)\$\$/g, (_, tex) => `\\[\n${tex.trim()}\n\\]`);
    // Inline math stays as $...$
    // Fenced code blocks
    out = out.replace(/```tex\n([\s\S]*?)```/g, (_, code) => code.trim());
    out = out.replace(/```\w*\n([\s\S]*?)```/g, (_, code) => `\\begin{verbatim}\n${code}\\end{verbatim}`);
    // Bold/italic
    out = out.replace(/\*\*(.+?)\*\*/g, "\\textbf{$1}");
    out = out.replace(/\*(.+?)\*/g, "\\emph{$1}");
    // Cross-refs [text](#label) → \hyperref[label]{text}
    out = out.replace(/\[([^\]]+)\]\(#([^)]+)\)/g, "\\hyperref[$2]{$1}");
    return out;
  }

  // ── Boot ────────────────────────────────────────────────
  fetchUser().then(() => {
    loadBranches().then(() => {
      startBranchPolling();
      route();
    });
  });
})();
