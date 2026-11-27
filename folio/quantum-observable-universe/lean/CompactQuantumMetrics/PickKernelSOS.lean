import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.BigOperators.Fin

/-!
# Weighted sums of squares and the Pick kernel `1/(1 - x y)`, algebraically

Over a linearly ordered field, a kernel `K : ι → ι → 𝕜` is a *weighted sum of squares on
`s`* (`IsWSOS s K`) when `K i j = ∑ₜ wₜ gₜ(i) gₜ(j)` on `s × s` with finitely many
`wₜ ≥ 0`. Such a kernel gives a nonnegative quadratic form (`IsWSOS.quadForm_nonneg`), and
the class is closed under sums, Hadamard products and rank-one rescaling.

The main result is `isWSOS_pick`: for points with `|xᵢ| < 1`, the Pick kernel
`1/(1 - xᵢ xⱼ)` is a weighted sum of squares on every finite set. The proof is one
identity, used once per point (no series, no limits):

  `1/(1-xy) = (1-a²) · 1/(1-xa) · 1/(1-ya) + φ(x) φ(y) /(1-xy)`,
  `φ(x) = (x - a)/(1 - x a)`,

and `φ(a) = 0`, so the point `a` drops out of the remainder.
-/

namespace QOU.AlgebraicSubstrate.PickSOS

open Finset

variable {𝕜 : Type*} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] {ι : Type*}

/-- `K` is a weighted sum of squares on `s`. -/
def IsWSOS (s : Finset ι) (K : ι → ι → 𝕜) : Prop :=
  ∃ (n : ℕ) (w : Fin n → 𝕜) (g : Fin n → ι → 𝕜), (∀ t, 0 ≤ w t) ∧
    ∀ i ∈ s, ∀ j ∈ s, K i j = ∑ t, w t * (g t i * g t j)

namespace IsWSOS

variable {s : Finset ι} {K L : ι → ι → 𝕜} {n : ℕ} {w : Fin n → 𝕜} {g : Fin n → ι → 𝕜}

omit [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] in
theorem quadForm_eq (h : ∀ i ∈ s, ∀ j ∈ s, K i j = ∑ t, w t * (g t i * g t j)) (c : ι → 𝕜) :
    ∑ i ∈ s, ∑ j ∈ s, c i * c j * K i j = ∑ t, w t * (∑ i ∈ s, c i * g t i) ^ 2 := by
  have e : ∀ t, w t * (∑ i ∈ s, c i * g t i) ^ 2 =
      ∑ i ∈ s, ∑ j ∈ s, w t * ((c i * g t i) * (c j * g t j)) := by
    intro t
    rw [sq, sum_mul_sum, mul_sum]
    exact sum_congr rfl fun i _ => by rw [mul_sum]
  calc ∑ i ∈ s, ∑ j ∈ s, c i * c j * K i j
      = ∑ i ∈ s, ∑ j ∈ s, ∑ t, w t * ((c i * g t i) * (c j * g t j)) := by
        refine sum_congr rfl fun i hi => sum_congr rfl fun j hj => ?_
        rw [h i hi j hj, mul_sum]
        exact sum_congr rfl fun t _ => by ring
    _ = ∑ i ∈ s, ∑ t, ∑ j ∈ s, w t * ((c i * g t i) * (c j * g t j)) :=
        sum_congr rfl fun i _ => sum_comm
    _ = ∑ t, ∑ i ∈ s, ∑ j ∈ s, w t * ((c i * g t i) * (c j * g t j)) := sum_comm
    _ = ∑ t, w t * (∑ i ∈ s, c i * g t i) ^ 2 := sum_congr rfl fun t _ => (e t).symm

theorem quadForm_nonneg (h : IsWSOS s K) (c : ι → 𝕜) :
    0 ≤ ∑ i ∈ s, ∑ j ∈ s, c i * c j * K i j := by
  obtain ⟨n, w, g, hw, hK⟩ := h
  rw [quadForm_eq hK]
  exact sum_nonneg fun t _ => mul_nonneg (hw t) (sq_nonneg _)

omit [IsStrictOrderedRing 𝕜] in
theorem mono {s' : Finset ι} (h : IsWSOS s K) (hs : s' ⊆ s) : IsWSOS s' K := by
  obtain ⟨n, w, g, hw, hK⟩ := h
  exact ⟨n, w, g, hw, fun i hi j hj => hK i (hs hi) j (hs hj)⟩

omit [IsStrictOrderedRing 𝕜] in
theorem congr_on (h : IsWSOS s K) (hKL : ∀ i ∈ s, ∀ j ∈ s, K i j = L i j) : IsWSOS s L := by
  obtain ⟨n, w, g, hw, hK⟩ := h
  exact ⟨n, w, g, hw, fun i hi j hj => (hKL i hi j hj).symm.trans (hK i hi j hj)⟩

omit [IsStrictOrderedRing 𝕜] in
/-- Rank-one rescaling `vᵢ vⱼ K i j`. -/
theorem outer (h : IsWSOS s K) (v : ι → 𝕜) : IsWSOS s fun i j => v i * v j * K i j := by
  obtain ⟨n, w, g, hw, hK⟩ := h
  refine ⟨n, w, fun t i => v i * g t i, hw, fun i hi j hj => ?_⟩
  dsimp only
  rw [hK i hi j hj, mul_sum]
  exact sum_congr rfl fun t _ => by ring

