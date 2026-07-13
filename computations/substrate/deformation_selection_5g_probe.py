"""Deformation selection for the deuteron law: 5g vs 1/g (D4 of the
full-derivation program).

D1 left a two-way deformation ambiguity for the classical integer
5 = (1 + [2]^2)|_{v=1}. This probe resolves the AMBIGUITY'S STRUCTURE
exactly and records the structural selection argument.

(1) THE TWO DEFORMATIONS ARE THE TWO CRITICALITY CANDIDATES (exact).
    With g = z/sqrt(1+z^2), z = 1/[2]_v:
        (i)  5 g                      (classical numerator, deformed rate)
        (ii) (1 + [2]_v^2) g  =  1/g  (fully deformed)
    — identity (ii) is the criticality reciprocal g^2 (1+[2]_v^2) = 1, so
    the D1 ambiguity IS the reeb-flow audit's "5g vs 1/g = |mu_q|"
    straddle (SS2e). Verified symbolically (g^2 form, no radicals).

(2) THE GAP IS EXACTLY x/5 (exact). [2]_v^2 = 4 + x with
    x = (v - v^{-1})^2, so
        1 + [2]_v^2 = 5 + x       (exact, no truncation)
        (1/g) / (5g) = 1 + x/5    (exact)
    — the two deformations coincide at v = 1 and split at first order in
    the deformation parameter x.

(3) THE SS2e CORRECTION LADDER IS DEFORMATION (i) (exact series). The
    reeb-flow audit's provable-target ladder
        B = sqrt(5) E_unit (1 - x/10 + 3x^2/200 - ...)
    is term-by-term the Taylor expansion of 5g = 5/sqrt(5 + x) =
    sqrt(5)/sqrt(1 + x/5) (verified to O(x^4)). The "correction ladder" is
    not a family of unknowns — it IS the 5g deformation, exactly.

(4) STRUCTURAL SELECTION (recorded as an argument, (a)-scoped, not a
    proof). D3 established that g is a LINKING RATE and T2b that
    topological winding data is q-RIGID (integer, does not flow with the
    modulus) while metric data deforms. In the law
    B = (channel weight) x (linking rate) x E_unit, the channel weight is
    counting data — linking multiplicities and classical channel
    dimensions are topological integers — hence sits on the RIGID side:
    the classical 5. The only deformed factor is the geometric rate g.
    This selects (i) 5g. Consequence: the dimensionless part of the linear
    law is EXACT as 5g, and the +0.41 % AME residual must be carried
    entirely by E_unit (or by beyond-bond physics) — sharpening
    E_unit = B_AME / 5g = 0.995940 MeV into a genuinely fundamental
    energy target. Honest counterpoint recorded: under (ii) the residual
    is +0.63 %; the selection argument is structural, not numerical, and
    no production tier is changed here.
"""
import json
import os

import sympy as sp

v, x = sp.symbols("v x", positive=True)
two_v = v + 1 / v
z = 1 / two_v
g_sq = z**2 / (1 + z**2)          # g^2, radical-free

# (1) deformation (ii) equals the criticality reciprocal: ((1+[2]^2) g)^2 = 1/g^2
ii_sq = (1 + two_v**2) ** 2 * g_sq
recip_ok = sp.simplify(ii_sq - 1 / g_sq) == 0

# (2) exact gap
xdef = (v - 1 / v) ** 2
five_plus_x_ok = sp.simplify((1 + two_v**2) - (5 + xdef)) == 0
gap_ok = sp.simplify(((1 / g_sq) / (5**2 * g_sq)) - (1 + xdef / 5) ** 2) == 0

# (3) the SS2e ladder is the 5g expansion: 5/sqrt(5+x) = sqrt(5)(1 - x/10 + 3x^2/200 - ...)
series = sp.series(5 / sp.sqrt(5 + x), x, 0, 4).removeO().expand()
c0_ok = sp.simplify(series.coeff(x, 0) - sp.sqrt(5)) == 0
c1_ok = sp.simplify(series.coeff(x, 1) + sp.sqrt(5) / 10) == 0
c2_ok = sp.simplify(series.coeff(x, 2) - 3 * sp.sqrt(5) / 200) == 0
c3_val = sp.nsimplify(series.coeff(x, 3) / sp.sqrt(5))

assertions = {
    "deformation_ii_equals_reciprocal_criticality": bool(recip_ok),
    "one_plus_bracket_sq_eq_5_plus_x": bool(five_plus_x_ok),
    "gap_exactly_1_plus_x_over_5": bool(gap_ok),
    "ladder_c0_sqrt5": bool(c0_ok),
    "ladder_c1_minus_x_over_10": bool(c1_ok),
    "ladder_c2_3x2_over_200": bool(c2_ok),
}

verdict = (
    "DEFORMATION AMBIGUITY STRUCTURALLY RESOLVED IN FAVOUR OF 5g "
    "((a)-scoped argument, exact identities): the two canonical "
    "deformations of the classical 5 are exactly the reeb-flow "
    "criticality pair 5g vs 1/g (fully-deformed = reciprocal, "
    "g^2(1+[2]^2) = 1), split by the exact factor 1 + x/5, and the SS2e "
    "provable-target ladder sqrt(5)(1 - x/10 + 3x^2/200 - ...) is "
    "term-by-term the expansion of 5g = 5/sqrt(5+x) (next term "
    f"{c3_val}*sqrt(5)*x^3). Selection: by D3 g is a linking RATE "
    "(metric, deforms) while channel weights are counting data "
    "(topological, q-rigid per T2b) — the weight stays classical 5, only "
    "the rate deforms. Consequence: the dimensionless law is exact as 5g "
    "and the +0.41% residual belongs entirely to E_unit (= B_AME/5g = "
    "0.995940 MeV, now a sharp fundamental-energy target) or beyond-bond "
    "physics. Counterpoint recorded: (ii) would give +0.63%; selection is "
    "structural, not numerical. No tier changed, nothing wired."
)

witness = {
    "computation": "deformation_selection_5g_probe",
    "description": (
        "D4: the D1 deformation ambiguity is exactly the 5g-vs-1/g "
        "criticality pair, split by 1 + x/5; the SS2e ladder is the exact "
        "5g expansion; rigid-vs-deformed structural argument selects 5g."
    ),
    "discipline": ("sympy exact throughout; selection argument recorded as "
                   "(a)-scoped structural reasoning, not numerics; no scan; "
                   "no tier change; nothing wired."),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "identity_ii": "(1+[2]_v^2) g = 1/g (criticality reciprocal)",
        "exact_split": "1+[2]_v^2 = 5 + x, ratio (1/g)/(5g) = 1 + x/5, x = (v-v^{-1})^2",
        "ladder": "5/sqrt(5+x) = sqrt(5)(1 - x/10 + 3x^2/200 - (x^3 term recorded) ...)",
        "ladder_x3_coeff_over_sqrt5": str(c3_val),
        "selection": "5g (rigid count x deformed rate); E_unit sharpened to B_AME/5g exactly",
        "related": [
            "deuteron-tower-fusion-frame-probe.witness.json (D1)",
            "gauss-linking-channel-slope-probe.witness.json (D3)",
            "docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md SS2e",
        ],
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "deformation-selection-5g-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for kk, val in assertions.items():
    print(f"  {kk}: {'PASS' if val else 'FAIL'}")
print(f"\nx^3 ladder coefficient / sqrt(5): {c3_val}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nwitness -> {out}")
