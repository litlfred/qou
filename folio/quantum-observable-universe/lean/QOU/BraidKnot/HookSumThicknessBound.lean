import QOU.BraidKnot.HookSumClosedForm

/-!
# Thickness costs hook length: `H(μ) ≥ r(μ)²`

For a Young diagram `μ` write `r(μ) := min (μ.rowLen 0) (μ.colLen 0)` — the smaller of its
first-row length and its first-column length, a crude "thickness". This module proves

    r(μ)^2  ≤  Σ_{c ∈ μ.cells} hookZ μ c                                      (`sq_min_le_sum_hookZ`)

together with the per-row strict decrease of hook lengths

    hookZ μ (i, j+1) + 1  ≤  hookZ μ (i, j)                                   (`hookZ_succ_lt`)

which is the reason each row can hold at most one cell of any given hook length.

## Why these two

They are the combinatorial content behind an analytic bound on the deuteron-wall quantity `REV`
(bean `qou-hok7`). There `R_λ ≤ C · r(λ)` follows from the per-row decrease, and the upper bound
`REV = O(n^{3/4})` needs a converse coupling `r` back to the hook sum — exactly `sq_min_le_sum_hookZ`.
The Python side (`computations/deltalambda/rev_sublinearity_closed_probe.py`) verifies both
exhaustively for `n ≤ 26`; this module proves them for every diagram.

## The proof is one line of the closed form, and it replaces a WRONG argument

`HookSumClosedForm.two_mul_sum_hookZ_eq_sum_sq` gives `2H = Σ_i (rowLen i)² + Σ_j (colLen j)²`.
Every summand is a square, hence non-negative, so each sum dominates its own `0`-th term:

    2H  ≥  (rowLen 0)² + (colLen 0)²  ≥  2 · min(rowLen 0, colLen 0)² .

That is the whole argument. It is recorded here because the *first* attempt at this bound, in
`computations/deltalambda/rev_sublinearity_proof_probe.py`, claimed the stronger
`H ≥ 3r² - 3r + 1` from `h(1,j) ≥ 2r - j` — a step that silently assumes column `j` has `≥ r` cells
for every `j ≤ r`, when only column `1` does. It is false, with 1168 counterexamples at `n ≤ 22`;
the sharpest is the hook shape `(11, 1^10)`, where `r = 11` and `H = 131` against a claimed `331`.
The bound proved here assumes nothing about columns `2..r`, and is *stronger* than the `r² - r + 1`
that a repaired row-plus-column count gives.

## Sharpness

`sq_min_le_sum_hookZ` is attained exactly at `μ = (1)`: there `r = 1` and `H = 1`. For every larger
diagram it is strict (checked exhaustively to `n = 26` on the Python side; not proved here, and not
needed — only the inequality is used downstream).

## Base ring

`ℤ` throughout, matching `PieceAGeneral` and `HookSumClosedForm`: no `ℝ`, no ordering on a
substrate parameter, no archimedean input. Per AGENTS.md §7c this is a purely combinatorial
statement and must not be stated over `ℝ`.

-- Ref: [leitner2026] computations/deltalambda/rev_sublinearity_closed_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset YoungDiagram QOU.BraidKnot.PieceA

/-- Hook lengths strictly decrease along a row: moving one cell to the right drops the arm by
exactly one and cannot raise the leg, since `colLen` is antitone. Consequently a row contains at
most one cell of any given hook length — the combinatorial fact behind `N_m(λ) ≤ ℓ(λ)`. -/
theorem hookZ_succ_lt (μ : YoungDiagram) (i j : ℕ) :
    hookZ μ (i, j + 1) + 1 ≤ hookZ μ (i, j) := by
  have hcol : (μ.colLen (j + 1) : ℤ) ≤ (μ.colLen j : ℤ) := by
    exact_mod_cast μ.colLen_anti j (j + 1) (Nat.le_succ j)
  simp only [hookZ, armZ, legZ]
  push_cast
  linarith

