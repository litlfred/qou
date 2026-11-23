/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.LiftingDescent.SweedlerJetIso

/-!
# Sweedler's algebra is Frobenius, and not symmetric

`SweedlerJetIso.lean` identifies Sweedler's four-dimensional Hopf algebra `H₄` with the
first noncommutative jet `k[ℤ/2] ⋉ Ω¹ᵤ(k[ℤ/2])`. The 2026-11-22 ruling (row 104 of
`docs/coordination/owner-rulings.md`) records that the commutative jet prolongation drops
the Frobenius structure at level `n ≥ 1`. This file checks what happens on the
noncommutative jet instead, over any commutative ring `k`:

* `frob : H₄ →ₗ[k] k`, the coefficient of `G X` in the basis `1, G, X, G X`;
* `frob_mul_coords`: `λ(x y) = a d' + b c' - c b' + d a'` in coordinates;
* `frob_nondegenerate_left` / `_right`: the pairing `(x, y) ↦ λ(x y)` has zero left and
  right radical, so `(H₄, λ)` is a Frobenius algebra;
* `nakayama`: the algebra automorphism `ν` with `G ↦ -G`, `X ↦ -X`, and
  `frob_mul_eq_frob_mul_nakayama`: `λ(x y) = λ(y ν(x))`;
* `not_symmetric_of_isUnit_two`: if `2` is a unit in a nontrivial `k`, no linear form
  `μ` with `μ(x y) = μ(y x)` is nondegenerate; `X` lies in its radical.

So the noncommutative jet level does carry a nondegenerate Frobenius pairing, but it is
symmetric only up to the Nakayama twist `ν`. The ruling itself is about the commutative
jet tower and is unchanged by this file.

No `sorry`.

