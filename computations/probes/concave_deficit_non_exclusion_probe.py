#!/usr/bin/env python3
"""The linear-minus-concave-deficit class cannot be excluded by three points.

CONTEXT.  `QOU.MassTheory.AggregatorConvexityDichotomy` narrowed the many-body
binding magnitude to CONVEX-through-the-origin aggregators Phi in
B(A) = Phi(m_A * g): the measured b3 = +1.4262225 > 0 excludes every concave one,
for every bond weight and every bond set.

`QOU.MassTheory.AggregatorFamilyExclusions` then excluded, with nothing fitted,
five FIXED correction shapes in the two-parameter family Phi = c*x + a*psi(x) --
among them the semi-empirical volume-minus-surface member c*x - a*x^(2/3).

A follow-up was proposed off the back of that (bean qou-zy94): exclude the whole
LINEAR-MINUS-CONCAVE-DEFICIT class Phi(x) = c*x - a*psi(x), psi concave, by
showing its local exponent must DECREASE while the measured one increases.  The
bean flagged the hypothesis as not obviously true and asserted it nowhere
durable.

WHAT THIS PROBE SHOWS.  The route cannot succeed, for two independent reasons.

  (1) DEFINITIONAL.  Subtracting the data from a line negates every secant slope,
      so the deficit psi := c*x - Phi is concave through the origin IFF Phi is
      convex through the origin -- for every c -- and strictly increasing as soon
      as c clears the largest secant slope.  So membership in the class FOLLOWS
      FROM the convexity that the same three points establish.  Checked here in
      EXACT rational arithmetic, and proved for a general ordered field in
      QOU/MassTheory/ConcaveDeficitNonExclusion.lean (9 declarations, sorry-free).

      The numerical face of this is that det3(x, psi, Phi) -- the very filter
      AggregatorFamilyExclusions uses -- vanishes EXACTLY for the data-derived
      psi, because that column is by construction a combination of the other two.
      The five nonzero determinants in aggregator_family_exclusion_probe.py are
      about PARAMETER COUNTING (three points, two parameters, one residual), not
      about the concave-deficit structure.

  (2) ANALYTIC, and independent of (1).  The stated monotone-exponent hypothesis
      is false as a claim about the class.  An explicit member --
      Phi(x) = c*x - a*(1 - exp(-x/L)) at (c, a, L) = (1.02, 100, 100) -- is
      convex, through the origin, asymptotically linear (so compatible with
      QOU.Mass.CoordinationSaturation), has a concave increasing deficit, and has
      INCREASING secant exponents on the same grid.  The hypothesis is true for
      psi(x) = x^s, where it was read off; it does not survive the class.

WHAT THIS DOES NOT SHOW.  Nothing about which psi is right.  A FIXED shape is
still testable by det3, and all five tried are still excluded.  The class member
in (2) carries three parameters (c, a, L) on three points, so it is
UNDERDETERMINED, hence untestable here -- exhibiting it refutes the monotonicity
hypothesis and is NOT evidence that it fits.  Extending the grid past A = 4 is
what would change any of this.

NO FREE PARAMETERS.  Checks 1-3 are exact rationals over AME2020.  Check 4 uses
one hand-chosen (c, a, L) purely to exhibit a counterexample; no fit is performed
and no framework quantity is consumed, so neither the convention-C/D question nor
the q0 pin can move anything here.

PRECISION.  Exact `fractions.Fraction` where the statement is rational; mpmath at
the repo compute dps for the one exponential member.  No float arithmetic.
"""
import datetime
import json
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

set_compute_dps()

# AME2020 total nuclear binding energies, MeV, as exact rationals.
AME = {"D": F("2.224566"), "3H": F("8.481798"),
       "3He": F("7.718043"), "4He": F("28.295673")}
PHI = [AME["D"], (AME["3H"] + AME["3He"]) / 2, AME["4He"]]
# Complete-graph bond counts on A = 2, 3, 4.  (Used only on A <= 4, where the
# complete graph is 3-regular and so coincides with bounded degree 3, which is
# why QOU.Mass.CoordinationSaturation -- which refutes m = C(A,2) as a LAW --
# does not bite on this grid.)
X = [F(1), F(3), F(6)]


def secants(x, f):
    """(s0, s1, s2): the secant from the origin, then across each interval."""
    return (f[0] / x[0],
            (f[1] - f[0]) / (x[1] - x[0]),
            (f[2] - f[1]) / (x[2] - x[1]))


def det3(x, psi, phi):
    """The 3x3 determinant of the columns (x, psi, phi) -- QOU det3, verbatim."""
    return (x[0] * (psi[1] * phi[2] - psi[2] * phi[1])
            - psi[0] * (x[1] * phi[2] - x[2] * phi[1])
            + phi[0] * (x[1] * psi[2] - x[2] * psi[1]))


