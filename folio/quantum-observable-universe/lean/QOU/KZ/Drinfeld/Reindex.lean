import QOU.KZ.Drinfeld.Legs

/-!
# Reindexing tensor powers along a bijection of legs

Stage S2 of bean `qou-zoyv`. For a bijection of legs `e : L ≃ L'`, `reidx e : V^{⊗L} → V^{⊗L'}`
is the induced linear isomorphism. It intertwines:

* flips: `reidx e · P_{ij} = P_{e i, e j} · reidx e`;
* block Casimirs: `reidx e · t_{S,T} = t_{e S, e T} · reidx e`;
* single-leg operators and the diagonal action.

It is also functorial: `reidx e' · reidx e = reidx (e.trans e')` and `reidx (refl) = 1`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues

variable {L L' L'' : Type*} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']
  [Fintype L''] [DecidableEq L'']

/-- The reindexing isomorphism `V^{⊗L} → V^{⊗L'}`. -/
def reidx (e : L ≃ L') : Matrix (L' → Fin 2) (L → Fin 2) ℂ :=
  Matrix.of fun y x => if x = y ∘ e then 1 else 0

theorem reidx_mul (e : L ≃ L') (e' : L' ≃ L'') : reidx e' * reidx e = reidx (e.trans e') := by
  ext z x
  simp only [Matrix.mul_apply, reidx, Matrix.of_apply, ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq' Finset.univ (z ∘ e')]
  simp only [Finset.mem_univ, if_true]
  rfl

theorem reidx_refl : reidx (Equiv.refl L) = 1 := by
  ext y x
  simp only [reidx, Matrix.of_apply, Matrix.one_apply, Equiv.coe_refl, Function.comp_id, eq_comm]

/-- Multiplying a matrix on the left by `reidx e` permutes its rows. -/
theorem reidx_mul_apply {κ : Type*} (e : L ≃ L') (M : Matrix (L → Fin 2) κ ℂ) (y k) :
    (reidx e * M) y k = M (y ∘ e) k := by
  simp only [Matrix.mul_apply, reidx, Matrix.of_apply, ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq' Finset.univ (y ∘ e)]
  simp

/-- Multiplying a matrix on the right by `reidx e` permutes its columns. -/
theorem mul_reidx_apply {κ : Type*} [Fintype κ] (e : L ≃ L') (M : Matrix κ (L' → Fin 2) ℂ) (k x) :
    (M * reidx e) k x = M k (x ∘ e.symm) := by
  simp only [Matrix.mul_apply, reidx, Matrix.of_apply, mul_ite, mul_one, mul_zero]
  rw [Finset.sum_eq_single (x ∘ e.symm) (fun y _ hy => by
      rw [if_neg]; intro h; apply hy; rw [h]; funext t; simp)
    (by simp)]
  rw [if_pos (by funext t; simp)]

theorem reidx_flip (e : L ≃ L') (i j : L) :
    reidx e * flipL ℂ 2 i j = flipL ℂ 2 (e i) (e j) * reidx e := by
  ext y x
  rw [reidx_mul_apply, mul_reidx_apply]
  simp only [flipL, permL, permMat, Matrix.of_apply]
  apply if_congr _ rfl rfl
  have key : ∀ t, (Equiv.swap (e i) (e j)) t = e (Equiv.swap i j (e.symm t)) := fun t => by
    rw [← Equiv.symm_trans_swap_trans i j e]; rfl
  constructor
  · intro h; funext t
    have := congrFun h (e.symm t)
    simp only [Function.comp_apply] at this ⊢
    rw [key, Equiv.symm_apply_apply, this, Equiv.apply_symm_apply]
  · intro h; funext t
    have := congrFun h (e t)
    simp only [Function.comp_apply, key, Equiv.symm_apply_apply] at this ⊢
    exact this

theorem reidx_tB (e : L ≃ L') (S T : Finset L) :
    reidx e * tB ℂ 2 S T = tB ℂ 2 (S.map e.toEmbedding) (T.map e.toEmbedding) * reidx e := by
  simp only [tB, Matrix.mul_sum, Matrix.sum_mul, reidx_flip, Finset.sum_map]
  rfl

theorem reidx_leafOp (e : L ≃ L') (i : L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    reidx e * leafOp i a = leafOp (e i) a * reidx e := by
  ext y x
  rw [reidx_mul_apply, mul_reidx_apply]
  simp only [leafOp, Matrix.of_apply, Function.comp_apply, Equiv.symm_apply_apply]
  congr 1
  apply if_congr _ rfl rfl
  constructor
  · intro h j hj
    have := h (e.symm j) (fun h' => hj (by rw [← h']; simp))
    simpa using this
  · intro h j hj
    have := h (e j) (fun h' => hj (e.injective h'))
    simpa using this

theorem reidx_diag (e : L ≃ L') (a : Matrix (Fin 2) (Fin 2) ℂ) :
    reidx e * diag L a = diag L' a * reidx e := by
  simp only [diag, Matrix.mul_sum, Matrix.sum_mul, reidx_leafOp]
  exact Equiv.sum_comp e (fun i => leafOp i a * reidx e)

end QOU.KZ.Drinfeld
