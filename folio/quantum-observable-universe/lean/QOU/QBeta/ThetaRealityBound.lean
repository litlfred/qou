import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# QOU.QBeta.ThetaRealityBound — what the T5 channel actually constrains

The T5 assembly (`DeltaLambdaT5Assembly.lean`) reads

  `S_K = A · κ · (ln²q₀ − ϑ_K²)`,   `κ = √3/4`,

and the T4 crux probe back-solved `ϑ_K` at the two anchors under the
constant `A = A_ω = 3`, reporting two checks: **both ϑ real**, and the
**boost/spin diagonal crossed** (`ϑ_μ < ln q₀ < ϑ_p`). The channel audit
of 2026-08-01 (`docs/audits/2026-08-01-3bp8-entirety-and-channel-correctness.md`)
then measured the substrate deformation of the σ₁σ₂ Stokes entry and
compared candidate values of `A` against those two checks.

This file settles, by proof rather than by numerical substitution, **what
those checks are actually worth**. Writing `ϑ² = ln²q₀ − S/(Aκ)`:

* `thetaSq_lt_of_pos` / `lt_thetaSq_of_neg` — for **any** `A, κ > 0`, a
  positive `S` forces `ϑ² < ln²q₀` and a negative `S` forces
  `ϑ² > ln²q₀`. Hence:
* `diagonal_crossed` — the boost/spin diagonal crossing is **equivalent to
  the sign flip of `S` itself** and holds for **every** positive `A`. It
  is therefore *not* evidence for any particular `A` — a deflation of one
  of the two T4 checks.
* `thetaSq_nonneg_iff` — reality of `ϑ` is a **one-sided lower bound**
  `A ≥ S/(κ·ln²q₀)`, and it binds only at the anchor with `S > 0`; the
  `S < 0` anchor is automatically real (`thetaSq_pos_of_neg`).

So the honest content of the audit's discriminator table is: the
constraint is `A ≥ A_c` with `A_c = S_μ/(κ·ln²q₀) ≈ 2.054`. The raw
σ₁σ₂ entry `1.5852` **fails** it; both `3` and the normalized value-ratio
`3.7067` **pass**. The table does *not* select between those two — a
sharper statement than the audit's prose, and the reason this file exists.

Nothing here derives `A_ω`; these are structural facts about the channel.

-- Ref: [leitner2026] docs/audits/2026-08-01-3bp8-entirety-and-channel-correctness.md
-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062
-/

namespace QOU.QBeta.ThetaRealityBound

/-- `ϑ²` as read off the T5 channel `S = A·κ·(ln²q₀ − ϑ²)`. -/
noncomputable def thetaSq (A κ lnq S : ℝ) : ℝ := lnq ^ 2 - S / (A * κ)

/-- **Boost domination is automatic for a positive leak.** If `S > 0` then
`ϑ² < ln²q₀` for every positive `A, κ` — no constraint on `A`. -/
theorem thetaSq_lt_of_pos {A κ lnq S : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS : 0 < S) : thetaSq A κ lnq S < lnq ^ 2 := by
  have hAκ : 0 < A * κ := mul_pos hA hκ
  have : 0 < S / (A * κ) := div_pos hS hAκ
  unfold thetaSq
  linarith

/-- **Spin domination is automatic for a negative leak.** If `S < 0` then
`ϑ² > ln²q₀` for every positive `A, κ`. -/
theorem lt_thetaSq_of_neg {A κ lnq S : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS : S < 0) : lnq ^ 2 < thetaSq A κ lnq S := by
  have hAκ : 0 < A * κ := mul_pos hA hκ
  have : S / (A * κ) < 0 := div_neg_of_neg_of_pos hS hAκ
  unfold thetaSq
  linarith

/-- In particular a negative leak always yields a genuinely real `ϑ`
(`ϑ² > 0`) once `ln q₀ ≠ 0`. -/
theorem thetaSq_pos_of_neg {A κ lnq S : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS : S < 0) (hlnq : lnq ≠ 0) : 0 < thetaSq A κ lnq S :=
  lt_of_lt_of_le (by positivity) (le_of_lt (lt_thetaSq_of_neg hA hκ hS))

/-- **The boost/spin diagonal crossing is equivalent to the sign flip of
`S`, for EVERY positive `A`.** Given one anchor with `S₁ > 0` and one with
`S₂ < 0`, the crossing `ϑ₁² < ln²q₀ < ϑ₂²` holds unconditionally in `A`.

Consequence (the deflation): the T4 crux probe's "diagonal crossed ✓" is
an identity given the measured sign flip — it is **not** independent
evidence for `A = 3`, nor for any other value. -/
theorem diagonal_crossed {A κ lnq S₁ S₂ : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS₁ : 0 < S₁) (hS₂ : S₂ < 0) :
    thetaSq A κ lnq S₁ < lnq ^ 2 ∧ lnq ^ 2 < thetaSq A κ lnq S₂ :=
  ⟨thetaSq_lt_of_pos hA hκ hS₁, lt_thetaSq_of_neg hA hκ hS₂⟩

/-- **Reality of `ϑ` at a positive-leak anchor is exactly a lower bound on
`A`.** For `S, κ, ln q₀ > 0`:  `ϑ² ≥ 0 ↔ S/(κ·ln²q₀) ≤ A`.

This is the only constraint the T5 channel places on `A` from the two
anchors — one-sided, and binding only at the `S > 0` anchor. -/
theorem thetaSq_nonneg_iff {A κ lnq S : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS : 0 < S) (hlnq : 0 < lnq) :
    0 ≤ thetaSq A κ lnq S ↔ S / (κ * lnq ^ 2) ≤ A := by
  have hAκ : 0 < A * κ := mul_pos hA hκ
  have hl2 : 0 < lnq ^ 2 := by positivity
  have hkl : 0 < κ * lnq ^ 2 := mul_pos hκ hl2
  unfold thetaSq
  rw [sub_nonneg, div_le_iff₀ hAκ, div_le_iff₀ hkl]
  constructor
  · intro h; nlinarith
  · intro h; nlinarith

/-- The critical value: `ϑ` is real at a positive-leak anchor exactly when
`A` is at least `A_c = S/(κ·ln²q₀)`. -/
noncomputable def criticalA (κ lnq S : ℝ) : ℝ := S / (κ * lnq ^ 2)

theorem real_iff_criticalA_le {A κ lnq S : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS : 0 < S) (hlnq : 0 < lnq) :
    0 ≤ thetaSq A κ lnq S ↔ criticalA κ lnq S ≤ A :=
  thetaSq_nonneg_iff hA hκ hS hlnq

/-- **Monotonicity: the bound is one-sided.** Any `A` above a value that
already yields a real `ϑ` also yields a real `ϑ`. So the reality check can
exclude candidates from below but never from above — it cannot select
among `3` and `3.7067`, only reject `1.5852`. -/
theorem thetaSq_nonneg_mono {A A' κ lnq S : ℝ} (hA : 0 < A) (hκ : 0 < κ)
    (hS : 0 < S) (hlnq : 0 < lnq) (hAA' : A ≤ A')
    (h : 0 ≤ thetaSq A κ lnq S) : 0 ≤ thetaSq A' κ lnq S := by
  have hA' : 0 < A' := lt_of_lt_of_le hA hAA'
  rw [thetaSq_nonneg_iff hA' hκ hS hlnq]
  rw [thetaSq_nonneg_iff hA hκ hS hlnq] at h
  linarith

end QOU.QBeta.ThetaRealityBound
