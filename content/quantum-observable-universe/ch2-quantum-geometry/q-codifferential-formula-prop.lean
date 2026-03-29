/-!
# QOU.QuantumGeometry.q_codifferential_formula — Closed formula for δ_q

The formal adjoint of d_q with respect to the Webster inner product is
δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ, characterised by the adjoint relation
⟨d_q α, β⟩_θ = ⟨α, δ_q β⟩_θ.

Works over an arbitrary commutative ring R (e.g. ℤ, ℤ[q, q⁻¹], ℝ).
The substrate parameter q is taken as a unit in R.

LaTeX label: `prop:q-codifferential-formula`

## References
- [manuscript] Ch. 2, §geometric-interpretations
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units

namespace QOU.QuantumGeometry

universe u

variable {R : Type u} [CommRing R]

/-- Abstract type for differential forms on a contact manifold,
    parametric over a commutative ring R. -/
axiom DiffForm (R : Type u) [CommRing R] : Type u

/-- The Webster inner product ⟨·,·⟩_θ valued in R. -/
axiom websterInner (R : Type u) [CommRing R] : DiffForm R → DiffForm R → R
/-- The classical exterior derivative d. -/
axiom d_classical (R : Type u) [CommRing R] : DiffForm R → DiffForm R
/-- The classical codifferential δ (formal adjoint of d). -/
axiom δ_classical (R : Type u) [CommRing R] : DiffForm R → DiffForm R
/-- The Reeb Lie derivative L_ξ. -/
axiom L_reeb (R : Type u) [CommRing R] : DiffForm R → DiffForm R
/-- The adjoint L_ξ*. -/
axiom L_reeb_star (R : Type u) [CommRing R] : DiffForm R → DiffForm R
/-- The interior product ι_ξ. -/
axiom ι_reeb (R : Type u) [CommRing R] : DiffForm R → DiffForm R
/-- The contact form wedge product θ∧(·). -/
axiom θ_wedge (R : Type u) [CommRing R] : DiffForm R → DiffForm R
/-- Scalar multiplication of R on differential forms. -/
axiom DiffForm.smul (R : Type u) [CommRing R] : R → DiffForm R → DiffForm R
/-- Addition of differential forms. -/
axiom DiffForm.add (R : Type u) [CommRing R] : DiffForm R → DiffForm R → DiffForm R

noncomputable instance : SMul R (DiffForm R) := ⟨DiffForm.smul R⟩
noncomputable instance : Add (DiffForm R) := ⟨DiffForm.add R⟩

/-- The q-exterior derivative: d_q = q⁻¹ d + (1 - q⁻¹) θ ∧ L_ξ.
    q is a unit in R (e.g. the substrate parameter in ℤ[q,q⁻¹]). -/
noncomputable axiom d_q (R : Type u) [CommRing R] (q : Rˣ) : DiffForm R → DiffForm R

/-! ## Axioms: R-module structure -/

-- Ref: [manuscript] Ch. 2 — DiffForm is an R-module
axiom smul_add' (r : R) (α β : DiffForm R) : r • (α + β) = r • α + r • β
axiom smul_smul' (r s : R) (α : DiffForm R) : r • (s • α) = (r * s) • α
axiom one_smul' (α : DiffForm R) : (1 : R) • α = α

/-! ## Axioms: Tanaka-Webster adjoint theory

On a strictly pseudoconvex CR manifold (M, θ) with Webster metric g_θ,
the Tanaka-Webster connection determines a pairing on sections of the
exterior bundle.  Over ℝ this is the L² inner product; over ℤ[q,q⁻¹]
it is the Markov-trace pairing. -/

-- Ref: [manuscript] Ch. 2 — Tanaka-Webster adjoint existence
axiom adjoint_exists_unique' (L : DiffForm R → DiffForm R) :
    ∃! (L_star : DiffForm R → DiffForm R),
      ∀ (α β : DiffForm R), websterInner R (L α) β = websterInner R α (L_star β)

/-! ## Axioms: specific adjoint identities -/

