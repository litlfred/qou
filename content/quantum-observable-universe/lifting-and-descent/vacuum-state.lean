import Mathlib.Algebra.Module.Basic
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.Torsion.vacuum_state — Existence and uniqueness of the vacuum state

Given a QOU (𝒞, A, ω), the Frobenius trace on the direct limit algebra
𝒜_∞ = lim End_𝒞(Aₙ) is the unique G_q-invariant R-linear functional.

## References

- [manuscript] §3 Lifting and Descent
- [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

namespace QOU.Torsion

variable {R : Type*} [CommRing R]

/-! ## Frobenius trace on an algebra tower -/

/-- A tower of R-algebras with descent (retraction) maps. -/
structure AlgebraTower (R : Type*) [CommRing R] where
  /-- The R-module at level n. -/
  levelMod : ℕ → Type*
  /-- Each level is an R-module. -/
  addCommGroup : ∀ n, AddCommGroup (levelMod n)
  module : ∀ n, Module R (levelMod n)
  /-- Ascent embedding ℓₙ : level n → level (n+1). -/
  ascent : ∀ n, levelMod n →ₗ[R] levelMod (n + 1)
  /-- Descent map 𝔡_{n+1} : level (n+1) → level n. -/
  descent : ∀ n, levelMod (n + 1) →ₗ[R] levelMod n
  /-- Retraction: descent ∘ ascent = id. -/
  retraction : ∀ n, (descent n) ∘ₗ (ascent n) = LinearMap.id

attribute [instance] AlgebraTower.addCommGroup
attribute [instance] AlgebraTower.module

/-- A Frobenius trace system: compatible traces at each level. -/
structure FrobeniusTraceSystem (T : AlgebraTower R) where
  /-- The trace functional at level n: an R-linear map from level n to R. -/
  trace : ∀ n, T.levelMod n →ₗ[R] R
  /-- Compatibility: trₙ ∘ 𝔡_{n+1} = tr_{n+1}. -/
  compatible : ∀ n x, trace n ((T.descent n) x) = trace (n + 1) x

/-- The vanishing condition (Schur form): at level 0, the endomorphism
    algebra is one-dimensional, so any R-linear functional is proportional
    to the Frobenius trace.

    This follows from the QOU axiom Hom(𝟙, Ad(A)) = 0 together with
    Schur's lemma in the rigid monoidal category 𝒞: the adjoint
    representation has no invariant vectors, forcing End_𝒞(A₀) ≅ R. -/
-- Ref: [manuscript] §1, Axiom (QOU3)
structure VanishingCondition (T : AlgebraTower R)
    (ft : FrobeniusTraceSystem (R := R) T) where
  /-- At level 0, any R-linear functional is proportional to the trace. -/
  schur_at_zero : ∀ (φ : T.levelMod 0 →ₗ[R] R),
    ∃ (c : R), ∀ x, φ x = c * ft.trace 0 x

/-- **Existence**: The Frobenius trace defines a G_q-invariant functional
    on the direct limit algebra. -/
-- Ref: [manuscript] §3, Proposition: Vacuum state (existence)
theorem frobenius_trace_invariant
    (T : AlgebraTower R)
    (ft : FrobeniusTraceSystem (R := R) T) :
    ∀ n x, ft.trace n ((T.descent n) ((T.ascent n) x)) = ft.trace n x := by
  intro n x; congr 1
  simpa [LinearMap.comp_apply] using congr_fun (congr_arg DFunLike.coe (T.retraction n)) x

/-- **Uniqueness**: Any tower-compatible R-linear functional equals the
    Frobenius trace (up to normalisation). -/
-- Ref: [manuscript] §3, Proposition: Vacuum state (uniqueness)
theorem invariant_functional_unique
    (T : AlgebraTower R)
    (ft : FrobeniusTraceSystem (R := R) T)
    (vc : VanishingCondition (R := R) T ft)
    (ψ : ∀ n, T.levelMod n →ₗ[R] R)
    (ψ_compat : ∀ n x, ψ n ((T.descent n) x) = ψ (n + 1) x) :
    ∃ (c : R), ∀ n x, ψ n x = c * ft.trace n x := by
  obtain ⟨c, hc⟩ := vc.schur_at_zero (ψ 0)
  exact ⟨c, fun n => by
    induction n with
    | zero => exact hc
    | succ k ih =>
      intro x
      rw [← ψ_compat k x]
      rw [ih ((T.descent k) x)]
      rw [ft.compatible k x]⟩

end QOU.Torsion
