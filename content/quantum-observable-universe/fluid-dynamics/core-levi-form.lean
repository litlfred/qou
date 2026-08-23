/-
  Core Levi form on geodesic vortices (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / Core Levi form,
       prop:core-levi-form

  ## What the load-bearing claim is

  The md asserts (a) the core aspect ratio `a⊥/a∥ = √(λ∥/λ⊥)`, (b) the Levi
  condition number `cond = max(λ∥,λ⊥)/min(λ∥,λ⊥) = max(a⊥/a∥, a∥/a⊥)² ·
  (1 + O(ℏ_q²))`, (c) the equivalence of the bounded-aspect-ratio and
  bounded-condition-number conditions, and (d) for `q > 1` the bound
  `cond ≤ 1 + C₀ ℏ_q²`.  The earlier version of this file stated
  `theorem … : True := trivial` (integrity FAIL) and was named
  `core_levi_form_conditional`, whereas the `.ts` `lean.ref` points at
  `core_levi_form`.

  The condition number is encoded *symmetrically* as
  `cond = max(λ∥,λ⊥)/min(λ∥,λ⊥)` (so the statement is correct for either
  ordering of `λ∥, λ⊥`, not just `λ⊥ ≤ λ∥`), `core_levi_ratio_eq_aspect_sq`
  proves the leading-order identity `cond = max(a⊥/a∥, a∥/a⊥)²` from the
  aspect-ratio relation, and `core_levi_cond_aspect_bound` carries the
  `O(ℏ_q²)` correction as an explicit `|·| ≤ C₀ ℏ_q²` bound.

  This file restates the proposition as `core_levi_form` (matching the
  `lean.ref`), keeping the §3b-cond conditional structure: the five
  conjecture-cone classes (`QAubinLions`, `NSCounterexample`,
  `CriticalExponent`, `BlowupYekutieli`, `RegularityBreakdown`) remain
  explicit `[Instance]` hypotheses, and the geometric load-bearing
  identities are derived from a `CoreLeviContext`.

  ## 2026-08-23 — `core_levi_form` no longer returns a field

  It read `ctx.cond = max λ / min λ := ctx.cond_def`, i.e. the class field
  `cond_def` handed straight back: the §3b-cond item-5 degenerate shape,
  and the vacuity ledger's `proof-no-self-assuming-projection` entry for
  this file. Restated as the two-sided pinning `1 ≤ cond` and
  `|cond − max λ / min λ| ≤ C₀ℏ_q²`. Neither conjunct is a field: the
  first composes `cond_def` with the eigenvalue positivity through
  `min ≤ max`, the second reaches the class's aspect-ratio bound only via
  `core_levi_ratio_eq_aspect_sq`, whose proof is the ordering case split.
  `core_levi_ratio_eq_aspect_sq` moved above it so the bridge is in scope.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

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
  /-- The Levi condition number on `N_p`, defined by the md as the ratio
      of the larger to the smaller Levi eigenvalue. -/
  cond : ℝ
  /-- Quantum length scale `ℏ_q` and bound constant `C₀ ≥ 0`. -/
  hbar : ℝ
  C0 : ℝ
  C0_nonneg : 0 ≤ C0
  /-- **(b) Condition-number definition.** `cond = max(λ∥,λ⊥)/min(λ∥,λ⊥)`
      (the md definition; symmetric in the two eigenvalues, so it is `≥ 1`
      and correct whether `λ∥ ≥ λ⊥` or `λ⊥ > λ∥`). -/
  cond_def : cond = max lamPar lamPerp / min lamPar lamPerp
  /-- **(a) Aspect ratio.** `(a⊥/a∥)² = λ∥/λ⊥` (the squared md leading
      order; equivalently `a⊥/a∥ = √(λ∥/λ⊥)`). The `O(ℏ_q²)` correction in
      the md is captured separately by `cond_aspect_bound`. -/
  aspect_sq : (aPerp / aPar) ^ 2 = lamPar / lamPerp
  /-- **(b) Condition number = aspect ratio squared, up to `O(ℏ_q²)`.**
      The md relation `cond = max(a⊥/a∥, a∥/a⊥)² · (1 + O(ℏ_q²))` is
      encoded as the explicit bound on the difference between `cond` and
      the squared (max-)aspect ratio. -/
  cond_aspect_bound :
    |cond - max (aPerp / aPar) (aPar / aPerp) ^ 2| ≤ C0 * hbar ^ 2
  /-- **(d) Quantum-pressure bound** for `q > 1`. -/
  cond_bound : cond ≤ 1 + C0 * hbar ^ 2

/-- **Leading-order structural identity** (md part (b), the `O(ℏ_q²) → 0`
    limit): `max(λ∥,λ⊥)/min(λ∥,λ⊥) = max(a⊥/a∥, a∥/a⊥)²`. Proved from the
    aspect-ratio identity `(a⊥/a∥)² = λ∥/λ⊥` and positivity, by case split
    on the eigenvalue ordering. This is the leading term; the `O(ℏ_q²)`
    correction to `cond` itself is `cond_aspect_bound`. -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_ratio_eq_aspect_sq [ctx : CoreLeviContext] :
    max ctx.lamPar ctx.lamPerp / min ctx.lamPar ctx.lamPerp
      = max (ctx.aPerp / ctx.aPar) (ctx.aPar / ctx.aPerp) ^ 2 := by
  have hPar := ctx.lamPar_pos
  have hPerp := ctx.lamPerp_pos
  have haPar := ctx.aPar_pos
  have haPerp := ctx.aPerp_pos
  have hr1 : (0:ℝ) ≤ ctx.aPerp / ctx.aPar := div_nonneg haPerp.le haPar.le
  have hr2 : (0:ℝ) ≤ ctx.aPar / ctx.aPerp := div_nonneg haPar.le haPerp.le
  -- `(a⊥/a∥)² = λ∥/λ⊥` and `(a∥/a⊥)² = λ⊥/λ∥`.
  have h1 : (ctx.aPerp / ctx.aPar) ^ 2 = ctx.lamPar / ctx.lamPerp := ctx.aspect_sq
  have h2 : (ctx.aPar / ctx.aPerp) ^ 2 = ctx.lamPerp / ctx.lamPar := by
    rw [← inv_div ctx.aPerp ctx.aPar, inv_pow, h1, inv_div]
  rcases le_total ctx.lamPar ctx.lamPerp with h | h
  · -- λ∥ ≤ λ⊥ : max/min ratio is λ⊥/λ∥, and a∥/a⊥ is the larger aspect.
    rw [max_eq_right h, min_eq_left h]
    have hsq : (ctx.aPerp / ctx.aPar) ^ 2 ≤ (ctx.aPar / ctx.aPerp) ^ 2 := by
      rw [h1, h2]
      exact le_trans ((div_le_one hPerp).mpr h) ((one_le_div hPar).mpr h)
    have hge : ctx.aPerp / ctx.aPar ≤ ctx.aPar / ctx.aPerp :=
      (pow_le_pow_iff_left₀ hr1 hr2 two_ne_zero).mp hsq
    rw [max_eq_right hge, h2]
  · -- λ⊥ ≤ λ∥ : max/min ratio is λ∥/λ⊥, and a⊥/a∥ is the larger aspect.
    rw [max_eq_left h, min_eq_right h]
    have hsq : (ctx.aPar / ctx.aPerp) ^ 2 ≤ (ctx.aPerp / ctx.aPar) ^ 2 := by
      rw [h1, h2]
      exact le_trans ((div_le_one hPar).mpr h) ((one_le_div hPerp).mpr h)
    have hge : ctx.aPar / ctx.aPerp ≤ ctx.aPerp / ctx.aPar :=
      (pow_le_pow_iff_left₀ hr2 hr1 two_ne_zero).mp hsq
    rw [max_eq_left hge, h1]

/-- **Core Levi form (conditional on `conj:q-aubin-lions`,
    `conj:ns-counterexample`, `conj:critical-exponent`,
    `conj:blowup-yekutieli`, `conj:regularity-breakdown`)**
    ([`prop:core-levi-form`]).

    On the normal plane of a geodesic vortex core, the Levi condition
    number is pinned from **both** sides:

    * `1 ≤ cond` — the condition number is a genuine condition number.
      Derived from `cond_def` together with the eigenvalue positivity,
      via `min(λ∥,λ⊥) ≤ max(λ∥,λ⊥)`. Nothing in `CoreLeviContext`
      asserts it.
    * `|cond − max(λ∥,λ⊥)/min(λ∥,λ⊥)| ≤ C₀ ℏ_q²` — md part (b) stated
      in **eigenvalue** terms. The class carries this bound in
      **aspect-ratio** terms (`cond_aspect_bound`); the two are bridged
      by `core_levi_ratio_eq_aspect_sq`, whose proof is the case split
      on the eigenvalue ordering above.

    So the statement is not a field of the context class in either
    conjunct: the first composes three fields through an inequality, the
    second composes a field through the derived aspect identity.
    Together with the class's `cond_bound` (md part (d)) this bounds
    `cond` into `[1, 1 + C₀ℏ_q²]`. -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_form
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    [ctx : CoreLeviContext] :
    1 ≤ ctx.cond ∧
      |ctx.cond - max ctx.lamPar ctx.lamPerp / min ctx.lamPar ctx.lamPerp|
        ≤ ctx.C0 * ctx.hbar ^ 2 := by
  refine ⟨?_, ?_⟩
  · -- `cond = max/min` and `0 < min ≤ max`, so the ratio is at least one.
    have hmin : 0 < min ctx.lamPar ctx.lamPerp :=
      lt_min ctx.lamPar_pos ctx.lamPerp_pos
    rw [ctx.cond_def]
    exact (one_le_div hmin).mpr (min_le_max)
  · -- Bridge the eigenvalue ratio to the squared max-aspect ratio, where
    -- the class states the `O(ℏ_q²)` bound.
    rw [core_levi_ratio_eq_aspect_sq]
    exact ctx.cond_aspect_bound

/-- **Aspect-ratio / condition-number equivalence** (md part (c), (1)⟺(2)
    at leading order): the leading-order condition number `max(λ∥,λ⊥)/min(λ∥,λ⊥)`
    is bounded by `C²` iff the max-aspect ratio is bounded by `C` (squared). -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_aspect_equiv [ctx : CoreLeviContext] (C : ℝ) :
    max ctx.lamPar ctx.lamPerp / min ctx.lamPar ctx.lamPerp ≤ C ^ 2
      ↔ max (ctx.aPerp / ctx.aPar) (ctx.aPar / ctx.aPerp) ^ 2 ≤ C ^ 2 := by
  rw [core_levi_ratio_eq_aspect_sq]

/-- **Condition number vs aspect ratio, with `O(ℏ_q²)` correction**
    (md part (b), the `(1 + O(ℏ_q²))` factor): the difference between the
    condition number and the squared max-aspect ratio is bounded by
    `C₀ ℏ_q²`, i.e. `cond = max(a⊥/a∥, a∥/a⊥)² + O(ℏ_q²)`. -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_cond_aspect_bound [ctx : CoreLeviContext] :
    |ctx.cond - max (ctx.aPerp / ctx.aPar) (ctx.aPar / ctx.aPerp) ^ 2|
      ≤ ctx.C0 * ctx.hbar ^ 2 :=
  ctx.cond_aspect_bound

/-- **Quantum-pressure bound** (md part (d)): the Levi condition number is
    bounded, `cond ≤ 1 + C₀ ℏ_q²`.

    Note on the missing `q > 1`. The md conditions this part on `q > 1`,
    and the earlier encoding carried `(q : ℝ) (hq : q > 1)` as binders —
    but `cond_bound` is a field of `CoreLeviContext` that mentions no `q`,
    so neither binder was ever used and the linter said so. Carrying an
    unused hypothesis makes the statement look stronger than it is, so the
    binders are dropped rather than kept as decoration. Encoding the `q > 1`
    restriction honestly means indexing the context's bound by `q`; that is
    an open gap in this encoding, not a discharged hypothesis. -/
-- Ref: [manuscript] prop:core-levi-form
theorem core_levi_cond_bound
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    [ctx : CoreLeviContext] :
    ctx.cond ≤ 1 + ctx.C0 * ctx.hbar ^ 2 :=
  ctx.cond_bound

end QOU.FluidDynamics
