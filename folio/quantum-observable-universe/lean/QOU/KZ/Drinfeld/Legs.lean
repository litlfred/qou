import QOU.KZ.Drinfeld.Category
import QOU.KZ.BlockResidues

/-!
# The diagonal action on legs, and its compatibility with leg permutations

Stage S2 of bean `qou-zoyv`. For a finite leg set `L` and `a ∈ 𝔤𝔩₂`:

* `leafOp i a` is `a` acting on leg `i`;
* `diag a = ∑_i leafOp i a` is the diagonal action;
* `Obj.ρ X a = diag a` (`ρ_eq_diag`);
* `permL_mul_leafOp`: `P_σ · a^{(i)} = a^{(σ⁻¹ i)} · P_σ`, so every leg permutation commutes with
  the diagonal action (`commute_permL_diag`). In particular every flip and every block Casimir
  commutes with `ρ`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues

variable {L : Type*} [Fintype L] [DecidableEq L]

/-- `a` acting on the leg `i`. -/
def leafOp (i : L) (a : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (L → Fin 2) (L → Fin 2) ℂ :=
  Matrix.of fun y x => a (y i) (x i) * if ∀ j, j ≠ i → y j = x j then 1 else 0

/-- The diagonal action. -/
def diag (L : Type*) [Fintype L] [DecidableEq L] (a : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix (L → Fin 2) (L → Fin 2) ℂ :=
  ∑ i, leafOp i a

theorem permL_mul_leafOp (σ : Equiv.Perm L) (i : L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    permL ℂ 2 σ * leafOp i a = leafOp (σ.symm i) a * permL ℂ 2 σ := by
  ext y x
  rw [Matrix.mul_apply, Matrix.mul_apply,
    Finset.sum_eq_single (y ∘ σ.symm) (fun z _ hz => by
      simp only [permL, permMat, Matrix.of_apply]
      rw [if_neg (fun h => hz (by rw [← h]; funext t; simp)), zero_mul]) (by simp),
    Finset.sum_eq_single (x ∘ σ) (fun z _ hz => by
      simp only [permL, permMat, Matrix.of_apply]
      rw [if_neg (fun h => hz h.symm), mul_zero]) (by simp)]
  simp only [permL, permMat, leafOp, Matrix.of_apply, Function.comp_apply, Equiv.apply_symm_apply]
  rw [if_pos (show (y ∘ ⇑σ.symm) ∘ ⇑σ = y by funext t; simp), one_mul]
  rw [if_true, mul_one]
  congr 1
  apply if_congr _ rfl rfl
  constructor
  · intro h j hj
    have := h (σ j) (by intro e; apply hj; rw [← e]; simp)
    simpa using this
  · intro h j hj
    have := h (σ.symm j) (fun e => hj (σ.symm.injective e))
    simpa using this

/-- Leg permutations commute with the diagonal action. -/
theorem commute_permL_diag (σ : Equiv.Perm L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (permL ℂ 2 σ) (diag L a) := by
  show permL ℂ 2 σ * diag L a = diag L a * permL ℂ 2 σ
  simp only [diag, Finset.mul_sum, Finset.sum_mul, permL_mul_leafOp]
  exact (Equiv.sum_comp σ.symm (fun i => leafOp i a * permL ℂ 2 σ))

theorem commute_tB_diag (S T : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (tB ℂ 2 S T) (diag L a) :=
  Commute.sum_left _ _ _ fun _ _ => Commute.sum_left _ _ _ fun _ _ => commute_permL_diag _ a

theorem leafOp_inl {L' : Type*} [Fintype L'] [DecidableEq L'] (i : L)
    (a : Matrix (Fin 2) (Fin 2) ℂ) :
    leafOp (L := L ⊕ L') (Sum.inl i) a = kron (leafOp i a) 1 := by
  ext y x
  simp only [leafOp, kron_apply, Matrix.of_apply, Matrix.one_apply, Function.comp_apply]
  rw [mul_assoc]
  congr 1
  by_cases h1 : ∀ j, j ≠ i → y (Sum.inl j) = x (Sum.inl j)
  · by_cases h2 : y ∘ Sum.inr = x ∘ Sum.inr
    · rw [if_pos, if_pos h1, if_pos h2, one_mul]
      rintro (j | j) hj
      · exact h1 j (fun e => hj (by rw [e]))
      · exact congrFun h2 j
    · rw [if_neg, if_neg h2, mul_zero]
      intro h; apply h2; funext j; exact h (Sum.inr j) (by simp)
  · rw [if_neg, if_neg h1, zero_mul]
    intro h; apply h1; intro j hj; exact h (Sum.inl j) (by simpa using hj)

theorem leafOp_inr {L' : Type*} [Fintype L'] [DecidableEq L'] (i : L')
    (a : Matrix (Fin 2) (Fin 2) ℂ) :
    leafOp (L := L ⊕ L') (Sum.inr i) a = kron 1 (leafOp i a) := by
  ext y x
  simp only [leafOp, kron_apply, Matrix.of_apply, Matrix.one_apply, Function.comp_apply]
  rw [mul_left_comm]
  congr 1
  by_cases h1 : ∀ j, j ≠ i → y (Sum.inr j) = x (Sum.inr j)
  · by_cases h2 : y ∘ Sum.inl = x ∘ Sum.inl
    · rw [if_pos, if_pos h1, if_pos h2, one_mul]
      rintro (j | j) hj
      · exact congrFun h2 j
      · exact h1 j (fun e => hj (by rw [e]))
    · rw [if_neg, if_neg h2, zero_mul]
      intro h; apply h2; funext j; exact h (Sum.inl j) (by simp)
  · rw [if_neg, if_neg h1, mul_zero]
    intro h; apply h1; intro j hj; exact h (Sum.inr j) (by simpa using hj)

theorem kron_sum_left {α β α' β' ι : Type*} (s : Finset ι)
    (f : ι → Matrix (α → Fin 2) (β → Fin 2) ℂ) (g : Matrix (α' → Fin 2) (β' → Fin 2) ℂ) :
    kron (∑ i ∈ s, f i) g = ∑ i ∈ s, kron (f i) g := by
  ext y x; simp [kron_apply, Matrix.sum_apply, Finset.sum_mul]

theorem kron_sum_right {α β α' β' ι : Type*} (s : Finset ι)
    (f : Matrix (α → Fin 2) (β → Fin 2) ℂ) (g : ι → Matrix (α' → Fin 2) (β' → Fin 2) ℂ) :
    kron f (∑ i ∈ s, g i) = ∑ i ∈ s, kron f (g i) := by
  ext y x; simp [kron_apply, Matrix.sum_apply, Finset.mul_sum]

/-- The recursive action `ρ` is the diagonal action. -/
theorem ρ_eq_diag (X : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) : Obj.ρ X a = diag (Obj.Leaves X) a := by
  induction X with
  | unit => simp [Obj.ρ, diag]
  | V =>
    ext y x
    rw [diag, Fintype.sum_unique]
    simp only [Obj.ρ, leafOp, Matrix.of_apply]
    rw [if_pos (fun j hj => absurd (Subsingleton.elim j default) hj), mul_one]
    try rfl
  | tensor X Y hX hY =>
    rw [Obj.ρ_tensor, hX, hY, diag, diag, diag]
    erw [Fintype.sum_sum_type]
    rw [kron_sum_left, kron_sum_right]
    congr 1
    · exact Finset.sum_congr rfl fun i _ => (leafOp_inl (L' := Obj.Leaves Y) i a).symm
    · exact Finset.sum_congr rfl fun i _ => (leafOp_inr (L := Obj.Leaves X) i a).symm

end QOU.KZ.Drinfeld
