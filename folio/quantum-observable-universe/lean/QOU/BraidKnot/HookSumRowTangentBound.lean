import QOU.BraidKnot.HookSumClosedForm

/-!
# The row-indexed tangent lower bound on the hook sum

For a Young diagram `μ` with `n` cells and `ℓ = μ.colLen 0` rows, the hook sum has the row form

    2 · Σ_{c∈μ} hook(c) = Σ_{i<ℓ} λ_i (λ_i + 2i + 1),        λ_i = μ.rowLen i   (rows 0-indexed),

obtained from `sum_hookZ_eq`, `two_mul_sum_snd` and `sum_fst_eq_bStat` in `HookSumClosedForm`.
Each row summand is a convex function of `λ_i`, so a tangent line of slope `2j + 1` at
`λ_i = j − i` (or at `λ_i = 1` when `j ≤ i`) bounds it from below.  Summing:

    2 Σ_c hook(c)  ≥  ℓ(ℓ+1) + (n − ℓ)(2j + 1) − Σ_{i<ℓ} ((j − (i+1))₊)²          for every j ≥ 0,

`two_mul_sum_hookZ_ge_tangent`.  The correction sum is written with ℕ-truncated subtraction, so
no hypothesis relating `j` to `ℓ` is needed; for `j ≤ ℓ` it equals `Σ_{d<j} d²`
(`sum_trunc_sq_eq_of_le`), and for every `ℓ` it is at most `Σ_{d<j} d²`
(`sum_trunc_sq_le`).

## The bound that settles `REV_n`

Writing `n = T_k + r` with `T_k = k(k+1)/2`, the min-hook shape is the staircase `δ_k` with its
first `r` rows extended by one cell, whose hook sum is `H⁺ = Σ_{i≤k} i² + r(k+1)`.  Taking `j = k`
and the closed form `6 Σ_{d<m} d² = m(m−1)(2m−1)` turns the tangent bound into the polynomial
identity

    2 ( Σ_c hook(c) − H⁺ )  ≥  (ℓ − k)² − r,                                 `two_mul_sum_hookZ_sub_hminClosed_ge`

for **every** diagram with `n` cells and **every** row count `ℓ` — no `k ≤ ℓ` hypothesis.  With
`R_λ ≤ (ℓ−1)·C` (hooks strictly decrease along a row, `HookSumThicknessBound`), this is what makes
the shape free energy `REV_n` of `qou-hok7` grow like `√n` and not `n^{3/4}`: the energy of an
`ℓ`-row shape grows quadratically in `ℓ − √(2n)` while its entropy grows only linearly in `ℓ`.
The archimedean maximisation `max_x (xC − x²L/2) = C²/(2L)` is `quad_max_le`, the one statement
here over `ℝ` (it needs the order).

## What is and is not proved here

* Proved: the row form, the tangent bound for every `j`, its `j = k` specialisation, and the
  quadratic maximum.  All sorry-free.
* Not proved here: that `H⁺` is the *minimum* hook sum over all diagrams with `n` cells (the
  closed form `H_min(n)` of `hmin_closed_form_and_rev_sublinearity_probe.py`).  The inequality
  above is stated against the defined quantity `hminClosed k r`; the probe
  `rev_sqrt_n_upper_bound_probe.py` verifies `H⁺ = H_min(n)` exactly for `n ≤ 30`, and the
  upper-bound argument only needs `H⁺ ≥ H_min(n)`, which is attainment by the shape `λ⁺`.

## Base ring

`ℤ` throughout, matching `HookSumClosedForm`; `ℝ` only in `quad_max_le`.

-- Ref: [leitner2026] computations/deltalambda/rev_sqrt_n_upper_bound_probe.py
-/
namespace QOU.BraidKnot.HookSum

open Finset QOU.BraidKnot.PieceA

/-! ## Rows below `colLen 0` are non-empty -/

/-- Every row index below the first column's length carries at least one cell. -/
theorem one_le_rowLen_of_lt_colLen (μ : YoungDiagram) {i : ℕ} (hi : i < μ.colLen 0) :
    1 ≤ μ.rowLen i := by
  have hmem : (i, 0) ∈ μ := (YoungDiagram.mem_iff_lt_colLen (μ := μ) (i := i) (j := 0)).mpr hi
  have h0 : 0 < μ.rowLen i := (YoungDiagram.mem_iff_lt_rowLen (μ := μ) (i := i) (j := 0)).mp hmem
  omega

/-! ## The row form of the hook sum -/

