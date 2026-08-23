import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Data.Fintype.Card
import QOU.Mathlib.RSKBurnsideTarget
import QOU.Mathlib.SchenstedRSKBurnside

/-!
# QOU.Mathlib.RSKBridge — Robinson–Schensted–Knuth bridge to Burnside

The classical Robinson–Schensted–Knuth correspondence gives a
bijection
  RSK : S_n  ≃  Σ_{λ ⊢ n} (SYT(λ) × SYT(λ))
which by counting yields the **Burnside / RSK identity**
  n! = Σ_{λ ⊢ n} (#SYT(λ))².

Mathlib's `Mathlib.Combinatorics.RSK` is partial — the
bijection is formalised in part but the *cardinality consequence*
above has not yet landed.  This file:

1. States `RSKBijection (n : ℕ)` as a class wrapping the
   bijection's existence with the cardinality identity as a
   field.

2. Provides a `BurnsideFromRSK` derivation:
   `[RSKBijection n] → BurnsideIdentity n numStandardYoungTableaux`.

3. Documents the upstream Mathlib path:
   - `Mathlib.Combinatorics.Young.SYT` supplies `SYT(λ)` (the
     finite type of standard Young tableaux of shape `λ`).
   - `Mathlib.Combinatorics.RSK.bijection` (when complete)
     supplies the equiv `S_n ≃ Σ_λ SYT(λ) × SYT(λ)`.
   - Burnside follows from
     `Fintype.card_congr RSK.bijection`,
     `Fintype.card_sigma`, and `Fintype.card_prod`.

The class shape is the §3b-cond pattern from AGENTS.md: the
upstream Mathlib theorem is the only sorry/instance the
downstream chain depends on; once it lands, the whole chain
becomes fully verified.

**File status**: upstreamable scaffolding.  The class fields
are concrete (not `Prop := True`), so the audit-level §3b-cond
hypothesis is content-bearing.

**References**:
- Robinson (1938), Schensted (1961), Knuth (1970) — original
  RSK papers.
- Stanley, *Enumerative Combinatorics* Vol 2, Ch. 7.
- Mathlib partial: `Mathlib.Combinatorics.RSK`.
-/

namespace QOU.Mathlib.RSKBridge

universe u

/-- **`RSKBijection` class** — the conjectural Mathlib upstream:
    the cardinality consequence of the RSK correspondence.

    Field `n_factorial_eq_sum_squares` asserts the Burnside
    identity directly; field `dim` is the supplied SYT-count
    function.  The class instance acts as the §3b-cond hook for
    discharging downstream `BurnsideIdentity` claims. -/
class RSKBijection (n : ℕ) where
  /-- The supplied SYT-count function (concrete instances use
      `Mathlib.Combinatorics.Young.SYT.card`). -/
  dim : Nat.Partition n → ℕ
  /-- The Burnside identity: `n! = Σ_λ (dim λ)²`. -/
  n_factorial_eq_sum_squares :
    ∑ Λ : Nat.Partition n, (dim Λ) ^ 2 = n.factorial

/-- **Bridge theorem**: from the RSK upstream class instance,
    derive the abstract `BurnsideIdentity` predicate. -/
theorem BurnsideFromRSK (n : ℕ) [R : RSKBijection n] :
    ∑ Λ : Nat.Partition n, (R.dim Λ) ^ 2 = n.factorial :=
  R.n_factorial_eq_sum_squares

/-! **Trivial canonical instance** (audit-level §3b-cond hook):
    pinning the supplied dim function to constant `0` AND the
    Burnside-identity field to a vacuous `0 = n.factorial`,
    which only holds when `n.factorial = 0`.  Since `n.factorial`
    is never `0` for `n : ℕ`, this trivial instance is **not
    constructible** at any `n` — exactly the right behaviour
    for the §3b-cond hook (the upstream theorem MUST land for
    the chain to discharge).

    To opt out of the trivial instance: caller supplies a
    custom `RSKBijection n` instance whose `dim` is the
    genuine SYT count and whose `n_factorial_eq_sum_squares`
    field is the upstream Mathlib RSK theorem. -/
-- Intentionally NO trivial instance: the §3b-cond pattern
-- requires the upstream theorem; a constant-zero dim would
-- give `0 = n.factorial` which fails for every `n : ℕ`.

/-- **The substrate identity, PROVED** (S-RSK-bijection).  The RSK bijection's cardinality
    consequence for every `n : ℕ`, stated with the **genuine `#SYT` count**
    (`QOU.Mathlib.RSKBurnsideHolds n := ∑_{p ⊢ n} (dimSYT p)² = n!`), not a hollow existential.

    **This was an `axiom` until 2026-08-23.**  Its own docstring recorded the exit condition —
    *"pending … the in-repo RSK proof under construction in `SchenstedInsertion.lean`, this is
    assumed; once either lands it becomes a derived consequence"*.  That proof landed
    (`QOU.Mathlib.rskBurnsideHolds`, epic `qou-nrex`), so the assumption is discharged and this is
    now a theorem.  Nothing downstream carries `RSK_substrate_axiom` in `#print axioms` any more.

    (Earlier still, it asserted only `∃ dimFn, ∑ dimFn² = n!`, which is satisfiable for trivial
    reasons and did **not** pin `dimFn` to the SYT count — a vacuity flag from the 2026-06-28
    review.  `rsk_substrate_exists` recovers that existential form.) -/
-- Ref: [stanley1999] Enumerative Combinatorics II §7.11 (RSK bijection cardinality Σ_λ (f^λ)² = n!).
theorem RSK_substrate_proved (n : ℕ) : QOU.Mathlib.RSKBurnsideHolds n :=
  QOU.Mathlib.rskBurnsideHolds n

/-- Compatibility spelling of `RSK_substrate_proved` under the name this was declared with while it
    was an axiom.  Retained so no call site has to change; **it is a theorem, not an axiom.**  New
    code should cite `RSK_substrate_proved`. -/
theorem RSK_substrate_axiom (n : ℕ) : QOU.Mathlib.RSKBurnsideHolds n := RSK_substrate_proved n

/-- The old existential form `∃ dimFn, ∑ dimFn² = n!` is now a *derived* consequence of the
    genuine identity (instantiate the witness with the concrete `dimSYT`), not the axiom itself.
    `RSK_substrate_proved n : RSKBurnsideHolds n` is by definition `∑ p, (dimSYT p)² = n!`, so
    `⟨dimSYT, RSK_substrate_proved n⟩` is exactly the existential. -/
theorem rsk_substrate_exists (n : ℕ) :
    ∃ dimFn : Nat.Partition n → ℕ, ∑ Λ : Nat.Partition n, (dimFn Λ) ^ 2 = n.factorial :=
  ⟨QOU.Mathlib.dimSYT, RSK_substrate_proved n⟩

/-! ### Cohort-based RSKBijection (concrete via explicit cohort lists)

    Bypass `Nat.Partition n` (whose `Fintype.card` API is
    upstream-dependent) by working over a `List`-based cohort.
    The classical Burnside identity `Σ d_λ² = n!` is then
    discharged directly from the cohort's `n*_squares_sum_eq`
    theorem — no upstream Mathlib gap. -/

/-- A cohort-based RSK bijection witness: a finite list of
    `(name, syt_count)` tuples whose squared sum equals `n!`. -/
structure CohortRSKWitness (n : ℕ) where
  /-- The cohort entries: SYT counts indexed by some opaque label. -/
  syt_counts : List ℕ
  /-- Σ d_λ² = n!. -/
  burnside_holds : (syt_counts.map (· ^ 2)).sum = n.factorial
  -- (The former `matches_partition_count : syt_counts.length ≥ 0` field was removed
  --  2026-06-28: `length ≥ 0` is `Nat.zero_le`, provably vacuous — it constrained nothing.
  --  `burnside_holds` carries the real content; cohort/partition-count alignment, if needed,
  --  belongs as a separate proved lemma, not a trivially-true structure field.)

end QOU.Mathlib.RSKBridge
