import QOU.Mathlib.HookLengthFormula
import QOU.BraidKnot.SYTEncodingBridgeTwo
import QOU.BraidKnot.PieceAGeneral

/-!
# QOU.BraidKnot.HookProductHLF — the FRT hook-length formula in the `BraidKnot` register

This file discharges the **brick-1 target** `numSYT μ * hookProduct μ = |μ|!` — the
Frame–Robinson–Thrall hook-length formula stated over `QOU.BraidKnot`'s own
`StandardYoungTableau` / `hookLength` definitions — **sorry-free**, by composing three
already-proved pieces:

1. `QOU.BraidKnot.SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux` (proved in
   `QOU.BraidKnot.SYTEncodingBridgeTwo`) —
   the tableau-count bridge `numSYT μ = numStandardYoungTableaux μ` (`BraidKnot` SYT ≃
   Mathlib-register SYT).
2. `hookProduct_eq_hookLengthProduct` (**proved below**) — the *hook* bridge
   `hookProduct μ = μ.hookLengthProduct`, i.e. `BraidKnot`'s `Finset.filter`-counted
   arm/leg equals the geometric `rowLen`/`colLen` arm/leg of `QOU.Mathlib`.
3. `QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct` — the geometric HLF,
   itself proved from the list-form Novelli–Pak–Stoyanovskii identity
   `SYTEnum.numSYTenum_mul_prodHooks`.

Only piece 2 was missing; it is the content of this file, and it reduces to the two
`Finset.card` computations already proved in `QOU.BraidKnot.PieceAGeneral`
(`armZ_eq_card`, `legZ_eq_card`), which identify the arm/leg *filters* with
`Finset.Ioo` images.

## Why this file rather than an in-place proof

`QOU.Mathlib.HookLengthFormula` transitively imports `QOU.BraidKnot.StandardYoungTableau`
(via `QOU.BraidKnot.SpechtClassification → Specht → StandardYoungTableau`), so the HLF is
**not** available where `numSYT_mul_hookProduct` was originally stated. The statement
therefore moves downstream to this leaf module, where the import is legal. Nothing
consumed the original `sorry`ed declaration (every other occurrence in the corpus was a
docstring/roadmap mention), so the move costs no consumer updates.
-/

namespace QOU.BraidKnot.HookProductHLF

open Finset YoungDiagram

/-- **Arm bridge.** For a genuine cell `(i, j) ∈ μ`, the `Finset.filter` count of cells
strictly to the right of `(i, j)` in row `i` — `BraidKnot`'s arm — equals the geometric
arm length `μ.rowLen i - j - 1`. -/
theorem armCard_eq_armLength (μ : YoungDiagram) {i j : ℕ} (h : (i, j) ∈ μ) :
    (μ.cells.filter (fun c => c.1 = i ∧ j < c.2)).card = μ.armLength i j := by
  have hcell : ((i, j) : ℕ × ℕ) ∈ μ.cells := by simpa using h
  have hZ := QOU.BraidKnot.PieceA.armZ_eq_card μ hcell
  have hj : j < μ.rowLen i := mem_iff_lt_rowLen.mp h
  have : ((μ.cells.filter (fun c => c.1 = i ∧ j < c.2)).card : ℤ)
      = (μ.armLength i j : ℤ) := by
    rw [← hZ]
    simp only [QOU.BraidKnot.PieceA.armZ, YoungDiagram.armLength]
    omega
  exact_mod_cast this

/-- **Leg bridge.** For a genuine cell `(i, j) ∈ μ`, the `Finset.filter` count of cells
strictly below `(i, j)` in column `j` — `BraidKnot`'s leg — equals the geometric leg
length `μ.colLen j - i - 1`. -/
theorem legCard_eq_legLength (μ : YoungDiagram) {i j : ℕ} (h : (i, j) ∈ μ) :
    (μ.cells.filter (fun c => c.2 = j ∧ i < c.1)).card = μ.legLength i j := by
  have hcell : ((i, j) : ℕ × ℕ) ∈ μ.cells := by simpa using h
  have hZ := QOU.BraidKnot.PieceA.legZ_eq_card μ hcell
  have hi : i < μ.colLen j := mem_iff_lt_colLen.mp h
  have : ((μ.cells.filter (fun c => c.2 = j ∧ i < c.1)).card : ℤ)
      = (μ.legLength i j : ℤ) := by
    rw [← hZ]
    simp only [QOU.BraidKnot.PieceA.legZ, YoungDiagram.legLength]
    omega
  exact_mod_cast this

/-- **The hook bridge, cellwise.** On a genuine cell the two hook-length definitions agree:
`BraidKnot`'s filter-counted `arm + leg + 1` is the geometric `armLength + legLength + 1`. -/
theorem hookLength_eq (μ : YoungDiagram) {i j : ℕ} (h : (i, j) ∈ μ) :
    QOU.BraidKnot.StandardYoungTableau.hookLength μ i j = μ.hookLength i j := by
  rw [QOU.BraidKnot.StandardYoungTableau.hookLength, YoungDiagram.hookLength,
    armCard_eq_armLength μ h, legCard_eq_legLength μ h]

/-- **The hook bridge.** The two hook-length *products* over `μ`'s cells agree. -/
theorem hookProduct_eq_hookLengthProduct (μ : YoungDiagram) :
    QOU.BraidKnot.hookProduct μ = μ.hookLengthProduct := by
  rw [QOU.BraidKnot.hookProduct, YoungDiagram.hookLengthProduct]
  refine Finset.prod_congr rfl (fun c hc => ?_)
  have : (c.1, c.2) ∈ μ := by simpa using hc
  exact hookLength_eq μ this

/-- **Frame–Robinson–Thrall hook-length formula** in the `QOU.BraidKnot` register,
**sorry-free**:

  `#SYT(μ) · ∏_{c ∈ μ} h(c) = |μ|!`,

equivalently `f^μ = |μ|! / ∏ h(c)`. Stated multiplicatively so it lives over `ℕ`
(`hookProduct_pos` makes the division form well-posed).

This is the brick-1 target formerly carried as a cited `sorry` in
`QOU.BraidKnot.StandardYoungTableau`; it is now discharged by composing the tableau-count
bridge, the hook bridge above, and the proved geometric HLF. -/
theorem numSYT_mul_hookProduct (μ : YoungDiagram) :
    QOU.BraidKnot.numSYT μ * QOU.BraidKnot.hookProduct μ = (μ.card).factorial := by
  rw [QOU.BraidKnot.SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux,
    hookProduct_eq_hookLengthProduct]
  exact QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct μ

end QOU.BraidKnot.HookProductHLF
