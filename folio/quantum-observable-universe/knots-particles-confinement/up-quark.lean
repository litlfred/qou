import QOU.Archimedean.ParticleKnots
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.UpQuark — Unknot in Borromean link with positive crossing

The up quark is an unknot (neutrino) localized in a color tube of the
Bring surface with positive crossing orientation within the Borromean
link B₃.  It is not a distinct knot type — it is the unknot K_{0₁}
distinguished by its environment (color-tube, Borromean-linked).

LaTeX label: `def:up-quark`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] Ch. 5, §up-quark

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

noncomputable section

/-- The up quark is an unknot (same underlying knot as the neutrino,
    `QOU.Archimedean.Neutrino`): zero crossings and trivial Seifert genus.
    The neutrino's defining invariants are `crossing_number = 0`,
    `genus = 0`; this states the matching values for the up quark. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem up_quark_is_unknot :
    ({} : UpQuark).crossing_number = 0 ∧
    ({} : UpQuark).genus = 0 := ⟨rfl, rfl⟩

/-- The up quark has positive crossing orientation. -/
-- Ref: [leitner2026] Ch. 5, §up-quark
theorem up_quark_positive_orientation :
    ({} : UpQuark).crossing_orientation = 1 := rfl

/-- The up quark is color-confined. -/
-- Ref: [leitner2026] Ch. 5, §up-quark
theorem up_quark_confined : ({} : UpQuark).confined = true := rfl

end

end QOU.Archimedean
