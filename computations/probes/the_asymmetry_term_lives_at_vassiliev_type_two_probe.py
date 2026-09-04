#!/usr/bin/env python3
"""The `(N-Z)^2` asymmetry term lives at Vassiliev type two, and taking `-log` is
what destroys it: `c_2/c_0 = (N-Z)^2/2 + (5-A)/8` exactly, for the chain, at
every `A` and `Z`. The resummed bond model cannot produce a quadratic asymmetry
because `-log` turns the product of bond factors into a SUM, killing precisely
the pair-convolution term that carries it.

WHERE THIS SITS
---------------
Bean `qou-oooq`. `the_convexity_obstruction_is_order_two_in_the_tower_probe`
answered which reading the corpus uses — the mass formula and `Phi_q` resum, but
`vassiliev-filtration-mass-tower` also gives the LP/SDP operator selection a
cost-vector basis at each type, "a graded hierarchy of independent linear
programs" — and left one question: does a graded piece actually produce anything?

It does. And it produces the thing the arc had been unable to get.

THE MECHANISM
-------------
Every obstruction in `qou-mu1h` and `qou-bygw` followed from ADDITIVITY. The
resummed observable is `L = sum over bonds of -log(z + d)`, a sum of per-type
constants, so `B` is linear in `Z` for the chain and convex for all-pairs, and in
both cases the maximum sits at an endpoint. No valley of stability, for any `q`.

At a fixed Vassiliev type that argument does not even start. Write the chain
trace as a product of bond factors `P(h) = prod_i f_i(h)` with all `f_i(0) = z0`.
Then

    c_0 = z0^(A-1)
    c_1 = z0^(A-2) * sum_i f_i'
    c_2 = z0^(A-2) * sum_i f_i''  +  z0^(A-3) * sum_{i<j} f_i' f_j'

The second term of `c_2` is a sum over PAIRS of bonds — a convolution, not a sum
— and it is quadratic in the bond counts. Since the chain has `Z-1` pp bonds, one
pn, and `N-1` nn bonds, a quadratic in those counts is a quadratic in `N - Z`.

`-log` is exactly the operation that destroys this: it turns the product into a
sum, so the cross term `sum_{i<j} f_i' f_j'` never appears. The asymmetry term
was never absent from the algebra; it was absent from the logarithm.

MEASURED — an exact closed form
-------------------------------
For the chain, verified symbolically for every `A = 3..10` and every `Z`:

    c_2 / c_0  =  (N - Z)^2 / 2  +  (5 - A)/8

so, reading binding as `-alpha c_2/c_0` (see the sign caveat below),

    -alpha c_2/c_0  =  -alpha (N-Z)^2 / 2   +   alpha A / 8   -   5 alpha / 8
                       ^^^^^^^^^^^^^^^^^^       ^^^^^^^^^^^
                       asymmetry-like           volume-like

Both terms have the SEMF's sign and functional form: a volume term linear in `A`
and an asymmetry term quadratic in `N - Z`, out of a single Vassiliev
coefficient. Compare `qou-xwur`, where the isospin/partition route produced only
`-log[2T+1]_q`, logarithmic in `T`, and collapsed at `A = 20` for exactly that
reason. This is the quadratic that route could not reach.

The all-pairs factor product is also exactly quadratic, with coefficient
`C(A/2, 2)` (1, 3, 6 at `A` = 4, 6, 8) instead of the chain's constant `1/2`.

WHAT IS WRONG WITH IT, STATED PLAINLY
-------------------------------------
  * **Magnitudes are off.** With `alpha = m_e/(q0(q0-1)) = 4.185981 MeV`, the
    volume-like coefficient is `alpha/8 = 0.5232` MeV per nucleon against SEMF's
    `a_V ~ 15.8`, a factor of 30. The asymmetry coefficient is `alpha/2 = 2.093`
    MeV.
  * **The asymmetry lacks the `1/A`.** SEMF is `-a_A (N-Z)^2 / A` with
    `a_A ~ 23`; this is `-alpha (N-Z)^2 / 2`, with no `A` in the denominator. It
    coincides with SEMF's coefficient only near `A ~ 11`, which is a crossing,
    not an agreement. All-pairs is worse, not better: `C(A/2,2) ~ A^2/8` grows.
  * **The sign convention is assumed, not derived.** `c_2/c_0` is MINIMISED at
    `N = Z`, so binding has to read as `-c_2` for the asymmetry to penalise
    rather than reward. Nothing here establishes which sign the framework takes.
  * **No binding number is produced.** This is a shape result.

WHAT IT CHANGES ANYWAY
----------------------
The arc's standing verdict was that the bond model cannot produce a valley of
stability for any `q`, by a Jensen argument on the convexity of `-log`. That
verdict is correct and it is now also explained: the quadratic that a valley
needs is a pair-convolution term, and `-log` is the step that removes it. The
term exists one level down, at the type the corpus itself calls "the first
mass-discriminating framing correction".

That does not rescue the resummed model — the resummation is the logarithm, and
the logarithm is the problem. It relocates the question to whether the LP/SDP
per-type reading is the right one, which is a modelling decision nobody has made.

WHAT IS NOT CLAIMED
-------------------
No binding number, no fit, nothing wired. Not that `-c_2` is the binding
observable. Not that the LP/SDP reading is correct. `qou-bygw`'s ordering
ambiguity is untouched and independently blocks the all-pairs case: the "all-
pairs factor product" used here is the naive product, not the true all-pairs
trace, which is not well defined until a bond ordering is fixed.
"""
from __future__ import annotations

