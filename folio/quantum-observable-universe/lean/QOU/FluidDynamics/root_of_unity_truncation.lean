import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.FluidDynamics.root_of_unity_truncation

Root-of-unity truncation (conditional on the q-NS cone).
Synchronised with the chapter sibling
`fluid-dynamics/root-of-unity-truncation.lean` so the decoy hypothesis
`root_unity_truncated` is eliminated and both copies state the same
`RootOfUnityTruncationContext` (bean `qou-klr1`).

Ref: [leitner2026] §Fluid dynamics / Root-of-unity truncation,
     prop:root-of-unity-truncation
-/

namespace QOU.FluidDynamics

/-- **Conditional hypotheses for the root-of-unity truncation.**

    The proposition is conditional on the q-NS conjecture cone
    (`conj:q-aubin-lions`, `conj:ns-counterexample`,
    `conj:critical-exponent`, `prop:blowup-yekutieli`,
    `conj:regularity-breakdown`) and on the `q`-Laplacian spectral
    tower truncation (`prop:q-laplacian-spectral-tower`).  Rather than
    concluding the vacuous `True` or routing through a decoy
    `root_unity_truncated` implication, this class carries the analytic
    facts the proposition actually asserts as **explicit
    hypotheses**, and `root_of_unity_truncation_conditional`
    bundles their conjunction (§3b-cond conditional pattern).

    **2026-11-15 (owner decision, PR #7747, bean `qou-fm7s`).** The field
    `leviNonDegenerate` ("the Levi form stays non-degenerate at
    collision") is replaced by `coreBounded` ("`κ(t) = O(1)`"). -/
class RootOfUnityTruncationContext where
  /-- Collision time `T*`. -/
  tStar : ℝ
  /-- Universal Bernstein constant `C > 0`. -/
  C : ℝ
  /-- Root-of-unity truncation level `κ` (`q = e^{iπ/κ}`). -/
  truncationLevel : ℝ
  /-- Vortex-core aspect ratio `κ(t) = a_⊥/a_∥`. -/
  coreAspect : ℝ → ℝ
  /-- Proposition "NS blows up at the collision". -/
  nsBlowsUp : Prop
  /-- Proposition "the core aspect ratio stays bounded, `κ(t) = O(1)`". -/
  coreBounded : Prop
  /-- **Bounded-degree core bound.**  At a root of unity the core
      boundary is a trigonometric polynomial of degree `≤ (κ-1)/2`,
      so by Bernstein the aspect ratio obeys
      `κ(t) ≤ 1 + C·(κ-1)` for `t < T*` (the hard finite-rank cutoff,
      not the soft generic damping). -/
  core_bound :
    ∀ t : ℝ, t < tStar → coreAspect t ≤ 1 + C * (truncationLevel - 1)
  /-- **Boxed equivalence (conditional).**  NS blows up at the
      collision **iff** the core aspect ratio stays bounded,
      `κ(t) = O(1)`.  Carried as a hypothesis from the conjectural
      cone. -/
  blowup_iff_coreBounded : nsBlowsUp ↔ coreBounded

/-- **Root-of-unity truncation (conditional).**

    **Assumed, not derived here:** `core_bound` and `blowup_iff_coreBounded`
    are carried as fields of `[RootOfUnityTruncationContext]` (from the open
    q-NS conjecture cone); this theorem bundles their conjunction for the
    `lean.ref` target `qou:QOU.FluidDynamics.root_of_unity_truncation_conditional`. -/
-- Ref: [leitner2026] prop:root-of-unity-truncation
theorem root_of_unity_truncation_conditional
    [ctx : RootOfUnityTruncationContext] :
    (∀ t : ℝ, t < ctx.tStar →
        ctx.coreAspect t ≤ 1 + ctx.C * (ctx.truncationLevel - 1)) ∧
    (ctx.nsBlowsUp ↔ ctx.coreBounded) := by
  exact ⟨ctx.core_bound, ctx.blowup_iff_coreBounded⟩

/-- Alias preserving the module-matching declaration name `root_of_unity_truncation`.
    **Assumed, not derived here:** projects `root_of_unity_truncation_conditional`
    from `[RootOfUnityTruncationContext]`. -/
-- Ref: [leitner2026] prop:root-of-unity-truncation
theorem root_of_unity_truncation
    [ctx : RootOfUnityTruncationContext] :
    (∀ t : ℝ, t < ctx.tStar →
        ctx.coreAspect t ≤ 1 + ctx.C * (ctx.truncationLevel - 1)) ∧
    (ctx.nsBlowsUp ↔ ctx.coreBounded) := by
  exact root_of_unity_truncation_conditional

/-- **Degenerate-level specialization (proved):** at truncation level `κ = 1`
    (zero active non-constant modes), the Bernstein bound `core_bound` forces
    the core aspect ratio to obey `coreAspect t ≤ 1` for all `t < tStar`. -/
-- Ref: [leitner2026] prop:root-of-unity-truncation
theorem root_of_unity_truncation_core_at_one
    [ctx : RootOfUnityTruncationContext]
    (hκ : ctx.truncationLevel = 1) (t : ℝ) (ht : t < ctx.tStar) :
    ctx.coreAspect t ≤ 1 := by
  have hb := ctx.core_bound t ht
  rw [hκ] at hb
  linarith

end QOU.FluidDynamics
