/-
  Bean `qou-rq9n` — evidence that survives the fix it accompanies.

  `lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean` used to ship a
  "canonical instance bundle": five unconditional global instances discharging
  its five q-NS carriers with zero. That bundle was the evidence
  `vacuous-prop-carrier-baseline.json` cited for those carriers — the corpus
  proved them vacuous itself, by inhabiting them.

  Removing the bundle (2026-08-30) closed the downstream hole and, in the same
  stroke, deleted the citation. This file replaces it, so the finding does not
  rest on a construction that no longer exists.

  THE POINT, which the removal alone could obscure: inhabitability is a
  property of the carriers' FIELDS, not of whether the file ships an instance.
  Removing the bundle stopped every `[C]`-conditional theorem in the cone from
  being dischargeable at its call site; it did NOT give the carriers content.
  Four of the five are still provable with no hypotheses, below — `CriticalExponent`
  is the exception and left this file; see the note where its example used to
  be. That is why
  `qou-rq9n`'s remaining work — encoding what the q-Aubin–Lions compactness
  claim, the blow-up bound and the critical exponent actually say — is
  untouched by the removal and is still open.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a `lake
  build` against a restored cache with `traces=0` evicts the restore):

      LEAN_PATH=<mathlib libs>:<dir holding QOU/AlgebraicSubstrate/ConditionalClasses.olean> \
        lean docs/audits/2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.AlgebraicSubstrate.ConditionalClasses

open QOU.AlgebraicSubstrate

/-- `∃ K, 0 ≤ K ∧ K ≤ 2·E` — witnessed by `K = 0`. The docstring claims "`K`
scales linearly with the energy bound"; linear scaling is not encoded. -/
example : QAubinLions := ⟨fun _ _ => ⟨0, le_refl 0, by linarith⟩⟩

/-- `∀ D₀ ≥ 0, ∃ T, 0 ≤ T`. `D₀` is bound and never mentioned again, so the
field says only "there exists a non-negative real". -/
example : NSCounterexample := ⟨fun _ _ => ⟨0, le_refl 0⟩⟩

/-  `CriticalExponent` WAS the fifth entry here, as

        example : CriticalExponent := ⟨rfl⟩

    and it is deliberately gone. It is no longer vacuous: `qou-93hu` replaced
    its field — a closed numeral identity `(3 * 4 : ℕ) = 12` with no exponent
    variable in it — with `alpha_eq : α = 4/3` over a class parameter. So the
    carrier now constrains `α` (`¬ CriticalExponent 2` is provable), it left
    the probe baseline as "no longer matches the filter" (23 → 22), and the
    line above no longer even elaborates: `CriticalExponent` is `ℝ → Prop`,
    not a type.

    **Recorded rather than silently deleted, because the stale line was caught
    by the merge pipeline and not by me.** I made the `qou-93hu` fix, verified
    the three affected modules and an ad-hoc probe, and did not re-run this
    committed file — so this evidence artifact spent two commits asserting a
    carrier was vacuous after I had proved it was not. The type error was the
    visible symptom; the false claim was the defect. -/

/-- `∃ r, 0 ≤ r ∧ r ≤ 1 + T` — witnessed by `r = 0`, i.e. by NO blow-up, the
negation of the claim the carrier is named for. -/
example : BlowupYekutieli := ⟨fun _ hT => ⟨0, le_refl 0, by linarith⟩⟩

/-- `∃ μ, 0 ≤ μ ∧ μ ≤ s` — witnessed by `μ = 0`. Note the witness reuses the
hypothesis `hs` directly: the proof term IS the hypothesis. -/
example : RegularityBreakdown := ⟨fun _ hs => ⟨0, le_refl 0, hs⟩⟩
