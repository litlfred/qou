import QOU.BraidKnot.PieceAGeneral

/-!
# The hook-sum closed form

For every Young diagram `μ` with `n = |μ|` cells, row lengths `λ` and column
lengths `λ'`,

    Σ_{c∈μ} hook(c) = Σ_i C(λ_i, 2) + Σ_j C(λ'_j, 2) + n,

equivalently, doubling to stay in `ℤ` and folding `n` into the squares,

    2 · Σ_{c∈μ} hook(c) = p₂(λ) + p₂(λ'),      p₂(λ) := Σ_i λ_i².

The second form is the one the Plancherel analysis uses: it exhibits `Σ_h` as a
**conjugation-symmetric** functional of the diagram, half the sum of `p₂` on `λ`
and on its transpose. That symmetry is what forces `Σ_h` outside the algebra
`Λ*` of shifted symmetric functions — the free cumulants `R_k` have conjugation
parity `R_k(λ') = (−1)^k R_k(λ)`, so a `Λ*` element invariant under conjugation
can carry no odd-degree part, while `Σ_h` grows like `n^{3/2}`.

This module supplies only the identity. It is proved from the reflection lemmas
already established for Piece A (`sum_armZ_generic`, `sum_legZ_generic`,
`sum_swap_transpose` in `PieceAGeneral`) plus a cells-to-rows decomposition,
so it carries no new combinatorial input.

## Prior art — the same identity in the `List ℕ` register

`QOU.Common.HookSumComplete.hookSum_eq` already proves this identity, sorry-free,
as `Σ_c h(c) = b(λ') + b(λ) + n` over a **sorted `List ℕ`**, with its own
`colLen` / `bStat` / `armPart` / `legPart` / `hookSum` definitions in `ℕ`
(truncated subtraction) and an explicit sortedness hypothesis. This module is
that identity restated where the rest of the corpus lives: on Mathlib's
`YoungDiagram`, over `ℤ`, on the `armZ` / `legZ` / `hookZ` of `PieceAGeneral` —
so it composes with `pieceA` and the rest of `QOU.BraidKnot`, which the
`List ℕ` version cannot, and needs no sortedness hypothesis, `YoungDiagram`
carrying that structurally.

`sum_hookZ_eq_bStat` below states the result in `HookSumComplete`'s own
`b(λ') + b(λ) + n` shape, term for term, so the correspondence is visible rather
than asserted. The two are **not** bridged: that needs `YoungDiagram.rowLens`
lemmas relating `l.getD i 0` to `μ.rowLen i` and the `ℕ`/`ℤ` cast, and is
tracked separately. The three `QOU.Common.HookSum*` modules are pre-existing
import orphans (bean `qou-kljb`, owner-scoped); this one is wired into
`QOU.BraidKnot`.

## Index sets

The row and column sums are taken over `range N` / `range M` for **any** `N`,
`M` large enough to cover the diagram (`μ.colLen 0 ≤ N` rows, `μ.rowLen 0 ≤ M`
columns). Outside that range `rowLen`/`colLen` vanish, so every admissible
choice gives the same value; taking a hypothesis rather than a canonical `N`
keeps the statement usable against whatever bound a caller already has.

## Base ring

All sums over `ℤ`, matching `PieceAGeneral` — no `ℝ`, no archimedean input.

-- Ref: [leitner2026] computations/deltalambda/wlambda_covariance_epic_A1_sigmah_not_polynomial.py
-/

namespace QOU.BraidKnot.HookSum

open Finset QOU.BraidKnot.PieceA

/-! ## Row arithmetic -/

/-- Gauss, cast to `ℤ`: `2 · Σ_{j<m} j = m(m−1)`. -/
theorem two_mul_sum_range_cast (m : ℕ) :
    2 * ∑ j ∈ range m, (j : ℤ) = (m : ℤ) * ((m : ℤ) - 1) := by
  induction m with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ]
    push_cast
    push_cast at ih
    linarith

/-! ## Cells to rows -/

/-- The `i`-th row is exactly the cells whose first coordinate is `i`. -/
theorem filter_fst_eq_row (μ : YoungDiagram) (i : ℕ) :
    μ.cells.filter (fun c => c.1 = i) = μ.row i := by
  ext c
  simp only [Finset.mem_filter, YoungDiagram.mem_row_iff, YoungDiagram.mem_cells]

/-- Every cell sits in one of the first `μ.colLen 0` rows. -/
theorem fst_lt_colLen_zero (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    c.1 < μ.colLen 0 := by
  have h1 : c.1 < μ.colLen c.2 := by
    have := (YoungDiagram.mem_iff_lt_colLen (μ := μ) (i := c.1) (j := c.2)).mp
      (by simpa using hc)
    exact this
  have h2 : μ.colLen c.2 ≤ μ.colLen 0 := μ.colLen_anti 0 c.2 (Nat.zero_le _)
  omega

/-- **Cells-to-rows decomposition.** A sum over the cells of `μ` is the sum over
rows `i < N` of the sum along row `i`, for any `N` covering the diagram. -/
theorem sum_cells_eq_sum_rows (μ : YoungDiagram) {N : ℕ} (hN : μ.colLen 0 ≤ N)
    (f : ℕ × ℕ → ℤ) :
    ∑ c ∈ μ.cells, f c = ∑ i ∈ range N, ∑ j ∈ range (μ.rowLen i), f (i, j) := by
  have hmaps : ∀ c ∈ μ.cells, c.1 ∈ range N := by
    intro c hc
    rw [Finset.mem_range]
    exact lt_of_lt_of_le (fst_lt_colLen_zero μ hc) hN
  rw [← Finset.sum_fiberwise_of_maps_to hmaps f]
  refine Finset.sum_congr rfl ?_
  intro i _
  rw [filter_fst_eq_row μ i, YoungDiagram.row_eq_prod, Finset.sum_product,
    Finset.sum_singleton]

/-- The row lengths sum to the number of cells. -/
theorem sum_rowLen_eq_card (μ : YoungDiagram) {N : ℕ} (hN : μ.colLen 0 ≤ N) :
    ∑ i ∈ range N, (μ.rowLen i : ℤ) = (μ.cells.card : ℤ) := by
  have h := sum_cells_eq_sum_rows μ hN (fun _ => (1 : ℤ))
  simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one] at h
  omega

/-- Transposing preserves the number of cells. -/
theorem card_transpose (μ : YoungDiagram) :
    (μ.transpose.cells.card : ℤ) = (μ.cells.card : ℤ) := by
  have h := sum_swap_transpose μ (fun _ => (1 : ℤ))
  simp only [Finset.sum_const, nsmul_eq_mul, mul_one] at h
  omega

/-- The column lengths sum to the number of cells. -/
theorem sum_colLen_eq_card (μ : YoungDiagram) {M : ℕ} (hM : μ.rowLen 0 ≤ M) :
    ∑ j ∈ range M, (μ.colLen j : ℤ) = (μ.cells.card : ℤ) := by
  have hcol0 : μ.transpose.colLen 0 ≤ M := by
    rw [YoungDiagram.colLen_transpose]; exact hM
  have h := sum_rowLen_eq_card μ.transpose hcol0
  simp only [YoungDiagram.rowLen_transpose] at h
  rw [h, card_transpose]

/-! ## The two coordinate sums -/

/-- `2 · Σ_c j(c) = Σ_i λ_i(λ_i−1)`: summing the column index over the cells
counts, twice, the ordered same-row pairs. -/
theorem two_mul_sum_snd (μ : YoungDiagram) {N : ℕ} (hN : μ.colLen 0 ≤ N) :
    2 * ∑ c ∈ μ.cells, (c.2 : ℤ)
      = ∑ i ∈ range N, (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) - 1) := by
  rw [sum_cells_eq_sum_rows μ hN (fun c => (c.2 : ℤ)), Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro i _
  exact two_mul_sum_range_cast (μ.rowLen i)

/-- `2 · Σ_c i(c) = Σ_j λ'_j(λ'_j−1)`, the transpose of `two_mul_sum_snd`. -/
theorem two_mul_sum_fst (μ : YoungDiagram) {M : ℕ} (hM : μ.rowLen 0 ≤ M) :
    2 * ∑ c ∈ μ.cells, (c.1 : ℤ)
      = ∑ j ∈ range M, (μ.colLen j : ℤ) * ((μ.colLen j : ℤ) - 1) := by
  have hswap : ∑ c ∈ μ.cells, (c.1 : ℤ) = ∑ d ∈ μ.transpose.cells, (d.2 : ℤ) := by
    have h := sum_swap_transpose μ (fun d => (d.2 : ℤ))
    simpa using h
  have hcol0 : μ.transpose.colLen 0 ≤ M := by
    rw [YoungDiagram.colLen_transpose]; exact hM
  rw [hswap, two_mul_sum_snd μ.transpose hcol0]
  simp only [YoungDiagram.rowLen_transpose]

/-! ## The hook sum -/

/-- The hook sum splits into the two coordinate sums plus the cell count — the
arm and leg reflections of `PieceAGeneral` applied at `F = id`. -/
theorem sum_hookZ_eq (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, hookZ μ c
      = (∑ c ∈ μ.cells, (c.2 : ℤ)) + (∑ c ∈ μ.cells, (c.1 : ℤ))
        + (μ.cells.card : ℤ) := by
  have h_arm : ∑ c ∈ μ.cells, armZ μ c = ∑ c ∈ μ.cells, (c.2 : ℤ) :=
    sum_armZ_generic μ (fun x => x)
  have h_leg : ∑ c ∈ μ.cells, legZ μ c = ∑ c ∈ μ.cells, (c.1 : ℤ) :=
    sum_legZ_generic μ (fun x => x)
  simp only [hookZ]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, h_arm, h_leg]
  simp

/-- **The hook-sum closed form.** `2 Σ_c hook(c) = Σ_i λ_i(λ_i−1) + Σ_j
λ'_j(λ'_j−1) + 2n`, i.e. `Σ_c hook(c) = Σ_i C(λ_i,2) + Σ_j C(λ'_j,2) + n`. -/
theorem two_mul_sum_hookZ (μ : YoungDiagram) {N M : ℕ}
    (hN : μ.colLen 0 ≤ N) (hM : μ.rowLen 0 ≤ M) :
    2 * ∑ c ∈ μ.cells, hookZ μ c
      = ∑ i ∈ range N, (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) - 1)
        + ∑ j ∈ range M, (μ.colLen j : ℤ) * ((μ.colLen j : ℤ) - 1)
        + 2 * (μ.cells.card : ℤ) := by
  rw [sum_hookZ_eq μ]
  have h2 := two_mul_sum_snd μ hN
  have h1 := two_mul_sum_fst μ hM
  linarith