/-- Nonnegative constant multiples. -/
theorem const_mul (h : IsWSOS s K) {a : 𝕜} (ha : 0 ≤ a) : IsWSOS s fun i j => a * K i j := by
  obtain ⟨n, w, g, hw, hK⟩ := h
  refine ⟨n, fun t => a * w t, g, fun t => mul_nonneg ha (hw t), fun i hi j hj => ?_⟩
  dsimp only
  rw [hK i hi j hj, mul_sum]
  exact sum_congr rfl fun t _ => by ring

/-- Hadamard (Schur) products of weighted sums of squares. -/
theorem mul (hK : IsWSOS s K) (hL : IsWSOS s L) : IsWSOS s fun i j => K i j * L i j := by
  obtain ⟨n, w, g, hw, hK⟩ := hK
  obtain ⟨m, v, f, hv, hL⟩ := hL
  refine ⟨n * m, fun t => w (finProdFinEquiv.symm t).1 * v (finProdFinEquiv.symm t).2,
    fun t i => g (finProdFinEquiv.symm t).1 i * f (finProdFinEquiv.symm t).2 i,
    fun t => mul_nonneg (hw _) (hv _), fun i hi j hj => ?_⟩
  dsimp only
  rw [hK i hi j hj, hL i hi j hj, sum_mul_sum, ← Fintype.sum_prod_type',
    ← finProdFinEquiv.symm.sum_comp]
  refine Fintype.sum_congr _ _ fun t => ?_
  ring

theorem one : IsWSOS s fun (_ _ : ι) => (1 : 𝕜) :=
  ⟨1, fun _ => 1, fun _ _ => 1, fun _ => zero_le_one, fun _ _ _ _ => by simp⟩

/-- Finite products of weighted sums of squares. -/
theorem prod {κ : Type*} (u : Finset κ) {F : κ → ι → ι → 𝕜} (hF : ∀ m ∈ u, IsWSOS s (F m)) :
    IsWSOS s fun i j => ∏ m ∈ u, F m i j := by
  classical
  induction u using Finset.induction_on with
  | empty => simpa using (one (s := s) (𝕜 := 𝕜))
  | insert a u ha ih =>
    have h1 := hF a (mem_insert_self a u)
    have h2 := ih fun m hm => hF m (mem_insert_of_mem hm)
    exact (h1.mul h2).congr_on fun i _ j _ => by rw [prod_insert ha]

end IsWSOS

theorem mul_lt_one_of_abs {x y : 𝕜} (hx : |x| < 1) (hy : |y| < 1) : x * y < 1 := by
  have : |x * y| < 1 := by
    rw [abs_mul]
    exact mul_lt_one_of_nonneg_of_lt_one_left (abs_nonneg x) hx hy.le
  exact lt_of_le_of_lt (le_abs_self _) this

/-- The Pick kernel `1/(1 - xᵢ xⱼ)` is a weighted sum of squares on every finite set of
points in `(-1, 1)`. -/
theorem isWSOS_pick (x : ι → 𝕜) (s : Finset ι) (hx : ∀ i ∈ s, |x i| < 1) :
    IsWSOS s fun i j => 1 / (1 - x i * x j) := by
  classical
  induction s using Finset.induction_on with
  | empty => exact ⟨0, Fin.elim0, Fin.elim0, fun t => t.elim0, fun i hi => by simp at hi⟩
  | insert a s ha ih =>
    obtain ⟨n, w, g, hw, hK⟩ := ih fun i hi => hx i (mem_insert_of_mem hi)
    have hxa := hx a (mem_insert_self a s)
    let φ : ι → 𝕜 := fun i => (x i - x a) / (1 - x i * x a)
    refine ⟨n + 1, Fin.cons (1 - x a ^ 2) w,
      Fin.cons (fun i => 1 / (1 - x i * x a)) fun t i => φ i * g t i,
      fun t => Fin.cases (by have := mul_lt_one_of_abs hxa hxa; simp only [Fin.cons_zero]; nlinarith) (fun t => hw t) t,
      fun i hi j hj => ?_⟩
    rw [Fin.sum_univ_succ]
    simp only [Fin.cons_zero, Fin.cons_succ]
    have hia : 1 - x i * x a ≠ 0 := (sub_pos.2 (mul_lt_one_of_abs (hx i hi) hxa)).ne'
    have hja : 1 - x j * x a ≠ 0 := (sub_pos.2 (mul_lt_one_of_abs (hx j hj) hxa)).ne'
    have hij : 1 - x i * x j ≠ 0 := (sub_pos.2 (mul_lt_one_of_abs (hx i hi) (hx j hj))).ne'
    have key : 1 / (1 - x i * x j) = (1 - x a ^ 2) * (1 / (1 - x i * x a) * (1 / (1 - x j * x a)))
        + φ i * φ j * (1 / (1 - x i * x j)) := by
      simp only [φ]
      field_simp
      ring
    have rest : φ i * φ j * (1 / (1 - x i * x j)) = ∑ t, w t * (φ i * g t i * (φ j * g t j)) := by
      by_cases hi' : i = a
      · subst hi'; simp [φ]
      by_cases hj' : j = a
      · subst hj'; simp [φ]
      have := hK i ((mem_insert.1 hi).resolve_left hi') j ((mem_insert.1 hj).resolve_left hj')
      simp only at this
      rw [this, mul_sum]
      exact sum_congr rfl fun t _ => by ring
    rw [key, rest]

end QOU.AlgebraicSubstrate.PickSOS