/-- `2 Σ_c hook(c) = Σ_{i<ℓ} λ_i (λ_i + 2i + 1)`, rows 0-indexed, `ℓ = colLen 0`. -/
theorem two_mul_sum_hookZ_rowform (μ : YoungDiagram) :
    2 * ∑ c ∈ μ.cells, hookZ μ c
      = ∑ i ∈ range (μ.colLen 0), (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) + 2 * (i : ℤ) + 1) := by
  have h0 := sum_hookZ_eq μ
  have h2 := two_mul_sum_snd μ (le_refl (μ.colLen 0))
  have h1 := sum_fst_eq_bStat μ (le_refl (μ.colLen 0))
  have hn := sum_rowLen_eq_card μ (le_refl (μ.colLen 0))
  have hsplit : ∑ i ∈ range (μ.colLen 0), (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) + 2 * (i : ℤ) + 1)
      = ∑ i ∈ range (μ.colLen 0), (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) - 1)
        + 2 * ∑ i ∈ range (μ.colLen 0), (i : ℤ) * (μ.rowLen i : ℤ)
        + 2 * ∑ i ∈ range (μ.colLen 0), (μ.rowLen i : ℤ) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl ?_
    intro i _
    ring
  rw [hsplit]
  linarith

/-! ## The per-row tangent inequality -/

/-- Per row: `L(L + 2i + 1) ≥ (2j+1)(L − 1) + 2(i+1) − ((j − (i+1))₊)²` for `L ≥ 1`.
Case `i + 1 ≤ j`: the difference is `(L + i − j)²`.  Case `i + 1 > j`: it is
`(L − 1)(L + 1 + 2(i − j))`, a product of non-negatives. -/
theorem row_tangent (L : ℤ) (hL : 1 ≤ L) (i j : ℕ) :
    (2 * (j : ℤ) + 1) * (L - 1) + 2 * ((i : ℤ) + 1) - ((j - (i + 1) : ℕ) : ℤ) ^ 2
      ≤ L * (L + 2 * (i : ℤ) + 1) := by
  rcases le_or_gt (i + 1) j with h | h
  · have hc : ((j - (i + 1) : ℕ) : ℤ) = (j : ℤ) - ((i : ℤ) + 1) := by
      rw [Nat.cast_sub h]
      push_cast
      ring
    rw [hc]
    nlinarith [sq_nonneg (L + (i : ℤ) - (j : ℤ))]
  · have hz : j - (i + 1) = 0 := Nat.sub_eq_zero_of_le h.le
    have hc : ((j - (i + 1) : ℕ) : ℤ) = 0 := by rw [hz]; simp
    rw [hc]
    have hij : (j : ℤ) ≤ (i : ℤ) := by exact_mod_cast Nat.lt_succ_iff.mp h
    have hL0 : (0 : ℤ) ≤ L - 1 := by linarith
    have hsec : (0 : ℤ) ≤ L + 1 + 2 * ((i : ℤ) - (j : ℤ)) := by linarith
    nlinarith [mul_nonneg hL0 hsec]

/-! ## Gauss and the sum of squares, cast to `ℤ` -/

/-- `2 Σ_{i<ℓ} (i+1) = ℓ(ℓ+1)`. -/
theorem two_mul_sum_range_succ_cast (ℓ : ℕ) :
    2 * ∑ i ∈ range ℓ, ((i : ℤ) + 1) = (ℓ : ℤ) * ((ℓ : ℤ) + 1) := by
  induction ℓ with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ]
    push_cast
    push_cast at ih
    linarith

/-- `6 Σ_{d<m} d² = m(m−1)(2m−1)`. -/
theorem six_mul_sum_range_sq (m : ℕ) :
    6 * ∑ d ∈ range m, (d : ℤ) ^ 2 = (m : ℤ) * ((m : ℤ) - 1) * (2 * (m : ℤ) - 1) := by
  induction m with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ]
    push_cast
    push_cast at ih
    linear_combination ih

/-! ## The truncated correction sum -/

/-- The correction sum over exactly `j` rows is `Σ_{d<j} d²` (reflect `i ↦ j − 1 − i`). -/
theorem sum_trunc_sq_range_self (j : ℕ) :
    ∑ i ∈ range j, ((j - (i + 1) : ℕ) : ℤ) ^ 2 = ∑ d ∈ range j, (d : ℤ) ^ 2 := by
  have h := Finset.sum_range_reflect (fun d : ℕ => ((d : ℕ) : ℤ) ^ 2) j
  simp only at h
  rw [← h]
  refine Finset.sum_congr rfl ?_
  intro i _
  have : j - (i + 1) = j - 1 - i := by omega
  rw [this]

