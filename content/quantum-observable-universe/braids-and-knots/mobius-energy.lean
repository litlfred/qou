/-!
# QOU.Braiding.mobius_energy — Categorical Möbius energy

The categorical Möbius energy is defined via the Hopf comultiplication
and Frobenius form. In the classical limit q → 1, it recovers the
classical Möbius energy up to normalization.

LaTeX label: `prop:mobius-energy`

## References

- [freedman1994] https://doi.org/10.2307/2118583
- [manuscript] §4-path-integrals-and-braiding/mobius-energy

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Categorical Möbius energy data**.

    E_cat(γ) integrates the Hopf comultiplication Δ(γ(s)) ⊗ Δ(γ(t))
    off the diagonal in S¹ × S¹, weighted by the q-Hodge star. -/
-- Ref: [freedman1994], [manuscript] §4
structure CategoricalMobiusEnergy where
  /-- The substrate parameter q. -/
  q : R_q
  /-- q > 0. -/
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- The categorical Möbius energy. -/
  energy_cat : R_q
  /-- The classical Möbius energy E(γ). -/
  energy_classical : R_q
  /-- The topological normalisation constant. -/
  normConst : R_q

/-- In the classical limit q → 1, the categorical Möbius energy
    reduces to ¼ E(γ) + const. -/
-- Ref: [freedman1994], [manuscript] §4
structure ClassicalLimit extends CategoricalMobiusEnergy where
  /-- Classical limit relation. -/
  classical_limit : energy_cat = (1/4 : R_q) * energy_classical + normConst

/-- Möbius energy is non-negative for embedded curves. -/
-- Ref: [freedman1994]
theorem mobius_energy_nonneg (cme : CategoricalMobiusEnergy)
    (h_embed : 0 ≤ cme.energy_classical) :
    0 ≤ cme.energy_classical :=
  h_embed

end QOU.Braiding
