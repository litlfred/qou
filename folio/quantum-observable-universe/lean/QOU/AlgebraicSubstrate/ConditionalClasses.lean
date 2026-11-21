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

  **🛑 Round 11's claim was WRONG, and this file was the corpus's exemplar for
  it. Read this before the paragraph it corrects (2026-08-30).**

  Round 11 (post Gemini review) upgraded each class field to a non-tautological
  *existential* predicate quantifying over an NS-evolution parameter, and
  argued — in this header, as settled fact — that *"the canonical instance
  discharges each existential with a concrete witness of the form `⟨0, …⟩`, but
  the SHAPE captures content (the conjecture asserts something about how a
  quantity scales / depends on parameters, not a vacuous `True`)."*

  **It does not.** The retraction is below, and the original wording is quoted
  above rather than restated as the file's own voice, because a reader skimming
  a header takes away whatever it asserts first — and the assertion here was the
  reverted one. (Flagged in review on PR #6122; the corpus documents this exact
  failure mode elsewhere as *"that heading is the line a skimming agent
  reads"*.)

  **The retraction.** AGENTS.md §3b-tax cited these classes as the model of a
  carrier stating "a parameter-quantified inequality in the *shape* of the
  claim". The shape was right and the content was absent: every field was an
  **existential** satisfied by choosing zero, so the conjectures were
  discharged by the bundle at the foot of this file and no shipped criterion
  fired — the audit raised 0 lines here, and the five carriers had 0 entries in
  the vacuity review ledger.

  Shape is not content, and the difference is **refutability**: an `∃` over a
  quantity you get to pick cannot be false, while a `∀` about a quantity the
  *caller* supplies can. Each re-encoded carrier below now takes that quantity
  as a class **parameter** (`Prop` classes cannot carry data) and constrains
  it, so there is a value at which the class is false — recorded per carrier.

  Status of the five, all under bean `qou-rq9n`:

  | carrier | state | refuted by |
  |---|---|---|
  | `QAubinLions` | re-encoded `qou-3ytx` | a non-linear `K` |
  | `NSCounterexample` | re-encoded `qou-5nj1` | a bounded vorticity |
  | `CriticalExponent` | re-encoded `qou-93hu`, then **de-boxed** `qou-4670` | a non-positive `α`, or a bounded enstrophy |
  | `RegularityBreakdown` | re-encoded `qou-m7a2` | a positive-measure set |
  | `BlowupYekutieli` | **replaced** `qou-88nf` — a rate existential became the upstream obstruction statement | every obstruction vanishing while `smooth` is `False` |

  The trivial-zero instance bundle that discharged all five is removed; see the
  note at the foot of this file.

  Ref: [leitner2026]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - prop:blowup-yekutieli   (NOT `conj:` — no such label is declared by any
                               content block; the live one is a proposition in
                               `lifting-and-descent/`. Bean `qou-88nf`.)
    - conj:regularity-breakdown
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
-- `RegularityBreakdown` states its claim against the real Lebesgue measure
-- rather than a numeric proxy for it (bean `qou-m7a2`).
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`.

    The q-deformed Aubin-Lions weak-compactness lemma.  `K` is the
    compactness constant as a function of the energy bound, and the claim is
    the one this class's docstring has always made: **`K` scales linearly with
    the energy bound** (the Aubin-Lions embedding constant).

    **What this encodes.** `∃ C > 0, ∀ E ≥ 0, K E = C · E` — linear, with a
    strictly positive constant. The strictness is what carries the content:
    without `0 < C` the zero function satisfies it and the class is back where
    it started.

    **What this does NOT encode**, so the fix is not over-read: nothing here
    ties `K` to a subsequence extraction, to the q-deformation, or to any
    function space. Those need the analytic setup, which is open. This is the
    docstring's *scaling* claim, stated about a supplied `K`.

    **History.** Until 2026-08-30 the field read
    `∀ E ≥ 0, ∃ K, 0 ≤ K ∧ K ≤ 2·E` — an existential per `E`, satisfied by
    `K = 0` for every `E`, so "scales linearly" appeared in the prose and
    nowhere in the Lean. `Prop` classes cannot carry data, hence `K` is a
    parameter. Bean `qou-3ytx`. -/
-- Ref: [leitner2026] conj:q-aubin-lions
class QAubinLions (K : ℝ → ℝ) : Prop where
  /-- The compactness constant is linear in the energy bound, with a strictly
      positive embedding constant. -/
  linear_in_energy : ∃ C : ℝ, 0 < C ∧ ∀ E : ℝ, 0 ≤ E → K E = C * E

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`.

    Finite-time singularity formation (q-deformed Beale-Kato-Majda
    obstruction).  `vorticitySup t` is the `L^∞` norm of the vorticity at time
    `t`, and the claim is the one this class's docstring has always made: **a
    non-negative singularity time `T*` exists at which the vorticity
    diverges**.

    **What this encodes.** `∃ T ≥ 0, ∀ M, ∀ t₀ < T, ∃ t ∈ (t₀, T), M <
    vorticitySup t` — the vorticity exceeds every bound at times **arbitrarily
    close to `T` from below**, which is the Beale-Kato-Majda shape. A bounded
    `vorticitySup` refutes it, which is exactly what the previous field could
    not do.

    **The `t₀` quantifier is load-bearing and was missing in the first
    encoding** (caught in review on PR #6122). Without it the field reads
    `∀ M, ∃ t < T, M < vorticitySup t`, which says only that the vorticity is
    unbounded somewhere on `(-∞, T)` — satisfied by a function that blows up
    early and is placid near `T`, i.e. by no blow-up *at* `T` at all. That is
    the "documented as a limit, stated without one" defect: the docstring said
    "as `t → T*`" and the statement had no device localising anything near
    `T`. Quantifying over `t₀ < T` is what turns "unbounded before `T`" into
    "unbounded approaching `T`".

    **What this does NOT encode.** That `vorticitySup` solves anything. There
    is no q-NS evolution here, no initial datum, no relation between `T` and
    the data — the previous field bound `D₀` and never mentioned it again, and
    this one does not bind it at all rather than pretend to use it. Supplying
    the evolution is the open work.

    **History.** Until 2026-08-30 the field read `∀ D₀ ≥ 0, ∃ T, 0 ≤ T` —
    literally "there exists a non-negative real", with the initial-datum norm
    bound and discarded, and its own sub-docstring conceded "Trivially: `T* = 0`
    works." Bean `qou-5nj1`. -/
-- Ref: [leitner2026] conj:ns-counterexample
class NSCounterexample (vorticitySup : ℝ → ℝ) : Prop where
  /-- The vorticity exceeds every bound `M` at times arbitrarily close to `T`
      from below: for every `t₀ < T` there is a `t` in `(t₀, T)` with
      `M < vorticitySup t`. -/
  blowup_at_finite_time :
    ∃ T : ℝ, 0 ≤ T ∧ ∀ M : ℝ, ∀ t₀ : ℝ, t₀ < T →
      ∃ t : ℝ, t₀ < t ∧ t < T ∧ M < vorticitySup t

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`.

    Enstrophy diverges as `q → 1⁺` with a positive exponent `α`. Both the
    enstrophy function and the exponent are class **parameters** (`Prop`
    classes cannot carry data); the fields are transcribed from the upstream
    carrier `QOU.FluidDynamics.CriticalExponent` in
    [`fluid-dynamics/p2-critical-exponent.lean`].

    **🛑 `α = 4/3` was REMOVED on 2026-08-30 and must not be put back.** It
    was here for one day, and it is the more interesting of this carrier's two
    defects.

    From 2026-08-30 the single field read `alpha_eq : α = 4/3`, which I wrote
    while draining the vacuity of the numeral identity below. That fixed the
    shape and introduced a worse problem: `4/3` is **not a result the corpus
    holds**. [`p2-critical-exponent.md`] gives it as one of *two* heuristic
    values under *two* named turbulence closures — `α = 1` under the
    dissipation closure `ε = ν_q·Ω`, `α = 4/3` under the Kolmogorov cascade —
    and says in terms: *"Neither closure is rigorous; the true `α` is fixed by
    the actual q-Navier–Stokes enstrophy spectrum (the turbulence-closure
    problem) and is open. The two values bracket it under their respective
    hypotheses."* Even under its own closure it carries a logarithmic
    correction, so it is not a clean power law.

    So the field asserted as settled a value its own source calls open, and
    picked the larger of the two bracketing candidates. The corpus had already
    decided against exactly this: bean `qou-15gb` (completed 2026-07-18)
    reconciled the inconsistency by making the exponent **closure-dependent,
    not a single boxed value**, and the established way to carry a value here
    is to name its closure — `QOU.FluidDynamics.enstrophy_alpha_one_of_dissipation_closure`
    in [`q_ns_classical_bridge.lean`] is the pattern. A closure-free `α = 4/3`
    in a hypothesis class re-boxed the value one namespace over.

    **What this encodes now.** `0 < α` and the divergence statement — which is
    what the `.md` asserts without hedging (*"diverges as `Ω_max(q) ~
    (q-1)^{-α}` for some `α > 0`"*), and what the upstream carrier encodes.
    The one-sided neighbourhood `1 < q ∧ q - 1 < ε` is load-bearing and is
    upstream's, not mine: without it the field says only that enstrophy is
    unbounded *somewhere*, which `enstrophy q = max q 0` satisfies while being
    the identity near `q = 1` — regular exactly where the conjecture asserts
    blow-up (bean `qou-k3hh`, witness in
    `docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean`).

    **What this still does NOT encode.** That `α` is the *rate* of the
    divergence. The asymptotic `Ω_max(q) ~ (q-1)^{-α}` relating the two
    parameters is absent here exactly as it is absent upstream, which says so
    itself: *"the divergence rate is not encoded, and `criticalExponent` is
    accordingly unconstrained by any field of this class."* Encoding it needs
    the asymptotic, and pinning `α` needs a closure that is not rigorous. That
    gap is the honest open state; it is not closed by choosing a number.

    **History.** Until 2026-08-30 the single field read
    `alpha_three_eq_four : (3 * 4 : ℕ) = 12` — a closed numeral identity with
    the values already substituted in, containing **no exponent variable at
    all**. `rfl` proved it whatever the physics, so the class constrained
    nothing and every `[CriticalExponent]`-conditional theorem was vacuous in
    its critical-exponent leg. Beans `qou-93hu` (the vacuity) and `qou-4670`
    (the boxed value). -/
-- Ref: [leitner2026] conj:critical-exponent
class CriticalExponent (enstrophy : ℝ → ℝ) (α : ℝ) : Prop where
  /-- The exponent is positive: a genuine divergence, not a bounded
      oscillation. Mirrors upstream `criticalExponent_pos`. -/
  alpha_pos : 0 < α
  /-- **The conjecture itself.** Enstrophy is unbounded on *every*
      right-neighbourhood of `q = 1`. Transcribed from upstream
      `QOU.FluidDynamics.CriticalExponent.enstrophy_diverges`. -/
  enstrophy_diverges :
    ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
      ∃ q : ℝ, 1 < q ∧ q - 1 < ε ∧ M < enstrophy q

/-- **§3b-cond hypothesis class** for [`prop:blowup-yekutieli`].

    Smoothness as lifting through the brane tower: `v` is smooth exactly when
    every obstruction class `κ_n(v)` vanishes. `obstruction n` is `κ_n(v)` at
    tower level `n`, valued in a coefficient group modelled by `ℕ` with its
    distinguished zero; `smooth` is the proposition "`v` lifts through the whole
    tower".

    Transcribed from the upstream carrier `QOU.FluidDynamics.BlowupYekutieli` in
    [`lifting-and-descent/p3-blowup-yekutieli.lean`], which states exactly this
    field and derives the blow-up direction from it by contraposition. Both
    parameters are class parameters because `Prop` classes cannot carry data.

    **🛑 THIS IS NOT THE CLASS THAT USED TO BE HERE, and the difference is not a
    strengthening (2026-08-30, beans `qou-88nf` / `qou-4670`).** Until today the
    field read `∀ T ≥ 0, ∃ r, 0 ≤ r ∧ r ≤ 1 + T` — an existential satisfied by
    `r = 0`, i.e. by *no blow-up*, the negation of the claim the carrier is
    named for. That field was about a **blow-up rate**. This one is about
    **obstruction-class vanishing**. They are two different propositions that
    happened to share a name, so this is a replacement, not a re-encoding of the
    same content, and a `[BlowupYekutieli …]` binder written before today did
    not mean what one written after it means.

    **Why it took a second look.** The carrier was left vacuous on the stated
    grounds that its docstring named "an explicit constant determined by the
    substrate scale" without saying which, so any bound would have been chosen
    by an agent rather than transcribed — and an audit concluded the rate is
    nowhere in the corpus and "its conjecture block does not exist". The first
    half stands: **there is still no Yekutieli blow-up rate in the corpus**, and
    none may be invented. The second half was wrong. There is no
    `conj:blowup-yekutieli`, which is what that grep tested, but the block is
    live at `lifting-and-descent/` under the label **`prop:`**, with ten blocks
    interpreting or using it. It had moved chapters, not been deleted.

    So the transcription needs no rate at all: the upstream statement is about
    obstructions, and it is the thing this class should always have carried.

    **Refutable**, which the old field was not: `BlowupYekutieli (fun _ => 0)
    False` is false, because every obstruction vanishes while `smooth` is
    `False`. Satisfiable both ways — trivially by `(fun _ => 0, True)`, and with
    a genuine blow-up by an `obstruction` that is nonzero somewhere against
    `smooth = False`. Witnesses in
    `docs/audits/2026-08-30-qns-carriers-are-refutable.lean`. -/
-- Ref: [leitner2026] prop:blowup-yekutieli
-- Ref: [yekutieli2010] https://doi.org/10.1007/s00029-010-0029-8
class BlowupYekutieli (obstruction : ℕ → ℕ) (smooth : Prop) : Prop where
  /-- **Smoothness-as-lifting.** `v` is smooth iff every brane-tower
      obstruction class vanishes. The blow-up characterisation — some finite
      level has `κ_{n*}(v) ≠ 0` — is *derived* from this by contraposition,
      not assumed. -/
  smooth_iff_all_obstructions_vanish : smooth ↔ ∀ n : ℕ, obstruction n = 0

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`.

    `breakdownSet` is the set of times at which regularity fails, and the claim
    is the one this class's docstring has always made: **breakdown is
    concentrated on a measure-zero set**.

    **What this encodes.** `volume breakdownSet = 0`, against Mathlib's
    Lebesgue measure — the actual statement, not a numeric proxy for it. It is
    false for any breakdown set of positive measure (an interval `Ioo a b` with
    `a < b` refutes it), which is what the previous field could not be.

    **What this does NOT encode.** That `breakdownSet` is the breakdown locus
    of anything. There is no q-NS solution here and no definition of
    regularity; supplying those is the open work.

    **History.** Until 2026-08-30 the field read
    `∀ s ≥ 0, ∃ μ, 0 ≤ μ ∧ μ ≤ s` — satisfied by `μ = 0` for every `s`, and
    its own sub-docstring conceded "Trivially: `μ = 0`". Note the discharger
    also reused the hypothesis directly (`⟨0, le_refl 0, hs⟩`): the proof term
    *was* the hypothesis. Bean `qou-m7a2`. -/
-- Ref: [leitner2026] conj:regularity-breakdown
class RegularityBreakdown (breakdownSet : Set ℝ) : Prop where
  /-- The breakdown locus is Lebesgue-null. -/
  breakdown_measure_zero : MeasureTheory.volume breakdownSet = 0

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

**Removing the bundle did not by itself make the carriers honest, only
unclosed.** At that moment their fields asserted far less than their docstrings
claimed — `NSCounterexample` bound `D₀` and never mentioned it again;
`CriticalExponent`'s entire content was a closed numeral identity with no
exponent variable in it. **That sentence is history as of later the same day:**
four of the five have since been re-encoded (see the table at the head of this
file). As of 2026-08-30 none of the five carries its original field:
`BlowupYekutieli` was the last, and it was REPLACED rather than re-encoded --
its rate existential and the upstream obstruction statement are different
propositions sharing a name (`qou-88nf`). Do **not** re-add an instance
to make a downstream result typecheck: with no instance, an attempt to use one
of these conditionally-proved theorems fails loudly, which is the correct
behaviour for an open conjecture.
-/

end QOU.AlgebraicSubstrate
