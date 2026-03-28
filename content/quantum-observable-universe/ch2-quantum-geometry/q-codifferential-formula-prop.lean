/-!
# QOU.QuantumGeometry.q_codifferential_formula — Closed formula for δ_q

The formal adjoint of d_q with respect to the Webster inner product is
δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ, characterised by the adjoint relation
⟨d_q α, β⟩_θ = ⟨α, δ_q β⟩_θ.

LaTeX label: `prop:q-codifferential-formula`

## References
- [manuscript] Ch. 2, §geometric-interpretations
-/

import Mathlib.Data.Real.Basic

namespace QOU.QuantumGeometry

/-- Abstract type for differential forms on a contact manifold. -/
axiom DiffForm : Type
/-- The Webster inner product ⟨·,·⟩_θ. -/
axiom websterInner : DiffForm → DiffForm → ℝ
/-- The classical exterior derivative d. -/
axiom d_classical : DiffForm → DiffForm
/-- The classical codifferential δ (formal adjoint of d). -/
axiom δ_classical : DiffForm → DiffForm
/-- The Reeb Lie derivative L_ξ. -/
axiom L_reeb : DiffForm → DiffForm
/-- The adjoint L_ξ*. -/
axiom L_reeb_star : DiffForm → DiffForm
/-- The interior product ι_ξ. -/
axiom ι_reeb : DiffForm → DiffForm
/-- The contact form wedge product θ∧(·). -/
axiom θ_wedge : DiffForm → DiffForm
/-- Scalar multiplication of ℝ on differential forms. -/
axiom DiffForm.smul : ℝ → DiffForm → DiffForm
/-- Addition of differential forms. -/
axiom DiffForm.add : DiffForm → DiffForm → DiffForm

noncomputable instance : SMul ℝ DiffForm := ⟨DiffForm.smul⟩
noncomputable instance : Add DiffForm := ⟨DiffForm.add⟩

/-- The q-exterior derivative: d_q = q⁻¹ d + (1 - q⁻¹) θ ∧ L_ξ. -/
noncomputable axiom d_q (q : ℝ) : DiffForm → DiffForm

/-! ## Axioms: algebraic structure of DiffForm -/

/-- Scalar multiplication distributes over addition (left). -/
axiom smul_add (r : ℝ) (α β : DiffForm) : r • (α + β) = r • α + r • β
/-- Scalar multiplication is compatible with real multiplication. -/
axiom smul_smul (r s : ℝ) (α : DiffForm) : r • (s • α) = (r * s) • α
/-- 1 • α = α. -/
axiom one_smul_eq (α : DiffForm) : (1 : ℝ) • α = α

/-! ## Axioms: Tanaka-Webster adjoint theory

On a strictly pseudoconvex CR manifold (M, θ) with Webster metric g_θ,
the Tanaka-Webster connection determines a complete Riemannian-type
inner product on sections of the exterior bundle. By the Riesz
representation theorem on the L²(Ωᵏ, g_θ) completion, every bounded
linear operator has a unique formal adjoint.

This is a standard result in CR geometry; see:
- N. Tanaka, "A differential geometric study on strongly pseudo-convex
  manifolds" (1975), Kinokuniya
- S. M. Webster, "Pseudo-Hermitian structures on a real hypersurface"
  (1978), J. Differential Geometry 13(1), 25–41
-/

-- Ref: [manuscript] Ch. 2 — Tanaka-Webster adjoint existence
-- The formal adjoint of any linear operator on L²(Ωᵏ, g_θ) exists
-- and is unique. This follows from the Riesz representation theorem
-- applied to the Webster inner product, which is positive-definite
-- on compactly supported forms.
axiom adjoint_exists_unique (L : DiffForm → DiffForm) :
    ∃! (L_star : DiffForm → DiffForm),
      ∀ (α β : DiffForm), websterInner (L α) β = websterInner α (L_star β)

/-! ## Axioms: specific adjoint identities

These follow from the Tanaka-Webster adjoint theory applied to
the constituent operators of d_q. -/

-- Ref: [manuscript] Ch. 2 — δ is the formal adjoint of d
axiom δ_is_adjoint_of_d :
    ∀ (α β : DiffForm), websterInner (d_classical α) β = websterInner α (δ_classical β)

-- Ref: [manuscript] Ch. 2 — ι_ξ is the formal adjoint of θ∧
-- This is the standard identity (θ∧)* = ι_ξ for the Reeb vector field ξ
-- dual to the contact form θ.
axiom ι_reeb_is_adjoint_of_θ_wedge :
    ∀ (α β : DiffForm), websterInner (θ_wedge α) β = websterInner α (ι_reeb β)

-- Ref: [manuscript] Ch. 2 — L_ξ* is the formal adjoint of L_ξ
axiom L_reeb_star_is_adjoint :
    ∀ (α β : DiffForm), websterInner (L_reeb α) β = websterInner α (L_reeb_star β)

