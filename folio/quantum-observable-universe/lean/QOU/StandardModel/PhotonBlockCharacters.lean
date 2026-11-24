/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Tactic

/-!
# The photon's characters on the three blocks of `H₃(q)`

Bean `qou-15sj`.  The `[10]_q` tree coefficient needs the block weights
`(1, 0, −1)` on `(3), (2,1), (1,1,1)` (`T35TenLinchpinFromH3.lean`).  This file
asks whether the photon (owner ruling 2026-11-18/20)

    γ(φ) = 1 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹

supplies them through its block characters.  Characters, with `h = q − q⁻¹`:

* `(3)`:     `σᵢ ↦ q`,     `χ = 1 + (φ₀ + φ₁)·q + φ₀₁`
* `(1,1,1)`: `σᵢ ↦ −q⁻¹`, `χ = 1 − (φ₀ + φ₁)·q⁻¹ + φ₀₁`
* `(2,1)`:   trace of the 2-dimensional representation of
  `T35TenLinchpinFromH3.lean`: `χ = 2 + (φ₀ + φ₁)·h + φ₀₁·(1 − q² − q⁻²)`
  (`tr σᵢ = h`, `tr σ₀σ₁⁻¹ = 1 − q² − q⁻²`).

Results:

* `chiral_vertex_one_dim` — `σ₀σ₁⁻¹` is `1` on both 1-dimensional blocks.
* `photon_supertrace` — `χ₍₃₎ − χ₍₁₁₁₎ = (φ₀ + φ₁)·[2]_q`: the `(1,0,−1)`
  combination drops the identity and the chiral vertex.
* `photon_chars_supertrace_iff` — the character vector is proportional to
  `(1, 0, −1)` (`χ₍₃₎ + χ₍₁₁₁₎ = 0` and `χ₍₂₁₎ = 0`) iff `φ₀₁ = 0` and
  `(φ₀ + φ₁)·h = −2`, given `[3]_q = q² + 1 + q⁻² ≠ 0`.  So a photon with its
  chiral vertex present cannot supply the weights this way.  This is a scoped
  negative about one reading (weights = block characters of `γ`).

No measured value enters this file.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-/

namespace QOU.AlphaEM.PhotonBlocks

variable {K : Type*} [Field K]

/-- Character of `γ` on `(3)`. -/
def chiSym (q φ0 φ1 φ01 : K) : K := 1 + φ0 * q + φ1 * q + φ01 * (q * q⁻¹)

/-- Character of `γ` on `(1,1,1)`. -/
def chiExt (q φ0 φ1 φ01 : K) : K :=
  1 + φ0 * (-q⁻¹) + φ1 * (-q⁻¹) + φ01 * ((-q⁻¹) * (-q⁻¹)⁻¹)

/-- Character of `γ` on `(2,1)`. -/
def chiHook (q φ0 φ1 φ01 : K) : K :=
  2 + (φ0 + φ1) * (q - q⁻¹) + φ01 * (1 - q ^ 2 - (q ^ 2)⁻¹)

theorem chiral_vertex_one_dim (q : K) (hq : q ≠ 0) :
    q * q⁻¹ = 1 ∧ (-q⁻¹) * (-q⁻¹)⁻¹ = 1 := by
  constructor
  · exact mul_inv_cancel₀ hq
  · exact mul_inv_cancel₀ (neg_ne_zero.2 (inv_ne_zero hq))

/-- **The `(1,0,−1)` combination of the photon is `(φ₀ + φ₁)·[2]_q`.** -/
theorem photon_supertrace (q φ0 φ1 φ01 : K) (hq : q ≠ 0) :
    chiSym q φ0 φ1 φ01 - chiExt q φ0 φ1 φ01 = (φ0 + φ1) * (q + q⁻¹) := by
  obtain ⟨h1, h2⟩ := chiral_vertex_one_dim q hq
  unfold chiSym chiExt
  rw [h1, h2]; ring

/-- **The photon's characters are proportional to `(1, 0, −1)` iff the chiral
    vertex is absent and `(φ₀ + φ₁)·h = −2`.** -/
theorem photon_chars_supertrace_iff (q φ0 φ1 φ01 : K) (hq : q ≠ 0)
    (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0) :
    (chiSym q φ0 φ1 φ01 + chiExt q φ0 φ1 φ01 = 0 ∧ chiHook q φ0 φ1 φ01 = 0) ↔
      (φ01 = 0 ∧ (φ0 + φ1) * (q - q⁻¹) = -2) := by
  obtain ⟨h1, h2⟩ := chiral_vertex_one_dim q hq
  have hsum : chiSym q φ0 φ1 φ01 + chiExt q φ0 φ1 φ01
      = 2 + (φ0 + φ1) * (q - q⁻¹) + 2 * φ01 := by
    unfold chiSym chiExt; rw [h1, h2]; ring
  have hdiff : chiSym q φ0 φ1 φ01 + chiExt q φ0 φ1 φ01 - chiHook q φ0 φ1 φ01
      = φ01 * (q ^ 2 + 1 + (q ^ 2)⁻¹) := by
    rw [hsum]; unfold chiHook; ring
  constructor
  · rintro ⟨hs, hh⟩
    have h0 : φ01 * (q ^ 2 + 1 + (q ^ 2)⁻¹) = 0 := by rw [← hdiff, hs, hh]; ring
    have hφ : φ01 = 0 := (mul_eq_zero.1 h0).resolve_right h3
    refine ⟨hφ, ?_⟩
    rw [hsum, hφ] at hs
    linear_combination hs
  · rintro ⟨hφ, hs⟩
    have e1 : chiSym q φ0 φ1 φ01 + chiExt q φ0 φ1 φ01 = 0 := by
      rw [hsum, hφ, hs]; ring
    refine ⟨e1, ?_⟩
    have := hdiff
    rw [e1] at this
    subst hφ
    linear_combination -this

end QOU.AlphaEM.PhotonBlocks
