/-!
# QOU.BraidGroup

The braid group B₃ = ⟨σ₁, σ₂ | σ₁σ₂σ₁ = σ₂σ₁σ₂⟩,
isomorphic to the fundamental group of the configuration space
of three unordered points in the plane.

LaTeX label: `def:braid-group`

## References

- [birman1974] https://doi.org/10.1515/9781400881420
-/

import QOU.Basic

namespace QOU

/-- **Braid group on n strands**: abstract presentation with
    Artin generators σ₁, ..., σ_{n-1} satisfying the braid relation. -/
-- Ref: [birman1974] Braids, Links, and Mapping Class Groups — see content/schema/references.ts
structure BraidGroupData where
  /-- Number of strands. -/
  numStrands : ℕ
  /-- numStrands ≥ 2. -/
  strands_ge_two : 2 ≤ numStrands
  /-- The group of braids. -/
  BraidType : Type*
  /-- Group structure. -/
  [grp : Group BraidType]
  /-- Artin generators σᵢ for 0 ≤ i < n-1. -/
  sigma : Fin (numStrands - 1) → BraidType
  /-- Braid relation: σᵢ σⱼ σᵢ = σⱼ σᵢ σⱼ for |i-j| = 1. -/
  braid_relation : ∀ (i j : Fin (numStrands - 1)),
    i.val + 1 = j.val →
    sigma i * sigma j * sigma i = sigma j * sigma i * sigma j

attribute [instance] BraidGroupData.grp

/-- B₃ has exactly 2 Artin generators. -/
-- Ref: [birman1974]
theorem b3_generators (bg : BraidGroupData) (h : bg.numStrands = 3) :
    bg.numStrands - 1 = 2 := by omega

end QOU