/-- Hook lengths are strictly decreasing along a row: `j < j'` gives `h(i,j') < h(i,j)`.
Induction on the one-step lemma. -/
theorem hookZ_strictAnti_row (μ : YoungDiagram) (i : ℕ) :
    ∀ {j j' : ℕ}, j < j' → hookZ μ (i, j') < hookZ μ (i, j) := by
  intro j j' hjj'
  induction j' with
  | zero => exact absurd hjj' (Nat.not_lt_zero j)
  | succ m ih =>
    rcases Nat.lt_succ_iff_lt_or_eq.mp hjj' with hlt | heq
    · exact lt_of_lt_of_le (by linarith [hookZ_succ_lt μ i m]) (le_of_lt (ih hlt))
    · subst heq; linarith [hookZ_succ_lt μ i j]

/-- **L1.** A row contains at most one cell of any given hook length. This is what bounds the
hook-length multiplicity `N_m(λ)` by the number of rows, and (via the conjugate statement) by the
number of columns — the input to `R_λ ≤ C · r(λ)` in the REV bound. -/
theorem card_row_filter_hookZ_le_one (μ : YoungDiagram) (i : ℕ) (m : ℤ) :
    ((μ.row i).filter (fun c => hookZ μ c = m)).card ≤ 1 := by
  rw [Finset.card_le_one]
  intro a ha b hb
  simp only [Finset.mem_filter, YoungDiagram.mem_row_iff] at ha hb
  obtain ⟨⟨-, ha1⟩, ha2⟩ := ha
  obtain ⟨⟨-, hb1⟩, hb2⟩ := hb
  -- both cells sit in row `i`, so they differ only in the column
  have hab : a = (i, a.2) := by rw [← ha1]
  have hbb : b = (i, b.2) := by rw [← hb1]
  rcases lt_trichotomy a.2 b.2 with h | h | h
  · exfalso
    have := hookZ_strictAnti_row μ i h
    rw [← hab, ← hbb] at this
    omega
  · rw [hab, hbb, h]
  · exfalso
    have := hookZ_strictAnti_row μ i h
    rw [← hab, ← hbb] at this
    omega

/-- Non-vacuity witness for `card_row_filter_hookZ_le_one`: rows are not empty, so that bound is a
real injectivity statement rather than a card-of-nothing triviality. The staircase `(3,2,1)` has
three cells in row 0. -/
example : (YoungDiagram.ofRowLens [3, 2, 1] (by decide)).rowLen 0 = 3 := by
  simpa using YoungDiagram.rowLen_ofRowLens (w := [3, 2, 1]) (hw := by decide) ⟨0, by norm_num⟩

/-- The first row length is dominated by the sum of squared row lengths. -/
private theorem sq_rowLen_zero_le (μ : YoungDiagram) {N : ℕ} (hN0 : 0 < N) :
    (μ.rowLen 0 : ℤ) ^ 2 ≤ ∑ i ∈ range N, (μ.rowLen i : ℤ) ^ 2 :=
  Finset.single_le_sum (f := fun i => (μ.rowLen i : ℤ) ^ 2)
    (fun i _ => sq_nonneg _) (mem_range.mpr hN0)

/-- The first column length is dominated by the sum of squared column lengths. -/
private theorem sq_colLen_zero_le (μ : YoungDiagram) {M : ℕ} (hM0 : 0 < M) :
    (μ.colLen 0 : ℤ) ^ 2 ≤ ∑ j ∈ range M, (μ.colLen j : ℤ) ^ 2 :=
  Finset.single_le_sum (f := fun j => (μ.colLen j : ℤ) ^ 2)
    (fun j _ => sq_nonneg _) (mem_range.mpr hM0)

/-- **Thickness costs hook length.** With `r = min (rowLen 0) (colLen 0)`,

    r^2 ≤ Σ_{c ∈ μ.cells} hookZ μ c .

Proved from `two_mul_sum_hookZ_eq_sum_sq` by keeping only the `0`-th term of each square sum. -/
theorem sq_min_le_sum_hookZ (μ : YoungDiagram) {N M : ℕ}
    (hN : μ.colLen 0 ≤ N) (hM : μ.rowLen 0 ≤ M) (hN0 : 0 < N) (hM0 : 0 < M) :
    (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ^ 2 ≤ ∑ c ∈ μ.cells, hookZ μ c := by
  have hid := two_mul_sum_hookZ_eq_sum_sq μ hN hM
  have hrow := sq_rowLen_zero_le μ (N := N) hN0
  have hcol := sq_colLen_zero_le μ (M := M) hM0
  -- min ≤ each, and both are non-negative, so min² ≤ each square
  have hmr : (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ≤ (μ.rowLen 0 : ℤ) := by
    exact_mod_cast Nat.min_le_left _ _
  have hmc : (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ≤ (μ.colLen 0 : ℤ) := by
    exact_mod_cast Nat.min_le_right _ _
  have hm0 : (0 : ℤ) ≤ (min (μ.rowLen 0) (μ.colLen 0) : ℤ) :=
    le_min (Int.natCast_nonneg _) (Int.natCast_nonneg _)
  have hsr : (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ^ 2 ≤ (μ.rowLen 0 : ℤ) ^ 2 := by
    nlinarith [hmr, hm0]
  have hsc : (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ^ 2 ≤ (μ.colLen 0 : ℤ) ^ 2 := by
    nlinarith [hmc, hm0]
  linarith

/-- The same bound with the index bounds instantiated at the diagram's own dimensions, for a
diagram with at least one cell. -/
theorem sq_min_le_sum_hookZ' (μ : YoungDiagram) (hr : 0 < μ.rowLen 0) (hc : 0 < μ.colLen 0) :
    (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ^ 2 ≤ ∑ c ∈ μ.cells, hookZ μ c :=
  sq_min_le_sum_hookZ μ (le_refl _) (le_refl _) hc hr

/-- The difference between the cellwise hook sum and the squared minimum dimension is non-negative. -/
theorem sum_hookZ_sub_sq_min_nonneg (μ : YoungDiagram) {N M : ℕ}
    (hN : μ.colLen 0 ≤ N) (hM : μ.rowLen 0 ≤ M) (hN0 : 0 < N) (hM0 : 0 < M) :
    0 ≤ ∑ c ∈ μ.cells, hookZ μ c - (min (μ.rowLen 0) (μ.colLen 0) : ℤ) ^ 2 :=
  sub_nonneg.mpr (sq_min_le_sum_hookZ μ hN hM hN0 hM0)

end QOU.BraidKnot.HookSum
