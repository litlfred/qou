#!/usr/bin/env python3
"""Does a `mpf(<float64 constant>)` site DECLINE a better value the corpus holds?

PRIOR ART FIRST -- this is not the discovery of the blind spot.
-------------------------------------------------------------
The `mpf(<float-valued NAME>)` shape is already named and measured in bean
`qou-qrsp` (in-progress, high), which states plainly that the source detector
`computations/mpf_float_source_audit.py` "documents it cannot catch" it: that
gate keys on the literal spelling `mpf(float(...))`, and a constant that IS
already a float needs no token.

`qou-qrsp` also carries a *stronger* tool than this one for FINDING such sites:
`computations/float64_entry_tracer.py` patches mpmath's `from_float` /
`from_npfloat` and reads off the source line where a float64 actually enters at
runtime -- so it sees floats arriving from JSON, from numpy, and from library
downcasts, none of which a static scan over named constants can reach. If you
want to know where float64 enters a producer, use the tracer, not this.

WHAT THIS ADDS, AND IT IS NARROW
--------------------------------
`qou-qrsp` records that while the *localization* is mechanizable, the
*judgment* is not:

    "For each re-padder decide whether the quantity is GENUINELY float64
     (then stop promoting it to mpf) or was DOWNCAST upstream from full
     precision (then padding is a symptom and the real defect is the lost
     precision). Guessing wrong either fakes precision or hides a real loss."

That judgment is decidable for one slice: when the float came from a named
constant in `qou_substrate.constants` and that module ALSO carries a
higher-precision string twin. Then the quantity was demonstrably not "genuinely
float64" -- the corpus holds a better value one import away, and the site
declined it. This audit decides that slice and nothing else.

THE DISCRIMINATOR IS THE POINT -- a raw site count is NOT a defect count
-----------------------------------------------------------------------
Measured on this tree: 214 sites match the shape; 10 are defects. Quoting the
214 would be a 21x over-flag, because most float64 constants here are CODATA
*measurements* carrying ~11-12 significant digits -- a float64 holds those to
~17, so wrapping one in `mpf` loses nothing that exists. `M_E_MEV` (112 sites)
is the type case and is fine.

Worked defect (`casimir_macdonald_probe.py:209`, `q = mpf(Q)`):

    mpf(Q)               -> 1.10997858275138083783417641825508326292037963867187500000000
    mpf(Q_50_DIGIT_STR)  -> 1.10997858275138080759166909561076887987449912187360000000000
                                           ^ diverge at significant digit 18

`mpf` of a python float stores the exact 53-bit binary value; `precision.fmt`
at OUTPUT_DPS then prints that binary value's exact decimal expansion -- the
`...50000000` tail -- which reads as precision and is not. The published
witness carries the float64 one.

The twin set is DERIVED at import time from `qou_substrate.constants`, never
hardcoded: a hardcoded name list is what goes stale, and deriving it found two
twins (`MASS_RATIO_MU_E`, diverging at digit 10, and `VOL_FIGURE_EIGHT`) that
a hand-written list from the obvious names missed.

NOT A GATE. Exit 0 always. Fix at the site (`mpf(Q)` -> `mpf(Q_50_DIGIT_STR)`)
and re-run the producer; per `qou-qrsp`, the source fix and the witness
regeneration are SEPARATE commits, because they change numbers.

For a quantity that is genuinely float64 (a deliberate f64 kernel), the fix is
NOT this -- it is `fmt(float(x))`, the convention `fmt()` already documents.
"""

from __future__ import annotations

import ast
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))

import qou_substrate.constants as C  # noqa: E402
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS, fmt  # noqa: E402

mp.dps = COMPUTE_DPS


def _float_constants() -> set[str]:
    """Every name in qou_substrate.constants bound to a python float."""
    return {n for n in dir(C) if not n.startswith("_")
            and isinstance(getattr(C, n, None), float)}


