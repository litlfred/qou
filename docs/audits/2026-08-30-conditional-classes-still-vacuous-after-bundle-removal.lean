/-
  Bean `qou-rq9n` — what is STILL vacuous in `ConditionalClasses.lean`.

  **This file has been narrowed twice in one day, and both narrowings are the
  point rather than churn.**

  It began as evidence that all five q-NS carriers remained inhabitable by zero
  after the fabricated "canonical instance bundle" was removed — the bundle
  having been the corpus's own proof of their vacuity, so removing it deleted
  the citation. Since then:

  - `CriticalExponent` was re-encoded (`qou-93hu`) and left;
  - `QAubinLions`, `NSCounterexample` and `RegularityBreakdown` were re-encoded
    (`qou-3ytx`, `qou-5nj1`, `qou-m7a2`) and left.

  Four of five carriers have gained content, so **only `BlowupYekutieli`
  remains**, and this file is now about that one.

  **Why the narrowing matters more than the file.** Each time a carrier was
  fixed, the example asserting it vacuous became a FALSE CLAIM in an artifact
  whose whole job is to be evidence — and on the first occasion that was caught
  by a merge pipeline rather than by me, two commits after the fact. An
  evidence file tracks the thing it is evidence about or it silently becomes
  the opposite. That is why this header records what left and when.

  For the complementary direction — that the four re-encoded carriers are now
  REFUTABLE, which is what "has content" actually means here — see
  [`2026-08-30-qns-carriers-are-refutable.lean`](2026-08-30-qns-carriers-are-refutable.lean).

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<dir with QOU/AlgebraicSubstrate/ConditionalClasses.olean> \
        lean docs/audits/2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.AlgebraicSubstrate.ConditionalClasses

open QOU.AlgebraicSubstrate

/-- `∀ T ≥ 0, ∃ r, 0 ≤ r ∧ r ≤ 1 + T` — witnessed by `r = 0`, i.e. by **no
blow-up**, the negation of the claim the carrier is named for.

This is the one carrier in the file that could not be fixed by transcription:
its docstring promises "an explicit constant determined by the substrate scale"
and never says which constant, so writing a bound would mean choosing it.
Tracked as `qou-88nf`; the blocker is stated at the declaration. -/
example : BlowupYekutieli := ⟨fun _ hT => ⟨0, le_refl 0, by linarith⟩⟩
