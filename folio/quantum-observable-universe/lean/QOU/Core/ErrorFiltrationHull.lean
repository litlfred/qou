import QOU.Core.ErrorFiltration
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.RingTheory.Ideal.Span

/-!
# QOU.Core.ErrorFiltrationHull — the weight filtration of an antitone tower

An antitone tower of ideals `J 0 ⊇ J 1 ⊇ …` need not be multiplicative, so the
quadratic-remainder calculus of `QOU.Core.ErrorFiltration` does not apply to it
directly. The Habiro tower `J n = ((q;q)_n)` is the case in point: it is antitone but
not multiplicative (`habiro_not_mul`).

The **weight filtration** (`hull`) fixes this. Level `n` is spanned by products
`x₁ ⋯ x_k` with `x_i ∈ J a_i` and `a₁ + ⋯ + a_k ≥ n`. It is

* an error filtration (multiplicative, antitone, `F 0 = ⊤`);
* above the tower: `J n ≤ hull n` (`le_hull`);
* the smallest such: any error filtration above the tower is above the hull
  (`hull_le`).

So `hull J` is the unique coarsest multiplicative error calculus that refines the
tower's notion of order. For Habiro it is strictly coarser than the tower:
`(1 − q)²` has weight 2 but is not in `((q;q)_2)` (`habiro_hull_ne`). Order-`n`
statements in the weight filtration are therefore weaker than order-`n` statements in
the Habiro tower, and must be quoted as weight statements.

No `sorry`, no axiom beyond Lean's three, no empirical value.
-/

namespace QOU.Core.Error

variable {R : Type*} [CommRing R]

/-- Generators of weight at least `n`: products of tower elements whose levels sum
to at least `n`. -/
def hullGen (J : ℕ → Ideal R) (n : ℕ) : Set R :=
  {x | ∃ l : List (ℕ × R), (∀ p ∈ l, p.2 ∈ J p.1) ∧ n ≤ (l.map Prod.fst).sum ∧
    x = (l.map Prod.snd).prod}

theorem hullGen_mul {J : ℕ → Ideal R} {a b : ℕ} {x y : R} (hx : x ∈ hullGen J a)
    (hy : y ∈ hullGen J b) : x * y ∈ hullGen J (a + b) := by
  obtain ⟨l₁, h₁, s₁, rfl⟩ := hx
  obtain ⟨l₂, h₂, s₂, rfl⟩ := hy
  refine ⟨l₁ ++ l₂, ?_, ?_, ?_⟩
  · intro p hp
    rcases List.mem_append.mp hp with hp | hp
    · exact h₁ p hp
    · exact h₂ p hp
  · simp only [List.map_append, List.sum_append]
    omega
  · simp [List.map_append, List.prod_append]

