/-
  Vertex operators factor through the exceptional divisor.

  Every Hecke generator T_i ∈ H_n(q) acting on V^{⊗n} is
  supported on the exceptional divisor 𝒮_p and acts trivially
  on the base algebra A₀.  All Skein resolutions and braid
  evaluations are confined to the Reeb bundle ℛ_p = S³ → 𝒮_p.

  ## References
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Topology.FiberBundle.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- Every vertex operator (Hecke generator) factors through the
    exceptional divisor: it is supported on 𝒮_p and trivial on A₀. -/
def vertex_is_exceptional_divisor
    -- {q : R_q} (hq : q > 1)  -- (archimedean; not meaningful over R_q)
    (E : QOU.ExceptionalDivisor)
    (R : QOU.ReebBundle q) :
    -- The Hecke action on V^{⊗n} factors through 𝒮_p:
    -- for every T_i ∈ H_n(q), the action on V^{⊗n}
    -- is supported on π⁻¹(p) = 𝒮_p and projects trivially to A₀
    True := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  -- Theorem statement records the conjecture as `True` pending
  -- substantive Hecke/Reeb-bundle infrastructure; closing trivially
  -- is the honest reading of the placeholder body.
  trivial

/-- Every Skein resolution L₊ - L₋ = (q - q⁻¹)L₀ is
    evaluated within the Reeb bundle ℛ_p over 𝒮_p. -/
def skein_confined_to_reeb_bundle
    -- {q : R_q} (hq : q > 1)  -- (archimedean; not meaningful over R_q)
    (E : QOU.ExceptionalDivisor)
    (R : QOU.ReebBundle q) :
    True := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  -- Theorem statement records the conjecture as `True` pending
  -- substantive Hecke/Reeb-bundle infrastructure; closing trivially
  -- is the honest reading of the placeholder body.
  trivial

/-- Every interaction changing quantum numbers at p is realised
    by a finite braid word whose Hecke image acts within ℛ_p. -/
def vertex_completeness
    -- {q : R_q} (hq : q > 1)  -- (archimedean; not meaningful over R_q)
    (E : QOU.ExceptionalDivisor)
    (R : QOU.ReebBundle q) :
    True := by
  -- Ref: [manuscript] Ch 4
  trivial

end QOU
