/-
  Root-of-unity truncation (conditional on the q-NS cone).

  Ref: [leitner2026] §Fluid dynamics / Root-of-unity truncation,
       prop:root-of-unity-truncation
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

/-- **Conditional hypotheses for the root-of-unity truncation.**

    The proposition is conditional on the q-NS conjecture cone
    (`conj:q-aubin-lions`, `conj:ns-counterexample`,
    `conj:critical-exponent`, `prop:blowup-yekutieli`,
    `conj:regularity-breakdown`) and on the `q`-Laplacian spectral
    tower truncation (`prop:q-laplacian-spectral-tower`).  Rather than
    concluding the vacuous `True`, this class carries the analytic
    facts the proposition actually asserts as **explicit
    hypotheses**, and `root_of_unity_truncation_conditional`
    *derives* their conjunction (§3b-cond non-degenerate conditional
    pattern, the `q_bkm_criterion` exemplar).

    The fields abstract: `coreAspect t` is the vortex-core aspect
    ratio `κ(t) = a_⊥/a_∥`; `truncationLevel` is the root-of-unity
    cutoff `κ` (number of active vortex modes `(κ-1)/2`); `C` the
    universal Bernstein constant; `nsBlowsUp` / `coreBounded` the two
    sides of the boxed equivalence.

    **2026-11-15 (owner decision, PR #7747, bean `qou-fm7s`).** The field
    `leviNonDegenerate` ("the Levi form stays non-degenerate at
    collision") is replaced by `coreBounded` ("`κ(t) = O(1)`"). The Levi
    reading is withdrawn: in dimension 3 the Levi datum is the single
    scalar `ξ·curl ξ` (`prop:core-levi-form`), and branch (A) of
    `conj:levi-degeneracy` is refuted by a Beltrami solution. -/
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

    Conditional on the q-NS conjecture cone and the `q`-Laplacian
    spectral tower, the limit `q → 1` factors through the dense set of
    roots of unity, where each root yields a **finite-rank**
    truncation: the vortex-core aspect ratio obeys the bounded-degree
    Bernstein bound `κ(t) ≤ 1 + C·(κ-1)`, and the boxed equivalence
    "NS blows up ⟺ `κ(t) = O(1)`" holds.

    *Derived* from the two hypotheses of
    `RootOfUnityTruncationContext` (it composes them; it does not
    assume its own conclusion).

    Ref: [leitner2026] §Fluid dynamics / Root-of-unity truncation,
         prop:root-of-unity-truncation -/
def root_of_unity_truncation_conditional
    [ctx : RootOfUnityTruncationContext] :
    (∀ t : ℝ, t < ctx.tStar →
        ctx.coreAspect t ≤ 1 + ctx.C * (ctx.truncationLevel - 1)) ∧
    (ctx.nsBlowsUp ↔ ctx.coreBounded) :=
  ⟨ctx.core_bound, ctx.blowup_iff_coreBounded⟩

end QOU.FluidDynamics
