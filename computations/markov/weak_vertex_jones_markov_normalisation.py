#!/usr/bin/env python3
"""
weak_vertex_jones_markov_normalisation.py — the weak-vertex trace's
normalisation IS the Jones-Markov relation, and the invariant-normalised
coupling is a product of two q-differences at the Jones exponents.

WHAT THIS DERIVES (bean qou-q2l7; owner: "derive coupling normalization",
2026-09-05).  qou-pfh7 EXCLUDED the family c*(W - W(1))*bridge by proving the
ratio runs, and left the normalisation itself open.  This closes that: the
normalisation is not a free constant to be found, it is fixed by topology.

1. THE NORMALISATION RULE.  For a braid word beta in B_n with exponent sum e,
   the canonical Markov trace of its closure is

       tr_M(closure beta) = q^(2e) * V_{closure beta}(q^-2) / [2]_q^(n-1)

   i.e. the trace is the Jones polynomial re-scaled by a FRAMING factor q^(2e)
   (the writhe correction, in the variable t = q^-2) and a RANK factor
   [2]_q^(n-1) (the Markov normalisation tr_M(1) = 1 on H_n).  Both factors are
   read off the braid word; neither is fitted.  Verified here against the
   canonical engine (markov_trace_canonical.tr_M_word, convention D) on eight
   torus knots spanning n = 2, 3, 4, 5 and including the mirror pairs
   T(3,4)/T(4,3) and T(3,5)/T(5,3).

   For the weak vertex T(3,5) = closure of (s1 s2)^5, n = 3 and e = 10:

       W * [2]_q^2 = q^12 + q^8 - 1 = q^20 * J,   J := V_{T(3,5)}(q^-2)
                                                    = q^-8 + q^-12 - q^-20

2. WHY THAT FIXES THE NORMALISATION WITH NO FREE CONSTANT.  V_K(1) = 1 and
   V'_K(1) = 0 for EVERY knot K (checked below on all eight).  So

       J - 1

   is the canonically-normalised deviation of the weak vertex from its classical
   value: the offset (1) and the vanishing order (2) are topological facts, not
   choices.  There is nothing left to rescale.  This is what W - W(1) was trying
   to be, and failed to be, in qou-pfh7 — W(1) = 1/4 is the trace's Markov
   normalisation showing through, not a knot invariant.

3. THE COUPLING IS A PRODUCT OF TWO q-DIFFERENCES.  Exactly, with
   h_k := q^k - q^-k:

       J - 1 = - h_4 * h_6 / q^10

   The two exponents 4 and 6 are the two Jones exponents of T(3,5)
   (V = t^4 + t^6 - t^10), and q^-10 is the framing.  Since h_k(1) = 0 and
   h_k'(1) = 2k, this vanishes to SECOND order automatically, with

       leading coeff = -(2*4)(2*6) = -96,    J''(1) = -192

   That is the derivation the excluded family lacked: second-order vanishing is
   not arranged by a bridge factor, it is a consequence of TWO q-differences.

4. WHAT THE beta-DECAY COUPLING IS, IN THE SAME LANGUAGE.  The rate's s^2 is
   also a product of two q-differences — the same one twice, at half scale:

       s^2 = (q^(1/2) - q^(-1/2))^2 = h_(1/2)^2,   h_(1/2)'(1) = 1

   So both objects are products of two q-differences vanishing to second order.
   They differ in WHICH exponents: {4, 6} for the trace, {1/2, 1/2} for the
   rate.  The leading ratio is therefore exactly

       (J - 1) / s^2  ->  -(2*4)(2*6) / (2*(1/2))^2  =  -96

5. THE RATIO IN CLOSED FORM — no limit, no derivative.  Clearing the framing
   turns (3) into a polynomial identity, and the cofactors are cyclotomic:

       q^20 * (J - 1) = -(q^8 - 1)(q^12 - 1)
       q^19 * (J - 1) = - s^2 * G_8(q) * G_12(q),    G_n(q) := 1 + q + ... + q^(n-1)

   so the ratio of the two couplings is EXACTLY

       (J - 1) / s^2 = - G_8(q) * G_12(q) / q^19

   which is -G_8(1)*G_12(1) = -8*12 = -96 at q = 1 and -37.0915 at q0.  The
   second-order vanishing, the leading coefficient, AND the running are all read
   off one rational function; nothing here is a limit or a numerical fit.  This
   is the form the Lean carries, which is why it stays over a generic field.

6. WHAT THIS DOES AND DOES NOT SETTLE.
   🛑 RETRACTED 2026-09-05 (bean qou-xql6).  This section claimed the ORDER of the
   substitution factor measured in qou-ix74 was DERIVED -- "96^2 = 9216 against the
   measured |W(q0)|^2/s(q0)^4 = 11875.4418936763 -- an overshoot of exactly
   1.2885679138".  Both halves are wrong.

   (i) THE COMPARISON IS A CATEGORY ERROR.  -96 is the classical value of
   (J-1)/s^2, in which the NUMERATOR vanishes: J(1) = 1 because V_K(1) = 1 for
   every knot.  The substitution factor's numerator does not vanish -- W(1) = 1/4
   is the Markov rank factor -- so |W|^2/s^k diverges as q -> 1 for every k >= 1
   and has NO leading constant.  There was nothing for -96 to be the order of.

   (ii) THE POWER WAS WRONG.  sSq/S_SQ is already s^2, so |W|^2/S_SQ^2 is |W|^2/s^4,
   while the rate carries s^2 exactly once (prf:trace-ratio-observable:
   |M_q|^2 = |skein_amp|^2 * |tr ratio|^2, skein_amp = q^(1/2) - q^(-1/2)).  The
   factor is 129.405107404, not 11875.4418936763.

   So this producer derives the NORMALISATION and nothing about the rate's
   magnitude.  Every identity in sections 1-5 is untouched and re-verified.  The
   qou-ix74 scope-(a) negative also survives at the corrected magnitude: 129x
   still cannot be a 10-17 % correction.

   HONEST LIMIT.  s^2 = h_(1/2)^2 is a formal HALF-SCALE analogue, not itself a
   Jones deviation: its exponents are 1/2, and a Jones exponent is an integer,
   so no knot's V - 1 equals s^2.  The derivation therefore explains the
   magnitude gap between the two couplings; it does not remove it, and it does
   not license substituting either for the other.

Precision: sympy-exact throughout; numerics mpmath at 60 dps evaluated from the
exact expressions; serialised at 50 digits.  No float is formed.

Output: computations/weak-vertex-jones-markov-normalisation.witness.json
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from markov_trace_canonical import tr_M_word  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = sp.symbols("q", positive=True)
t = sp.symbols("t", positive=True)

Z_D = q ** 3 / (q ** 2 + 1)          # convention D
H_Q = q - 1 / q
TWO_Q = q + 1 / q
S_SQ = (q - 1) ** 2 / q              # the beta-decay coupling
W = q ** 2 * (q ** 12 + q ** 8 - 1) / (q ** 2 + 1) ** 2

# T(p, r) is the closure of (s_1 ... s_{p-1})^r in B_p: n = p, e = r*(p-1).
TORUS = [(2, 3), (2, 5), (2, 7), (3, 4), (3, 5), (3, 7), (4, 3), (5, 3)]


def jones_torus(p: int, r: int):
    """V_{T(p,r)}(t), positive-crossing convention."""
    return sp.cancel(t ** sp.Rational((p - 1) * (r - 1), 2)
                     * (1 - t ** (p + 1) - t ** (r + 1) + t ** (p + r))
                     / (1 - t ** 2))


def h_diff(k):
    """The q-difference h_k = q^k - q^-k (k may be rational)."""
    return q ** sp.Rational(k) - q ** (-sp.Rational(k))


def geom_sum(n: int):
    """G_n(q) = 1 + q + ... + q^(n-1); the cyclotomic cofactor of q^n - 1."""
    return sum(q ** i for i in range(n))


def leading(expr, order):
    """Coefficient of (q-1)^order in the expansion about q = 1."""
    return sp.nsimplify(sp.limit(sp.simplify(expr / (q - 1) ** order), q, 1))


def main() -> int:
    mp.mp.dps = 60
    q0 = Q_MP
    f = lambda e: sp.lambdify(q, e, "mpmath")(q0)      # noqa: E731
    n = lambda x, d=50: mp.nstr(x, d, strip_zeros=False)  # noqa: E731

    # --- 1. the normalisation rule, against the canonical engine ------------
    rule_rows = []
    for p, r in TORUS:
        nb, e = p, r * (p - 1)
        word = tuple(list(range(1, p)) * r)
        tr = sp.cancel(sp.simplify(tr_M_word(word, nb, Z_D, H_Q)))
        V = jones_torus(p, r)
        pred = sp.cancel(q ** (2 * e) * V.subs(t, q ** -2) / TWO_Q ** (nb - 1))
        rule_rows.append({
            "knot": f"T({p},{r})", "braid_index": nb, "exponent_sum": e,
            "word": "(" + "".join(f"s{i}" for i in range(1, p)) + f")^{r}",
            "jones": str(sp.expand(V)),
            "jones_at_one": str(sp.nsimplify(V.subs(t, 1))),
            "jones_prime_at_one": str(sp.nsimplify(sp.diff(V, t).subs(t, 1))),
            "trace": str(sp.factor(tr)),
            "matches_q2e_V_over_two_q_pow": sp.simplify(tr - pred) == 0,
        })

    # --- 2. the T(3,5) instance and the factorisation ----------------------
    J = jones_torus(3, 5).subs(t, q ** -2)
    J_minus_one = sp.cancel(J - 1)
    factored = -h_diff(4) * h_diff(6) / q ** 10
    S_AS_HALF = h_diff(sp.Rational(1, 2)) ** 2

    ratio = sp.cancel(sp.simplify(J_minus_one / S_SQ))
    ratio_pts = {str(pt): n(f(ratio.subs(q, sp.Rational(pt))), 20)
                 for pt in ("11/10", "3/2", "2")}

    lead_J = leading(J_minus_one, 2)
    lead_s = leading(S_SQ, 2)

    assertions = [
        {"name": "normalisation_rule_holds_on_eight_torus_knots",
         "passed": all(r_["matches_q2e_V_over_two_q_pow"] for r_ in rule_rows),
         "note": "tr_M(closure) = q^(2e)*V(q^-2)/[2]_q^(n-1) verified against "
                 "markov_trace_canonical for n = 2,3,4,5 incl. mirror pairs"},
        {"name": "every_jones_has_V_one_equals_one_and_V_prime_one_zero",
         "passed": all(sp.nsimplify(jones_torus(p, r).subs(t, 1)) == 1
                       and sp.nsimplify(sp.diff(jones_torus(p, r), t).subs(t, 1)) == 0
                       for p, r in TORUS),
         "note": "the offset and the vanishing order of J - 1 are topological, "
                 "not chosen — this is what fixes the normalisation"},
        {"name": "weak_vertex_trace_is_jones_over_two_q_squared",
         "passed": sp.simplify(W - q ** 20 * J / TWO_Q ** 2) == 0,
         "note": "W = q^20 * V_{T(3,5)}(q^-2) / [2]_q^2 with e = 10, n = 3"},
        {"name": "numerator_is_q20_times_jones",
         "passed": sp.simplify(sp.expand(W * TWO_Q ** 2) - (q ** 12 + q ** 8 - 1)) == 0
                   and sp.simplify(q ** 20 * J - (q ** 12 + q ** 8 - 1)) == 0,
         "note": "W*[2]_q^2 = q^12 + q^8 - 1 = q^20 * J"},
        {"name": "jones_deviation_is_product_of_two_q_differences",
         "passed": sp.simplify(J_minus_one - factored) == 0,
         "note": "J - 1 = -h_4*h_6/q^10 exactly; exponents 4 and 6 are the "
                 "Jones exponents of T(3,5), q^-10 is the framing"},
        {"name": "q_difference_derivative_at_one_is_two_k",
         "passed": all(sp.nsimplify(sp.diff(h_diff(k), q).subs(q, 1)) == 2 * sp.Rational(k)
                       for k in (4, 6, sp.Rational(1, 2))),
         "note": "h_k'(1) = 2k, so a product of two of them vanishes to second "
                 "order with leading coefficient (2k1)(2k2)"},
        {"name": "jones_deviation_leading_coefficient_is_minus_ninety_six",
         "passed": lead_J == -96 and sp.nsimplify(sp.diff(J, q, 2).subs(q, 1)) == -192,
         "note": "-(2*4)(2*6) = -96, J''(1) = -192 — derived from the exponents"},
        {"name": "jones_deviation_is_polynomial_after_framing",
         "passed": sp.simplify(q ** 20 * J_minus_one + (q ** 8 - 1) * (q ** 12 - 1)) == 0,
         "note": "q^20*(J-1) = -(q^8-1)(q^12-1): the same fact with no negative "
                 "powers, and the form the (q-1)^2 factor is read off"},
        {"name": "ratio_has_exact_cyclotomic_closed_form",
         "passed": sp.simplify(q ** 19 * J_minus_one + S_SQ * geom_sum(8) * geom_sum(12)) == 0,
         "note": "q^19*(J-1) = -s^2*G_8*G_12, so (J-1)/s^2 = -G_8*G_12/q^19 "
                 "EXACTLY — the ratio and its running, with no limit taken"},
        {"name": "cyclotomic_cofactors_at_one_are_the_jones_exponents",
         "passed": sp.nsimplify(geom_sum(8).subs(q, 1)) == 8
                   and sp.nsimplify(geom_sum(12).subs(q, 1)) == 12
                   and sp.nsimplify(sp.cancel(-geom_sum(8) * geom_sum(12) / q ** 19).subs(q, 1)) == -96,
         "note": "G_8(1) = 8, G_12(1) = 12, so the ratio at q = 1 is -8*12 = -96 "
                 "— the Jones exponents themselves, doubled by h_k'(1) = 2k"},
        {"name": "decay_coupling_is_half_scale_q_difference_squared",
         "passed": sp.simplify(S_SQ - S_AS_HALF) == 0 and lead_s == 1,
         "note": "s^2 = h_(1/2)^2 exactly; leading coefficient (2*(1/2))^2 = 1"},
        {"name": "leading_ratio_is_minus_ninety_six_but_ratio_runs",
         "passed": sp.nsimplify(sp.limit(ratio, q, 1)) == -96
                   and sp.simplify(sp.diff(ratio, q)) != 0,
         "note": "(J-1)/s^2 -> -96 at q=1 and -37.09 at q0: the framing q^-10 "
                 "suppresses it, so no CONSTANT relates the two couplings "
                 "(consistent with the qou-pfh7 exclusion, and explains it)"},
        {"name": "order_claim_retracted_substitution_factor_diverges",
         "passed": sp.limit(sp.cancel(W ** 2 / S_SQ), q, 1) == sp.oo
                   and sp.nsimplify(W.subs(q, 1)) == sp.Rational(1, 4),
         "note": "RETRACTED (bean qou-xql6): this producer claimed the ORDER of the "
                 "substitution factor was derived, 96^2 = 9216 against |W|^2/s^4 = "
                 "11875. |W|^2/s^k DIVERGES as q->1 for k >= 1 because W(1) = 1/4 "
                 "!= 0, so it has no leading constant; -96 is the leading value of "
                 "(J-1)/s^2, whose numerator vanishes since V_K(1) = 1 for every "
                 "knot. Two different ratios. Also the power was s^2, not s^4, so "
                 "the factor is 129.405107404"},
    ]

    witness = {
        "computation": "weak-vertex-jones-markov-normalisation",
        "description": (
            "The weak-vertex trace's normalisation is the Jones-Markov relation: "
            "tr_M(closure of beta) = q^(2e)*V(q^-2)/[2]_q^(n-1), verified against "
            "the canonical engine on eight torus knots at n = 2,3,4,5. For "
            "T(3,5) this gives W = q^20*V(q^-2)/[2]_q^2, so the canonically-"
            "normalised coupling is J - 1 with J = V(q^-2) — no free constant, "
            "because V(1) = 1 and V'(1) = 0 for every knot. It factors as "
            "J - 1 = -h_4*h_6/q^10, a product of two q-differences at the two "
            "Jones exponents, which is why it vanishes to second order with "
            "leading coefficient -(2*4)(2*6) = -96. The beta-decay coupling is "
            "the same shape at half scale, s^2 = h_(1/2)^2, leading coefficient "
            "1. So the leading ratio is exactly -96, which derives the ORDER of "
            "the 1.19e4 substitution factor of qou-ix74 (96^2 = 9216) while "
            "confirming no constant relates them: the ratio runs to -37.09 at q0."
        ),
        "convention": {"markov_z": "q**3/(q**2+1) (D)", "hecke_h": "q - 1/q",
                       "jones_variable": "t = q**-2",
                       "anchor": "proton pin (Q_50_DIGIT_STR); identities exact in q"},
        "q0": Q_50_DIGIT_STR,
        "normalisation_rule": "tr_M(closure of beta) = q**(2*e) * V(q**-2) / [2]_q**(n-1)",
        "normalisation_rule_checks": rule_rows,
        "weak_vertex": {
            "knot": "T(3,5)", "braid_word": "(s1 s2)^5",
            "braid_index": 3, "exponent_sum": 10,
            "jones": "t**4 + t**6 - t**10",
            "J_at_q": str(sp.expand(J)),
            "trace_closed_form": str(sp.factor(W)),
            "numerator": "q**12 + q**8 - 1",
            "W_at_q0": n(f(W)), "W_at_one": "1/4",
        },
        "coupling_factorisation": {
            "identity": "J - 1 == -h_4*h_6/q**10   with h_k := q**k - q**-k",
            "jones_exponents": [4, 6],
            "framing": "q**-10",
            "h_k_prime_at_one": "2*k",
            "leading_coefficient": str(lead_J),
            "J_second_derivative_at_one": str(sp.nsimplify(sp.diff(J, q, 2).subs(q, 1))),
            "J_minus_one_at_q0": n(f(J_minus_one)),
        },
        "decay_coupling": {
            "identity": "s**2 == (q**(1/2) - q**(-1/2))**2 == h_(1/2)**2",
            "exponents": ["1/2", "1/2"],
            "leading_coefficient": str(lead_s),
            "s_sq_at_q0": n(f(S_SQ)),
            "honest_limit": ("a Jones exponent is an integer, so s^2 is a FORMAL "
                             "half-scale analogue and not itself any knot's V - 1"),
        },
        "ratio": {
            "closed_form": str(sp.factor(ratio)),
            "cyclotomic_form": "-G_8(q)*G_12(q)/q**19   with G_n(q) = 1+q+...+q**(n-1)",
            "cyclotomic_identity": "q**19*(J-1) == -s**2*G_8(q)*G_12(q)",
            "G_8_at_one": "8", "G_12_at_one": "12",
            "limit_at_one": "-96 = -(2*4)*(2*6)",
            "at_q0": n(f(ratio), 20),
            "at_rational_points": ratio_pts,
            "runs": True,
        },
        "order_of_substitution_factor": {
            "status": "RETRACTED 2026-09-05 (bean qou-xql6)",
            "withdrawn_claim": ("the ORDER of the substitution factor is derived: "
                                "96**2 = 9216 against |W|**2/s**4 = 11875.44"),
            "why_it_fails": ("|W|**2/s**k diverges as q->1 for every k >= 1 "
                             "(W(1) = 1/4 != 0, s**2(1) = 0), so there is no leading "
                             "constant; -96 is the leading value of (J-1)/s**2, a "
                             "DIFFERENT ratio whose numerator vanishes because "
                             "V_K(1) = 1 for every knot"),
            "and_the_power_was_wrong": ("the rate carries s**2 once "
                                        "(prf:trace-ratio-observable), so the factor "
                                        "is 129.405107404, not 11875.4418936763"),
            "what_survives": ("every exact identity in this witness: the Jones-Markov "
                              "relation on eight torus knots, J - 1 = -h_4*h_6/q**10, "
                              "the cyclotomic ratio -G_8*G_12/q**19, and its classical "
                              "value -96"),
        },
        "scope": ("POSITIVE derivation of the normalisation (the framing and rank "
                  "factors are read off the braid word; the offset and vanishing "
                  "order of J - 1 are topological). It does NOT derive the order of "
                  "the decay-rate substitution factor -- that claim is retracted, "
                  "see order_of_substitution_factor. NOT a rescaling constant — the ratio provably "
                  "runs, consistent with the scope-(b) exclusion in qou-pfh7."),
        "lean": ["QOU.Braiding.WeakVertexT35.jonesT35",
                 "QOU.Braiding.WeakVertexT35.weakVertexTrace_eq_jones_markov",
                 "QOU.Braiding.WeakVertexT35.jonesT35_sub_one_eq_qdiff_product",
                 "QOU.Braiding.WeakVertexT35.sSq_eq_qdiff_half_sq",
                 "QOU.Braiding.WeakVertexT35.hasDerivAt_qDiff_one",
                 "QOU.Braiding.WeakVertexT35.jonesT35_sub_one_mul_pow",
                 "QOU.Braiding.WeakVertexT35.jones_dev_eq_sSq_mul_geom",
                 "QOU.Braiding.WeakVertexT35.couplingRatio_one",
                 "QOU.Braiding.WeakVertexT35.couplingRatio_near_q0",
                 "QOU.Braiding.WeakVertexT35.substitutionRateFactor_has_no_classical_leading_value"],
        "reference_blocks": ["prop:hadron-half-life", "prf:hadron-half-life",
                             "rem:hadron-half-life-fermi"],
        "related_beans": ["qou-egvf (closed form)", "qou-4x7c (content)",
                          "qou-ix74 (10^4 negative)", "qou-pfh7 (family exclusion)"],
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="sympy+mpmath")
    witness["scriptFile"] = str(pathlib.Path(__file__).resolve()
                                 .relative_to(REPO / "computations"))
    out = REPO / "computations" / "weak-vertex-jones-markov-normalisation.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")

    for r_ in rule_rows:
        print(f"  {r_['knot']:8} n={r_['braid_index']} e={r_['exponent_sum']:2}  "
              f"rule={'OK' if r_['matches_q2e_V_over_two_q_pow'] else 'FAIL'}  "
              f"V={r_['jones']}")
    print(f"  J - 1 = {sp.factor(J_minus_one)}  ==  -h_4*h_6/q^10")
    print(f"  leading: J-1 -> {lead_J}(q-1)^2   s^2 -> {lead_s}(q-1)^2   "
          f"ratio -> {sp.limit(ratio, q, 1)}")
    print(f"  at q0: s^2={n(f(S_SQ), 12)}  J-1={n(f(J_minus_one), 12)}  "
          f"ratio={n(f(ratio), 12)}")
    print(f"  ratio = -G_8*G_12/q^19  ->  {sp.cancel(-geom_sum(8)*geom_sum(12)/q**19).subs(q,1)} at q=1")
    print(f"  |W|^2/s^4 at q0 = {n(f(W**2/S_SQ**2), 12)}   vs 96^2 = 9216"
          f"   overshoot {n(f(W**2/S_SQ**2)/mp.mpf(96)**2, 12)}")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"  allPassed = {witness['allPassed']} -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
