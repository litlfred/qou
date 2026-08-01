import Mathlib.Tactic
import Mathlib.Combinatorics.Young.YoungDiagram

/-!
# Piece A of Identity I — general-`n` (Mathlib `YoungDiagram`, HLF-free)

The per-partition hook–content identity

    Σ_{c∈μ} hook(c)² = Σ_{c∈μ} content(c)² + n²,   n = |μ|,

for **every** Young diagram `μ` (`docs/audits/2026-08-01-keystone-identity-I-piece-A-general-proof.md`,
bean `qou-o5xj`). This is the HLF-free half of Identity I `2M(n)=n(3n−1)`, the
carried input to the keystone defect closed form `144·C(n)=−n(n−1)(2n−13)`
(`WLambdaDefectClosedForm`). No hook-length formula, no dimensions, no RSK.

Stage 1 (this commit): definitions + the hook decomposition
`hook(i,j) = rowLen i + colLen j − i − j − 1` and cell non-negativity.

## Base ring (§7c)

All sums over `ℤ` (contents are signed); no `ℝ`, no archimedean input.

-- Ref: [manuscript] docs/audits/2026-08-01-keystone-identity-I-piece-A-general-proof.md; bean qou-o5xj
-/

namespace QOU.BraidKnot.PieceA

open Finset

