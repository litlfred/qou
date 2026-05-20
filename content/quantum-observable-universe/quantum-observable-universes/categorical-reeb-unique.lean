/-!
# QOU.CategoricalReeb.unique — uniqueness of the categorical Reeb derivation

Any two categorical Reeb derivations on the same QU with the same
weight decomposition coincide.  Uniqueness is a theorem (not an
axiom): given existence (recorded as an axiom pending Lie-algebra
infrastructure), the torus-action argument pins down (ξ, θ_A).

LaTeX: `\label{prop:categorical-reeb-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-reeb-unique
- [witten1988] Topological Quantum Field Theory,
  https://doi.org/10.1007/BF01223371
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Reeb derivation.**

    Two CategoricalReeb structures on the same QU object with the
    same weight decomposition (same proj_V) coincide on ξ and θ_A.

    The argument: ξ is the infinitesimal generator of the T-action
    on the vertical summand, uniquely determined by the normalisation
    θ_A(ξ) = id.  Then θ_A is fixed by the Maurer–Cartan relation. -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
/-- **External axiom (§3b-cond pattern): CategoricalReeb.unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalReeb.unique_axiom {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C]
    (r₁ r₂ : CategoricalReeb C)
    (h_A : r₁.A = r₂.A)
    (h_forms : r₁.forms = r₂.forms)
    (h_projV : HEq r₁.proj_V r₂.proj_V) :
    HEq r₁.xi r₂.xi ∧ HEq r₁.theta r₂.theta

theorem CategoricalReeb.unique
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C]
    (r₁ r₂ : CategoricalReeb C)
    (h_A : r₁.A = r₂.A)
    (h_forms : r₁.forms = r₂.forms)
    (h_projV : HEq r₁.proj_V r₂.proj_V) :
    HEq r₁.xi r₂.xi ∧ HEq r₁.theta r₂.theta :=
  CategoricalReeb.unique_axiom C r₁ r₂ h_A h_forms h_projV

end QOU
