#!/usr/bin/env python3
"""qou-99qc, option (1): can the corpus's OTHER crossing template rescue the
prose description of `Delta`? No. The exclusion extends to all four.

WHAT THIS ANSWERS. `qou-avt6` proved, scope-(b), that no difference of two
TYPED-CROSSING words has counit `epsNPq = h(h-2)/2`, and fenced itself
explicitly:

    "colour-weighted crossings fall outside the q^m([2]/2)^c normal form, so
     do NOT quote the exclusion for words that do."

That carve-out was the last place the prose could still be right. This closes
it: admitting `averaged_weighted` does NOT let a two-word difference reach
`epsNPq` either.

FIRST, DISPOSE OF THE VACUOUS READING. The counit is an algebra homomorphism
onto Q(q), so it is SURJECTIVE -- `eps(epsNPq * 1) = epsNPq` trivially, and
indeed the skein relation makes `sigma - sigma^-1 = h` a scalar outright. So
"does an element with this counit exist" is not a real question; the content
is entirely in WHICH CLASS the element is drawn from. The class the prose
names is "difference of the neutron and proton typed-crossing elements", and
that is what is excluded here.

THE FOURTH TEMPLATE. `canonical_braid_crossings.d_for_ctype` recognises
exactly four: sigma (d=0), sigma_inv (d=-h), averaged (d=-h/2), and
averaged_weighted (d = -h(1/2 - delta/4)) with the substrate flavour split

    delta(q) = (q-1)^2 (1 - q^-4) / 3        [flavor_split_leading, exact]

so the fourth crossing's counit is a genuine rational function of q,

    w(q) = q - h(q)*(1/2 - delta(q)/4),

and `eps` of any word over the four templates is  q^m ([2]_q/2)^c w^k.

THE ARGUMENT. Same silver-ratio route, one more generator. At q = 1 + sqrt2:

    epsNPq  = 0          (its factor q^2 - 2q - 1 vanishes)
    h       = 2          exactly -- (1+sqrt2) - (sqrt2-1)
    [2]_q/2 = sqrt2      exactly
    w       = (15 sqrt2 - 16)/3

A two-word difference vanishing there forces
`(1+sqrt2)^M (sqrt2)^C w^K = 1` with M, C, K the exponent differences. Take
ABSOLUTE NORMS in Q(sqrt2), N(a + b sqrt2) = a^2 - 2b^2, which is
multiplicative:

    |N(1+sqrt2)| = 1        the fundamental unit
    |N(sqrt2)|   = 2
    |N(w)|       = 194/9  =  2 * 97 / 3^2       <- the new ingredient

giving  2^(C+K) * 97^K * 3^(-2K) = 1.  Unique factorisation in Q_{>0} reads
off K = 0 from the 97, then C = 0 from the 2, then M = 0 since 1+sqrt2 is not
a root of unity. The difference is identically zero; `epsNPq` is not. QED

97 is what does the work, and it is not a coincidence anyone arranged: it is
whatever prime the flavour split happens to contribute at that point. Had
|N(w)| been a power of 2 the argument would have failed and the probe would
say so -- CHECK 4 tests the factorisation rather than asserting it.

CONTROL, so the argument does not prove too much: `chi_block_3` IS such a
difference and must survive. It does, at (M,C,K) = (-2,0,0).

ARITHMETIC. Exact throughout -- sympy over Q(q), and the norms as exact
rationals via `sympy.Rational`. No float anywhere.

WHAT THIS DOES NOT DO. It does not adjudicate the qou-99qc fork. It removes
one of the two escapes from option (1): the prose cannot be repaired by
widening the crossing vocabulary. What remains open is whether `Delta` is a
difference of two words AT ALL, and whether `epsNPq` is simply wrong.
"""

from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/substrate",
           "tools/qou-substrate/python"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

q = sp.Symbol("q", positive=True)
h = q - 1 / q
SILVER = 1 + sp.sqrt(2)

# The corpus's asserted counit, from QOU.Interactions.QBetaEnergyScale.epsNPq.
EPS_NP = sp.cancel(h * (h - 2) / 2)

