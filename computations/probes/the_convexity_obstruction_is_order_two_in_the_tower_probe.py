#!/usr/bin/env python3
"""The convexity obstruction is ORDER TWO in the tower, and the first escape is
at order five: `L_pn - (L_pp + L_nn)/2` has `hbar`-expansion `-2 hbar^2 +
(4/3) hbar^5 + ...`, so the graded pieces at orders 5, 8, 10, 12, 13 put `pn`
ABOVE the midpoint. The escape is real and it is numerically irrelevant at the
substrate's coupling: the largest positive term is `7.6e-4` of the leading
negative one.

WHERE THIS SITS
---------------
Bean `qou-oooq`, opened on the owner's question "are you in the full tower, not
just order 0?". The answer was no: everything in `qou-mu1h` / `qou-bygw` was a
single Markov trace at `q_0`.

`the_pn_bond_is_an_average_and_cannot_be_extremal_probe` established an
obstruction with exactly two ingredients:

  1. the pn letter is a convex combination in the offset `d` — a statement about
     the ALGEBRA ELEMENT, so it survives to every order;
  2. `L = -log(trace)` is convex — order-zero-specific.

Jensen on (1) + (2) gives `L_pn < (L_pp + L_nn)/2`, hence the all-pairs binding
is convex in `Z`, hence no valley of stability in any sum-over-bonds model.
Ingredient (2) is the only one that could fail higher up. This probe tests it.

THE TOWER, STATED PRECISELY
---------------------------
Set `q = exp(hbar)`. The `hbar`-expansion IS the Vassiliev / `phi_q` grading:
the coefficient of `hbar^k` in a Hecke-trace observable is an order-`k` graded
piece, and `hbar -> 0` is the classical point `q = 1` where the deformation
switches off. So the order-`k` observable for bond type `X` is

    [hbar^k] L_X(hbar),        L_X = -log(z + d_X),  z = q^3/(q^2+1),

and the question "can `pn` be extremal at some order" is exactly the sign of

    Delta(hbar) = L_pn - (L_pp + L_nn)/2,   coefficient by coefficient.

MEASURED
--------
`delta = (q-1)^2 (1 - q^-4)/3 = (4/3) hbar^3 - (4/3) hbar^4 + (5/3) hbar^5 + ...`
is `O(hbar^3)`, so the pn letter is the EXACT midpoint of the pp and nn letters
through order `hbar^2` — the colour weighting is a third-order effect.

    k    [hbar^k] Delta      sign      term at hbar_0
    2         -2             NEG       -2.177e-02
    5          4/3           POS       +1.649e-05
    6        -59/45          NEG       -1.692e-06
    7         -5/9           NEG       -7.480e-08
    8        149/126         POS       +1.661e-08
    9         -7/54          NEG       -1.900e-10
   10       1537/3600        POS       +6.530e-11
   11     -14527/9072        NEG       -2.555e-11
   12    644251/2993760      POS       +3.583e-13
   13      88051/38880       POS       +3.935e-13

Orders 0, 1, 3, 4 vanish identically. **The obstruction is order two**, with the
clean coefficient `-2`, and the first order at which `pn` sits above the
midpoint is **five**.

VALIDATION
----------
Summed at `hbar_0 = log(q_0) = 0.104340720`, the series gives
`-0.021759232508` against the independently computed 200-bit value
`-0.021759233` from `the_pn_bond_is_an_average_and_cannot_be_extremal_probe`.
Nine digits, from a symbolic expansion on one side and an exact Markov trace on
the other. The expansion is what it claims to be.

WHAT THIS SETTLES, AND WHAT IT DOES NOT
---------------------------------------
It settles the bean's question in the interesting direction: **the obstruction
is NOT uniform across the tower.** Ingredient (2) genuinely fails at orders 5, 8,
10, 12 and 13, so an all-orders convexity theorem does not exist and the
order-zero result cannot be promoted to one.

It does not hand anyone a working model. At `hbar_0` the `k = 2` term is
`-2.18e-02` and the largest positive term is `+1.65e-05`, a ratio of `7.6e-4`.
Any observable that resums the tower is dominated by order two and inherits the
obstruction unchanged — which is exactly what the 200-bit measurement shows,
since it IS the resummation. The escape is available only to a reading that
takes a single graded piece as the physical observable, and nothing in this
probe argues that such a reading is correct.

So the honest summary is: the door is not locked, but nobody has shown there is
a room behind it.

WHAT IS NOT CLAIMED
-------------------
Not that any graded piece is the physical binding observable. Not that the
`phi_q` resummation and the Vassiliev filtration are the same grading — this
probe uses the `hbar`-expansion, which both are built on, and does not
distinguish them. Nothing about `A >= 3`, the closure, or the valley of
stability; those inherit whatever the bond constants do. No claim that a
positive graded piece would survive the other obstructions
(`qou-bygw`'s ordering ambiguity is untouched by any of this).
"""
from __future__ import annotations

