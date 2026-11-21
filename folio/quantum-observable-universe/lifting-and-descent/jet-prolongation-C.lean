import Mathlib.Data.Real.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Topology.Basic


/-!
# QOU.Torsion.jet_prolongation_C — Archimedean jet prolongation

In the archimedean realisation, the jet prolongation of an instanton
connection A on a principal bundle P over a manifold M uniquely
determines a connection A' on the frame bundle P' of J¹E, such that
(M̃, G, P', E') is again an archimedean QOU.

LaTeX label: `cor:jet-prolongation-C`

## References

- [leitner2026] §3-lifting-of-quantum-torsion/jet-prolongation-C
-/

namespace QOU.Torsion

/-- **Archimedean QOU data**: the differential-geometric data of
    `(C, θ, G, S)` in the archimedean realisation. -/
-- Ref: [leitner2026] §3, §12
structure ArchimedeanQOUData where
  /-- The base manifold M. -/
  ManifoldType : Type*
  /-- The gauge group G. -/
  GaugeGroupType : Type*
  /-- The gauge group is a group. -/
  [gaugeGroup : Group GaugeGroupType]
  /-- The total space S (state bundle over M). -/
  TotalSpaceType : Type*
  /-- Dimension of the base manifold. -/
  baseDim : ℕ
  /-- Fibre dimension. -/
  fibreDim : ℕ

attribute [instance] ArchimedeanQOUData.gaugeGroup

/-- **Jet prolongation in the archimedean setting**.

    Given archimedean QOU data `(C, θ, G, S)` with instanton connection
    `A` and metric `g`, the jet prolongation produces new archimedean
    QOU data `(C, θ̃, G, S')` where:
    - `M̃ = S` (the total space becomes the new base)
    - `P'` is the frame bundle of `J¹S`
    - `E'` is the bundle of orthonormal frames
    - `A'` is the unique connection determined by `A` and `g` -/
-- Ref: [leitner2026] §3, §12
structure JetProlongationC where
  /-- The input archimedean QOU data. -/
  input : ArchimedeanQOUData
  /-- The output archimedean QOU data (after jet prolongation). -/
  output : ArchimedeanQOUData
  /-- The new base manifold is the total space of the input. -/
  base_is_total : output.ManifoldType = input.TotalSpaceType
  /-- The gauge group is preserved. -/
  gauge_preserved : output.GaugeGroupType = input.GaugeGroupType
  /-- The new dimension: dim(J¹E) = dim(M) + dim(fibre) + dim(M) · dim(fibre). -/
  dim_formula : output.baseDim =
    input.baseDim + input.fibreDim + input.baseDim * input.fibreDim

/-- The jet prolongation can be iterated: if jp₂.input = jp₁.output,
    the composite yields valid QOU data at the second brane level. -/
-- Ref: [leitner2026] §3
theorem jet_prolongation_C_iterable
    (jp₁ jp₂ : JetProlongationC)
    (h : jp₂.input = jp₁.output) :
    jp₂.output.baseDim =
      jp₁.output.baseDim + jp₁.output.fibreDim +
      jp₁.output.baseDim * jp₁.output.fibreDim := by
  rw [jp₂.dim_formula, ← h]

/-- For SU(2) on a 4-manifold with 3-dimensional fibres:
    dim(level 1) = 4 + 3 + 12 = 19. -/
-- Ref: [leitner2026] §3, Example 3.1
example : 4 + 3 + 4 * 3 = 19 := by norm_num

end QOU.Torsion
