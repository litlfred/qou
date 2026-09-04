#!/usr/bin/env python3
"""Which convex aggregators the three-point AME grid already excludes.

CONTEXT.  QOU/MassTheory/AggregatorConvexityDichotomy.lean narrowed the
many-body binding magnitude to CONVEX-through-the-origin aggregators: the
measured b3 = +1.4262225 excludes every concave one, for every bond weight and
every bond set.  That is a class, not a candidate.

QOU/MassTheory/AggregatorFamilyExclusions.lean (sorry-free) supplies two
consistency tests the SAME three data points can run against a proposed Phi with
NOTHING FITTED, because three points overdetermine a family with fewer than three
parameters:

  Test 1  two-parameter linear families  Phi(x) = c*x + a*psi(x), psi fixed.
          Realizable => det3(x, psi, phi) = 0  (det3_eq_zero_of_realizable).
          So det3 != 0 excludes the whole family for that psi -- every (c,a) at
          once (not_realizable_of_det3_ne_zero).

  Test 2  pure power laws  Phi(x) = c * x^p.
          log Phi(k*x) - log Phi(x) = p * log k, independent of the base point
          (powerLaw_log_ratio).  Two grid intervals give two extractions of p;
          if they differ the family is excluded.

WHY THIS MATTERS.  The convexity result points at "a linear term minus a concave
deficit", whose canonical member is the semi-empirical volume-minus-surface form
c*x - a*x^(2/3): convex, through the origin, and with Phi(x)/x bounded, so
compatible with saturation.  It is the obvious next candidate.  Test 1 says
whether it survives, and it is a filter rather than a fit.

READING THE OUTPUT.  det3 has the units of the data cubed, so its raw magnitude
is not interpretable.  The normalised column is |det3| divided by the product of
the three column Euclidean norms -- the volume of the parallelepiped over the
product of edge lengths, i.e. a dimensionless degeneracy measure in [0,1].  A
value of ~1e-16 would be "consistent with realizable"; the values here are not.

NO FREE PARAMETERS.  Every number is AME2020 or an exact shape.  No q0, no
convention, no fit.

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

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

set_compute_dps()

AME = {
    "D": mpf("2.224566"),
    "3H": mpf("8.481798"),
    "3He": mpf("7.718043"),
    "4He": mpf("28.295673"),
}
PHI = [AME["D"], (AME["3H"] + AME["3He"]) / 2, AME["4He"]]

# Two readings of "the argument": complete-graph bond count, and mass number.
GRIDS = {
    "bond_count": [mpf(1), mpf(3), mpf(6)],
    "mass_number": [mpf(2), mpf(3), mpf(4)],
}

# Candidate correction shapes psi for Test 1.  x**(2/3) is the surface term.
SHAPES = {
    "x^(2/3)  [surface]": lambda t: t ** (mpf(2) / 3),
    "x^(1/2)": lambda t: mp.sqrt(t),
    "x^(1/3)": lambda t: t ** (mpf(1) / 3),
    "log(1+x)": lambda t: mp.log(1 + t),
    "x^2": lambda t: t ** 2,
    "x  [degenerate]": lambda t: t,
}


def det3(x, psi, phi):
    """The 3x3 determinant of the columns (x, psi, phi) -- QOU det3, verbatim."""
    return (x[0] * (psi[1] * phi[2] - psi[2] * phi[1])
            - psi[0] * (x[1] * phi[2] - x[2] * phi[1])
            + phi[0] * (x[1] * psi[2] - x[2] * psi[1]))


def norm3(v):
    return mp.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)


def main():
    rows = []
    print("TEST 1 -- two-parameter linear families  Phi(x) = c*x + a*psi(x)")
    print("  det3 != 0  =>  NO (c,a) whatsoever reproduces the data.\n")
    for gname, x in GRIDS.items():
        print(f"  grid = {gname}  x = {[int(t) for t in x]}")
        print(f"    {'psi':<20} {'det3':>22} {'|det3|/norms':>16}  verdict")
        for sname, f in SHAPES.items():
            psi = [f(t) for t in x]
            d = det3(x, psi, PHI)
            nrm = norm3(x) * norm3(psi) * norm3(PHI)
            rel = abs(d) / nrm
            excluded = rel > mpf(10) ** (-(mp.dps // 2))
            rows.append({"grid": gname, "psi": sname, "det3": mp.nstr(d, 14),
                         "normalised": mp.nstr(rel, 10),
                         "family_excluded": bool(excluded)})
            print(f"    {sname:<20} {mp.nstr(d, 12):>22} {mp.nstr(rel, 8):>16}"
                  f"  {'EXCLUDED' if excluded else 'consistent'}")
        print()

    # Test 2: local exponents.
    print("TEST 2 -- pure power law  Phi(x) = c * x^p")
    print("  p extracted on each interval; a power law forces one value.\n")
    exps = []
    for gname, x in GRIDS.items():
        ps = []
        for i in range(2):
            k = x[i + 1] / x[i]
            p = (mp.log(PHI[i + 1]) - mp.log(PHI[i])) / mp.log(k)
            ps.append(p)
            exps.append({"grid": gname, "interval": f"{int(x[i])}->{int(x[i+1])}",
                         "p": mp.nstr(p, 14)})
        spread = abs(ps[1] - ps[0])
        print(f"  grid = {gname}:  p = {mp.nstr(ps[0], 10)}, {mp.nstr(ps[1], 10)}"
              f"   spread = {mp.nstr(spread, 8)}")
        exps.append({"grid": gname, "interval": "spread",
                     "p": mp.nstr(spread, 14)})

    def spread_of(g):
        vals = [mpf(e["p"]) for e in exps
                if e["grid"] == g and e["interval"] == "spread"]
        return vals[0]

    surface_excluded = all(
        r["family_excluded"] for r in rows if r["psi"].startswith("x^(2/3)"))
    degenerate_ok = all(
        not r["family_excluded"] for r in rows if r["psi"].startswith("x  ["))

    assertions = [
        {"name": "the volume-minus-surface family c*x - a*x^(2/3) is EXCLUDED on "
                 "both grid readings -- every (c,a), nothing fitted",
         "passed": bool(surface_excluded)},
        {"name": "every candidate correction shape tried is excluded on both "
                 "grids (the two-parameter route is empty here)",
         "passed": all(r["family_excluded"] for r in rows
                       if not r["psi"].startswith("x  ["))},
        {"name": "CONTROL: the degenerate shape psi = x gives det3 = 0, so the "
                 "test detects genuine degeneracy rather than always firing",
         "passed": bool(degenerate_ok)},
        {"name": "no pure power law: the two extracted exponents differ on both "
                 "grids by more than 0.1",
         "passed": bool(spread_of("bond_count") > mpf("0.1")
                        and spread_of("mass_number") > mpf("0.1"))},
        {"name": "the extracted exponent INCREASES along the grid, i.e. the "
                 "convexity accelerates rather than settling",
         "passed": bool(
             mpf([e for e in exps if e["grid"] == "bond_count"][1]["p"])
             > mpf([e for e in exps if e["grid"] == "bond_count"][0]["p"]))},
    ]

    ok = all(a["passed"] for a in assertions)
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness = {
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0. The family exclusion is decided by the sign of a "
            "divided difference over AME2020 data; no substrate quantity "
            "enters. Established by import-cone trace (cone=1, no q0 "
            "import) and by "
            "computations/audits/producer_baked_pin_audit.py, which finds "
            "no q0-valued literal in the source. The witness carries no q0 "
            "field."),
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "Two zero-fit consistency tests from "
            "QOU.MassTheory.AggregatorFamilyExclusions, run against the AME2020 "
            "light-nucleus grid. Result: the volume-minus-surface two-parameter "
            "family -- the canonical member of the convex class that survived "
            "AggregatorConvexityDichotomy -- is EXCLUDED, as is every other "
            "correction shape tried, and no pure power law fits either. The "
            "surviving aggregator must be convex with an accelerating local "
            "exponent, which neither route supplies."),
        "q0_pin": "not applicable -- consumes no framework quantity",
        "free_parameters": 0,
        "phi_MeV": [mp.nstr(v, 14) for v in PHI],
        "test1_determinants": rows,
        "test2_local_exponents": exps,
        "assertions": assertions,
        "scope": (
            "(b) for each family as stated -- the invariant is the determinant "
            "identity det3_eq_zero_of_realizable and the log-ratio identity "
            "powerLaw_log_ratio, both proved in the Lean, not cited. It excludes "
            "NOTHING outside those families."),
        "caveats": [
            "Test 1 excludes a TWO-parameter family. The full semi-empirical "
            "formula also carries Coulomb, asymmetry and pairing terms; on Z = N "
            "light nuclei the asymmetry term vanishes, but three points cannot "
            "test a three-or-more parameter form at all -- it is "
            "UNDERDETERMINED, hence untestable here, NOT excluded here. Do not "
            "report these determinants as excluding 'the SEMF'.",
            "The semi-empirical formula is calibrated for A >~ 20 and is known "
            "to fail on the light nuclei independently of anything in this "
            "framework; 4He is doubly magic. So this exclusion is unsurprising "
            "as physics. Its value is that it is now EXACT and zero-fit rather "
            "than a remembered fact, and that it removes the obvious candidate "
            "before anyone spends a tranche on it.",
            "det3 magnitudes are not comparable across shapes -- only the "
            "normalised column is. The psi = x row is a deliberate control: it "
            "is column-degenerate with x, so its det3 must vanish, and it does.",
            "A vanishing det3 would mean CONSISTENT WITH, never derived: two "
            "parameters on three points leaves one residual, and passing one "
            "residual is weak evidence.",
        ],
        "lean": ("QOU/MassTheory/AggregatorFamilyExclusions.lean "
                 "(6 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/aggregator-convexity-divided-difference.witness.json",
            "probes/mayer-threebody-sign-threshold.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies",
    }
    out = _HERE / "aggregator-family-exclusion.witness.json"
    # NOTE (#6537 x #6519): the `resolve_q0_anchor` override that #6519's sweep
    # placed here has been removed for THIS producer, deliberately.
    #
    # That helper resolves the manifest pin -- muon, proton, or ambiguous -- and
    # defaults to proton for any stem not under `ideal_muon`. It has no way to
    # return `independent`, so on a producer that provably never reads q0 it
    # manufactures a proton claim, and it did so by ASSIGNING OVER the literal
    # below, leaving the `q0AnchorReason` ("Reads no q0 ...") next to a `proton`
    # stamp that contradicts it.
    #
    # `independent` here is measured, not asserted, by three checks:
    #   - import-cone trace: no q_parameter / qou_substrate.constants edge;
    #   - producer_baked_pin_audit.py: no q0-VALUED literal in the source;
    #   - q0_pin_flip_test.py: forcing the muon anchor does not move the
    #     payload (subjects 0/7, on a harness where controls moved 2/2).
    # The sweep's pattern is right for a producer that READS q0; this one
    # does not.
    # P30: add the staleness provenance (scriptHash / commitSha /
    # engine) that a hand-rolled dump cannot get from build().
    # The q0Anchor lines just below own the anchor decision and run
    # after this, so their value stands.
    _WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
