// qou-site-extras: per-block QA report + Lean status on the folio site.
// Written by scripts/folio-site/qou-site-extras.py next to the platform loader
// (folio-site.js). It decorates each block's link row (.block-links) after the
// loader draws it, from <paper>/qa/<chapter>/<block>.json.
(() => {
  const body = document.body;
  const root = body.dataset.root || "./";
  const paper = body.dataset.paper;
  if (!paper) return;
  const pbase = `${root}${paper}/`;
  const el = (tag, attrs = {}, text) => {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) if (v !== undefined && v !== null) e.setAttribute(k, v);
    if (text !== undefined) e.textContent = text;
    return e;
  };
  const cfgP = fetch(`${root}assets/qou-site-extras.json`).then((r) => (r.ok ? r.json() : {})).catch(() => ({}));
  const repo = "litlfred/qou";
  const ref = "main";

  // The publish root (gh-pages root): the part of the path before STAGING/<slug>/ if
  // present, else before the route. The Lean docs live at <publish root>/lean/docs/.
  const publishRoot = () => {
    const p = location.pathname;
    const s = p.indexOf("/STAGING/");
    if (s >= 0) return p.slice(0, s + 1);
    const r = p.indexOf("/cat-harness/folio/");
    return r >= 0 ? p.slice(0, r + 1) : "/";
  };

  // ── QA dialog ──
  let dlg = null;
  const dialog = () => {
    if (dlg) return dlg;
    dlg = el("dialog", { class: "qou-qa-dialog", "aria-label": "QA report" });
    document.body.append(dlg);
    dlg.addEventListener("click", (e) => { if (e.target === dlg) dlg.close(); });
    return dlg;
  };
  const resClass = (r) => {
    r = String(r || "").toLowerCase();
    if (r === "pass") return "pass";
    if (["fail", "error", "critical", "major"].includes(r)) return "fail";
    if (["flag", "warn", "needs-agent"].includes(r)) return "flag";
    if (["n/a", "na", "skip", "skipped"].includes(r)) return "na";
    return "other";
  };
  const openQa = (data, title) => {
    const d = dialog();
    d.replaceChildren();
    const head = el("div", { class: "qou-qa-head" });
    head.append(el("h2", {}, `QA report — ${title}`));
    const x = el("button", { type: "button", class: "qou-qa-close", "aria-label": "Close" }, "✕");
    x.onclick = () => d.close();
    head.append(x);
    d.append(head);
    const q = data.qa;
    const lean = data.lean || {};
    const meta = el("p", { class: "qou-qa-meta" });
    if (q) {
      const c = q.counts;
      meta.append(`${q.criteria.length} criteria: ${c.pass} pass, ${c.bad} fail/flag, ${c.na} n/a, ${c.other} other; ${c.stale} stale (source changed since the verdict). Source: `);
      meta.append(el("a", { href: `https://github.com/${repo}/blob/${ref}/${q.sidecar}`, target: "_blank", rel: "noopener" }, q.sidecar));
    } else meta.append("No QA sidecar for this block.");
    d.append(meta);
    // Lean summary
    const lp = el("p", { class: "qou-qa-meta" });
    if (lean.path) {
      lp.append("Lean: ");
      lp.append(el("a", { href: `https://github.com/${repo}/blob/${ref}/${lean.path}`, target: "_blank", rel: "noopener" }, lean.path));
      lp.append(` (${lean.via === "ref" ? "via lean.ref " + lean.ref : "sibling"}; ${lean.sorry ? "contains sorry" : "no sorry"}; build: ${lean.compiles || "unchecked"})`);
      if (lean.error) lp.append(el("code", { class: "qou-qa-err" }, lean.error));
    } else lp.append(lean.expected ? `Lean: expected for this kind${lean.ref ? " (lean.ref " + lean.ref + ")" : ""}, none found.` : "Lean: not expected for this kind.");
    d.append(lp);
    if (q) {
      let group = null, tb = null;
      for (const r of q.criteria) {
        if (r.group !== group) {
          group = r.group;
          const det = el("details", { class: "qou-qa-group" + (group === "Milnor exposition" ? " milnor" : "") });
          if (group === "Milnor exposition" || q.criteria.some((z) => z.group === group && ["fail", "flag"].includes(resClass(z.result)))) det.open = true;
          const n = q.criteria.filter((z) => z.group === group);
          const bad = n.filter((z) => ["fail", "flag"].includes(resClass(z.result))).length;
          det.append(el("summary", {}, `${group} — ${n.length} criteria${bad ? `, ${bad} not passing` : ""}`));
          tb = el("table");
          tb.append(Object.assign(el("tr"), { innerHTML: "<th>criterion</th><th>result</th><th>reviewer</th><th>date</th><th>notes</th>" }));
          det.append(tb);
          d.append(det);
        }
        const tr = el("tr");
        tr.append(el("td", {}, r.id));
        const rc = el("td", { class: `res res-${resClass(r.result)}` }, String(r.result ?? "—") + (r.stale ? " (stale)" : ""));
        tr.append(rc);
        tr.append(el("td", {}, [r.reviewer, r.by, r.model].filter(Boolean).join(" · ")));
        tr.append(el("td", {}, r.at || ""));
        const nt = el("td", { class: "notes" });
        if (r.notes) { const det = el("details"); det.append(el("summary", {}, r.notes.slice(0, 90) + (r.notes.length > 90 ? "…" : ""))); det.append(el("div", {}, r.notes)); nt.append(det); }
        tr.append(nt);
        tb.append(tr);
      }
    }
    d.showModal();
  };

  // ── Decorate each block's link row ──
  const done = new WeakSet();
  const decorate = async (row) => {
    if (done.has(row)) return;
    done.add(row);
    const src = row.dataset.src || "";
    const m = src.match(/^folio\/[^/]+\/(.+)\.md$/);
    if (!m) return;
    let data;
    try { const r = await fetch(`${pbase}qa/${m[1]}.json`); if (!r.ok) return; data = await r.json(); } catch { return; }
    const title = row.dataset.sec || row.dataset.block || src;
    // Lean: replace the platform's sibling-only link with the resolved one.
    row.querySelectorAll('a[data-fa-link="source"]').forEach((a) => a.remove());
    const L = data.lean || {};
    if (L.path) {
      const st = L.compiles === "pass" ? "builds" : L.compiles === "fail" ? "build fails" : L.compiles === "unverifiable" ? "build unverifiable" : "build unchecked";
      const glyph = L.compiles === "pass" ? "✓" : L.compiles === "fail" ? "✗" : "?";
      const a = el("a", {
        href: `https://github.com/${repo}/blob/${ref}/${L.path}`, target: "_blank", rel: "noopener",
        class: `qou-lean lean-${L.sorry ? "sorry" : "proved"} build-${L.compiles || "unchecked"}`,
        title: `Lean: ${L.path}${L.via === "ref" ? " (via lean.ref " + L.ref + ")" : ""} — ${L.sorry ? "contains sorry" : "no sorry"}; ${st}${L.error ? "\n" + L.error : ""}`,
      });
      a.textContent = `Lean ${L.sorry ? "◐" : "✓"} · ${glyph} ${st}`;
      row.append(a);
    } else if (L.expected) {
      row.append(el("span", { class: "qou-lean lean-absent", "aria-disabled": "true",
        title: `A ${data.qa?.kind || "block"} of this kind is expected to carry Lean${L.ref ? " (lean.ref " + L.ref + " does not resolve)" : ""}; none found.` }, "Lean — absent"));
    }
    // QA badge.
    const q = data.qa;
    const b = el("a", { href: "#", class: "qou-qa-badge", role: "button", title: "Open this block's QA report" });
    if (q) {
      const c = q.counts;
      const mil = Object.values(q.milnor || {});
      const milTxt = mil.length ? (mil.every((r) => r === "pass") ? " · Milnor ✓" : ` · Milnor ${mil.filter((r) => r !== "pass").length}✗`) : "";
      b.textContent = `QA ${c.pass}✓${c.bad ? " " + c.bad + "✗" : ""}${milTxt}`;
      if (c.bad) b.classList.add("has-bad");
      if (mil.some((r) => r !== "pass")) b.classList.add("milnor-bad");
    } else { b.textContent = "QA —"; b.classList.add("none"); }
    b.addEventListener("click", (e) => { e.preventDefault(); openQa(data, title); });
    row.prepend(b);
  };
  const scan = (n) => (n.querySelectorAll ? n.querySelectorAll(".block-links[data-src]") : []).forEach(decorate);
  new MutationObserver((recs) => { for (const r of recs) r.addedNodes.forEach((n) => { if (n.nodeType === 1) { if (n.matches?.(".block-links[data-src]")) decorate(n); scan(n); } }); })
    .observe(document.body, { childList: true, subtree: true });
  document.addEventListener("DOMContentLoaded", () => scan(document));

  // ── "Lean" group in the harness navbar (or under the contents without the harness) ──
  const addNav = async () => {
    const cfg = await cfgP;
    const docs = publishRoot() + (cfg.leanDocs || "lean/docs/");
    const links = [
      ["Lean API documentation", docs + "QOU.html"],
      ["Lean library sources", `https://github.com/${repo}/tree/${ref}/folio/quantum-observable-universe/lean/QOU`],
    ];
    const graphs = document.querySelector("nav.fa-nav .fa-nav-graphs");
    if (graphs) {
      if (graphs.querySelector(".qou-lean-nav")) return true;
      const g = el("details", { class: "fa-nav-group qou-lean-nav", open: "" });
      const s = el("summary");
      s.append(el("span", { class: "fa-nav-glyph", "aria-hidden": "true" }, "∀"), el("span", { class: "fa-nav-label" }, "Lean"));
      const sub = el("div", { class: "fa-nav-sub" });
      const ul = el("ul");
      for (const [t, h] of links) { const li = el("li"); li.append(el("a", { href: h }, t)); ul.append(li); }
      sub.append(ul); g.append(s, sub);
      const contents = graphs.querySelector(".folio-contents");
      if (contents) contents.after(g); else graphs.prepend(g);
      return true;
    }
    return false;
  };
  const navTry = () => addNav().then((ok) => {
    if (ok) return;
    const nav = document.querySelector("nav.fa-nav");
    if (nav) { const mo = new MutationObserver(() => addNav().then((k) => k && mo.disconnect())); mo.observe(nav, { childList: true, subtree: true }); setTimeout(() => mo.disconnect(), 10000); }
    else {
      const toc = document.getElementById("toc");
      if (toc && !toc.querySelector(".qou-lean-nav")) cfgP.then((cfg) => {
        const p = el("p", { class: "qou-lean-nav" }); p.append(el("a", { href: publishRoot() + (cfg.leanDocs || "lean/docs/") + "QOU.html" }, "∀ Lean API documentation")); toc.append(p);
      });
    }
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", navTry); else navTry();
  setTimeout(navTry, 1500);
})();