/-- **`Σ_h` is half the sum of `p₂` on `λ` and on `λ'`.** `2 Σ_c hook(c) =
Σ_i λ_i² + Σ_j λ'_j²` — the conjugation-symmetric form. -/
theorem two_mul_sum_hookZ_eq_sum_sq (μ : YoungDiagram) {N M : ℕ}
    (hN : μ.colLen 0 ≤ N) (hM : μ.rowLen 0 ≤ M) :
    2 * ∑ c ∈ μ.cells, hookZ μ c
      = ∑ i ∈ range N, (μ.rowLen i : ℤ) ^ 2
        + ∑ j ∈ range M, (μ.colLen j : ℤ) ^ 2 := by
  have hmain := two_mul_sum_hookZ μ hN hM
  have hrow : ∑ i ∈ range N, (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) - 1)
      = (∑ i ∈ range N, (μ.rowLen i : ℤ) ^ 2) - (μ.cells.card : ℤ) := by
    rw [Finset.sum_congr rfl (fun i _ => by ring :
        ∀ i ∈ range N, (μ.rowLen i : ℤ) * ((μ.rowLen i : ℤ) - 1)
          = (μ.rowLen i : ℤ) ^ 2 - (μ.rowLen i : ℤ)),
      Finset.sum_sub_distrib, sum_rowLen_eq_card μ hN]
  have hcol : ∑ j ∈ range M, (μ.colLen j : ℤ) * ((μ.colLen j : ℤ) - 1)
      = (∑ j ∈ range M, (μ.colLen j : ℤ) ^ 2) - (μ.cells.card : ℤ) := by
    rw [Finset.sum_congr rfl (fun j _ => by ring :
        ∀ j ∈ range M, (μ.colLen j : ℤ) * ((μ.colLen j : ℤ) - 1)
          = (μ.colLen j : ℤ) ^ 2 - (μ.colLen j : ℤ)),
      Finset.sum_sub_distrib, sum_colLen_eq_card μ hM]
  rw [hrow, hcol] at hmain
  linarith

