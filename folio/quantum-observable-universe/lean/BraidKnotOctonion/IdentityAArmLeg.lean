import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.IdentityAArmLeg — toward the general (all-`n`) proof of Identity (A)

**Status: COMPLETE — `statistics_combine` and `identityA` are proved sorry-free** (all-`n`,
every Young diagram), on **Mathlib's `YoungDiagram`**:

  **(A)**  `Σ_cells hook(c)² = Σ_cells content(c)² + n²`.

`#print axioms` for both shows only `[propext, Classical.choice, Quot.sound]` (no `sorryAx`,
no `native_decide`/`decide`). It complements
[`IdentityIContentDecomposition.lean`](IdentityIContentDecomposition.lean), whose list-model defs
are tuned for `native_decide` (exhaustive `n ≤ 22`, all 4507 partitions) and are hostile to
symbolic proof; this is the symbolic, genuinely-general counterpart.

**Foundation.** Built directly on `Mathlib.Combinatorics.Young.YoungDiagram` (`μ.cells`,
`μ.rowLen`, `μ.colLen`, `μ.transpose`). The `transpose` API
(`rowLen_transpose : μ.transpose.rowLen i = μ.colLen i`, and `colLen_transpose`) is exactly the
**conjugation relation** the heart's leg-sums need — `leg μ` over `μ.cells` matches `arm μ.transpose`
over `μ.transpose.cells` under the cell swap `(i,j) ↦ (j,i)`. Hook/arm/leg/content are `ℤ`-valued
to avoid `ℕ`-subtraction.

## Proof architecture (all sorry-free)

`identityA = sumSq_hook_expand ∘ statistics_combine`. The expansion is pure `ring`; the heart
`statistics_combine` is discharged by reducing each of its six statistic sums and the cross term:

- **Squares are reflections.** `sum_arm_sq_eq_sum_jsq` (`Σ arm² = Σ (col)²`, per-row reflection
  `j ↦ rowLen i − 1 − j`) and `sum_leg_sq_eq_sum_isq` (`Σ leg² = Σ (row)²`, its transpose via
  `sum_transpose_swap`); likewise the linear `sum_arm_eq_sum_col`, `sum_leg_eq_sum_row`.
- **The cross term `Σ arm·leg` is a cell-pair cardinality.** `arm_mul_leg_card` writes
  `arm·leg = card(Ioo j (rowLen i) ×ˢ Ioo i (colLen j))`; `sum_armleg_eq_card_bigNE` then
  identifies `Σ arm·leg = card(bigNE)` (cells `R` strictly NE of `S`) by `fiber_card` over the
  corner map (`card_eq_sum_card_fiberwise`).
- **Counting `bigNE`.** `card_product_partition` is the 9-class trichotomy of `cells ×ˢ cells`
  (`split_ifs <;> omega`); with the swap symmetries (`card_bigSW_eq`, `card_bigSE_eq`), the
  NW-rectangle count (`card_bigNW_eq : card(bigNW) = Σ row·col` — left-justification fills the
  rectangle), the axis cards (`card_rowEq_eq`, `card_colEq_eq`) and the diagonal (`card_diag_eq`),
  this yields the closed form `two_sum_armleg`:
  `2·Σ arm·leg = n² + n − Σ rowLen(c.1) − Σ colLen(c.2) − 2·Σ(c.1·c.2)`.
- **Final `ring`/`linarith`.** `sum_rowLen_cells`/`sum_colLen_cells` (`rowLen = arm + col + 1`)
  feed `two_sum_armleg` into the reflections; `linarith` closes.

This is the symbolic realisation of the **arm-leg / co-arm-co-leg** decomposition of §"Proof of (A)"
(`A := arm+1`, `L := leg+1`), with the genuinely-2D cross term handled by the SE-pair count
`#{R SE of S} = Σ c.1·c.2`.

## Retained scaffold helpers (sorry-free)

`sum_one_eq_numCells`, `content_swap`, `leg_eq_arm_transpose`, `sum_arm_transpose_eq_sum_leg`,
`sum_cells_fiberwise`, `sum_arm_row`, `sum_arm_cells`, `sum_leg_cells`.

## References

- [leitner2026] `docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md` §"Proof of (A)"
- [leitner2026] `docs/coordination/s5-so3-keystone.md` (Identity I is the one carried RT input)
-/

open Finset

namespace QOU.BraidKnot.IdentityAArmLeg