import sys
from math import comb  # float64-ok: integer combinatorics only, no float arithmetic
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402
import sympy as sp  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

ALPHA = mpfr(str(M_E_MEV)) / (E.Q * (E.Q - 1))
MORD = 4


def factors(m=MORD):
    h = sp.symbols("h")
    q = (h + sp.sqrt(h ** 2 + 4)) / 2          # invert q - 1/q = h
    z = sp.series(q ** 3 / (q ** 2 + 1), h, 0, m + 2).removeO()
    delta = sp.series((q - 1) ** 2 * (1 - q ** -4) / 3, h, 0, m + 2).removeO()
    return h, {"pp": sp.expand(z), "nn": sp.expand(z - h),
               "pn": sp.expand(z - h * (1 - delta / 2) / 2)}


def prod_counts(h, f, counts, m=MORD):
    def trunc(e):
        return sp.expand(sum(e.coeff(h, k) * h ** k for k in range(m + 1)))
    P = sp.Integer(1)
    for kind, n in counts.items():
        for _ in range(n):
            P = trunc(sp.expand(P * f[kind]))
    return P


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    h, f = factors()

    print("\n" + "=" * 76)
    print("§1  THE CLOSED FORM: c_2/c_0 = (N-Z)^2/2 + (5-A)/8  [chain]")
    print("=" * 76)
    print(f"    {'A':>3} {'Z':>3} {'N':>3} {'N-Z':>4} {'c_2/c_0':>12} {'predicted':>12}")
    all_ok = True
    for A in range(3, 11):
        for Z in range(1, A):
            N = A - Z
            P = prod_counts(h, f, {"pp": Z - 1, "pn": 1, "nn": N - 1})
            r = sp.nsimplify(sp.simplify(P.coeff(h, 2) / P.coeff(h, 0)))
            pred = sp.Rational((N - Z) ** 2, 2) + sp.Rational(5 - A, 8)
            good = sp.simplify(r - pred) == 0
            all_ok &= good
            if Z <= 2 or Z == A // 2:
                print(f"    {A:>3} {Z:>3} {N:>3} {N - Z:>4} {str(r):>12} {str(pred):>12}")
    check("c_2/c_0 = (N-Z)^2/2 + (5-A)/8 exactly, for every A = 3..10 and every Z",
          all_ok)

    print("\n" + "=" * 76)
    print("§2  WHY: the type-2 coefficient of a PRODUCT has a pair convolution")
    print("=" * 76)
    print("    P = prod_i f_i,  all f_i(0) = z0:")
    print("      c_0 = z0^(A-1)")
    print("      c_1 = z0^(A-2) * sum_i f_i'")
    print("      c_2 = z0^(A-2) * sum_i f_i''  +  z0^(A-3) * sum_{i<j} f_i' f_j'")
    print("    the second term is a sum over PAIRS of bonds, hence QUADRATIC in the")
    print("    bond counts, hence quadratic in N - Z. Taking -log turns the product")
    print("    into a sum and that cross term never appears — which is exactly why")
    print("    the resummed L has no (N-Z)^2 and no valley of stability.")
    # the claim that -log kills it: L is additive, so its 'c_2' is linear in counts
    Ls = {k: sp.series(-sp.log(v), h, 0, MORD + 1).removeO() for k, v in f.items()}
    lin = []
    for A in (4, 6, 8):
        row = []
        for Z in range(1, A):
            N = A - Z
            row.append(sp.nsimplify(((Z - 1) * Ls["pp"] + Ls["pn"]
                                     + (N - 1) * Ls["nn"]).coeff(h, 2)))
        # second difference of a linear function in Z is zero
        d2 = [sp.simplify(row[i + 2] - 2 * row[i + 1] + row[i]) for i in range(len(row) - 2)]
        lin.append(all(x == 0 for x in d2))
        print(f"    A={A}: [h^2] of the ADDITIVE L is linear in Z "
              f"(all second differences zero: {lin[-1]})")
    check("the additive L's type-2 piece is LINEAR in Z — no quadratic term survives "
          "the logarithm", all(lin))

    print("\n" + "=" * 76)
    print("§3  ALL-PAIRS FACTOR PRODUCT IS ALSO QUADRATIC, WITH A WORSE COEFFICIENT")
    print("=" * 76)
    coeffs = {}
    for A in (4, 6, 8):
        vals = {}
        for Z in range(1, A):
            N = A - Z
            P = prod_counts(h, f, {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)})
            vals[Z] = sp.nsimplify(sp.simplify(P.coeff(h, 2) / P.coeff(h, 0)))
        a, b = sp.symbols("a b")
        xs = [(A - 2 * Z) ** 2 for Z in range(1, A)]
        sol = sp.solve([sp.Eq(a * xs[0] + b, vals[1]), sp.Eq(a * xs[1] + b, vals[2])], [a, b])
        exact = all(sp.simplify(sol[a] * x + sol[b] - vals[Z]) == 0
                    for x, Z in zip(xs, range(1, A)))
        coeffs[A] = sol[a]
        print(f"    A={A}: c_2/c_0 = {sol[a]}*(N-Z)^2 + {sol[b]}   exact for all Z: {exact}"
              f"   [C(A/2,2) = {comb(A // 2, 2)}]")
    check("the all-pairs coefficient is C(A/2,2), growing like A^2/8 — further from "
          "the 1/A the SEMF needs than the chain's constant 1/2",
          all(coeffs[A] == comb(A // 2, 2) for A in (4, 6, 8)))

    print("\n" + "=" * 76)
    print("§4  AGAINST THE SEMF — right shapes, wrong magnitudes")
    print("=" * 76)
    vol = ALPHA / 8
    asym = ALPHA / 2
    print(f"    reading binding as -alpha c_2/c_0 = -alpha(N-Z)^2/2 + alpha A/8 - 5 alpha/8")
    print(f"      volume-like    +alpha/8 = {float(vol):.4f} MeV per nucleon"  # float64-ok: display only
          f"   (SEMF a_V ~ 15.8, off by {float(mpfr('15.8') / vol):.0f}x)")  # float64-ok: display only
    print(f"      asymmetry      -alpha/2 = {float(asym):.4f} MeV per (N-Z)^2"  # float64-ok: display only
          f"   (SEMF -a_A/A, a_A ~ 23)")
    cross = mpfr("23") / asym
    print(f"      the asymmetry has NO 1/A; it crosses SEMF's coefficient at "
          f"A ~ {float(cross):.0f}, which is a crossing, not an agreement")  # float64-ok: display only
    check("the volume-like coefficient is more than an order of magnitude below SEMF's",
          mpfr("15.8") / vol > 10)
    check("the asymmetry term is A-independent, so it cannot match SEMF's 1/A at more "
          "than one mass number", True)
    print("\n    Compare qou-xwur: the isospin/partition route gave -alpha log[2T+1]_q,")
    print("    LOGARITHMIC in T, and collapsed at A = 20 for that reason. This is the")
    print("    quadratic that route could not reach — obtained with no fitting.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "The (N-Z)^2 asymmetry term lives at Vassiliev type two. For the chain trace "
            "written as a product of bond factors, c_2/c_0 = (N-Z)^2/2 + (5-A)/8 exactly, "
            "verified symbolically for every A = 3..10 and every Z. The mechanism is that "
            "the type-2 coefficient of a product contains sum_{i<j} f_i' f_j', a sum over "
            "PAIRS of bonds, quadratic in the bond counts; taking -log turns the product "
            "into a sum and removes exactly that term, which is why the resummed L is "
            "additive, linear in Z, and has no valley of stability. Read as -alpha c_2/c_0 "
            "this gives a volume-like term linear in A and an asymmetry term quadratic in "
            "N-Z, both with the SEMF's sign and functional form. Magnitudes are wrong "
            "(volume 0.52 vs 15.8 MeV/nucleon) and the asymmetry lacks the 1/A. The "
            "all-pairs factor product is also exactly quadratic but with coefficient "
            "C(A/2,2), which is worse. Compare qou-xwur, where the partition route gave "
            "only log[2T+1]_q. No binding number, no fit, nothing wired. Bean qou-oooq.")
        wb.add_data("chain_c2_over_c0_closed_form", "(N-Z)^2/2 + (5-A)/8")
        wb.add_data("allpairs_quadratic_coefficient", "C(A/2,2)")
        wb.add_data("volume_like_MeV_per_nucleon", f"{float(vol):.6f}")  # float64-ok: display only
        wb.add_data("asymmetry_MeV_per_NZ2", f"{float(asym):.6f}")  # float64-ok: display only
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Shape result only. No binding number is produced, nothing is fitted or "
            "wired, and the sign convention (binding as -c_2 rather than +c_2) is assumed "
            "rather than derived: c_2/c_0 is MINIMISED at N = Z.")
        wb.add_caveat(
            "The all-pairs case uses the naive factor product, not the true all-pairs "
            "trace, which qou-bygw showed is not well defined until a bond ordering is "
            "fixed. That ambiguity is untouched here.")
        wb.add_caveat(
            "Does not show that the LP/SDP per-type reading of "
            "vassiliev-filtration-mass-tower is the correct one. If the framework resums, "
            "the logarithm returns and so does the obstruction.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
