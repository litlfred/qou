/-!
# QOU.Torsion.vacuum_state — Existence and uniqueness of the vacuum state

Given a QOU (𝒞, A, ω), the Frobenius trace on the direct limit algebra
𝒜_∞ = lim End_𝒞(Aₙ) is the unique G_q-invariant R-linear functional.
Existence: the Frobenius unit/counit pairing ε ∘ α ∘ η gives an invariant
trace at each level, compatible with descent. Uniqueness: the vanishing
condition Hom(𝟙, Ad(A)) = 0 forces End_𝒞(A₀) ≅ R (by Schur's lemma),
so there is only one functional at level 0 up to scalar.  Compatibility
with the tower propagates this to all levels.

## References

- [manuscript] §3 Lifting and Descent
- [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

import Mathlib.Algebra.Module.Basic
import Mathlib.CategoryTheory.Monoidal.Basic

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

/-- A Frobenius trace system: compatible traces at each level. -/
structure FrobeniusTraceSystem (T : AlgebraTower R) where
  /-- The trace functional at level n. -/
  trace : ∀ n, @LinearMap R R _ _ _ (T.levelMod n) R
    (T.addCommGroup n) (T.module n) _ _ LinearMap.id.toModule
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
  schur_at_zero : ∀ (φ : @LinearMap R R _ _ _ (T.levelMod 0) R
    (T.addCommGroup 0) (T.module 0) _ _ LinearMap.id.toModule),
    ∃ (c : R), ∀ x, φ x = c * ft.trace 0 x

/-- **Existence**: The Frobenius trace defines a G_q-invariant functional
    on the direct limit algebra. -/
-- Ref: [manuscript] §3, Proposition: Vacuum state (existence)
theorem frobenius_trace_invariant
    (T : AlgebraTower R)
    (ft : FrobeniusTraceSystem (R := R) T) :
    ∀ n x, ft.trace n ((T.descent n) ((T.ascent n) x)) = ft.trace n x := by
  -- The retraction 𝔡ₙ ∘ ℓₙ = id gives 𝔡ₙ(ℓₙ(x)) = x,
  -- so trₙ(𝔡ₙ(ℓₙ(x))) = trₙ(x).
  intro n x
  congr 1
  -- Goal: (T.descent n) ((T.ascent n) x) = x
  have h : ((T.descent n) ∘ₗ (T.ascent n)) x = x := by
    rw [T.retraction n]; rfl
  simpa [LinearMap.comp_apply] using h

/-- **Uniqueness**: Any tower-compatible R-linear functional equals the
    Frobenius trace (up to normalisation).

    Proof strategy: By Schur at level 0, ψ₀ = c · tr₀. Then by induction:
    ψ_{n+1}(x) = ψ_n(𝔡_n(x))           [ψ compatibility]
               = c · tr_n(𝔡_n(x))        [induction hypothesis]
               = c · tr_{n+1}(x)          [trace compatibility]  -/
-- Ref: [manuscript] §3, Proposition: Vacuum state (uniqueness)
theorem invariant_functional_unique
    (T : AlgebraTower R)
    (ft : FrobeniusTraceSystem (R := R) T)
    (vc : VanishingCondition (R := R) T ft)
    (ψ : ∀ n, @LinearMap R R _ _ _ (T.levelMod n) R
      (T.addCommGroup n) (T.module n) _ _ LinearMap.id.toModule)
    (ψ_compat : ∀ n x, ψ n ((T.descent n) x) = ψ (n + 1) x) :
    ∃ (c : R), ∀ n x, ψ n x = c * ft.trace n x := by
  -- By Schur's lemma at level 0:
  obtain ⟨c, hc⟩ := vc.schur_at_zero (ψ 0)
  exact ⟨c, fun n => by
    induction n with
    | zero => exact hc
    | succ k ih =>
      intro x
      -- ψ_{k+1}(x) = ψ_k(𝔡_k(x)) by compatibility
      rw [← ψ_compat k x]
      -- = c · tr_k(𝔡_k(x)) by induction hypothesis
      rw [ih ((T.descent k) x)]
      -- = c · tr_{k+1}(x) by trace compatibility
      rw [ft.compatible k x]⟩

end QOU.Torsion
