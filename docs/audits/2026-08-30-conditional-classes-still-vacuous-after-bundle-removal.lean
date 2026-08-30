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
  All five are still provable with no hypotheses, below. That is why
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

/-- The whole content is `(3 * 4 : ℕ) = 12` — a closed numeral identity with no
exponent variable in it, so nothing constrains α. `rfl` proves it whatever the
physics. -/
example : CriticalExponent := ⟨rfl⟩

/-- `∃ r, 0 ≤ r ∧ r ≤ 1 + T` — witnessed by `r = 0`, i.e. by NO blow-up, the
negation of the claim the carrier is named for. -/
example : BlowupYekutieli := ⟨fun _ hT => ⟨0, le_refl 0, by linarith⟩⟩

/-- `∃ μ, 0 ≤ μ ∧ μ ≤ s` — witnessed by `μ = 0`. Note the witness reuses the
hypothesis `hs` directly: the proof term IS the hypothesis. -/
example : RegularityBreakdown := ⟨fun _ hs => ⟨0, le_refl 0, hs⟩⟩
