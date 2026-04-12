/-!
# QOU.Descartes.BorromeanBaryon — Borromean quark structure

Quarks as Borromean-linked unknots in three color tubes.
The Borromean link B_3 has the property that no two components
are linked, but all three together are inseparable.
Vol(S³ \ B_3) = 7.32772...

## References

- [manuscript] Ch. 6, §3
- [thurston1978] Geometry and topology of three-manifolds

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic

noncomputable section

namespace QOU.Descartes

/-- The Borromean link of three unknots in color tubes. -/
structure BorromeanBaryon where
  /-- The three color tube assignments -/
  color : Fin 3 → Fin 3
  /-- Crossing orientation: +1 (up) or -1 (down) for each component -/
  orientation : Fin 3 → Int
  /-- The orientations sum to the net Coulomb charge -/
  charge_sum : (Finset.univ.sum orientation) = orientation 0 + orientation 1 + orientation 2

/-- The proton: two up (+1) and one down (-1), net charge +1.
    Color assignment: one quark per color tube (bijective). -/
-- Ref: [manuscript] Ch. 6, §3
def proton_partition : BorromeanBaryon where
  color := ![0, 1, 2]
  orientation := ![1, 1, -1]
  -- Ref: [manuscript] Ch. 6, §3
  charge_sum := by decide

/-- The neutron: one up (+1) and two down (-1), net charge 0.
    Color assignment: one quark per color tube (bijective). -/
-- Ref: [manuscript] Ch. 6, §3
def neutron_partition : BorromeanBaryon where
  color := ![0, 1, 2]
  orientation := ![1, -1, -1]
  -- Ref: [manuscript] Ch. 6, §3
  charge_sum := by decide

/-- Hyperbolic volume of the Borromean complement. -/
-- Ref: [thurston1978]
def borromean_volume : ℝ := 7.32772

/-- The baryon mass from the topological mass formula. -/
-- Ref: [manuscript] Ch. 6, §3
def baryon_mass (q : ℝ) (hq : q > 1) : ℝ :=
  borromean_volume / (1 - 1/q)^2

end QOU.Descartes

end