/-- Arm of cell `c = (i, j)` in `μ`: cells strictly to the right in the same row. -/
def arm (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := (μ.rowLen c.1 : ℤ) - (c.2 : ℤ) - 1

/-- Leg of cell `c = (i, j)` in `μ`: cells strictly below in the same column. -/
def leg (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := (μ.colLen c.2 : ℤ) - (c.1 : ℤ) - 1

/-- Content of cell `(i, j)` is `j − i`. -/
def content (c : ℕ × ℕ) : ℤ := (c.2 : ℤ) - (c.1 : ℤ)

/-- Hook length of `c` is `arm + leg + 1` — the number of cells in the hook of `c`. -/
def hook (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := arm μ c + leg μ c + 1

/-- Number of cells, `n = |μ|`. -/
def numCells (μ : YoungDiagram) : ℤ := (μ.cells.card : ℤ)

/-- The constant term: `Σ_cells 1 = n`. -/
theorem sum_one_eq_numCells (μ : YoungDiagram) :
    (∑ _c ∈ μ.cells, (1 : ℤ)) = numCells μ := by
  simp [numCells]

/-- **Algebraic expansion of `Σ hook²`** (sorry-free): pure `Finset`-linearity + `ring`.
Reduces Identity (A) to the six per-statistic sums. -/
theorem sumSq_hook_expand (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, (hook μ c) ^ 2
      = (∑ c ∈ μ.cells, (arm μ c) ^ 2) + (∑ c ∈ μ.cells, (leg μ c) ^ 2)
        + (∑ _c ∈ μ.cells, (1 : ℤ)) + 2 * (∑ c ∈ μ.cells, arm μ c * leg μ c)
        + 2 * (∑ c ∈ μ.cells, arm μ c) + 2 * (∑ c ∈ μ.cells, leg μ c) := by
  have hpt : ∀ c, (hook μ c) ^ 2
      = (arm μ c) ^ 2 + (leg μ c) ^ 2 + (1 : ℤ) + 2 * (arm μ c * leg μ c)
        + 2 * (arm μ c) + 2 * (leg μ c) := by
    intro c; simp only [hook]; ring
  simp only [hpt, Finset.sum_add_distrib, Finset.mul_sum]

/-- Content negates under the transpose cell-swap `(i,j) ↦ (j,i)`: `content (j,i) = − content (i,j)`.
Hence `Σ content²` is transpose-invariant — one of the symmetries the heart exploits. -/
theorem content_swap (c : ℕ × ℕ) : content c.swap = - content c := by
  simp only [content, Prod.fst_swap, Prod.snd_swap]; ring

/-- **Pointwise conjugation.** The leg of `c` in `μ` is the arm of `c.swap` in `μ.transpose`:
`leg μ (i,j) = μ.colLen j − i − 1 = μ.transpose.rowLen j − i − 1 = arm μ.transpose (j,i)`. -/
theorem leg_eq_arm_transpose (μ : YoungDiagram) (c : ℕ × ℕ) :
    leg μ c = arm μ.transpose c.swap := by
  simp only [leg, arm, Prod.fst_swap, Prod.snd_swap, YoungDiagram.rowLen_transpose]

/-- **Conjugation relation (leg-sum = transpose arm-sum).** Via the cell swap
`μ.transpose.cells = (prodComm) '' μ.cells`, the arm-sum over `μ.transpose` equals the leg-sum over
`μ`. This is the structural bridge the heart uses to trade leg-statistics for arm-statistics. -/
theorem sum_arm_transpose_eq_sum_leg (μ : YoungDiagram) :
    ∑ c ∈ μ.transpose.cells, arm μ.transpose c = ∑ c ∈ μ.cells, leg μ c := by
  have hmap : μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding := by
    simp [YoungDiagram.transpose, Equiv.finsetCongr_apply]
  rw [hmap, Finset.sum_map]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  simp only [Equiv.coe_toEmbedding, Equiv.prodComm_apply]
  exact (leg_eq_arm_transpose μ c).symm

/-- **Cells decompose into rows** (general, reusable). Any cell-sum is the sum over rows
`i < μ.colLen 0` (the number of rows) of the sum over that row. The workhorse for turning a
cell-statistic into a row-by-row computation. -/
theorem sum_cells_fiberwise (μ : YoungDiagram) (f : ℕ × ℕ → ℤ) :
    (∑ c ∈ μ.cells, f c) = ∑ i ∈ Finset.range (μ.colLen 0), ∑ c ∈ μ.row i, f c := by
  rw [← Finset.sum_fiberwise_of_maps_to (g := Prod.fst) (t := Finset.range (μ.colLen 0))]
  · refine Finset.sum_congr rfl (fun i _ => ?_)
    refine Finset.sum_congr ?_ (fun _ _ => rfl)
    ext c; simp [YoungDiagram.row, YoungDiagram.mem_cells, and_comm]
  · intro c hc
    rw [Finset.mem_range]
    rw [YoungDiagram.mem_cells] at hc
    have h0 : (c.fst, 0) ∈ μ := μ.up_left_mem (le_refl _) (Nat.zero_le _) hc
    rwa [YoungDiagram.mem_iff_lt_colLen] at h0

/-- **Per-row arm sum** = Gauss sum of the row length: `Σ_{c ∈ row i} arm = Σ_{k < rowLen i} k`
(`= rowLen_i·(rowLen_i − 1)/2`), via `row_eq_prod` + the reflection `b ↦ rowLen_i − 1 − b`. -/
theorem sum_arm_row (μ : YoungDiagram) (i : ℕ) :
    (∑ c ∈ μ.row i, arm μ c) = ∑ k ∈ Finset.range (μ.rowLen i), (k : ℤ) := by
  rw [YoungDiagram.row_eq_prod, Finset.sum_product]
  simp only [Finset.sum_singleton, arm]
  rw [← Finset.sum_range_reflect (fun k => (k : ℤ)) (μ.rowLen i)]
  refine Finset.sum_congr rfl (fun b hb => ?_)
  rw [Finset.mem_range] at hb; omega

/-- **`Σ arm` in closed form**: the arm-sum over all cells is `Σ_i Σ_{k < rowLen i} k`
(`= Σ_i C(rowLen_i, 2)`). Combines `sum_cells_fiberwise` with `sum_arm_row`; the first concrete
statistic of the heart. -/
theorem sum_arm_cells (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, arm μ c)
      = ∑ i ∈ Finset.range (μ.colLen 0), ∑ k ∈ Finset.range (μ.rowLen i), (k : ℤ) := by
  rw [sum_cells_fiberwise]
  exact Finset.sum_congr rfl (fun i _ => sum_arm_row μ i)

/-- **`Σ leg` in closed form**, for free from the conjugation bridge: `Σ leg` over `μ` is the
arm-sum over `μ.transpose`, hence `Σ_i Σ_{k < μ.transpose.rowLen i} k` (`= Σ_j C(colLen_j, 2)`).
A one-line corollary of `sum_arm_transpose_eq_sum_leg` + `sum_arm_cells` — the payoff of the
transpose bridge. -/
theorem sum_leg_cells (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, leg μ c)
      = ∑ i ∈ Finset.range (μ.transpose.colLen 0),
          ∑ k ∈ Finset.range (μ.transpose.rowLen i), (k : ℤ) := by
  rw [← sum_arm_transpose_eq_sum_leg, sum_arm_cells]

/-! ## Fiberwise per-statistic sums (sorry-free)

The six statistic sums are now pinned in closed form. Two are *trivial reflections*
(`sum_arm_sq_eq_sum_jsq` : the arm of a row ranges over the same set as the column index;
`sum_leg_sq_eq_sum_isq` : its transpose), and the cross term `Σ arm·leg` is identified with a
**cardinality** of an ordered cell-pair set and counted by a 9-class partition of `cells ×ˢ cells`.
-/

private theorem cast_sub2 (m j : ℕ) (hj : j < m) :
    ((m - j - 1 : ℕ) : ℤ) = (m : ℤ) - j - 1 := by
  rw [Nat.cast_sub (by omega : 1 ≤ m - j), Nat.cast_sub (by omega : j ≤ m)]; ring

/-- Generic per-row reducer: `Σ_{c∈row i} f c = Σ_{j<rowLen i} f (i,j)`. -/
theorem sum_row_eq (μ : YoungDiagram) (i : ℕ) (f : ℕ × ℕ → ℤ) :
    (∑ c ∈ μ.row i, f c) = ∑ j ∈ Finset.range (μ.rowLen i), f (i, j) := by
  rw [YoungDiagram.row_eq_prod, Finset.sum_product]; simp

/-- General transpose bridge: `Σ_{c∈μᵀ.cells} g c = Σ_{c∈μ.cells} g c.swap`. -/
theorem sum_transpose_swap (μ : YoungDiagram) (g : ℕ × ℕ → ℤ) :
    ∑ c ∈ μ.transpose.cells, g c = ∑ c ∈ μ.cells, g c.swap := by
  have hmap : μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding := by
    simp [YoungDiagram.transpose, Equiv.finsetCongr_apply]
  rw [hmap, Finset.sum_map]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  simp only [Equiv.coe_toEmbedding, Equiv.prodComm_apply]

/-- **R1 (per row).** `Σ_{c∈row i} arm² = Σ_{j<rowLen i} j²`: in row `i` the arm
`rowLen i − j − 1` ranges over `{0,…,rowLen i−1}`, the same set as the column index `j`
(reflection `j ↦ rowLen i − 1 − j`). -/
theorem sum_arm_sq_row (μ : YoungDiagram) (i : ℕ) :
    (∑ c ∈ μ.row i, (arm μ c)^2) = ∑ j ∈ Finset.range (μ.rowLen i), ((j : ℤ))^2 := by
  rw [sum_row_eq]
  rw [← Finset.sum_range_reflect (fun j => ((j : ℤ))^2) (μ.rowLen i)]
  refine Finset.sum_congr rfl (fun b hb => ?_)
  rw [Finset.mem_range] at hb
  simp only [arm]
  rw [show ((μ.rowLen i : ℤ) - (b:ℤ) - 1) = (↑(μ.rowLen i - 1 - b)) by
    rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; push_cast; omega]

/-- **R1 over cells.** `Σ arm² = Σ (col index)²`; both reduce to `Σ_i Σ_{j<rowLen i} j²`. -/
theorem sum_arm_sq_eq_sum_jsq (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (arm μ c)^2) = ∑ c ∈ μ.cells, ((c.2 : ℤ))^2 := by
  rw [sum_cells_fiberwise, sum_cells_fiberwise]
  exact Finset.sum_congr rfl (fun i _ => by rw [sum_arm_sq_row]; rw [sum_row_eq])

/-- **R2 over cells.** `Σ leg² = Σ (row index)²`, via the transpose bridge (R1 on `μᵀ`). -/
theorem sum_leg_sq_eq_sum_isq (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (leg μ c)^2) = ∑ c ∈ μ.cells, ((c.1 : ℤ))^2 := by
  have h1 : (∑ c ∈ μ.cells, (leg μ c)^2) = ∑ c ∈ μ.cells, (arm μ.transpose c.swap)^2 :=
    Finset.sum_congr rfl (fun c _ => by rw [leg_eq_arm_transpose])
  rw [h1, ← sum_transpose_swap μ (fun c => (arm μ.transpose c)^2),
     sum_arm_sq_eq_sum_jsq μ.transpose, sum_transpose_swap μ (fun c => ((c.2 : ℤ))^2)]
  simp

/-! ### Cross term `Σ arm·leg` via a cell-pair cardinality

Set `A := arm + 1 = rowLen i − j` (cells weakly right) and `L := leg + 1 = colLen j − i`
(cells weakly below). `arm·leg = (A−1)(L−1) = card(Ioo j (rowLen i) ×ˢ Ioo i (colLen j))`.
Summing over cells and reindexing by the *corner* identifies `Σ arm·leg` with the cardinality
of `bigNE := {(R,S) ∈ cells × cells : rowR < rowS ∧ colR > colS}` (cells with `R` strictly
NE of `S`). The 9-class trichotomy partition of `cells ×ˢ cells` then counts it. -/

/-- `arm·leg` on a cell, as the `ℤ`-cast of a `Nat` rectangle cardinality. -/
theorem arm_mul_leg_card (μ : YoungDiagram) (i j : ℕ) (h : (i,j) ∈ μ) :
    arm μ (i,j) * leg μ (i,j) = (((μ.rowLen i - j - 1) * (μ.colLen j - i - 1) : ℕ) : ℤ) := by
  have hj : j < μ.rowLen i := (YoungDiagram.mem_iff_lt_rowLen).mp h
  have hi : i < μ.colLen j := (YoungDiagram.mem_iff_lt_colLen).mp h
  simp only [arm, leg]
  rw [Nat.cast_mul, cast_sub2 _ _ hj, cast_sub2 _ _ hi]

/-- `R` strictly NE of `S`. -/
noncomputable def bigNE (μ : YoungDiagram) : Finset ((ℕ×ℕ) × (ℕ×ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 < p.2.1 ∧ p.1.2 > p.2.2)
/-- `R` strictly SW of `S`. -/
noncomputable def bigSW (μ : YoungDiagram) : Finset ((ℕ×ℕ) × (ℕ×ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 > p.2.1 ∧ p.1.2 < p.2.2)
/-- `R` strictly NW of `S`. -/
noncomputable def bigNW (μ : YoungDiagram) : Finset ((ℕ×ℕ) × (ℕ×ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 < p.2.1 ∧ p.1.2 < p.2.2)
/-- `R` strictly SE of `S`. -/
noncomputable def bigSE (μ : YoungDiagram) : Finset ((ℕ×ℕ) × (ℕ×ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 > p.2.1 ∧ p.1.2 > p.2.2)

/-- The fiber of `bigNE` over corner cell `(i,j)` has card `(rowLen i − j − 1)(colLen j − i − 1)`:
`(R,S) ↦ (R.2, S.1)` is a bijection onto `Ioo j (rowLen i) ×ˢ Ioo i (colLen j)`. -/
theorem fiber_card (μ : YoungDiagram) (i j : ℕ) (_h : (i,j) ∈ μ) :
    ((bigNE μ).filter (fun p => p.1.1 = i ∧ p.2.2 = j)).card
      = (μ.rowLen i - j - 1) * (μ.colLen j - i - 1) := by
  rw [← Nat.card_Ioo j (μ.rowLen i), ← Nat.card_Ioo i (μ.colLen j), ← Finset.card_product]
  apply Finset.card_bij (fun p _ => (p.1.2, p.2.1))
  · intro p hp
    simp only [bigNE, Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells] at hp
    obtain ⟨⟨⟨hR, hS⟩, hrow, hcol⟩, hci, hcj⟩ := hp
    have hRlt : p.1.2 < μ.rowLen p.1.1 := (YoungDiagram.mem_iff_lt_rowLen).mp (by
      rw [show (p.1.1, p.1.2) = p.1 from rfl]; exact hR)
    have hSlt : p.2.1 < μ.colLen p.2.2 := (YoungDiagram.mem_iff_lt_colLen).mp (by
      rw [show (p.2.1, p.2.2) = p.2 from rfl]; exact hS)
    simp only [Finset.mem_product, Finset.mem_Ioo]
    refine ⟨⟨?_, ?_⟩, ?_, ?_⟩
    · rw [hcj] at hcol; exact hcol
    · rw [hci] at hRlt; exact hRlt
    · rw [hci] at hrow; exact hrow
    · rw [hcj] at hSlt; exact hSlt
  · intro p hp q hq hpq
    simp only [bigNE, Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells] at hp hq
    obtain ⟨_, hpi, hpj⟩ := hp
    obtain ⟨_, hqi, hqj⟩ := hq
    simp only [Prod.mk.injEq] at hpq
    obtain ⟨h1, h2⟩ := hpq
    ext
    · rw [hpi, hqi]
    · exact h1
    · exact h2
    · rw [hpj, hqj]
  · intro b hb
    simp only [Finset.mem_product, Finset.mem_Ioo] at hb
    obtain ⟨⟨hj1, hj2⟩, hi1, hi2⟩ := hb
    have hRmem : (i, b.1) ∈ μ := (YoungDiagram.mem_iff_lt_rowLen).mpr hj2
    have hSmem : (b.2, j) ∈ μ := (YoungDiagram.mem_iff_lt_colLen).mpr hi2
    refine ⟨((i, b.1), (b.2, j)), ?_, ?_⟩
    · rw [Finset.mem_filter]
      refine ⟨?_, rfl, rfl⟩
      simp only [bigNE, Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells]
      exact ⟨⟨hRmem, hSmem⟩, hi1, hj1⟩
    · simp

/-- **`Σ arm·leg = card(bigNE)`.** Sum the rectangle cardinality over cells and reindex by the
corner map `(R,S) ↦ (R.1, S.2)` (`card_eq_sum_card_fiberwise` + `fiber_card`). -/
theorem sum_armleg_eq_card_bigNE (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, arm μ c * leg μ c) = ((bigNE μ).card : ℤ) := by
  have hmaps : Set.MapsTo (fun p : (ℕ×ℕ)×(ℕ×ℕ) => (p.1.1, p.2.2)) ↑(bigNE μ) ↑μ.cells := by
    intro p hp
    simp only [bigNE, Finset.coe_filter, Finset.mem_coe, Set.mem_setOf_eq, Finset.mem_product,
      YoungDiagram.mem_cells] at hp ⊢
    obtain ⟨⟨hR, hS⟩, _, hcol⟩ := hp
    exact μ.up_left_mem (le_refl _) (le_of_lt hcol) hR
  rw [Finset.card_eq_sum_card_fiberwise hmaps]
  push_cast
  refine Finset.sum_congr rfl (fun c hc => ?_)
  rw [YoungDiagram.mem_cells] at hc
  obtain ⟨i, j⟩ := c
  rw [arm_mul_leg_card μ i j hc]
  congr 1
  rw [← fiber_card μ i j hc]
  congr 1
  ext p
  simp only [Finset.mem_filter, Prod.mk.injEq]

/-- `card(bigSW) = card(bigNE)` by the swap involution `(P,Q) ↦ (Q,P)`. -/
theorem card_bigSW_eq (μ : YoungDiagram) : (bigSW μ).card = (bigNE μ).card := by
  apply Finset.card_bij (fun p _ => (p.2, p.1))
  · intro p hp; simp only [bigSW, bigNE, Finset.mem_filter, Finset.mem_product] at hp ⊢
    obtain ⟨⟨h1, h2⟩, h3, h4⟩ := hp; exact ⟨⟨h2, h1⟩, by omega, by omega⟩
  · intro p hp q hq h; simp only [Prod.mk.injEq] at h; ext <;> simp_all
  · intro b hb; simp only [bigNE, Finset.mem_filter, Finset.mem_product] at hb
    obtain ⟨⟨h1, h2⟩, h3, h4⟩ := hb
    refine ⟨(b.2, b.1), ?_, by simp⟩
    simp only [bigSW, Finset.mem_filter, Finset.mem_product]; exact ⟨⟨h2, h1⟩, by omega, by omega⟩

/-- `card(bigSE) = card(bigNW)` by the swap involution. -/
theorem card_bigSE_eq (μ : YoungDiagram) : (bigSE μ).card = (bigNW μ).card := by
  apply Finset.card_bij (fun p _ => (p.2, p.1))
  · intro p hp; simp only [bigSE, bigNW, Finset.mem_filter, Finset.mem_product] at hp ⊢
    obtain ⟨⟨h1, h2⟩, h3, h4⟩ := hp; exact ⟨⟨h2, h1⟩, by omega, by omega⟩
  · intro p hp q hq h; simp only [Prod.mk.injEq] at h; ext <;> simp_all
  · intro b hb; simp only [bigNW, Finset.mem_filter, Finset.mem_product] at hb
    obtain ⟨⟨h1, h2⟩, h3, h4⟩ := hb
    refine ⟨(b.2, b.1), ?_, by simp⟩
    simp only [bigSE, Finset.mem_filter, Finset.mem_product]; exact ⟨⟨h2, h1⟩, by omega, by omega⟩

/-- **`card(bigNW) = Σ_c (row·col)`.** For `(P,Q)` with `P` strictly NW of `Q`, the fiber over
`Q = (i,j)` is `{P : P.1 < i ∧ P.2 < j} = range i ×ˢ range j` (left-justified rows make the whole
NW rectangle present), card `i·j`. -/
theorem card_bigNW_eq (μ : YoungDiagram) :
    ((bigNW μ).card : ℤ) = ∑ c ∈ μ.cells, ((c.1 : ℤ) * (c.2 : ℤ)) := by
  have hmaps : Set.MapsTo (fun p : (ℕ×ℕ)×(ℕ×ℕ) => p.2) ↑(bigNW μ) ↑μ.cells := by
    intro p hp
    simp only [bigNW, Finset.coe_filter, Finset.mem_coe, Set.mem_setOf_eq, Finset.mem_product,
      YoungDiagram.mem_cells] at hp ⊢
    exact hp.1.2
  rw [Finset.card_eq_sum_card_fiberwise hmaps]
  push_cast
  refine Finset.sum_congr rfl (fun c hc => ?_)
  rw [YoungDiagram.mem_cells] at hc
  obtain ⟨i, j⟩ := c
  have hkey : ((bigNW μ).filter (fun p => p.2 = (i,j))).card = i * j := by
    rw [show (i*j) = (Finset.range i ×ˢ Finset.range j).card by
      rw [Finset.card_product, Finset.card_range, Finset.card_range]]
    apply Finset.card_bij (fun p _ => p.1)
    · intro p hp
      simp only [bigNW, Finset.mem_filter, Finset.mem_product] at hp
      obtain ⟨⟨_, hcond⟩, hp2⟩ := hp
      simp only [Finset.mem_product, Finset.mem_range]
      rw [hp2] at hcond
      exact ⟨hcond.1, hcond.2⟩
    · intro p hp q hq h
      simp only [bigNW, Finset.mem_filter] at hp hq
      exact Prod.ext h (hp.2.trans hq.2.symm)
    · intro b hb; simp only [Finset.mem_product, Finset.mem_range] at hb
      have h1 : (i, b.2) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hb.2) hc
      have hbmem : (b.1, b.2) ∈ μ := μ.up_left_mem (le_of_lt hb.1) (le_refl b.2) h1
      have hbmem' : b ∈ μ := by simpa using hbmem
      refine ⟨(b, (i,j)), ?_, rfl⟩
      rw [Finset.mem_filter]
      refine ⟨?_, rfl⟩
      simp only [bigNW, Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells]
      exact ⟨⟨hbmem', hc⟩, hb.1, hb.2⟩
  rw [show ((i:ℤ) * (j:ℤ)) = ((i*j : ℕ) : ℤ) by push_cast; ring]
  rw [← hkey]

/-- **9-class trichotomy partition** of `cells ×ˢ cells` (diag moved left to avoid `ℕ` subtraction):
every ordered pair lands in exactly one of NE / SW / NW / SE / row-equal / col-equal, with the
diagonal double-counted by the two equalities. -/
theorem card_product_partition (μ : YoungDiagram) :
    (μ.cells ×ˢ μ.cells).card
      + ((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1 ∧ p.1.2 = p.2.2)).card
      = (bigNE μ).card + (bigSW μ).card + (bigNW μ).card + (bigSE μ).card
        + ((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1)).card
        + ((μ.cells ×ˢ μ.cells).filter (fun p => p.1.2 = p.2.2)).card := by
  simp only [bigNE, bigSW, bigNW, bigSE]
  rw [Finset.card_eq_sum_ones (μ.cells ×ˢ μ.cells)]
  simp only [Finset.card_filter]
  rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib,
      ← Finset.sum_add_distrib, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  simp only [gt_iff_lt]
  split_ifs <;> omega

/-- `#{(P,Q) : rowP = rowQ} = Σ_c rowLen(c.1)`: the fiber over `P` is its whole row. -/
theorem card_rowEq_eq (μ : YoungDiagram) :
    (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1)).card : ℤ)
      = ∑ c ∈ μ.cells, (μ.rowLen c.1 : ℤ) := by
  have hmaps : Set.MapsTo (fun p : (ℕ×ℕ)×(ℕ×ℕ) => p.1)
      ↑((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1)) ↑μ.cells := by
    intro p hp
    simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_coe, Finset.mem_product,
      YoungDiagram.mem_cells] at hp ⊢
    exact hp.1.1
  rw [Finset.card_eq_sum_card_fiberwise hmaps]
  push_cast
  refine Finset.sum_congr rfl (fun c hc => ?_)
  rw [YoungDiagram.mem_cells] at hc
  obtain ⟨i, j⟩ := c
  -- fiber over (i,j) = {(P,Q): P=(i,j), Q.1=i} ↔ row i (the Q's), card = rowLen i
  have hkey : (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1)).filter
      (fun p => p.1 = (i,j))).card = μ.rowLen i := by
    rw [← Finset.card_range (μ.rowLen i)]
    apply Finset.card_bij (fun p _ => p.2.2)
    · intro p hp
      simp only [Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells] at hp
      obtain ⟨⟨⟨_, hQ⟩, heq⟩, hp1⟩ := hp
      simp only [Finset.mem_range]
      have hr : p.2.1 = i := by rw [← heq, hp1]
      have hlt := (YoungDiagram.mem_iff_lt_rowLen).mp (by rw [show (p.2.1, p.2.2) = p.2 from rfl]; exact hQ)
      rw [hr] at hlt; exact hlt
    · intro p hp q hq h
      simp only [Finset.mem_filter] at hp hq
      have hp1 : p.1 = (i,j) := hp.2
      have hq1 : q.1 = (i,j) := hq.2
      have hpr : p.2.1 = i := by rw [← hp.1.2, hp1]
      have hqr : q.2.1 = i := by rw [← hq.1.2, hq1]
      have : p.2 = q.2 := Prod.ext (hpr.trans hqr.symm) h
      exact Prod.ext (hp1.trans hq1.symm) this
    · intro b hb
      simp only [Finset.mem_range] at hb
      have hQmem : (i, b) ∈ μ := (YoungDiagram.mem_iff_lt_rowLen).mpr hb
      refine ⟨((i,j), (i,b)), ?_, rfl⟩
      rw [Finset.mem_filter]
      refine ⟨?_, rfl⟩
      simp only [Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells, and_true]
      exact ⟨hc, hQmem⟩
  rw [show (μ.rowLen (i,j).1 : ℤ) = ((μ.rowLen i : ℕ) : ℤ) from rfl, ← hkey, Finset.filter_filter]

/-- `#{(P,Q) : colP = colQ} = Σ_c colLen(c.2)` (transpose of `card_rowEq_eq`). -/
theorem card_colEq_eq (μ : YoungDiagram) :
    (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.2 = p.2.2)).card : ℤ)
      = ∑ c ∈ μ.cells, (μ.colLen c.2 : ℤ) := by
  have hmaps : Set.MapsTo (fun p : (ℕ×ℕ)×(ℕ×ℕ) => p.1)
      ↑((μ.cells ×ˢ μ.cells).filter (fun p => p.1.2 = p.2.2)) ↑μ.cells := by
    intro p hp
    simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_coe, Finset.mem_product,
      YoungDiagram.mem_cells] at hp ⊢
    exact hp.1.1
  rw [Finset.card_eq_sum_card_fiberwise hmaps]
  push_cast
  refine Finset.sum_congr rfl (fun c hc => ?_)
  rw [YoungDiagram.mem_cells] at hc
  obtain ⟨i, j⟩ := c
  have hkey : (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.2 = p.2.2)).filter
      (fun p => p.1 = (i,j))).card = μ.colLen j := by
    rw [← Finset.card_range (μ.colLen j)]
    apply Finset.card_bij (fun p _ => p.2.1)
    · intro p hp
      simp only [Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells] at hp
      obtain ⟨⟨⟨_, hQ⟩, heq⟩, hp1⟩ := hp
      simp only [Finset.mem_range]
      have hc2 : p.2.2 = j := by rw [← heq, hp1]
      have hlt := (YoungDiagram.mem_iff_lt_colLen).mp (by rw [show (p.2.1, p.2.2) = p.2 from rfl]; exact hQ)
      rw [hc2] at hlt; exact hlt
    · intro p hp q hq h
      simp only [Finset.mem_filter] at hp hq
      have hp1 : p.1 = (i,j) := hp.2
      have hq1 : q.1 = (i,j) := hq.2
      have hpc : p.2.2 = j := by rw [← hp.1.2, hp1]
      have hqc : q.2.2 = j := by rw [← hq.1.2, hq1]
      have : p.2 = q.2 := Prod.ext h (hpc.trans hqc.symm)
      exact Prod.ext (hp1.trans hq1.symm) this
    · intro b hb
      simp only [Finset.mem_range] at hb
      have hQmem : (b, j) ∈ μ := (YoungDiagram.mem_iff_lt_colLen).mpr hb
      refine ⟨((i,j), (b,j)), ?_, rfl⟩
      rw [Finset.mem_filter]
      refine ⟨?_, rfl⟩
      simp only [Finset.mem_filter, Finset.mem_product, YoungDiagram.mem_cells, and_true]
      exact ⟨hc, hQmem⟩
  rw [show (μ.colLen (i,j).2 : ℤ) = ((μ.colLen j : ℕ) : ℤ) from rfl, ← hkey, Finset.filter_filter]

