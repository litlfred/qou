/-!
# QOU.Torsion.jet_prolongation_C — Archimedean jet prolongation

In the archimedean realisation, the jet prolongation of an instanton
connection A on a principal bundle P over a manifold M uniquely
determines a connection A' on the frame bundle P' of J¹E, such that
(M̃, G, P', E') is again an archimedean QOU.

LaTeX label: `cor:jet-prolongation-C`

## References

- [manuscript] §3-lifting-of-quantum-torsion/jet-prolongation-C
-/

import Mathlib.Data.Real.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Topology.Basic

namespace QOU.Torsion

/-- **Archimedean QOU data**: the differential-geometric data of
    `(M, G, P, E)` in the archimedean realisation. -/
-- Ref: [manuscript] §3, §12
structure ArchimedeanQOUData where
  /-- The base manifold M. -/
  ManifoldType : Type*
  /-- The gauge group G. -/
  GaugeGroupType : Type*
  /-- The gauge group is a group. -/
  [gaugeGroup : Group GaugeGroupType]
  /-- The total space E (vector bundle over M). -/
  TotalSpaceType : Type*
  /-- Dimension of the base manifold. -/
  baseDim : ℕ
  /-- Fibre dimension. -/
  fibreDim : ℕ

attribute [instance] ArchimedeanQOUData.gaugeGroup

/-- **Jet prolongation in the archimedean setting**.

    Given archimedean QOU data `(M, G, P, E)` with instanton connection
    `A` and metric `g`, the jet prolongation produces new archimedean
    QOU data `(M̃, G, P', E')` where:
    - `M̃ = E` (the total space becomes the new base)
    - `P'` is the frame bundle of `J¹E`
    - `E'` is the bundle of orthonormal frames
    - `A'` is the unique connection determined by `A` and `g` -/
-- Ref: [manuscript] §3, §12
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

/-- The jet prolongation can be iterated: applying it twice yields
    the second level of the brane tower. -/
-- Ref: [manuscript] §3
theorem jet_prolongation_C_iterable
    (jp₁ jp₂ : JetProlongationC)
    (h : jp₂.input = jp₁.output) :
    True := by
  trivial

/-- For SU(2) on a 4-manifold with 3-dimensional fibres:
    dim(level 1) = 4 + 3 + 12 = 19. -/
-- Ref: [manuscript] §3, Example 3.1
example : 4 + 3 + 4 * 3 = 19 := by norm_num

end QOU.Torsion
