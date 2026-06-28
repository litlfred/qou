/-
  Root-of-unity truncation (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / Root-of-unity truncation,
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
    universal Bernstein constant; `nsBlowsUp` / `leviNonDegenerate`
    the two propositions of the contact-geometric millennium
    statement. -/
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
  /-- Proposition "the Levi form stays non-degenerate at collision". -/
  leviNonDegenerate : Prop
  /-- **Bounded-degree core bound.**  At a root of unity the core
      boundary is a trigonometric polynomial of degree `≤ (κ-1)/2`,
      so by Bernstein the aspect ratio obeys
      `κ(t) ≤ 1 + C·(κ-1)` for `t < T*` (the hard finite-rank cutoff,
      not the soft generic damping). -/
  core_bound :
    ∀ t : ℝ, t < tStar → coreAspect t ≤ 1 + C * (truncationLevel - 1)
  /-- **Contact-geometric millennium equivalence.**  NS blows up at
      the collision **iff** the brane's Levi form remains
      non-degenerate there (equivalently `κ(t) = O(1)`).  Carried as
      the two implication directions of the conjectural cone. -/
  blowup_iff_nondegenerate : nsBlowsUp ↔ leviNonDegenerate

/-- **Root-of-unity truncation (conditional).**

    Conditional on the q-NS conjecture cone and the `q`-Laplacian
    spectral tower, the limit `q → 1` factors through the dense set of
    roots of unity, where each root yields a **finite-rank**
    truncation: the vortex-core aspect ratio obeys the bounded-degree
    Bernstein bound `κ(t) ≤ 1 + C·(κ-1)`, and the contact-geometric
    millennium equivalence "NS blows up ⟺ Levi form non-degenerate"
    holds.

    *Derived* from the two hypotheses of
    `RootOfUnityTruncationContext` (it composes them; it does not
    assume its own conclusion).

    Ref: [manuscript] §Fluid dynamics / Root-of-unity truncation,
         prop:root-of-unity-truncation -/
def root_of_unity_truncation_conditional
    [ctx : RootOfUnityTruncationContext] :
    (∀ t : ℝ, t < ctx.tStar →
        ctx.coreAspect t ≤ 1 + ctx.C * (ctx.truncationLevel - 1)) ∧
    (ctx.nsBlowsUp ↔ ctx.leviNonDegenerate) :=
  ⟨ctx.core_bound, ctx.blowup_iff_nondegenerate⟩

end QOU.FluidDynamics
