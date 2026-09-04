#!/usr/bin/env python3
"""AME2020's own binding is a CONVEX function of bond count -- measured.

CONTEXT.  Two assemblies have been machine-checked to miss the measured 3-body
Ursell cumulant, in opposite directions:

  * multiplicative / Mayer  W(K) = 1 - PROD f_ij   ->  b3 < 0
    (QOU.MassTheory.MayerThreeBodySign, QOU.MassTheory.Mu3SlotExclusion)
  * bond-functional additive sum                   ->  b3 = 0 exactly
    (QOU.Mass.PairwiseCumulantVanishing, QOU.MassTheory.BodyOrderCumulant)
  * AME2020                                        ->  b3 = +1.426222 MeV

QOU/MassTheory/AggregatorConvexityDichotomy.lean (sorry-free, verified
lean-direct) proves those are ONE failure: writing B(A) = Phi(m_A * g) for the
total bond weight, b3 = Phi(3g) - 3*Phi(g) is a secant comparison on the ray
through the origin, so Jensen gives

    Phi concave through 0  =>  b3 <= 0        (b3Agg_nonpos_of_concaveOn)
    Phi convex  through 0  =>  b3 >= 0        (b3Agg_nonneg_of_convexOn)

and the measured positive b3 excludes EVERY concave-through-the-origin
aggregator, for every bond weight and every bond set
(not_concaveOn_of_b3Agg_pos).

WHAT THIS PROBE MEASURES.  The Lean says what the sign forbids.  It does not say
whether the AME data is actually consistent with the surviving (convex) branch,
which is a question about numbers.  This probe answers it directly, with no
model and no free parameter: read Phi off AME at the three bond counts the light
nuclei supply, and test convexity by divided differences.

  A=2 (deuteron)  m = C(2,2) = 1 bond   Phi(1g) = B(D)
  A=3 (isospin av) m = C(3,2) = 3 bonds  Phi(3g) = Bbar(3)
  A=4 (helium)    m = C(4,2) = 6 bonds  Phi(6g) = B(4He)

Phi is convex on a grid iff its divided differences are non-decreasing.  The
secant-through-origin ratio Phi(x)/x is the saturation diagnostic: convex
through the origin makes it monotone, and saturation (B/A bounded) requires it
to be bounded, i.e. Phi asymptotically linear.

NO FREE PARAMETERS.  Every number is AME2020 or an exact rational.  No q0, no
convention, no fit -- this probe deliberately consumes no framework quantity, so
its verdict cannot be moved by the convention-C/D question or the q0 pin.

PRECISION.  mpmath end to end at the repo compute dps; no float arithmetic.
"""
import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# AME2020 total nuclear binding, MeV -- the SAME literals as
# probes/he4_body_order_shortfall_location_probe.py and
# probes/mayer_threebody_sign_threshold_probe.py.
AME = {
    "D": mpf("2.224566"),
    "3H": mpf("8.481798"),
    "3He": mpf("7.718043"),
    "4He": mpf("28.295673"),
}

# Complete-graph bond counts C(A,2).  At A = 4 the complete graph is 3-regular,
# so this coincides with bounded-degree-3 there and the coordination-saturation
# exclusion (QOU.Mass.CoordinationSaturation, which refutes m = C(A,2) as a LAW)
# does not bite on this grid.  Beyond A = 4 it would, and this probe stops at 4.
BONDS = {2: 3 - 2, 3: 3, 4: 6}  # 1, 3, 6


def phi_grid():
    """Phi read off AME at bond counts 1, 3, 6 (and Phi(0) = 0 by definition)."""
    bbar3 = (AME["3H"] + AME["3He"]) / 2
    return [(mpf(0), mpf(0)), (mpf(1), AME["D"]), (mpf(3), bbar3),
            (mpf(6), AME["4He"])]


def divided_differences(pts):
    """First divided differences [x_i, x_{i+1}] of the grid."""
    return [(pts[i][0], pts[i + 1][0],
             (pts[i + 1][1] - pts[i][1]) / (pts[i + 1][0] - pts[i][0]))
            for i in range(len(pts) - 1)]


def ursell(B):
    """b2 = B(D); b3 = Bbar(3) - 3 b2; b4 = B(4He) - 6 b2 - 4 b3."""
    b2 = B["D"]
    b3 = (B["3H"] + B["3He"]) / 2 - 3 * b2
    b4 = B["4He"] - 6 * b2 - 4 * b3
    return b2, b3, b4


def mult_b3(f):
    """The multiplicative cumulant at a common bond factor f, both forms."""
    direct = (1 - f ** 3) - 3 * (1 - f)
    factored = -((f - 1) ** 2 * (f + 2))
    return direct, factored


