/-!
# QOU.Torsion.vacuum_state — Existence and uniqueness of the vacuum state

Given a QOU (𝒞, A, ω), the Frobenius trace on the direct limit algebra
𝒜_∞ = lim End_𝒞(Aₙ) is the unique G_q-invariant R-linear functional.
Existence: the Frobenius unit/counit pairing ε ∘ α ∘ η gives an invariant
trace at each level, compatible with descent. Uniqueness: the vanishing
condition Hom(𝟙, Ad(A)) = 0 forces the G_q-fixed subalgebra to be
one-dimensional, by Schur's lemma in 𝒞.

## References

- [leitner2026] §3 Lifting and Descent
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

/-- The vanishing condition: the G_q-fixed subalgebra is one-dimensional.
    Categorically: Hom(𝟙, Ad(A)) = 0. -/
-- Ref: [leitner2026] §1, Axiom (QOU3)
structure VanishingCondition (T : AlgebraTower R) where
  /-- The identity element at each level. -/
  one : ∀ n, T.levelMod n
  /-- Every invariant element is a scalar multiple of the identity. -/
  invariant_is_scalar : ∀ n (x : T.levelMod n),
    (∀ m, (T.descent m) ((T.ascent m) x) = x) →
    ∃ (r : R), x = r • (one n)

/-- **Existence**: The Frobenius trace defines a G_q-invariant functional
    on the direct limit algebra. -/
-- Ref: [leitner2026] §3, Proposition: Vacuum state (existence)
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

/-- **Uniqueness**: Any G_q-invariant functional equals the Frobenius trace
    (up to normalisation), by the vanishing condition and Schur's lemma. -/
-- Ref: [leitner2026] §3, Proposition: Vacuum state (uniqueness)
theorem invariant_functional_unique
    (T : AlgebraTower R)
    (vc : VanishingCondition (R := R) T)
    (ft : FrobeniusTraceSystem (R := R) T)
    (ψ : ∀ n, @LinearMap R R _ _ _ (T.levelMod n) R
      (T.addCommGroup n) (T.module n) _ _ LinearMap.id.toModule)
    (ψ_compat : ∀ n x, ψ n ((T.descent n) x) = ψ (n + 1) x)
    (ψ_inv : ∀ n x, ψ n ((T.descent n) ((T.ascent n) x)) = ψ n x) :
    ∃ (c : R), ∀ n x, ψ n x = c • ft.trace n x := by
  -- Proof sketch (requires non-degeneracy of tr, not yet in hypotheses):
  -- 1. Define δₙ = ψₙ - c · trₙ for c = ψ₀(1₀) / tr₀(1₀).
  -- 2. δₙ is compatible (δₙ ∘ 𝔡ₙ = δ_{n+1}) and invariant (δₙ ∘ τₙ = δₙ).
  -- 3. For any G_q-fixed x, the vanishing condition gives x = r · 1,
  --    so δₙ(x) = r · δₙ(1) = r · (ψ(1) - c · tr(1)) = 0 by choice of c.
  -- 4. Extend to all x by decomposing via descent eigenspaces.
  -- Requires: tr(1) ≠ 0 (non-degeneracy), which follows from
  -- the faithfulness of the fibre functor in the QOU axioms.
  -- Ref: [leitner2026] §3, Proposition: Vacuum state (uniqueness)
  sorry

end QOU.Torsion
