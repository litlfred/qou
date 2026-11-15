import Mathlib.Algebra.Ring.Basic
import Mathlib.Analysis.Normed.Ring.Basic


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

**Pre-Archimedean stub.** The previous version coupled this stub
to `[NormedCommRing R]` and returned `ℝ` via `‖·‖`.  The Hecke
mass element lives in `H_n(R, q)` for any commutative ring
`R ⊇ ℤ[q^±1]`; the Archimedean norm is post-τ.  We split into
two declarations:

  1. `frobeniusMassSquared` — the pre-Arch squared mass,
     `m² := ⟨massElement, massElement⟩_F`, valued in `R` (caller
     supplies the Frobenius pairing).
  2. `mass` — the post-τ Archimedean realisation, valued in `ℝ`,
     requires `[NormedCommRing R]`.

LaTeX label: `def:hecke-mass-element`

## References

- [leitner2026] §4/hecke-mass-element
- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.Braiding

universe u

/-! ## Hecke mass element -/

/-- The Hecke mass element: given a particle's Hecke element ρ(β)
    and the Frobenius–comultiplication dressing, the mass element
    is the dressed element whose Markov trace computes the mass.

    Abstractly: Φ_mass(β) = τ(L_{α_ϱ}) where
    α_ϱ = (∫_A ⊗ id) ∘ Δ ∘ ϱ and L denotes left multiplication
    in the Frobenius–Hopf algebra.

    We encode this as a structure carrying the decomposition data,
    polymorphic in the ground ring `R` (pre-Arch: `R = ℤ[q^±1]`). -/
-- Ref: [leitner2026] §4/hecke-mass-element
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
structure HeckeMassElement (R : Type u) [CommRing R] where
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

/-- **Pre-Arch Frobenius mass squared.**

    `m²(Φ) := ⟨Φ.massElement, Φ.massElement⟩_F`, where the Frobenius
    pairing is supplied by the caller.  Valued in `R` (no Archimedean
    norm). -/
-- Ref: [leitner2026] §4/hecke-mass-element
def frobeniusMassSquared
    {R : Type u} [CommRing R] (frobenius_form : R → R → R)
    (Φ : HeckeMassElement R) : R :=
  frobenius_form Φ.massElement Φ.massElement

/-- **Post-Arch Archimedean mass.**

    The categorical mass equals the Archimedean norm of the mass
    element (standing in for `‖tr_M(Φ_mass)‖`).  Requires
    `[NormedCommRing R]`; lives downstream of the formal chain.

    Per `QOU.GroundRingAnnotations`, this is **not** part of the
    pre-Arch chain. -/
-- Ref: [leitner2026] §4/hecke-mass-element
noncomputable def HeckeMassElement.mass
    {R : Type u} [NormedCommRing R]
    (Φ : HeckeMassElement R) : ℝ :=
  ‖Φ.massElement‖

/-- The mass decomposes via the triangle inequality, with equality
    when descended and transient components are non-negative reals. -/
-- Ref: [leitner2026] §4/hecke-mass-element
theorem mass_upper_bound {R : Type u} [NormedCommRing R]
    (Φ : HeckeMassElement R) :
    Φ.mass ≤ ‖Φ.descendedComponent‖ + ‖Φ.transientComponent‖ := by
  unfold HeckeMassElement.mass
  rw [Φ.decomposition]
  exact norm_add_le Φ.descendedComponent Φ.transientComponent

/-- Exact mass decomposition for non-negative real components. -/
-- Ref: [leitner2026] §4/hecke-mass-element
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem mass_exact
    (Φ : HeckeMassElement ℝ)
    (h_desc : 0 ≤ Φ.descendedComponent)
    (h_trans : 0 ≤ Φ.transientComponent) :
    Φ.mass = ‖Φ.descendedComponent‖ + ‖Φ.transientComponent‖ := by
  unfold HeckeMassElement.mass
  rw [Φ.decomposition,
      Real.norm_of_nonneg (add_nonneg h_desc h_trans),
      Real.norm_of_nonneg h_desc,
      Real.norm_of_nonneg h_trans]

end QOU.Braiding
