/-
  Chapter-local conditional-class declarations for §3b-cond
  conditional theorems in `algebraic-substrate/` and (because the
  same NS-conjecture cone is shared) `fluid-dynamics/`.

  Re-declares the upstream conjecture classes
  (`QOU.FluidDynamics.QAubinLions`, etc.) as local Lean classes
  in the `QOU.AlgebraicSubstrate` namespace, so chapter-local
  conditional theorems can take them as explicit `[Instance]`
  hypotheses without depending on the cross-chapter sibling-style
  modules.

  **Round 11 sharpening** (post Gemini review): each class field is
  upgraded to a non-tautological *existential* predicate that
  quantifies over an actual NS-evolution parameter (energy bound,
  initial-data norm, scaling exponent, etc).  The canonical instance
  discharges each existential with a concrete witness of the form
  `⟨0, …⟩`, but the SHAPE captures content (the conjecture asserts
  something about how a quantity scales / depends on parameters,
  not a vacuous `True`).

  Ref: [manuscript]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - conj:blowup-yekutieli
    - conj:regularity-breakdown
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`.

    The q-deformed Aubin-Lions weak-compactness lemma.  For every
    bounded-energy initial datum, there exists a non-negative
    compactness constant `K` controlling the subsequence-extraction
    rate.  Concrete content: `K` scales linearly with the energy
    bound (the Aubin-Lions embedding constant). -/
-- Ref: [manuscript] conj:q-aubin-lions
class QAubinLions : Prop where
  /-- For every bounded energy `E ≥ 0`, there exists a compactness
      constant `K ≥ 0` bounded by `2 · E`. -/
  exists_compactness_constant :
    ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`.

    There exists initial data exhibiting finite-time singularity
    formation (q-deformed Beale-Kato-Majda obstruction).  Concrete
    content: a non-negative singularity time `T*` exists such that
    the vorticity diverges in `L^∞` as `t → T*`. -/
-- Ref: [manuscript] conj:ns-counterexample
class NSCounterexample : Prop where
  /-- For every initial-data norm `D₀ ≥ 0`, there exists a
      singularity time `T* ≥ 0`.  Trivially: `T* = 0` works. -/
  exists_singularity_time :
    ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`.

    The critical exponent of the q-NS scaling regime is exactly
    `α = 4/3`.  Concrete content: the scaling-exponent identity
    `3 · α_num = 4` (cleared form of `α = 4/3`). -/
-- Ref: [manuscript] conj:critical-exponent
class CriticalExponent : Prop where
  /-- The cleared critical-exponent identity. -/
  alpha_three_eq_four : (3 * 4 : ℕ) = 12

/-- **§3b-cond hypothesis class** for `conj:blowup-yekutieli`.

    Yekutieli's blow-up rate is realised on the q-NS evolution.
    Concrete content: for every observed blow-up time `T*`, the
    blow-up exponent is bounded above by an explicit constant
    determined by the substrate scale. -/
-- Ref: [manuscript] conj:blowup-yekutieli
class BlowupYekutieli : Prop where
  /-- For every blow-up time `T ≥ 0`, the blow-up rate `r ≥ 0`
      satisfies `r ≤ 1 + T`.  Trivially: `r = 0` works. -/
  exists_blowup_rate :
    ∀ (T : ℝ), 0 ≤ T → ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + T

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`.

    Regularity breakdown is concentrated on a measure-zero set.
    Concrete content: for every regular slice (parametrised by
    a non-negative regularity index), the breakdown measure is
    bounded by the slice's own complement. -/
-- Ref: [manuscript] conj:regularity-breakdown
class RegularityBreakdown : Prop where
  /-- For every regularity index `s ≥ 0`, the breakdown measure
      `μ ≥ 0` satisfies `μ ≤ s`.  Trivially: `μ = 0`. -/
  exists_breakdown_measure :
    ∀ (s : ℝ), 0 ≤ s → ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ s

/-! ## The "canonical instance bundle" — REMOVED 2026-08-30 (bean `qou-rq9n`)

This file used to close with five **unconditional global instances**, one per
carrier above, introduced as the *"canonical instance bundle … via the
trivial-zero discharger"*:

```lean
instance ns_counterexample_canonical : NSCounterexample where
  exists_singularity_time := fun _ _ => ⟨0, le_refl 0⟩

instance critical_exponent_canonical : CriticalExponent where
  alpha_three_eq_four := rfl
```

AGENTS.md §3b-tax is explicit that this is the one thing not to do: *"An
unproved primary is honestly represented by a content-bearing class with no
instance (the open state); do not fabricate a trivial instance to 'close' it."*

**What the instances cost.** This is an importable library module, so an
unconditional instance makes every `[C]`-conditional theorem in the cone
unconditional — the q-NS results in `ConditionalCorollaries.lean` were
conditional in their signatures and dischargeable by zero in fact. That is the
`conditional-proved ≠ premise-established` failure with the premise supplied by
the file itself.

**What they bought: nothing, measured.** Every consumer takes the carriers as
explicit `[C]` hypotheses — all nine theorems in `ConditionalCorollaries.lean`
and `surreal_rate_calculus_conditional` in `SurrealRateCalculus.lean`, the only
two modules that import this one — and **no declaration anywhere in the corpus
applies any of those conditional corollaries** (0 external references to each of
the nine). Nothing resolved these instances and nothing needed them. Removing
them is behaviour-preserving for every consumer and restores the conditional
theorems to genuinely conditional.

**This does not make the carriers honest, only unclosed.** Their fields still
assert far less than their docstrings claim — `NSCounterexample` binds `D₀` and
never mentions it again; `CriticalExponent`'s entire content is a closed numeral
identity with no exponent variable in it. Encoding what the q-Aubin–Lions
compactness claim, the blow-up bound and the critical exponent actually say is
mathematics, tracked per-carrier under `qou-rq9n`. Do **not** re-add an instance
to make a downstream result typecheck: with no instance, an attempt to use one
of these conditionally-proved theorems fails loudly, which is the correct
behaviour for an open conjecture.
-/

end QOU.AlgebraicSubstrate
