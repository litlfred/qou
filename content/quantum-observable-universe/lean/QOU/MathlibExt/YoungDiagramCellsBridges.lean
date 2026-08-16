import QOU.MathlibExt.YoungDiagramCells
import QOU.BraidKnot.IdentityAArmLeg
import QOU.BraidKnot.TableauContent
import QOU.BraidKnot.JucysMurphy
import QOU.BraidKnot.PieceAGeneral
import QOU.MathlibExt.QPartitionCombinatorics
import QOU.MathlibExt.WenzlSchurElement
import QOU.BraidKnot.TwoFiltrationBridge

/-!
# Bridges from the scattered cell statistics onto the single home

Bean `qou-cdup`. `QOU.MathlibExt.YoungDiagramCells` is the one home for
`content` / `arm` / `leg` / `hook`; this file connects the pre-existing copies
to it, so a lemma proved against one is usable against any other.

## Why bridges rather than a migration

Deleting each local definition and rewriting its call sites would touch proofs
in six modules at once. These lemmas are **purely additive** — no existing file
changes — and they are what a later migration would rewrite along. They also
*test* a claim I had so far only asserted, in a bean and two commit messages,
namely that every copy is definitionally equal so every bridge is `rfl`.

## What the test found

**Thirteen bridges land: twelve by `rfl`, one conditional. Two copies cannot be
bridged at all.** Broken down, because a single number here would hide the two
different things being counted — *content* copies, and *arm/leg/hook* copies:

| | reachable | `rfl` |
|---|---|---|
| `content` copies (8 in the tree) | **6** | 6 |
| `arm` / `leg` / `hook` copies (2 sets) | 2 | 6 lemmas |
| `hookLength` (ℕ-valued) | 1 | **no** — needs `c ∈ μ` |

The blanket claim I had been repeating — *"eight copies, each a `rfl` bridge"* —
was wrong in both directions:

* **Two copies are unreachable.** `QOU.BraidsAndKnots.cellContent`
  (`mass-theory/y-lambda-recipe-from-partition.lean`) and
  `QOU.BraidKnot.cellContent`
  (`mass-theory/jucys-murphy-central-elements-qou.lean`) live in **standalone
  content-block siblings**, not library modules, so nothing can import them.
  The second is additionally the clash partner from the `cdup` record — it
  shares a fully-qualified name with a library declaration — so it is
  *unbridgeable by construction*: importing both is the very error the bridge
  would have to survive.
* **`hookLength` is not `rfl`.** `TwoFiltrationBridge.hookLength` is valued in
  `ℕ` with truncated subtraction, so it agrees with the `ℤ`-valued `hook` only
  **on cells of the diagram** — off-diagram the ℕ version saturates at `0`
  while the ℤ version goes negative. It is a real lemma with a hypothesis, and
  recording it as "a `rfl` bridge" would have been wrong.

So the honest count for the migration is: six free, one conditional, two
requiring the sibling to be promoted to a library module first.
-/

namespace QOU.MathlibExt.YoungDiagramCells

/-! ### The six free bridges

Each is `rfl`: the definitions are syntactically identical up to binder name. -/

theorem content_eq_identityAArmLeg (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.IdentityAArmLeg.content c := rfl

theorem content_eq_tableauContent (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.TableauContent.content c := rfl

theorem content_eq_jucysMurphy (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.JucysMurphy.cellContent c := rfl

theorem content_eq_pieceA (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.PieceA.contentZ c := rfl

/-- The curried copies take `(i j : ℕ)` rather than a pair, so the bridge is
stated at the uncurried point. Still `rfl`. -/
theorem content_eq_qPartitionCombinatorics (i j : ℕ) :
    content (i, j) = QOU.MathlibExt.QPartitionCombinatorics.cellContent i j := rfl

theorem content_eq_wenzlSchurElement (i j : ℕ) :
    content (i, j) = QOU.MathlibExt.WenzlSchurElement.cellContent i j := rfl

/-! ### Arm, leg and hook -/

theorem arm_eq_identityAArmLeg (μ : YoungDiagram) (c : ℕ × ℕ) :
    arm μ c = QOU.BraidKnot.IdentityAArmLeg.arm μ c := rfl

theorem leg_eq_identityAArmLeg (μ : YoungDiagram) (c : ℕ × ℕ) :
    leg μ c = QOU.BraidKnot.IdentityAArmLeg.leg μ c := rfl

theorem hook_eq_identityAArmLeg (μ : YoungDiagram) (c : ℕ × ℕ) :
    hook μ c = QOU.BraidKnot.IdentityAArmLeg.hook μ c := rfl

theorem arm_eq_pieceA (μ : YoungDiagram) (c : ℕ × ℕ) :
    arm μ c = QOU.BraidKnot.PieceA.armZ μ c := rfl

theorem leg_eq_pieceA (μ : YoungDiagram) (c : ℕ × ℕ) :
    leg μ c = QOU.BraidKnot.PieceA.legZ μ c := rfl

theorem hook_eq_pieceA (μ : YoungDiagram) (c : ℕ × ℕ) :
    hook μ c = QOU.BraidKnot.PieceA.hookZ μ c := rfl

/-! ### The one conditional bridge

`hookLength` is `ℕ`-valued with truncated subtraction, so it agrees with `hook`
only where the cell is actually in the diagram. This is the lemma my earlier
"every bridge is `rfl`" claim mis-described. -/

theorem hook_eq_hookLength {μ : YoungDiagram} {c : ℕ × ℕ} (hc : c ∈ μ) :
    hook μ c = (QOU.BraidKnot.TwoFiltrationBridge.hookLength μ c : ℤ) := by
  have hj : c.2 < μ.rowLen c.1 := (YoungDiagram.mem_iff_lt_rowLen).mp hc
  have hi : c.1 < μ.colLen c.2 := (YoungDiagram.mem_iff_lt_colLen).mp hc
  simp only [hook, arm, leg, QOU.BraidKnot.TwoFiltrationBridge.hookLength]
  omega

end QOU.MathlibExt.YoungDiagramCells
