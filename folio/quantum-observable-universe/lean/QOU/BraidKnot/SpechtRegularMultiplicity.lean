import QOU.BraidKnot.SpechtBlockDimension

/-!
# QOU.BraidKnot.SpechtRegularMultiplicity — the multiplicity of `S^μ` in `k[S_n]`

Brick 4b of **W1+W3** of the Wedderburn epic (`qou-bxw4`), after #5139 (W2), #5151 (Schur
orthonormality), #5156 (`Hom_G(k[G], V) ≃ V`) and #5162 (both sides of the dimension count).

States, in the epic's own vocabulary, the multiplicity fact those bricks add up to:

  `dim_k Hom_G(k[S_n], S^μ) = dim_k S^μ`.

`Hom_G(k[G], V)` is the multiplicity space of `V` in the regular representation — a `k[G]`-map
out of `k[G]` is its value at `[1]`, which is #5156 — and W2 is what makes that space measure
multiplicity *on the nose* rather than in units of `dim End_G(S^μ)`. Together with the
orthonormality of #5151 this is the classical "each irreducible occurs in the regular
representation with multiplicity equal to its dimension", for Specht modules over any
characteristic-zero field.

## Honest scope

This is the **per-partition** statement. It does not sum: concluding
`n! = Σ_μ (dim S^μ)²` needs the multiplicity spaces for distinct `μ` to exhaust and to be
independent, which is the decomposition of the regular module and is not proved here.
`sn_isotypic_specht_split` remains open, and the two keystones that inherit `sorryAx` from it
keep their labels.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]`. No `ℝ`.
-/

namespace QOU.BraidKnot.SpechtRegularMultiplicity

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open QOU.MathlibExt.RepresentationCharacter
open QOU.MathlibExt.RegularHom
open Equiv (Perm)
open Module

variable {k : Type} [Field k] [CharZero k]

omit [CharZero k] in
/-- **The multiplicity of `S^μ` in the regular representation is `dim_k S^μ`.**

Immediate from `RegularHom.finrank_homG_regular` once the Specht module is viewed as a
representation of `Perm (Fin n)`. It is stated separately because `Hom_G(k[G], −)` is only a
*multiplicity* space because the commutant is the base field, which is W2
(`SpechtAbsolutelyIrreducible.specht_end_scalar`, via the orthonormality of
`SpechtSchurDiagonal.finrank_homG_specht`); over a base where the commutant were a larger
division ring this dimension would count multiplicity in units of `dim 𝔇`, not on the nose.

`-- Ref: [sagan2001] §1.10`. -/
theorem finrank_homG_regular_specht {n : ℕ} {μ : YoungDiagram} (h : Specht.nOf μ = n) :
    finrank k (homG (regular k (Perm (Fin n))) (spechtRepAt (k := k) h))
      = finrank k (SpechtSubmodule (k := k) μ) :=
  finrank_homG_regular (spechtRepAt (k := k) h)

omit [CharZero k] in
/-- The same statement indexed by `PartitionIndex n`, the form the block count consumes. -/
theorem finrank_homG_regular_partitionIndex {n : ℕ} (i : PartitionIndex n) :
    finrank k (homG (regular k (Perm (Fin n))) (spechtRepAt (k := k) i.property))
      = finrank k (SpechtSubmodule (k := k) i.diagram) :=
  finrank_homG_regular_specht (k := k) i.property

omit [CharZero k] in
/-- Zero-subtracted difference between the regular representation multiplicity of `S^{i.diagram}` and `dim_k S^{i.diagram}` vanishes. -/
theorem finrank_homG_regular_partitionIndex_sub_eq_zero {n : ℕ} (i : PartitionIndex n) :
    finrank k (homG (regular k (Perm (Fin n))) (spechtRepAt (k := k) i.property))
      - finrank k (SpechtSubmodule (k := k) i.diagram) = 0 := by
  rw [finrank_homG_regular_partitionIndex (k := k) i]
  exact Nat.sub_self _

end QOU.BraidKnot.SpechtRegularMultiplicity