import sys
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

NORD = 16
# the 200-bit value from the_pn_bond_is_an_average_and_cannot_be_extremal_probe
EXACT_DELTA = "-0.021759233"


def dec(x, k=12):
    """Decimal string of an mpfr, with the point where it belongs."""
    m, e, _ = gmpy2.digits(x, 10, k)
    sign = "-" if m.startswith("-") else ""
    m = m.lstrip("-")
    if 0 < e <= len(m):
        return f"{sign}{m[:e]}.{m[e:]}"
    return f"{sign}0.{'0' * (-e)}{m}" if e <= 0 else f"{sign}{m}e{e}"


def series_data(n=NORD):
    hb = sp.symbols("hbar")
    q = sp.exp(hb)
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    delta = (q - 1) ** 2 * (1 - q ** -4) / 3
    d = {"pp": sp.Integer(0), "nn": -h, "pn": -h * (1 - delta / 2) / 2}
    L = {k: sp.series(-sp.log(z + v), hb, 0, n).removeO().expand()
         for k, v in d.items()}
    D = sp.expand(L["pn"] - (L["pp"] + L["nn"]) / 2)
    coeffs = {}
    for k in range(n):
        c = sp.Rational(sp.nsimplify(D.coeff(hb, k), rational=True))
        if c != 0:
            coeffs[k] = c
    dser = sp.series(delta, hb, 0, 6).removeO().expand()
    return coeffs, dser, hb


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    coeffs, dser, hb = series_data()

    print("\n" + "=" * 74)
    print("§1  THE TOWER: q = exp(hbar), graded piece = [hbar^k]")
    print("=" * 74)
    print(f"    delta(hbar) = {dser}")
    lowest = min(int(t) for t in sp.Poly(dser, hb).monoms() and
                 [m[0] for m in sp.Poly(dser, hb).monoms()])
    print(f"    lowest order in delta: hbar^{lowest}  -> the pn letter is the EXACT")
    print(f"    midpoint of the pp and nn letters through order hbar^{lowest - 1};")
    print(f"    the colour weighting is a third-order effect.")
    check("delta = O(hbar^3), so the pn offset is the exact midpoint to order hbar^2",
          lowest == 3)

    print("\n" + "=" * 74)
    print("§2  Delta(hbar) = L_pn - (L_pp + L_nn)/2, ORDER BY ORDER")
    print("=" * 74)
    h0 = gmpy2.log(E.Q)
    print(f"    hbar_0 = log(q_0) = {dec(h0)}")
    print(f"    {'k':>3} {'[hbar^k] Delta':>22} {'sign':>6} {'term at hbar_0':>16}")
    pos, total = [], mpfr(0)
    for k in sorted(coeffs):
        c = coeffs[k]
        term = mpfr(c.p) / mpfr(c.q) * h0 ** k
        total += term
        if c > 0:
            pos.append(k)
        print(f"    {k:>3} {str(c):>22} {('POS' if c > 0 else 'NEG'):>6} "
              f"{float(term):>16.3e}")  # float64-ok: display only — term is mpfr
    print(f"\n    orders 0, 1, 3, 4 vanish identically")
    print(f"    orders with pn ABOVE the midpoint: {pos}")
    check("the obstruction is ORDER TWO, with coefficient exactly -2",
          coeffs.get(2) == sp.Integer(-2))
    check("orders 0, 1, 3 and 4 vanish identically",
          all(k not in coeffs for k in (0, 1, 3, 4)))
    check("the first order at which pn sits ABOVE the midpoint is FIVE, coefficient 4/3",
          pos and pos[0] == 5 and coeffs[5] == sp.Rational(4, 3))
    check("the obstruction is NOT uniform across the tower — several graded pieces "
          "are positive, so no all-orders convexity theorem exists",
          len(pos) >= 4)

    print("\n" + "=" * 74)
    print("§3  VALIDATION AGAINST THE 200-BIT MEASUREMENT")
    print("=" * 74)
    exact = mpfr(EXACT_DELTA)
    print(f"    series sum at hbar_0 = {dec(total)}")
    print(f"    200-bit exact Delta  = {EXACT_DELTA}   "
          f"(the_pn_bond_is_an_average_and_cannot_be_extremal_probe)")
    print(f"    |difference| = {float(abs(total - exact)):.2e}"  # float64-ok: display only
          f"   — symbolic expansion on one side, exact Markov trace on the other")
    check("the hbar-expansion reproduces the independently measured 200-bit Delta",
          abs(total - exact) < mpfr("1e-9"))

    print("\n" + "=" * 74)
    print("§4  THE ESCAPE IS FORMAL, NOT NUMERICAL")
    print("=" * 74)
    neg2 = mpfr(-2) * h0 ** 2
    c5 = coeffs[5]
    p5 = mpfr(c5.p) / mpfr(c5.q) * h0 ** 5
    ratio = abs(p5 / neg2)
    print(f"    leading NEG term  k=2 : {float(neg2):+.6e}")  # float64-ok: display only
    print(f"    largest POS term  k=5 : {float(p5):+.6e}")  # float64-ok: display only
    print(f"    ratio                 : {float(ratio):.2e}")  # float64-ok: display only
    check("the largest positive graded term is below 1e-3 of the leading negative one, "
          "so any resummed observable inherits the obstruction unchanged",
          ratio < mpfr("1e-3"))
    print("    => a reading that RESUMS the tower is dominated by order two and gains")
    print("       nothing; the escape is available only to a reading that takes a SINGLE")
    print("       graded piece as the physical observable, which nothing here justifies.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Lifting the pn-midpoint obstruction into the tower. With q = exp(hbar), the "
            "hbar-expansion is the Vassiliev/phi_q grading. Delta = L_pn - (L_pp+L_nn)/2 "
            "expands as -2 hbar^2 + (4/3) hbar^5 - (59/45) hbar^6 + ..., with orders 0, 1, "
            "3, 4 vanishing. The obstruction is order two; the first order putting pn "
            "ABOVE the midpoint is five, and orders 5, 8, 10, 12, 13 are positive, so no "
            "all-orders convexity theorem exists and the order-zero result cannot be "
            "promoted to one. The series summed at hbar_0 = log(q0) reproduces the "
            "independently computed 200-bit Delta to 9 digits. But the largest positive "
            "term is 7.6e-4 of the leading negative one, so any resummed observable "
            "inherits the obstruction unchanged: the escape is formal, available only to "
            "a reading that takes a single graded piece as physical. Bean qou-oooq.")
        for k in sorted(coeffs):
            wb.add_data(f"delta_coeff_hbar{k}", str(coeffs[k]))
        wb.add_data("first_positive_order", str(pos[0]))
        wb.add_data("positive_orders", str(pos))
        wb.add_data("series_sum_at_hbar0", dec(total, 15))
        wb.add_data("exact_200bit_delta", EXACT_DELTA)
        wb.add_data("largest_pos_over_leading_neg", f"{float(ratio):.4e}")  # float64-ok: display only
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Uses the hbar-expansion, which both the phi_q resummation and the Vassiliev "
            "filtration are built on; it does NOT distinguish the two gradings, and the "
            "bean's question of which tower is meant remains open.")
        wb.add_caveat(
            "No claim that any single graded piece is the physical binding observable. "
            "Without such a reading the positive orders are unusable, since the "
            "resummation is dominated by order two.")
        wb.add_caveat(
            "Says nothing about qou-bygw's ordering ambiguity, the valley of stability, "
            "or A >= 3; those inherit whatever the bond constants do.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
