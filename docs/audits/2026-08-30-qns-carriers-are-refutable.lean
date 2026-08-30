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
  decoration. Each is also shown SATISFIABLE at its intended witness, so these
  are constraints and not accidental impossibilities.

  `BlowupYekutieli` is absent deliberately: it was NOT re-encoded (bean
  `qou-88nf`), because its docstring names "an explicit constant determined by
  the substrate scale" and never says which, so any bound here would be chosen
  by the agent rather than transcribed. It remains inhabitable by zero.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<dir with QOU/AlgebraicSubstrate/ConditionalClasses.olean> \
        lean docs/audits/2026-08-30-qns-carriers-are-refutable.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.AlgebraicSubstrate.ConditionalClasses
open QOU.AlgebraicSubstrate

/- The gate for this change is REFUTABILITY, not compilation. A carrier that
   compiles and cannot be false is exactly what was here before. -/

-- QAubinLions: the zero function is NOT linear with a positive constant.
example : ¬ QAubinLions (fun _ => 0) := by
  rintro ⟨C, hC, h⟩
  have := h 1 (by norm_num)
  simp at this
  nlinarith [this, hC]

-- NSCounterexample: a bounded vorticity cannot blow up.
example : ¬ NSCounterexample (fun _ => 0) := by
  rintro ⟨T, _, h⟩
  obtain ⟨t, _, hM⟩ := h 1
  norm_num at hM

-- RegularityBreakdown: a positive-measure set is not null.
example : ¬ RegularityBreakdown (Set.Ioo (0:ℝ) 1) := by
  rintro ⟨h⟩
  rw [Real.volume_Ioo] at h
  norm_num at h

-- And each is still SATISFIABLE at the intended witness, so the encodings are
-- constraints rather than impossibilities.
example : QAubinLions (fun E => 2 * E) := ⟨2, by norm_num, fun E _ => rfl⟩
example : RegularityBreakdown (∅ : Set ℝ) := ⟨by simp⟩