def main():
    pts = phi_grid()
    dd = divided_differences(pts)
    b2, b3, b4 = ursell(AME)

    print("AME2020 binding as a function of bond count (no model, no fit)\n")
    print("   A   bonds        Phi (MeV)      Phi/bonds        B/A")
    for A in (2, 3, 4):
        m = mpf(BONDS[A])
        val = [p[1] for p in pts if p[0] == m][0]
        print(f"  {A:>2}  {int(m):>5}  {mp.nstr(val, 12):>15}"
              f"  {mp.nstr(val / m, 12):>13}  {mp.nstr(val / A, 10):>10}")

    print("\n  first divided differences (convex <=> non-decreasing):")
    for a, b, s in dd:
        print(f"    [{int(a)}, {int(b)}]  ->  {mp.nstr(s, 14)}")

    dd_increasing = all(dd[i][2] < dd[i + 1][2] for i in range(len(dd) - 1))
    ratios = [(p[0], p[1] / p[0]) for p in pts if p[0] != 0]
    ratio_increasing = all(ratios[i][1] < ratios[i + 1][1]
                           for i in range(len(ratios) - 1))

    print(f"\n  divided differences strictly increasing : {dd_increasing}")
    print(f"  Phi(x)/x strictly increasing            : {ratio_increasing}")
    print(f"\n  Ursell:  b2 = {mp.nstr(b2, 12)}   b3 = {mp.nstr(b3, 12)}"
          f"   b4 = {mp.nstr(b4, 12)}")

    # The Lean factorisation, checked numerically at the four measured bond
    # factors of the 2026-08-29 sweep plus two brackets.
    print("\n  multiplicative b3 = -(f-1)^2 (f+2), checked at measured f_pn:")
    fchecks = []
    for label, fval in (("D/probe2", mpf("0.50823")), ("D/chi", mpf("0.61268804")),
                        ("C/probe2", mpf("0.39486")), ("C/chi", mpf("0.49932033")),
                        ("f=1 (decoupled)", mpf(1)), ("f=0.9", mpf("0.9"))):
        d, fac = mult_b3(fval)
        agree = abs(d - fac) < mpf(10) ** (-(mp.dps - 10))
        fchecks.append({"label": label, "f": mp.nstr(fval, 12),
                        "b3_direct": mp.nstr(d, 14),
                        "b3_factored": mp.nstr(fac, 14),
                        "forms_agree": bool(agree), "b3_nonpos": bool(d <= 0)})
        print(f"    {label:>16}  f={mp.nstr(fval, 10):>12}  b3={mp.nstr(d, 12):>15}"
              f"  agree={agree}")

    assertions = [
        {"name": "AME b3 is strictly POSITIVE, so the Lean exclusion applies",
         "passed": bool(b3 > 0)},
        {"name": "AME Phi is CONVEX on the measured bond grid "
                 "(divided differences strictly increasing)",
         "passed": bool(dd_increasing)},
        {"name": "AME Phi is strictly SUPERADDITIVE through the origin "
                 "(Phi(x)/x strictly increasing)",
         "passed": bool(ratio_increasing)},
        {"name": "the multiplicative b3 factorisation -(f-1)^2(f+2) agrees "
                 "with the direct form at every f tested",
         "passed": all(r["forms_agree"] for r in fchecks)},
        {"name": "the multiplicative b3 is non-positive at every f tested, "
                 "including the two convention-C values",
         "passed": all(r["b3_nonpos"] for r in fchecks)},
        {"name": "b4 is POSITIVE too, but its sign does NOT discriminate: "
                 "sqrt is concave and also yields b4 > 0",
         "passed": bool(b4 > 0 and (mp.sqrt(6) - 4 * mp.sqrt(3) + 6) > 0)},
    ]

    ok = all(a["passed"] for a in assertions)
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "AME2020's binding, read as a function of complete-graph bond count "
            "at A = 2, 3, 4, is CONVEX and strictly superadditive through the "
            "origin. With QOU.MassTheory.AggregatorConvexityDichotomy this "
            "converts the two known assembly failures (multiplicative b3 < 0, "
            "additive b3 = 0) into one statement -- both aggregators are "
            "concave-through-the-origin -- and orients the replacement: the "
            "aggregator must be strictly convex at small argument."),
        "q0_pin": "not applicable -- consumes no framework quantity",
        "free_parameters": 0,
        "phi_grid_MeV": [{"bonds": int(x), "phi": mp.nstr(y, 14),
                          "phi_over_bonds": (mp.nstr(y / x, 14) if x != 0 else None)}
                         for x, y in pts],
        "divided_differences": [{"from": int(a), "to": int(b),
                                 "slope": mp.nstr(s, 14)} for a, b, s in dd],
        "ursell_MeV": {"b2": mp.nstr(b2, 14), "b3": mp.nstr(b3, 14),
                       "b4": mp.nstr(b4, 14)},
        "multiplicative_factorisation_checks": fchecks,
        "assertions": assertions,
        "scope": (
            "(b) for the CONCAVE class -- invariant = Jensen, proved in "
            "AggregatorConvexityDichotomy.b3Agg_nonpos_of_concaveOn. The convex "
            "branch is OPEN and reachable (b3Agg_sq_pos). This probe does NOT "
            "close the magnitude and does NOT identify Phi; it measures that the "
            "data lies in the surviving branch and says which property a "
            "candidate aggregator must have."),
        "caveats": [
            "The bond count C(A,2) is used only on A <= 4, where it coincides "
            "with bounded degree 3; QOU.Mass.CoordinationSaturation refutes it "
            "as a law for larger A, so this grid must not be extended naively.",
            "Convexity is measured on THREE interior points. Three points "
            "cannot distinguish convex from convex-then-concave, and saturation "
            "requires the latter eventually -- Phi(x)/x is bounded only if Phi "
            "is asymptotically linear. So 'convex' here is a local statement "
            "about the light nuclei, not an asymptotic claim.",
            "b4 > 0 is NOT evidence for convexity: sqrt is concave and gives "
            "b4 = sqrt(6) - 4 sqrt(3) + 6 > 0. b3 is the discriminator.",
        ],
        "lean": ("QOU/MassTheory/AggregatorConvexityDichotomy.lean "
                 "(8 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/mayer-threebody-sign-threshold.witness.json",
            "probes/he4-body-order-shortfall-location.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies",
    }
    out = _HERE / "aggregator-convexity-divided-difference.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    witness["q0Anchor"] = _q0a
    if _q0v:
        witness["q0Value"] = _q0v
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
