import QOU.MassTheory.StaircaseMinimisers
import Mathlib.Algebra.Polynomial.Degree.Operations
import Mathlib.Algebra.Polynomial.BigOperators

/-!
# From the staircase minimisers to the leading coefficient of `S(n)`

Second step of the partition count behind `conj:cyclotomic-boundary-at-keystone`
(first step: `QOU.Mass.StaircaseMinimisers`).

* `shapes n` is the finite set of Young diagrams with `n` cells, as lower sets of `ℕ × ℕ`.
* `three_mul_N_stair`: `3 · N(stair (m+1)) = m (m + 1) (m + 2)`, so the minimum of `N` over `shapes (T_m + r)`
  is an explicit cubic in `m` plus `r m`.
* `card_minimisers`: for `1 ≤ r ≤ m + 1`, exactly `C(m+1, r)` diagrams with `T_m + r` cells
  attain the minimum `N(stair m) + r m`.
* `coeff_sum_eq_card_of_top`: for any family of integer polynomials whose member for `λ` has
  degree at most `M - N(λ)` and coefficient `1` there, the coefficient of the sum at degree
  `M - N_min` counts the minimisers.
* `coeff_sum_shapes_of_top` combines the two: the coefficient is `C(m+1, r)`.

The hypothesis of `coeff_sum_shapes_of_top` is the top term of the `q`-hook-length formula:
`q^M dim_q λ` (a polynomial in `q` after clearing denominators) has degree `M - N(λ)` with
leading coefficient `1`. That formula is not proved here, so the result carries it as a
hypothesis (`_of_top`). Not yet formalised: the hook formula itself, the comparison of `S(n)`
with `S(n-1)` and `[n-1] S(n-2)` inside `D(n)`, and the `δ = 1, 2` counts behind `a₁`, `a₂`.
-/

namespace QOU.Mass.StaircaseMinimisers

open Finset Polynomial

/-- Adding antidiagonal `m` to `stair m` adds `(m + 1) m` to `N`. -/
theorem N_stair_succ (m : ℕ) : N (stair (m + 1)) = N (stair m) + (m + 1) * m := by
  have hu : stair m ∪ antidiagonal m = stair (m + 1) := by
    ext c; simp [mem_stair, mem_antidiagonal, val, Nat.lt_succ_iff_lt_or_eq]
  have := N_stair_union (m := m) (R := antidiagonal m) subset_rfl
  rw [hu] at this
  simpa using this

/-- `3 · N(stair (m+1)) = m (m + 1) (m + 2)`, i.e. `N(stair m) = ∑_{t < m} t (t + 1)`. -/
theorem three_mul_N_stair (m : ℕ) : 3 * N (stair (m + 1)) = m * (m + 1) * (m + 2) := by
  induction m with
  | zero => simp [N, stair, val]
  | succ k ih =>
    rw [N_stair_succ, mul_add, ih]
    ring

/-- Young diagrams with `n` cells, as lower sets of `ℕ × ℕ`. Every such set lies in
`range n ×ˢ range n`. -/
noncomputable def shapes (n : ℕ) : Finset (Finset (ℕ × ℕ)) := by
  classical
  exact ((range n ×ˢ range n).powerset).filter
    (fun s => s.card = n ∧ IsLowerSet (s : Set (ℕ × ℕ)))

theorem mem_shapes {n : ℕ} {s : Finset (ℕ × ℕ)} :
    s ∈ shapes n ↔ s ⊆ range n ×ˢ range n ∧ s.card = n ∧ IsLowerSet (s : Set (ℕ × ℕ)) := by
  classical
  simp [shapes]