/-- `#{(P,Q) : P = Q} = numCells`: the diagonal of `cells ×ˢ cells`, via `p ↦ p.1`. -/
theorem card_diag_eq (μ : YoungDiagram) :
    (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1 ∧ p.1.2 = p.2.2)).card : ℤ)
      = numCells μ := by
  rw [numCells]
  congr 1
  apply Finset.card_bij (fun p _ => p.1)
  · intro p hp
    simp only [Finset.mem_filter, Finset.mem_product] at hp
    exact hp.1.1
  · intro p hp q hq h
    simp only [Finset.mem_filter, Finset.mem_product] at hp hq
    obtain ⟨_, hp1, hp2⟩ := hp
    obtain ⟨_, hq1, hq2⟩ := hq
    have hpe : p.1 = p.2 := Prod.ext hp1 hp2
    have hqe : q.1 = q.2 := Prod.ext hq1 hq2
    exact Prod.ext h (hpe.symm.trans (h.trans hqe))
  · intro b hb
    refine ⟨(b, b), ?_, rfl⟩
    simp only [Finset.mem_filter, Finset.mem_product, and_true, and_self]
    exact hb


/-- Per-row reflection: `Σ arm = Σ (col index)`. -/
theorem sum_arm_eq_sum_col (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, arm μ c) = ∑ c ∈ μ.cells, (c.2 : ℤ) := by
  rw [sum_cells_fiberwise, sum_cells_fiberwise]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [sum_row_eq (f := fun c => arm μ c), sum_row_eq (f := fun c => (c.2 : ℤ))]
  rw [← Finset.sum_range_reflect (fun j => ((j : ℤ))) (μ.rowLen i)]
  refine Finset.sum_congr rfl (fun b hb => ?_)
  rw [Finset.mem_range] at hb
  simp only [arm]
  rw [show ((μ.rowLen i : ℤ) - (b:ℤ) - 1) = (↑(μ.rowLen i - 1 - b)) by
    rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; push_cast; omega]

