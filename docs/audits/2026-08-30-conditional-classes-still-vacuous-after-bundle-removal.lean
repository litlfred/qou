/-
  Bean `qou-rq9n` — what is still vacuous in `ConditionalClasses.lean`.

  **NOTHING IS. The answer this file exists to give is now "none of them", and
  the file has been narrowed to nothing in a single day.**

  It began as evidence that all five q-NS carriers remained inhabitable by zero
  after the fabricated "canonical instance bundle" was removed — the bundle
  having been the corpus's own proof of their vacuity, so removing it deleted
  the citation. Then, in order:

  - `CriticalExponent` re-encoded (`qou-93hu`), later de-boxed (`qou-4670`);
  - `QAubinLions`, `NSCounterexample`, `RegularityBreakdown` re-encoded
    (`qou-3ytx`, `qou-5nj1`, `qou-m7a2`);
  - `BlowupYekutieli` **replaced** (`qou-88nf`) — the last one.

  So this file no longer carries an example, and that absence is its result.
  Deleting it instead would destroy the record of what the five used to be and
  why each stopped being it; an evidence file whose finding has gone to zero
  should say so, not vanish.

  **`BlowupYekutieli` was REPLACED, not re-encoded, and the distinction is the
  reason it took a second attempt.** Its field was
  `∀ T ≥ 0, ∃ r, 0 ≤ r ∧ r ≤ 1 + T`, witnessed by `r = 0` — by *no blow-up*,
  the negation of the claim the carrier is named for. It was left alone on the
  stated grounds that its docstring promised "an explicit constant determined
  by the substrate scale" and never said which, so writing a bound would have
  meant choosing it; and an audit reported that the rate is nowhere in the
  corpus and that "its conjecture block does not exist".

  The first half of that stands — **there is still no Yekutieli blow-up rate in
  this corpus, and none may be invented.** The second half was wrong, and wrong
  in a way worth recording: there is no `conj:blowup-yekutieli`, which is what
  the grep tested, but the block is live under the label **`prop:`** in
  `lifting-and-descent/`, with ten blocks interpreting or using it. It had
  moved chapters. Its carrier states `smooth ↔ ∀ n, obstruction n = 0` — about
  obstruction-class vanishing, not about a rate — so the transcription never
  needed a rate at all, and a `[BlowupYekutieli …]` binder written before
  2026-08-30 does not mean what one written after it means.

  **Why the narrowing matters more than the file.** Each time a carrier was
  fixed, the example asserting it vacuous became a FALSE CLAIM in an artifact
  whose whole job is to be evidence — and on the first occasion that was caught
  by a merge pipeline rather than by me, two commits after the fact. An
  evidence file tracks the thing it is evidence about or it silently becomes
  the opposite. That is why this header records what left and when, and why the
  final example is removed rather than left to rot: it would no longer compile,
  and if it did it would be a lie.

  For the complementary direction — that all five carriers are now REFUTABLE,
  which is what "has content" actually means here — see
  [`2026-08-30-qns-carriers-are-refutable.lean`](2026-08-30-qns-carriers-are-refutable.lean),
  which carries the witnesses.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<dir with QOU/AlgebraicSubstrate/ConditionalClasses.olean> \
        lean docs/audits/2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean

  Measured 2026-08-30: exit 0, 0 errors. The import is retained deliberately —
  it keeps this file compiling against the real classes, so a future change
  that reintroduced a vacuous carrier here would still be checked against a
  file that says there are none.
-/
import QOU.AlgebraicSubstrate.ConditionalClasses

open QOU.AlgebraicSubstrate

-- No example. Every carrier in `ConditionalClasses.lean` now constrains a
-- caller-supplied parameter, so none can be inhabited with no hypotheses.
-- The refutations and satisfiability witnesses live in the companion file.