## References
- [larson-sweedler1969] f.d. Hopf algebras are Frobenius.
- [taft1971] Taft algebras `T_N(ω)` at roots of unity (`N = 2` is Sweedler's `H₄`).
- [lorenz2011] Nakayama automorphism of a Frobenius algebra.
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent.Sweedler

variable (k : Type*) [CommRing k]

/-! ### The Frobenius form -/

/-- The Frobenius form on `H₄`: the coefficient of `G X`, read through `jetMap`. -/
noncomputable def frob : Sweedler k →ₗ[k] k where
  toFun s := coef2 k gZ gZ (val k (jetMap k s).snd)
  map_add' s t := by
    rw [map_add, TrivSqZeroExt.snd_add, val_add, map_add]
  map_smul' c s := by
    rw [map_smul, TrivSqZeroExt.snd_smul, val_smul_k, map_smul]
    rfl

theorem frob_coords (a b c d : k) :
    frob k (a • 1 + b • G k + c • X k + d • (G k * X k)) = d := by
  change coef2 k gZ gZ (val k (jetMap k _).snd) = d
  rw [jetMap_coords]
  simp only [TrivSqZeroExt.snd_add, TrivSqZeroExt.snd_inl, TrivSqZeroExt.snd_inr, zero_add,
    val_add, val_smul_k, val_smul_A, val_dg, g_dgT]
  simp [dgT, map_sub]

theorem frob_one : frob k 1 = 0 := by
  simpa using frob_coords k 1 0 0 0

theorem frob_G : frob k (G k) = 0 := by
  simpa using frob_coords k 0 1 0 0

theorem frob_X : frob k (X k) = 0 := by
  simpa using frob_coords k 0 0 1 0

theorem frob_GX : frob k (G k * X k) = 1 := by
  simpa using frob_coords k 0 0 0 1

/-- The pairing `λ(x y)` in coordinates. -/
theorem frob_mul_coords (a b c d a' b' c' d' : k) :
    frob k ((a • 1 + b • G k + c • X k + d • (G k * X k)) *
      (a' • 1 + b' • G k + c' • X k + d' • (G k * X k))) =
      a * d' + b * c' - c * b' + d * a' := by
  simp only [add_mul, mul_add, Algebra.smul_mul_assoc, Algebra.mul_smul_comm, one_mul,
    mul_one, G_mul_G, X_mul_X, X_mul_G, G_mul_GX, X_mul_GX, GX_mul_G, GX_mul_X, GX_mul_GX,
    ← mul_assoc, smul_zero, mul_neg, neg_mul, smul_neg]
  simp only [map_add, map_smul, map_neg, frob_one, frob_G, frob_X, frob_GX, smul_eq_mul,
    mul_zero, mul_one, neg_zero, add_zero, zero_add, map_zero]
  ring

/-- Left nondegeneracy: if `λ(x y) = 0` for every `y`, then `x = 0`. -/
theorem frob_nondegenerate_left (x : Sweedler k) (h : ∀ y, frob k (x * y) = 0) : x = 0 := by
  obtain ⟨a, b, c, d, rfl⟩ := exists_coords k x
  have h1 := h ((1 : k) • 1 + (0 : k) • G k + (0 : k) • X k + (0 : k) • (G k * X k))
  have h2 := h ((0 : k) • 1 + (1 : k) • G k + (0 : k) • X k + (0 : k) • (G k * X k))
  have h3 := h ((0 : k) • 1 + (0 : k) • G k + (1 : k) • X k + (0 : k) • (G k * X k))
  have h4 := h ((0 : k) • 1 + (0 : k) • G k + (0 : k) • X k + (1 : k) • (G k * X k))
  rw [frob_mul_coords] at h1 h2 h3 h4
  have ha : a = 0 := by linear_combination h4
  have hb : b = 0 := by linear_combination h3
  have hc : c = 0 := by linear_combination -h2
  have hd : d = 0 := by linear_combination h1
  simp [ha, hb, hc, hd]

/-- Right nondegeneracy: if `λ(x y) = 0` for every `x`, then `y = 0`. -/
theorem frob_nondegenerate_right (y : Sweedler k) (h : ∀ x, frob k (x * y) = 0) : y = 0 := by
  obtain ⟨a, b, c, d, rfl⟩ := exists_coords k y
  have h1 := h ((1 : k) • 1 + (0 : k) • G k + (0 : k) • X k + (0 : k) • (G k * X k))
  have h2 := h ((0 : k) • 1 + (1 : k) • G k + (0 : k) • X k + (0 : k) • (G k * X k))
  have h3 := h ((0 : k) • 1 + (0 : k) • G k + (1 : k) • X k + (0 : k) • (G k * X k))
  have h4 := h ((0 : k) • 1 + (0 : k) • G k + (0 : k) • X k + (1 : k) • (G k * X k))
  rw [frob_mul_coords] at h1 h2 h3 h4
  have ha : a = 0 := by linear_combination h4
  have hb : b = 0 := by linear_combination -h3
  have hc : c = 0 := by linear_combination h2
  have hd : d = 0 := by linear_combination h1
  simp [ha, hb, hc, hd]

/-! ### The Nakayama automorphism -/

theorem negG_sq : (-G k) * (-G k) = 1 := by rw [neg_mul_neg, G_mul_G]

theorem negX_sq : (-X k) * (-X k) = 0 := by rw [neg_mul_neg, X_mul_X]

theorem negX_negG : (-X k) * (-G k) = -((-G k) * (-X k)) := by
  rw [neg_mul_neg, neg_mul_neg, X_mul_G]

/-- The Nakayama automorphism of `(H₄, λ)`: `G ↦ -G`, `X ↦ -X`. -/
noncomputable def nakayama : Sweedler k →ₐ[k] Sweedler k :=
  lift (-G k) (-X k) (negG_sq k) (negX_sq k) (negX_negG k)

theorem nakayama_coords (a b c d : k) :
    nakayama k (a • 1 + b • G k + c • X k + d • (G k * X k)) =
      a • 1 + (-b) • G k + (-c) • X k + d • (G k * X k) := by
  simp only [map_add, map_smul, map_one, map_mul, nakayama, lift_G, lift_X, neg_mul_neg,
    neg_smul, smul_neg]

/-- `ν` is an involution, hence an automorphism. -/
theorem nakayama_nakayama (x : Sweedler k) : nakayama k (nakayama k x) = x := by
  obtain ⟨a, b, c, d, rfl⟩ := exists_coords k x
  rw [nakayama_coords, nakayama_coords, neg_neg, neg_neg]

/-- **The Frobenius pairing is symmetric up to the Nakayama twist:** `λ(x y) = λ(y ν(x))`. -/
theorem frob_mul_eq_frob_mul_nakayama (x y : Sweedler k) :
    frob k (x * y) = frob k (y * nakayama k x) := by
  obtain ⟨a, b, c, d, rfl⟩ := exists_coords k x
  obtain ⟨a', b', c', d', rfl⟩ := exists_coords k y
  rw [nakayama_coords, frob_mul_coords, frob_mul_coords]
  ring

/-- `λ` itself is not symmetric: `λ(G X) = 1` while `λ(X G) = -1`. -/
theorem frob_GX_XG : frob k (G k * X k) = 1 ∧ frob k (X k * G k) = -1 := by
  refine ⟨frob_GX k, ?_⟩
  rw [X_mul_G, map_neg, frob_GX]

/-! ### No symmetric Frobenius form when `2` is a unit -/

/-- If `2` is a unit, every linear form `μ` with `μ(x y) = μ(y x)` has `X` in its radical. -/
theorem symm_form_kills_X (h2 : IsUnit (2 : k)) (μ : Sweedler k →ₗ[k] k)
    (hμ : ∀ x y, μ (x * y) = μ (y * x)) (y : Sweedler k) : μ (y * X k) = 0 := by
  have hX : μ (X k) = 0 := by
    have h := hμ (G k) (G k * X k)
    rw [G_mul_GX, GX_mul_G, map_neg] at h
    have h' : (2 : k) * μ (X k) = 0 := by linear_combination h
    exact (h2.mul_right_eq_zero).mp h'
  have hGX : μ (G k * X k) = 0 := by
    have h := hμ (G k) (X k)
    rw [X_mul_G, map_neg] at h
    have h' : (2 : k) * μ (G k * X k) = 0 := by linear_combination h
    exact (h2.mul_right_eq_zero).mp h'
  obtain ⟨a, b, c, d, rfl⟩ := exists_coords k y
  simp only [add_mul, Algebra.smul_mul_assoc, one_mul, X_mul_X, GX_mul_X,
    smul_zero, add_zero, map_add, map_smul, hX, hGX, smul_eq_mul, mul_zero]

/-- **`H₄` is not a symmetric Frobenius algebra when `2` is a unit:** no symmetric linear
form on `H₄` is nondegenerate. -/
theorem not_symmetric_of_isUnit_two [Nontrivial k] (h2 : IsUnit (2 : k))
    (μ : Sweedler k →ₗ[k] k) (hμ : ∀ x y, μ (x * y) = μ (y * x)) :
    ¬ ∀ y : Sweedler k, (∀ x, μ (x * y) = 0) → y = 0 := by
  intro hnd
  have hX0 : X k = 0 := hnd (X k) (symm_form_kills_X k h2 μ hμ)
  have h := congrArg (frob k) (congrArg (fun z => G k * z) hX0)
  simp only [mul_zero, map_zero, frob_GX] at h
  exact one_ne_zero h

end QOU.LiftingDescent.Sweedler
