import QOU.BraidsAndKnots.RationalAssociator.ExpHalfTrunc

/-!
# An explicit rational associator modulo `4`, for the level-`4` exponential

Audit `docs/audits/2026-11-27-grt-action-pentagon-derivation.md` §17q.

`ExpHalfTrunc.lean` gives `1 + [X, Y]/24` as an associator modulo `3` (`assocU4_three`). This
file goes one degree up, unconditionally:

* `assocU4_four`: `φ = 1 + [X, Y]/24` is a rational associator in `U4 4` for the level-`4`
  exponential `expHalfTrunc 4 = 1 + X/2 + X²/8 + X³/48`. No degree-`3` correction is needed:
  the degree-`3` part of the hexagon defect of `φ` is exactly cancelled by the new monomial
  `X³/48` of the level-`4` exponential (for the level-`3` exponential it is not).
* `GL_four`: `φ` is group-like modulo `FF2 4`.
* `exists_assoc_GL_four`: hence `∃ Φ, AssocU4 4 (expHalfTrunc 4) Φ ∧ GL 4 Φ`.

The degree-`3` linear system was solved exactly over `ℚ` by
`computations/audits/rational_associator_level4_probe.py` (exact `Fraction` arithmetic): its
solutions are `φ + α·([X,[X,Y]] + [Y,[X,Y]])`, `α ∈ ℚ` free (the `GRT` direction in degree `3`);
`α = 0` is the one proved here. The Lean proof does not use the probe.

Method. In `U4 4` every product of four elements of `Fil 1` vanishes (`trunc4_fil`). For the
hexagon, `z = t₁₂ + t₁₃ + t₂₃` commutes with `t₁₂` and `t₁₃` (Drinfeld–Kohno), so after
`t₂₃ = z − t₁₂ − t₁₃` the identity is checked by moving `z` to the left and truncating
(`hexagon4_central`, valid in any `ℚ`-algebra). The pentagon and inversion hold because
`φ − 1` has no degree-`1` part, so every product of two corrections has degree `4`.

No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

section Abstract

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- Every word of length four in elements of `S` vanishes (right-associated form). -/
def Trunc4 (S : Set R) : Prop :=
  ∀ {x y z w : R}, x ∈ S → y ∈ S → z ∈ S → w ∈ S → x * (y * (z * w)) = 0

/-- `exp(x/2)` truncated at degree `4`. -/
def expHalf4 (x : R) : R :=
  1 + (1 / 2 : ℚ) • x + (1 / 8 : ℚ) • (x * x) + (1 / 48 : ℚ) • (x * (x * x))

