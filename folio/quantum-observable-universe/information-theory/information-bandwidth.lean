import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs
import Mathlib.Tactic.Ring


/-!
# QOU.Information.informationBandwidth — Information bandwidth per Planck time

The information bandwidth 𝔅(q) := q·η_q / (q - 1)² is the
Bremermann-analog bit budget of the substrate: the maximum number of
distinguishable q-bits one Planck step carries across the light-cone
boundary.  It is the product of the speed of light c_q = 1/(q - 1),
the iteration count n_R(q) = 1/ℏ_q, and the operational entropy η_q.

LaTeX label: `def:information-bandwidth`

## Base ring (AGENTS.md §7c)

Stated over a bare `CommRing R`.  The only division in the formula is by
`(q - 1)²`, so `q - 1` is carried as a **unit** `u : Rˣ` pinned by
`↑u = q - 1`; the speed of light is then `c_q = ↑u⁻¹` and the bandwidth
is the division-free product `q · η · (↑u⁻¹)²`.  Over a field with
`q ≠ 1` take `u = Units.mk0 (q - 1) _`, recovering the previous
`[Field k]` statement; the factorisation lemma below then needs neither
`field_simp` nor the `q ≠ 0` / `q - 1 ≠ 0` side conditions — it is a
`ring` identity.

## References
- [leitner2026] §9/information-bandwidth
-/

namespace QOU.Information

/-- **Information bandwidth** per Planck time at substrate parameter q.

    𝔅(q) := q · η_q / (q - 1)²

    The product of the speed of light c_q = 1/(q - 1), the iteration
    count n_R(q) = 1/ℏ_q, and the operational entropy η_q per fibre. -/
-- Ref: [leitner2026] §9/information-bandwidth
def informationBandwidth {R : Type*} [CommRing R]
    (q η : R) (u : Rˣ) (_hu : (u : R) = q - 1) : R :=
  q * η * (↑u⁻¹ : R) ^ 2

/-- The information bandwidth factors as c_q · n_R · η, with
    c_q = 1/(q - 1) = `↑u⁻¹` the speed of light and
    n_R = 1/ℏ_q = q/(q-1) = `q · ↑u⁻¹`. -/
-- Ref: [leitner2026] §9/information-bandwidth
theorem informationBandwidth_eq_factored {R : Type*} [CommRing R]
    (q η : R) (u : Rˣ) (hu : (u : R) = q - 1) :
    informationBandwidth q η u hu = (↑u⁻¹ : R) * (q * (↑u⁻¹ : R)) * η := by
  -- Ref: [leitner2026] §9/information-bandwidth
  unfold informationBandwidth
  ring

end QOU.Information
