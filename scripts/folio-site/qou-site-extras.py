#!/usr/bin/env python3
"""qou-site-extras — per-block QA reports and Lean status on the folio site.

Runs AFTER the platform's `build-folio-site.ts` (folio-assistant-core) and
before `rail-standalone-pages.ts`, on the built tree. It adds, per block:

  * a [QA] badge that opens the block's QA report: every criterion in the
    block's committed `<block>.qa.json` sidecar (Milnor exposition, voice,
    devil's-advocate, proof, canonical, …), latest verdict, reviewer, date,
    notes, and whether the verdict is STALE (its recorded field hash no longer
    matches the current source);
  * a Lean link that is resolved through the block's `lean.ref` as well as its
    sibling `.lean` (the platform draws one only for a sibling), and a GREYED
    "Lean — absent" marker when the kind expects a formalisation and none is
    found;
  * the Lean compile status, from a measured lean-direct sweep
    (`--lean-status <json>`, schema qou-lean-status/v1) — never from the
    sidecar's `proof-lean-compiles`, which is `n/a` on 1078 of 1209 blocks and
    so is not a compile measurement;
  * a "Lean" group in the harness navbar linking the Lean documentation.

Why qou-side: the renderer lives in litlfred/folio-assistant-core, which this
session could not push to. Everything here reads only qou data, so it can move
upstream into build-folio-site.ts unchanged in substance.

    python3 scripts/folio-site/qou-site-extras.py --site <site-dir> \
        [--route cat-harness/folio] [--lean-status lean-status.json] \
        [--lean-docs lean/]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ASSETS = Path(__file__).resolve().parent / "assets"

# Kinds whose block is expected to carry Lean (AGENTS.md "Type system":
# definition required; theorem/lemma/proposition/corollary expected).
LEAN_EXPECTED = {"definition", "theorem", "lemma", "proposition", "corollary"}

LEAN_PACKAGES = {  # lean.ref prefix -> Lake package root (folio-assistant schemas/lean-packages.ts)
    "qou": "folio/quantum-observable-universe/lean",
    "ugb": "folio/unital-groebner-bases/lean",
    "fred2005": "folio/fred2005-formal-groups/lean",
}

# Criterion groups, in display order. First match wins.
GROUPS = [
    ("Milnor exposition", re.compile(r"^(expo-|milnor-)")),
    ("Voice", re.compile(r"^(voice-|trap-)")),
    ("Clarity", re.compile(r"^clarity-")),
    ("Devil's advocate", re.compile(r"^da-")),
    ("Proof / Lean", re.compile(r"^(proof-|lean-|uses-)")),
    ("Canonical / compute", re.compile(r"^(canonical-|compute-|framework-|fit-)")),
    ("Wall / q-usage", re.compile(r"^(wall-|q-usage-)")),
    ("Structure", re.compile(r"^detangler-")),
    ("Bibliography", re.compile(r"^(bib-|cite-)")),
]
BAD = {"fail", "flag", "error", "critical", "major", "warn", "needs-agent"}


def sha12(p: Path) -> str | None:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    except OSError:
        return None


def group_of(cid: str) -> str:
    for name, rx in GROUPS:
        if rx.search(cid):
            return name
    return "Other"


# ── Lean declaration index (full name -> file) ────────────────────────────
DECL_RX = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|unsafe|nonrec)\s+)*"
    r"(?:theorem|lemma|def|structure|class|abbrev|instance|inductive|axiom|opaque)\s+([^\s:({\[]+)"
)
NS_RX = re.compile(r"^\s*namespace\s+(\S+)")
END_RX = re.compile(r"^\s*end\s+(\S+)")


def index_lean(root: Path) -> dict[str, str]:
    idx: dict[str, str] = {}
    for f in root.rglob("*.lean"):
        if ".lake" in f.parts:
            continue
        stack: list[str] = []
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        rel = str(f.relative_to(REPO))
        for ln in lines:
            m = NS_RX.match(ln)
            if m:
                stack.append(m.group(1)); continue
            m = END_RX.match(ln)
            if m and stack and stack[-1] == m.group(1):
                stack.pop(); continue
            m = DECL_RX.match(ln)
            if m:
                n = m.group(1)
                full = n[len("_root_."):] if n.startswith("_root_.") else ".".join(stack + [n])
                idx.setdefault(full, rel)
    return idx


def resolve_ref(ref: str, idx: dict[str, dict[str, str]]) -> str | None:
    if ":" not in ref:
        return None
    pkg, decl = ref.split(":", 1)
    root = LEAN_PACKAGES.get(pkg)
    if not root:
        return None
    hit = idx[pkg].get(decl)
    if hit:
        return hit
    parts = decl.split(".")  # module-path walk, as the pipeline's candidate 2
    for k in range(len(parts), 0, -1):
        f = REPO / root / ("/".join(parts[:k]) + ".lean")
        if f.exists():
            return str(f.relative_to(REPO))
    return None


def has_sorry(path: str) -> bool:
    try:
        src = (REPO / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    src = re.sub(r"/-.*?-/", "", src, flags=re.S)
    src = re.sub(r"--.*", "", src)
    return re.search(r"\bsorry\b", src) is not None


# ── QA sidecar → report ───────────────────────────────────────────────────
def qa_report(md: Path) -> dict | None:
    side = md.with_suffix(".qa.json")
    if not side.exists():
        return None
    try:
        d = json.loads(side.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    cur = {k: sha12(REPO / v) for k, v in (d.get("paths") or {}).items()}
    rows = []
    for cid, hist in (d.get("criteria") or {}).items():
        if not hist:
            continue
        # The MOST RECENT verdict by review time, not by position: writers disagree
        # on whether a new entry goes first or last (the 2026-10-10 Milnor audit
        # put its verdict first, ahead of expired entries).
        e = max(hist, key=lambda h: h.get("reviewed_at") or "")
        fh = e.get("field_hash") or {}
        stale = None
        if fh:
            stale = any(k in cur and cur[k] and v != cur[k] for k, v in fh.items() if k in ("md", "ts", "lean"))
        notes = e.get("notes") or ""
        if "[EXPIRED" in notes:
            stale = True if stale is None else stale
        rv = e.get("reviewer") or {}
        rows.append({
            "id": cid, "group": group_of(cid), "result": e.get("result"),
            "severity": e.get("severity"), "notes": notes[:4000],
            "reviewer": rv.get("kind"), "by": rv.get("agent_skill") or rv.get("id"),
            "model": rv.get("agent_model"), "at": (e.get("reviewed_at") or "")[:10],
            "stale": stale, "history": len(hist),
        })
    order = [g for g, _ in GROUPS] + ["Other"]
    rows.sort(key=lambda r: (order.index(r["group"]), r["id"]))
    counts = {"pass": 0, "bad": 0, "na": 0, "other": 0, "stale": 0}
    for r in rows:
        res = str(r["result"]).lower()
        if res == "pass":
            counts["pass"] += 1
        elif res in BAD:
            counts["bad"] += 1
        elif res in ("n/a", "na", "skip", "skipped"):
            counts["na"] += 1
        else:
            counts["other"] += 1
        if r["stale"]:
            counts["stale"] += 1
    milnor = [r for r in rows if r["group"] == "Milnor exposition"]
    return {
        "label": d.get("label"), "kind": d.get("kind"), "sidecar": str(side.relative_to(REPO)),
        "counts": counts, "criteria": rows,
        "milnor": {r["id"]: r["result"] for r in milnor},
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True)
    ap.add_argument("--route", default="cat-harness/folio")
    ap.add_argument("--lean-status", help="qou-lean-status/v1 JSON from a lean-direct sweep")
    ap.add_argument("--lean-docs", default="lean/",
                    help="Lean documentation path, relative to the publish root (gh-pages root)")
    a = ap.parse_args()

    base = Path(a.site).resolve() / a.route
    if not (base / "papers.json").exists():
        print(f"qou-site-extras: no papers.json under {base}", file=sys.stderr)
        return 2

    status = {}
    status_meta = None
    if a.lean_status and Path(a.lean_status).exists():
        s = json.loads(Path(a.lean_status).read_text())
        status = {**(s.get("library") or {}), **(s.get("files") or {})}
        status_meta = {k: s.get(k) for k in ("measured_at", "qou_commit", "method", "toolchain")}

    idx = {p: index_lean(REPO / r) for p, r in LEAN_PACKAGES.items() if (REPO / r).exists()}

    summaries: dict[Path, dict] = {}
    totals = {"blocks": 0, "qa": 0, "lean_found": 0, "lean_absent": 0, "lean_via_ref": 0}
    papers = json.loads((base / "papers.json").read_text()).get("papers", [])
    for p in papers:
        pdir = base / p["slug"]
        for bj in sorted((pdir / "blocks").rglob("*.json")):
            n = json.loads(bj.read_text())
            src = n.get("source")
            if not src:
                continue
            totals["blocks"] += 1
            md = REPO / src
            rel = bj.relative_to(pdir / "blocks")
            rep = qa_report(md)
            kind = n.get("kind") or ""
            lean_path = n.get("leanSource")
            via = "sibling" if lean_path else None
            if not lean_path and n.get("leanRef"):
                lean_path = resolve_ref(n["leanRef"], idx)
                via = "ref" if lean_path else None
                if lean_path:
                    totals["lean_via_ref"] += 1
            expected = kind in LEAN_EXPECTED or bool(n.get("leanRef"))
            lean = {"expected": expected, "path": lean_path, "via": via, "ref": n.get("leanRef")}
            if lean_path:
                totals["lean_found"] += 1
                lean["sorry"] = has_sorry(lean_path)
                st = status.get(lean_path)
                lean["compiles"] = (st or {}).get("status", "unchecked")
                if st and st.get("error"):
                    lean["error"] = st["error"][:500]
            elif expected:
                totals["lean_absent"] += 1
            out = {"lean": lean, "qa": rep}
            if rep:
                totals["qa"] += 1
            # One small summary per chapter (badge + Lean link, fetched once per page);
            # the full report only when the reader opens it.
            summ = {"lean": lean}
            if rep:
                summ["qa"] = {"counts": rep["counts"], "milnor": rep["milnor"], "kind": rep["kind"]}
            summaries.setdefault(pdir / "qa-summary" / (rel.parts[0] + ".json"), {})[str(rel.with_suffix(""))] = summ
            dst = pdir / "qa" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(json.dumps(out, separators=(",", ":")) + "\n")

    for f, d in summaries.items():
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(d, separators=(",", ":")) + "\n")

    (base / "assets").mkdir(exist_ok=True)
    for f in ("qou-site-extras.js", "qou-site-extras.css"):
        shutil.copy2(ASSETS / f, base / "assets" / f)
    commit = subprocess.run(["git", "rev-parse", "--short=9", "HEAD"], cwd=REPO,
                            capture_output=True, text=True).stdout.strip()
    (base / "assets" / "qou-site-extras.json").write_text(json.dumps({
        "leanDocs": a.lean_docs, "leanStatus": status_meta, "qouCommit": commit,
        "repository": "litlfred/qou",
    }, indent=1) + "\n")

    # Load the extras in every shell, after the platform loader.
    shells = 0
    for html in base.rglob("index.html"):
        t = html.read_text()
        if "qou-site-extras.js" in t or "folio-site.js" not in t:
            continue
        m = re.search(r'<script defer src="([^"]*)assets/folio-site\.js"></script>', t)
        if not m:
            continue
        pre = m.group(1)
        t = t.replace(m.group(0), m.group(0)
                      + f'\n<link rel="stylesheet" href="{pre}assets/qou-site-extras.css">'
                      + f'\n<script defer src="{pre}assets/qou-site-extras.js"></script>')
        html.write_text(t)
        shells += 1
    print(f"qou-site-extras: {totals['blocks']} blocks, {totals['qa']} with a QA sidecar, "
          f"Lean found {totals['lean_found']} ({totals['lean_via_ref']} via lean.ref only), "
          f"expected-but-absent {totals['lean_absent']}; {shells} shells; "
          f"compile status: {'from ' + a.lean_status if status else 'NOT MEASURED (unchecked)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