/-- **The hexagon modulo degree `4`**, with `t₂₃ = z − a − b` and `z` commuting with
`a = t₁₂`, `b = t₁₃`. -/
theorem hexagon4_central {a b z : R} (h : Trunc4 ({a, b, z} : Set R))
    (ha : Commute z a) (hb : Commute z b) :
    expHalf4 (b + (z - a - b)) =
      phi (1 / 24) b a * expHalf4 b * phi (1 / 24) (z - a - b) b * expHalf4 (z - a - b) *
        phi (1 / 24) a (z - a - b) := by
  unfold Trunc4 at h
  have e1 : a * z = z * a := ha.eq.symm
  have e2 : b * z = z * b := hb.eq.symm
  have e1' : ∀ w : R, a * (z * w) = z * (a * w) := fun w => by rw [← mul_assoc, e1, mul_assoc]
  have e2' : ∀ w : R, b * (z * w) = z * (b * w) := fun w => by rw [← mul_assoc, e2, mul_assoc]
  simp only [phi, expHalf4, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one, mul_assoc, smul_zero, sub_zero, add_zero, mul_zero, smul_add,
    smul_sub, e1, e2, e1', e2', h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
  module

/-- Inversion modulo degree `4`. -/
theorem inversion4 (c : ℚ) {a b : R} (h : Trunc4 ({a, b} : Set R)) :
    phi c a b * phi c b a = 1 := by
  unfold Trunc4 at h
  simp only [phi, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, mul_assoc, smul_zero, sub_zero, smul_sub,
    h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
  module

/-- The pentagon modulo degree `4`, for every `c`. -/
theorem pentagon4 (c : ℚ) {t12 t13 t14 t23 t24 t34 : R}
    (h : Trunc4 ({t12, t13, t14, t23, t24, t34} : Set R))
    (d1 : Commute t12 t34) (d2 : Commute t13 t24) :
    phi c t12 (t23 + t24) * phi c (t13 + t23) t34 =
      phi c t23 t34 * phi c (t12 + t13) (t24 + t34) * phi c t12 t23 := by
  unfold Trunc4 at h
  have e1 := d1.eq
  have e2 := d2.eq
  simp only [phi, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, mul_assoc, smul_zero, sub_zero, add_zero, smul_add, smul_sub,
    h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
  rw [e1, e2]
  module

end Abstract

/-! ### In `U4 4` -/

theorem trunc4_fil {S : Set (U4 4)} (hS : ∀ w ∈ S, w ∈ Fil 4 1) : Trunc4 S :=
  fun hx hy hz hw => eq_zero_of_mem_Fil (mul_mem_Fil' (a := 1) (b := 3) (c := 4) rfl (hS _ hx)
    (mul_mem_Fil' (a := 1) (b := 2) (c := 3) rfl (hS _ hy)
      (mul_mem_Fil' (a := 1) (b := 1) (c := 2) rfl (hS _ hz) (hS _ hw))))

theorem eval_expHalfTrunc_four {R : Type*} [Ring R] [Algebra ℚ R] (x : R) :
    eval x 0 (expHalfTrunc 4) = expHalf4 x := by
  simp only [expHalfTrunc, Finset.sum_range_succ, Finset.sum_range_zero, zero_add, map_add,
    map_smul, map_pow, eval_X, expHalf4]
  norm_num [Nat.factorial, pow_succ, mul_assoc]

/-- **A rational associator modulo `4`** for the level-`4` exponential: `1 + [X, Y]/24`. -/
theorem assocU4_four : AssocU4 4 (expHalfTrunc 4) (phiPoly (1 / 24)) where
  const := by simp [phiPoly, FreeAlgebra.algebraMapInv]
  inv := fun a b ha hb => by
    rw [eval_phiPoly, eval_phiPoly]
    refine inversion4 _ (trunc4_fil ?_)
    intro w hw; rcases hw with rfl | rfl <;> assumption
  hex := by
    have dk := dk4 4
    set a := t 4 0
    set b := t 4 1
    set z := a + b + t 4 3 with hz
    have h3 : t 4 3 = z - a - b := by rw [hz]; abel
    have hza : Commute z a := by
      rw [hz, add_assoc]; exact (Commute.refl a).add_left dk.n12_3.symm
    have hzb : Commute z b := by
      rw [hz, add_comm a b, add_assoc]; exact (Commute.refl b).add_left dk.n13_2.symm
    have hzF : z ∈ Fil 4 1 := add_mem (add_mem (t_mem_Fil_one _) (t_mem_Fil_one _))
      (t_mem_Fil_one _)
    have hT : Trunc4 ({a, b, z} : Set (U4 4)) := by
      refine trunc4_fil ?_
      intro w hw; rcases hw with rfl | rfl | rfl
      · exact t_mem_Fil_one _
      · exact t_mem_Fil_one _
      · exact hzF
    unfold Hexagon
    simp only [eval_phiPoly, eval_expHalfTrunc_four]
    rw [h3]
    exact hexagon4_central hT hza hzb
  pent := by
    have dk := dk4 4
    unfold Pentagon
    simp only [eval_phiPoly]
    refine pentagon4 _ (t14 := t 4 2) (trunc4_fil ?_) dk.f12_34 dk.f13_24
    intro w hw; rcases hw with rfl | rfl | rfl | rfl | rfl | rfl <;> exact t_mem_Fil_one _

/-- `[X, Y]` is primitive. -/
theorem isPrimitive_commXY :
    IsPrimitive (FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 - FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0) :=
  IsPrimitive.commutator (isPrimitive_ι 0) (isPrimitive_ι 1)

/-- **`1 + c·[X, Y]` is group-like modulo `FF2 4`**: its defect is `−c²·[X,Y] ⊗ [X,Y]`. -/
theorem GL_four (c : ℚ) : GL 4 (phiPoly c) := by
  set L : F2 := FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 - FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0
    with hL
  have hp : cop L = L ⊗ₜ 1 + 1 ⊗ₜ L := isPrimitive_commXY
  have e : cop (phiPoly c) - phiPoly c ⊗ₜ phiPoly c = -((c * c) • (L ⊗ₜ L)) := by
    have : phiPoly c = 1 + c • L := rfl
    rw [this, map_add, map_one, map_smul, hp]
    simp only [add_tmul, tmul_add, smul_tmul', tmul_smul, smul_add, smul_smul,
      Algebra.TensorProduct.one_def]
    abel
  unfold GL
  rw [e]
  exact neg_mem (Submodule.smul_mem _ _ (tmul_mem_FF2 (i := 2) (j := 2) commutator_mem_FF2
    commutator_mem_FF2))

/-- **Level `4`, unconditionally**: a rational associator modulo `4` for `expHalfTrunc 4`,
group-like modulo `FF2 4`. -/
theorem exists_assoc_GL_four : ∃ Φ : F2, AssocU4 4 (expHalfTrunc 4) Φ ∧ GL 4 Φ :=
  ⟨phiPoly (1 / 24), assocU4_four, GL_four _⟩

end QOU.BraidsAndKnots.RationalAssociator
