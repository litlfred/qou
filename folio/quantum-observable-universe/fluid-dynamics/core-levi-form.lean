/-
  Core Levi form on geodesic vortices (conditional on the q-NS cone).

  Ref: [leitner2026] §Fluid dynamics / Core Levi form,
       prop:core-levi-form

  ## What the load-bearing claim is

  The md asserts (a) the core aspect ratio `a⊥/a∥ = √(λ∥/λ⊥)·(1 + O(ℏ_q²))`,
  (b) the Levi condition number `cond = max(λ∥,λ⊥)/min(λ∥,λ⊥) =
  max(a⊥/a∥, a∥/a⊥)²·(1 + O(ℏ_q²))`, (c) the equivalence of the
  bounded-aspect-ratio and bounded-condition-number conditions, and (d) for
  `q > 1` the bound `cond ≤ 1 + C₀ℏ_q²`.

  ## 2026-08-31 — the data are PARAMETERS now, and one field was redundant

  This file used to state all of the above over a `CoreLeviContext` class
  that carried `lamPar`, `lamPerp`, `aPar`, `aPerp`, `cond`, `hbar`, `C0`
  **and** the md's conclusions (b) and (d) as its own fields.  Because the
  data were fields rather than parameters, the instance chose them:
  `lamPar = lamPerp = aPar = aPerp = cond = 1`, `hbar = C0 = 0` satisfies
  every field, so a `[CoreLeviContext]` binder assumed nothing.  Two
  declarations — `core_levi_cond_aspect_bound` and `core_levi_cond_bound` —
  returned a field directly (AGENTS.md §3b-cond item 5; bean `qou-z9ws`).

  Re-encoded with `CoreLeviData` carrying **only data** and every claim a
  named proposition over it: `NonDegenerate`, `CondIsEigenvalueRatio` (the
  md's definition of `cond`), `AspectSqIsEigenvalueRatio` (md (a) at leading
  order) and `QuantumPressureBound` (md (d)).

  **One of the two projections turned out to be redundant, and that is a
  finding.**  `cond_aspect_bound` was described in the previous docstring as
  *"carrying the `O(ℏ_q²)` correction as an explicit `|·| ≤ C₀ℏ_q²` bound"*.
  It carried nothing: the class already asserted `cond = max λ/min λ` and
  `(a⊥/a∥)² = λ∥/λ⊥` **exactly**, and those two force
  `cond = max(a⊥/a∥, a∥/a⊥)²` on the nose.  So the "bound" was `0 ≤ C₀ℏ_q²`
  wearing an absolute value.  It is now `core_levi_cond_aspect_bound`,
  **derived** — and the honest statement of md (b) is the exact identity in
  `core_levi_form`, not a bound.

  **What is therefore NOT encoded.**  The `(1 + O(ℏ_q²))` factors of md (a)
  and (b) are absent: the hypotheses state the leading-order idealisation as
  an exact equality.  Encoding the correction means indexing the aspect
  relation by `ℏ_q`, which is not done here.  Likewise md (c) is encoded only
  as the (1)⟺(2) equivalence — clauses (3), (4), (5) (contact
  non-degeneracy, the observability axiom, Frobenius failure) have no Lean
  here — and md (e), the `q = 1` degeneration, has none either.

  ## The five q-NS carrier copies were DELETED 2026-08-30

  This file used to re-declare `QAubinLions`, `NSCounterexample`,
  `CriticalExponent`, `BlowupYekutieli` and `RegularityBreakdown` verbatim, in
  this namespace, with the vacuous fields they had upstream — `∃ K, 0 ≤ K ∧
  K ≤ 2E` (`K = 0`), `∀ D₀ ≥ 0, ∃ T, 0 ≤ T` (`D₀` bound and unused),
  `(3 * 4 : ℕ) = 12` (no exponent variable at all), and so on — and bound all
  five on `core_levi_form` and `core_levi_cond_bound`.

  Two defects at once. The copies were a **second, undocumented set** of the
  same carriers, so the upstream repair (`qou-rq9n` / `qou-93hu`, and the
  per-carrier encoding on `main`) did not reach them; and the binders were
  **decorative**, since both proofs use only the context data and elaborate
  unchanged without them.

  The conditional dependency of `prop:core-levi-form` on the q-NS cone is a
  manuscript-level claim and lives in the `.md`, which states it.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.FluidDynamics