-- Ref: [manuscript] Ch. 2 — δ is the formal adjoint of d
axiom δ_is_adjoint_of_d' :
    ∀ (α β : DiffForm R), websterInner R (d_classical R α) β =
      websterInner R α (δ_classical R β)

-- Ref: [manuscript] Ch. 2 — ι_ξ is the formal adjoint of θ∧
axiom ι_reeb_is_adjoint_of_θ_wedge' :
    ∀ (α β : DiffForm R), websterInner R (θ_wedge R α) β =
      websterInner R α (ι_reeb R β)

-- Ref: [manuscript] Ch. 2 — L_ξ* is the formal adjoint of L_ξ
axiom L_reeb_star_is_adjoint' :
    ∀ (α β : DiffForm R), websterInner R (L_reeb R α) β =
      websterInner R α (L_reeb_star R β)

/-! ## Axioms: bilinearity of the Webster inner product -/

-- Ref: [manuscript] Ch. 2 — bilinearity of ⟨·,·⟩_θ
axiom websterInner_add_left' (α₁ α₂ β : DiffForm R) :
    websterInner R (α₁ + α₂) β = websterInner R α₁ β + websterInner R α₂ β

axiom websterInner_smul_left' (r : R) (α β : DiffForm R) :
    websterInner R (r • α) β = r * websterInner R α β

axiom websterInner_add_right' (α β₁ β₂ : DiffForm R) :
    websterInner R α (β₁ + β₂) = websterInner R α β₁ + websterInner R α β₂

axiom websterInner_smul_right' (r : R) (α β : DiffForm R) :
    websterInner R α (r • β) = r * websterInner R α β

/-! ## Axiom: d_q decomposition -/

axiom d_q_decomposition' (q : Rˣ) (α : DiffForm R) :
    d_q R q α = (↑q⁻¹ : R) • d_classical R α +
      (1 - (↑q⁻¹ : R)) • θ_wedge R (L_reeb R α)

/-! ## Main result -/

/-- **Part (a)**: The formal adjoint δ_q of d_q exists. -/
theorem q_codifferential_exists (q : Rˣ) :
    ∃ (δ_q : DiffForm R → DiffForm R),
      ∀ (α β : DiffForm R), websterInner R (d_q R q α) β =
        websterInner R α (δ_q β) := by
  obtain ⟨δ_q, hδ, _⟩ := adjoint_exists_unique' (d_q R q)
  exact ⟨δ_q, hδ⟩

/-- **Part (b)**: The candidate δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ
    satisfies the adjoint relation for d_q. -/
theorem q_codifferential_adjoint_relation (q : Rˣ) (α β : DiffForm R) :
    websterInner R (d_q R q α) β =
      websterInner R α ((↑q⁻¹ : R) • δ_classical R β +
        (1 - (↑q⁻¹ : R)) • L_reeb_star R (ι_reeb R β)) := by
  rw [d_q_decomposition']
  rw [websterInner_add_left']
  rw [websterInner_smul_left', websterInner_smul_left']
  rw [δ_is_adjoint_of_d']
  rw [ι_reeb_is_adjoint_of_θ_wedge', L_reeb_star_is_adjoint']
  rw [websterInner_add_right']
  rw [websterInner_smul_right', websterInner_smul_right']

/-- **Closed formula for the q-codifferential.**
    The formal adjoint of d_q is δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ. -/
theorem q_codifferential_formula (q : Rˣ) :
    ∃ (δ_q : DiffForm R → DiffForm R),
      (∀ (α β : DiffForm R), websterInner R (d_q R q α) β =
        websterInner R α (δ_q β)) ∧
      (∀ (β : DiffForm R), δ_q β = (↑q⁻¹ : R) • δ_classical R β +
        (1 - (↑q⁻¹ : R)) • (L_reeb_star R (ι_reeb R β))) := by
  refine ⟨fun β => (↑q⁻¹ : R) • δ_classical R β +
    (1 - (↑q⁻¹ : R)) • (L_reeb_star R (ι_reeb R β)), ?_, ?_⟩
  · exact q_codifferential_adjoint_relation q
  · intro β; rfl

end QOU.QuantumGeometry
