/-
# Schur uniqueness of invariant symmetric forms — the α_EM B2 τ-identification core (Option B)

Attack option B of the B2 τ-identification (`docs/audits/2026-07-24-alpha-em-b2-tau-
identification-attack-options.md`, epic `qou-6ufi`). The remaining B2 input is:
the α_EM loop weight `W` on `H^{1,0}(Bring)` equals `complexify` of the Markov Gram.
Because `H^{1,0}(Bring) = std` is the **irreducible** standard S₅-representation
(#2701), Schur's lemma forces any two invariant symmetric bilinear forms on it to be
**proportional** — shrinking the wall from "construct the whole τ-functor" to "prove
the τ-image is equivariant + fix one scalar."

This file formalizes that Schur mechanism at the matrix level (sorry-free):

* `Commute`-form invariance `Gᵀ`-sandwich `(ρ s)ᵀ * G * (ρ s) = G` for a
  representation `ρ`;
* **`invariantForm_proportional_of_commutantScalar`** — if the commutant of `ρ` is
  scalar (the absolute-irreducibility hypothesis, Schur) and `G₁` is a unit, then any
  invariant `G₂` is `c • G₁`. The proof runs through the endomorphism `A = G₁⁻¹ * G₂`,
  which commutes with `ρ` (invariance + units), so `A = c • 1` (Schur), hence
  `G₂ = c • G₁`.

**Instantiation (the wall, restated).** With `ρ = ` the S₅-action on `std`,
`G₁ = ` the Hodge Gram (invariant — Aut(Bring) acts by isometries), `G₂ = ` the
τ-image of the Markov Gram (invariant *if τ-equivariant*), and the scalar-commutant
hypothesis discharged by the absolute irreducibility of `std` (#2701), this yields
`τ(Markov Gram) = c · Hodge Gram`. The two OPEN sub-pieces after B are exactly:
(i) the τ-image is S₅-equivariant on `std`; (ii) the scalar `c` (Option C pins it).

STRICT (§"Axiomatization is NOT a Proof"): this DERIVES proportionality from the
scalar-commutant hypothesis — it does NOT assume the identification, construct `τ`,
or register a `TauRhoHodgeLift` instance. The scalar-commutant hypothesis is the
Schur/absolute-irreducibility of `std`, a *separate* provable input, taken here as a
named hypothesis, not fabricated. `1/(8π)` stays a phase-4 identification.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [serre1977] Linear Representations of Finite Groups (Schur's lemma)
-/
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

namespace QOU.Archimedean.SchurInvariantFormProportional

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n] {k : Type*} [Field k]
variable {G : Type*}

/-- Invariance of a bilinear-form matrix `M` under `ρ s`: the transpose-sandwich
`(ρ s)ᵀ * M * (ρ s) = M`. -/
def InvariantForm (ρ : G → Matrix n n k) (M : Matrix n n k) : Prop :=
  ∀ s, (ρ s)ᵀ * M * (ρ s) = M

/-- **Key commuting step.** If `G₁` and `G₂` are both invariant forms for a
representation `ρ` by units, then `A = G₁⁻¹ * G₂` commutes with every `ρ s`. (This is
why an invariant form defines a `ρ`-equivariant map to the dual.) -/
theorem commute_of_invariantForm {ρ : G → Matrix n n k}
    (hρ : ∀ s, IsUnit (ρ s).det) {G₁ G₂ : Matrix n n k}
    (h₁ : InvariantForm ρ G₁) (h₂ : InvariantForm ρ G₂) (hG₁ : IsUnit G₁.det)
    (s : G) : (G₁⁻¹ * G₂) * (ρ s) = (ρ s) * (G₁⁻¹ * G₂) := by
  have hρT : IsUnit ((ρ s)ᵀ).det := by
    rw [Matrix.det_transpose]; exact hρ s
  -- P1 : G₁ * ρs = (ρsᵀ)⁻¹ * G₁   (from (ρsᵀ) G₁ ρs = G₁, left-cancel ρsᵀ)
  have P1 : G₁ * (ρ s) = ((ρ s)ᵀ)⁻¹ * G₁ := by
    have h := h₁ s
    have : ((ρ s)ᵀ)⁻¹ * ((ρ s)ᵀ * G₁ * (ρ s)) = ((ρ s)ᵀ)⁻¹ * G₁ := by rw [h]
    rwa [← Matrix.mul_assoc, ← Matrix.mul_assoc,
      Matrix.nonsing_inv_mul _ hρT, Matrix.one_mul] at this
  -- P2 : G₂ * ρs = (ρsᵀ)⁻¹ * G₂
  have P2 : G₂ * (ρ s) = ((ρ s)ᵀ)⁻¹ * G₂ := by
    have h := h₂ s
    have : ((ρ s)ᵀ)⁻¹ * ((ρ s)ᵀ * G₂ * (ρ s)) = ((ρ s)ᵀ)⁻¹ * G₂ := by rw [h]
    rwa [← Matrix.mul_assoc, ← Matrix.mul_assoc,
      Matrix.nonsing_inv_mul _ hρT, Matrix.one_mul] at this
  -- ρs * G₁⁻¹ = G₁⁻¹ * (ρsᵀ)⁻¹   (from P1)
  have P3 : (ρ s) * G₁⁻¹ = G₁⁻¹ * ((ρ s)ᵀ)⁻¹ := by
    have e1 : G₁⁻¹ * (G₁ * (ρ s)) = (ρ s) := by
      rw [← Matrix.mul_assoc, Matrix.nonsing_inv_mul _ hG₁, Matrix.one_mul]
    have e2 : (((ρ s)ᵀ)⁻¹ * G₁) * G₁⁻¹ = ((ρ s)ᵀ)⁻¹ := by
      rw [Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hG₁, Matrix.mul_one]
    calc (ρ s) * G₁⁻¹
        = (G₁⁻¹ * (G₁ * (ρ s))) * G₁⁻¹ := by rw [e1]
      _ = (G₁⁻¹ * (((ρ s)ᵀ)⁻¹ * G₁)) * G₁⁻¹ := by rw [P1]
      _ = G₁⁻¹ * ((((ρ s)ᵀ)⁻¹ * G₁) * G₁⁻¹) := by rw [Matrix.mul_assoc]
      _ = G₁⁻¹ * ((ρ s)ᵀ)⁻¹ := by rw [e2]
  -- assemble: (G₁⁻¹ G₂) ρs = G₁⁻¹ (ρsᵀ)⁻¹ G₂ = ρs (G₁⁻¹ G₂)
  calc (G₁⁻¹ * G₂) * (ρ s)
      = G₁⁻¹ * (G₂ * (ρ s)) := by rw [Matrix.mul_assoc]
    _ = G₁⁻¹ * (((ρ s)ᵀ)⁻¹ * G₂) := by rw [P2]
    _ = (G₁⁻¹ * ((ρ s)ᵀ)⁻¹) * G₂ := by rw [Matrix.mul_assoc]
    _ = ((ρ s) * G₁⁻¹) * G₂ := by rw [P3]
    _ = (ρ s) * (G₁⁻¹ * G₂) := by rw [Matrix.mul_assoc]

/-- **Schur proportionality of invariant forms.** If the commutant of `ρ` is scalar
(the absolute-irreducibility hypothesis — every matrix commuting with all `ρ s` is
`c • 1`), and `G₁` is a unit, then any invariant form `G₂` is a scalar multiple of
`G₁`. This is the Option-B core: two invariant symmetric forms on an irreducible
representation are proportional. -/
theorem invariantForm_proportional_of_commutantScalar {ρ : G → Matrix n n k}
    (hρ : ∀ s, IsUnit (ρ s).det)
    (schur : ∀ A : Matrix n n k, (∀ s, A * (ρ s) = (ρ s) * A) → ∃ c : k, A = c • (1 : Matrix n n k))
    {G₁ G₂ : Matrix n n k} (hG₁ : IsUnit G₁.det)
    (h₁ : InvariantForm ρ G₁) (h₂ : InvariantForm ρ G₂) :
    ∃ c : k, G₂ = c • G₁ := by
  obtain ⟨c, hc⟩ := schur (G₁⁻¹ * G₂) (commute_of_invariantForm hρ h₁ h₂ hG₁)
  refine ⟨c, ?_⟩
  have : G₁ * (G₁⁻¹ * G₂) = G₁ * (c • (1 : Matrix n n k)) := by rw [hc]
  rwa [← Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hG₁, Matrix.one_mul,
    Matrix.mul_smul, Matrix.mul_one] at this

end QOU.Archimedean.SchurInvariantFormProportional
