#!/usr/bin/env python3
"""
beta_rate_skein_power_audit.py — the beta-decay rate carries ONE s^2, not s^4;
the substitution factor is 129.4 and not 1.19e4; and the live rate formula
double-counts the weak vertex.

WHAT THIS CORRECTS (bean qou-xql6, 2026-09-05).  Three defects, two of them mine
from earlier today, one in the corpus's own rate formula.  All three are read off
the source blocks, not inferred.

WHAT THE SOURCE SAYS.  prf:trace-ratio-observable states the matrix element in
words and in symbols:

    |M_q|^2 = |skein_amp|^2 * |tr(par)/tr(dau)|^2,    skein_amp = q^(1/2) - q^(-1/2)

  -- "The transition matrix element is the Skein amplitude at the beta-decay
  vertex, which is proportional to the trace ratio."

So the single-crossing Skein amplitude enters the RATE squared exactly ONCE, as
s^2, inside |M_q|^2.  Nothing else in the rate carries an s: [2]_q = q + q^-1 is
a full-scale q-integer, the pair Skein mass carries q^(1/2) + q^(-1/2) (a SUM at
half scale, not s), and f(Q) ~ Q^5 with Q ~ (q - q^-1) = h_1, the full-scale
q-difference.  The rate is

    Gamma_beta = |W(q)|^2 * mu_0/(2 pi^3) * [2]_q * |M_q|^2 * f(Q)

DEFECT 1 -- MINE, MECHANICAL, AND IT MOVES A HEADLINE NUMBER BY 92x.
`WeakVertexSubstitutionScale.lean` (merged, PR #6715, bean qou-ix74) defines

    substitutionRateFactor q := (weakVertexTrace q)^2 / (sSq q)^2

and `sSq q := (q-1)^2/q` IS ALREADY s^2 -- verified below, sSq q == (sqrt q -
1/sqrt q)^2 identically.  So squaring it gives s^4, and the definition computes
|W|^2/s^4.  The rate carries s^2.  Measured at the proton pin:

    |W|^2 / s^4  = 11875.4418937      <- the merged figure, WRONG
    |W|^2 / s^2  =   129.405107404    <- the substitution factor
    error factor = 1/s^2 = 91.7694991484

This is a name-vs-content confusion: `sSq` reads as "s, squared" and was used as
though it were "s".  Every "1.19e4" / "10^4" / "four orders of magnitude" figure
in the qou-ix74 / qou-pfh7 / qou-q2l7 arc inherits it.

  THE VERDICT OF qou-ix74 SURVIVES; ITS MAGNITUDE DOES NOT.  A factor of 129 is
  still absurd against the measured 10-17 % heavy-nucleus overshoot the
  substitution was meant to explain, so substituting |W|^2 for s^2 remains a
  scope-(a) negative.  What is withdrawn is "10^4" and "four orders of
  magnitude"; the correct statement is "two orders of magnitude, ~129x".

DEFECT 2 -- MINE, AND IT IS A RETRACTION RATHER THAN A RE-SCOPING.
qou-q2l7 (merged PR #6765, ~20 minutes before this was found) claimed the ORDER
of the substitution factor is DERIVED, on the strength of (J-1)/s^2 -> -96 and
96^2 = 9216 against |W|^2/s^4 = 11875.  That comparison is a category error:

    lim_{q->1} (J - 1)/s^2  = -96        numerator AND denominator vanish
    lim_{q->1} |W|^2/s^2    = +infinity  W(1) = 1/4 != 0, s^2(1) = 0
    lim_{q->1} |W|^2/s^4    = +infinity

The substitution factor has NO finite classical limit, so there is no leading
constant for -96 to be.  The two ratios differ by the framing q^20/[2]_q^2 and
by the -1 offset: J - 1 vanishes at q = 1 because V_K(1) = 1 for every knot,
while W(1) = 1/4 is the Markov rank factor and does not vanish.  Comparing them
is exactly the shape-conflation AGENTS.md's "grep the claim SHAPE" section
describes.

  WHAT SURVIVES FROM qou-q2l7 IS THE MATHEMATICS, ALL OF IT.  The Jones-Markov
  relation on eight torus knots, J - 1 = -h_4*h_6/q^10, the cyclotomic ratio
  (J-1)/s^2 = -G_8*G_12/q^19, and its classical value -96 = -8*12 are exact
  identities and are untouched.  What is withdrawn is the bridge from -96 to the
  substitution factor -- i.e. the claim that the 10^4 (now 10^2) was derived to
  order.  It was not derived at all.

  Note the irony, recorded because it is the lesson: that same PR withdrew a
  "within a factor of two" bracket for being a window chosen against the target,
  while the object inside the bracket was the wrong ratio.  Fixing how a number
  is reported does not check whether it is the right number.

DEFECT 3 -- THE CORPUS'S, STRUCTURAL, AND NOT MINE TO DECIDE.
prf:hadron-half-life item 1 says |W(q)|^2 "replaces the single-crossing
approximation s^2".  Item 3 of the SAME block, six lines later, defines
|M_q|^2 = s^2 * prod |V_i^par/V_i^dau|^2 -- retaining it.  Both factors are
multiplied into the same rate, so as written the formula carries the full
10-crossing vertex trace AND its own single-crossing approximation:

    Gamma_beta ~ |W|^2 * s^2 * ...

Exactly one of three things is true, and they are different defects:
  (A) item 3's s^2 is the vertex coupling  => the rate DOUBLE-COUNTS the vertex,
      and is too small by s^2 ~ 0.0109 (half-life too long by ~92x);
  (B) item 1's "replaces" is wrong         => nothing was replaced, a factor was
      ADDED, and item 3 must say what its s^2 is if not the vertex;
  (C) item 3 is stale pre-W text           => the tables (which use s^2 alone,
      per the 2026-09-04 author note on ex:hadron-half-life-verification) match
      neither the pre- nor post-W formula.
prf:trace-ratio-observable's own words -- "the Skein amplitude at the beta-decay
vertex" -- point at (A), but the block asserting the replacement is the one that
would have to be corrected, so this is put to the author rather than picked here.
No number in this producer depends on which is chosen.

Precision: sympy-exact throughout; numerics mpmath at 60 dps evaluated from the
exact expressions; serialised at 50 digits.  No float is formed.

Output: computations/beta-rate-skein-power-audit.witness.json
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
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = sp.symbols("q", positive=True)

W = q ** 2 * (q ** 12 + q ** 8 - 1) / (q ** 2 + 1) ** 2   # weakVertexTrace
S_SQ = (q - 1) ** 2 / q                                    # sSq q, i.e. s^2
S_AMP = sp.sqrt(q) - 1 / sp.sqrt(q)                        # skein_amp = s
TWO_Q = q + 1 / q
H_1 = q - 1 / q
PAIR_DEN = sp.sqrt(q) + 1 / sp.sqrt(q)                     # pair Skein denominator
J = (q ** -2) ** 4 + (q ** -2) ** 6 - (q ** -2) ** 10      # V_{T(3,5)}(q^-2)


def main() -> int:
    mp.mp.dps = 60
    q0 = Q_MP
    f = lambda e: sp.lambdify(q, e, "mpmath")(q0)         # noqa: E731
    n = lambda x, d=50: mp.nstr(x, d, strip_zeros=False)  # noqa: E731

    w2, s2 = f(W ** 2), f(S_SQ)
    merged = w2 / s2 ** 2       # |W|^2 / s^4  -- the merged substitutionRateFactor
    correct = w2 / s2           # |W|^2 / s^2  -- the rate's actual power
    err = 1 / s2

    assertions = [
        {"name": "sSq_is_already_s_squared",
         "passed": sp.simplify(S_SQ - S_AMP ** 2) == 0,
         "note": "sSq q = (q-1)^2/q IS (q^(1/2) - q^(-1/2))^2 identically, so "
                 "squaring it gives s^4 -- the name reads as 's, squared' and was "
                 "consumed as though it were 's'"},
        {"name": "nothing_else_in_the_rate_carries_an_s",
         "passed": (sp.simplify(TWO_Q - (q + 1 / q)) == 0
                    and sp.simplify(PAIR_DEN - (sp.sqrt(q) + 1 / sp.sqrt(q))) == 0
                    and sp.simplify(PAIR_DEN - S_AMP) != 0
                    and sp.simplify(H_1 - S_AMP) != 0),
         "note": "[2]_q is full-scale; the pair Skein denominator is the half-scale "
                 "SUM q^(1/2)+q^(-1/2), not s; Q ~ h_1 = q - q^-1 is full-scale. "
                 "So s enters the rate once, squared, via |M_q|^2"},
        {"name": "merged_substitution_factor_uses_s_to_the_fourth",
         "passed": mp.mpf("11875.44") < merged < mp.mpf("11875.45"),
         "note": "(weakVertexTrace q)^2/(sSq q)^2 = |W|^2/s^4 = 11875.4418937 "
                 "-- the figure merged in PR #6715 and repeated in #6735, #6765"},
        {"name": "corrected_substitution_factor_is_one_hundred_twenty_nine",
         "passed": mp.mpf("129.405") < correct < mp.mpf("129.406"),
         "note": "|W|^2/s^2 = 129.405107404 is the factor the rate actually gets"},
        {"name": "error_factor_is_one_over_s_squared",
         "passed": mp.mpf("91.769") < err < mp.mpf("91.770")
                   and abs(merged / correct - err) < mp.mpf("1e-40"),
         "note": "the two differ by exactly 1/s^2 = 91.7694991484, so every "
                 "'10^4' figure in the arc is high by ~92x"},
        {"name": "substitution_factor_has_no_finite_classical_limit",
         "passed": sp.limit(sp.cancel(W ** 2 / S_SQ), q, 1) == sp.oo
                   and sp.limit(sp.cancel(W ** 2 / S_SQ ** 2), q, 1) == sp.oo,
         "note": "W(1) = 1/4 != 0 while s^2(1) = 0, so |W|^2/s^k diverges for "
                 "k >= 1: there is NO leading constant, at either power"},
        {"name": "the_minus_ninety_six_belongs_to_a_different_ratio",
         "passed": sp.nsimplify(sp.limit(sp.cancel((J - 1) / S_SQ), q, 1)) == -96
                   and sp.nsimplify(J.subs(q, 1)) == 1
                   and sp.nsimplify(W.subs(q, 1)) == sp.Rational(1, 4),
         "note": "(J-1)/s^2 -> -96 because J(1) = 1 makes the NUMERATOR vanish "
                 "(V_K(1) = 1 for every knot); W(1) = 1/4 does not vanish. So "
                 "-96 cannot be the leading constant of |W|^2/s^k -- qou-q2l7's "
                 "'order derived' bridge is RETRACTED, not re-scoped"},
        {"name": "qou_q2l7_identities_are_untouched",
         "passed": sp.simplify(W * TWO_Q ** 2 - q ** 20 * J) == 0
                   and sp.simplify(q ** 20 * (J - 1) + (q ** 8 - 1) * (q ** 12 - 1)) == 0
                   and sp.simplify(q ** 19 * (J - 1)
                                   + S_SQ * sum(q ** i for i in range(8))
                                   * sum(q ** i for i in range(12))) == 0,
         "note": "the Jones-Markov relation, J - 1 = -(q^8-1)(q^12-1)/q^20, and "
                 "the cyclotomic ratio all still hold: the mathematics of "
                 "qou-q2l7 survives, only its bridge to the rate does not"},
        {"name": "negative_of_qou_ix74_survives_at_the_corrected_magnitude",
         "passed": correct > 100,
         "note": "129x is still far too large to explain a measured 10-17 % "
                 "overshoot, so substituting |W|^2 for s^2 remains a scope-(a) "
                 "negative -- the verdict stands, the magnitude was wrong by 92x"},
    ]

    witness = {
        "computation": "beta-rate-skein-power-audit",
        "description": (
            "The beta-decay rate carries the single-crossing Skein amplitude "
            "squared exactly ONCE (prf:trace-ratio-observable: |M_q|^2 = "
            "|skein_amp|^2 * |tr(par)/tr(dau)|^2). The merged "
            "substitutionRateFactor squares sSq, which is already s^2, so it "
            "computes |W|^2/s^4 = 11875.44 where the rate gets |W|^2/s^2 = "
            "129.405107404 -- every '10^4' in the qou-ix74/pfh7/q2l7 arc is high "
            "by 1/s^2 = 91.77x. The verdict of qou-ix74 survives (129x still "
            "cannot explain a 10-17 % overshoot); its magnitude does not. "
            "Separately, qou-q2l7's 'order derived' claim is RETRACTED: |W|^2/s^k "
            "diverges as q->1 because W(1) = 1/4 != 0, so the -96 leading value "
            "of (J-1)/s^2 -- a ratio whose numerator DOES vanish -- was never its "
            "leading constant. Every exact identity of qou-q2l7 is untouched. "
            "Third, prf:hadron-half-life multiplies |W|^2 by a |M_q|^2 that still "
            "contains s^2, so the live formula carries the vertex trace AND its "
            "own single-crossing approximation; which of the three readings is "
            "intended is an author decision, recorded and not picked."
        ),
        "convention": {"markov_z": "q**3/(q**2+1) (D)", "hecke_h": "q - 1/q",
                       "anchor": "proton pin (Q_50_DIGIT_STR); identities exact in q"},
        "q0": Q_50_DIGIT_STR,
        "skein_amplitude": {
            "definition": "skein_amp = q**(1/2) - q**(-1/2)   (prf:trace-ratio-observable)",
            "sSq_identity": "sSq q = (q-1)**2/q == skein_amp**2 == s**2",
            "power_in_the_rate": 2,
            "power_in_merged_substitutionRateFactor": 4,
            "s_sq_at_q0": n(f(S_SQ)),
            "s_fourth_at_q0": n(f(S_SQ ** 2)),
        },
        "substitution_factor": {
            "merged_W2_over_s4": n(merged, 20),
            "corrected_W2_over_s2": n(correct, 20),
            "error_factor_one_over_s_sq": n(err, 20),
            "W2_at_q0": n(w2, 20),
            "verdict": ("the qou-ix74 negative SURVIVES -- 129x cannot explain a "
                        "measured 10-17 % overshoot -- but '10^4' and 'four orders "
                        "of magnitude' are withdrawn in favour of '~129x, two "
                        "orders'"),
        },
        "retracted_order_claim": {
            "claim": "qou-q2l7: the ORDER of the substitution factor is derived, "
                     "96^2 = 9216 against 11875",
            "why_it_fails": ("|W|^2/s^k diverges as q->1 for k >= 1 (W(1) = 1/4 != 0, "
                             "s^2(1) = 0), so it has no leading constant; -96 is the "
                             "leading value of (J-1)/s^2, whose numerator vanishes "
                             "because V_K(1) = 1 for every knot"),
            "limit_jones_dev_over_s_sq": "-96",
            "limit_W2_over_s_sq": "+oo",
            "limit_W2_over_s_fourth": "+oo",
            "what_survives": ("every exact identity: W*[2]_q^2 = q^20*V(q^-2); "
                              "J - 1 = -h_4*h_6/q^10; (J-1)/s^2 = -G_8*G_12/q^19; "
                              "couplingRatio(1) = -96"),
        },
        "vertex_double_count": {
            "live_formula": "Gamma_beta = |W(q)|^2 * mu_0/(2 pi^3) * [2]_q * |M_q|^2 * f(Q)",
            "item_1_says": "|W(q)|^2 replaces the single-crossing approximation s^2",
            "item_3_says": "|M_q|^2 = s^2 * prod |V_i^par / V_i^dau|^2",
            "consequence": "the product carries |W|^2 AND s^2",
            "readings": {
                "A_double_count": "item 3's s^2 IS the vertex coupling => rate too "
                                  "small by s^2 ~ 0.0109, half-life too long by ~92x",
                "B_replaces_is_wrong": "nothing was replaced, a factor was added; "
                                       "item 3 must say what its s^2 is",
                "C_item_3_stale": "the tables use s^2 alone and match neither the "
                                  "pre- nor the post-W formula",
            },
            "source_leans_toward": ("A -- prf:trace-ratio-observable calls its "
                                    "skein_amp 'the Skein amplitude at the "
                                    "beta-decay vertex'"),
            "decision": "AUTHOR'S -- not picked here; no number above depends on it",
        },
        "affected_artifacts": [
            "QOU.Braiding.WeakVertexT35.substitutionRateFactor (and its two "
            "ten-thousand envelope theorems) -- merged PR #6715",
            "QOU.Braiding.WeakVertexT35.substitutionRateFactor_overshoot_of_"
            "leading_square -- merged PR #6765",
            "computations/weak-vertex-substitution-scale.witness.json",
            "computations/weak-vertex-jones-markov-normalisation.witness.json",
            "docs/audits/2026-09-05-weak-vertex-coupling-normalisation.md",
            "docs/audits/2026-09-05-weak-vertex-jones-markov-derivation.md",
            "beans qou-ix74, qou-pfh7, qou-q2l7",
        ],
        "reference_blocks": ["prop:hadron-half-life", "prf:hadron-half-life",
                            "prop:trace-ratio-observable",
                            "prf:trace-ratio-observable",
                            "def:beta-decay-skein"],
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="sympy+mpmath")
    witness["scriptFile"] = str(pathlib.Path(__file__).resolve()
                                 .relative_to(REPO / "computations"))
    out = REPO / "computations" / "beta-rate-skein-power-audit.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print(f"  sSq q == s^2 ?                 {sp.simplify(S_SQ - S_AMP**2) == 0}")
    print(f"  |W|^2/s^4 (merged)           = {n(merged, 12)}")
    print(f"  |W|^2/s^2 (rate's power)     = {n(correct, 12)}")
    print(f"  error factor 1/s^2           = {n(err, 12)}")
    print(f"  lim |W|^2/s^2  at q->1       = {sp.limit(sp.cancel(W**2/S_SQ), q, 1)}")
    print(f"  lim (J-1)/s^2  at q->1       = {sp.limit(sp.cancel((J-1)/S_SQ), q, 1)}")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"  allPassed = {witness['allPassed']} -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
