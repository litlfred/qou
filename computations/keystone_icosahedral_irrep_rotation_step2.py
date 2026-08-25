#!/usr/bin/env python3
# polynomial_q_not_applicable: finite icosahedral convergence test; exact in Q(sqrt5).
"""
Keystone fibre map — step 2: is the argmax-χ candidate CANONICAL?  Convergence
test against the independent SO(3)-tower structure.  Also records the candidate
as an explicit CONJECTURE (not wired).

A derived map is canonical only if INDEPENDENT canonical structures agree on it.
Step 1 found two structures:
  * SO(3)↓I tower (icosBranchingMult, in Lean): canonical ORDERING by appearance ℓ
    — first-ℓ {A:0,T₁:1,H:2,T₂:3,G:3} (T₂,G collide); second-ℓ splits them
    {G:4, T₂:5}, giving the canonical tower order  A ≺ T₁ ≺ H ≺ G ≺ T₂.
  * argmax-χ angle map {A:0°,T₁:72°,H:180°,T₂:144°,G:120°}.

CONVERGENCE TEST: does the argmax-χ ANGLE order match the tower APPEARANCE order?
If yes → two independent structures agree → argmax-χ is canonical (promote).
If no  → the angle map is a heuristic, NOT determined by the tower → not canonical
         (the irrep→angle map needs the deeper Bring-equivariant identity).

Exploratory; no fit, nothing wired.  Run:
  python3 -u computations/keystone_icosahedral_irrep_rotation_step2.py 2>&1 | tee /tmp/icos2.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

IRREPS = ["A", "T1", "T2", "G", "H"]

# argmax-χ angle map (degrees) from step 1.
ARGMAX_CHI_DEG = {"A": 0, "T1": 72, "T2": 144, "G": 120, "H": 180}

# SO(3)↓I tower appearances (from the in-Lean icosBranchingMult, ℓ=0..6).
# Each irrep -> sorted list of ℓ at which it occurs.
TOWER_APPEARANCES = {
    "A":  [0, 6],
    "T1": [1, 5, 6],
    "T2": [3, 5],
    "G":  [3, 4, 6],
    "H":  [2, 4, 5, 6],
}


def main() -> int:
    set_compute_dps()

    # canonical tower order: lexicographic by (first ℓ, second ℓ, ...)
    tower_order = sorted(IRREPS, key=lambda r: TOWER_APPEARANCES[r])
    # argmax-χ order: by angle
    angle_order = sorted(IRREPS, key=lambda r: ARGMAX_CHI_DEG[r])

    print("\n  KEYSTONE FIBRE MAP — STEP 2: is argmax-χ canonical? (convergence test)\n")
    print("  SO(3)-tower appearances (ℓ-list):")
    for r in IRREPS:
        print(f"    {r:2}: {TOWER_APPEARANCES[r]}")
    print(f"\n  canonical TOWER order (lex by appearance ℓ): {' ≺ '.join(tower_order)}")
    print(f"  argmax-χ ANGLE order (by degrees):           {' ≺ '.join(angle_order)}")
    print(f"  argmax-χ angles: {ARGMAX_CHI_DEG}\n")

    converge = tower_order == angle_order
    print("  ---------------------------------------------------------------")
    print("  VERDICT (step-2 gate)")
    print(f"   * Tower order   : {tower_order}")
    print(f"   * argmax-χ order: {angle_order}")
    print(f"   * AGREE? {converge}")
    if not converge:
        # locate the disagreement
        diffs = [(r, TOWER_APPEARANCES[r][0], ARGMAX_CHI_DEG[r])
                 for r in IRREPS]
        print("   * They DISAGREE: the argmax-χ angle ordering is NOT the SO(3)-tower")
        print("     appearance ordering.  e.g. H first appears at ℓ=2 (early in the")
        print("     tower) but argmax sends it to 180° (the LARGEST angle); T₂ appears")
        print("     later (ℓ=3) yet gets a smaller angle (144°).  Two independent")
        print("     canonical structures give DIFFERENT maps.")
        print("   => argmax-χ is a HEURISTIC, not canonical.  The irrep→angle map is")
        print("      NOT determined by elementary icosahedral combinatorics (tower +")
        print("      character).  It requires the deeper Bring-equivariant identity")
        print("      (how I↪SO(3) acts on the curve jointly with its G-cohomology).")
        print("   => CONFIRMS the step-1 recommendation: pause the construction; do")
        print("      not wire any instance.  argmax-χ is recorded below as a CONJECTURE.")
    else:
        print("   * They AGREE — argmax-χ is corroborated by the tower; candidate to promote.")
    print()
    print("  CONJECTURE (recorded, NOT wired):")
    print("    conj:s5-so3-argmax-chi-fibre — IF the Bring-induced BringFiberAction")
    print("    map exists, a plausible (unconfirmed) form is the argmax-χ angle map")
    print("    {A:0°, T₁:72°, T₂:144°, G:120°, H:180°}.  Status: HEURISTIC lead only,")
    print("    refuted as canonical by the tower-disagreement above; preserved as a")
    print("    target for the equivariant-identity computation to confirm or refute.\n")

    w = WitnessBuilder("keystone-icosahedral-irrep-rotation-step2", engine="python")
    w.set_description(
        "Convergence test for the keystone fibre map. The argmax-χ candidate angle "
        "order and the canonical SO(3)-tower appearance order DISAGREE, so argmax-χ "
        "is a heuristic, not canonical: the irrep→angle map is not determined by "
        "elementary icosahedral combinatorics and needs the Bring-equivariant "
        "identity. argmax-χ recorded as conj:s5-so3-argmax-chi-fibre (NOT wired).")
    w.add_data("tower_order", tower_order)
    w.add_data("argmax_chi_order", angle_order)
    w.add_data("orders_converge", bool(converge))
    w.add_data("argmax_chi_angle_map_deg", ARGMAX_CHI_DEG)
    w.add_data("conjecture", {
        "label": "conj:s5-so3-argmax-chi-fibre",
        "form": ARGMAX_CHI_DEG,
        "status": "heuristic-lead; refuted-as-canonical-by-tower-disagreement; not wired",
    })
    w.add_assertion("argmax_chi_not_canonical", float(not converge), 1.0,
                    source="argmax-χ angle order ≠ SO(3)-tower appearance order")
    w.add_caveat(
        "Negative/structural result: no convergent canonical irrep→angle map from "
        "elementary icosahedral combinatorics (tower + character disagree). The map "
        "needs the deeper Bring-equivariant identity. Nothing wired; the BringFiberAction "
        "class stays without an instance (genuinely conditional).")
    path = w.save()
    print(f"  witness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