/-- Levi-form geometry of the vortex core on the normal plane `N_pϱ`:
    the Levi eigenvalues `λ∥, λ⊥`, the core radii `a∥, a⊥`, the Levi
    condition number `cond`, the quantum length `ℏ_q` and the bound constant
    `C₀`.

    **Data only.**  Every claim the md makes about these quantities is a
    named proposition below, taken as a hypothesis where it is used.  Nothing
    here is a claim, so an inhabitant of this structure asserts nothing. -/
structure CoreLeviData where
  /-- Levi eigenvalue toward an adjacent filament. -/
  lamPar : ℝ
  /-- Levi eigenvalue perpendicular to it. -/
  lamPerp : ℝ
  /-- Core radius in the `∥` direction. -/
  aPar : ℝ
  /-- Core radius in the `⊥` direction. -/
  aPerp : ℝ
  /-- The Levi condition number on `N_p`. -/
  cond : ℝ
  /-- Quantum length scale `ℏ_q`. -/
  hbar : ℝ
  /-- Bound constant `C₀`. -/
  C0 : ℝ

namespace CoreLeviData

/-- **Non-degeneracy on the collision locus** (md (c) clause 3, in the form
the other parts need): both Levi eigenvalues and both core radii are strictly
positive, and the bound constant is non-negative. -/
def NonDegenerate (d : CoreLeviData) : Prop :=
  0 < d.lamPar ∧ 0 < d.lamPerp ∧ 0 < d.aPar ∧ 0 < d.aPerp ∧ 0 ≤ d.C0

/-- **The md's definition of the condition number** (md (b), definitional
half): `cond = max(λ∥,λ⊥)/min(λ∥,λ⊥)`.  Symmetric in the two eigenvalues, so
it is correct whichever is the larger. -/
def CondIsEigenvalueRatio (d : CoreLeviData) : Prop :=
  d.cond = max d.lamPar d.lamPerp / min d.lamPar d.lamPerp

/-- **The aspect-ratio relation at leading order** (md (a)):
`(a⊥/a∥)² = λ∥/λ⊥`, i.e. `a⊥/a∥ = √(λ∥/λ⊥)`.  The md's `(1 + O(ℏ_q²))`
factor is **not** encoded — see the module docstring. -/
def AspectSqIsEigenvalueRatio (d : CoreLeviData) : Prop :=
  (d.aPerp / d.aPar) ^ 2 = d.lamPar / d.lamPerp

/-- **Quantum-pressure bound** (md (d), for `q > 1`): `cond ≤ 1 + C₀ℏ_q²`.

Named, not asserted.  This is the one part of the proposition that does not
follow from the setup: the eigenvalue ratio is bounded *below* by 1 for free,
and bounding it above is the physical claim that continuous quantum pressure
enforces near-isotropy of the core.  It is a hypothesis wherever it is used.

The md conditions this part on `q > 1`.  That restriction is not encoded:
`CoreLeviData` carries no `q`, and an unused `q`-binder would make the
statement look stronger than it is.  Encoding it honestly means indexing the
bound by `q`; that is an open gap here, not a discharged hypothesis. -/
def QuantumPressureBound (d : CoreLeviData) : Prop :=
  d.cond ≤ 1 + d.C0 * d.hbar ^ 2

end CoreLeviData

/-- **Leading-order structural identity** (md (b), the eigenvalue-to-aspect
bridge): `max(λ∥,λ⊥)/min(λ∥,λ⊥) = max(a⊥/a∥, a∥/a⊥)²`.