/-- **The number of minimisers.** For `n = T_m + r` with `1 ≤ r ≤ m + 1`, exactly `C(m+1, r)`
Young diagrams with `n` cells have `N = N(stair m) + r m`, the minimum (`le_N_of_card`). -/
theorem card_minimisers {m r : ℕ} (hr1 : 1 ≤ r) (hr : r ≤ m + 1) :
    ((shapes ((stair m).card + r)).filter (fun s => N s = N (stair m) + r * m)).card =
      (m + 1).choose r := by
  classical
  rw [← card_choices m r]
  have hdisj : ∀ R : Finset (ℕ × ℕ), R ⊆ antidiagonal m → Disjoint (stair m) R := by
    intro R hR
    rw [Finset.disjoint_left]
    intro c hc hcR
    rw [mem_stair, val, mem_antidiagonal.1 (hR hcR)] at hc
    exact lt_irrefl _ hc
  have hm : m < (stair m).card + r := by
    have := two_mul_card_stair m
    nlinarith
  symm
  refine card_nbij' (fun R => stair m ∪ R) (fun s => s \ stair m) ?_ ?_ ?_ ?_
  · intro R hR
    rw [mem_coe, mem_powersetCard] at hR
    rw [mem_coe, mem_filter, mem_shapes]
    refine ⟨⟨?_, ?_, isLowerSet_stair_union hR.1⟩, ?_⟩
    · intro c hc
      have hv : val c ≤ m := by
        rcases mem_union.1 hc with h | h
        · exact (mem_stair.1 h).le
        · exact (mem_antidiagonal.1 (hR.1 h)).le
      simp only [mem_product, mem_range]
      simp only [val] at hv
      omega
    · rw [card_union_of_disjoint (hdisj R hR.1), hR.2]
    · rw [N_stair_union hR.1, hR.2]
  · intro s hs
    rw [mem_coe, mem_filter, mem_shapes] at hs
    obtain ⟨R, hRsub, hRcard, rfl⟩ := (N_eq_iff hr hs.1.2.1).1 hs.2
    simp only [mem_coe, mem_powersetCard, union_sdiff_left, (hdisj R hRsub).sdiff_eq_right]
    exact ⟨hRsub, hRcard⟩
  · intro R hR
    rw [mem_coe, mem_powersetCard] at hR
    simp only [union_sdiff_left, (hdisj R hR.1).sdiff_eq_right]
  · intro s hs
    rw [mem_coe, mem_filter, mem_shapes] at hs
    obtain ⟨R, hRsub, hRcard, rfl⟩ := (N_eq_iff hr hs.1.2.1).1 hs.2
    simp only [union_sdiff_left, (hdisj R hRsub).sdiff_eq_right]

/-- **Leading coefficient of a sum.** Let every `f λ` have degree at most `M - N λ` and
coefficient `1` at that degree, with `N λ ≤ M` and `N_min ≤ N λ` on `I`. Then the coefficient of
`∑ f λ` at degree `M - N_min` is the number of `λ ∈ I` with `N λ = N_min`. -/
theorem coeff_sum_eq_card_of_top {ι : Type*} (I : Finset ι) (Nf : ι → ℕ) (f : ι → ℤ[X])
    (M Nmin : ℕ) (hM : ∀ i ∈ I, Nf i ≤ M) (hmin : ∀ i ∈ I, Nmin ≤ Nf i)
    (hdeg : ∀ i ∈ I, (f i).natDegree ≤ M - Nf i) (htop : ∀ i ∈ I, (f i).coeff (M - Nf i) = 1) :
    (∑ i ∈ I, f i).coeff (M - Nmin) = ((I.filter (fun i => Nf i = Nmin)).card : ℤ) := by
  classical
  rw [finset_sum_coeff, card_eq_sum_ones, Nat.cast_sum, sum_filter]
  refine sum_congr rfl (fun i hi => ?_)
  by_cases h : Nf i = Nmin
  · rw [if_pos h, ← h, htop i hi]; simp
  · rw [if_neg h]
    apply coeff_eq_zero_of_natDegree_lt
    have := hdeg i hi
    have := hM i hi
    have := hmin i hi
    omega

/-- **The leading coefficient is `C(m+1, r)`**, given the top term of each summand (the top
term of the `q`-hook formula; see the module docstring). Here `n = T_m + r`, `1 ≤ r ≤ m + 1`,
and `f λ` stands for `q^M dim_q λ`. -/
theorem coeff_sum_shapes_of_top {m r : ℕ} (hr1 : 1 ≤ r) (hr : r ≤ m + 1)
    (f : Finset (ℕ × ℕ) → ℤ[X]) (M : ℕ)
    (hM : ∀ s ∈ shapes ((stair m).card + r), N s ≤ M)
    (hdeg : ∀ s ∈ shapes ((stair m).card + r), (f s).natDegree ≤ M - N s)
    (htop : ∀ s ∈ shapes ((stair m).card + r), (f s).coeff (M - N s) = 1) :
    (∑ s ∈ shapes ((stair m).card + r), f s).coeff (M - (N (stair m) + r * m)) =
      ((m + 1).choose r : ℤ) := by
  rw [coeff_sum_eq_card_of_top _ N f M _ hM
    (fun s hs => le_N_of_card hr ((mem_shapes.1 hs).2.1)) hdeg htop,
    card_minimisers hr1 hr]

end QOU.Mass.StaircaseMinimisers
