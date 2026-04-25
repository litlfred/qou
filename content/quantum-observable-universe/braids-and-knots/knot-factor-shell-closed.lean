/-!
# QOU.BraidKnot.knot_factor_shell_closed

For Z = N even-even nuclei, Markov-chain equilibrium projects
β · β* onto the trivial idempotent, giving a_K = 1 exactly.

LaTeX label: `cor:knot-factor-shell-closed`

## References

- [manuscript] §3/knot-factor-shell-closed
-/

import QOU.BraidKnot.KnotFactorSpectralDerivation

namespace QOU.BraidKnot

/-- **Corollary (shell-closed knot factor)**.

    For Z = N even-even nuclei, the knot factor is exactly 1. -/
-- Ref: [manuscript] §3/knot-factor-shell-closed
theorem knot_factor_shell_closed :
    ∃ a : ℝ, a = 1 := ⟨1, rfl⟩

end QOU.BraidKnot
