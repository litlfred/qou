/-!
# QOU.Braiding.HeckeMassElement — Hecke mass element

The Hecke mass element Φ_mass(β) ∈ H_n(q) is the fibre-functor image
of the mass integrand (∫_A ⊗ id) ∘ Δ ∘ ϱ, viewed as an endomorphism
of A via left multiplication in the Frobenius–Hopf algebra.

By quantum Schur–Weyl duality, every SU_q(2)-equivariant endomorphism
of V^{⊗n} is an element of H_n(q), so the mass element is well-defined.

The descent involution decomposes it:
  Φ_mass = Φ^desc + Φ^trans

and the Markov trace of Φ_mass recovers the categorical mass.

LaTeX label: `def:hecke-mass-element`

## References

- [manuscript] §4/hecke-mass-element
- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Normed.Group.Basic

namespace QOU.Braiding

/-! ## Hecke mass element -/

/-- The Hecke mass element: given a particle's Hecke element ρ(β)
    and the Frobenius–comultiplication dressing, the mass element
    is the dressed element whose Markov trace computes the mass.

    Abstractly: Φ_mass(β) = τ(L_{α_ϱ}) where
    α_ϱ = (∫_A ⊗ id) ∘ Δ ∘ ϱ and L denotes left multiplication
    in the Frobenius–Hopf algebra.

    We encode this as a structure carrying the decomposition data. -/
-- Ref: [manuscript] §4/hecke-mass-element
-- Ref: [jones1987] https://doi.org/10.2307/1971403
structure HeckeMassElement (R : Type*) [NormedCommRing R] where
  /-- The particle's Hecke element ρ(β) (before Frobenius dressing). -/
  particleElement : R
  /-- The descended component Φ^desc (base-level cycle). -/
  descendedComponent : R
  /-- The transient component Φ^trans (blow-up contributions). -/
  transientComponent : R
  /-- The mass element is the sum of descended and transient components. -/
  massElement : R
  /-- Decomposition: Φ_mass = Φ^desc + Φ^trans. -/
  decomposition : massElement = descendedComponent + transientComponent

/-- The categorical mass equals the norm of the mass element
    (standing in for ‖tr_M(Φ_mass)‖). -/
-- Ref: [manuscript] §4/hecke-mass-element
noncomputable def HeckeMassElement.mass {R : Type*} [NormedCommRing R]
    (Φ : HeckeMassElement R) : ℝ :=
  ‖Φ.massElement‖

/-- The mass decomposes via the triangle inequality, with equality
    when descended and transient components are non-negative reals. -/
-- Ref: [manuscript] §4/hecke-mass-element
theorem HeckeMassElement.mass_upper_bound {R : Type*} [NormedCommRing R]
    (Φ : HeckeMassElement R) :
    Φ.mass ≤ ‖Φ.descendedComponent‖ + ‖Φ.transientComponent‖ := by
  unfold mass
  rw [Φ.decomposition]
  exact norm_add_le Φ.descendedComponent Φ.transientComponent

/-- Exact mass decomposition for non-negative real components. -/
-- Ref: [manuscript] §4/hecke-mass-element
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem HeckeMassElement.mass_exact
    (Φ : HeckeMassElement ℝ)
    (h_desc : 0 ≤ Φ.descendedComponent)
    (h_trans : 0 ≤ Φ.transientComponent) :
    Φ.mass = ‖Φ.descendedComponent‖ + ‖Φ.transientComponent‖ := by
  unfold mass
  rw [Φ.decomposition,
      Real.norm_of_nonneg (add_nonneg h_desc h_trans),
      Real.norm_of_nonneg h_desc,
      Real.norm_of_nonneg h_trans]

end QOU.Braiding