Derived from the aspect relation and positivity by case split on the
eigenvalue ordering. -/
-- Ref: [leitner2026] prop:core-levi-form
theorem core_levi_ratio_eq_aspect_sq (d : CoreLeviData)
    (hnd : d.NonDegenerate) (hasp : d.AspectSqIsEigenvalueRatio) :
    max d.lamPar d.lamPerp / min d.lamPar d.lamPerp
      = max (d.aPerp / d.aPar) (d.aPar / d.aPerp) ^ 2 := by
  obtain ⟨hPar, hPerp, haPar, haPerp, _⟩ := hnd
  have hr1 : (0:ℝ) ≤ d.aPerp / d.aPar := div_nonneg haPerp.le haPar.le
  have hr2 : (0:ℝ) ≤ d.aPar / d.aPerp := div_nonneg haPar.le haPerp.le
  -- `(a⊥/a∥)² = λ∥/λ⊥` and `(a∥/a⊥)² = λ⊥/λ∥`.
  have h1 : (d.aPerp / d.aPar) ^ 2 = d.lamPar / d.lamPerp := hasp
  have h2 : (d.aPar / d.aPerp) ^ 2 = d.lamPerp / d.lamPar := by
    rw [← inv_div d.aPerp d.aPar, inv_pow, h1, inv_div]
  rcases le_total d.lamPar d.lamPerp with h | h
  · -- λ∥ ≤ λ⊥ : max/min ratio is λ⊥/λ∥, and a∥/a⊥ is the larger aspect.
    rw [max_eq_right h, min_eq_left h]
    have hsq : (d.aPerp / d.aPar) ^ 2 ≤ (d.aPar / d.aPerp) ^ 2 := by
      rw [h1, h2]
      exact le_trans ((div_le_one hPerp).mpr h) ((one_le_div hPar).mpr h)
    have hge : d.aPerp / d.aPar ≤ d.aPar / d.aPerp :=
      (pow_le_pow_iff_left₀ hr1 hr2 two_ne_zero).mp hsq
    rw [max_eq_right hge, h2]
  · -- λ⊥ ≤ λ∥ : max/min ratio is λ∥/λ⊥, and a⊥/a∥ is the larger aspect.
    rw [max_eq_left h, min_eq_right h]
    have hsq : (d.aPar / d.aPerp) ^ 2 ≤ (d.aPerp / d.aPar) ^ 2 := by
      rw [h1, h2]
      exact le_trans ((div_le_one hPar).mpr h) ((one_le_div hPerp).mpr h)
    have hge : d.aPar / d.aPerp ≤ d.aPerp / d.aPar :=
      (pow_le_pow_iff_left₀ hr2 hr1 two_ne_zero).mp hsq
    rw [max_eq_left hge, h1]

/-- **Core Levi form** ([`prop:core-levi-form`]).

On the normal plane of a geodesic vortex core, given the md's definition of
`cond` and its leading-order aspect relation:

* `1 ≤ cond` — the condition number is a genuine condition number, from
  `min(λ∥,λ⊥) ≤ max(λ∥,λ⊥)` and eigenvalue positivity; and
* `cond = max(a⊥/a∥, a∥/a⊥)²` — md part (b), **exactly** at leading order.

Both conjuncts are derived; neither is a hypothesis restated.  The md writes
part (b) with a `(1 + O(ℏ_q²))` factor, which the hypotheses here do not
carry — see the module docstring. -/
-- Ref: [leitner2026] prop:core-levi-form
theorem core_levi_form (d : CoreLeviData)
    (hnd : d.NonDegenerate) (hcond : d.CondIsEigenvalueRatio)
    (hasp : d.AspectSqIsEigenvalueRatio) :
    1 ≤ d.cond ∧
      d.cond = max (d.aPerp / d.aPar) (d.aPar / d.aPerp) ^ 2 := by
  obtain ⟨hPar, hPerp, haPar, haPerp, hC0⟩ := id hnd
  have hc : d.cond = max d.lamPar d.lamPerp / min d.lamPar d.lamPerp := hcond
  refine ⟨?_, ?_⟩
  · have hmin : 0 < min d.lamPar d.lamPerp := lt_min hPar hPerp
    rw [hc]
    exact (one_le_div hmin).mpr min_le_max
  · rw [hc, core_levi_ratio_eq_aspect_sq d hnd hasp]