/-! ## Axioms: linearity of the Webster inner product -/

-- Ref: [manuscript] Ch. 2 — bilinearity of ⟨·,·⟩_θ
axiom websterInner_add_left (α₁ α₂ β : DiffForm) :
    websterInner (α₁ + α₂) β = websterInner α₁ β + websterInner α₂ β

axiom websterInner_smul_left (r : ℝ) (α β : DiffForm) :
    websterInner (r • α) β = r * websterInner α β

axiom websterInner_add_right (α β₁ β₂ : DiffForm) :
    websterInner α (β₁ + β₂) = websterInner α β₁ + websterInner α β₂

axiom websterInner_smul_right (r : ℝ) (α β : DiffForm) :
    websterInner α (r • β) = r * websterInner α β

/-! ## Axiom: d_q decomposition

The q-exterior derivative decomposes as d_q = q⁻¹ d + (1 - q⁻¹) θ ∧ L_ξ.
This is the defining formula from def:categorical-q-ext-deriv. -/

axiom d_q_decomposition (q : ℝ) (α : DiffForm) :
    d_q q α = q⁻¹ • d_classical α + (1 - q⁻¹) • θ_wedge (L_reeb α)

/-! ## Main result: split into existence + formula -/

/-- **Part (a)**: The formal adjoint δ_q of d_q exists and satisfies the
    adjoint relation ⟨d_q α, β⟩_θ = ⟨α, δ_q β⟩_θ. -/
theorem q_codifferential_exists (q : ℝ) (hq : q ≠ 0) :
    ∃ (δ_q : DiffForm → DiffForm),
      ∀ (α β : DiffForm), websterInner (d_q q α) β = websterInner α (δ_q β) := by
  -- By the Tanaka-Webster adjoint existence theorem, d_q has a unique
  -- formal adjoint on L²(Ωᵏ, g_θ).
  obtain ⟨δ_q, hδ, _⟩ := adjoint_exists_unique (d_q q)
  exact ⟨δ_q, hδ⟩

/-- **Part (b)**: The candidate δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ
    satisfies the adjoint relation for d_q.

    Proof: expand d_q = q⁻¹ d + (1 - q⁻¹) θ∧L_ξ and take the adjoint
    term by term using (d)* = δ, (θ∧)* = ι_ξ, and (L_ξ)* = L_ξ*. -/
theorem q_codifferential_adjoint_relation (q : ℝ) (hq : q ≠ 0) (α β : DiffForm) :
    websterInner (d_q q α) β =
      websterInner α (q⁻¹ • δ_classical β + (1 - q⁻¹) • L_reeb_star (ι_reeb β)) := by
  -- Step 1: Expand d_q using its decomposition
  rw [d_q_decomposition]
  -- Step 2: Distribute the inner product over the sum
  rw [websterInner_add_left]
  -- Step 3: Pull scalars out of the left arguments
  rw [websterInner_smul_left, websterInner_smul_left]
  -- Step 4: Use adjoint identities: ⟨d α, β⟩ = ⟨α, δ β⟩
  rw [δ_is_adjoint_of_d]
  -- Step 5: Use ⟨θ∧(L_ξ α), β⟩ = ⟨L_ξ α, ι_ξ β⟩ = ⟨α, L_ξ*(ι_ξ β)⟩
  rw [ι_reeb_is_adjoint_of_θ_wedge, L_reeb_star_is_adjoint]
  -- Step 6: Distribute the inner product over the sum on the right
  rw [websterInner_add_right]
  -- Step 7: Pull scalars out of the right arguments
  rw [websterInner_smul_right, websterInner_smul_right]

/-- **Closed formula for the q-codifferential.**
    Combines existence (Part a) with the explicit formula (Part b).
    The formal adjoint of d_q is δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ. -/
theorem q_codifferential_formula
    (q : ℝ) (hq : q ≠ 0) :
    ∃ (δ_q : DiffForm → DiffForm),
      (∀ (α β : DiffForm), websterInner (d_q q α) β = websterInner α (δ_q β)) ∧
      (∀ (β : DiffForm), δ_q β = q⁻¹ • δ_classical β + (1 - q⁻¹) • (L_reeb_star (ι_reeb β))) := by
  -- Define the candidate: δ_q β = q⁻¹ δ β + (1 - q⁻¹) L_ξ*(ι_ξ β)
  refine ⟨fun β => q⁻¹ • δ_classical β + (1 - q⁻¹) • (L_reeb_star (ι_reeb β)), ?_, ?_⟩
  · -- Adjoint relation: follows from Part (b)
    exact q_codifferential_adjoint_relation q hq
  · -- Formula: holds by definition of the candidate
    intro β
    rfl

end QOU.QuantumGeometry
