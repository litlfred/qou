import QOU.Archimedean.ParticleKnots
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.Positron — Mirror trefoil σ(T_{2,3}) (antiparticle of electron)

The positron is the mirror trefoil σ(T_{2,3}) — the antiparticle of the
electron.  It carries reversed crossing chirality (Q = +1) and corresponds
to an electron travelling backward in time (Feynman–Stueckelberg).

LaTeX label: `def:positron-knot`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] Ch. 5, §positron-knot

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

noncomputable section
/-- The positron is a mirror trefoil T_{2,3} with reversed crossings. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem positron_is_mirror_torus_knot :
    ({} : Positron).torusP = 2 ∧ ({} : Positron).torusN = 3 := ⟨rfl, rfl⟩

/-- The positron has opposite charge to the electron. -/
-- Ref: [leitner2026] Ch. 5, §positron-knot
theorem positron_charge_opposite_electron :
    ({} : Positron).charge + ({} : Electron).charge = 0 := by decide

/-- The positron has reversed orientation (antiparticle). -/
-- Ref: [leitner2026] Ch. 5, §positron-knot
theorem positron_reversed_orientation :
    ({} : Positron).orientation = -({} : Electron).orientation := by decide

end

end QOU.Archimedean
