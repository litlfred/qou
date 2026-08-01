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

end QOU.BraidKnot.PieceA
