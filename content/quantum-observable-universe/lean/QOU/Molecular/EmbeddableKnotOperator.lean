/-
# QOU.Molecular.EmbeddableKnotOperator

Generic embeddable knot operator with geometric overlap weighting, for
content block `def:embeddable-knot-operator`.

A knot operator embedded into the ambient 3-manifold carries an overlap
weight `w ∈ (0, 1]` set by its embedding direction relative to the bond
axis: axial (σ-type) channels have `w = 1`; transverse (π-type) channels
have `w < 1`. The embedded binding contribution is `baseBinding * w`, and
the binding of a composite is the overlap-weighted sum.

Archimedean specialisation over ℝ (AGENTS.md §7c): bindings and weights
are real energies, with the ordering hypotheses `0 < w` and `w ≤ 1`.
-/
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.LinearAlgebra.Dimension.Finite

namespace QOU.Molecular

/-- A knot operator embedded into the ambient 3-manifold with a geometric
overlap weight `w ∈ (0, 1]`. Axial (σ-type) channels have
`overlapWeight = 1`; transverse (π-type) channels have `overlapWeight < 1`. -/
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

/-- An axial (σ-type) operator: full head-on overlap `w = 1`. -/
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

/-- An axial channel binds at its full base binding (`w = 1`). -/
@[simp] theorem axial_binding (b : ℝ) : (axial b).binding = b := by
  simp [binding, axial]

/-- A transverse channel binds at `base · w`. -/
@[simp] theorem transverse_binding (b w : ℝ) (hw : 0 < w) (hw1 : w ≤ 1) :
    (transverse b w hw hw1).binding = b * w := by
  simp [binding, transverse]

end EmbeddableKnotOperator

/-- Overlap-weighted total binding of a composite of embeddable operators. -/
def totalBinding (ops : List EmbeddableKnotOperator) : ℝ :=
  (ops.map EmbeddableKnotOperator.binding).sum

/-- An order-`(m+1)` bond: one axial σ channel and `m` transverse π channels. -/
def multipleBond (baseσ w : ℝ) (m : ℕ) (hw : 0 < w) (hw1 : w ≤ 1) :
    List EmbeddableKnotOperator :=
  EmbeddableKnotOperator.axial baseσ ::
    List.replicate m (EmbeddableKnotOperator.transverse baseσ w hw hw1)

/-- The channel count of an order-`(m+1)` bond is `m+1` — the bond order —
independent of the overlap weight `w`: weighting changes only the energy. -/
@[simp] theorem multipleBond_length (baseσ w : ℝ) (m : ℕ) (hw : 0 < w) (hw1 : w ≤ 1) :
    (multipleBond baseσ w m hw hw1).length = m + 1 := by
  simp [multipleBond]

/-- Order-`(m+1)` bond energy: `baseσ · (1 + m·w)`. For `w = 1` (equal
channels) this is `baseσ · (m+1)`; a lateral weight `w < 1` reduces it. -/
theorem multipleBond_binding (baseσ w : ℝ) (m : ℕ) (hw : 0 < w) (hw1 : w ≤ 1) :
    totalBinding (multipleBond baseσ w m hw hw1) = baseσ * (1 + m * w) := by
  simp only [totalBinding, multipleBond, List.map_cons, List.map_replicate,
    List.sum_cons, List.sum_replicate, EmbeddableKnotOperator.axial_binding,
    EmbeddableKnotOperator.transverse_binding, nsmul_eq_mul]
  ring

/-- **Spatial-dimension bound.** In `ℝ³` a family of pairwise-orthogonal
nonzero vectors has at most three members: orthogonal nonzero vectors are
linearly independent, and a linearly independent family in a space of
`finrank` 3 has cardinality `≤ 3`. Embedding bond channels as mutually
orthogonal directions, the number of channels — the bond order — is capped
by the spatial dimension, so no bond exceeds order three. -/
theorem orthogonal_channels_le_dim
    {ι : Type*} [Fintype ι] (v : ι → EuclideanSpace ℝ (Fin 3))
    (hne : ∀ i, v i ≠ 0)
    (horth : Pairwise (fun i j => @inner ℝ _ _ (v i) (v j) = 0)) :
    Fintype.card ι ≤ 3 := by
  have hli : LinearIndependent ℝ v :=
    linearIndependent_of_ne_zero_of_inner_eq_zero hne horth
  have hcard := hli.fintype_card_le_finrank
  rwa [finrank_euclideanSpace_fin] at hcard

end QOU.Molecular
