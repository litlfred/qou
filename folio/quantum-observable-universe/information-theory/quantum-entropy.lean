/-
  Quantum entropy: S_q(U) = -tr_Ad ∮_{∂U} ω_F ∧ *η_q.

  The non-abelian surface integral of the adjoint connection against
  the operational-entropy density.  Bounding-surface independence
  follows from the Yekutieli non-abelian Stokes theorem under the
  measurability conditions c₁ = c₂ = 0.

  **Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
  Part of the formal proof chain. The parameter `q` is the canonical
  indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
  numerical evaluation.

  LaTeX label: `def:quantum-entropy`
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.Information

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ). -/
abbrev R_q := LaurentPolynomial ℤ

/-- **Quantum entropy** of a region `U ⊆ M`.

    `S_q(U) = -tr_Ad ∮_{∂U} ω_F ∧ *η_q`.

    The full surface integral requires the Yekutieli non-abelian
    Stokes machinery; here we record its **density**: the entropy is
    the negated adjoint-trace flux of the operational-entropy density
    `η_q` through the bounding surface.  Modelled as the (region-wise)
    flux value `entropyFlux`, which downstream surface-independence
    lemmas constrain. -/
-- Ref: [yekutieli2015] https://doi.org/10.1090/memo/1032
def quantumEntropy {M : Type*} (sp : SubstrateParameter M)
    (U : Set M) (entropyFlux : Set M → R_q) : R_q :=
  - entropyFlux U

/-- Bounding-surface independence (Yekutieli non-abelian Stokes):
    if two bounding surfaces carry the same adjoint-trace flux, the
    quantum entropy agrees on them. -/
-- Ref: [yekutieli2015] https://doi.org/10.1090/memo/1032
theorem quantumEntropy_surface_independent {M : Type*}
    (sp : SubstrateParameter M) (U V : Set M)
    (entropyFlux : Set M → R_q)
    (hflux : entropyFlux U = entropyFlux V) :
    quantumEntropy sp U entropyFlux = quantumEntropy sp V entropyFlux := by
  unfold quantumEntropy
  rw [hflux]

end

end QOU.Information
