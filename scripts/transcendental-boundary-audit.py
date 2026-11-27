#!/usr/bin/env python3
"""Transcendental boundary audit (owner ruling 2026-11-27, bean qou-dk7p).

Every transcendental or analytic result lives in one isolated Lean subgraph,
`QOU/Transcendental/`. Outside it, a transcendental quantity may appear only as
a symbol in a ring together with its cut. This script lists the Lean modules
outside the boundary that still use a transcendental or analytic API (comments
and docstrings are stripped first).

Modes
  (default)      print counts by class and by directory
  --write        write the baseline (drain-only ratchet) to the JSON file
  --report PATH  write a markdown QA report (classes, directories, import taint)
  --check        exit 1 if a module NOT in the baseline uses the API, or if the
                 baseline lists a module that no longer does (shrink it)

The baseline only shrinks. Never add a file to it by hand to get past --check:
move the result behind the boundary instead (strangler pattern).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAN = ROOT / "folio/quantum-observable-universe/lean"
BOUNDARY = "QOU/Transcendental/"
BASELINE = ROOT / "docs/audits/transcendental-boundary-baseline.json"

CLASSES = {
    "transcendental-function": r"\bReal\.(exp|log|pi|cos|sin|tan|arctan|arcsin|arccos|cosh|sinh|tanh|Gamma|logb)\b"
        r"|\bComplex\.(exp|log|cos|sin|cpow)\b|\bReal\.rpow\b|\bdilog\b|\bClausen\b|\bLobachevsky\b",
    "real-completion": r"\bReal\.sqrt\b|\bNNReal\.sqrt\b|\bReal\.sSup\b|\bReal\.sInf\b|\bReal\.iSup\b|\bReal\.iInf\b|\bReal\.exists_isLUB\b|√",
    "analysis": r"\bintervalIntegral\b|\bMeasureTheory\b|∫|\bHasDerivAt\b|\bderiv\b|\bFilter\.Tendsto\b|\bTendsto\b"
        r"|\bContinuous\b|\bDifferentiable\b|\bHasSum\b|\btsum\b",
}
RX = {k: re.compile(v) for k, v in CLASSES.items()}
# A bare `π` is Real.pi only under `open Real` / `open scoped Real`; elsewhere it is an
# ordinary bound name (a permutation, an epimorphism, ...) and must not be counted.
OPEN_REAL = re.compile(r"^\s*open\b[^\n]*\bReal\b", re.M)
BARE_PI = re.compile(r"(?<![\w.])π(?![\w])")

def strip_comments(src: str) -> str:
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and src.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            i += 1; continue
        if src.startswith("--", i):
            j = src.find("\n", i); i = n if j < 0 else j; continue
        if src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append('""'); i = j + 1; continue
        out.append(src[i]); i += 1
    return "".join(out)

def scan():
    hits = {}
    for p in sorted(LEAN.rglob("*.lean")):
        rel = p.relative_to(LEAN).as_posix()
        if rel.startswith(".lake/") or rel.startswith(BOUNDARY):
            continue
        code = strip_comments(p.read_text(encoding="utf-8", errors="replace"))
        cls = {k for k, rx in RX.items() if rx.search(code)}
        if OPEN_REAL.search(code) and BARE_PI.search(code):
            cls.add("transcendental-function")
        cls = sorted(cls)
        if cls:
            hits[rel] = cls
    return hits

IMPORT_RX = re.compile(r"^import\s+([\w.]+)", re.M)

def graph():
    mods, imps = {}, {}
    for p in sorted(LEAN.rglob("*.lean")):
        rel = p.relative_to(LEAN).as_posix()
        if rel.startswith(".lake/"):
            continue
        name = rel[:-5].replace("/", ".")
        mods[name] = rel
        imps[name] = IMPORT_RX.findall(p.read_text(encoding="utf-8", errors="replace"))
    return mods, imps

def report(path, hits):
    mods, imps = graph()
    trans = {n for n, r in mods.items() if r in hits}
    tainted, memo = {}, {}
    def via(n, stack=()):
        if n in memo: return memo[n]
        memo[n] = None
        for i in imps.get(n, []):
            if i not in mods or i in stack: continue
            if i in trans: memo[n] = i; return i
            w = via(i, stack + (n,))
            if w: memo[n] = w; return w
        return memo[n]
    clean = [n for n in mods if n not in trans]
    for n in clean:
        w = via(n)
        if w: tainted[n] = w
    pure = [n for n in clean if n not in tainted]
    indeg = {}
    for n in clean:
        for i in imps[n]:
            if i in trans: indeg[i] = indeg.get(i, 0) + 1
    by_cls = {k: sum(1 for v in hits.values() if k in v) for k in CLASSES}
    dirs = {}
    for f in hits:
        d = f.rsplit("/", 1)[0] if "/" in f else "."
        dirs[d] = dirs.get(d, 0) + 1
    L = ["# Transcendental and analytic boundary: QA report", "",
         "Owner ruling 2026-11-27 (bean `qou-dk7p`): every transcendental or analytic result lives in one",
         f"isolated subgraph, `{BOUNDARY}`, and the rest of the corpus stays algebraic. A transcendental",
         "quantity may appear outside the boundary only as a symbol in a ring together with its cut.",
         "Generated by `scripts/transcendental-boundary-audit.py --report`; comments and docstrings are",
         "stripped before matching. This is a measurement, not a verdict on any one file.", "",
         "## Summary", "", "| quantity | count |", "|---|---:|",
         f"| Lean modules (paper package tree) | {len(mods)} |",
         f"| inside the boundary `{BOUNDARY}` | {sum(1 for r in mods.values() if r.startswith(BOUNDARY))} |",
         f"| outside, using a transcendental/analytic API directly | {len(trans)} |",
         f"| outside, algebraic but importing one transitively (tainted) | {len(tainted)} |",
         f"| outside, algebraic and import-clean (pure) | {len(pure)} |", "",
         "## Direct use by class", "", "| class | modules | matched API |", "|---|---:|---|"]
    for k, v in by_cls.items():
        L.append(f"| {k} | {v} | `{CLASSES[k][:90]}…` |")
    L += ["", f"Modules whose only use is `real-completion` (`Real.sqrt`, `sSup`, …): "
          f"{sum(1 for v in hits.values() if v == ['real-completion'])}. These are the cheapest to move:",
          "`Real.sqrt` of an algebraic number is algebraic, so most of them can become a root in an",
          "algebraic extension.", "", "## Direct use by directory", "", "| directory | modules |", "|---|---:|"]
    for d, c in sorted(dirs.items(), key=lambda x: -x[1])[:25]:
        L.append(f"| `{d}` | {c} |")
    L += ["", "## Strangler targets: transcendental modules most imported by algebraic ones", "",
          "Moving one of these behind the boundary, or splitting its algebraic part out, frees the most",
          "algebraic modules.", "", "| module | algebraic importers |", "|---|---:|"]
    for n, c in sorted(indeg.items(), key=lambda x: -x[1])[:25]:
        L.append(f"| `{n}` | {c} |")
    L += ["", "## Gate", "", "`--check` against `docs/audits/transcendental-boundary-baseline.json` fails when a",
          "module outside the boundary starts using a transcendental/analytic API (NEW), or when a",
          "baseline entry has become clean and should be dropped (GONE). The baseline only shrinks.", ""]
    Path(path).write_text("\n".join(L))
    print(f"wrote {path}: direct {len(trans)}, tainted {len(tainted)}, pure {len(pure)}")

def main():
    hits = scan()
    if "--report" in sys.argv:
        report(sys.argv[sys.argv.index("--report") + 1], hits)
        return 0
    total = sum(1 for p in LEAN.rglob("*.lean") if not p.relative_to(LEAN).as_posix().startswith(".lake/"))
    if "--write" in sys.argv:
        BASELINE.parent.mkdir(parents=True, exist_ok=True)
        BASELINE.write_text(json.dumps({"schema": "transcendental-boundary/v1", "boundary": BOUNDARY,
                                        "modules": hits}, indent=1, ensure_ascii=False) + "\n")
        print(f"wrote {len(hits)} modules to {BASELINE.relative_to(ROOT)}")
        return 0
    if "--check" in sys.argv:
        base = json.loads(BASELINE.read_text())["modules"]
        new = sorted(set(hits) - set(base))
        gone = sorted(set(base) - set(hits))
        for f in new: print(f"NEW  {f}  {hits[f]}")
        for f in gone: print(f"GONE {f}  (drop it from the baseline: it is now clean)")
        print(f"outside boundary: {len(hits)} (baseline {len(base)}), new {len(new)}, gone {len(gone)}")
        return 1 if (new or gone) else 0
    by_cls = {k: sum(1 for v in hits.values() if k in v) for k in CLASSES}
    print(f"Lean modules: {total}; outside boundary using transcendental/analytic API: {len(hits)}")
    for k, v in by_cls.items(): print(f"  {k}: {v}")
    only_sqrt = sum(1 for v in hits.values() if v == ["real-completion"])
    print(f"  (real-completion only: {only_sqrt})")
    dirs = {}
    for f in hits: dirs[f.rsplit('/', 1)[0] if '/' in f else '.'] = dirs.get(f.rsplit('/', 1)[0] if '/' in f else '.', 0) + 1
    for d, c in sorted(dirs.items(), key=lambda x: -x[1])[:15]: print(f"  {c:5d} {d}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
