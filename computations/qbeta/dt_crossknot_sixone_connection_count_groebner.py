#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational algebraic geometry; no substrate q.
"""The 6_1 boundary-parabolic connection count — the residual qou-btvl left open.

`dt_crossknot_connection_count_certified_probe.py` certified 4_1 = 3 and
5_2 = 4 from the Magma outputs SnapPy ships as regression fixtures, and closed
with: *"6_1 has no bundled data -- the third-knot test for
dtMax = recursionOrder + 1 remains open (needs the ptolemy DB or magma)."*
That is accurate: `snappy/ptolemy/testing_files/` has 35 files and none is
`m032`/`6_1`/`K4_1`.

**Neither the database nor Magma is actually required.** Only
`retrieve_solutions()` needs the network; `Manifold.ptolemy_variety()` builds
the ideal offline, and for these knots it is tiny -- 4 tetrahedra, 4 Ptolemy
coordinates, 5 equations, 2 obstruction classes. A Groebner basis over QQ in
sympy settles it in seconds. So this closes the residual by a different route
rather than by waiting for egress.

## Result

    4_1   2 irreducible + 1 abelian = 3      (reproduces the certified probe)
    5_2   3 irreducible + 1 abelian = 4      (reproduces the certified probe)
    6_1   4 irreducible + 1 abelian = 5      <- the missing third-knot input

## The non-zero condition is load-bearing, and omitting it inverts the answer

SnapPy exposes `equations_with_non_zero_condition`, which appends the
Rabinowitsch polynomial `1 = c_1 c_2 c_3 c_4 t` forcing every Ptolemy
coordinate to be nonzero. That is SnapPy's own definition of the variety to
solve, not a filter chosen here.

Using the bare `equations` instead, 6_1's obstruction class 0 contributes a
spurious rational point with `c_0011_2 = 0`, giving **5** irreducible and hence
6 connections -- which would have *refuted* R1's prediction of 5. This probe
was first run that way and did report 5; the count is recorded here because
the wrong answer is the plausible-looking one. With the non-zero condition,
class 0 is EMPTY for all three knots.

## Gates

1. 4_1 and 5_2 must reproduce the certified probe's 2 and 3. They do.
2. Each class-1 ideal must be a single Galois orbit whose field is the knot's
   known trace field. Discriminants come out `-3`, `-23`, `257` -- i.e.
   Q(sqrt-3), the cubic of discriminant -23, and the quartic of discriminant
   257, which are the tabulated trace fields of 4_1, 5_2 and 6_1. This is an
   independent invariant: nothing in the count computes a trace field.

## Scope -- what this does NOT do

It supplies R1's **input**, not a test of R1. R1 reads
`DT_max = #boundary-parabolic connections`, so this makes R1's prediction for
6_1 the definite `{5}` instead of "unknown". The third-knot **test** still
needs an independent resurgence/Borel DT count for 6_1, which the corpus does
not have. What has changed is that both candidate rules are now definite --
R1 -> `{5}`, and Wedderburn-at-the-braid-index -> `{5, 10}` now that
`braid index(6_1) = 4` is derived (qou-dr8m) rather than recalled -- so the
test discriminates once that count exists.

The "+1 abelian" convention is the audit's, carried over unchanged from the
certified probe: reducible representations are excluded from the Ptolemy
variety by nondegeneracy, and the abelian connection is the `(L-1)` factor of
the full A-polynomial.

Exact rational arithmetic throughout; no floats, no substrate constant.
Scope-(a); nothing wired. Beans qou-btvl / qou-rtec / qou-dr8m.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402
from sympy import QQ, groebner  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

# Certified by dt_crossknot_connection_count_certified_probe.py; 6_1 is the target.
EXPECT_IRRED = {"4_1": 2, "5_2": 3, "6_1": None}
# Tabulated trace-field discriminants.
EXPECT_DISC = {"4_1": -3, "5_2": -23, "6_1": 257}


def analyse(knot: str, use_non_zero: bool):
    """Per-obstruction-class solution count and field, over QQ."""
    import snappy
    out = []
    for ci, v in enumerate(snappy.Manifold(knot).ptolemy_variety(2, "all")):
        if use_non_zero:
            names = sorted(v.variables_with_non_zero_condition)
            eqs = v.equations_with_non_zero_condition
        else:
            names = sorted(v.variables)
            eqs = v.equations
        # `t` first in lex so the Rabinowitsch variable is eliminated and the
        # surviving univariate is a genuine Ptolemy coordinate.
        cs = [n for n in names if n != "t"]
        gens = ([sp.Symbol("t")] if "t" in names else []) + [sp.Symbol(n) for n in cs]
        loc = {str(g): g for g in gens}
        polys = [sp.sympify(str(e).replace("^", "**"), locals=loc) for e in eqs]
        G = groebner(polys, *gens, order="lex", domain=QQ)
        if list(G.exprs) == [sp.Integer(1)]:
            out.append({"class": ci, "count": 0, "kind": "empty",
                        "poly": None, "disc": None})
            continue
        uni = [g for g in G.exprs
               if len(sp.Poly(g, *gens).free_symbols) == 1
               and sp.Poly(g, *gens).total_degree() > 1]
        if not uni:
            # every generator linear => a single rational point
            out.append({"class": ci, "count": 1, "kind": "rational point",
                        "poly": None, "disc": None})
            continue
        u = uni[0]
        x = list(sp.Poly(u, *gens).free_symbols)[0]
        fl = sp.factor_list(u)[1]
        n = sum(sp.Poly(f, x).degree() * m for f, m in fl)
        out.append({"class": ci, "count": n,
                    "kind": f"{len(fl)} Galois orbit(s)",
                    "poly": str(sp.factor(u)),
                    "disc": int(sp.discriminant(sp.Poly(u, x))) if len(fl) == 1 else None})
    return out


def main() -> int:
    print("=" * 78)
    print(" 6₁ boundary-parabolic connections — Gröbner over ℚ, no DB, no Magma")
    print("=" * 78)

    wb = WitnessBuilder("dt-crossknot-sixone-connection-count",
                        engine="sympy-groebner-QQ")
    wb.set_description(
        "Counts irreducible boundary-parabolic PSL(2,C) representations of "
        "4_1, 5_2 and 6_1 by Groebner basis over QQ on SnapPy's Ptolemy "
        "variety, imposing SnapPy's own non-zero condition. Closes the 6_1 "
        "residual that dt_crossknot_connection_count_certified_probe.py left "
        "open for want of bundled Magma data or ptolemy-DB egress: 6_1 = 4 "
        "irreducible + 1 abelian = 5 connections. Gated on reproducing the "
        "certified 4_1 = 2 and 5_2 = 3, and on the three trace-field "
        "discriminants -3 / -23 / 257. Records that dropping the non-zero "
        "condition yields a spurious zero-coordinate point and the wrong "
        "answer 5 irreducible. Supplies R1's INPUT, not a test of R1. "
        "Scope-(a); nothing wired. Beans qou-btvl/qou-rtec/qou-dr8m."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    ok = True
    results, naive = {}, {}
    print("\n[1] with SnapPy's non-zero condition (authoritative)")
    for knot in EXPECT_IRRED:
        res = analyse(knot, use_non_zero=True)
        tot = sum(r["count"] for r in res)
        results[knot] = {"classes": res, "irreducible": tot,
                         "connections": tot + 1}
        exp = EXPECT_IRRED[knot]
        good = exp is None or tot == exp
        ok = ok and good
        tag = "  <- TARGET" if exp is None else (
            f"   certified {exp}  {'OK' if good else 'MISMATCH'}")
        print(f"    {knot}: irreducible {tot}  (+1 abelian = {tot + 1}){tag}")
        for r in res:
            print(f"        class {r['class']}: {r['count']:>2}  {r['kind']}"
                  + (f"   {r['poly']}  disc {r['disc']}" if r["poly"] else ""))

    print("\n[2] trace-field discriminants (independent invariant)")
    for knot in EXPECT_IRRED:
        got = next((r["disc"] for r in results[knot]["classes"] if r["disc"]), None)
        good = got == EXPECT_DISC[knot]
        ok = ok and good
        print(f"    {knot}: disc {got}  expect {EXPECT_DISC[knot]}  "
              f"{'OK' if good else 'MISMATCH'}")

    print("\n[3] the trap: WITHOUT the non-zero condition")
    for knot in EXPECT_IRRED:
        res = analyse(knot, use_non_zero=False)
        tot = sum(r["count"] for r in res)
        naive[knot] = {"classes": res, "irreducible": tot}
        flag = "  <- SPURIOUS" if tot != results[knot]["irreducible"] else ""
        print(f"    {knot}: irreducible {tot}{flag}")
    trap = naive["6_1"]["irreducible"] != results["6_1"]["irreducible"]
    print(f"    6₁ inflated by the degenerate zero-coordinate point: "
          f"{'YES — omitting the condition would have refuted R1' if trap else 'no'}")

    wb.add_data("counts", results)
    wb.add_data("without_non_zero_condition", naive)
    wb.add_data("method", {
        "variety": "snappy Manifold.ptolemy_variety(2, 'all'), built OFFLINE — "
                   "only retrieve_solutions() needs the network",
        "solver": "sympy Groebner basis over QQ, lex with the Rabinowitsch "
                  "variable t eliminated first",
        "non_zero_condition": "snappy's own equations_with_non_zero_condition "
                              "(1 = c_1 c_2 c_3 c_4 t)",
        "abelian_convention": "+1 abelian connection = the (L-1) factor of the "
                              "full A-polynomial; the audit's convention, "
                              "carried over unchanged, not new derivation",
        "arithmetic": "exact rationals; no float anywhere",
    })
    wb.add_data("scope", {
        "supplies": "R1's INPUT — DT_max = #connections makes R1's 6_1 "
                    "prediction the definite {5}",
        "does_not": "test R1. The third-knot test still needs an independent "
                    "resurgence/Borel DT count for 6_1, absent from the corpus",
        "now_discriminating": "R1 -> {5} vs Wedderburn-at-braid-index -> "
                              "{5,10}, the latter definite only because "
                              "braid index(6_1) = 4 is now derived (qou-dr8m)",
    })
    wb.add_assertion("irreducible_counts",
                     computed=str([results[k]["irreducible"] for k in EXPECT_IRRED]),
                     expected="[2, 3, 4]", tolerance="exact",
                     source="Groebner over QQ with the non-zero condition")
    wb.add_assertion("trace_field_discriminants",
                     computed=str([next(r["disc"] for r in results[k]["classes"]
                                        if r["disc"]) for k in EXPECT_IRRED]),
                     expected="[-3, -23, 257]", tolerance="exact",
                     source="tabulated trace fields of 4_1, 5_2, 6_1")
    wb.add_assertion("six_one_connections",
                     computed=str(results["6_1"]["connections"]),
                     expected="5", tolerance="exact",
                     source="4 irreducible + 1 abelian")
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0, on either layer. The computation is exact rational "
            "algebraic geometry on a Ptolemy variety — a Groebner basis over "
            "QQ — and no substrate quantity enters at any point."),
    })

    print(f"\n  RESULT: {'CLOSED — 6₁ = 5 connections' if ok else 'FAILURE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