/-- Transpose of `sum_arm_eq_sum_col`: `Σ leg = Σ (row index)`. -/
theorem sum_leg_eq_sum_row (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, leg μ c) = ∑ c ∈ μ.cells, (c.1 : ℤ) := by
  have h1 : (∑ c ∈ μ.cells, leg μ c) = ∑ c ∈ μ.cells, arm μ.transpose c.swap :=
    Finset.sum_congr rfl (fun c _ => by rw [leg_eq_arm_transpose])
  rw [h1, ← sum_transpose_swap μ (fun c => arm μ.transpose c), sum_arm_eq_sum_col μ.transpose,
     sum_transpose_swap μ (fun c => (c.2 : ℤ))]
  simp

/-- `Σ rowLen(c.1) = Σ arm + Σ(c.2) + numCells` (pointwise `rowLen i = arm + j + 1` on cells). -/
theorem sum_rowLen_cells (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (μ.rowLen c.1 : ℤ))
      = (∑ c ∈ μ.cells, arm μ c) + (∑ c ∈ μ.cells, (c.2 : ℤ)) + numCells μ := by
  rw [show numCells μ = ∑ _c ∈ μ.cells, (1:ℤ) from (sum_one_eq_numCells μ).symm]
  rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun c hc => ?_)
  rw [YoungDiagram.mem_cells] at hc
  simp only [arm]
  ring

