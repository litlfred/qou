import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Pi
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Tactic.Ring

/-!
# Kronecker products of tensor-power matrices on `Sum`-indexed legs

Infrastructure for the Drinfeld category `D_ℏ` (bean `qou-zoyv`, stage S2). A tensor power of
`V = ℂ²` with leg set `L` is indexed by `L → Fin 2`. For leg sets `L, L'` the legs of the tensor
product are `L ⊕ L'`, and the Kronecker product of matrices is
`kron f g y x = f (y ∘ inl) (x ∘ inl) · g (y ∘ inr) (x ∘ inr)`.

* `kron_mul`: `kron f g * kron f' g' = kron (f * f') (g * g')`.
* `kron_one`: `kron 1 1 = 1`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

namespace QOU.KZ.Drinfeld

open Finset

variable {K : Type*} [CommRing K]

/-- The Kronecker product on `Sum`-indexed legs. -/
def kron {α β α' β' : Type*} (f : Matrix (α → Fin 2) (β → Fin 2) K)
    (g : Matrix (α' → Fin 2) (β' → Fin 2) K) :
    Matrix (α ⊕ α' → Fin 2) (β ⊕ β' → Fin 2) K :=
  Matrix.of fun y x => f (y ∘ Sum.inl) (x ∘ Sum.inl) * g (y ∘ Sum.inr) (x ∘ Sum.inr)

theorem kron_apply {α β α' β' : Type*} (f : Matrix (α → Fin 2) (β → Fin 2) K)
    (g : Matrix (α' → Fin 2) (β' → Fin 2) K) (y x) :
    kron f g y x = f (y ∘ Sum.inl) (x ∘ Sum.inl) * g (y ∘ Sum.inr) (x ∘ Sum.inr) := rfl

/-- Sums over `L ⊕ L' → Fin 2` split as double sums. -/
theorem sum_sumArrow {L L' : Type*} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']
    {M : Type*} [AddCommMonoid M] (F : (L ⊕ L' → Fin 2) → M) :
    ∑ z, F z = ∑ u : L → Fin 2, ∑ v : L' → Fin 2, F (Sum.elim u v) := by
  rw [← (Equiv.sumArrowEquivProdArrow L L' (Fin 2)).symm.sum_comp, Fintype.sum_prod_type]
  rfl

theorem kron_mul {α β γ α' β' γ' : Type*} [Fintype β] [DecidableEq β] [Fintype β']
    [DecidableEq β'] (f : Matrix (α → Fin 2) (β → Fin 2) K) (g : Matrix (α' → Fin 2) (β' → Fin 2) K)
    (f' : Matrix (β → Fin 2) (γ → Fin 2) K) (g' : Matrix (β' → Fin 2) (γ' → Fin 2) K) :
    kron f g * kron f' g' = kron (f * f') (g * g') := by
  ext y x
  simp only [Matrix.mul_apply, kron_apply]
  rw [sum_sumArrow, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun v _ => ?_
  simp only [Sum.elim_comp_inl, Sum.elim_comp_inr]
  ring

theorem kron_one {α α' : Type*} [Fintype α] [DecidableEq α] [Fintype α'] [DecidableEq α'] :
    kron (1 : Matrix (α → Fin 2) (α → Fin 2) K) (1 : Matrix (α' → Fin 2) (α' → Fin 2) K) = 1 := by
  ext y x
  simp only [kron_apply, Matrix.one_apply]
  by_cases h : y = x
  · subst h; simp
  · rw [if_neg h]
    have : ¬ (y ∘ Sum.inl = x ∘ Sum.inl ∧ y ∘ Sum.inr = x ∘ Sum.inr) := fun ⟨h1, h2⟩ =>
      h (funext fun i => by
        rcases i with i | i
        · exact congrFun h1 i
        · exact congrFun h2 i)
    by_cases h1 : y ∘ Sum.inl = x ∘ Sum.inl
    · rw [if_pos h1, if_neg fun h2 => this ⟨h1, h2⟩, mul_zero]
    · rw [if_neg h1, zero_mul]

end QOU.KZ.Drinfeld
