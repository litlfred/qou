#!/usr/bin/env python3
"""`q_c = 3.4580993…` is not an unexplained constant — it is where the p-n average stops averaging.

RETRACTION OF MY OWN FRAMING
-----------------------------
`k_versus_selected_operator_probe.py` derived `q_c`, the single real root above 1
of `q^6 - 2q^5 - 5q^4 - q^2 + 2q - 1`, as the sign boundary of `D_PN` and hence
of the deuteron binding operator's inverse-crossing content. I flagged it as *"an
unexplained structural constant … nothing in the corpus references it"*.

**It has a complete explanation, and this probe gives it.** The "unexplained"
label is withdrawn. What survives is narrower and more useful: `q_c` is a
degree-6 algebraic number marking a **convexity boundary**, and the corpus does
not name it.

THE IDENTITY
------------
The colour-weighted `p`-`n` interface is `sigma - h(1/2 - delta/4) . 1` with
`delta = flavor_split_leading(q)`. Rearranged, that is exactly a weighted
average of the two crossing chiralities:

    sigma - h(1/2 - delta/4).1  =  (1/2 + delta/4) sigma  +  (1/2 - delta/4) sigma^-1

— the two weights summing to 1 identically. And the offset itself is

    D_PN(q)  =  -h(q) * (2 - delta(q)) / 4          [verified: difference is 0]

so for `q > 1` (where `h > 0`)

    D_PN < 0   <=>   delta < 2   <=>   the sigma^-1 weight is POSITIVE

**`q_c` is precisely the root of `delta(q) = 2`.** The sextic that appeared in the
`D_PN` numerator is that equation rearranged — verified identical, not merely
equal numerically:

    -6q^4 + (q-1)^2(q^4-1)   ==   numer(delta - 2)   ==   q^6 - 2q^5 - 5q^4 - q^2 + 2q - 1

WHAT HAPPENS THERE
------------------
At `delta = 2` the `sigma^-1` weight `(1/2 - delta/4)` is **exactly zero**:
the colour-weighted interface degenerates to a **pure `sigma`**, with no inverse
crossing at all. Beyond `q_c` the weight goes *negative* and the expression stops
being a convex combination — it is still a well-defined algebra element, but it
is no longer an average of the two chiralities.

So the three regimes are:

    1 < q < q_c    sigma^-1 weight > 0    genuine convex average; D_PN < 0
    q = q_c        sigma^-1 weight = 0    pure sigma; D_PN = 0
    q > q_c        sigma^-1 weight < 0    not a convex combination; D_PN > 0

and the earlier result — `K(2H)` lies outside the positive sector exactly on
`1 < q < q_c` — is now readable in one line: **the binding operator carries
inverse-crossing content exactly as long as the `p`-`n` interface actually
contains an inverse crossing.** That is a tautology once the identity is seen,
which is the right outcome for a constant that looked mysterious.

WHERE `q_0` SITS
----------------
    delta(q_0)        =  0.001375710807
    sigma weight      =  0.500343927702
    sigma^-1 weight   =  0.499656072298

so at the substrate value the interface is within `0.07 %` of the *symmetric*
average `(sigma + sigma^-1)/2` — `q_0` is not merely inside the convex regime, it
sits essentially at its centre, `delta` being three orders of magnitude below the
boundary value 2. `q_0 / q_c = 0.32098`.

WHAT REMAINS GENUINELY OPEN
----------------------------
Two small things, both stated so they are not overclaimed:

  - **The sextic is irreducible over `Q`**, so `q_c` is an algebraic number of
    degree exactly 6 — its own minimal polynomial. It is not a root of unity, not
    quadratic, and has no closed form in radicals worth writing.
  - **The corpus does not reference it.** A grep for `3.458` across
    `computations/`, `content/` and `docs/` returns only unrelated decimals
    (mass-table digits, an unrelated `3.4584e-12`). So `q_c` is a real boundary
    of the `PN_CONVENTION = "bring_color_weighted"` scheme that nothing in the
    corpus currently records — worth a line wherever that convention is
    documented, and nothing more.

Nothing here claims `q_c` is physically meaningful, and no physical quantity
enters the computation.

DISCIPLINE
----------
All exact: sympy closed form throughout, no floating point in any conclusion
except the reported decimal expansions. No fit; no `B_AME`; nothing wired.

-- Ref: [manuscript] bean t7qv; k_versus_selected_operator_probe.py;
   pyhecke.constants.pn_interface_offset
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

from pyhecke.constants import flavor_split_leading, pn_interface_offset  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

Q = sp.symbols("q", positive=True)


def main() -> int:
    assertions = []
    h = Q - 1 / Q
    delta = sp.simplify(flavor_split_leading(Q))
    dpn = sp.simplify(pn_interface_offset(Q))
    w_plus = sp.Rational(1, 2) + delta / 4
    w_minus = sp.Rational(1, 2) - delta / 4

    print("t7qv — what is q_c = 3.4580993…?")
    print(f"\n  delta(q) = {delta}")
    print(f"  D_PN(q)  = {sp.factor(dpn)}")

    # ── A1. D_PN = -h(2 - delta)/4, exactly ───────────────────────────
    resid = sp.simplify(dpn - (-h * (2 - delta) / 4))
    ok = resid == 0
    print(f"\n  A1  D_PN = -h(2 - delta)/4 identically ................... "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      residual = {resid}")
    print("      => for q > 1 (h > 0):  D_PN < 0  <=>  delta < 2")
    assertions.append(("dpn_equals_minus_h_times_2_minus_delta_over_4", ok,
                       f"residual {resid}"))

    # ── A2. The sextic IS `delta = 2` rearranged ──────────────────────
    sextic_from_dpn = sp.expand(-6 * Q ** 4 + (Q - 1) ** 2 * (Q ** 4 - 1))
    sextic_from_delta = sp.expand(sp.numer(sp.together(delta - 2)))
    ok = sp.simplify(sextic_from_dpn - sextic_from_delta) == 0
    print(f"\n  A2  the sextic IS the equation delta = 2 ................. "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      from D_PN numerator : {sextic_from_dpn}")
    print(f"      from delta - 2      : {sextic_from_delta}")
    assertions.append(("sextic_is_delta_equals_two", ok,
                       str(sp.expand(sextic_from_dpn))))

    # ── A3. The two chirality weights sum to 1; sigma^-1 vanishes at q_c
    sum_ok = sp.simplify(w_plus + w_minus) == 1
    qc = [r for r in sp.real_roots(sp.Poly(sextic_from_dpn, Q))
          if r.evalf() > 1][0]
    w_at_qc = sp.simplify(w_minus.subs(Q, qc))
    vanishes = abs(complex(sp.N(w_at_qc, 30)).real) < 1e-25
    ok = sum_ok and vanishes
    print(f"\n  A3  weights sum to 1, and sigma^-1 weight = 0 at q_c ..... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      sigma - h(1/2 - delta/4).1 = (1/2 + delta/4) sigma"
          " + (1/2 - delta/4) sigma^-1")
    print(f"      sigma^-1 weight at q_c = {sp.N(w_at_qc, 12)}")
    print("      => at q_c the p-n interface is a PURE sigma. Beyond it the")
    print("         weight is negative and it is no longer a convex average.")
    assertions.append(("sigma_inverse_weight_vanishes_at_qc", ok,
                       f"weights sum to 1: {sum_ok}; w-(q_c) = {sp.N(w_at_qc, 6)}"))

    # ── A4. q_0 sits essentially at the centre of the convex regime ───
    q0 = sp.Float(str(Q0), 30)
    d0 = delta.subs(Q, q0)
    wp0, wm0 = w_plus.subs(Q, q0), w_minus.subs(Q, q0)
    ok = bool(sp.N(d0) < sp.Rational(1, 100)) and bool(abs(sp.N(wm0 - sp.Rational(1, 2))) < sp.Rational(1, 100))
    print(f"\n  A4  q_0 is deep inside the convex regime ................. "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      delta(q_0)      = {sp.N(d0, 12)}   (boundary value is 2)")
    print(f"      sigma weight    = {sp.N(wp0, 12)}")
    print(f"      sigma^-1 weight = {sp.N(wm0, 12)}")
    print(f"      q_0/q_c         = {sp.N(q0 / qc, 10)}")
    print("      => within 0.07 % of the SYMMETRIC average (sigma+sigma^-1)/2.")
    assertions.append(("q0_is_deep_inside_the_convex_regime", ok,
                       f"delta(q_0) = {sp.N(d0, 10)}, w- = {sp.N(wm0, 10)}"))

    # ── A5. What genuinely remains: degree 6, and unrecorded ──────────
    irred = sp.Poly(sextic_from_dpn, Q).is_irreducible
    minpoly = sp.minimal_polynomial(qc, Q)
    deg = sp.Poly(minpoly, Q).degree()
    ok = bool(irred) and deg == 6
    print(f"\n  A5  q_c is algebraic of degree exactly 6 ................. "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      sextic irreducible over Q: {irred}")
    print(f"      minimal polynomial: {minpoly}")
    print(f"      q_c = {sp.N(qc, 30)}")
    assertions.append(("qc_is_degree_six_algebraic", ok,
                       f"irreducible {irred}, degree {deg}"))

    print("\n### VERDICT: q_c is NOT an unexplained constant — my own earlier")
    print("    label is withdrawn. It is the root of delta(q) = 2, i.e. the")
    print("    point where the colour-weighted p-n interface degenerates from a")
    print("    convex average of sigma and sigma^-1 into a PURE sigma. The")
    print("    earlier result — K(2H) leaves the positive sector exactly on")
    print("    1 < q < q_c — is then a tautology: the binding operator carries")
    print("    inverse-crossing content exactly while the p-n interface has an")
    print("    inverse crossing in it. What remains is small and true: q_c is")
    print("    algebraic of degree 6, and nothing in the corpus records it.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("qc-convexity-boundary", engine="sympy",
                                output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): explains q_c = 3.4580993..., which "
                "k_versus_selected_operator_probe derived as the sign boundary "
                "of D_PN and which I there flagged as 'an unexplained "
                "structural constant'. That label is WITHDRAWN. Exactly, "
                "D_PN = -h(2 - delta)/4, so for q > 1 D_PN < 0 iff delta < 2, "
                "and the sextic in the D_PN numerator IS the equation delta = 2 "
                "rearranged (verified identical symbolically). The "
                "colour-weighted p-n interface is a weighted average "
                "(1/2 + delta/4) sigma + (1/2 - delta/4) sigma^-1 whose weights "
                "sum to 1; at q_c the sigma^-1 weight is exactly ZERO, so the "
                "interface degenerates to a pure sigma, and beyond q_c the "
                "weight is negative and it is no longer a convex combination. "
                "The earlier result that K(2H) leaves the positive sector "
                "exactly on 1 < q < q_c is then a tautology. At q_0, "
                "delta = 0.0013757 and the weights are 0.50034/0.49966 — within "
                "0.07% of the symmetric average, three orders of magnitude "
                "below the boundary. What genuinely remains: the sextic is "
                "irreducible over Q so q_c is algebraic of degree exactly 6, "
                "and a grep of computations/, content/ and docs/ finds nothing "
                "in the corpus recording it. All exact (sympy). No fit; no "
                "B_AME; no physical claim.")
            wb.add_data("delta", str(delta))
            wb.add_data("D_PN_factored", str(sp.factor(dpn)))
            wb.add_data("identity_residual", str(resid))
            wb.add_data("sextic", str(sextic_from_dpn))
            wb.add_data("sigma_inv_weight_at_qc", str(sp.N(w_at_qc, 20)))
            wb.add_data("q_c", str(sp.N(qc, 30)))
            wb.add_data("q_c_minimal_polynomial", str(minpoly))
            wb.add_data("q_c_degree", int(deg))
            wb.add_data("at_q0", {"delta": str(sp.N(d0, 15)),
                                  "w_sigma": str(sp.N(wp0, 15)),
                                  "w_sigma_inv": str(sp.N(wm0, 15)),
                                  "q0_over_qc": str(sp.N(q0 / qc, 15))})
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "RETRACTION: k_versus_selected_operator_probe called q_c 'an "
                "unexplained structural constant'. It is explained — the root "
                "of delta = 2, the convexity boundary of the colour-weighted "
                "p-n average. Only two narrower claims survive: q_c is "
                "algebraic of degree exactly 6, and the corpus does not record "
                "it.")
            wb.add_caveat(
                "This is a boundary of the PN_CONVENTION = 'bring_color_"
                "weighted' scheme specifically. Under 'strict_averaged' the "
                "offset is -h/2 with no delta, the weights are 1/2 and 1/2 at "
                "every q, and no such boundary exists. So q_c is a property of "
                "the colour weighting, not of the Hecke algebra.")
            wb.add_caveat(
                "No physical claim. Nothing here says q_c is meaningful beyond "
                "the algebra, and no physical quantity enters the computation.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
