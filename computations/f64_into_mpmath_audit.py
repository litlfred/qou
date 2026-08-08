#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; runs nothing, writes no witness.
"""Find float64 substrate constants being fed into high-precision paths.

Owner directive: NO FLOAT64. This is the static detector for the shape that
directive keeps being violated by — not a proximity heuristic, a check on
which NAME a script reads.

## Why a name check finds real defects

`q_parameter` exports the same quantity twice: `Q` is a Python float (~17
significant digits), `Q_MP` / `Q_50_DIGIT_STR` carry the full 50. `pyhecke.gram`
does the same with `h`. Reading the f64 name and then computing at 50 dps
produces a number that is *typed* as high precision and is not.

Three live examples, all found this way and all now fixed:

  * `mass_at_3A_proper.atom_braid_word_3A` used the f64 `gram.h` for every
    crossing offset, so the braid word entered a 50-dps χ computation with 17
    good digits. The dual-path cross-check bottomed out at ~1e-16 for every
    atom; it now reaches ~1e-50.
  * `mass_binding_dashboard` built its q₀⁻¹ leg by dividing into
    `mp.mpf(str(q_parameter.Q))`, so the inverse-anchor leg was capped while
    the forward leg was not.
  * `chi_convention_from_values_audit` recomputed with `_avg_color_delta()`
    (f64 internally) to check witnesses that had gone exact — the audit became
    the coarser side of its own comparison.

## The two tiers, and why the first one is not a guess

`LAUNDERED` is `mpf(str(X))` where X is an f64 constant. That idiom converts a
double to a high-precision TYPE while preserving only its 17 digits, and it is
the most misleading form because the result looks exact at every later
inspection — `type()` says mpf, `mp.nstr(..., 50)` prints 50 digits. There is
no legitimate reason to write it: if you want the value, read the `_MP` or
`_50_DIGIT_STR` name. Treated as a defect, not a candidate.

`F64_IMPORT` is a module that imports an f64 constant and also uses mpmath.
That is circumstantial — plenty of scripts legitimately hold an f64 for a numpy
kernel or a display string beside unrelated mpmath work — so it is REPORTED and
never auto-failed. Reading it as a defect list would be wrong; it is a list of
places to look.

Read-only and static: parses sources, imports nothing, runs no producer, writes
no witness. Safe beside any other work.

Usage:
    python3 computations/f64_into_mpmath_audit.py
    python3 computations/f64_into_mpmath_audit.py --tier LAUNDERED
    python3 computations/f64_into_mpmath_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# f64-valued substrate names. Their high-precision partners are the `_MP`
# suffix and `Q_50_DIGIT_STR`; anything here is a double by construction.
F64_NAMES = {
    "Q", "Q_INV", "HA", "HA_VAL", "HBAR_Q", "HBAR_Q_SQ", "LN_Q", "TANH_LN_Q",
    "E_CROSS", "S_SKEIN", "TWO_Q",
}
# `pyhecke.gram` re-exports the same doubles under shorter names.
F64_GRAM = {"h", "q0", "qi", "z"}
MP_MODULES = {"mpmath"}


def _mpmath_aliases(tree: ast.AST) -> set[str]:
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name in MP_MODULES:
                    out.add(a.asname or a.name)
        elif isinstance(n, ast.ImportFrom) and n.module in MP_MODULES:
            for a in n.names:
                out.add(a.asname or a.name)
    return out


def f64_imports(tree: ast.AST) -> dict:
    """Local name -> origin, for every f64 substrate constant imported.

    Follows `as` renaming, which matters: the dashboard defect was
    `from q_parameter import Q as Q0_val`, invisible to a search for `Q`.
    """
    out = {}
    for n in ast.walk(tree):
        if not isinstance(n, ast.ImportFrom) or not n.module:
            continue
        pool = F64_NAMES if "q_parameter" in n.module else (
            F64_GRAM if n.module.endswith("gram") else None)
        if pool is None:
            continue
        for a in n.names:
            if a.name in pool:
                out[a.asname or a.name] = f"{n.module}.{a.name}"
    return out


def laundered_calls(tree: ast.AST, names: dict, aliases: set[str]) -> list:
    """`mpf(str(X))` / `mp.mpf(str(X))` for an f64 X. Returns [(line, origin)].

    Matched structurally rather than by regex so `mp.mpf(str(Q0_val))`,
    `mpmath.mpf(str(Q))` and a bare `mpf(str(h))` all land, and a legitimate
    `mpf(str(Q_50_DIGIT_STR))` does not.
    """
    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call) or not n.args:
            continue
        f = n.func
        is_mpf = (getattr(f, "id", None) == "mpf"
                  or (isinstance(f, ast.Attribute) and f.attr == "mpf"
                      and getattr(f.value, "id", None) in aliases | {"mp"}))
        if not is_mpf:
            continue
        inner = n.args[0]
        if not (isinstance(inner, ast.Call)
                and getattr(inner.func, "id", None) == "str" and inner.args):
            continue
        target = inner.args[0]
        nm = getattr(target, "id", None)
        if nm in names:
            hits.append((getattr(n, "lineno", 0), names[nm]))
    return hits


def scan_source(src: str) -> dict:
    """Classify one module. Pure over text — self-tested below."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"tier": None, "laundered": [], "f64": {}}
    names = f64_imports(tree)
    aliases = _mpmath_aliases(tree)
    if not names:
        return {"tier": None, "laundered": [], "f64": {}}
    hits = laundered_calls(tree, names, aliases)
    if hits:
        return {"tier": "LAUNDERED", "laundered": hits, "f64": names}
    if aliases:
        return {"tier": "F64_IMPORT", "laundered": [], "f64": names}
    # Holds an f64 but never reaches mpmath: not this audit's business.
    return {"tier": None, "laundered": [], "f64": names}


