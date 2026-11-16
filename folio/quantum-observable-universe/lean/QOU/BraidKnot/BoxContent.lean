import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring
import QOU.MathlibExt.YoungDiagramCells

/-!
# QOU.BraidKnot.BoxContent — box content, and what it is NOT

Former carrier for `prop:content-scaling-correspondence`
(`mass-theory/content-scaling-correspondence.md`), and the record of why that
block was re-worded.

Until 2026-09-04 the block's mathematical sentence read: *"by q-Schur–Weyl
duality `V^{⊗n} ≅ ⊕_λ V_λ ⊗ S_λ`, the content `c = j − i` of a box at position
`(i,j)` equals the magnetic quantum number `m_j` of the corresponding `SU_q(2)`
weight space"*, and this file held only the definition `boxContent`, so the
block's `lean.ref` resolved while the proposition itself had no Lean
(bean `qou-59x9`, audit
`docs/audits/2026-09-04-lean-ref-resolution-count-mass-theory.md`). The
theorems below refute that sentence; on the owner's go (bean `qou-kpx7`) the
block now states the true fact — content is the `q`-Jucys–Murphy eigenvalue
exponent, `QOU.SchurWeyl.SeminormalRep.seminormalRep_qJM` — and its `lean.ref`
names that theorem. The scaling table moved to `rem:content-scaling-dictionary`.

**Formalised here: the sentence is false in its literal reading**, and the
obstruction is structural, not numerical. For `SU(2)` the shapes are two-row,
`λ = (a, b)` with `b ≤ a`, and `V_λ` has spin `j = (a − b)/2`, so its weights
are `m` with `2m ∈ {−(a−b), −(a−b)+2, …, a−b}` — `a − b + 1` of them — while
`λ` has `a + b` cells.

* `twoRow_card_cells_ne_card_weights` — `a + b ≠ a − b + 1` for every `a b : ℕ`
  (it would need `2b = 1`). So no bijection "box ↔ weight space" exists for
  any shape at all; "the corresponding weight space" names nothing.
* `top_content_not_weight` — for `3 ≤ a + b` the cell `(0, a−1)` has content
  `a − 1`, and `2(a−1) > a − b`, so that content is not a weight of `V_λ`
  under **any** assignment of boxes to weight spaces.
* `single_box_content_not_weight`, `column_content_not_weight` — the two
  shapes with `n ≤ 2` other than `(2,0)` fail as well (`(1,0)` by parity,
  `(1,1)` by range). `row_two_contents_are_weights` — `(2,0)` is the one shape
  where every content is a weight, and it is the only one.

What **is** true, and is corpus infrastructure already: box contents are the
(q-)Jucys–Murphy eigenvalues (`QOU.SchurWeyl.QJucysMurphyEigen`), i.e. they
track the *total-spin increments* of the sub-tower `V^{⊗k}`, `k ≤ n` — a
Casimir datum, not a weight. The consumer
`crystal-isospin-degeneracy-proof` uses only `c(·)` as a cell statistic and
content *differences* (`axialDistance`), which this refutation does not touch.

`boxContent` is kept (it is what the manifest names) and bridged by `rfl` to
the canonical `QOU.MathlibExt.YoungDiagramCells.content`, so nothing proved
against the one copy is unreachable from the other (bean `qou-cdup`).

Base ring: everything is over `ℕ`/`ℤ`; no archimedean construct (§7c).
-/

namespace QOU.BraidKnot

/-- A cell in a Young diagram, parameterized by `(row, col)` (0-indexed). -/
structure Cell where
  row : ℕ
  col : ℕ
deriving DecidableEq, Repr

/-- The content `c = j - i` of a box at position `(i,j)` in a Young diagram.

    This is the q-Jucys–Murphy eigenvalue datum of the box. It is **not** the
    magnetic quantum number of an `SU_q(2)` weight space — see the module
    header and `top_content_not_weight` below. -/
def boxContent (x : Cell) : ℤ :=
  (x.col : ℤ) - (x.row : ℤ)

/-- `boxContent` is the canonical cell content (`qou-cdup` single home). -/
theorem boxContent_eq_content (x : Cell) :
    boxContent x = QOU.MathlibExt.YoungDiagramCells.content (x.row, x.col) := rfl

/-! ## Two-row shapes and `SU(2)` weights, over `ℤ` (twice the weight) -/

/-- Twice the spin of `V_λ` for the two-row shape `λ = (a, b)`: `2j = a − b`. -/
def twoRowTwiceSpin (a b : ℕ) : ℤ := (a : ℤ) - (b : ℤ)

/-- `m2` is twice a weight of `V_{(a,b)}`: `|m2| ≤ 2j` and `m2 ≡ 2j (mod 2)`.
    Stated without `abs` so that `omega` can discharge every instance. -/
def IsTwoRowWeight (a b : ℕ) (m2 : ℤ) : Prop :=
  -(twoRowTwiceSpin a b) ≤ m2 ∧ m2 ≤ twoRowTwiceSpin a b ∧
    (m2 - twoRowTwiceSpin a b) % 2 = 0

