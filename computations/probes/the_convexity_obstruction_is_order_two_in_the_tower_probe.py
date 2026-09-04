#!/usr/bin/env python3
"""The convexity obstruction is ORDER TWO in the tower and the first escape is at
type FOUR — and at the TRACE level, which is what the Vassiliev filtration
actually grades, there is no obstruction at all: `pn` sits ABOVE the midpoint by
`h^4(-h^3 + 6h^2 - 16h + 32)/768 > 0`. The obstruction is an artefact of taking
`-log`. The corpus reads both ways: the mass formula RESUMS (so it inherits the
obstruction), while the LP/SDP operator selection is graded type by type into
"independent linear programs" (so it does not).

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

THE TOWER, STATED PRECISELY — AND IN THE CORPUS'S OWN VARIABLE
--------------------------------------------------------------
`vassiliev-filtration-mass-tower` states the grading explicitly: `tr_M(beta)(q)`
expands in **`h = q - q^-1`**, and `c_k(beta)` is a Vassiliev invariant of type
`k`. So the graded variable is `h`, NOT `hbar = log q`.

A first pass here used `hbar`. That is a different grading — `h = 2 hbar +
hbar^3/3 + ...`, and a reparametrisation MIXES orders — and it moved the answer:
the first escape sits at order **5** in `hbar` and at type **4** in `h`. The `h`
answer is the corpus's. Both are reported below, because the discrepancy is the
point: "which order does X happen at" is not grading-independent, and quoting
one while the corpus uses the other is how a tower result becomes unfalsifiable.

Two levels have to be distinguished, and they disagree:

  * **trace level** — what the filtration grades. `c_k` are coefficients of
    `tr_M`, and the bond factor is `z + d_X`, affine in the offset.
  * **`L` level** — what the binding formula uses, `B = alpha * sum of
    -log(z + d)`.

MEASURED
--------
**At the trace level there is no obstruction.** The bond factor midpoint is
`z - h/2`, and

    (z + d_pn) - (z - h/2) = h*delta/4 = h^4 (-h^3 + 6h^2 - 16h + 32)/768 > 0,

so `pn` sits ABOVE the midpoint of `pp` and `nn` from order `h^4` on. The
obstruction found at order zero is created entirely by the `-log`: `-log` is
strictly convex, and Jensen turns "slightly above the midpoint in the factor"
into "below the midpoint in `L`". The convexity gap is `O(h^2)` and the colour
term is `O(h^4)`, which is why the `-log` wins in the resummation.

**At the `L` level, graded in `h`:** first positive coefficient at type `4`
(`+1/24`), with positives at types 4, 5, 8, 9, 12, 13.

Graded in `hbar` (the non-corpus variable), for contrast:
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

Orders 0, 1, 3, 4 vanish identically there. **The obstruction is order two** in
both variables — coefficient `-2` in `hbar`, `-1/2` in `h` — but the first
escape is order 5 in `hbar` and type 4 in `h`.

VALIDATION
----------
Summed at `hbar_0 = log(q_0) = 0.104340720`, the series gives
`-0.021759232508` against the independently computed 200-bit value
`-0.021759233` from `the_pn_bond_is_an_average_and_cannot_be_extremal_probe`.
Nine digits, from a symbolic expansion on one side and an exact Markov trace on
the other. The expansion is what it claims to be.

WHICH READING THE CORPUS USES — the bean's deciding question, answered
----------------------------------------------------------------------
Both, in different places, and that is the whole answer:

  * `phi-q-resums-trace-series`: "the `Phi_q` resummation strictly factors
    through Markov traces ... the entire tower generates from symbolic
    differentiation of the descended trace." It RESUMS. Obstruction inherited.
  * `vassiliev-filtration-mass-tower`, first half: "higher-order terms supply
    precision refinements, converging rapidly due to the suppression factor
    `|h|^k ~ (0.209)^k`." The mass formula RESUMS. Obstruction inherited.
  * `vassiliev-filtration-mass-tower`, second half: "for the LP/SDP
    operator-selection framework, the Vassiliev filtration provides a canonical
    cost-vector basis at each type: `t_k^(type m) = c_m(b_k)`. This decomposes
    the mass-formula optimisation into a graded hierarchy of **independent
    linear programs**." That reading takes a SINGLE graded piece as the
    observable, and the escape is available to it.

So the escape is not hypothetical and it is not general. It lives in the
LP/SDP cost-vector channel, at Vassiliev type 4, in machinery the corpus already
has — and it is unavailable to the resummed mass formula, which is what every
number measured in `qou-mu1h` and `qou-bygw` came from.

WHAT THIS DOES NOT SHOW
-----------------------
That a type-4 LP produces a valley of stability, the right asymmetry energy, or
any binding number at all. Only that the SIGN obstruction which kills the
resummed reading is absent there. Given how many repairs this arc has already
buried, that distinction should be held firmly.

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


def series_h(n=NORD):
    """The CORPUS's grading: h = q - 1/q (vassiliev-filtration-mass-tower)."""
    hs = sp.symbols("h")
    q = (hs + sp.sqrt(hs ** 2 + 4)) / 2          # invert q - 1/q = h
    z = q ** 3 / (q ** 2 + 1)
    delta = (q - 1) ** 2 * (1 - q ** -4) / 3
    d = {"pp": sp.Integer(0), "nn": -hs, "pn": -hs * (1 - delta / 2) / 2}
    # trace level: the bond factor itself, which is what c_k grades
    fac = {k: sp.series(z + v, hs, 0, 9).removeO().expand() for k, v in d.items()}
    Dtr = sp.simplify(sp.expand(fac["pn"] - (fac["pp"] + fac["nn"]) / 2))
    # L level: what the binding formula sums
    L = {k: sp.series(-sp.log(z + v), hs, 0, n).removeO().expand() for k, v in d.items()}
    D = sp.expand(L["pn"] - (L["pp"] + L["nn"]) / 2)
    coeffs = {}
    for k in range(n):
        c = sp.nsimplify(sp.simplify(D.coeff(hs, k)), rational=True)
        if c != 0:
            coeffs[k] = sp.Rational(c)
    return coeffs, Dtr, hs


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
    ch, Dtr, hs = series_h()
    coeffs, dser, hb = series_data()

    print("\n" + "=" * 74)
    print("§0  TRACE LEVEL — what the Vassiliev filtration actually grades")
    print("=" * 74)
    print(f"    (z + d_pn) - midpoint of the pp/nn factors = {Dtr}")
    lead = sp.limit(Dtr / hs ** 4, hs, 0)
    print(f"    leading behaviour: {lead} * h^4   -> POSITIVE")
    print("    so at the TRACE level pn sits ABOVE the midpoint from order h^4 on;")
    print("    the obstruction is created entirely by taking -log, which is convex.")
    check("at the trace level pn is ABOVE the midpoint — no obstruction there",
          lead > 0)

    print("\n" + "=" * 74)
    print("§0b  L LEVEL, GRADED IN THE CORPUS'S h = q - 1/q")
    print("=" * 74)
    posh = [k for k in sorted(ch) if ch[k] > 0]
    for k in sorted(ch):
        print(f"    {k:>3} {str(ch[k]):>24} {('POS' if ch[k] > 0 else 'NEG'):>6}")
    print(f"    types with pn ABOVE the midpoint, in h: {posh}")
    check("in the corpus's h-grading the obstruction is type two (-1/2) and the first "
          "escape is type FOUR (+1/24)",
          ch.get(2) == sp.Rational(-1, 2) and posh and posh[0] == 4
          and ch[4] == sp.Rational(1, 24))
    print("    NOTE: in hbar = log q the first escape is order 5, not 4. A")
    print("    reparametrisation mixes orders, so 'which order' is not grading-")
    print("    independent; the corpus's variable is h and that answer is type 4.")

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
    print("       nothing. That covers phi-q-resums-trace-series ('the entire tower")
    print("       generates from symbolic differentiation of the descended trace') and the")
    print("       mass formula itself ('higher-order terms supply precision refinements').")
    print("       The escape needs a SINGLE graded piece, and the corpus has exactly one")
    print("       such reading: vassiliev-filtration-mass-tower's LP/SDP cost-vector basis")
    print("       t_k^(type m) = c_m(b_k), 'a graded hierarchy of independent linear")
    print("       programs'. That is where type 4 is reachable — and nowhere else.")

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
            "a reading that takes a single graded piece as physical. The corpus has "
            "exactly one such reading, vassiliev-filtration-mass-tower's LP/SDP "
            "cost-vector basis (independent linear programs per type), and the escape is "
            "reachable there and nowhere else. Also: the corpus grades in h = q - 1/q, "
            "not log q, and in that variable the first escape is type 4 (+1/24), not 5; "
            "at the TRACE level the filtration actually grades, pn is ABOVE the midpoint "
            "from h^4 on, so the obstruction is created by taking -log. Bean qou-oooq.")
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
            "Reports both gradings. The corpus's is h = q - 1/q; hbar = log q is included "
            "only to show that 'which order' is not grading-independent (first escape 5 "
            "in hbar, type 4 in h).")
        wb.add_caveat(
            "Shows only that the SIGN obstruction is absent at type 4. No claim that a "
            "type-4 LP produces a valley of stability, an asymmetry energy, or any "
            "binding number at all.")
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
