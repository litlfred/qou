// QOU Assistant — Single-Page Application
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
  let currentBranch = null;   // HEAD branch on server
  let selectedBranch = null;  // branch the user is viewing (null = current)
  let diffData = null;        // PaperDiff from /api/diff

  const app = $("#app");
  const navLinks = $("#nav-links");
  const branchSelect = $("#c-br");
  const diffBtn = $("#c-diff");

  // ── Theme / font toggles ────────────────────────────────
  $("#c-th").onclick = () => {
    const t = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = t;
    $("#c-th").textContent = t === "dark" ? "light" : "dark";
    localStorage.setItem("qou-theme", t);
  };
  $("#c-fn").onclick = () => {
    const f = document.body.dataset.font === "paper" ? "web" : "paper";
    document.body.dataset.font = f;
    $("#c-fn").textContent = f === "paper" ? "web" : "paper";
    localStorage.setItem("qou-font", f);
  };
  // restore saved prefs
  const savedTheme = localStorage.getItem("qou-theme");
  if (savedTheme) {
    document.documentElement.dataset.theme = savedTheme;
    $("#c-th").textContent = savedTheme === "dark" ? "light" : "dark";
  }
  const savedFont = localStorage.getItem("qou-font");
  if (savedFont) {
    document.body.dataset.font = savedFont;
    $("#c-fn").textContent = savedFont === "paper" ? "web" : "paper";
  }

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
  function route() {
    const hash = location.hash || "#/";
    const parts = hash.slice(2).split("/").filter(Boolean);

    if (parts[0] === "paper" && parts[1]) {
      loadPaper(parts[1]);
    } else {
      loadFolio();
    }
  }
  window.addEventListener("hashchange", route);

  // ── API helpers ─────────────────────────────────────────
  async function api(path) {
    const r = await fetch(path);
    if (!r.ok) throw new Error(`${r.status} ${r.statusText}`);
    return r.json();
  }

  // ── Folio (landing page) ────────────────────────────────
  async function loadFolio() {
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
    app.innerHTML = '<div class="loading">loading paper...</div>';
    try {
      const data = await api(branchQuery(`/api/paper?id=${encodeURIComponent(id)}`));
      paper = data;
      katexMacros = buildKatexMacros(data.macros);
      buildBlockIndex();
      updateReadOnlyBanner();
      if (mode === "diff") await loadDiff();
      else if (mode === "qc") renderQC();
      else renderPaper();
    } catch (e) {
      app.innerHTML = `<div class="err">${esc(e.message)}</div>`;
    }
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
      readLink.onclick = (e) => { e.preventDefault(); mode = "read"; renderPaper(); };
      navLinks.appendChild(readLink);

      const qcLink = h("a", mode === "qc" ? "active" : "", "qc");
      qcLink.href = "#";
      qcLink.onclick = (e) => { e.preventDefault(); mode = "qc"; renderQC(); };
      navLinks.appendChild(qcLink);

      if (selectedBranch && selectedBranch !== "main" && selectedBranch !== "master") {
        const diffLink = h("a", mode === "diff" ? "active" : "", "diff");
        diffLink.href = "#";
        diffLink.onclick = async (e) => { e.preventDefault(); mode = "diff"; await loadDiff(); };
        navLinks.appendChild(diffLink);
      }
    }
  }

  // ── Paper: read mode ────────────────────────────────────
  function renderPaper() {
    updateNav();
    const wrap = h("div", "paper-layout");

    // sidebar
    const sb = h("aside", "sidebar");
    const sbHead = h("div", "sidebar-header", esc(paper.title));
    sb.appendChild(sbHead);
    for (const ch of paper.chapters || []) {
      const chEl = h("div", "sb-ch", `<span class="arrow">&#9654;</span> ${esc(ch.title)}`);
      const secList = h("div", "sb-secs");
      for (const sec of ch.sections || []) {
        const secEl = h("div", "sb-sec", esc(sec.title));
        if (sec.label) secEl.dataset.sbLabel = sec.label;
        secEl.onclick = () => {
          const target = document.getElementById(sec.label || "");
          if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
        };
        secList.appendChild(secEl);

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
          secList.appendChild(blkEl);
        }
      }
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

    // chapters
    for (const ch of paper.chapters || []) {
      content.appendChild(renderChapter(ch));
    }
    wrap.appendChild(content);

    app.innerHTML = "";
    app.appendChild(wrap);
    renderMath(app);
    observeVisibleBlocks(sb);
  }

  function renderChapter(ch) {
    const el = h("div", "ch");
    el.innerHTML = `<h2 class="ch-t"><span class="n">${ch.number}.</span> ${esc(ch.title)}</h2>`;
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
      el.innerHTML = `<div class="bb">${mdToHtml(blk.md || "")}</div>`;
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

    // action bar
    const actions = h("div", "blk-actions");
    const srcBtn = h("button", "blk-act", "src");
    srcBtn.title = "Toggle source";
    actions.appendChild(srcBtn);
    const fbBtn = h("button", "blk-act", "fb");
    fbBtn.title = "Send feedback";
    fbBtn.onclick = () => openFeedback(blk);
    actions.appendChild(fbBtn);
    el.appendChild(actions);

    // body
    const bb = h("div", "bb", mdToHtml(blk.md || ""));
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
        ${td.priority ? td.priority : ""}
        ${td.assignee ? " &middot; " + esc(td.assignee) : ""}
        ${td.createdAt ? " &middot; " + esc(td.createdAt.slice(0, 10)) : ""}
      </div>`;

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
    updateNav();
    app.innerHTML = '<div class="loading">computing diff...</div>';
    try {
      const base = "main";
      const head = selectedBranch || currentBranch;
      const data = await api(`/api/diff?id=${encodeURIComponent(paper.id)}&base=${encodeURIComponent(base)}&head=${encodeURIComponent(head)}`);
      diffData = data;
      renderDiff();
    } catch (e) {
      app.innerHTML = `<div class="err">${esc(e.message)}</div>`;
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
  function mdToHtml(md) {
    let out = md;
    // display math $$...$$
    out = out.replace(/\$\$([\s\S]*?)\$\$/g, (_, tex) =>
      `<span class="katex-display-raw" data-tex="${escAttr(tex.trim())}"></span>`);
    // inline math $...$
    out = out.replace(/\$([^\n$]+?)\$/g, (_, tex) =>
      `<span class="katex-inline-raw" data-tex="${escAttr(tex.trim())}"></span>`);
    // fenced code blocks
    out = out.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => {
      if (lang === "tex" || lang === "latex") {
        return `<div class="txb ph">${esc(code.trim())}</div>`;
      }
      return `<pre style="background:var(--bg-r);padding:.6rem;border-radius:4px;overflow-x:auto;font-size:.8rem"><code>${esc(code)}</code></pre>`;
    });
    // bold, italic
    out = out.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    out = out.replace(/\*(.+?)\*/g, "<em>$1</em>");
    // cross-refs [text](#label)
    out = out.replace(/\[([^\]]+)\]\(#([^)]+)\)/g,
      '<a class="uref" href="#$2" onclick="event.preventDefault();document.getElementById(\'$2\')?.scrollIntoView({behavior:\'smooth\',block:\'start\'})">$1</a>');
    // paragraphs
    out = out.replace(/\n{2,}/g, "</p><p>");
    out = "<p>" + out + "</p>";
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

  // ── Boot ────────────────────────────────────────────────
  loadBranches().then(() => {
    startBranchPolling();
    route();
  });
})();
