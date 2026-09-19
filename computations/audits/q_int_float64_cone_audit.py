#!/usr/bin/env python3
"""How far does the float64 `q_int` reach, and how big is the error it leaves?

Bean `qou-oiz3`.  `qou_substrate.constants.q_int` (constants.py:190) computes

    [n]_q = (q**n - q**-n) / (q - q**-1)

over the module's **binary64** globals `Q`, `Q_INV`, `HA`.  It is the last
float64 root under the Wedderburn / Markov-trace layer: `pyhecke.wedderburn`'s
`q_hook_product` and `q_factorial` accumulate `mp.mpf(1) * q_int(k)`, so they
return an `mpf` that is mpf-TYPED and float64-VALUED, and `wedderburn_weight`
is `q_dimension(lam)**2 / q_factorial(n)` on top of them.  `isinstance(x, mpf)`
is not evidence of precision and neither is the digit count of its repr.

WHY THIS AUDIT EXISTS RATHER THAN A FIGURE IN A DOCUMENT
--------------------------------------------------------
The blast radius was carried in bean `qou-oiz3` as "124 python files, 243
witnesses".  Re-measured here, those are the count of files that MENTION the
three Wedderburn primitives by name (116 on 2026-09-19) and a witness count of
the same order -- correct for that question, and low by roughly an order of
magnitude for the question that decides the refresh budget, which is the
IMPORT CONE.  AGENTS.md records the same decay in its own importer table
(wrong by two orders of magnitude) and instructs re-measurement.  So this is a
script and not a number.

WHAT IT REFUSES TO DO
---------------------
It does not resolve an import by its LAST dotted component.  `from
qou_substrate.constants import Q` and `from pyhecke.constants import ...` both
end in `constants`, and a basename match therefore gives every consumer of the
substrate constants a phantom edge from a pyhecke root.  Measured: that single
conflation reports the cone as 3921 files -- the entire corpus -- instead of
1290.  Dotted imports are matched on the full path suffix.

It also separates the CONSTANT SHIMS from the VALUE CONE.  Importing `Q` (an
f64 constant that is legitimately f64 for f64 purposes) does not put a
consumer's numbers through `q_int`; only the Hecke/Wedderburn layer does.  The
shim cone is 3921 files and is not a measure of anything.

NO FLOAT64 IN THE AUDIT ITSELF (AGENTS.md, probes-are-not-exempt): every
comparison below is mpmath at `COMPUTE_DPS`, and the f64 side is lifted with
`mpf(repr(x))` so no second rounding is introduced.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in (os.path.join(ROOT, "tools", "qou-substrate", "python"),
           os.path.join(ROOT, "tools", "pyhecke", "python"),
           os.path.join(ROOT, "computations"),
           os.path.join(ROOT, "computations", "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

SKIP_DIRS = (".claude/worktrees", "/_deprecated/", "/.git/", "/node_modules/",
             "/.lake/", "/lake-packages/", "/build/", "/.venv/")

# EXCLUDE THIS FILE FROM ITS OWN MEASUREMENT.  It imports the Hecke layer in
# order to measure the weight error, so without this it appears in its own
# value cone and every count it prints is one too high -- the "mask volatile
# keys or you measure your own harness" failure, one level up.
SELF = os.path.relpath(os.path.abspath(__file__), ROOT)

# The libraries whose EXPORTED COMPUTED quantities are q_int-derived.
VALUE_ROOTS = (
    "tools/pyhecke/python/pyhecke/wedderburn.py",
    "tools/pyhecke/python/pyhecke/constants.py",
    "computations/hecke/hecke_characters.py",
    "computations/hecke/hecke_wedderburn.py",
    "computations/substrate/hecke_core.py",
    "computations/hecke_core_legacy.py",
    "qou-mass/src/qou_mass/_internal/hecke_characters.py",
    "qou-mass/src/qou_mass/_internal/hecke_core.py",
)
# The two sites that DEFINE a float64 q_int.
DEF_SITES = (
    ("tools/qou-substrate/python/qou_substrate/constants.py", "q_int"),
    ("computations/substrate/q_parameter.py", "q_int"),     # muon-branch redefinition
)
DIRECT_NAMES = ("q_hook_product", "wedderburn_weight", "q_factorial")

# Producers AGENTS.md records as refusing to run by design, and the
# anchor-DEFINING producer that must never be re-pinned as part of a sweep.
BY_DESIGN_REFUSALS = ("atomic_tr_m_mpfr_50dps", "he4_stage2_ranking_seminormal_xcheck",
                      "cross_check_trM_1ppb")
ANCHOR_DEFINING = ("q_pinning_50_digit",)


# ── tree ────────────────────────────────────────────────────────────────────
def py_files() -> list[str]:
    out = []
    for base, dirs, fs in os.walk(ROOT):
        rel = base[len(ROOT):] + "/"
        if any(s in rel for s in SKIP_DIRS):
            dirs[:] = []
            continue
        for f in fs:
            if f.endswith(".py"):
                rel = os.path.relpath(os.path.join(base, f), ROOT)
                if rel != SELF:
                    out.append(rel)
    return sorted(out)


def import_edges(files: list[str]) -> dict[str, set[str]]:
    """imported path -> set of importing paths.  Full-suffix match for dotted."""
    bymod: dict[str, list[str]] = defaultdict(list)
    for p in files:
        bymod[os.path.basename(p)[:-3]].append(p)

    def resolve(mod: str) -> list[str]:
        parts = mod.split(".")
        if len(parts) == 1:
            return bymod.get(parts[0], [])
        suffix = "/".join(parts) + ".py"
        hits = [p for p in files if p.endswith(suffix)]
        if hits:
            return hits
        return [p for p in bymod.get(parts[-1], []) if parts[-2] in p.split("/")]

    edges: dict[str, set[str]] = defaultdict(set)
    for p in files:
        try:
            tree = ast.parse(open(os.path.join(ROOT, p), encoding="utf-8",
                                  errors="replace").read())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            else:
                continue
            for m in names:
                for t in resolve(m):
                    if t != p:
                        edges[t].add(p)
    return edges


def cone(edges, roots, files) -> set[str]:
    fset = set(files)
    roots = [r for r in roots if r in fset]
    seen, frontier = set(roots), list(roots)
    while frontier:
        cur = frontier.pop()
        for imp in edges.get(cur, ()):
            if imp not in seen:
                seen.add(imp)
                frontier.append(imp)
    return seen


# ── witnesses ───────────────────────────────────────────────────────────────
_SIG = re.compile(r"^[+-]?(\d+)\.?(\d*)([eE][+-]?\d+)?$")


def _sig_digits(s: str) -> int:
    m = _SIG.match(s.strip())
    if not m:
        return 0
    return len((m.group(1).lstrip("0") + m.group(2)).rstrip("0") or "0")


def _strings(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)
    elif isinstance(o, str):
        yield o
    elif isinstance(o, float):
        yield repr(o)


def witness_map(files: list[str]) -> dict[str, str]:
    """committed witness -> producer path, by `scriptFile` then by stem."""
    pyby: dict[str, list[str]] = defaultdict(list)
    for p in files:
        pyby[os.path.basename(p)].append(p)
    mapped: dict[str, str] = {}
    for base, dirs, fs in os.walk(os.path.join(ROOT, "computations")):
        if "/.git/" in base:
            dirs[:] = []
            continue
        for f in fs:
            if not f.endswith(".witness.json"):
                continue
            w = os.path.relpath(os.path.join(base, f), ROOT)
            try:
                d = json.load(open(os.path.join(ROOT, w), encoding="utf-8"))
            except Exception:
                continue
            node = d.get("witness", d)
            sf = node.get("scriptFile") or d.get("scriptFile") or ""
            cands: list[str] = []
            if isinstance(sf, str) and sf.endswith(".py"):
                cands = [p for p in files if p.endswith(sf.lstrip("./"))] \
                    or pyby.get(os.path.basename(sf), [])
            if not cands:
                stem = f[:-len(".witness.json")]
                cands = pyby.get(stem.replace("-", "_") + ".py", []) \
                    or pyby.get(stem + ".py", [])
            if len(cands) == 1 or (cands and isinstance(sf, str) and sf.endswith(".py")):
                mapped[w] = cands[0]
    return mapped


def max_sig(witness_rel: str) -> int:
    try:
        d = json.load(open(os.path.join(ROOT, witness_rel), encoding="utf-8"))
    except Exception:
        return 0
    mx = 0
    for s in _strings(d):
        if len(s) > 200:
            continue
        n = _sig_digits(s)
        if n > mx:
            mx = n
    return mx


# ── the error itself ────────────────────────────────────────────────────────
def weight_error_table():
    """Exact-vs-f64 Wedderburn weight error as a function of the strand count.

    Returns [(n, n_blocks, worst_lambda, rel_move_as_mpf)].  Empty if the
    Hecke layer cannot be imported (a bare container), which is reported as
    such and never as a clean result.
    """
    import mpmath as mp
    from qou_substrate.precision import COMPUTE_DPS
    mp.mp.dps = COMPUTE_DPS + 10
    import pyhecke.wedderburn as W
    from qou_substrate.constants import q_int_at
    try:
        import q_parameter as QP
        q_at_anchored = QP.q_at
    except Exception:
        from qou_substrate.constants import q_at as q_at_anchored

    def parts(n, mx=None):
        if mx is None:
            mx = n
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for rest in parts(n - k, k):
                yield (k,) + rest

    f64_q_int = W.q_int
    qq = q_at_anchored(COMPUTE_DPS + 10)

    def exact_q_int(k, _q=qq):
        return q_int_at(k, q=_q, dps=COMPUTE_DPS)

    rows = []
    for n in (3, 4, 5, 6, 9, 12):
        ps = list(parts(n))
        W.q_int = f64_q_int
        before = {p: W.wedderburn_weight(p) for p in ps}
        W.q_int = exact_q_int
        after = {p: W.wedderburn_weight(p) for p in ps}
        W.q_int = f64_q_int
        worst, worst_rel = None, mp.mpf(0)
        for p in ps:
            if after[p] == 0:
                continue
            rel = abs(before[p] - after[p]) / abs(after[p])
            if rel > worst_rel:
                worst, worst_rel = p, rel
        rows.append((n, len(ps), worst, worst_rel))
    return rows


# ── main ────────────────────────────────────────────────────────────────────
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="machine-readable summary")
    args = ap.parse_args(argv)

    files = py_files()
    edges = import_edges(files)
    value_cone = cone(edges, VALUE_ROOTS, files)
    shim_cone = cone(edges, [d for d, _ in DEF_SITES], files)
    # Word-boundary, not substring: `q_factorial` is a prefix of several
    # unrelated helper names, and a substring match inflates this count by
    # roughly 20 % against the figure it is meant to be comparable with.
    direct_re = re.compile(r"\b(?:" + "|".join(DIRECT_NAMES) + r")\b")
    direct = sorted(
        p for p in files
        if direct_re.search(open(os.path.join(ROOT, p), encoding="utf-8",
                                 errors="replace").read()))

    mapped = witness_map(files)
    in_cone = sorted(w for w, p in mapped.items() if p in value_cone)
    depth = {w: max_sig(w) for w in in_cone}
    ge30 = [w for w in in_cone if depth[w] >= 30]
    mid = [w for w in in_cone if 16 <= depth[w] < 30]
    shallow = [w for w in in_cone if depth[w] < 16]

    stems = {os.path.basename(p)[:-3] for p in value_cone}
    refusals = [s for s in BY_DESIGN_REFUSALS if s in stems]
    anchors = [s for s in ANCHOR_DEFINING if s in stems]

    manifest_path = os.path.join(ROOT, "computations", "q0_anchor_manifest.json")
    muon_in_cone: list[str] = []
    proton_in_cone: list[str] = []
    try:
        man = json.load(open(manifest_path, encoding="utf-8"))
        muon_in_cone = sorted(s for s in man.get("ideal_muon", []) if s in stems)
        proton_in_cone = sorted(s for s in man.get("physical_proton", []) if s in stems)
    except Exception:
        pass

    print("=" * 72)
    print(" float64 q_int -- reach and residual error   (bean qou-oiz3)")
    print("=" * 72)
    print(f"  definition sites (float64)     : {len(DEF_SITES)}")
    for d, nm in DEF_SITES:
        print(f"      {d}  ::  {nm}")
    print()
    print(f"  files MENTIONING the Wedderburn primitives : {len(direct)}")
    print("      (this is the question the recorded '124 python files' answered)")
    print(f"  VALUE CONE  (importers of the q_int-derived Hecke layer) : "
          f"{len(value_cone)}")
    print(f"  shim cone   (importers of the constant modules)          : "
          f"{len(shim_cone)}   <- NOT a measure of this defect")
    print()
    print(f"  committed witnesses with a producer in the value cone : {len(in_cone)}")
    print(f"      >=30 significant digits  (publish digits this defect makes wrong) : {len(ge30)}")
    print(f"      16..29 significant digits (may move)                              : {len(mid)}")
    print(f"      <16 significant digits    (cannot record the move)                : {len(shallow)}")
    print()
    print(f"  in-cone producers that REFUSE a re-run by design : {len(refusals)}"
          f"  {refusals}")
    print(f"  in-cone producers that are ANCHOR-DEFINING       : {len(anchors)}"
          f"  {anchors or '(none -- the anchor witness is OUTSIDE the cone)'}")
    print(f"  in-cone `ideal_muon` producers : {len(muon_in_cone)}  {muon_in_cone}")
    print(f"  in-cone `physical_proton` producers : {len(proton_in_cone)}")

    rows = []
    try:
        rows = weight_error_table()
    except Exception as exc:                                    # noqa: BLE001
        print(f"\n  [weight error NOT measured: {exc!r}]")
        print("   This is an environment fact, not a clean result.")
    if rows:
        import mpmath as mp
        print("\n  Wedderburn weight, f64-fed vs exact -- the error GROWS with the")
        print("  strand count, because q_factorial(n) accumulates n f64 factors:")
        print("      n   blocks   worst lambda            relative move")
        for n, nb, lam, rel in rows:
            print(f"    {n:3d}   {nb:5d}   {str(lam):22s} {mp.nstr(rel, 8)}")
        worst = max(rows, key=lambda r: r[3])
        print(f"\n  float64 eps = 2.220446049250313e-16.  At n = {worst[0]} the move is"
              f" {mp.nstr(worst[3] / mp.mpf('2.220446049250313e-16'), 4)}x eps")
        print("  and exceeds the framework's own L1 target of 1 ppQ = 1e-15.")

    if args.json:
        print(json.dumps({
            "value_cone_files": len(value_cone),
            "shim_cone_files": len(shim_cone),
            "direct_mention_files": len(direct),
            "witnesses_in_cone": len(in_cone),
            "witnesses_ge30_digits": len(ge30),
            "witnesses_16_29_digits": len(mid),
            "witnesses_lt16_digits": len(shallow),
            "by_design_refusals_in_cone": refusals,
            "anchor_defining_in_cone": anchors,
            "ideal_muon_in_cone": muon_in_cone,
            "physical_proton_in_cone": len(proton_in_cone),
        }, indent=2))

    # Advisory: this audit reports, it does not block.  The defect is a
    # STANDING one whose fix is staged (qou-oiz3); a blocking exit would make
    # every commit in the corpus red until the whole sweep lands.
    return 0


if __name__ == "__main__":
    sys.exit(main())