# The four crossing counits eps(sigma_g + d) = q + d, one per d_for_ctype row.
DELTA = (q - 1) ** 2 * (1 - q ** -4) / 3          # flavor_split_leading
COUNIT = {
    "sigma":             sp.cancel(q),
    "sigma_inv":         sp.cancel(q - h),
    "averaged":          sp.cancel(q - h / 2),
    "averaged_weighted": sp.cancel(q - h * (sp.Rational(1, 2) - DELTA / 4)),
}


def norm_q_sqrt2(x) -> sp.Rational:
    """|N(a + b sqrt2)| = |a^2 - 2 b^2|, for x in Q(sqrt2). Exact."""
    x = sp.nsimplify(sp.radsimp(sp.expand(x)))
    poly = sp.Poly(sp.expand(x), sp.sqrt(2))
    if poly.degree() > 1:
        raise ValueError(f"not in Q(sqrt2): {x}")
    b = sp.Rational(poly.coeff_monomial(sp.sqrt(2)) or 0)
    a = sp.Rational(poly.coeff_monomial(1) or 0)
    return sp.Abs(a ** 2 - 2 * b ** 2)


RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


def main() -> int:
    print("qou-99qc option (1) — does the colour-weighted template rescue the prose?\n")

    # ---- 0. the vacuous reading, disposed of -------------------------------
    print("CHECK 0 — the counit is surjective, so 'does an element exist' is vacuous")
    skein = sp.simplify(COUNIT["sigma"] - COUNIT["sigma_inv"] - h)
    check("skein_makes_sigma_minus_sigma_inv_a_scalar", skein == 0,
          "eps(sigma) - eps(sigma^-1) = h; and sigma - sigma^-1 = h in the algebra")
    check("epsNPq_is_a_scalar_in_Qq",
          sp.simplify(EPS_NP - sp.cancel(h * (h - 2) / 2)) == 0,
          f"epsNPq = {sp.factor(EPS_NP)} — so eps(epsNPq * 1) = epsNPq trivially")
    print()

    # ---- 1. the silver-ratio evaluations, all four -------------------------
    print("CHECK 1 — evaluations at the silver ratio 1 + sqrt2")
    vals = {k: sp.radsimp(sp.simplify(v.subs(q, SILVER))) for k, v in COUNIT.items()}
    eps_at = sp.simplify(EPS_NP.subs(q, SILVER))
    h_at = sp.simplify(h.subs(q, SILVER))
    check("epsNPq_vanishes_at_silver", sp.simplify(eps_at) == 0,
          "the factor q^2 - 2q - 1 is what vanishes")
    check("h_is_exactly_two_at_silver", sp.simplify(h_at - 2) == 0)
    check("averaged_counit_is_sqrt2_at_silver",
          sp.simplify(vals["averaged"] - sp.sqrt(2)) == 0,
          f"[2]_q/2 = {vals['averaged']}")
    w = vals["averaged_weighted"]
    w_expected = (15 * sp.sqrt(2) - 16) / 3
    check("colour_weighted_counit_at_silver",
          sp.simplify(w - w_expected) == 0,
          f"w = {sp.nsimplify(w)} = {sp.N(w, 12)}")
    print()

    # ---- 2. the norms ------------------------------------------------------
    print("CHECK 2 — absolute norms in Q(sqrt2)")
    n_sigma = norm_q_sqrt2(vals["sigma"])
    n_avg = norm_q_sqrt2(vals["averaged"])
    n_w = norm_q_sqrt2(w)
    check("norm_sigma_is_one", n_sigma == 1, "1 + sqrt2 is the fundamental unit")
    check("norm_averaged_is_two", n_avg == 2)
    check("norm_colour_weighted", n_w == sp.Rational(194, 9),
          f"|N(w)| = {n_w} = 2 * 97 / 3^2")
    # sigma_inv is 1/sigma, so it contributes -1 to the same exponent M.
    check("sigma_inv_is_the_inverse_of_sigma",
          sp.simplify(vals["sigma_inv"] * vals["sigma"] - 1) == 0,
          "so sigma^-1 shifts M by -1 rather than adding a generator")
    print()

    # ---- 3. the exclusion, from unique factorisation -----------------------
    print("CHECK 3 — the norm equation forces M = C = K = 0")
    M, C, K = sp.symbols("M C K", integer=True)
    # |N|: 1^M * 2^C * (2*97/9)^K = 1  ->  2^(C+K) * 97^K * 3^(-2K) = 1
    expo_97 = K
    expo_3 = -2 * K
    expo_2 = C + K
    sol = sp.solve([expo_97, expo_3, expo_2], [M, C, K], dict=True)
    forced = sol and all(s.get(C, 0) == 0 and s.get(K, 0) == 0 for s in sol)
    check("norm_equation_forces_C_and_K_zero", bool(forced),
          "97^K = 1 => K = 0; then 2^C = 1 => C = 0")
    check("silver_ratio_is_not_a_root_of_unity", sp.N(SILVER, 10) > 1,
          "1 + sqrt2 > 1, so (1+sqrt2)^M = 1 forces M = 0")
    print()

    # ---- 4. the argument is not circular: test the factorisation -----------
    print("CHECK 4 — the argument DEPENDS on |N(w)| carrying an odd prime")
    num, den = sp.fraction(sp.Rational(n_w))
    odd_primes = [p for p in sp.factorint(num) if p != 2]
    check("norm_w_carries_an_odd_prime", bool(odd_primes) or den != 1,
          f"|N(w)| = {n_w}; odd primes in numerator: {odd_primes}, denominator {den}. "
          "Had this been a pure power of 2 the exclusion would NOT follow.")
    print()

    # ---- 5. bounded independent sweep + the control ------------------------
    print("CHECK 5 — bounded sweep, and the chi_block_3 control")
    chi3 = sp.cancel(-(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q))
    probes = [sp.Rational(13, 10), sp.Rational(77, 100), sp.Rational(23, 20)]

    def sweep(target):
        hits = []
        for m1, c1, k1, m2, c2, k2 in product(range(-6, 7), range(0, 4), range(0, 3),
                                              range(-6, 7), range(0, 4), range(0, 3)):
            if (m1, c1, k1) == (m2, c2, k2):
                continue
            ok = True
            for qv in probes:
                a = (COUNIT["sigma"] ** m1 * COUNIT["averaged"] ** c1
                     * COUNIT["averaged_weighted"] ** k1).subs(q, qv)
                b = (COUNIT["sigma"] ** m2 * COUNIT["averaged"] ** c2
                     * COUNIT["averaged_weighted"] ** k2).subs(q, qv)
                if sp.simplify(sp.nsimplify(a - b) - target.subs(q, qv)) != 0:
                    ok = False
                    break
            if ok:
                hits.append((m1, c1, k1, m2, c2, k2))
        return hits

    eps_hits = sweep(EPS_NP)
    chi_hits = sweep(chi3)
    check("sweep_finds_no_epsNPq_representation", len(eps_hits) == 0,
          f"m in [-6,6], c in [0,3], k in [0,2] at three generic q — {len(eps_hits)} hits")
    check("sweep_finds_the_chi_block_3_control", len(chi_hits) > 0,
          f"control found at {chi_hits[:2]} — the argument does not prove too much")
    print()

    ok = all(r[1] for r in RESULTS)
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — the qou-avt6 exclusion extends to ALL FOUR crossing templates.")
    print("The prose describing Delta cannot be repaired by widening the crossing")
    print("vocabulary. Still open, and still the owner's call: whether Delta is a")
    print("two-word difference at all, and whether epsNPq is simply wrong.")

    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder("qbeta-epsnpq-colour-weighted-exclusion", _script_path=__file__)
        wb.set_description(
            "Extends the qou-avt6 scope-(b) exclusion to the colour-weighted "
            "crossing template, closing the carve-out avt6 named. No difference "
            "of two words over ALL FOUR templates has counit epsNPq."
        )
        wb.add_data("markov_convention", "not applicable — no z enters this computation")
        wb.add_data("q0_anchor",
                    "none — symbolic in q; delta uses the exact closed form "
                    "flavor_split_leading(q), never the q0-pinned cache")
        wb.add_data("colour_weighted_counit_at_silver", str(sp.nsimplify(w)))
        wb.add_data("absolute_norms_in_Q_sqrt2",
                    {"sigma": str(n_sigma), "averaged": str(n_avg),
                     "averaged_weighted": str(n_w)})
        wb.add_caveat(
            "scope-(b) on a proved invariant (unique factorisation of absolute "
            "norms in Q(sqrt2)), fenced to the class 'difference of TWO words "
            "over the four d_for_ctype templates'. It says nothing about "
            "elements outside that class, and it does not adjudicate qou-99qc."
        )
        for name, passed, det in RESULTS:
            wb.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        wb.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
