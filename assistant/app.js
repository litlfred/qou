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
  let mode = "read";      // "read" | "qc"
  let blockIndex = {};    // label → ResolvedBlock (for cross-ref lookup)

  const app = $("#app");
  const navLinks = $("#nav-links");

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
      const data = await api("/api/folio");
      folio = data.papers || [];
      renderFolio(data.title, folio);
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
      const data = await api(`/api/paper?id=${encodeURIComponent(id)}`);
      paper = data;
      buildBlockIndex();
      if (mode === "qc") renderQC(); else renderPaper();
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
        secEl.onclick = () => {
          const target = document.getElementById(sec.label || "");
          if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
        };
        secList.appendChild(secEl);
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
    bh.innerHTML = `
      <span class="bk">${esc(blk.kind)}</span>
      ${blk.title ? `<span class="bt">${esc(blk.title)}</span>` : ""}
      ${blk.label ? `<span class="bl">${esc(blk.label)}</span>` : ""}`;
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

    // lean badge
    if (blk.lean) {
      const cls = blk.status || blk.lean.validation || "";
      el.appendChild(h("div", `lb ${cls}`,
        `<span class="vi ${blk.lean.validation || ""}"></span> ${esc(blk.lean.decl)} ${cls ? `(${cls})` : ""}`));
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
      for (const td of blk.todos) list.appendChild(renderTodoItem(td));
      badge.onclick = () => list.classList.toggle("open");
      el.appendChild(badge);
      el.appendChild(list);
    }

    return el;
  }

  function renderTodoItem(td) {
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
        history.prepend(renderTodoItem(data.todo));
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
  function renderMath(root) {
    if (!window.katex) return;
    root.querySelectorAll(".katex-display-raw").forEach(el => {
      try {
        katex.render(el.dataset.tex, el, { displayMode: true, throwOnError: false });
      } catch (_) { el.textContent = el.dataset.tex; }
    });
    root.querySelectorAll(".katex-inline-raw").forEach(el => {
      try {
        katex.render(el.dataset.tex, el, { displayMode: false, throwOnError: false });
      } catch (_) { el.textContent = el.dataset.tex; }
    });
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
  route();
})();