/-- Transpose: `Σ colLen(c.2) = Σ leg + Σ(c.1) + numCells`. -/
theorem sum_colLen_cells (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (μ.colLen c.2 : ℤ))
      = (∑ c ∈ μ.cells, leg μ c) + (∑ c ∈ μ.cells, (c.1 : ℤ)) + numCells μ := by
  rw [show numCells μ = ∑ _c ∈ μ.cells, (1:ℤ) from (sum_one_eq_numCells μ).symm]
  rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun c hc => ?_)
  rw [YoungDiagram.mem_cells] at hc
  simp only [leg]
  ring

/-- **Cross-term closed form (the crux, sorry-free).**
`2·Σ arm·leg = numCells² + numCells − Σ rowLen(c.1) − Σ colLen(c.2) − 2·Σ(c.1·c.2)`,
from the 9-class partition of `cells ×ˢ cells` with the four quadrant cards
(NE = SW = `Σ arm·leg`, NW = SE = `Σ c.1·c.2`), the two axis cards, and the diagonal. -/
theorem two_sum_armleg (μ : YoungDiagram) :
    2 * (∑ c ∈ μ.cells, arm μ c * leg μ c)
      = (numCells μ)^2 + numCells μ
        - (∑ c ∈ μ.cells, (μ.rowLen c.1 : ℤ)) - (∑ c ∈ μ.cells, (μ.colLen c.2 : ℤ))
        - 2 * (∑ c ∈ μ.cells, ((c.1 : ℤ) * (c.2 : ℤ))) := by
  have hpart : ((μ.cells ×ˢ μ.cells).card : ℤ)
      + (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1 ∧ p.1.2 = p.2.2)).card : ℤ)
      = ((bigNE μ).card : ℤ) + ((bigSW μ).card : ℤ) + ((bigNW μ).card : ℤ) + ((bigSE μ).card : ℤ)
        + (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.1 = p.2.1)).card : ℤ)
        + (((μ.cells ×ˢ μ.cells).filter (fun p => p.1.2 = p.2.2)).card : ℤ) := by
    exact_mod_cast card_product_partition μ
  rw [Finset.card_product] at hpart
  push_cast at hpart
  have hNE : ((bigNE μ).card : ℤ) = ∑ c ∈ μ.cells, arm μ c * leg μ c :=
    (sum_armleg_eq_card_bigNE μ).symm
  have hSW : ((bigSW μ).card : ℤ) = ∑ c ∈ μ.cells, arm μ c * leg μ c := by
    rw [card_bigSW_eq]; exact hNE
  have hSE : ((bigSE μ).card : ℤ) = ∑ c ∈ μ.cells, ((c.1 : ℤ) * (c.2 : ℤ)) := by
    rw [card_bigSE_eq]; exact card_bigNW_eq μ
  rw [hNE, hSW, hSE, card_bigNW_eq μ, card_rowEq_eq μ, card_colEq_eq μ, card_diag_eq μ] at hpart
  -- hpart : numCells*numCells + numCells = Σarmleg+Σarmleg+Σij+Σij+ΣrowLen+ΣcolLen
  rw [numCells] at hpart ⊢
  linarith [hpart]

