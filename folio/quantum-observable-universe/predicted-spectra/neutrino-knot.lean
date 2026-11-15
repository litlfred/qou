import QOU.Archimedean.ParticleKnots
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.Neutrino — Unknot K_{0₁} (trivial knot)

The neutrino is the unknot K_{0₁} with zero crossings, Seifert genus 0,
and trivial Jones polynomial J_ν(q) = 1.  It carries no topological mass;
neutrino mass comes entirely from vacuum drag.

LaTeX label: `def:neutrino-knot`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] Ch. 5, §neutrino-knot

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

noncomputable section
/-- The neutrino is electrically neutral (zero crossing chirality). -/
-- Ref: [leitner2026] Ch. 5, §neutrino-knot
theorem neutrino_neutral : ({} : Neutrino).charge = 0 := rfl

/-- The unknot has trivial genus. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem neutrino_genus_zero : ({} : Neutrino).genus = 0 := rfl

/-- The unknot has zero crossings. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem neutrino_crossing_zero : ({} : Neutrino).crossing_number = 0 := rfl

end

end QOU.Archimedean
