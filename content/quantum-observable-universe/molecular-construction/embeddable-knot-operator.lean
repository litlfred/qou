/-
# QOU.Molecular.EmbeddableKnotOperator

Generic embeddable knot operator with geometric overlap weighting, for
content block `def:embeddable-knot-operator`.

A knot operator embedded into the ambient 3-manifold carries an overlap
weight `w ∈ (0, 1]` set by its embedding direction relative to the Reeb
axis: axial (σ-type, Reeb-aligned) channels have `w = 1`; transverse
(π-type, contact-plane) channels have `w < 1`. The embedded binding
contribution is `baseBinding * w`, and the binding of a composite is the
overlap-weighted sum.

Archimedean specialisation over ℝ (CLAUDE.md §7c): bindings and weights
are real energies, with the ordering hypotheses `0 < w` and `w ≤ 1`.
-/
import Mathlib

namespace QOU.Molecular

/-- A knot operator embedded into the ambient 3-manifold with a geometric
overlap weight `w ∈ (0, 1]`. Axial (σ-type, Reeb-aligned) channels have
`overlapWeight = 1`; transverse (π-type, contact-plane) channels have
`overlapWeight < 1`. -/
structure EmbeddableKnotOperator where
  /-- Un-embedded channel binding (energy units). -/
  baseBinding : ℝ
  /-- Geometric overlap weight set by the embedding direction. -/
  overlapWeight : ℝ
  /-- The overlap weight is positive: the channel binds. -/
  weight_pos : 0 < overlapWeight
  /-- The overlap weight does not exceed the axial (head-on) maximum. -/
  weight_le_one : overlapWeight ≤ 1

namespace EmbeddableKnotOperator

/-- Embedded binding contribution: base binding scaled by the overlap weight. -/
def binding (op : EmbeddableKnotOperator) : ℝ :=
  op.baseBinding * op.overlapWeight

/-- An axial (σ-type) operator: Reeb-aligned, full head-on overlap `w = 1`. -/
def axial (baseBinding : ℝ) : EmbeddableKnotOperator where
  baseBinding := baseBinding
  overlapWeight := 1
  weight_pos := one_pos
  weight_le_one := le_refl 1

/-- A transverse (π-type) operator with lateral overlap `0 < w ≤ 1`. -/
def transverse (baseBinding w : ℝ) (hw : 0 < w) (hw1 : w ≤ 1) :
    EmbeddableKnotOperator where
  baseBinding := baseBinding
  overlapWeight := w
  weight_pos := hw
  weight_le_one := hw1

end EmbeddableKnotOperator

/-- Overlap-weighted total binding of a composite of embeddable operators. -/
def totalBinding (ops : List EmbeddableKnotOperator) : ℝ :=
  (ops.map EmbeddableKnotOperator.binding).sum

end QOU.Molecular