/-- Arm length of cell `c=(i,j)` in `μ`, over `ℤ`: cells strictly right in the row. -/
def armZ (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := (μ.rowLen c.1 : ℤ) - (c.2 : ℤ) - 1

/-- Leg length of cell `c=(i,j)` in `μ`, over `ℤ`: cells strictly below in the column. -/
def legZ (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := (μ.colLen c.2 : ℤ) - (c.1 : ℤ) - 1

/-- Hook length `= arm + leg + 1`. -/
def hookZ (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := armZ μ c + legZ μ c + 1

/-- Content `= j − i`. -/
def contentZ (c : ℕ × ℕ) : ℤ := (c.2 : ℤ) - (c.1 : ℤ)

theorem hookZ_eq (μ : YoungDiagram) (c : ℕ × ℕ) :
    hookZ μ c = (μ.rowLen c.1 : ℤ) + (μ.colLen c.2 : ℤ) - (c.1 : ℤ) - (c.2 : ℤ) - 1 := by
  simp only [hookZ, armZ, legZ]; ring

/-- For a genuine cell, the arm is non-negative (`j < rowLen i`). -/
theorem armZ_nonneg (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ) : 0 ≤ armZ μ c := by
  have h : c.2 < μ.rowLen c.1 := by
    have := μ.mem_iff_lt_rowLen (i := c.1) (j := c.2)
    simpa using this.mp (by simpa using hc)
  simp only [armZ]
  have : (c.2 : ℤ) + 1 ≤ (μ.rowLen c.1 : ℤ) := by exact_mod_cast h
  linarith

/-- For a genuine cell, the leg is non-negative (`i < colLen j`). -/
theorem legZ_nonneg (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ) : 0 ≤ legZ μ c := by
  have h : c.1 < μ.colLen c.2 := by
    have := μ.mem_iff_lt_colLen (i := c.1) (j := c.2)
    simpa using this.mp (by simpa using hc)
  simp only [legZ]
  have : (c.1 : ℤ) + 1 ≤ (μ.colLen c.2 : ℤ) := by exact_mod_cast h
  linarith

/-! ## Stage 2 — row reflection: `Σ F(arm) = Σ F(left)` -/

/-- Row reflection `(i,j) ↦ (i, rowLen i − 1 − j)` — an involution on cells that
sends the arm length to the left-count `j`. -/
def rowRefl (μ : YoungDiagram) (c : ℕ × ℕ) : ℕ × ℕ := (c.1, μ.rowLen c.1 - 1 - c.2)

theorem mem_cells_iff_snd_lt (μ : YoungDiagram) (c : ℕ × ℕ) :
    c ∈ μ.cells ↔ c.2 < μ.rowLen c.1 := by
  rw [YoungDiagram.mem_cells]; exact μ.mem_iff_lt_rowLen

theorem rowRefl_mem (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    rowRefl μ c ∈ μ.cells := by
  have hlt : c.2 < μ.rowLen c.1 := (mem_cells_iff_snd_lt μ c).mp hc
  rw [mem_cells_iff_snd_lt]
  simp only [rowRefl]
  omega

theorem rowRefl_invol (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    rowRefl μ (rowRefl μ c) = c := by
  have hlt : c.2 < μ.rowLen c.1 := (mem_cells_iff_snd_lt μ c).mp hc
  simp only [rowRefl]
  ext
  · rfl
  · simp only; omega

theorem armZ_eq_rowRefl_snd (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    armZ μ c = ((rowRefl μ c).2 : ℤ) := by
  have hlt : c.2 < μ.rowLen c.1 := (mem_cells_iff_snd_lt μ c).mp hc
  simp only [armZ, rowRefl]
  omega

/-- **Row reflection.** For any `F`, summing `F(arm)` over the cells equals summing
`F(left-count j)` — the arm/left multisets agree per row. -/
theorem sum_armZ_generic (μ : YoungDiagram) (F : ℤ → ℤ) :
    ∑ c ∈ μ.cells, F (armZ μ c) = ∑ c ∈ μ.cells, F ((c.2 : ℤ)) := by
  refine Finset.sum_bij' (fun c _ => rowRefl μ c) (fun c _ => rowRefl μ c)
    (fun c hc => rowRefl_mem μ hc) (fun c hc => rowRefl_mem μ hc)
    (fun c hc => rowRefl_invol μ hc) (fun c hc => rowRefl_invol μ hc)
    (fun c hc => by rw [armZ_eq_rowRefl_snd μ hc])

/-! ## Stage 3 — leg reflection via transpose: `Σ F(leg) = Σ F(above)` -/

/-- Legs of `μ` are arms of the transpose (swapped): `leg μ c = arm μᵀ c.swap`. -/
theorem legZ_eq_transpose_armZ (μ : YoungDiagram) (c : ℕ × ℕ) :
    legZ μ c = armZ μ.transpose c.swap := by
  simp only [legZ, armZ, Prod.fst_swap, Prod.snd_swap, YoungDiagram.rowLen_transpose]

/-- Reindex a cell sum by `swap` to the transpose diagram. -/
theorem sum_swap_transpose (μ : YoungDiagram) (H : ℕ × ℕ → ℤ) :
    ∑ c ∈ μ.cells, H c.swap = ∑ d ∈ μ.transpose.cells, H d := by
  refine Finset.sum_bij' (fun c _ => c.swap) (fun d _ => d.swap)
    ?_ ?_ ?_ ?_ ?_
  · intro c hc
    simp only [YoungDiagram.mem_cells, YoungDiagram.mem_transpose, Prod.swap_swap]
    simpa only [YoungDiagram.mem_cells] using hc
  · intro d hd
    simpa only [YoungDiagram.mem_cells, YoungDiagram.mem_transpose] using hd
  · intro c _; exact Prod.swap_swap c
  · intro d _; exact Prod.swap_swap d
  · intro c _; rfl

/-- **Leg reflection.** For any `F`, summing `F(leg)` over the cells equals summing
`F(above-count i)`. -/
theorem sum_legZ_generic (μ : YoungDiagram) (F : ℤ → ℤ) :
    ∑ c ∈ μ.cells, F (legZ μ c) = ∑ c ∈ μ.cells, F ((c.1 : ℤ)) := by
  have e1 : ∑ c ∈ μ.cells, F (legZ μ c)
      = ∑ c ∈ μ.cells, (fun d => F (armZ μ.transpose d)) c.swap := by
    apply Finset.sum_congr rfl
    intro c _; rw [legZ_eq_transpose_armZ]
  rw [e1, sum_swap_transpose μ (fun d => F (armZ μ.transpose d)),
      sum_armZ_generic μ.transpose F, ← sum_swap_transpose μ (fun d => F (d.2 : ℤ))]
  apply Finset.sum_congr rfl
  intro c _; simp only [Prod.snd_swap]

/-! ## Stage 4 — the separable reduction

`Σh² − Σcontent² = card + 2Σ(arm·leg) + 2Σ(i·j) + 2Σj + 2Σi`, the arm²/left² and
leg²/above² squares cancelling by the reflections. -/

theorem pieceA_reduction (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (hookZ μ c) ^ 2) - (∑ c ∈ μ.cells, (contentZ c) ^ 2)
    = (μ.cells.card : ℤ)
      + 2 * (∑ c ∈ μ.cells, armZ μ c * legZ μ c)
      + 2 * (∑ c ∈ μ.cells, ((c.1 : ℤ) * (c.2 : ℤ)))
      + 2 * (∑ c ∈ μ.cells, (c.2 : ℤ))
      + 2 * (∑ c ∈ μ.cells, (c.1 : ℤ)) := by
  have hsq_arm : ∑ c ∈ μ.cells, (armZ μ c) ^ 2 = ∑ c ∈ μ.cells, ((c.2 : ℤ)) ^ 2 :=
    sum_armZ_generic μ (fun x => x ^ 2)
  have hsq_leg : ∑ c ∈ μ.cells, (legZ μ c) ^ 2 = ∑ c ∈ μ.cells, ((c.1 : ℤ)) ^ 2 :=
    sum_legZ_generic μ (fun x => x ^ 2)
  have h_arm : ∑ c ∈ μ.cells, armZ μ c = ∑ c ∈ μ.cells, (c.2 : ℤ) :=
    sum_armZ_generic μ (fun x => x)
  have h_leg : ∑ c ∈ μ.cells, legZ μ c = ∑ c ∈ μ.cells, (c.1 : ℤ) :=
    sum_legZ_generic μ (fun x => x)
  have expand : ∀ c ∈ μ.cells,
      (hookZ μ c) ^ 2 - (contentZ c) ^ 2
      = ((armZ μ c) ^ 2 - ((c.2 : ℤ)) ^ 2) + ((legZ μ c) ^ 2 - ((c.1 : ℤ)) ^ 2)
        + 1 + 2 * (armZ μ c * legZ μ c) + 2 * ((c.1 : ℤ) * (c.2 : ℤ))
        + 2 * armZ μ c + 2 * legZ μ c := by
    intro c _; simp only [hookZ, contentZ]; ring
  rw [← Finset.sum_sub_distrib, Finset.sum_congr rfl expand]
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum,
    Finset.sum_const, nsmul_eq_mul, mul_one]
  rw [hsq_arm, hsq_leg, h_arm, h_leg]
  ring

/-! ## Stage 5 — Piece A from the pair-counting identity

The remaining combinatorial core is the **pair-counting identity**
`2Σ(arm·leg) + 2Σ(i·j) + 2A + 2L = card² − card` (bean `qou-o5xj`): the four terms
count, respectively, ordered UR/LL pairs, ordered UL/LR pairs, same-row and
same-column ordered pairs — together every ordered pair of distinct cells. Given
it, Piece A is immediate from the reduction. -/

/-- The pair-counting identity: the arm·leg, i·j, left and above sums account for
every ordered distinct-cell pair. Proof plan (bean `qou-o5xj`): express `armZ`/`legZ`
as `Finset.card` of arm/leg filters, expand the product to a triple sum
`Σ_c Σ_R Σ_B`, collapse the `c`-sum (`c = (R.1, B.2)` is forced) to
`#{(R,B) : R.1<B.1 ∧ B.2<R.2}`, likewise `Σ(i·j) = #{(A,L) UL/LR}`, then
`card²−card = Σ_{p,q}[p≠q]` split into the four disjoint position classes. -/
def PairCount (μ : YoungDiagram) : Prop :=
  2 * (∑ c ∈ μ.cells, armZ μ c * legZ μ c)
    + 2 * (∑ c ∈ μ.cells, ((c.1 : ℤ) * (c.2 : ℤ)))
    + 2 * (∑ c ∈ μ.cells, (c.2 : ℤ))
    + 2 * (∑ c ∈ μ.cells, (c.1 : ℤ))
  = (μ.cells.card : ℤ) ^ 2 - (μ.cells.card : ℤ)

/-- **Piece A, given the pair-counting identity.** `Σ hook² = Σ content² + n²`.
Fully sorry-free modulo the single `PairCount` hypothesis (bean `qou-o5xj`);
everything else — the reflections and the separable reduction — is machine-checked. -/
theorem pieceA_of_pairCount (μ : YoungDiagram) (hpc : PairCount μ) :
    ∑ c ∈ μ.cells, (hookZ μ c) ^ 2
    = (∑ c ∈ μ.cells, (contentZ c) ^ 2) + (μ.cells.card : ℤ) ^ 2 := by
  have hred := pieceA_reduction μ
  rw [PairCount] at hpc
  linarith [hred, hpc]

/-! ## Stage 6 — arm/leg as `Finset.card` of the arm/leg cell filters -/

/-- The arm length is the number of cells strictly right of `p` in its row. -/
theorem armZ_eq_card (μ : YoungDiagram) {p : ℕ × ℕ} (hp : p ∈ μ.cells) :
    armZ μ p = ((μ.cells.filter (fun R => R.1 = p.1 ∧ p.2 < R.2)).card : ℤ) := by
  have hlt : p.2 < μ.rowLen p.1 := (mem_cells_iff_snd_lt μ p).mp hp
  have hset : μ.cells.filter (fun R => R.1 = p.1 ∧ p.2 < R.2)
      = (Finset.Ioo p.2 (μ.rowLen p.1)).image (fun j => (p.1, j)) := by
    ext R
    simp only [Finset.mem_filter, Finset.mem_image, Finset.mem_Ioo]
    constructor
    · rintro ⟨hRc, hR1, hR2⟩
      exact ⟨R.2, ⟨hR2, by rw [← hR1]; exact (mem_cells_iff_snd_lt μ R).mp hRc⟩,
        by rw [← hR1]⟩
    · rintro ⟨j, ⟨hj1, hj2⟩, rfl⟩
      exact ⟨by rw [mem_cells_iff_snd_lt]; exact hj2, rfl, hj1⟩
  rw [hset, Finset.card_image_of_injective _ (fun a b h => by simpa using h),
    Nat.card_Ioo]
  simp only [armZ]
  omega

/-- The leg length is the number of cells strictly below `p` in its column. -/
theorem legZ_eq_card (μ : YoungDiagram) {p : ℕ × ℕ} (hp : p ∈ μ.cells) :
    legZ μ p = ((μ.cells.filter (fun B => B.2 = p.2 ∧ p.1 < B.1)).card : ℤ) := by
  have hlt : p.1 < μ.colLen p.2 := by
    have := μ.mem_iff_lt_colLen (i := p.1) (j := p.2)
    rw [YoungDiagram.mem_cells] at hp; simpa using this.mp (by simpa using hp)
  have hset : μ.cells.filter (fun B => B.2 = p.2 ∧ p.1 < B.1)
      = (Finset.Ioo p.1 (μ.colLen p.2)).image (fun i => (i, p.2)) := by
    ext B
    simp only [Finset.mem_filter, Finset.mem_image, Finset.mem_Ioo]
    constructor
    · rintro ⟨hBc, hB2, hB1⟩
      refine ⟨B.1, ⟨hB1, ?_⟩, ?_⟩
      · rw [← hB2]
        have := μ.mem_iff_lt_colLen (i := B.1) (j := B.2)
        rw [YoungDiagram.mem_cells] at hBc; simpa using this.mp (by simpa using hBc)
      · rw [← hB2]
    · rintro ⟨i, ⟨hi1, hi2⟩, rfl⟩
      refine ⟨?_, rfl, hi1⟩
      rw [YoungDiagram.mem_cells]
      have := μ.mem_iff_lt_colLen (i := i) (j := p.2)
      simpa using this.mpr hi2
  rw [hset, Finset.card_image_of_injective _ (fun a b h => by simpa using h),
    Nat.card_Ioo]
  simp only [legZ]
  omega

end QOU.BraidKnot.PieceA
