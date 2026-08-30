/-
  Bean `qou-rq9n` — the gate for the q-NS carrier re-encoding.

  Three of the five carriers in `ConditionalClasses.lean` were re-encoded on
  2026-08-30 by transcribing the claim each docstring already made:
  `QAubinLions` (`qou-3ytx`), `NSCounterexample` (`qou-5nj1`) and
  `RegularityBreakdown` (`qou-m7a2`), joining `CriticalExponent` (`qou-93hu`).

  COMPILATION IS NOT THE GATE. The previous fields compiled too, and AGENTS.md
  §3b-tax cited them as the model of a carrier "in the *shape* of the claim".
  The shape was right and the content was absent, because every field was an
  existential over a quantity the class got to pick — and an `∃` you witness
  yourself cannot be false.

  So the gate is REFUTABILITY: for each re-encoded carrier there must be a
  value at which the class is FALSE. That is what the previous fields could not
  offer and what makes a `[C]` hypothesis a real assumption rather than
  decoration.

  WHAT THIS FILE SHOWS, EXACTLY — stated narrowly on purpose:

    - refutations for all four re-encoded carriers;
    - satisfiability for `QAubinLions`, `RegularityBreakdown` and
      `CriticalExponent`.

  It does NOT exhibit a satisfiability witness for `NSCounterexample`, and the
  header said otherwise until review on PR #6122 caught it — an over-claim in a
  file whose whole job is to be evidence, which is the defect this arc keeps
  finding, here in my own audit.

  **Read that absence correctly.** A satisfiability witness for the blow-up
  carrier needs a function unbounded on *every* left-neighbourhood of `T` (e.g.
  `1/(1-t)` at `T = 1`) together with the ε-style argument picking `t` close
  enough to `T` for each `M` — a genuine analysis exercise, not a one-liner. Its
  absence here is a fact about this file's scope, **not** evidence that the
  class is uninhabitable. Forcing a fragile proof to make a header true would
  be the wrong trade.

  `BlowupYekutieli` is absent deliberately: it was NOT re-encoded (bean
  `qou-88nf`), because its docstring names "an explicit constant determined by
  the substrate scale" and never says which, so any bound would be chosen by the
  agent rather than transcribed. It remains inhabitable by zero. See
  `2026-08-30-blowup-yekutieli-has-no-source.md` — the rate is not in the corpus
  at all, and its conjecture block does not exist.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<dir with QOU/AlgebraicSubstrate/ConditionalClasses.olean> \
        lean docs/audits/2026-08-30-qns-carriers-are-refutable.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.AlgebraicSubstrate.ConditionalClasses

open QOU.AlgebraicSubstrate

/-! ## Refutations — the gate -/

/-- The zero function is not linear with a strictly positive constant. -/
example : ¬ QAubinLions (fun _ => 0) := by
  rintro ⟨C, hC, h⟩
  have := h 1 (by norm_num)
  simp at this
  nlinarith [this, hC]

/-- A bounded vorticity cannot blow up: the field demands values exceeding
every `M`, and the constant `0` function exceeds none. -/
example : ¬ NSCounterexample (fun _ => 0) := by
  rintro ⟨T, _, h⟩
  obtain ⟨t, _, _, hM⟩ := h 1 (T - 1) (by linarith)
  norm_num at hM

/-- A positive-measure set is not Lebesgue-null. -/
example : ¬ RegularityBreakdown (Set.Ioo (0:ℝ) 1) := by
  rintro ⟨h⟩
  rw [Real.volume_Ioo] at h
  norm_num at h

/-- Any exponent other than `4/3` refutes the critical-exponent carrier. -/
example : ¬ CriticalExponent 2 := by
  rintro ⟨h⟩; norm_num at h

/-! ## Satisfiability — three of the four, per the header -/

example : QAubinLions (fun E => 2 * E) := ⟨2, by norm_num, fun E _ => rfl⟩
example : RegularityBreakdown (∅ : Set ℝ) := ⟨by simp⟩
example : CriticalExponent (4 / 3) := ⟨rfl⟩
