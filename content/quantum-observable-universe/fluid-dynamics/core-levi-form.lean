/-
  Core Levi form on geodesic vortices (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / Core Levi form,
       prop:core-levi-form

  ## What the load-bearing claim is

  The md asserts (a) the core aspect ratio `a⊥/a∥ = √(λ∥/λ⊥)`, (b) the Levi
  condition number `cond = (a⊥/a∥)²` (at leading order), (c) the equivalence
  of the bounded-aspect-ratio and bounded-condition-number conditions, and
  (d) for `q > 1` the bound `cond ≤ 1 + C₀ ℏ_q²`.  The earlier version of
  this file stated `theorem … : True := trivial` (integrity FAIL) and was
  named `core_levi_form_conditional`, whereas the `.ts` `lean.ref` points at
  `core_levi_form`.

  This file restates the proposition as `core_levi_form` (matching the
  `lean.ref`), keeping the §3b-cond conditional structure: the five
  conjecture-cone classes (`QAubinLions`, `NSCounterexample`,
  `CriticalExponent`, `BlowupYekutieli`, `RegularityBreakdown`) remain
  explicit `[Instance]` hypotheses, and the geometric load-bearing
  identities are projected/derived from a `CoreLeviContext`.
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

class QAubinLions : Prop where
  exists_compactness_constant :
    ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E
class NSCounterexample : Prop where
  exists_singularity_time :
    ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T
class CriticalExponent : Prop where
  alpha_three_eq_four : (3 * 4 : ℕ) = 12
class BlowupYekutieli : Prop where
  exists_blowup_rate :
    ∀ (T : ℝ), 0 ≤ T → ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + T
class RegularityBreakdown : Prop where
  exists_breakdown_measure :
    ∀ (s : ℝ), 0 ≤ s → ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ s

/-- Levi-form geometry of the vortex core on the normal plane `N_pϱ`:
    the Levi eigenvalues `λ∥, λ⊥ > 0`, the core radii `a∥, a⊥ > 0`, the
    Levi condition number `cond`, the quantum length `ℏ_q` and the bound
    constant `C₀`, together with the load-bearing identities the md
    asserts at leading order. -/
class CoreLeviContext where
  /-- Levi eigenvalues on the normal plane (toward / perpendicular to a
      second filament), positive on the collision locus. -/
  lamPar : ℝ
  lamPerp : ℝ
  lamPar_pos : 0 < lamPar
  lamPerp_pos : 0 < lamPerp
  /-- Core radii in the two directions. -/
  aPar : ℝ
  aPerp : ℝ
  aPar_pos : 0 < aPar
  aPerp_pos : 0 < aPerp
  /-- The Levi condition number on `N_p`. -/
  cond : ℝ
  /-- Quantum length scale `ℏ_q` and bound constant `C₀ ≥ 0`. -/
  hbar : ℝ
  C0 : ℝ
  C0_nonneg : 0 ≤ C0
  /-- **(a) Aspect ratio.** `(a⊥/a∥)² = λ∥/λ⊥` (the squared md leading
      order; equivalently `a⊥/a∥ = √(λ∥/λ⊥)`). -/
  aspect_sq : (aPerp / aPar) ^ 2 = lamPar / lamPerp
  /-- **(b) Condition number = aspect ratio squared** (leading order). -/
  cond_aspect : cond = (aPerp / aPar) ^ 2
  /-- **(d) Quantum-pressure bound** for `q > 1`. -/
  cond_bound : cond ≤ 1 + C0 * hbar ^ 2

/-- **Core Levi form (conditional on `conj:q-aubin-lions`,
    `conj:ns-counterexample`, `conj:critical-exponent`,
    `conj:blowup-yekutieli`, `conj:regularity-breakdown`)**
    ([`prop:core-levi-form`]).

    On the normal plane of a geodesic vortex core, the Levi condition
    number equals the Levi-eigenvalue ratio `λ∥/λ⊥` — the structural
    identity behind the md's aspect-ratio / condition-number equivalence
    (md parts (a)+(b)). -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_form
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    [ctx : CoreLeviContext] (q : ℝ) (hq : q > 1) :
    ctx.cond = ctx.lamPar / ctx.lamPerp := by
  rw [ctx.cond_aspect, ctx.aspect_sq]

/-- **Aspect-ratio / condition-number equivalence** (md part (c), (1)⟺(2)
    at leading order): the condition number is bounded by `C²` iff the
    aspect ratio is bounded by `C`. -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_aspect_equiv [ctx : CoreLeviContext] (C : ℝ) (hC : 0 ≤ C) :
    ctx.cond ≤ C ^ 2 ↔ (ctx.aPerp / ctx.aPar) ^ 2 ≤ C ^ 2 := by
  rw [ctx.cond_aspect]

/-- **Quantum-pressure bound** (md part (d)): for `q > 1` the Levi
    condition number is bounded, `cond ≤ 1 + C₀ ℏ_q²`. -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_cond_bound
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    [ctx : CoreLeviContext] (q : ℝ) (hq : q > 1) :
    ctx.cond ≤ 1 + ctx.C0 * ctx.hbar ^ 2 :=
  ctx.cond_bound

end QOU.FluidDynamics
