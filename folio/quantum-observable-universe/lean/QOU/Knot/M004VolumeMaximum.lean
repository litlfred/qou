import QOU.Knot.MultiTetVolumeConcave
import QOU.Archimedean.LobachevskyMaximum

/-!
# QOU.Knot.M004VolumeMaximum — the regular point IS the m004 volume maximiser

Bean `qou-krvm` (iv), m004 half.

`MultiTetVolumeConcave.m004Vol_maximizer_unique` proves the m004 volume
functional `totalVol` has **at most one** maximiser on the m004 angle polytope.
Uniqueness alone is vacuous without existence. This file supplies existence and
names the maximiser: it is the regular point `(π/3, π/3)²`, two regular ideal
tetrahedra.

The argument is per-tetrahedron. `totalVol` on `Fin 2` is the sum of two
`tetVol` blocks, and Milnor's theorem in the corpus's analytic form
(`IdealTetrahedronConcavity.volChart_isMaxOn_regular`) says each block is
maximised over its own open simplex at `(π/3, π/3)`. The m004 polytope is a
subset of the product of the two simplices, and the regular point lies in it
(`m004_regular_mem`), so the product maximum is attained inside the polytope.
**The edge equation and the m004 symmetry group play no role**: the regular
point maximises each tetrahedron independently and happens to satisfy the gluing
equation. That is why this anchor closes without `optima_coincide`; it is not
true for L6a4, whose symmetric point gives each tetrahedron angles
`(π/4, π/4, π/2)`, which is not the per-tetrahedron maximum.

**What this is not.** `tetVol` is DEFINED as the Lobachevsky sum; that it is the
hyperbolic volume of the ideal tetrahedron is `qou-idvt` T2, open. So the value
`2·Cl₂(π/3)` below is the maximum of the analytic functional, not a proof that
`Vol(4₁) = 2·Cl₂(π/3)`.

Archimedean (ℝ).

-- Ref: [rivin1994] https://doi.org/10.2307/2118572 (volume maximisation on the
--      angle-structure polytope)
-/

namespace QOU.Knot.M004VolumeMaximum

open QOU.Archimedean QOU.Knot.MultiTetVolumeConcave
open QOU.Archimedean.IdealTetrahedronConcavity

/-- The regular point of the m004 polytope: two regular ideal tetrahedra. -/
noncomputable def regularPoint : Fin 2 → ℝ × ℝ :=
  ![(Real.pi / 3, Real.pi / 3), (Real.pi / 3, Real.pi / 3)]

/-- Each block of the m004 volume is at most the regular tetrahedron's. -/
theorem tetVol_le_regular {p : ℝ × ℝ} (hp : p ∈ tetSimplex) :
    tetVol p ≤ tetVol ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) :=
  volChart_isMaxOn_regular hp

/-- **Existence: the regular point maximises the m004 volume functional** on the
m004 angle polytope. -/
theorem regularPoint_isMax :
    ∀ z ∈ m004Polytope, totalVol z ≤ totalVol regularPoint := by
  intro z hz
  simp only [totalVol, Fin.sum_univ_two, regularPoint, Matrix.cons_val_zero,
    Matrix.cons_val_one]
  exact add_le_add (tetVol_le_regular (hz.1 0)) (tetVol_le_regular (hz.1 1))

/-- **Existence and uniqueness together.** A point of the m004 polytope maximises
`totalVol` there if and only if it is the regular point. The `←` direction is
`regularPoint_isMax`; the `→` direction is `m004Vol_maximizer_unique`, which the
existence result makes non-vacuous. -/
theorem isMax_iff_regular {p : Fin 2 → ℝ × ℝ} (hpK : p ∈ m004Polytope) :
    (∀ z ∈ m004Polytope, totalVol z ≤ totalVol p) ↔ p = regularPoint := by
  constructor
  · intro hp
    exact m004Vol_maximizer_unique hpK hp m004_regular_mem regularPoint_isMax
  · rintro rfl
    exact regularPoint_isMax

/-- The maximum value is `2·Cl₂(π/3)` — twice the regular tetrahedron's
Lobachevsky sum (`volChart_max_value`). A value of the analytic functional only;
see the module docstring. -/
theorem totalVol_regularPoint :
    totalVol regularPoint = 2 * QOU.Archimedean.Cl_2 (Real.pi / 3) := by
  have h : tetVol ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) = QOU.Archimedean.Cl_2 (Real.pi / 3) :=
    volChart_max_value
  simp only [totalVol, Fin.sum_univ_two, regularPoint, Matrix.cons_val_zero,
    Matrix.cons_val_one, h]
  ring

end QOU.Knot.M004VolumeMaximum
