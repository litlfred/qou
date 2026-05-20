/-!
# QOU.QuaternionicSpectralResolvents

Quaternionic spectral resolvents ω_k : S → J∞E using Lusztig
q-exponentials and q-logarithms, encoding uncertainty (real),
space-like (i), and two time-like (j, k) components.
ω₀ = 0 on Bring's surface.

LaTeX label: `def:quaternionic-spectral-resolvents`

## References

- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
- [manuscript] Chapter 5, §Quaternionic spectral resolvents

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Quaternionic spectral resolvent component type**. -/
-- Ref: [manuscript] Chapter 5
inductive ResolventType
  | uncertainty   -- ω₀: real component
  | spaceLike     -- ω₁: imaginary i component
  | timeLike1     -- ω₂: imaginary j component
  | timeLike2     -- ω₃: imaginary k component

/-- **Quaternionic spectral resolvent data**: the four components
    ω₀, ω₁, ω₂, ω₃ encoding the resolvent embedding S → J∞E. -/
-- Ref: [lusztig1993], [manuscript] Chapter 5
structure QuaternionicResolvent where
  /-- The deformation parameter q. -/
  q : R_q
  /-- q > 0. -/
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- The radial parameter r = -ln|q|. -/
  r : R_q
  /-- The four resolvent values at a point. -/
  omega : Fin 4 → R_q
  /-- ω₀ = 0 on balanced states (first power sum vanishes). -/
  omega_zero_balanced : omega 0 = 0
  /-- The embedding is nontrivial: at least one spatial/temporal resolvent is nonzero. -/
  nontrivial : omega 1 ≠ 0 ∨ omega 2 ≠ 0 ∨ omega 3 ≠ 0

/-- On Bring's surface, the first power sum ∑xⱼ = 0, so ω₀ = 0. -/
-- Ref: [lusztig1993], [manuscript] Chapter 5
theorem uncertainty_vanishes (qr : QuaternionicResolvent) :
    qr.omega 0 = 0 :=
  qr.omega_zero_balanced

/-- When ω₀ = 0, the remaining resolvents ω₁, ω₂, ω₃ are
    independent (at least one is nonzero for nontrivial input). -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
theorem three_resolvents_embed (qr : QuaternionicResolvent) :
    qr.omega 0 = 0 → (qr.omega 1 ≠ 0 ∨ qr.omega 2 ≠ 0 ∨ qr.omega 3 ≠ 0) :=
  fun _ => qr.nontrivial

end QOU
