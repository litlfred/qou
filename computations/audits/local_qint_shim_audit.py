#!/usr/bin/env python3
"""local_qint_shim_audit.py — find LOCAL q-integer re-implementations that read
the anchor shim, i.e. the copy-paste route to the entry-point-tracking defect.

WHY THIS EXISTS

`qou-6p3b` scoped the `qfac`/`dim_q` migration as one library surface. It is
two. Measured 2026-08-24: 41 of the 133 name-matched sites call a function the
file DEFINES ITSELF, never touching `hecke_characters`. Threading the library
fixes none of those.

Most are harmless — 8 are sympy-symbolic and so anchor-free by construction, and
one already reads `qou_substrate` (which is not rebound). The problem is the
rest: a local `qint`/`qfac`/`dim_q` that closes over `q_parameter`'s `Q`, which
the shim REBINDS to muon when the running process's argv stem is manifest-listed.
Each such file reproduces the whole defect privately.

This audit does NOT try to migrate them. Consolidating them onto the library
would be a real change with real risk — a local q-integer may use a different
convention (balanced `(q^k - q^-k)/(q - q^-1)` vs unbalanced `(q^k - 1)/(q - 1)`)
and silently unifying two conventions changes numbers. It exists so the class is
VISIBLE and cannot quietly grow: `docs/audits/scripts/` already holds three
hand-rolled q-explicit variants with TWO different argument orders, which is this
route being created in real time.

Usage:
    python3 local_qint_shim_audit.py            # report
    python3 local_qint_shim_audit.py --strict   # exit 1 if the count grew
    python3 local_qint_shim_audit.py --selftest # detector must find its knowns
"""
from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
SKIP = (".git", "_deprecated", "fsh-guts", "node_modules", "__pycache__", ".claude", "qou-mass")
QNAMES = ("qint", "q_int", "qfac", "qfact", "dim_q")

# The shim is the thing that gets rebound. `qou_substrate.constants` is NOT.
SHIM = re.compile(r"^\s*from\s+q_parameter\s+import|(?<![\w.])q_parameter\s*\.", re.M)
SYMBOLIC = re.compile(r"Symbol\(\s*[\"']q|sympy")


def classify(path: pathlib.Path):
    """(verdict, detail) for a file that defines its own q-integer family."""
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src)
    except (OSError, SyntaxError):
        return None, ""
    # A definition that TAKES a q is not the defect — it is the fix. Only a
    # definition that closes over an ambient q reproduces the entry-point
    # tracking. Checking the name alone over-counts by 6x (measured: 124 vs 20),
    # because a file can define `dim_q(shape, q)` and separately import
    # q_parameter for something unrelated. Role, not appearance.
    # MODULE-LEVEL definitions only. A NESTED `def qint(...)` is scoped to its
    # enclosing function, which typically supplies the q as a parameter — so it
    # is parameterised by the caller even though the inner signature does not
    # say so. Counting nested defs added false positives (measured: the
    # docs/audits/scripts/keystone_* family, whose qint sits inside a function
    # that takes q). Role, not appearance — again.
    defined = set()
    for n in tree.body:
        if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if n.name not in QNAMES:
            continue
        params = {a.arg for a in n.args.args} | {a.arg for a in n.args.kwonlyargs}
        if params & {"q", "q0", "q_val", "qq"}:
            continue          # parameterised — the caller names the anchor
        defined.add(n.name)
    if not defined:
        return None, ""
    if SYMBOLIC.search(src):
        return "symbolic", "sympy — anchor-free by construction"
    if SHIM.search(src):
        return "SHIM", f"defines {sorted(defined)} over a shim-derived q"
    if "qou_substrate" in src:
        return "substrate", "reads qou_substrate — not rebound, anchor-free"
    return "unknown", f"defines {sorted(defined)}, q source not identified"


def scan():
    out = {}
    for p in sorted(REPO.rglob("*.py")):
        if any(x in p.parts for x in SKIP):
            continue
        v, d = classify(p)
        if v:
            out.setdefault(v, []).append((str(p.relative_to(REPO)), d))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if the SHIM population grew past the baseline")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--baseline", type=int, default=None,
                    help="override the recorded baseline (drains only, never grows)")
    args = ap.parse_args(argv)

    res = scan()
    shim = res.get("SHIM", [])

    if args.selftest:
        # young_qdim is the known SYMBOLIC case; q_mpmath the known SHIM case.
        names = {f for f, _ in res.get("symbolic", [])}
        shim_names = {f for f, _ in shim}
        ok = (any("young_qdim" in n for n in names)
              and any("q_mpmath" in n for n in shim_names))
        print(f"  symbolic detected: {len(names)}   shim detected: {len(shim_names)}")
        print("  selftest OK" if ok else
              "  SELFTEST FAILED — a known case is not detected")
        return 0 if ok else 1

    print("=" * 72)
    print("local q-integer re-implementations — the copy-paste route (qou-6p3b)")
    print("=" * 72)
    for k, label in (("SHIM", "READS THE SHIM — reproduces the defect privately"),
                     ("unknown", "q source unidentified — needs a human read"),
                     ("symbolic", "symbolic, anchor-free — not in scope"),
                     ("substrate", "reads qou_substrate, anchor-free — not in scope")):
        rows = res.get(k, [])
        print(f"\n  {k:<10} {len(rows):3d}   {label}")
        if k in ("SHIM", "unknown"):
            for f, d in rows:
                print(f"       {f}")

    base = args.baseline if args.baseline is not None else BASELINE
    print(f"\n  SHIM population {len(shim)} against baseline {base}")
    print("  Baselines DRAIN, never grow — if this is over, a new local"
          "\n  re-implementation was added; write it against the library instead.")
    print("=" * 72)
    if args.strict and len(shim) > base:
        return 1
    return 0


#: Measured on main 2026-08-24: 41 files, module-level defs that close over a
#: shim-derived q. NOTE this is a BROADER population than the 16 in
#: docs/audits/2026-08-24-qfac-dimq-threading-scope.md, which counted only files
#: that ALSO had a defaulted qfac/dim_q call site. Both are real; they measure
#: different things. Lower this when files are migrated; never raise it.
BASELINE = 41

if __name__ == "__main__":
    raise SystemExit(main())
