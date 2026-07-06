#!/usr/bin/env python3
# polynomial_q_not_applicable: finite Reeb-Casimir level + chirality structure of
# the A₅-irrep fibre map. Exact integer/Q(sqrt5) arithmetic.
"""
Keystone fibre map — step 3 ("look to Reeb", owner steer): the Reeb-spin
eigenvalue grades irrepToRotation, BUT it does not separate the chirality pair.

The on-main canonical Reeb eigenvalue (prop:q-heat-kernel-peter-weyl) is
    μ_λ(q) = ℏ_q² Σ_□ [c(□)]_q [c(□)+1]_q    (the content / Reeb-spin Casimir)
indexed by PARTITIONS λ⊢n — NOT the five A₅ irreps. Its A₅-irrep pullback via the
SO(3) tower is the Casimir at first appearance ℓ (classical limit ℓ(ℓ+1)):
    A→ℓ0(0)  T₁→ℓ1(2)  H→ℓ2(6)  T₂→ℓ3(12)  G→ℓ3(12).
=> T₂ and G COLLIDE (both ℓ=3, Casimir 12) — the SAME obstruction as first-ℓ.

The separating invariant is NOT a Reeb level: it is the CHIRALITY (the self-
conjugate (3,1,1)=T₁⊕T₂ split, the deltaSign parity already proved in
S5SO3FiberAction.lean). So the fibre map is a COMPOSITE of two on-main canonical
structures:  irrepToRotation = (Reeb-Casimir level) ⊕ (chirality tie-break).

This advances the construction (pins the structure, grounded on-main) but does
NOT wire the instance: the exact ANGLES need the Seifert-S¹ Reeb weights on
S³/2I (sibling #2524, open) and #2488's A5IrrepToClass bijection (unmerged).
NOT wired.

Exploratory; no fit.  Run:
  python3 -u computations/keystone_reeb_casimir_chirality_step3.py 2>&1 | tee /tmp/icos3.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

IRREPS = ["A", "T1", "T2", "G", "H"]
FIRST_ELL = {"A": 0, "T1": 1, "H": 2, "T2": 3, "G": 3}     # icosBranchingMult (in Lean)
# chirality of the A₅ irreps: T₁/T₂ are the chirality pair (self-conj (3,1,1) split);
# A,G,H are chirality-neutral. (sign = the deltaSign parity from the Lean file.)
CHIRALITY = {"A": 0, "T1": +1, "T2": -1, "G": 0, "H": 0}


def casimir(ell: int) -> int:
    return ell * (ell + 1)


def main() -> int:
    print("\n  KEYSTONE STEP 3 — Reeb-Casimir level + chirality (look-to-Reeb)\n")
    reeb = {r: casimir(FIRST_ELL[r]) for r in IRREPS}
    print("  Reeb-spin Casimir at first-appearance ℓ (classical ℓ(ℓ+1)):")
    for r in IRREPS:
        print(f"    {r:2}: ℓ={FIRST_ELL[r]}  Casimir={reeb[r]:>2}  chirality={CHIRALITY[r]:+d}")
    distinct_reeb = len(set(reeb.values())) == len(reeb)
    # composite key: (Reeb Casimir, chirality)
    comp = {r: (reeb[r], CHIRALITY[r]) for r in IRREPS}
    distinct_comp = len(set(comp.values())) == len(comp)
    collide = [r for r in IRREPS if list(reeb.values()).count(reeb[r]) > 1]

    print(f"\n  Reeb-level alone injective? {distinct_reeb}  "
          f"(collision: {sorted(collide)} both Casimir 12)")
    print(f"  Reeb-level ⊕ chirality injective? {distinct_comp}  "
          f"(chirality {CHIRALITY['T1']:+d}/{CHIRALITY['T2']:+d} splits the ℓ=3 pair)\n")

    print("  ---------------------------------------------------------------")
    print("  VERDICT (step-3)")
    print("   * The Reeb-spin eigenvalue (content-Casimir, prop:q-heat-kernel-peter-weyl)")
    print("     is the canonical grading — but on-main it indexes PARTITIONS, and its")
    print("     A₅-irrep pullback (Casimir at first-ℓ) COLLIDES T₂,G at ℓ=3 (Casimir 12).")
    print("   * The separator is the CHIRALITY (the (3,1,1)=T₁⊕T₂ split / deltaSign,")
    print("     already proved in S5SO3FiberAction.lean) — NOT a finer Reeb level.")
    print("   => Structure pinned (grounded on-main): irrepToRotation =")
    print("        (Reeb-Casimir level)  ⊕  (chirality tie-break).")
    print("      A composite of two on-main canonical structures — NOT a heuristic")
    print("      (unlike argmax-χ, step 2) and NOT separated by SO(3) level alone.")
    print("   * Still NOT wireable: the exact ANGLES need the Seifert-S¹ Reeb weights")
    print("     on S³/2I (#2524, open) + #2488's A5IrrepToClass bijection (unmerged).")
    print("     No BringFiberAction instance is provided (genuinely conditional).\n")

    w = WitnessBuilder("keystone-reeb-casimir-chirality-step3", engine="python")
    w.set_description(
        "Look-to-Reeb structural result. The Reeb-spin eigenvalue μ_λ "
        "(prop:q-heat-kernel-peter-weyl, content-Casimir) indexes partitions; its "
        "A₅-irrep pullback (Casimir at first-ℓ) collides T₂,G at ℓ=3. The chirality "
        "(the (3,1,1)=T₁⊕T₂ split, deltaSign, already Lean-proved) is the separator. "
        "So irrepToRotation = Reeb-Casimir level ⊕ chirality — a composite of two "
        "on-main canonical structures, not a heuristic. Exact angles still need the "
        "Seifert Reeb weights (#2524) + #2488 bijection (unmerged). NOT wired.")
    w.add_data("reeb_casimir_at_first_ell", reeb)
    w.add_data("chirality", CHIRALITY)
    w.add_data("reeb_level_alone_injective", bool(distinct_reeb))
    w.add_data("reeb_plus_chirality_injective", bool(distinct_comp))
    w.add_data("collision", sorted(collide))
    w.add_assertion("reeb_level_collides_T2_G", float(not distinct_reeb), 1.0,
                    source="T₂,G both at ℓ=3, Casimir 12")
    w.add_assertion("reeb_plus_chirality_separates", float(distinct_comp), 1.0,
                    source="chirality +1/-1 splits the ℓ=3 pair")
    w.add_caveat(
        "Structure-pinning, NOT a closure. The composite (Reeb level ⊕ chirality) "
        "is grounded on on-main canonical structures (μ_λ content-Casimir, "
        "icosBranchingMult, deltaSign) but the exact rotation angles need the open "
        "Seifert-S¹ Reeb weights on S³/2I (#2524) and #2488's A5IrrepToClass "
        "bijection (unmerged). No instance wired; BringFiberAction stays conditional.")
    path = w.save()
    print(f"  witness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
