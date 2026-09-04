#!/usr/bin/env python3
"""Carrier crossing numbers are quantised, and no integer choice reaches b3.

THE QUESTION (qou-brng).  Where does the count channel's multiplicity mu come
from, rather than being fitted?  QOU/Mass/CountChannelCarrierLocus.lean fixes
the shape -- mu = (n+ + n-)/2 = HALF THE CARRIER'S CROSSING COUNT, and the
overall scale cancels, so

    b3/b2 = mu_triple/mu_pair - 3 = c3/c2 - 3.

Both c2 and c3 are crossing counts of braid words, hence NON-NEGATIVE INTEGERS.
That is the whole content of this probe: with c2 pinned, b3/b2 lives on a
lattice, and the measured value falls in a gap.

WHAT CHANGED, AND WHY THE OLD OBSTRUCTION IS NOW LIVE.  CountChannelCarrierLocus
records a quantisation argument as WRONG, because it assumed mu_pair = 1 while
mu_pair was free.  That retraction was correct at the time.  OWNER RULING A of
2026-08-29 supplies the missing assumption: the deuteron carrier is the
canonical braid closure -- the Hopf link, sigma_g^2, c2 = 2.  With c2 pinned the
freedom collapses to a single integer and the obstruction returns, now
CONDITIONAL ON THAT RULING rather than on a guess.

THE FOUR RULES THE CORPUS ACTUALLY DERIVES.  Each is read off an existing
artifact, not invented here:

  min-length enumeration   computations/_deprecated/binding-k-enumerator.witness.json
                           returns bindingKWord = [3,3] = sigma_3^2 for
                           deuterium, tritium AND helium-3 alike.  The labels
                           "6_2"/"8_11"/"L6a4" on the Lean instances are
                           retained CENSUS NAMES, not what was enumerated.
                           NOTE the criterion is NOT minimality: the sort key
                           is (PSD_feasible, markov_residual_to_target, L_K) --
                           Frobenius-residual minimisation, with length only a
                           TIEBREAK.  All three returned the same word because
                           the search was TRUNCATED at L_K_max = 3-4, not
                           because the principle is A-blind.
  chain / coordination     one clasp per interface, z = A-1  (the corpus's
                           coordination carrier, bk-coordination-multiplicity).
  canonical Brunnian       Hopf pair, Borromean L6a4 triple.
  census volume-match      6_2 for 2H; 8_11 / L6a4 for 3H / 3He.  The atlas
                           registry FLAGS THIS TIER AS AME-INVERTED in its own
                           words -- "we picked the knot whose volume is closest
                           to B_AME/rho" -- so it is circular and is recorded
                           only for completeness.

THE STRADDLE TRAP.  Taking c2 = 2 from the owner-ruled Hopf deuteron and c3 = 7
from the census A=3 row gives b3/b2 = +1/2: right sign, 22% low, and MEANINGLESS,
because the two numbers come from different assignments.  Read either assignment
consistently and the answer is 0 or -11/6.  Asserted below so the coincidence is
not rediscovered as a result.

NO FREE PARAMETERS.  AME2020 plus integers.  No q0, no convention, no pin -- so
neither the convention-C/D question nor the proton/muon anchor can move any
number here.

PRECISION.  Exact Fraction end to end, INCLUDING THE WITNESS.  Every quantity is a ratio of integers
(AME literals are exact decimals; crossing counts are integers), so Fraction is
exact where mpmath would only be accurate -- per AGENTS.md, "use mpmath
equivalents, or Fraction when the quantity is exact".  float() appears only inside
f-strings for display; every serialized number is an exact rational string, so
the witness carries no float64 (the raw-float64 ratchet flagged an earlier draft
that serialized two of them, and it was right to).

LEAN.  QOU/Mass/CarrierCrossingQuantisation.lean, 11 declarations, sorry-free,
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

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

# AME2020 total nuclear binding, MeV -- the same literals as
# probes/pair_locality_shortfall_probe.py.
AME = {"D": F("2.224566"), "3H": F("8.481798"),
       "3He": F("7.718043"), "4He": F("28.295673")}

# The four derived rules, as (label, c2, c3, provenance).
RULES = [
    ("min-length enumeration (sigma_g^2 for all three)", 2, 2,
     "computations/_deprecated/binding-k-enumerator.witness.json"),
    ("chain / coordination z = A-1", 2, 4,
     "content/.../mass-theory/bk-coordination-multiplicity.md"),
    ("canonical Brunnian (Hopf, Borromean L6a4)", 2, 6,
     "QOU.Mass.CountChannelCarrierLocus.canonical_carriers_b3_eq_zero"),
    ("census volume-match (6_2 ; avg of 8_11, L6a4)", 6, 7,
     "AME-INVERTED tier -- recursive-atom-knot-atlas-registry.md"),
]


def b_ratio(c2, c3):
    """b3/b2 for a carrier pair with crossing counts c2, c3.  mu = c/2, and the
    factor of 1/2 cancels -- QOU...CarrierCrossingQuantisation.bRatio_of_crossings."""
    return F(c3, 1) / F(c2, 1) - 3


def main():
    ok = True
    assertions = []

    def check(name, cond, detail):
        nonlocal ok
        ok = ok and bool(cond)
        assertions.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}\n         {detail}")

    b2 = AME["D"]
    bbar3 = (AME["3H"] + AME["3He"]) / 2
    b3 = bbar3 - 3 * b2
    r = b3 / b2

    print("Carrier crossing numbers vs the measured three-body cumulant\n")
    print(f"  b2            = {float(b2):.6f} MeV")
    print(f"  b3            = {float(b3):.7f} MeV")
    print(f"  b3/b2         = {r}  = {float(r):.10f}")
    print(f"  required mu_t/mu_p (mu_p = 1, Hopf) = {float(r + 3):.10f}")
    print(f"  required c3   = 2*(r+3) = {float(2 * (r + 3)):.10f}   <- NOT an integer\n")

    check("measured b3/b2 is the exact rational 950815/1483044",
          r == F(950815, 1483044),
          f"r = {r}; matches the Lean constant rMeasured")

    print("\n  The four rules the corpus derives:\n")
    print(f"    {'rule':52} {'c2':>3} {'c3':>3} {'b3/b2':>9}")
    rows = []
    for label, c2, c3, prov in RULES:
        v = b_ratio(c2, c3)
        rows.append({"rule": label, "c2": c2, "c3": c3,
                     "b3_over_b2": str(v), "provenance": prov})
        print(f"    {label:52} {c2:3} {c3:3} {float(v):+9.4f}")

    check("every consistently-read rule gives b3/b2 <= 0",
          all(b_ratio(c2, c3) <= 0 for _, c2, c3, _ in RULES),
          "min-length -2, chain -1, canonical Brunnian 0, census -11/6; "
          f"measured is {float(r):+.4f}")

    check("the canonical Brunnian carriers sit EXACTLY on the degenerate locus",
          b_ratio(2, 6) == 0,
          "c3/c2 = 6/2 = 3 exactly; agrees with "
          "CountChannelCarrierLocus.canonical_carriers_b3_eq_zero")

    straddle = b_ratio(2, 7)
    check("the straddle (Hopf c2=2 with census c3=7) manufactures the sign",
          straddle == F(1, 2) and b_ratio(6, 7) == F(-11, 6),
          f"straddled = {straddle} (+ sign, {float((straddle - r) / r) * 100:.2f}% off) "
          f"but census read CONSISTENTLY = {b_ratio(6, 7)}; the two crossing "
          "numbers come from different carrier assignments")

    # --- the lattice obstruction ---------------------------------------------
    # single A=3 carrier: mu_t = c3/2, half-integer grid.
    # distinct 3H/3He carriers: mu_t = (cH + cHe)/4, quarter-integer grid.
    half = [(n, F(n, 2) - 3) for n in range(2, 13)]
    quarter = [(m, F(m, 4) - 3) for m in range(8, 21)]

    hit = [n for n, v in half if v == r] + [m for m, v in quarter if v == r]
    check("NO integer carrier assignment reproduces the measured b3",
          not hit,
          "scanned the half-integer grid n in [2,12] and the quarter-integer "
          "grid m in [8,20]; the Lean proves it for ALL integers "
          "(no_quarter_lattice_point_is_measured)")

    best_h = min(half, key=lambda t: abs(t[1] - r))
    best_q = min(quarter, key=lambda t: abs(t[1] - r))
    gap_q = abs(best_q[1] - r)

    print(f"\n  nearest half-integer point:    c3 = {best_h[0]}, b3/b2 = {best_h[1]}"
          f"  ({float((best_h[1] - r) / r) * 100:+.2f}%)")
    print(f"  nearest quarter-integer point: c(3H)+c(3He) = {best_q[0]}, "
          f"b3/b2 = {best_q[1]}  ({float((best_q[1] - r) / r) * 100:+.2f}%)")

    check("the finest lattice still misses by 161468/1483044 (16.98%)",
          gap_q == F(161468, 1483044) and best_q[0] == 15,
          f"gap = {gap_q} = {float(gap_q):.6f} in b3/b2 units, "
          f"{float(gap_q / r) * 100:.2f}% of the measured value; matches the "
          "Lean bound in quarter_lattice_gap")

    check("the single-carrier grid misses by more (22.01%), as a sublattice must",
          abs(best_h[1] - r) >= gap_q and best_h[0] == 7,
          f"c3 = 7 gives {best_h[1]}, {float((best_h[1] - r) / r) * 100:.2f}%; "
          f"c3 = 8 gives {F(8, 2) - 3}, "
          f"{float((F(8, 2) - 3 - r) / r) * 100:+.2f}%")

    check("escaping the gap needs c3 > 6, ABOVE the minimal Brunnian 3-braid",
          all(b_ratio(2, c) <= 0 for c in range(0, 7)) and b_ratio(2, 7) > 0,
          "QOU.Knots.KauffmanTL3 machine-checks that no braid word of length "
          "< 6 is both Brunnian and nontrivial, so 6 is minimal; with parity "
          "the next available value is c3 = 8, not 7")

    # --- PARITY: a Brunnian carrier has n+ = n-, so c = n+ + n- is EVEN ---
    quarter_even = [(m, F(m, 4) - 3) for m in range(8, 21, 2)]
    best_qe = min(quarter_even, key=lambda t: abs(t[1] - r))
    gap_qe = abs(best_qe[1] - r)

    print(f"\n  PARITY: a Brunnian A=3 carrier has n+ = n-, so c3 is EVEN.")
    print(f"  nearest EVEN quarter point: c(3H)+c(3He) = {best_qe[0]}, "
          f"b3/b2 = {best_qe[1]}  ({float((best_qe[1] - r) / r) * 100:+.2f}%)")

    check("the Brunnian parity constraint EXCLUDES both previously-nearest points",
          best_q[0] % 2 == 1 and best_h[0] % 2 == 1,
          f"the unconstrained nearest were c(3H)+c(3He) = {best_q[0]} and "
          f"c3 = {best_h[0]}, BOTH ODD, hence unreachable by carriers with "
          "n+ = n-; parity is not a refinement of the bound, it deletes the "
          "two points the bound was attained at")

    check("under parity the gap WIDENS to 209293/1483044 (22.01%)",
          gap_qe == F(209293, 1483044) and best_qe[0] == 14,
          f"gap = {gap_qe} = {float(gap_qe):.6f}, "
          f"{float(gap_qe / r) * 100:.2f}% of measured -- up from the "
          f"{float(gap_q / r) * 100:.2f}% that ignoring parity allows; "
          "matches the Lean bound in even_lattice_gap")

    check("a SINGLE Brunnian A=3 carrier makes b3/b2 an integer, nearest +55.98%",
          all((F(c, 2) - 3).denominator == 1 for c in range(2, 13, 2))
          and b_ratio(2, 8) == 1,
          "c3 even => b3/b2 = c3/2 - 3 is an integer; nearest positive is 1 "
          f"at c3 = 8, {float((F(1) - r) / r) * 100:+.2f}%, and 0 at the "
          "Borromean c3 = 6 is the degenerate locus")

    witness = {
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0. The crossing counts are integer braid data and "
            "the quantisation test is on their ratios; the trace is never "
            "evaluated at the substrate modulus. Established by import-cone "
            "trace (cone=1, no q0 import) and by "
            "computations/audits/producer_baked_pin_audit.py, which finds "
            "no q0-valued literal in the source. The witness carries no q0 "
            "field."),
        "computation": "carrier-crossing-quantisation",
        "scriptFile": "probes/carrier_crossing_quantisation_probe.py",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "contentBlock": "qou-brng",
        "description": (
            "The count channel's multiplicity is half the carrier's crossing "
            "count, so with the owner-ruled Hopf pair carrier (c2 = 2) the "
            "ratio b3/b2 = c3/2 - 3 lives on a lattice. The measured "
            "0.6411239316 falls in a gap: the nearest integer carrier "
            "assignment misses by 16.98%. All four carrier rules the corpus "
            "derives give b3/b2 <= 0. Exact rational arithmetic, no free "
            "parameters."),
        "measured": {
            "b2_MeV": str(b2), "b3_MeV": str(b3),
            "b3_over_b2": str(r),
            "required_mu_ratio": str(r + 3),
            "required_c3_given_c2_2": str(2 * (r + 3)),
        },
        "rules": rows,
        "lattice": {
            "unconstrained": {
                "half_integer_nearest": {"c3": best_h[0],
                                         "value": str(best_h[1])},
                "quarter_integer_nearest": {"c_3H_plus_c_3He": best_q[0],
                                            "value": str(best_q[1])},
                "gap": str(gap_q),
                "gap_relative_fraction_of_measured": str(gap_q / r),
                "note": ("BOTH nearest points are ODD and are EXCLUDED once "
                         "the carrier is Brunnian -- see 'brunnian_parity'"),
            },
            "brunnian_parity": {
                "constraint": "n+ = n- => c = n+ + n- is EVEN",
                "nearest": {"c_3H_plus_c_3He": best_qe[0],
                            "value": str(best_qe[1])},
                "gap": str(gap_qe),
                "gap_relative_fraction_of_measured": str(gap_qe / r),
                "single_carrier_nearest_positive": {"c3": 8, "value": "1"},
            },
        },
        "straddle_trap": {
            "c2_from": "owner ruling A 2026-08-29, Hopf deuteron carrier",
            "c3_from": "census volume-match tier (AME-inverted)",
            "value": str(straddle),
            "verdict": "NOT a result -- two different carrier assignments",
        },
        "assertions": assertions,
        "allPassed": ok,
        "scope": (
            "(b) on the CONJUNCTION {count channel, mu = c/2, Hopf pair "
            "carrier c2 = 2, integer crossing counts}, with the invariant "
            "named: integrality of a crossing count. (a) on every ingredient "
            "separately -- it excludes neither the count channel, nor the "
            "Brunnian mechanism (brunnian_binding_survives untouched), nor "
            "mu = c/2. Releasing any one reopens it."),
        "caveats": [
            "CONDITIONAL ON OWNER RULING A (2026-08-29). The obstruction "
            "exists only because c2 is pinned. CountChannelCarrierLocus "
            "correctly records that with mu_pair FREE the count channel has "
            "ample freedom and no quantisation argument applies; that "
            "retraction is not reversed, its hypothesis is now supplied.",
            "The cheapest escape is dropping mu = c/2: a multiplicity that is "
            "not half a crossing count is not lattice-valued, and the "
            "obstruction evaporates. This probe does not argue for mu = c/2 -- "
            "it takes it from CountChannelCarrierLocus.countChannel.",
            "The census row is AME-INVERTED by the atlas registry's own "
            "admission and is NOT a derivation. It appears here only to show "
            "that even it gives the wrong sign when read consistently, so the "
            "circularity is not what rescues the sign -- the straddle is.",
            "b3 uses the isospin-averaged Bbar(3). If 3H and 3He carry "
            "different links the grid refines from half- to quarter-integer, "
            "which is the case computed; it does not become dense.",
            "Three body orders is three data points, and b4 is not tested "
            "here at all. Nothing about A > 4 follows.",
            "The Brunnian parity constraint applies to the A >= 3 carriers "
            "only. The A = 2 Hopf carrier is NOT Brunnian (lk = 1, n+ = 2, "
            "n- = 0) -- it is the boundary case where lk = z = 1 -- so c2 = 2 "
            "is even for a different reason and nothing here depends on that.",
            "The range where the answer could differ (word length >= 8) has "
            "NEVER been searched: the enumeration ran at L_K_max = 3-4, and "
            "L <= 8 over 4 inter-nucleon generators is ~87,000 words against "
            "the ~84 that were tried. This probe does not run that search; it "
            "establishes that the search is the open question.",
        ],
        "lean": ("QOU/Mass/CarrierCrossingQuantisation.lean "
                 "(11 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/pair-locality-shortfall.witness.json",
            "probes/count-channel-carrier-locus.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies; integer crossing counts",
    }
    out = _HERE / "carrier-crossing-quantisation.witness.json"
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