/-- Beyond row `j` every correction term vanishes. -/
theorem sum_trunc_sq_Ico_eq_zero (j ℓ : ℕ) :
    ∑ i ∈ Ico j ℓ, ((j - (i + 1) : ℕ) : ℤ) ^ 2 = 0 := by
  refine Finset.sum_eq_zero ?_
  intro i hi
  have hji : j ≤ i := (Finset.mem_Ico.mp hi).1
  have : j - (i + 1) = 0 := by omega
  rw [this]
  simp

/-- For `j ≤ ℓ` the correction sum is exactly `Σ_{d<j} d²`. -/
theorem sum_trunc_sq_eq_of_le {j ℓ : ℕ} (hj : j ≤ ℓ) :
    ∑ i ∈ range ℓ, ((j - (i + 1) : ℕ) : ℤ) ^ 2 = ∑ d ∈ range j, (d : ℤ) ^ 2 := by
  rw [← Finset.sum_range_add_sum_Ico _ hj, sum_trunc_sq_Ico_eq_zero, add_zero,
    sum_trunc_sq_range_self]

/-- For every `ℓ` the correction sum is at most `Σ_{d<j} d²`. -/
theorem sum_trunc_sq_le (j ℓ : ℕ) :
    ∑ i ∈ range ℓ, ((j - (i + 1) : ℕ) : ℤ) ^ 2 ≤ ∑ d ∈ range j, (d : ℤ) ^ 2 := by
  have hsub : range ℓ ⊆ range (max ℓ j) := Finset.range_mono (le_max_left ℓ j)
  have hle : ∑ i ∈ range ℓ, ((j - (i + 1) : ℕ) : ℤ) ^ 2
      ≤ ∑ i ∈ range (max ℓ j), ((j - (i + 1) : ℕ) : ℤ) ^ 2 :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => sq_nonneg _)
  rw [sum_trunc_sq_eq_of_le (le_max_right ℓ j)] at hle
  exact hle

/-! ## The tangent bound -/

/-- **Row-indexed tangent lower bound.** For every `j ≥ 0`,

    2 Σ_c hook(c) ≥ ℓ(ℓ+1) + (n − ℓ)(2j+1) − Σ_{i<ℓ} ((j − (i+1))₊)²,

with `ℓ = colLen 0` and `n = |μ|`.  Equality holds on the shapes `δ_j + 1^{ℓ−j}`. -/
theorem two_mul_sum_hookZ_ge_tangent (μ : YoungDiagram) (j : ℕ) :
    (μ.colLen 0 : ℤ) * ((μ.colLen 0 : ℤ) + 1)
        + ((μ.cells.card : ℤ) - (μ.colLen 0 : ℤ)) * (2 * (j : ℤ) + 1)
        - ∑ i ∈ range (μ.colLen 0), ((j - (i + 1) : ℕ) : ℤ) ^ 2
      ≤ 2 * ∑ c ∈ μ.cells, hookZ μ c := by
  rw [two_mul_sum_hookZ_rowform μ]
  have hn := sum_rowLen_eq_card μ (le_refl (μ.colLen 0))
  have hg := two_mul_sum_range_succ_cast (μ.colLen 0)
  have hrow : ∀ i ∈ range (μ.colLen 0),
      (2 * (j : ℤ) + 1) * ((μ.rowLen i : ℤ) - 1) + 2 * ((i : ℤ) + 1)
          - ((j - (i + 1) : ℕ) : ℤ) ^ 2
        ≤ (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) + 2 * (i : ℤ) + 1) := by
    intro i hi
    have h1 : 1 ≤ μ.rowLen i := one_le_rowLen_of_lt_colLen μ (Finset.mem_range.mp hi)
    exact row_tangent (μ.rowLen i) (by exact_mod_cast h1) i j
  have hsum := Finset.sum_le_sum hrow
  have hexp : ∑ i ∈ range (μ.colLen 0),
      ((2 * (j : ℤ) + 1) * ((μ.rowLen i : ℤ) - 1) + 2 * ((i : ℤ) + 1)
          - ((j - (i + 1) : ℕ) : ℤ) ^ 2)
      = (2 * (j : ℤ) + 1) * ((∑ i ∈ range (μ.colLen 0), (μ.rowLen i : ℤ)) - (μ.colLen 0 : ℤ))
        + 2 * ∑ i ∈ range (μ.colLen 0), ((i : ℤ) + 1)
        - ∑ i ∈ range (μ.colLen 0), ((j - (i + 1) : ℕ) : ℤ) ^ 2 := by
    rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
      Finset.sum_sub_distrib]
    simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one]
  rw [hexp, hn] at hsum
  linarith

/-! ## Specialisation to the min-hook shape -/