/-! ## The same identity in the `n(λ)` register

`HookSumComplete` states the hook sum as `b(λ') + b(λ) + n` with
`b(λ) = Σ_i i·λ_i`. These three lemmas give that shape here, so the two
statements can be read against each other term by term. -/

/-- `Σ_c i(c) = Σ_i i·λ_i = b(λ)`: row `i` contributes `λ_i` cells, each of
first coordinate `i`. -/
theorem sum_fst_eq_bStat (μ : YoungDiagram) {N : ℕ} (hN : μ.colLen 0 ≤ N) :
    ∑ c ∈ μ.cells, (c.1 : ℤ) = ∑ i ∈ range N, (i : ℤ) * (μ.rowLen i : ℤ) := by
  rw [sum_cells_eq_sum_rows μ hN (fun c => (c.1 : ℤ))]
  refine Finset.sum_congr rfl ?_
  intro i _
  simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  ring

/-- `Σ_c j(c) = Σ_j j·λ'_j = b(λ')`, the transpose of `sum_fst_eq_bStat`. -/
theorem sum_snd_eq_bStat_conj (μ : YoungDiagram) {M : ℕ} (hM : μ.rowLen 0 ≤ M) :
    ∑ c ∈ μ.cells, (c.2 : ℤ) = ∑ j ∈ range M, (j : ℤ) * (μ.colLen j : ℤ) := by
  have hswap : ∑ c ∈ μ.cells, (c.2 : ℤ) = ∑ d ∈ μ.transpose.cells, (d.1 : ℤ) := by
    have h := sum_swap_transpose μ (fun d => (d.1 : ℤ))
    simpa using h
  have hcol0 : μ.transpose.colLen 0 ≤ M := by
    rw [YoungDiagram.colLen_transpose]; exact hM
  rw [hswap, sum_fst_eq_bStat μ.transpose hcol0]
  simp only [YoungDiagram.rowLen_transpose]

/-- **The hook-sum identity in the `n(λ)` register**: `Σ_c h(c) = b(λ') + b(λ) + n`.
This is `QOU.Common.HookSumComplete.hookSum_eq` on `YoungDiagram` over `ℤ`. -/
theorem sum_hookZ_eq_bStat (μ : YoungDiagram) {N M : ℕ}
    (hN : μ.colLen 0 ≤ N) (hM : μ.rowLen 0 ≤ M) :
    ∑ c ∈ μ.cells, hookZ μ c
      = ∑ j ∈ range M, (j : ℤ) * (μ.colLen j : ℤ)
        + ∑ i ∈ range N, (i : ℤ) * (μ.rowLen i : ℤ)
        + (μ.cells.card : ℤ) := by
  rw [sum_hookZ_eq μ, sum_snd_eq_bStat_conj μ hM, sum_fst_eq_bStat μ hN]

end QOU.BraidKnot.HookSum