/-- **The weight filtration** of a tower. -/
def hull (J : ℕ → Ideal R) : ErrorFiltration R where
  F n := Ideal.span (hullGen J n)
  anti := by
    intro n m h
    refine Ideal.span_mono ?_
    rintro x ⟨l, hl, hs, rfl⟩
    exact ⟨l, hl, le_trans h hs, rfl⟩
  zero_top := by
    rw [eq_top_iff, ← Ideal.span_singleton_one]
    refine Ideal.span_mono ?_
    rintro _ rfl
    exact ⟨[], by simp, by simp, by simp⟩
  mul_le a b := by
    rw [Ideal.span_mul_span']
    refine Ideal.span_le.mpr ?_
    rintro _ ⟨x, hx, y, hy, rfl⟩
    exact Ideal.subset_span (hullGen_mul hx hy)

/-- The tower sits inside its weight filtration. -/
theorem le_hull (J : ℕ → Ideal R) (n : ℕ) : J n ≤ (hull J).F n := by
  intro x hx
  exact Ideal.subset_span ⟨[(n, x)], by simpa using hx, by simp, by simp⟩

/-- A list of tower elements multiplies into the level of the summed weights. -/
theorem ErrorFiltration.list_prod_mem (E : ErrorFiltration R) :
    ∀ l : List (ℕ × R), (∀ p ∈ l, p.2 ∈ E.F p.1) →
      (l.map Prod.snd).prod ∈ E.F (l.map Prod.fst).sum
  | [], _ => by simp [E.zero_top]
  | p :: l, h => by
    simp only [List.map_cons, List.prod_cons, List.sum_cons]
    exact E.mul_mem (h p (List.mem_cons_self ..))
      (E.list_prod_mem l fun q hq => h q (List.mem_cons_of_mem _ hq))

/-- **Minimality.** Any error filtration above the tower is above the weight
filtration. -/
theorem hull_le (J : ℕ → Ideal R) (E : ErrorFiltration R) (hJ : ∀ n, J n ≤ E.F n)
    (n : ℕ) : (hull J).F n ≤ E.F n := by
  refine Ideal.span_le.mpr ?_
  rintro _ ⟨l, hl, hs, rfl⟩
  exact E.anti hs (E.list_prod_mem l fun p hp => hJ p.1 (hl p hp))

/-! ### The Habiro tower -/

/-- The `q`-Pochhammer symbol `(q;q)_n = ∏_{i<n} (1 − q^{i+1})`. -/
def qPoch (q : R) (n : ℕ) : R := ∏ i ∈ Finset.range n, (1 - q ^ (i + 1))

theorem qPoch_dvd (q : R) {n m : ℕ} (h : n ≤ m) : qPoch q n ∣ qPoch q m :=
  Finset.prod_dvd_prod_of_subset _ _ _ (Finset.range_subset_range.mpr h)

theorem qPoch_one (q : R) : qPoch q 1 = 1 - q := by simp [qPoch]

theorem qPoch_two (q : R) : qPoch q 2 = (1 - q) * (1 - q ^ 2) := by
  simp [qPoch, Finset.prod_range_succ]

/-- The Habiro tower `J n = ((q;q)_n)`. -/
def habiroTower (q : R) (n : ℕ) : Ideal R := Ideal.span {qPoch q n}

theorem habiroTower_anti (q : R) : Antitone (habiroTower q) := fun _ _ h =>
  Ideal.span_singleton_le_span_singleton.mpr (qPoch_dvd q h)

/-- The Habiro weight filtration: the multiplicative hull of the Habiro tower. -/
def habiroWeight (q : R) : ErrorFiltration R := hull (habiroTower q)

open Polynomial

/-- `(1 − q)²` is not divisible by `(q;q)_2 = (1 − q)(1 − q²)` in `ℤ[q]`: evaluate at
`q = −1`. -/
theorem one_sub_sq_not_mem_habiroTower_two :
    (1 - X) * (1 - X) ∉ habiroTower (X : ℤ[X]) 2 := by
  intro h
  obtain ⟨g, hg⟩ := Ideal.mem_span_singleton.mp h
  rw [qPoch_two] at hg
  have := congrArg (eval (-1 : ℤ)) hg
  simp only [eval_mul, eval_sub, eval_one, eval_X, eval_pow] at this
  norm_num at this

/-- **The Habiro tower is not multiplicative.** -/
theorem habiro_not_mul :
    ¬ (habiroTower (X : ℤ[X]) 1 * habiroTower (X : ℤ[X]) 1 ≤ habiroTower (X : ℤ[X]) 2) := by
  intro h
  have h1 : (1 - X : ℤ[X]) ∈ habiroTower (X : ℤ[X]) 1 :=
    Ideal.mem_span_singleton.mpr ⟨1, by rw [qPoch_one, mul_one]⟩
  exact one_sub_sq_not_mem_habiroTower_two (h (Ideal.mul_mem_mul h1 h1))

/-- **The weight filtration is strictly coarser than the Habiro tower.** -/
theorem habiro_hull_ne :
    ((1 - X) * (1 - X) : ℤ[X]) ∈ (habiroWeight (X : ℤ[X])).F 2 ∧
      ((1 - X) * (1 - X) : ℤ[X]) ∉ habiroTower (X : ℤ[X]) 2 := by
  refine ⟨?_, one_sub_sq_not_mem_habiroTower_two⟩
  have h1 : (1 - X : ℤ[X]) ∈ (habiroWeight (X : ℤ[X])).F 1 :=
    le_hull _ 1 (Ideal.mem_span_singleton.mpr ⟨1, by rw [qPoch_one, mul_one]⟩)
  have h2 := (habiroWeight (X : ℤ[X])).mul_mem h1 h1
  rwa [show (1 : ℕ) + 1 = 2 from rfl] at h2

end QOU.Core.Error