/-- The hook sum of the min-hook shape at `n = T_k + r`: `Σ_{i≤k} i² + r(k+1)`.  This is the
closed form `H_min(n)` of `hmin_closed_form_and_rev_sublinearity_probe.py`; that it is the
minimum over all shapes is verified there and in `rev_sqrt_n_upper_bound_probe.py`, not here. -/
def hminClosed (k r : ℕ) : ℤ :=
  (∑ d ∈ range (k + 1), (d : ℤ) ^ 2) + (r : ℤ) * ((k : ℤ) + 1)

/-- **The energy of an `ℓ`-row shape is quadratic in `ℓ − k`.** If `2n = k(k+1) + 2r` then for every
diagram with `n` cells and `ℓ` rows,

    2 (Σ_c hook(c) − hminClosed k r) ≥ (ℓ − k)² − r.

No hypothesis on `ℓ` versus `k`.  This is the inequality behind `REV_n = O(√n)`. -/
theorem two_mul_sum_hookZ_sub_hminClosed_ge (μ : YoungDiagram) (k r : ℕ)
    (hn : 2 * μ.cells.card = k * (k + 1) + 2 * r) :
    ((μ.colLen 0 : ℤ) - (k : ℤ)) ^ 2 - (r : ℤ)
      ≤ 2 * ∑ c ∈ μ.cells, hookZ μ c - 2 * hminClosed k r := by
  have h4 := two_mul_sum_hookZ_ge_tangent μ k
  have hcorr := sum_trunc_sq_le k (μ.colLen 0)
  have e1 := six_mul_sum_range_sq k
  have e2 := six_mul_sum_range_sq (k + 1)
  have hn' : (2 : ℤ) * (μ.cells.card : ℤ) = (k : ℤ) * ((k : ℤ) + 1) + 2 * (r : ℤ) := by
    exact_mod_cast hn
  push_cast at e2
  unfold hminClosed
  nlinarith [h4, hcorr, e1, e2, hn']

/-- The same bound with the positive part made explicit: for `ℓ ≥ k`,
`2 (Σ hook − hminClosed k r) ≥ (ℓ − k)² − r` with `ℓ − k` a natural number. -/
theorem two_mul_sum_hookZ_sub_hminClosed_ge_of_le (μ : YoungDiagram) (k r : ℕ)
    (hn : 2 * μ.cells.card = k * (k + 1) + 2 * r) (hk : k ≤ μ.colLen 0) :
    ((μ.colLen 0 - k : ℕ) : ℤ) ^ 2 - (r : ℤ)
      ≤ 2 * ∑ c ∈ μ.cells, hookZ μ c - 2 * hminClosed k r := by
  have h := two_mul_sum_hookZ_sub_hminClosed_ge μ k r hn
  rw [Nat.cast_sub hk]
  exact h

/-! ## The archimedean maximisation -/

/-- `x C − x² L / 2 ≤ C² / (2L)` for `L > 0`: the quadratic in the number of rows above the
staircase is maximised at `x = C / L`.  Over `ℝ` because it needs the order. -/
theorem quad_max_le (C L x : ℝ) (hL : 0 < L) :
    x * C - x ^ 2 * L / 2 ≤ C ^ 2 / (2 * L) := by
  rw [le_div_iff₀ (by positivity)]
  nlinarith [sq_nonneg (C - x * L), hL]


/-- **Polynomial closed form for `6 · hminClosed k r` (`qou-0ie7`).** -/
theorem six_mul_hminClosed (k r : ℕ) :
    6 * hminClosed k r =
      (k : ℤ) * ((k : ℤ) + 1) * (2 * (k : ℤ) + 1) + 6 * (r : ℤ) * ((k : ℤ) + 1) := by
  have e2 := six_mul_sum_range_sq (k + 1)
  push_cast at e2
  have hpoly : ((k : ℤ) + 1) * ((k : ℤ) + 1 - 1) * (2 * ((k : ℤ) + 1) - 1) =
      (k : ℤ) * ((k : ℤ) + 1) * (2 * (k : ℤ) + 1) := by ring
  unfold hminClosed
  linarith [e2, hpoly]

/-- **Staircase boundary continuity of `hminClosed` (`qou-0ie7`).**
Completing row `r = k + 1` above `T_k` matches the base of the next staircase `T_{k+1}`:
`hminClosed k (k + 1) = hminClosed (k + 1) 0`. -/
theorem hminClosed_step_continuity (k : ℕ) :
    hminClosed k (k + 1) = hminClosed (k + 1) 0 := by
  unfold hminClosed
  rw [Finset.sum_range_succ (fun d : ℕ => (d : ℤ) ^ 2) (k + 1)]
  push_cast
  ring

end QOU.BraidKnot.HookSum