def _string_twins(floats: set[str]) -> dict[str, tuple[str, int]]:
    """float-constant -> (higher-precision str twin, first diverging char).

    Derived, never hardcoded. A twin counts only if it actually carries more
    information: if mpf(float) and mpf(str) agree to OUTPUT_DPS the wrap is
    harmless and the site is not a defect.
    """
    out: dict[str, tuple[str, int]] = {}
    strs = [n for n in dir(C)
            if n.endswith("_STR") and isinstance(getattr(C, n, None), str)]
    for f in floats:
        stem = f.replace("_MEV", "")
        for s in strs:
            if not (s.startswith(f) or s.startswith(stem)):
                continue
            try:
                a, b = fmt(mpf(getattr(C, f))), fmt(mpf(getattr(C, s)))
            except Exception:
                continue
            d = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), None)
            if d is not None:
                out[f] = (s, d)
                break
    return out


def _bound_names(tree: ast.Module) -> dict[str, str]:
    """local name -> the ORIGINAL name it was imported under.

    Exists because the first version of this audit matched a bare `Name`
    against `qou_substrate.constants` and never asked what the file itself had
    bound that name to. `homfly_ocneanu_trace.py` does

        from q_parameter import Q_50_DIGIT_STR as Q
        q0 = mp.mpf(Q)                     # already the 50-digit STRING

    which the name-only match reported as a lossy `mpf(Q)`. It is the opposite
    -- the file is doing exactly what this audit recommends. One of ten
    reported defects was this, i.e. a 10 % false-positive rate from a single
    unhandled spelling; the same class as every other row in the corpus's
    detector-blindness taxonomy.
    """
    out: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for al in node.names:
                out[al.asname or al.name] = al.name
        elif isinstance(node, ast.Import):
            for al in node.names:
                if al.asname:
                    out[al.asname] = al.name
    return out


def main() -> int:
    floats = _float_constants()
    twins = _string_twins(floats)

    defects: list[tuple[str, int, str]] = []
    benign = 0
    aliased_away = 0
    for p in sorted((ROOT / "computations").rglob("*.py")):
        if p.resolve() == pathlib.Path(__file__).resolve():
            continue
        try:
            tree = ast.parse(p.read_text())
        except (SyntaxError, UnicodeDecodeError):
            continue
        bound = _bound_names(tree)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not node.args:
                continue
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
            if nm != "mpf":
                continue
            a = node.args[0]
            local = (a.id if isinstance(a, ast.Name)
                     else a.attr if isinstance(a, ast.Attribute) else None)
            if local is None:
                continue
            # Resolve what THIS FILE bound the name to. A bare `Name` may be an
            # alias -- `from q_parameter import Q_50_DIGIT_STR as Q` makes the
            # local name `Q` the high-precision STRING, and flagging it is a
            # false positive. An `Attribute` (`C.Q`) names the original
            # directly, so it resolves to itself.
            arg = bound.get(local, local) if isinstance(a, ast.Name) else local
            if arg not in floats:
                if local in floats:
                    aliased_away += 1   # flagged by name, cleared by its import
                continue
            rel = str(p.relative_to(ROOT))
            if arg in twins:
                defects.append((rel, node.lineno, arg))
            else:
                benign += 1

    print("=" * 78)
    print("mpf(<float64 constant>) with no float() token")
    print("=" * 78)
    print(f"  float64 constants in qou_substrate.constants : {len(floats)}")
    print(f"  ...of which a higher-precision str twin exists: {len(twins)}")
    for f, (s, d) in sorted(twins.items()):
        print(f"        {f} -> {s}   (diverge at significant digit {d})")
    print()
    print(f"  sites wrapping a constant with NO better twin : {benign}  (not defects)")
    print(f"  sites cleared by their own import alias       : {aliased_away}  (not defects)")
    print(f"  sites DECLINING an available better twin      : {len(defects)}")
    print()
    if defects:
        print("  --- lossy: a higher-precision string is one import away ---")
        for rel, ln, arg in defects:
            print(f"    {rel}:{ln}  mpf({arg})   ->  mpf({twins[arg][0]})")
        print()
        print("  by constant:", dict(Counter(a for _, _, a in defects)))
        print("  distinct files:", len({f for f, _, _ in defects}))
    print()
    print("  A raw site count is NOT a defect count -- see this file's docstring.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
