import Mathlib.Data.List.Basic
import Mathlib.Data.Nat.Basic

/-!
# QOU.Molecular.WaterBraid — H₂O molecular braid

Water assembled as a composite braid in `H₂₈(q)` from three sub-units —
oxygen `O(8,8)` (A+Z = 16+8 = 24 strands) and two hydrogens (2 strands
each) — via the molecular assembly projector `e_{λ,μ}` over the parabolic
subalgebra `H_λ(q)`, `λ = (24,2,2)`. Self-contained per the content-block
`.lean` convention (it carries its strand data directly, matching
`StrandPartition` / `ParabolicHecke`).

The two hydrogen sub-units carry equal strand count, so exchanging them
fixes the strand-partition and hence the assembly projector: that `S₂`
stabiliser is the `C₂ᵥ` symmetry of water — the H₂O instance of "molecular
symmetry = stabiliser of the assembly projector" (benzene's three equal
acetylene units give `S₃`).

## References
- [leitner2026] Ch. 12, Definition: H₂O molecular braid
- [kassel1995] Kassel, "Quantum Groups," GTM 155
-/

namespace QOU.Molecular

/-- The H₂O molecular strand-partition `λ = (24, 2, 2)`: oxygen `O(8,8)`
(24 strands) and two hydrogens (2 strands each). -/
def waterParts : List ℕ := [24, 2, 2]

/-- Total strand count `N = 28`: H₂O is a braid in `H₂₈(q)`. -/
theorem water_total : waterParts.sum = 28 := by decide

/-- Three sub-units: `O`, `H₁`, `H₂`. -/
theorem water_numUnits : waterParts.length = 3 := by decide

/-- Bonding (cross-block) generators `k − 1 = 2`: the two O–H σ-bonds. -/
theorem water_numBonding : waterParts.length - 1 = 2 := by decide

/-- Intra-unit generators `N − k = 25`. -/
theorem water_numGenerators : (waterParts.map (· - 1)).sum = 25 := by decide

/-- Exchange of the two hydrogen sub-units (swap of the 2nd and 3rd parts). -/
def swapH : List ℕ → List ℕ
  | a :: b :: c :: rest => a :: c :: b :: rest
  | l => l

/-- **C₂ᵥ from the projector stabiliser.** Exchanging the two hydrogens
fixes the strand-partition — the two H sub-units carry equal strand count —
so it fixes the assembly projector `e_{λ,μ}`. This `S₂` stabiliser is the
`C₂ᵥ` symmetry of water, the H₂O analogue of benzene's `S₃`. -/
theorem water_h_swap_symmetry : swapH waterParts = waterParts := by decide

end QOU.Molecular
