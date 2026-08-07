/-
  Closing `QOU.BraidKnot.numSYT_mul_hookProduct` — the bespoke Frame–Robinson–Thrall
  hook-length formula `#SYT(μ) · ∏_{c∈μ} h(c) = |μ|!`.

  This is the last open `sorry` of Identity-I program brick 1 (P2), and the single
  keystone whose closure cascades through `RSKBurnsideDischarge` to close
  `DeltaLambdaSignRule.burnside` (`Σ_λ (f^λ)² = n!`). It is **not** the famous HLF
  as an open problem: the geometric HLF is already proved sorry-free upstream as
  `QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct`, and the two SYT
  encodings are identified sorry-free by
  `QOU.BraidKnot.numSYT_eq_numStandardYoungTableaux`. What remains is a purely
  combinatorial *bridge of the two hook-length products*:

  * `QOU.BraidKnot.hookProduct μ` — `∏_{c∈μ} (armFilterCard + legFilterCard + 1)`,
    with arm/leg counted as `μ.cells.filter …` cardinalities
    (`StandardYoungTableau.hookLength`);
  * `YoungDiagram.hookLengthProduct μ` — `∏_{c∈μ} μ.hookLength c` with
    `μ.hookLength = μ.armLength + μ.legLength + 1`, `armLength = rowLen − j − 1`,
    `legLength = colLen − i − 1` (`HookLengthFormula`).

  The bridge is per-cell: the arm/leg filter cardinalities equal `rowLen i − j − 1`
  and `colLen j − i − 1` (each an `Ioo`-cardinality via a `Finset.card_bij` on the
  free column/row coordinate — the same technique as `IdentityAArmLeg.fiber_card`),
  so the two per-cell hook lengths agree and the products are equal.

  Import note: this must be a downstream leaf file — `SytMathlibBridge` (needed for
  `numSYT_eq_numStandardYoungTableaux`) imports `StandardYoungTableau`, so the proof
  cannot live in `StandardYoungTableau.lean` without a cycle.

  -- Ref: [sagan2001] Sagan, The Symmetric Group §3.10 (hook-length formula)
  -- Ref: [manuscript] docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md (P2)
-/
import QOU.BraidKnot.StandardYoungTableau
import QOU.BraidKnot.SytMathlibBridge
import QOU.Mathlib.HookLengthFormula

open Finset

namespace QOU.BraidKnot

variable {μ : YoungDiagram}

/-- The **arm** filter cardinality of `StandardYoungTableau.hookLength` equals the
`YoungDiagram.armLength` closed form `rowLen i − j − 1`: cells of `μ` in row `i`
strictly right of column `j` biject with `Ioo j (rowLen i)` via `c ↦ c.2`. -/
theorem armFilter_card (μ : YoungDiagram) (i j : ℕ) :
    (μ.cells.filter (fun c => c.1 = i ∧ j < c.2)).card = μ.rowLen i - j - 1 := by
  rw [← Nat.card_Ioo j (μ.rowLen i)]
  apply Finset.card_bij (fun c _ => c.2)
  · intro c hc
    simp only [Finset.mem_filter, YoungDiagram.mem_cells] at hc
    obtain ⟨hcell, hci, hcj⟩ := hc
    rw [Finset.mem_Ioo]
    refine ⟨hcj, ?_⟩
    have : (i, c.2) ∈ μ := by rw [← hci]; exact hcell
    exact (YoungDiagram.mem_iff_lt_rowLen).mp this
  · intro c hc c' hc' h
    simp only [Finset.mem_filter, YoungDiagram.mem_cells] at hc hc'
    obtain ⟨_, hci, _⟩ := hc
    obtain ⟨_, hci', _⟩ := hc'
    exact Prod.ext (hci.trans hci'.symm) h
  · intro b hb
    rw [Finset.mem_Ioo] at hb
    refine ⟨(i, b), ?_, rfl⟩
    simp only [Finset.mem_filter, YoungDiagram.mem_cells]
    exact ⟨(YoungDiagram.mem_iff_lt_rowLen).mpr hb.2, trivial, hb.1⟩

/-- The **leg** filter cardinality equals the `YoungDiagram.legLength` closed form
`colLen j − i − 1`: cells of `μ` in column `j` strictly below row `i` biject with
`Ioo i (colLen j)` via `c ↦ c.1`. -/
theorem legFilter_card (μ : YoungDiagram) (i j : ℕ) :
    (μ.cells.filter (fun c => c.2 = j ∧ i < c.1)).card = μ.colLen j - i - 1 := by
  rw [← Nat.card_Ioo i (μ.colLen j)]
  apply Finset.card_bij (fun c _ => c.1)
  · intro c hc
    simp only [Finset.mem_filter, YoungDiagram.mem_cells] at hc
    obtain ⟨hcell, hcj, hci⟩ := hc
    rw [Finset.mem_Ioo]
    refine ⟨hci, ?_⟩
    have : (c.1, j) ∈ μ := by rw [← hcj]; exact hcell
    exact (YoungDiagram.mem_iff_lt_colLen).mp this
  · intro c hc c' hc' h
    simp only [Finset.mem_filter, YoungDiagram.mem_cells] at hc hc'
    obtain ⟨_, hcj, _⟩ := hc
    obtain ⟨_, hcj', _⟩ := hc'
    exact Prod.ext h (hcj.trans hcj'.symm)
  · intro b hb
    rw [Finset.mem_Ioo] at hb
    refine ⟨(b, j), ?_, rfl⟩
    simp only [Finset.mem_filter, YoungDiagram.mem_cells]
    exact ⟨(YoungDiagram.mem_iff_lt_colLen).mpr hb.2, trivial, hb.1⟩

/-- Per-cell: the bespoke `StandardYoungTableau.hookLength` equals the
`YoungDiagram.hookLength` (both are `arm + leg + 1`; the arm/leg counts match by
`armFilter_card` / `legFilter_card`). -/
theorem hookLength_eq (μ : YoungDiagram) (i j : ℕ) :
    hookLength μ i j = μ.hookLength i j := by
  rw [hookLength, armFilter_card, legFilter_card, YoungDiagram.hookLength,
    YoungDiagram.armLength, YoungDiagram.legLength]

/-- The two hook-length products agree. -/
theorem hookProduct_eq_hookLengthProduct (μ : YoungDiagram) :
    hookProduct μ = μ.hookLengthProduct := by
  rw [hookProduct, YoungDiagram.hookLengthProduct]
  exact Finset.prod_congr rfl (fun c _ => hookLength_eq μ c.1 c.2)

/-- **Frame–Robinson–Thrall hook-length formula** for the bespoke SYT count,
now proved (closes the brick-1 `sorry` in `StandardYoungTableau.lean`):
`#SYT(μ) · ∏_{c∈μ} h(c) = |μ|!`. Composes the geometric HLF
(`numStandardYoungTableaux_mul_hookLengthProduct`), the SYT-encoding identity
(`numSYT_eq_numStandardYoungTableaux`), and the hook-product bridge above. -/
theorem numSYT_mul_hookProduct_proved (μ : YoungDiagram) :
    numSYT μ * hookProduct μ = (μ.cells.card).factorial := by
  rw [numSYT_eq_numStandardYoungTableaux, hookProduct_eq_hookLengthProduct]
  exact QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct μ

end QOU.BraidKnot
