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

-- Ref: [leitner2026] docs/audits/2026-08-01-keystone-identity-I-piece-A-general-proof.md; bean qou-o5xj
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
every ordered distinct-cell pair. Proved sorry-free by `pairCount_holds` below
(bean `qou-o5xj` closed); the proof: express `armZ`/`legZ`
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
Modulo the single `PairCount` hypothesis — which is itself discharged
unconditionally by `pairCount_holds` (bean `qou-o5xj` closed), giving the
sorry-free unconditional `pieceA` below; everything else — the reflections and
the separable reduction — is machine-checked. -/
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

/-! ## Stage 7 — `Σ(arm·leg)` counts the UR/LL pair set

Each cell `p` contributes `arm(p)·leg(p)` = pairs (one arm cell `R`, one leg cell
`B`); the map `(p,R,B) ↦ (R,B)` bijects onto `{(R,B) : R.1<B.1 ∧ B.2<R.2}`, with
`p = (R.1, B.2)` recovered (always a cell). -/

/-- The UR/LL ordered pair set: `R` upper-right of `B`. -/
def urllPairs (μ : YoungDiagram) : Finset ((ℕ × ℕ) × (ℕ × ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun RB => RB.1.1 < RB.2.1 ∧ RB.2.2 < RB.1.2)

theorem sum_armLeg_eq_urll (μ : YoungDiagram) :
    (∑ p ∈ μ.cells, armZ μ p * legZ μ p) = ((urllPairs μ).card : ℤ) := by
  have step : ∀ p ∈ μ.cells, armZ μ p * legZ μ p
      = (((μ.cells.filter (fun R => R.1 = p.1 ∧ p.2 < R.2)) ×ˢ
          (μ.cells.filter (fun B => B.2 = p.2 ∧ p.1 < B.1))).card : ℤ) := by
    intro p hp
    rw [armZ_eq_card μ hp, legZ_eq_card μ hp, ← Nat.cast_mul, Finset.card_product]
  rw [Finset.sum_congr rfl step, ← Nat.cast_sum]
  congr 1
  rw [← Finset.card_biUnion]
  · congr 1
    ext RB
    simp only [Finset.mem_biUnion, Finset.mem_product, Finset.mem_filter, urllPairs]
    constructor
    · rintro ⟨p, hp, ⟨hRc, hR1, hR2⟩, ⟨hBc, hB2, hB1⟩⟩
      exact ⟨⟨hRc, hBc⟩, by omega, by omega⟩
    · rintro ⟨⟨hRc, hBc⟩, h1, h2⟩
      have hlt := (mem_cells_iff_snd_lt μ RB.1).mp hRc
      refine ⟨(RB.1.1, RB.2.2), ?_, ⟨hRc, rfl, h2⟩, ⟨hBc, rfl, h1⟩⟩
      rw [mem_cells_iff_snd_lt]
      show RB.2.2 < μ.rowLen RB.1.1
      omega
  · intro p hp q hq hpq
    simp only [Finset.disjoint_left, Finset.mem_product, Finset.mem_filter]
    rintro RB ⟨⟨_, hR1, _⟩, ⟨_, hB2, _⟩⟩ ⟨⟨_, hR1', _⟩, ⟨_, hB2', _⟩⟩
    exact hpq (Prod.ext (hR1.symm.trans hR1') (hB2.symm.trans hB2'))

/-! ## Stage 8 — `Σ(i·j)` counts the UL/LR pair set

For a Young diagram the up-left rectangle of any cell `p` is entirely filled
(down-closure), so `p.1·p.2` literally counts the cells strictly up-left of `p`.
Grouping those pairs by the lower-right corner gives `Σ(i·j) = |UL/LR pairs|` — no
rectangle-compensation needed. -/

/-- `p.1·p.2` counts the cells strictly up-left of `p` (all present by down-closure). -/
theorem prod_eq_card (μ : YoungDiagram) {p : ℕ × ℕ} (hp : p ∈ μ.cells) :
    (p.1 : ℤ) * (p.2 : ℤ) = ((μ.cells.filter (fun a => a.1 < p.1 ∧ a.2 < p.2)).card : ℤ) := by
  have hset : μ.cells.filter (fun a => a.1 < p.1 ∧ a.2 < p.2)
      = Finset.range p.1 ×ˢ Finset.range p.2 := by
    ext a
    simp only [Finset.mem_filter, Finset.mem_product, Finset.mem_range]
    constructor
    · rintro ⟨_, h1, h2⟩; exact ⟨h1, h2⟩
    · rintro ⟨h1, h2⟩
      refine ⟨?_, h1, h2⟩
      rw [YoungDiagram.mem_cells] at hp ⊢
      have : (a.1, a.2) ∈ μ := μ.up_left_mem (le_of_lt h1) (le_of_lt h2) hp
      simpa using this
  rw [hset, Finset.card_product, Finset.card_range, Finset.card_range, Nat.cast_mul]

/-- The UL/LR ordered pair set: `a` strictly up-left of `q`. -/
def ullrPairs (μ : YoungDiagram) : Finset ((ℕ × ℕ) × (ℕ × ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun aq => aq.1.1 < aq.2.1 ∧ aq.1.2 < aq.2.2)

theorem sum_prod_eq_ullr (μ : YoungDiagram) :
    (∑ p ∈ μ.cells, (p.1 : ℤ) * (p.2 : ℤ)) = ((ullrPairs μ).card : ℤ) := by
  have step : ∀ p ∈ μ.cells, (p.1 : ℤ) * (p.2 : ℤ)
      = (((μ.cells.filter (fun a => a.1 < p.1 ∧ a.2 < p.2)) ×ˢ ({p} : Finset (ℕ × ℕ))).card : ℤ) := by
    intro p hp
    rw [prod_eq_card μ hp, Finset.card_product, Finset.card_singleton, mul_one]
  rw [Finset.sum_congr rfl step, ← Nat.cast_sum]
  congr 1
  rw [← Finset.card_biUnion]
  · congr 1
    ext aq
    simp only [Finset.mem_biUnion, Finset.mem_product, Finset.mem_filter,
      Finset.mem_singleton, ullrPairs]
    constructor
    · rintro ⟨p, hp, ⟨hac, h1, h2⟩, rfl⟩
      exact ⟨⟨hac, hp⟩, h1, h2⟩
    · rintro ⟨⟨hac, hqc⟩, h1, h2⟩
      exact ⟨aq.2, hqc, ⟨hac, h1, h2⟩, rfl⟩
  · intro p hp q hq hpq
    simp only [Finset.disjoint_left, Finset.mem_product, Finset.mem_singleton]
    rintro aq ⟨_, rfl⟩ ⟨_, h⟩
    exact hpq h

/-! ## Stage 9 — same-row / same-column counts

`Σj = |{(L,q) : L.1=q.1 ∧ L.2<q.2}|` (same row, `L` left of `q`) and dually for
columns. The left-cell count of `q` is exactly `q.2` (contiguous row). -/

/-- `q.2` counts the cells strictly left of `q` in its row. -/
theorem snd_eq_card (μ : YoungDiagram) {q : ℕ × ℕ} (hq : q ∈ μ.cells) :
    (q.2 : ℤ) = ((μ.cells.filter (fun L => L.1 = q.1 ∧ L.2 < q.2)).card : ℤ) := by
  have hset : μ.cells.filter (fun L => L.1 = q.1 ∧ L.2 < q.2)
      = (Finset.range q.2).image (fun j => (q.1, j)) := by
    ext L
    simp only [Finset.mem_filter, Finset.mem_image, Finset.mem_range]
    constructor
    · rintro ⟨_, hL1, hL2⟩; exact ⟨L.2, hL2, by rw [← hL1]⟩
    · rintro ⟨j, hj, rfl⟩
      have hqlt : q.2 < μ.rowLen q.1 := (mem_cells_iff_snd_lt μ q).mp hq
      exact ⟨by rw [mem_cells_iff_snd_lt]; simp only; omega, rfl, hj⟩
  rw [hset, Finset.card_image_of_injective _ (fun a b h => by simpa using h),
    Finset.card_range]

/-- `q.1` counts the cells strictly above `q` in its column. -/
theorem fst_eq_card (μ : YoungDiagram) {q : ℕ × ℕ} (hq : q ∈ μ.cells) :
    (q.1 : ℤ) = ((μ.cells.filter (fun A => A.2 = q.2 ∧ A.1 < q.1)).card : ℤ) := by
  have hset : μ.cells.filter (fun A => A.2 = q.2 ∧ A.1 < q.1)
      = (Finset.range q.1).image (fun i => (i, q.2)) := by
    ext A
    simp only [Finset.mem_filter, Finset.mem_image, Finset.mem_range]
    constructor
    · rintro ⟨_, hA2, hA1⟩; exact ⟨A.1, hA1, by rw [← hA2]⟩
    · rintro ⟨i, hi, rfl⟩
      have hqlt : q.1 < μ.colLen q.2 := by
        have := μ.mem_iff_lt_colLen (i := q.1) (j := q.2)
        rw [YoungDiagram.mem_cells] at hq; simpa using this.mp (by simpa using hq)
      refine ⟨?_, rfl, hi⟩
      rw [YoungDiagram.mem_cells]
      have := μ.mem_iff_lt_colLen (i := i) (j := q.2)
      simpa using this.mpr (by omega)
  rw [hset, Finset.card_image_of_injective _ (fun a b h => by simpa using h),
    Finset.card_range]

/-- Same-row ordered pairs with the first cell strictly left. -/
def srLowerPairs (μ : YoungDiagram) : Finset ((ℕ × ℕ) × (ℕ × ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun Lq => Lq.1.1 = Lq.2.1 ∧ Lq.1.2 < Lq.2.2)

/-- Same-column ordered pairs with the first cell strictly above. -/
def scLowerPairs (μ : YoungDiagram) : Finset ((ℕ × ℕ) × (ℕ × ℕ)) :=
  (μ.cells ×ˢ μ.cells).filter (fun Aq => Aq.1.2 = Aq.2.2 ∧ Aq.1.1 < Aq.2.1)

theorem sum_snd_eq_srLower (μ : YoungDiagram) :
    (∑ q ∈ μ.cells, (q.2 : ℤ)) = ((srLowerPairs μ).card : ℤ) := by
  have step : ∀ q ∈ μ.cells, (q.2 : ℤ)
      = (((μ.cells.filter (fun L => L.1 = q.1 ∧ L.2 < q.2)) ×ˢ ({q} : Finset (ℕ × ℕ))).card : ℤ) := by
    intro q hq
    rw [snd_eq_card μ hq, Finset.card_product, Finset.card_singleton, mul_one]
  rw [Finset.sum_congr rfl step, ← Nat.cast_sum]
  congr 1
  rw [← Finset.card_biUnion]
  · congr 1
    ext Lq
    simp only [Finset.mem_biUnion, Finset.mem_product, Finset.mem_filter,
      Finset.mem_singleton, srLowerPairs]
    constructor
    · rintro ⟨q, hq, ⟨hLc, h1, h2⟩, rfl⟩; exact ⟨⟨hLc, hq⟩, h1, h2⟩
    · rintro ⟨⟨hLc, hqc⟩, h1, h2⟩; exact ⟨Lq.2, hqc, ⟨hLc, h1, h2⟩, rfl⟩
  · intro p hp q hq hpq
    simp only [Finset.disjoint_left, Finset.mem_product, Finset.mem_singleton]
    rintro Lq ⟨_, rfl⟩ ⟨_, h⟩; exact hpq h

theorem sum_fst_eq_scLower (μ : YoungDiagram) :
    (∑ q ∈ μ.cells, (q.1 : ℤ)) = ((scLowerPairs μ).card : ℤ) := by
  have step : ∀ q ∈ μ.cells, (q.1 : ℤ)
      = (((μ.cells.filter (fun A => A.2 = q.2 ∧ A.1 < q.1)) ×ˢ ({q} : Finset (ℕ × ℕ))).card : ℤ) := by
    intro q hq
    rw [fst_eq_card μ hq, Finset.card_product, Finset.card_singleton, mul_one]
  rw [Finset.sum_congr rfl step, ← Nat.cast_sum]
  congr 1
  rw [← Finset.card_biUnion]
  · congr 1
    ext Aq
    simp only [Finset.mem_biUnion, Finset.mem_product, Finset.mem_filter,
      Finset.mem_singleton, scLowerPairs]
    constructor
    · rintro ⟨q, hq, ⟨hAc, h1, h2⟩, rfl⟩; exact ⟨⟨hAc, hq⟩, h1, h2⟩
    · rintro ⟨⟨hAc, hqc⟩, h1, h2⟩; exact ⟨Aq.2, hqc, ⟨hAc, h1, h2⟩, rfl⟩
  · intro p hp q hq hpq
    simp only [Finset.disjoint_left, Finset.mem_product, Finset.mem_singleton]
    rintro Aq ⟨_, rfl⟩ ⟨_, h⟩; exact hpq h

/-! ## Stage 10 — the offDiag assembly: `PairCount`

`card² − card = |offDiag| = 2|urll| + 2|ullr| + 2|srLower| + 2|scLower|`, via the
pointwise identity that the 8 sign-classes (both orderings of UR/LL, UL/LR,
same-row, same-col) partition the off-diagonal, plus swap-reindexing to fold each
ordering pair into a factor of 2. -/

/-- Reindex a pair sum by `Prod.swap` (the cell-pair set is swap-symmetric). -/
theorem swap_reindex (μ : YoungDiagram) (f : (ℕ × ℕ) × (ℕ × ℕ) → ℤ) :
    (∑ pq ∈ μ.cells ×ˢ μ.cells, f pq.swap) = ∑ pq ∈ μ.cells ×ˢ μ.cells, f pq := by
  refine Finset.sum_bij' (fun pq _ => pq.swap) (fun pq _ => pq.swap) ?_ ?_ ?_ ?_ ?_
  · intro pq hpq; simpa [Finset.mem_product, and_comm] using hpq
  · intro pq hpq; simpa [Finset.mem_product, and_comm] using hpq
  · intro pq _; exact Prod.swap_swap pq
  · intro pq _; exact Prod.swap_swap pq
  · intro pq _; rfl

/-- **The pair-counting identity** (bean `qou-o5xj`). -/
theorem pairCount_holds (μ : YoungDiagram) : PairCount μ := by
  rw [PairCount, sum_armLeg_eq_urll, sum_prod_eq_ullr, sum_snd_eq_srLower,
    sum_fst_eq_scLower]
  -- turn each pair-set card into an indicator sum over cells ×ˢ cells
  have cast_card : ∀ P : (ℕ × ℕ) × (ℕ × ℕ) → Prop, ∀ _ : DecidablePred P,
      (((μ.cells ×ˢ μ.cells).filter P).card : ℤ)
        = ∑ pq ∈ μ.cells ×ˢ μ.cells, (if P pq then (1 : ℤ) else 0) := by
    intro P _
    simp only [Finset.card_filter, Nat.cast_sum, Nat.cast_ite, Nat.cast_one, Nat.cast_zero]
  rw [urllPairs, ullrPairs, srLowerPairs, scLowerPairs, cast_card, cast_card,
    cast_card, cast_card]
  -- RHS: card² − card = Σ indicator of the off-diagonal
  have hle : μ.cells.card ≤ μ.cells.card * μ.cells.card := by
    rcases Nat.eq_zero_or_pos μ.cells.card with h | h
    · simp [h]
    · exact Nat.le_mul_of_pos_left _ h
  have hoff : (μ.cells.card : ℤ) ^ 2 - (μ.cells.card : ℤ)
      = ∑ pq ∈ μ.cells ×ˢ μ.cells, (if pq.1 ≠ pq.2 then (1 : ℤ) else 0) := by
    have hcast : (∑ pq ∈ μ.cells ×ˢ μ.cells, (if pq.1 ≠ pq.2 then (1 : ℤ) else 0))
        = (((μ.cells ×ˢ μ.cells).filter (fun pq => pq.1 ≠ pq.2)).card : ℤ) := by
      simp only [Finset.card_filter, Nat.cast_sum, Nat.cast_ite, Nat.cast_one, Nat.cast_zero]
    rw [hcast]
    have heq : (μ.cells ×ˢ μ.cells).filter (fun pq => pq.1 ≠ pq.2) = μ.cells.offDiag := by
      ext pq
      simp only [Finset.mem_filter, Finset.mem_product, Finset.mem_offDiag]
      tauto
    rw [heq, Finset.offDiag_card, Nat.cast_sub hle]
    push_cast; ring
  rw [hoff]
  -- fold the swapped orderings and match pointwise
  have fold : ∀ P : (ℕ × ℕ) × (ℕ × ℕ) → Prop, ∀ _ : DecidablePred P,
      (2 : ℤ) * ∑ pq ∈ μ.cells ×ˢ μ.cells, (if P pq then (1 : ℤ) else 0)
        = ∑ pq ∈ μ.cells ×ˢ μ.cells,
            ((if P pq then (1 : ℤ) else 0) + (if P pq.swap then (1 : ℤ) else 0)) := by
    intro P _
    rw [Finset.sum_add_distrib, swap_reindex μ (fun pq => if P pq then (1 : ℤ) else 0), two_mul]
  rw [fold, fold, fold, fold, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib,
    ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro pq _
  obtain ⟨⟨a, c⟩, ⟨b, d⟩⟩ := pq
  simp only [Prod.swap, Prod.mk.injEq, ne_eq, not_and]
  by_cases hab : a = b <;> by_cases hcd : c = d <;>
    simp_all <;> split_ifs <;> omega

/-- **Piece A — general `n`, sorry-free** (bean `qou-o5xj` closed):
`Σ hook² = Σ content² + n²` for every Young diagram. -/
theorem pieceA (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, (hookZ μ c) ^ 2
    = (∑ c ∈ μ.cells, (contentZ c) ^ 2) + (μ.cells.card : ℤ) ^ 2 :=
  pieceA_of_pairCount μ (pairCount_holds μ)

end QOU.BraidKnot.PieceA
