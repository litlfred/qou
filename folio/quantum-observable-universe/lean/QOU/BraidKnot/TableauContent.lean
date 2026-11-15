/-
# Cell content and axial distance — the SYT geometry layer

Infra 1 (bean `qou-ujfg`) of the YT seminormal-sum Mathlib-gap program. Mathlib
carries `YoungDiagram` and `SemistandardTableau` but **no** cell-content / axial-
distance apparatus and **no** standard-tableau seminormal representation. The
seminormal character sum

  χ_λ(σ) = Σ_{T ∈ SYT(λ)}  a_{ρ(T)},   ρ(T) = axial distance of the boxes of i, i+1

needs the **axial distance** `ρ` between two cells — the difference of their
*contents* `c(i,j) = j − i`. This file supplies that layer and ties it to the
Infra-2 weight layer (`SeminormalWeight`): the axial-distance antisymmetry
`ρ(a,b) = −ρ(b,a)` composes with the pairing identity `g_ρ + g_{−ρ} = 1` to give
the box-pair pairing `g_{ρ(a,b)} + g_{ρ(b,a)} = 1` — the cell-geometry statement of
why a reduced-weight sum over a swap-symmetric tableau set is an integer `c_λ`.

Base ring (§7c): `content`/`axialDistance` are `ℤ`-valued combinatorics (no ring);
the weight tie is over a generic `[Field R]`. No archimedean structure.

-- Ref: [sagan2001] The Symmetric Group, §3.3 (contents, axial distance, seminormal form)
-/
import Mathlib.Tactic
import QOU.BraidKnot.SeminormalWeight

namespace QOU.BraidKnot.TableauContent

/-- **Content of a cell** `(i, j)`: column index minus row index, `c(i,j) = j − i`.
    Cells on the same diagonal share a content; it is the seminormal-form
    coordinate of a box.

    Overlap note (reuse audit): `QOU.IwahoriHecke.Hoefsmit.content (i j : ℕ)` carries
    the same `j − i` formula in two-argument shape. This file keeps the *pair*-shaped
    version deliberately — it is a lightweight foundational brick (imports only
    `Mathlib.Tactic` + the weight layer), whereas `Hoefsmit` sits on the heavy
    `Wedderburn`/`Matrix.Charpoly` cone. The correct consolidation direction is to
    extract this pair primitive here and have `Hoefsmit` depend on it, not to pull
    the heavy cone into the combinatorial base; tracked as a follow-up, not done in
    this PR to avoid coupling the brick to `Hoefsmit`'s dependencies. -/
def content (cell : ℕ × ℕ) : ℤ := (cell.2 : ℤ) - (cell.1 : ℤ)

/-- **Axial distance** between two cells: the difference of their contents. For the
    boxes holding `i` and `i+1` in a standard tableau this is the `ρ` of the
    seminormal weight `a_ρ`. -/
def axialDistance (a b : ℕ × ℕ) : ℤ := content b - content a

@[simp] theorem content_row_step (i j : ℕ) :
    content (i, j + 1) = content (i, j) + 1 := by simp [content]; ring

@[simp] theorem content_col_step (i j : ℕ) :
    content (i + 1, j) = content (i, j) - 1 := by simp [content]; ring

/-- Cells on the same diagonal (shifted by `(k,k)`) share a content. -/
theorem content_diag (i j k : ℕ) : content (i + k, j + k) = content (i, j) := by
  simp only [content]; push_cast; ring

/-- **Axial distance is antisymmetric**: `ρ(a,b) = −ρ(b,a)`. This is the
    cell-geometry root of the seminormal ρ ↔ −ρ pairing — swapping the two boxes
    (the `i ↔ i+1` transposition acting on a standard tableau) negates `ρ`. -/
theorem axialDistance_antisymm (a b : ℕ × ℕ) :
    axialDistance a b = -axialDistance b a := by simp [axialDistance]

@[simp] theorem axialDistance_self (a : ℕ × ℕ) : axialDistance a a = 0 := by
  simp [axialDistance]

open SeminormalWeight in
/-- **Box-pair pairing** — the cell-geometry form of `g_ρ + g_{−ρ} = 1`. For two
    off-diagonal cells (`q^{2·ρ(a,b)} ≠ 1`, i.e. `a`, `b` not on the same
    diagonal in the sense that makes the weight degenerate), the reduced
    seminormal weights at the two orientations of the pair sum to `1`. Composing
    Infra 1 (`axialDistance_antisymm`) with Infra 2 (`reducedWeight_add_neg`):
    each off-diagonal box pair contributes exactly `1` to the reduced-weight sum,
    which is *why* `χ_λ(σ)/h = c_λ ∈ ℤ`. -/
theorem reducedWeight_pair {R : Type*} [Field R] (q : R) (a b : ℕ × ℕ)
    (hq : q ≠ 0) (hx : q ^ (2 * axialDistance a b) ≠ 1) :
    reducedWeight q (axialDistance a b) + reducedWeight q (axialDistance b a) = 1 := by
  rw [axialDistance_antisymm b a]
  exact reducedWeight_add_neg q (axialDistance a b) hq hx

end QOU.BraidKnot.TableauContent
