/-!
# QOU.Braiding.NucleonHeckeElement — Nucleon Hecke element

The nucleon Hecke element 𝔑(f₁, f₂, f₃) ∈ H_3(q) is the product
of the Borromean link element ℬ₃ = (σ₀σ₁⁻¹)³ with the three typed
crossing operators C(f_i, f_j; σ_k) for the quark flavor triple
of a Borromean baryon.

LaTeX label: `def:nucleon-hecke-element`

## References

- [manuscript] Ch 3 §16

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- The nucleon Hecke element: the product in H_3(q) encoding
    the full braiding structure of a nucleon (proton or neutron)
    as a Borromean baryon with typed crossings.

    𝔑(f₁, f₂, f₃) = ℬ₃ · C(f₁, f₂; σ₀) · C(f₁, f₃; σ₀) · C(f₂, f₃; σ₁)

    where ℬ₃ = (σ₀σ₁⁻¹)³ is the Borromean link element. -/
-- Ref: [manuscript] Ch 3 §16
structure NucleonHeckeElement where
  /-- Flavor triple (f₁, f₂, f₃) of the three quarks. -/
  flavors : Fin 3 → QuarkFlavor
  /-- The resulting Hecke algebra element in H_3(q). -/
  -- Ref: [manuscript] Ch 3 §16
  element : LaurentPolynomial ℤ := sorry

/-- A proton has flavor triple (u, u, d). -/
-- Ref: [manuscript] Ch 3 §16
def protonFlavors : Fin 3 → QuarkFlavor
  | ⟨0, _⟩ => .up
  | ⟨1, _⟩ => .up
  | ⟨2, _⟩ => .down
  | ⟨n + 3, h⟩ => absurd h (by decide)

/-- A neutron has flavor triple (u, d, d). -/
-- Ref: [manuscript] Ch 3 §16
def neutronFlavors : Fin 3 → QuarkFlavor
  | ⟨0, _⟩ => .up
  | ⟨1, _⟩ => .down
  | ⟨2, _⟩ => .down
  | ⟨n + 3, h⟩ => absurd h (by decide)

end QOU.Braiding
