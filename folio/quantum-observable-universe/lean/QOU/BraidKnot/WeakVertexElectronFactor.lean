import QOU.MathlibExt.BraidGroup
import Mathlib.Tactic.Group

/-!
# The weak vertex `(σ₀σ₁)⁵` carries the electron word as a braid factor

Owner ruling 2026-11-21: the electron is the braid word `e⁻ = σ₀σ₁σ₀ ∈ B₃`
(closure: the Hopf link). In `B₃` this word is the Garside element `Δ`.

The β-decay block (`def:beta-decay-skein`) inserts the weak vertex
`β_{T(3,5)} = (σ₀σ₁)⁵`, a positive word of length `10`. This file proves, in
the braid group `B₃` itself (Artin presentation
`QOU.MathlibExt.Braid.BraidGroup 2`), that

    (σ₀σ₁)⁵ = e⁻ · (e⁻ · (σ₀σ₁)²),

so the weak vertex splits into the electron word (`3` letters) and a positive
residue of `7` letters. This is the `3 + 7` crossing split of the β-decay
block, now as an identity of braids rather than a count. The antineutrino is
the trivial one-strand braid and takes `0` letters.

The mirror statement for `β⁺`, with `e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹`, is
`(σ₀⁻¹σ₁⁻¹)⁵ = e⁺ · (e⁺ · (σ₀⁻¹σ₁⁻¹)²)`.

Two further facts are recorded:
* `electron_sq_eq` — `e⁻ · e⁻ = (σ₀σ₁)³`, the full twist;
* `pow_five_eq_of_braid` — the same identity in any group, for any pair satisfying the braid relation.

Nothing here is analytic and no number is compared with experiment.

-- Ref: [kassel2008] Kassel & Turaev, Braid Groups, §1.3 (Garside element, full twist)
-- Ref: [leitner2026] predicted-spectra, beta-decay-skein; docs/coordination/owner-rulings.md
-/

namespace QOU.BraidKnot.WeakVertexElectronFactor

open QOU.MathlibExt.Braid

/-- `σ₀ ∈ B₃`. -/
abbrev s0 : BraidGroup 2 := σ 0
/-- `σ₁ ∈ B₃`. -/
abbrev s1 : BraidGroup 2 := σ 1

/-- The braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` in `B₃`. -/
theorem braid_rel : s0 * s1 * s0 = s1 * s0 * s1 := by
  have hmem : FreeGroup.of (0 : Fin 2) * FreeGroup.of (1 : Fin 2) * FreeGroup.of (0 : Fin 2) *
      (FreeGroup.of (1 : Fin 2) * FreeGroup.of (0 : Fin 2) * FreeGroup.of (1 : Fin 2))⁻¹ ∈
      braidRelators 2 := Or.inr ⟨0, by decide, rfl⟩
  have := PresentedGroup.mk_eq_mk_of_mul_inv_mem hmem
  simpa only [map_mul] using this

/-- The electron word `e⁻ = σ₀σ₁σ₀` (owner ruling 2026-11-21). -/
def electron : BraidGroup 2 := s0 * s1 * s0

/-- The positron word `e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹`. -/
def positron : BraidGroup 2 := s0⁻¹ * s1⁻¹ * s0⁻¹

/-- The weak vertex `β_{T(3,5)} = (σ₀σ₁)⁵`. -/
def weakVertex : BraidGroup 2 := (s0 * s1) ^ 5

/-- The mirror weak vertex `(σ₀⁻¹σ₁⁻¹)⁵` used for `β⁺`. -/
def weakVertexMirror : BraidGroup 2 := (s0⁻¹ * s1⁻¹) ^ 5

/-- `e⁺` is the inverse of `e⁻`. -/
theorem positron_eq_inv : positron = electron⁻¹ := by
  unfold positron electron
  group

/-- In any group, two elements satisfying the braid relation `aba = bab` give
`(ab)⁵ = (aba)·((aba)·(ab)²)`. -/
theorem pow_five_eq_of_braid {G : Type*} [Group G] (a b : G) (hab : a * b * a = b * a * b) :
    (a * b) ^ 5 = a * b * a * (a * b * a * (a * b) ^ 2) := by
  have step : (a * b) ^ 5 = a * b * a * (b * a * b) * (a * b) ^ 2 := by
    simp only [pow_succ, pow_zero, one_mul, mul_assoc]
  rw [step, ← hab]
  group

/-- The full twist: `e⁻ · e⁻ = (σ₀σ₁)³`. -/
theorem electron_sq_eq : electron * electron = (s0 * s1) ^ 3 := by
  unfold electron
  have step : (s0 * s1) ^ 3 = s0 * s1 * s0 * (s1 * s0 * s1) := by
    simp only [pow_succ, pow_zero, one_mul, mul_assoc]
  rw [step, ← braid_rel]

/-- **The weak vertex carries the electron word.**
`(σ₀σ₁)⁵ = e⁻ · (e⁻ · (σ₀σ₁)²)`: the 10-letter vertex is the 3-letter electron
word followed by a 7-letter positive residue. -/
theorem weakVertex_eq_electron_mul : weakVertex = electron * (electron * (s0 * s1) ^ 2) :=
  pow_five_eq_of_braid s0 s1 braid_rel

/-- The braid relation for the inverse generators. -/
theorem braid_rel_inv : s0⁻¹ * s1⁻¹ * s0⁻¹ = s1⁻¹ * s0⁻¹ * s1⁻¹ := by
  have h := congrArg (·⁻¹) braid_rel
  simp only [mul_inv_rev] at h
  simpa only [mul_assoc] using h

/-- **Mirror (β⁺).** `(σ₀⁻¹σ₁⁻¹)⁵ = e⁺ · (e⁺ · (σ₀⁻¹σ₁⁻¹)²)`. -/
theorem weakVertexMirror_eq_positron_mul :
    weakVertexMirror = positron * (positron * (s0⁻¹ * s1⁻¹) ^ 2) :=
  pow_five_eq_of_braid s0⁻¹ s1⁻¹ braid_rel_inv

end QOU.BraidKnot.WeakVertexElectronFactor