/-- **The heart (sorry-free).** The six statistic sums combine to `Σ content² + n²`, proved by
combining the fiberwise reflections `Σ arm² = Σ(col)²`, `Σ leg² = Σ(row)²`, `Σ arm = Σ col`,
`Σ leg = Σ row` with the cross-term closed form `two_sum_armleg`.
-- Ref: [leitner2026] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (A)" -/
theorem statistics_combine (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (arm μ c) ^ 2) + (∑ c ∈ μ.cells, (leg μ c) ^ 2)
        + (∑ _c ∈ μ.cells, (1 : ℤ)) + 2 * (∑ c ∈ μ.cells, arm μ c * leg μ c)
        + 2 * (∑ c ∈ μ.cells, arm μ c) + 2 * (∑ c ∈ μ.cells, leg μ c)
      = (∑ c ∈ μ.cells, (content c) ^ 2) + (numCells μ) ^ 2 := by
  -- content² = (c.2 - c.1)² = (c.2)² - 2 c.1 c.2 + (c.1)²  pointwise
  have hcontent : (∑ c ∈ μ.cells, (content c) ^ 2)
      = (∑ c ∈ μ.cells, ((c.2 : ℤ))^2) - 2 * (∑ c ∈ μ.cells, ((c.1 : ℤ) * (c.2 : ℤ)))
        + (∑ c ∈ μ.cells, ((c.1 : ℤ))^2) := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun c _ => by simp only [content]; ring)
  have h1c : (∑ _c ∈ μ.cells, (1 : ℤ)) = numCells μ := sum_one_eq_numCells μ
  rw [sum_arm_sq_eq_sum_jsq, sum_leg_sq_eq_sum_isq, hcontent, h1c,
      sum_arm_eq_sum_col, sum_leg_eq_sum_row]
  have hcross := two_sum_armleg μ
  rw [sum_rowLen_cells, sum_colLen_cells, sum_arm_eq_sum_col, sum_leg_eq_sum_row] at hcross
  linarith [hcross]

/-- **Identity (A), general form** — `Σ hook² = Σ content² + n²`, for every Young diagram `μ`.
Proved by the algebraic expansion (`sumSq_hook_expand`) composed with the now-discharged heart
(`statistics_combine`). Sorry-free. -/
theorem identityA (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, (hook μ c) ^ 2
      = (∑ c ∈ μ.cells, (content c) ^ 2) + (numCells μ) ^ 2 := by
  rw [sumSq_hook_expand, statistics_combine]

end QOU.BraidKnot.IdentityAArmLeg