def main():
    s = secants(X, PHI)
    print("AME2020 light-nucleus grid, bond-count reading  x = [1, 3, 6]")
    print(f"  Phi (MeV)        {[str(v) for v in PHI]}")
    print(f"  secant slopes    {float(s[0]):.8f}  {float(s[1]):.8f}  "
          f"{float(s[2]):.8f}")
    convex = s[0] <= s[1] <= s[2]
    print(f"  convex through the origin (s0 <= s1 <= s2): {convex}\n")

    # ---- Check 1/2/3: the deficit at a ray of c, exactly. ----------------
    print("The deficit psi := c*x - Phi, over a ray of c above the top secant")
    print(f"  top secant slope s2 = {float(s[2]):.8f};  any c > s2 qualifies\n")
    print(f"    {'c':>10} {'concave':>9} {'increasing':>11} {'det3(x,psi,Phi)':>18}")
    deficit_rows = []
    for c in (F(7), F(8), F(10), F(1000), F("6.7319176")):
        psi = [c * X[i] - PHI[i] for i in range(3)]
        t = secants(X, psi)
        concave = t[1] <= t[0] and t[2] <= t[1]
        increasing = t[0] > 0 and t[1] > 0 and t[2] > 0
        d = det3(X, psi, PHI)
        deficit_rows.append({"c": str(c), "deficit_concave": bool(concave),
                             "deficit_increasing": bool(increasing),
                             "det3": str(d),
                             "deficit_secants": [str(v) for v in t]})
        print(f"    {float(c):>10.6f} {str(concave):>9} {str(increasing):>11}"
              f" {str(d):>18}")
    print()

    # ---- Check 4: the monotone-exponent hypothesis is false on the class. --
    # An explicit member: Phi(x) = c*x - a*(1 - exp(-x/L)).
    C_E, A_E, L_E = mpf("1.02"), mpf(100), mpf(100)

    def phi_exp(t):
        return C_E * t - A_E * (1 - mp.e ** (-t / L_E))

    xe = [mpf(1), mpf(3), mpf(6)]
    fe = [phi_exp(t) for t in xe]
    se = (fe[0] / xe[0], (fe[1] - fe[0]) / (xe[1] - xe[0]),
          (fe[2] - fe[1]) / (xe[2] - xe[1]))
    # psi = 1 - exp(-x/L) is concave increasing through the origin, so the
    # member is genuinely in the class; recorded rather than asserted in prose.
    psie = [(1 - mp.e ** (-t / L_E)) for t in xe]
    tpsi = (psie[0] / xe[0], (psie[1] - psie[0]) / (xe[1] - xe[0]),
            (psie[2] - psie[1]) / (xe[2] - xe[1]))
    p1 = mp.log(fe[1] / fe[0]) / mp.log(xe[1] / xe[0])
    p2 = mp.log(fe[2] / fe[1]) / mp.log(xe[2] / xe[1])
    print("An explicit class member with INCREASING local exponent")
    print(f"  Phi(x) = {mp.nstr(C_E, 4)}*x - {int(A_E)}*(1 - exp(-x/{int(L_E)}))")
    print(f"  Phi          {[mp.nstr(v, 10) for v in fe]}")
    print(f"  psi concave increasing through origin: "
          f"{bool(tpsi[1] <= tpsi[0] and tpsi[2] <= tpsi[1] and tpsi[2] > 0)}")
    print(f"  Phi convex through origin:             "
          f"{bool(se[0] <= se[1] <= se[2])}")
    print(f"  secant exponents  p1 = {mp.nstr(p1, 10)}  p2 = {mp.nstr(p2, 10)}"
          f"   -> {'INCREASING' if p2 > p1 else 'decreasing'}")

    assertions = [
        {"name": "the AME grid is convex through the origin (the antecedent of "
                 "the Lean theorem holds on the corpus's own numbers)",
         "passed": bool(convex)},
        {"name": "for EVERY c above the top secant slope the deficit is concave "
                 "through the origin AND strictly increasing -- an open ray of "
                 "witnesses, not a lucky one",
         "passed": all(r["deficit_concave"] and r["deficit_increasing"]
                       for r in deficit_rows)},
        {"name": "det3(x, psi, Phi) = 0 EXACTLY for every data-derived psi, so "
                 "the AggregatorFamilyExclusions filter returns 'consistent' on "
                 "the class -- its five nonzero determinants are about parameter "
                 "counting, not about the concave-deficit structure",
         "passed": all(F(r["det3"]) == 0 for r in deficit_rows)},
        {"name": "the monotone-exponent hypothesis is FALSE on the class: the "
                 "member c*x - a*(1 - exp(-x/L)) is convex through the origin "
                 "with a concave increasing deficit and INCREASING secant "
                 "exponents",
         "passed": bool(se[0] <= se[1] <= se[2]
                        and tpsi[1] <= tpsi[0] and tpsi[2] <= tpsi[1]
                        and tpsi[2] > 0 and p2 > p1)},
        {"name": "CAVEAT ASSERTED: that member carries THREE parameters "
                 "(c, a, L) on three points, so it is underdetermined and "
                 "untestable here -- it refutes the monotonicity hypothesis and "
                 "is NOT evidence that it fits",
         "passed": True},
    ]
    ok = all(a["passed"] for a in assertions)
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness = {
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0. Checks 1-3 are exact rational identities over AME2020 "
            "binding energies; check 4 evaluates one hand-chosen exponential "
            "member. No substrate quantity enters, so neither the "
            "convention-C/D question nor the q0 pin can move the payload. The "
            "witness carries no q0 field."),
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The linear-minus-concave-deficit class Phi = c*x - a*psi(x), psi "
            "concave -- the class qou-zy94 proposed to exclude -- cannot be "
            "excluded by three points, because membership follows from the "
            "convexity the same points establish. Shown two ways: exactly, via "
            "det3 = 0 for every data-derived psi over an open ray of c; and by "
            "an explicit member with INCREASING local exponent, which refutes "
            "the proposed monotone-exponent route directly."),
        "q0_pin": "not applicable -- consumes no framework quantity",
        "free_parameters": 0,
        "grid_bond_counts": [str(v) for v in X],
        "phi_MeV": [str(v) for v in PHI],
        "phi_secants": [str(v) for v in s],
        "grid_is_convex_through_origin": bool(convex),
        "deficit_rows": deficit_rows,
        "exponential_member": {
            "form": "Phi(x) = c*x - a*(1 - exp(-x/L))",
            "c": mp.nstr(C_E, 12), "a": mp.nstr(A_E, 12), "L": mp.nstr(L_E, 12),
            "phi": [mp.nstr(v, 20) for v in fe],
            "phi_secants": [mp.nstr(v, 20) for v in se],
            "psi_secants": [mp.nstr(v, 20) for v in tpsi],
            "secant_exponents": [mp.nstr(p1, 16), mp.nstr(p2, 16)],
            "exponent_increases": bool(p2 > p1),
        },
        "assertions": assertions,
        "scope": (
            "(b) for the proposed exclusion route -- the invariant is the "
            "slope-negation identity proved in "
            "QOU.MassTheory.ConcaveDeficitNonExclusion, not cited. It excludes "
            "no aggregator; it excludes a METHOD of excluding aggregators."),
        "caveats": [
            "This says nothing about which psi is right. A FIXED shape remains "
            "testable by det3, and all five shapes tried in "
            "aggregator_family_exclusion_probe.py are still excluded. Do not "
            "read this as reopening those.",
            "The exponential member has three parameters on three points and is "
            "therefore UNDERDETERMINED, hence untestable here -- exactly the "
            "regime the SEMF caveat in the sibling probe describes. Exhibiting "
            "it refutes the monotonicity hypothesis; it is NOT a candidate fit.",
            "The monotone-exponent hypothesis IS true for psi(x) = x^s, where it "
            "was read off. What fails is its generalisation to the class.",
            "Three points are three points. This is a statement about what this "
            "grid can decide; extending it past A = 4 with a DERIVED bond set is "
            "what would change it.",
        ],
        "lean": ("QOU/MassTheory/ConcaveDeficitNonExclusion.lean "
                 "(9 declarations, sorry-free, lean-direct exit 0, "
                 "#print axioms = [propext, Classical.choice, Quot.sound])"),
        "related": [
            "probes/aggregator-family-exclusion.witness.json",
            "probes/aggregator-convexity-divided-difference.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies",
    }
    out = _HERE / "concave-deficit-non-exclusion.witness.json"
    # P30: add the staleness provenance (scriptHash / commitSha / engine) that a
    # hand-rolled dump cannot get from build().  `q0Anchor` above is
    # `independent` deliberately and is NOT resolved through the manifest: this
    # producer provably reads no q0 (no q_parameter / qou_substrate.constants
    # edge in its import cone, and no q0-valued literal in its source), so the
    # manifest helper -- which cannot return `independent` -- would manufacture
    # a proton claim contradicting the reason string beside it.  Same decision,
    # and same reasoning, as aggregator_family_exclusion_probe.py.
    _WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
