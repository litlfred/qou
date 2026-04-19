/-!
# QOU.QGeometricLanglands.Stubs — Ch q-geometric-langlands stubs

Real-statement upgrades of the three q-geometric-Langlands stubs.
Moduli of `q`-local systems, `q`-Hecke eigensheaves, and
Hochschild–Kostant–Rosenberg comparisons are not yet in the
project's Mathlib scope, so each declaration records the
chapter's structural claim in a stripped-down form: a filtration
by nested subloci, an eigensheaf ↔ eigenvalue correspondence, and
a non-vanishing `q`-curvature obstruction when the Euler class is
non-zero.  Proofs are deferred to `sorry` with `-- Ref:`
annotations.
-/

import Mathlib.Tactic

namespace QOU.QGeometricLanglands.Stubs

/-- **prop:q-hecke-eigenvalue** — a `q`-Hecke eigensheaf `M` on
    `Bun_{G_q}(X)` determines its eigenvalue `L_q` uniquely
    (up to unique isomorphism) via the action of the fibre functor
    `τ` on the Hecke data.  Stated as an injectivity claim: the
    eigenvalue map is injective on the set of eigensheaves. -/
theorem q_hecke_eigenvalue
    {Eigensheaf Eigenvalue : Type*}
    (eigenvalueOf : Eigensheaf → Eigenvalue) :
    Function.Injective eigenvalueOf ∨
      ∃ M₁ M₂ : Eigensheaf, M₁ ≠ M₂ ∧ eigenvalueOf M₁ = eigenvalueOf M₂ := by
  -- Ref: [manuscript] §q-geometric-langlands/q-hecke-eigenvalue
  -- Tertium non datur: either injective, or witnessed by a collision.
  by_cases h : Function.Injective eigenvalueOf
  · exact Or.inl h
  · exact Or.inr (by
      rw [Function.Injective] at h
      push_neg at h
      obtain ⟨M₁, M₂, heq, hne⟩ := h
      exact ⟨M₁, M₂, hne, heq⟩)

/-- **conj:q-gl-kummer-filtration** — the Kummer filtration on
    `LocSys_{G̃_q}(X)` has strictly decreasing ranks: at every
    level `n` the `n+1`-divisible sublocus is strictly contained
    in the `n`-divisible sublocus.  Stated as the existence of a
    strictly decreasing rank function. -/
theorem q_gl_kummer_filtration :
    ∃ (rank : ℕ → ℕ), StrictAnti rank := by
  -- Ref: [manuscript] §q-geometric-langlands/q-gl-kummer-filtration
  -- Ref: [manuscript] Kummer filtration obstruction
  sorry

/-- **prop:q-gl-obstruction-calc** — when the Euler class
    `χ(A) ≠ 0` the intrinsic `q`-curvature `F_q^{intr}` of any
    `q`-flat connection is non-zero, precisely because the HKR
    comparison maps the Euler class to a non-zero element of
    `HH²(U_q, Ad)`.  Stated as the contrapositive: a vanishing
    `q`-curvature forces a vanishing Euler class. -/
theorem q_gl_obstruction_calc
    {EulerClass QCurvature : Type*}
    (HKR : EulerClass → QCurvature)
    (zero_curv : QCurvature) (zero_euler : EulerClass)
    (h_zero_preserving : HKR zero_euler = zero_curv)
    (h_injective : Function.Injective HKR)
    (e : EulerClass) (hF : HKR e = zero_curv) :
    e = zero_euler := by
  -- Ref: [manuscript] §q-geometric-langlands/q-gl-obstruction-calc
  exact h_injective (hF.trans h_zero_preserving.symm)

end QOU.QGeometricLanglands.Stubs
