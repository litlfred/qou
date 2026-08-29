#!/usr/bin/env python3
"""The mirror mechanism cannot produce the quark charges it is said to produce.

`def:down-quark` and `rem:up-quark-properties` state one mechanism and
one pair of numbers, and the two are incompatible.

**The mechanism.** The down quark "differs from the up quark only by
crossing orientation": at every crossing where the up strand passes
over, the down strand passes under. `down-quark.lean` formalises
exactly this and proves it, sorry-free —

    quark_crossing_asymmetry :
      DownQuark.crossing_orientation = -(UpQuark.crossing_orientation)

**The numbers.** The same two blocks assign the up quark a "Coulomb
charge contribution of +2/3" and the down quark "-1/3".

**The obstruction.** `def:coulomb-charge` is `Q = (n_+ - n_-)/2`, which
is *odd* under the mirror `(n_+, n_-) -> (n_-, n_+)`. So the mechanism
forces `Q(d) = -Q(u)`: equal magnitude, opposite sign. The asserted
pair has ratio `-2`. No crossing count repairs this — it is a symmetry
statement, independent of how many crossings a colour tube carries.

This script establishes four exact facts, in `fractions.Fraction`
throughout (no floating point anywhere, and no numerical anchor: the
argument is independent of q).

  1. `Q` is odd under the mirror, exhaustively on a grid.
  2. The asserted ratio `-2` is therefore unreachable, for every
     crossing count.
  3. `Q` takes values in `(1/2)Z`, so `+/-2/3` and `+/-1/3` are outside
     its range for *every* braid word -- a second, independent failure.
  4. The sharp consequence: under any charge that is odd under the
     mirror, `Q(neutron) = -Q(proton)`. Demanding the neutron be
     neutral forces every quark charge to vanish, and hence the proton
     to be neutral too. Equivalently, the mechanism predicts a neutron
     of charge `-1` alongside a proton of charge `+1`.

Fact 4 is the one that bites, because it is mechanism-independent: it
uses only oddness under orientation reversal, not the particular form
`(n_+ - n_-)/2`. The Standard Model's assignment works precisely
because `|Q_u| = 2|Q_d|`, an asymmetry between the two orientations
that a pure mirror cannot supply.

**Scope, per the (a)/(b) discipline.** Fact 4 is a scope-(b)
*structural exclusion*: the invariant is oddness of the charge under
crossing-orientation reversal, which `down-quark.lean` proves the two
quarks are related by. It excludes the stated mechanism as a route to
the observed charges. It does *not* exclude the framework from
deriving fractional charge by some other route -- see
`flavor-charge-assignments`, which already records the ribbon
content-sum route as a tested scope-(a) refutation.

Cross-references:
  - `def:coulomb-charge`  (Q = (n_+ - n_-)/2)
  - `def:down-quark`, `rem:up-quark-properties`  (the two blocks)
  - `def:categorical-neutron`  (asserts 1*(+2/3) + 2*(-1/3) = 0)
  - `prop:flavor-charge-assignments`  (the honest treatment)
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# Path bridge (subdirectory refactor): keeps flat-namespace imports
# (`from witness_base import …`) resolving from the `probes/` cluster.
import _path_bridge as _bridge  # noqa: E402, F401

WITNESS_OUT = HERE / "quark-charge-mirror-obstruction-probe.witness.json"

# The asserted per-quark charges, exactly.
Q_UP_ASSERTED = Fraction(2, 3)
Q_DOWN_ASSERTED = Fraction(-1, 3)

# Crossing-count grid. B_3 gives each component 4 crossings with the
# other two in the standard 6-crossing diagram; the grid runs well past
# that so the conclusion cannot be an artefact of the bound.
GRID = 9


def coulomb_charge(n_plus: int, n_minus: int) -> Fraction:
    """`def:coulomb-charge`: Q = (n_+ - n_-)/2."""
    return Fraction(n_plus - n_minus, 2)


def fact1_mirror_is_odd() -> dict:
    """Q(mirror(w)) = -Q(w) on every grid cell, exactly."""
    checked = 0
    failures = []
    for n_plus in range(GRID):
        for n_minus in range(GRID):
            q = coulomb_charge(n_plus, n_minus)
            q_mirror = coulomb_charge(n_minus, n_plus)
            checked += 1
            if q_mirror != -q:
                failures.append([n_plus, n_minus, str(q), str(q_mirror)])
    return {
        "claim": "Q(n_-, n_+) = -Q(n_+, n_-) for all crossing counts",
        "cells_checked": checked,
        "failures": failures,
        "holds": not failures,
    }


def fact2_ratio_obstruction() -> dict:
    """A mirror pair has ratio -1; the asserted pair has ratio -2."""
    asserted_ratio = Q_UP_ASSERTED / Q_DOWN_ASSERTED
    # For every crossing count, the mirror pair's ratio.
    mirror_ratios = set()
    for n_plus in range(GRID):
        for n_minus in range(GRID):
            q_up = coulomb_charge(n_plus, n_minus)
            q_down = coulomb_charge(n_minus, n_plus)
            if q_down != 0:
                mirror_ratios.add(q_up / q_down)
    return {
        "claim": "no crossing count gives the asserted ratio",
        "asserted_ratio_Qu_over_Qd": str(asserted_ratio),
        "mirror_ratios_attainable": sorted(str(r) for r in mirror_ratios),
        "asserted_ratio_attainable": asserted_ratio in mirror_ratios,
        "obstruction_holds": asserted_ratio not in mirror_ratios,
    }


def fact3_representability() -> dict:
    """Q lands in (1/2)Z, so thirds are outside its range entirely."""
    attained = {coulomb_charge(a, b)
                for a in range(GRID) for b in range(GRID)}
    thirds = [Fraction(2, 3), Fraction(-1, 3),
              Fraction(1, 3), Fraction(-2, 3)]
    return {
        "claim": "Q in (1/2)Z; thirds are unrepresentable",
        "grid": GRID,
        "any_third_attained": [str(t) for t in thirds if t in attained],
        "all_attained_have_denominator_dividing_two": all(
            v.denominator in (1, 2) for v in attained),
        "obstruction_holds": not any(t in attained for t in thirds),
    }


def fact4_neutron_neutrality(a: Fraction) -> dict:
    """Mechanism-independent: any odd-under-mirror charge gives
    Q(neutron) = -Q(proton).

    Only oddness is used: Q(u) = a forces Q(d) = -a. The proton is
    `uud`, the neutron `udd`.
    """
    q_up, q_down = a, -a
    proton = 2 * q_up + q_down          # uud
    neutron = q_up + 2 * q_down         # udd
    # The same sums under the Standard Model assignment, for contrast.
    sm_up, sm_down = Fraction(2, 3), Fraction(-1, 3)
    sm_proton = 2 * sm_up + sm_down
    sm_neutron = sm_up + 2 * sm_down
    return {
        "Q_up": str(q_up),
        "Q_down_forced_by_mirror": str(q_down),
        "Q_proton_uud": str(proton),
        "Q_neutron_udd": str(neutron),
        "neutron_equals_minus_proton": neutron == -proton,
        "neutron_neutral": neutron == 0,
        "standard_model_proton": str(sm_proton),
        "standard_model_neutron": str(sm_neutron),
        "sm_magnitude_ratio_up_over_down": str(abs(sm_up / sm_down)),
    }


def main() -> int:
    print("Quark charge under the mirror mechanism — exact, no floating point")
    print("=" * 70)

    f1 = fact1_mirror_is_odd()
    print(f"\n[1] {f1['claim']}")
    print(f"    cells checked: {f1['cells_checked']}   "
          f"failures: {len(f1['failures'])}   holds: {f1['holds']}")

    f2 = fact2_ratio_obstruction()
    print(f"\n[2] {f2['claim']}")
    print(f"    asserted  Q_u/Q_d = {f2['asserted_ratio_Qu_over_Qd']}")
    print(f"    attainable by any mirror pair: "
          f"{', '.join(f2['mirror_ratios_attainable'])}")
    print(f"    obstruction holds: {f2['obstruction_holds']}")

    f3 = fact3_representability()
    print(f"\n[3] {f3['claim']}")
    print(f"    thirds attained on the {GRID}x{GRID} grid: "
          f"{f3['any_third_attained'] or 'none'}")
    print(f"    every attained value has denominator | 2: "
          f"{f3['all_attained_have_denominator_dividing_two']}")
    print(f"    obstruction holds: {f3['obstruction_holds']}")

    print("\n[4] neutron neutrality under an odd-under-mirror charge")
    ladder = []
    for a in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(0)):
        row = fact4_neutron_neutrality(a)
        ladder.append(row)
        print(f"    Q_u = {row['Q_up']:>4}  ->  Q_d = "
              f"{row['Q_down_forced_by_mirror']:>4}   "
              f"proton {row['Q_proton_uud']:>4}   "
              f"neutron {row['Q_neutron_udd']:>4}   "
              f"neutron neutral: {row['neutron_neutral']}")
    only_zero = [r for r in ladder if r["neutron_neutral"]]
    print(f"    neutron is neutral only when Q_u = 0, which makes the "
          f"proton neutral too: "
          f"{all(r['Q_proton_uud'] == '0' for r in only_zero)}")
    print(f"    Standard Model, for contrast: proton "
          f"{ladder[0]['standard_model_proton']}, neutron "
          f"{ladder[0]['standard_model_neutron']}, with "
          f"|Q_u/Q_d| = {ladder[0]['sm_magnitude_ratio_up_over_down']} "
          f"— the mirror forces this ratio to 1.")

    verdict = (f1["holds"] and f2["obstruction_holds"]
               and f3["obstruction_holds"])

    print("\n" + "=" * 70)
    print("VERDICT: the mechanism stated in `def:down-quark` and "
          "`rem:up-quark-properties`")
    print("         cannot produce the charges those blocks assert. It "
          "forces")
    print("         Q(d) = -Q(u), hence Q(neutron) = -Q(proton): a neutron "
          "of")
    print("         charge -1 beside a proton of +1. The charges are "
          "asserted,")
    print("         not derived.  obstruction established: "
          f"{verdict}")

    out = {
        "schemaVersion": "1.0.0",
        "description": (
            "Exact obstruction: the crossing-orientation mirror that "
            "def:down-quark states as its mechanism forces Q(d) = -Q(u), "
            "which is incompatible with the asserted +2/3 / -1/3 and "
            "makes the neutron non-neutral whenever the proton is charged."
        ),
        "computation": {
            "script": "computations/probes/"
                      "quark_charge_mirror_obstruction_probe.py",
            "arithmetic": "exact rational (fractions.Fraction) throughout; "
                          "no floating point, no numerical q anchor",
        },
        "facts": {
            "mirror_is_odd": f1,
            "ratio_obstruction": f2,
            "representability": f3,
            "neutron_neutrality_ladder": ladder,
        },
        "summary": {
            "obstruction_established": verdict,
            "scope": "(b) structural exclusion of the STATED MECHANISM, "
                     "not of the framework deriving fractional charge by "
                     "another route",
            "invariant_cited": "oddness of the Coulomb charge under "
                               "crossing-orientation reversal, which "
                               "down-quark.lean proves relates the two "
                               "quarks (quark_crossing_asymmetry)",
            "headline": "the mechanism predicts Q(neutron) = -Q(proton); "
                        "neutron neutrality forces every quark charge to 0",
            "note": (
                "Two independent failures, either alone sufficient: the "
                "ratio must be -1 and is asserted as -2; and Q lies in "
                "(1/2)Z so thirds are unreachable for every braid word. "
                "The Standard Model assignment needs |Q_u| = 2|Q_d|, an "
                "asymmetry between the two orientations that a pure mirror "
                "cannot supply."
            ),
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
