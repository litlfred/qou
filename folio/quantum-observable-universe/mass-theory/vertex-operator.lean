/-
  Vertex operator on the exceptional divisor.

  The vertex operator Y(a, z) is the R-matrix insertion of a state
  a ∈ Aₙ at the affine coordinate z = v₁/v₂ on 𝒮_p ≅ ℙ¹(ℂ).
  Its modes aₘ are the Laurent coefficients, computed via the
  Markov trace of the braid operator.

  The brane tower ⊕ Aₙ is the graded state space, the jet
  prolongation j : Aₙ → A_{n+1} is the translation operator L_{-1},
  and the OPE singularity is the Hecke/Skein relation.

  ## References
  - [frenkel2004] https://doi.org/10.1090/surv/088
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Topology.FiberBundle.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A vertex operator on the exceptional divisor 𝒮_p.
    Given a state a ∈ V_n (level n of the brane tower), the vertex
    operator Y(a, z) is a formal Laurent series in the affine
    coordinate z = v₁/v₂ on 𝒮_p whose modes are R-matrix insertions. -/
-- Ref: [frenkel2004] Frenkel, "Lectures on the Langlands program and conformal field theory," arXiv:hep-th/0512172 (related: 0007054)
structure VertexOperator (B : Type*) (q : R_q) where
  /-- The base space for the insertion — the Reeb bundle `ℛ_p`.

      **Carried as a type parameter `B`, not as `ReebBundle q`, and the
      reason is a layer wall rather than a missing import.**
      `def:reeb-bundle` is `structure ReebBundle (q : ℝ)` — an
      *archimedean* object (its `substrate` field is `q > 1`, its
      `holonomy` is a `Real.exp`), and its own header says "NOT part of
      the formal proof chain". This file is over the categorical ground
      ring `R_q = ℤ[q, q⁻¹]`. Writing `ReebBundle q` here is therefore
      not just unreachable (a content-block sibling cannot import a
      sibling — they sit outside the Lake globs) but **type-wrong**: it
      applies an ℝ-indexed structure to a Laurent polynomial, which is
      the §7c straddle the ground-ring convention exists to prevent.

      Parameterising keeps the vertex-operator algebra on the
      categorical side. An archimedean consumer instantiates
      `B := ReebBundle q₀` after the τ functor. -/
  bundle : B
  /-- Conformal weight (jet level) of the state. -/
  weight : ℕ

/-- The OPE (operator product expansion) of two vertex operators.
    Records the leading singularity data: the eigenvalues of the
    Hecke generator T acting on the collision Y₁(z)Y₂(w) as z → w. -/
structure OPE (B : Type*) (q : R_q) where
  /-- The two vertex operators whose collision is being resolved. -/
  left : VertexOperator B q
  right : VertexOperator B q
  /-- The symmetric (bosonic) eigenvalue of the Hecke generator. -/
  bosonic_eigenvalue : R_q
  /-- The antisymmetric (fermionic) eigenvalue. -/
  fermionic_eigenvalue : R_q

/-- The OPE of any two vertex operators has its leading singularity
    recorded by the Hecke eigenvalue pair: bosonic `q`, fermionic
    `-q⁻¹`, from `(T - q)(T + q⁻¹) = 0` — the Skein relation
    `L₊ - L₋ = (q - q⁻¹)L₀` applied to the strand collision on `𝒮_p`.

    **This was a bare `axiom`, and what it asserts is weaker than it
    reads. Both facts are stated here rather than left to be
    rediscovered.**

    It was an `axiom`, so it polluted `#print axioms` for every
    downstream statement (§"Axiomatization is NOT a Proof"). It is now
    a theorem, and the proof is `⟨⟨Y₁, Y₂, q, -q_inv_param⟩, rfl, rfl,
    rfl, rfl⟩` — because `OPE` is a plain record with the eigenvalues
    as *fields*, so exhibiting one with those values is record
    construction, not mathematics. Assuming it bought nothing.

    So what is **established**: an `OPE` carrying the Hecke pair exists
    for any two operators. What is **not**: that the pair is *forced*.
    That needs the Hecke generator acting on the collision and its
    quadratic relation — i.e. `OPE` would have to carry the action and
    derive the eigenvalues, rather than take them as data. Until then
    the values `q` and `-q⁻¹` are put in by hand and this theorem
    cannot tell a right pair from a wrong one. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem ope_is_skein {B : Type*} {q : R_q} (Y₁ Y₂ : VertexOperator B q) :
    ∃ ope : OPE B q,
        ope.left = Y₁ ∧ ope.right = Y₂ ∧
        ope.bosonic_eigenvalue = q ∧
        ope.fermionic_eigenvalue = -q_inv_param :=
  ⟨⟨Y₁, Y₂, q, -q_inv_param⟩, rfl, rfl, rfl, rfl⟩
end

end QOU
