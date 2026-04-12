/-!
# QOU.AlgebraicSubstrate.QChebyshevFunction

The q-Chebyshev function — partial sum of the q-von Mangoldt function
over maximal ideals with bounded norm.
LaTeX: `\label{def:q-chebyshev-function}`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The q-Chebyshev function ψ_q(X).

    Sums the q-von Mangoldt weights Λ_q(𝔪) over all maximal ideals
    𝔪 ∈ MaxSpec(𝒪_q(ℬ)) with N(𝔪) ≤ X.

    NOTE: Depends on QVonMangoldtFunction which requires evaluation
    over ℝ. This definition is deferred to the evaluation layer. -/
-- noncomputable def QChebyshevFunction
--     (hbar_q : R_q) (hbar_pos : 0 < hbar_q)
--     (ideals : List MaxIdeal) (X : R_q) : R_q :=
--   (ideals.filter (fun m => decide (m.norm ≤ X))).foldl
--     (fun acc m => acc + QVonMangoldtFunction hbar_q hbar_pos m) 0

end QOU.AlgebraicSubstrate