Q50 = "Q_50_DIGIT_STR"
CASES = [
    ("the laundering idiom is a defect",
     "import mpmath as mp\nfrom q_parameter import Q\nx = mp.mpf(str(Q))\n",
     "LAUNDERED"),
    # The dashboard's actual shape: renamed on import, so a text search for
    # "mpf(str(Q))" misses it entirely.
    ("renamed on import is still caught",
     "import mpmath as mp\nfrom q_parameter import Q as Q0_val\n"
     "x = mp.mpf(str(Q0_val))\n", "LAUNDERED"),
    ("bare mpf() is caught",
     "from mpmath import mpf\nfrom q_parameter import HA\ny = mpf(str(HA))\n",
     "LAUNDERED"),
    ("gram's short names count too",
     "import mpmath as mp\nfrom pyhecke.gram import h\nz = mp.mpf(str(h))\n",
     "LAUNDERED"),
    # The whole point of the name check: same shape, correct source.
    (f"mpf(str({Q50})) is CORRECT, not a hit",
     f"import mpmath as mp\nfrom q_parameter import {Q50}\n"
     f"x = mp.mpf(str({Q50}))\n", None),
    ("the _MP family is correct too",
     "import mpmath as mp\nfrom q_parameter import Q_MP\nx = Q_MP * 2\n", None),
    ("f64 import beside mpmath is circumstantial, not a defect",
     "import mpmath as mp\nfrom q_parameter import Q\nprint(float(Q))\n",
     "F64_IMPORT"),
    # An f64 held for a numpy kernel with no mpmath anywhere is out of scope —
    # flagging it would bury the real hits under hundreds of non-findings.
    ("f64 with no mpmath at all is out of scope",
     "import numpy as np\nfrom q_parameter import Q\na = np.array([Q])\n",
     None),
    ("a module touching neither is silent", "x = 1\n", None),
    ("unparseable source is skipped, not guessed", "def (\n", None),
]


def self_test() -> int:
    fails = 0
    for label, src, want in CASES:
        got = scan_source(src)["tier"]
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    # The detector must not fire on its OWN prose, which quotes the idiom.
    ok = scan_source(Path(__file__).read_text(encoding="utf-8"))["tier"] is None
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  the audit does not flag itself")
    total = len(CASES) + 1
    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=("LAUNDERED", "F64_IMPORT"))
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    rows = []
    for p in sorted(ROOT.rglob("*.py")):
        if "_deprecated" in p.parts or "node_modules" in p.parts:
            continue
        if p.resolve() == Path(__file__).resolve():
            continue
        try:
            r = scan_source(p.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if r["tier"] and (not a.tier or r["tier"] == a.tier):
            rows.append((r["tier"], p.relative_to(ROOT).as_posix(), r))

    laundered = [r for r in rows if r[0] == "LAUNDERED"]
    imports = [r for r in rows if r[0] == "F64_IMPORT"]

    if laundered:
        print(f"LAUNDERED — mpf(str(<f64>)): {len(laundered)} file(s). "
              f"These are defects.")
        for _, path, r in laundered:
            for line, origin in r["laundered"]:
                print(f"  {path}:{line}  <- {origin}")
    else:
        print("LAUNDERED — none.")

    print(f"\nF64_IMPORT — imports an f64 constant and uses mpmath: "
          f"{len(imports)} file(s). CIRCUMSTANTIAL — review, do not bulk-edit.")
    for _, path, r in imports[:40]:
        print(f"  {path}  ({', '.join(sorted(r['f64'])[:4])})")
    if len(imports) > 40:
        print(f"  … and {len(imports) - 40} more")

    print("\nFix by reading the high-precision name: Q_50_DIGIT_STR / the _MP\n"
          "family / flavor_split_leading(q) — not by widening a tolerance.\n"
          "Exit status reflects LAUNDERED only; F64_IMPORT never fails a run.")
    return 1 if laundered else 0


if __name__ == "__main__":
    raise SystemExit(main())