/-- **Condition number vs aspect ratio, with the `O(ℏ_q²)` slot** (md (b)).

`|cond − max(a⊥/a∥, a∥/a⊥)²| ≤ C₀ℏ_q²`.

This was a **field** of the old context class, described there as carrying
the `O(ℏ_q²)` correction.  It carries none: the two hypotheses already pin
`cond` to the squared aspect ratio exactly, so the left-hand side is `0` and
the statement is `0 ≤ C₀ℏ_q²`.  Kept as a derived corollary because the md
writes part (b) in this form, and recorded as redundant so no later reader
mistakes it for content. -/
-- Ref: [leitner2026] prop:core-levi-form
theorem core_levi_cond_aspect_bound (d : CoreLeviData)
    (hnd : d.NonDegenerate) (hcond : d.CondIsEigenvalueRatio)
    (hasp : d.AspectSqIsEigenvalueRatio) :
    |d.cond - max (d.aPerp / d.aPar) (d.aPar / d.aPerp) ^ 2|
      ≤ d.C0 * d.hbar ^ 2 := by
  obtain ⟨_, _, _, _, hC0⟩ := id hnd
  rw [(core_levi_form d hnd hcond hasp).2, sub_self, abs_zero]
  exact mul_nonneg hC0 (sq_nonneg _)

/-- **Aspect-ratio / condition-number equivalence** (md (c), (1)⟺(2)):
the condition number is bounded by `C²` iff the squared max-aspect ratio is.

md (c) also lists clauses (3) contact non-degeneracy, (4) the observability
axiom `Hom_𝐂(𝟙, Ad(A)) = 0`, and (5) clean failure of Frobenius
integrability, as strictly equivalent.  None of those three is encoded. -/
-- Ref: [leitner2026] prop:core-levi-form
theorem core_levi_aspect_equiv (d : CoreLeviData)
    (hnd : d.NonDegenerate) (hasp : d.AspectSqIsEigenvalueRatio) (C : ℝ) :
    max d.lamPar d.lamPerp / min d.lamPar d.lamPerp ≤ C ^ 2
      ↔ max (d.aPerp / d.aPar) (d.aPar / d.aPerp) ^ 2 ≤ C ^ 2 := by
  rw [core_levi_ratio_eq_aspect_sq d hnd hasp]

/-- **Quantum pressure bounds the core aspect ratio** (md (d) ⟹ md (c)(1)).

If the quantum-pressure bound holds, the squared max-aspect ratio is bounded
by `1 + C₀ℏ_q²`.

This replaces the old `core_levi_cond_bound`, which was `:= ctx.cond_bound` —
the bound handed straight back from the class that assumed it.  Here md (d)
is an explicit hypothesis on caller-supplied data and the conclusion is a
different statement derived from it through `core_levi_form`. -/
-- Ref: [leitner2026] prop:core-levi-form
theorem core_levi_aspect_bounded_of_quantum_pressure (d : CoreLeviData)
    (hnd : d.NonDegenerate) (hcond : d.CondIsEigenvalueRatio)
    (hasp : d.AspectSqIsEigenvalueRatio) (hqp : d.QuantumPressureBound) :
    max (d.aPerp / d.aPar) (d.aPar / d.aPerp) ^ 2 ≤ 1 + d.C0 * d.hbar ^ 2 := by
  have hb : d.cond ≤ 1 + d.C0 * d.hbar ^ 2 := hqp
  rw [← (core_levi_form d hnd hcond hasp).2]
  exact hb

end QOU.FluidDynamics
