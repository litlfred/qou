import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Dimension.RankNullity
import Mathlib.Tactic.Linarith

/-!
# A flat non-abelian twist cannot remove the harmonic velocity modes on Bring

Owner question, 2026-11-25: *"can we use non-commutative vorticity? does that give
the gap needed?"* (bean `qou-4k93`).

A flat `G`-connection in a rank-`r` representation turns the DEC complex into a
twisted complex `C⁰ ⊗ K^r → C¹ ⊗ K^r → C² ⊗ K^r` with `d₁ d₀ = 0` (flatness is
exactly this). Its harmonic 1-forms are `H¹ = ker d₁ / im d₀`. By rank–nullity,
`dim H¹ ≥ dim C¹ − dim C⁰ − dim C²` (`finrank_H1_lower`). On the Bring {5,4} map
`(dim C⁰, dim C¹, dim C²) = (30r, 60r, 24r)`, so `dim H¹ ≥ 6r > 0`
(`bring_twisted_H1_pos`): for **every** flat twist, abelian or not, there remain
velocity modes that viscosity does not damp. Scope (b), invariant: the Euler
characteristic `χ = −6 < 0`.

A *non-flat* connection (nonzero curvature) can gap the section Laplacian (the
magnetic/Landau mechanism), but then `d₁ d₀ ≠ 0`: there is no cochain complex,
and the energy identities of `DECNavierStokes.lean` do not apply verbatim. That
route is not formalised here.

Base field generic (§7c). Ref: [leitner2026] `DECNavierStokes.lean`;
standard rank–nullity.
-/

namespace QOU.FluidDynamics.TwistedHarmonic

variable {K C0 C1 C2 : Type*} [Field K]
  [AddCommGroup C0] [Module K C0] [FiniteDimensional K C0]
  [AddCommGroup C1] [Module K C1] [FiniteDimensional K C1]
  [AddCommGroup C2] [Module K C2] [FiniteDimensional K C2]

/-- `dim (ker d₁) − dim (im d₀) ≥ dim C¹ − dim C⁰ − dim C²` (the lower bound on
`dim H¹`; `d₁ ∘ d₀ = 0` is not even needed for the inequality). -/
theorem finrank_H1_lower (d0 : C0 →ₗ[K] C1) (d1 : C1 →ₗ[K] C2) :
    (Module.finrank K C1 : ℤ) - Module.finrank K C0 - Module.finrank K C2
      ≤ (Module.finrank K (LinearMap.ker d1) : ℤ) - Module.finrank K (LinearMap.range d0) := by
  have h0 := LinearMap.finrank_range_add_finrank_ker d0
  have h1 := LinearMap.finrank_range_add_finrank_ker d1
  have h2 := Submodule.finrank_le (LinearMap.range d1)
  have h0' : (Module.finrank K (LinearMap.range d0) : ℤ) ≤ Module.finrank K C0 := by
    exact_mod_cast (by omega : Module.finrank K (LinearMap.range d0) ≤ Module.finrank K C0)
  omega

/-- On the Bring {5,4} map twisted by any rank-`r` flat connection
(`dim Cᵏ = 30r, 60r, 24r`), the harmonic space has dimension at least `6r`. -/
theorem bring_twisted_H1_pos (r : ℕ) (hr : 0 < r) (d0 : C0 →ₗ[K] C1) (d1 : C1 →ₗ[K] C2)
    (h0 : Module.finrank K C0 = 30 * r) (h1 : Module.finrank K C1 = 60 * r)
    (h2 : Module.finrank K C2 = 24 * r) :
    (6 * r : ℤ) ≤ (Module.finrank K (LinearMap.ker d1) : ℤ)
      - Module.finrank K (LinearMap.range d0) ∧ 0 < 6 * r := by
  have := finrank_H1_lower d0 d1
  rw [h0, h1, h2] at this
  refine ⟨by push_cast at this ⊢; linarith, by omega⟩

end QOU.FluidDynamics.TwistedHarmonic
