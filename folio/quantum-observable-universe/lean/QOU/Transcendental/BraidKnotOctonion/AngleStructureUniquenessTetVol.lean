import BraidKnotOctonion.AngleStructureUniqueness
import QOU.Transcendental.BraidKnotOctonion.IdealTetrahedronVolumeConcave

/-!
# Rivin uniqueness for the single ideal tetrahedron

Transcendental companion of `BraidKnotOctonion/AngleStructureUniqueness.lean` (strangler split,
bean `qou-dk7p`). The generic uniqueness mechanism stays outside the boundary; its instantiation
to the Lobachevsky volume `tetVol` lives here.

-- Ref: [rivin2003] Rivin, Combinatorial optimization in geometry, Adv. Appl. Math. (2003), arXiv:math/9907032, Thm 1.4
-/

namespace QOU.Knot.AngleStructureUniqueness

/-! ## Instantiation: the single ideal tetrahedron -/

open QOU.Archimedean in
/-- **Rivin Thm 1.4 for the single ideal tetrahedron.** The Lobachevsky volume
`tetVol` of an ideal tetrahedron has **at most one** maximiser on the open angle
simplex `tetSimplex`.  Discharged sorry-free from the strict concavity
`tetVol_strictConcaveOn` (bean `qou-idvt` T3-plumbing) via the generic
uniqueness mechanism above — the analytic half of `qou-krvm` (ii) for the
one-tetrahedron anchor. -/
theorem tetVol_maximizer_unique {p q : ℝ × ℝ}
    (hpK : p ∈ tetSimplex) (hp : ∀ z ∈ tetSimplex, tetVol z ≤ tetVol p)
    (hqK : q ∈ tetSimplex) (hq : ∀ z ∈ tetSimplex, tetVol z ≤ tetVol q) : p = q :=
  strictConcaveOn_maximizer_unique tetVol_strictConcaveOn hpK hp hqK hq

end QOU.Knot.AngleStructureUniqueness