/-- Number of cells of `(a, b)` versus number of weights of `V_{(a,b)}`:
    `a + b ≠ (a − b) + 1`, always. There is no bijection "box ↔ weight space"
    for any two-row shape, so "the corresponding weight space" of a box is
    not defined. -/
theorem twoRow_card_cells_ne_card_weights (a b : ℕ) :
    ((a : ℤ) + b) ≠ twoRowTwiceSpin a b + 1 := by
  unfold twoRowTwiceSpin
  omega

/-- The rightmost cell of the first row, `(0, a−1)`, has content `a − 1`; for
    `3 ≤ a + b` twice that exceeds `2j = a − b`, so it is not a weight of
    `V_{(a,b)}` — under any assignment of boxes to weight spaces. -/
theorem top_content_not_weight {a b : ℕ} (hab : b ≤ a) (h3 : 3 ≤ a + b) :
    ¬ IsTwoRowWeight a b (2 * boxContent ⟨0, a - 1⟩) := by
  unfold IsTwoRowWeight twoRowTwiceSpin boxContent
  simp only
  omega

/-- `λ = (1)`: the single box has content `0`, but `V_{(1)}` has spin `1/2`
    and its weights are `±1/2`; `0` fails by parity. -/
theorem single_box_content_not_weight :
    ¬ IsTwoRowWeight 1 0 (2 * boxContent ⟨0, 0⟩) := by
  unfold IsTwoRowWeight twoRowTwiceSpin boxContent
  simp only
  omega

/-- `λ = (1,1)`: the lower box has content `−1`, but `V_{(1,1)}` is the
    trivial representation with the single weight `0`. -/
theorem column_content_not_weight :
    ¬ IsTwoRowWeight 1 1 (2 * boxContent ⟨1, 0⟩) := by
  unfold IsTwoRowWeight twoRowTwiceSpin boxContent
  simp only
  omega

/-- `λ = (2)` is the one shape on which every content is a weight: contents
    `0, 1` inside the spin-1 weights `−1, 0, 1`. -/
theorem row_two_contents_are_weights :
    IsTwoRowWeight 2 0 (2 * boxContent ⟨0, 0⟩) ∧
    IsTwoRowWeight 2 0 (2 * boxContent ⟨0, 1⟩) := by
  unfold IsTwoRowWeight twoRowTwiceSpin boxContent
  simp only
  omega

/-! ## Uniqueness of `(2, 0)` and axial-distance shift invariance (`qou-59x9`) -/

/-- **Complete classification of non-empty two-row shapes (`qou-59x9`).**
For any non-empty two-row diagram `λ = (a, b)` (`b ≤ a`, `1 ≤ a + b`), if merely the
corner cell `(0, 0)`, the second-row lead `(1, 0)` (when `b = 1`), and the top-row
tail `(0, a - 1)` have contents that are `SU(2)` weights of `V_{(a,b)}`, then
`(a, b) = (2, 0)` is forced. Together with `row_two_contents_are_weights`, this proves
`(2, 0)` is the unique non-empty two-row shape whose box contents all lie in the weight
set of `V_{(a,b)}`. -/
theorem twoRow_all_weights_forces_two_zero {a b : ℕ} (hab : b ≤ a) (hpos : 1 ≤ a + b)
    (h00 : IsTwoRowWeight a b (2 * boxContent ⟨0, 0⟩))
    (h10 : b = 1 → IsTwoRowWeight a b (2 * boxContent ⟨1, 0⟩))
    (htop : IsTwoRowWeight a b (2 * boxContent ⟨0, a - 1⟩)) :
    a = 2 ∧ b = 0 := by
  unfold IsTwoRowWeight twoRowTwiceSpin boxContent at h00 h10 htop
  simp only at h00 h10 htop
  by_cases hb1 : b = 1
  · have h10' := h10 hb1
    omega
  · omega

/-- Transposing a cell `(row, col) ↦ (col, row)` negates its content:
`boxContent ⟨x.col, x.row⟩ = -boxContent x`. -/
theorem boxContent_transpose_neg (x : Cell) :
    boxContent ⟨x.col, x.row⟩ = -boxContent x := by
  rcases x with ⟨r, c⟩
  unfold boxContent
  dsimp only
  omega

/-- The axial distance `c(y) - c(x)` between two cells `x, y` in a Young diagram
(the quantity consumed by Hoefsmit matrix entries and `crystal-isospin-degeneracy-proof`). -/
def axialDistance (x y : Cell) : ℤ :=
  boxContent y - boxContent x

/-- Diagonal shifts `(i, j) ↦ (i + k, j + k)` preserve `boxContent` and `axialDistance`
identically, explaining why `crystal-isospin-degeneracy-proof` depends only on cell
content differences rather than on the refuted weight-space identification (`qou-59x9`). -/
theorem axialDistance_shift_invariant (x y : Cell) (k : ℕ) :
    axialDistance ⟨x.row + k, x.col + k⟩ ⟨y.row + k, y.col + k⟩ =
      axialDistance x y := by
  rcases x with ⟨rx, cx⟩
  rcases y with ⟨ry, cy⟩
  unfold axialDistance boxContent
  dsimp only
  omega

end QOU.BraidKnot
