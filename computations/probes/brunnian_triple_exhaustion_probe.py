"""The A=3 count-channel carrier space is one integer, and it is exhausted.

qou-brng's next step was "search the 20 binding-relevant triples and select on
something that is not the Markov trace."  THERE IS NOTHING TO SEARCH.  The space
collapses once more, to a single integer, and enumerating it is a proof rather
than a scan.

THE COLLAPSE, IN TWO STEPS.

  1. countChannel_depends_only_on_total: the binding sees only n+ + n- per
     nucleon-pair, so all NINE bands joining a pair are equivalent and a
     carrier's binding-relevant content is the triple (m1,m2,m3) -- n+ = n- = m_i
     on each pair, m_i >= 1 because a Brunnian carrier links every pair.  That
     took 382,637,520 band words down to 20 triples at c <= 12.

  2. HERE: with c2 = 2 (the owner-ruled Hopf pair carrier) and c3 = 2(m1+m2+m3),
     bRatio_hopf_pair gives  b3/b2 = c3/2 - 3 = M - 3,  M := m1+m2+m3.
     So b3 cannot see the triple either -- only its sum.  The 20 triples collapse
     to four values of M, and the carrier space b3 can distinguish is the
     integers.

THE EXHAUSTION.  M >= 3, so b3/b2 = M - 3 is a NON-NEGATIVE INTEGER, while the
measured 950815/1483044 ~ 0.6411 lies strictly between 0 and 1.  Nothing hits it,
and every M misses by at least 532229/1483044 ~ 0.35888 -- 55.98% of the measured
value, attained at M = 4.

AND c <= 12 WAS NEVER A RESTRICTION.  b3/b2 = M - 3 INCREASES with M, so nothing
above M = 4 can do better.  The enumeration is complete over EVERY crossing
number.  There is no larger search to run.

NO FREE PARAMETERS.  AME2020 plus integers.  No q0, no convention, no pin.

PRECISION.  Exact Fraction end to end; every serialized number is an exact
rational string.  float() appears only inside f-strings for display.

LEAN.  QOU/Mass/BrunnianTripleExhaustion.lean, 8 declarations, sorry-free,
lean-direct exit 0, standard three axioms.
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
from qou_substrate.witness import WitnessBuilder  # noqa: E402

# AME2020 total nuclear binding, MeV -- same literals as the sibling probes.
AME = {"D": F("2.224566"), "3H": F("8.481798"), "3He": F("7.718043")}


def main():
    ok = True
    assertions = []

    def check(name, cond, detail):
        nonlocal ok
        ok = ok and bool(cond)
        assertions.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}\n         {detail}")

    b2 = AME["D"]
    r = ((AME["3H"] + AME["3He"]) / 2 - 3 * b2) / b2

    print("The A=3 count-channel carrier space, exhausted\n")
    print(f"  measured b3/b2 = {r} = {float(r):.10f}\n")

    check("the measured ratio is the exact rational the Lean carries",
          r == F(950815, 1483044),
          "matches QOU.Mass.CarrierCrossingQuantisation.rMeasured, imported by "
          "the Lean rather than restated")

    # --- collapse: the triple's b3 depends only on its sum -------------------
    triples = [(m1, m2, m3)
               for m1 in range(1, 7) for m2 in range(1, 7) for m3 in range(1, 7)
               if 2 * (m1 + m2 + m3) <= 12]
    by_sum = {}
    for t in triples:
        by_sum.setdefault(sum(t), []).append(t)

    check("b3 sees only the SUM -- the 20 triples collapse to 4 values of M",
          len(triples) == 20 and sorted(by_sum) == [3, 4, 5, 6]
          and all(len({F(sum(t) - 3) for t in ts}) == 1
                  for ts in by_sum.values()),
          f"{len(triples)} triples at c <= 12, {len(by_sum)} distinct M; every "
          "triple with the same sum gives the identical b3/b2 (Lean "
          "bRatio_depends_only_on_sum)")

    print(f"\n    {'M':>2} {'c3':>3} {'b3/b2':>7} {'rel err':>10}  triples")
    rows = []
    for M in sorted(by_sum):
        v = F(M - 3)
        rows.append({"M": M, "c3": 2 * M, "b3_over_b2": str(v),
                     "rel_err_fraction": str((v - r) / r),
                     "n_triples": len(by_sum[M]),
                     "example": list(by_sum[M][0])})
        print(f"    {M:>2} {2 * M:>3} {float(v):>7.2f} "
              f"{float((v - r) / r) * 100:>9.2f}%  {len(by_sum[M]):>4}")

    # --- the exhaustion ------------------------------------------------------
    check("M = 3 is FORCED to be (1,1,1) -- the Borromean -- and gives exactly 0",
          by_sum[3] == [(1, 1, 1)] and F(3 - 3) == 0,
          "one clasp per pair is the only triple summing to 3; it lands exactly "
          "on the degenerate locus, agreeing with "
          "CountChannelCarrierLocus.canonical_carriers_b3_eq_zero -- reached "
          "here by exhaustion rather than by assignment")

    check("no integer M reproduces the measured b3",
          all(F(M - 3) != r for M in range(-50, 200)),
          "b3/b2 = M - 3 is an integer; the measured value lies strictly "
          "between 0 and 1. The Lean proves it for EVERY integer, and does not "
          "even need the Brunnian hypothesis (no_carrier_reproduces_b3)")

    gaps = {M: abs(F(M - 3) - r) for M in range(3, 60)}
    best_M = min(gaps, key=gaps.get)
    check("and every carrier misses by >= 532229/1483044 (55.98%), attained at M=4",
          gaps[best_M] == F(532229, 1483044) and best_M == 4,
          f"min gap {gaps[best_M]} = {float(gaps[best_M]):.6f}, "
          f"{float(gaps[best_M] / r) * 100:.2f}% of measured, at M = {best_M}; "
          "matches the Lean bound carrier_gap_bounded_below")

    check("c <= 12 was NEVER a restriction -- the gap grows monotonically past M=4",
          all(gaps[M] < gaps[M + 1] for M in range(4, 59)),
          "b3/b2 = M - 3 increases with M, so no larger carrier can do better "
          "(Lean gap_increases_beyond_four). The enumeration is complete over "
          "EVERY crossing number, not merely c <= 12 -- there is no larger "
          "search to run")

    witness = {
        "computation": "brunnian-triple-exhaustion",
        "scriptFile": "probes/brunnian_triple_exhaustion_probe.py",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "contentBlock": "qou-brng",
        "description": (
            "The A=3 count-channel carrier space collapses to a single integer "
            "M = m1+m2+m3, and is exhausted: b3/b2 = M - 3 is a non-negative "
            "integer while the measured ratio is 950815/1483044, strictly "
            "between 0 and 1. Every carrier misses by at least 532229/1483044 "
            "(55.98%), attained at M=4, and the gap grows monotonically beyond "
            "-- so the exclusion is complete over every crossing number. This "
            "closes the 'search the 20 triples' step by proving there is "
            "nothing to search."),
        "measured_b3_over_b2": str(r),
        "collapse": {
            "step_1": ("countChannel depends only on n+ + n-, so 382,637,520 "
                       "band words -> 20 triples at c <= 12"),
            "step_2": ("b3/b2 = M - 3 depends only on the SUM, so 20 triples "
                       "-> 4 values of M"),
            "n_triples_c_le_12": len(triples),
            "n_distinct_M": len(by_sum),
        },
        "enumeration": rows,
        "exhaustion": {
            "min_gap": str(gaps[best_M]),
            "min_gap_at_M": best_M,
            "min_gap_relative_fraction": str(gaps[best_M] / r),
            "complete_over_all_c": True,
            "reason": ("b3/b2 = M - 3 increases with M, so nothing above M=4 "
                       "can do better; c <= 12 was never a restriction"),
        },
        "assertions": assertions,
        "allPassed": ok,
        "scope": (
            "(b) on the conjunction {b3 carried by the count channel, mu ∝ c, "
            "Hopf pair carrier c2 = 2, Brunnian A=3 carrier}, invariant named: "
            "M is an integer >= 3, so b3/b2 is a non-negative integer while the "
            "measured ratio is not one. (a) on each ingredient separately -- it "
            "does NOT say the count channel is wrong nor that the carrier is "
            "not Brunnian; brunnian_binding_survives is untouched."),
        "caveats": [
            "The live ingredient is the FIRST one -- that b3 is carried by the "
            "count channel at all. Owner ruling A fixes the pair carrier; "
            "dropping Brunnian-ness hits not_pairLocal_of_noIsolatedPairEnergy "
            "(renamed 2026-09-07 from brunnian_not_pairLocal; a pair-local "
            "carrier forces b3 = 0, refuted by AME); and bRatio_scale_invariant "
            "shows mu ∝ c is not a convention one can relax. So the exclusion "
            "points back to qou-brng's original framing: the extensive term is "
            "somewhere the crossing count does not reach.",
            "This is A=3 only. b4 and the A=4 carrier (6 pairs, not 3) are not "
            "touched, and nothing here follows for them.",
            "b3 uses the isospin-averaged Bbar(3). A carrier assigning DIFFERENT "
            "triples to 3H and 3He would put b3/b2 on the half-integer grid "
            "rather than the integers -- that case is the one already covered by "
            "CarrierCrossingQuantisation.even_lattice_gap (22.01%), not by this "
            "file, and it is still excluded.",
            "The Lean imports rMeasured from CarrierCrossingQuantisation rather "
            "than restating it, so the two cannot drift apart.",
        ],
        "lean": ("QOU/Mass/BrunnianTripleExhaustion.lean "
                 "(8 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/carrier-crossing-quantisation.witness.json",
            "probes/enumerator-selection-criterion-audit.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies; integer crossing counts",
    }
    # P30: stamp WitnessBuilder provenance (scriptHash / commitSha /
    # engine) so the staleness machinery can track this witness. Written
    # with raw json below because the payload carries a flat
    # assertions/allPassed shape, which is what stamp_staleness_metadata
    # is for; wrap_legacy().save() would reshape it.
    # q0_anchor=False: nothing here evaluates at q0 -- the arithmetic is
    # exact rational over AME literals and integers -- so stamping an
    # anchor would assert a dependence this probe does not have.
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python", q0_anchor=False)

    out = _HERE / "brunnian-triple-exhaustion.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
