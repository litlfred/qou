import QOU.QBeta.QBetaErrorBudget
import QOU.QBeta.OneSidedNonlinearMaps

/-!
# The one-sided lepton factor in the invariance-forced normalisation

Thread "Find where the n–p mass error comes from", 2026-11-21 (owner: "keep pushing on lepton").
Audit `docs/audits/2026-11-21-lepton-factor-forced-normalisation.md`.

## Setting

The eigenphase thread (PR #8836, `LeptonStrandNormalisation.lean` and the probe
`qbeta_lepton_normalisation`) derives the lepton normalisation `q^(−2 wr)·Tr(K ρ)/[2]^c`, lepton
strands summed. Three premises force it: agreement with D1, invariance under an idle strand, and
Markov invariance. On the γγ words the unlinked lepton block then takes exactly two values,
* `fE = (q⁴+1)/(q⁴(q²+1))` for e⁻ν̄, and
* `fM = q²(q⁴+1)/(q²+1)` for the mirror e⁺ν.

These closed forms are imported here as definitions (from the probe's exact check M5), not
derived.

## What is proved

1. `fM_eq`: `fM = q⁶·fE`.
2. `inv_sq_sub_fE`: `q⁻² − fE = (q²−1)/(q⁴(q²+1))`. So `fE < q⁻²` for every `q > 1`
   (`fE_lt_inv_sq`), and `fE(1) = 1`.
3. `one_lt_fM`: `fM > 1` for every `q > 1`.
4. Hence, for every `q > 1`, the unlinked e⁻ν̄ lies below the window `(ε_n, ε_p)` and the
   unlinked mirror lies above it (`unlinked_outside_window`). This is the q₀ finding of the
   earlier audit §16, now shown for every `q`.
5. `fForced_eq`: the one-sided functional `ε_n − ε_p·fE` equals
   `−ε_flavour(V³)/(q²(q²+1))`. With the forced normalisation, the one-sided placement is the
   two-sided scored cell times `1/(q²(q²+1))`.
6. `qbetaForced_eq`, `qbetaForced_one`, `qbetaForced_le`: `E₀^full·(ε_n − ε_p fE)/m_e =
   R(q)/(q²(q²+1))`, its `q = 1` value is `3/8`, and it is `≤ 3/8` for every `q ≥ 1`.
   The one-sided reading **halves** the classical value of the scored cell. It does not supply
   the missing factor; it widens the gap.

No numerical or empirical value is used.
-/

namespace QOU.QBeta.ForcedLeptonFactor

open QOU.QBeta.FlavourWeightSplit
open QOU.QBeta.QBetaErrorBudget
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

section Generic

variable {R : Type*} [Field R]

/-- Unlinked e⁻ν̄ lepton factor in the forced normalisation. -/
def fE (q : R) : R := (q ^ 4 + 1) / (q ^ 4 * (q ^ 2 + 1))

/-- Unlinked mirror e⁺ν lepton factor in the forced normalisation. -/
def fM (q : R) : R := q ^ 2 * (q ^ 4 + 1) / (q ^ 2 + 1)

/-- The one-sided functional with the forced lepton factor. -/
def fForced (q : R) : R := epsN q (borromeanV3B q) - epsP q (borromeanV3A q) * fE q

theorem fM_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : fM q = q ^ 6 * fE q := by
  unfold fM fE; field_simp

theorem inv_sq_sub_fE (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 / q ^ 2 - fE q = (q ^ 2 - 1) / (q ^ 4 * (q ^ 2 + 1)) := by
  unfold fE; field_simp; ring

theorem fE_one (h2 : (2 : R) ≠ 0) : fE (1 : R) = 1 := by
  unfold fE; norm_num
  exact div_self h2

/-- **The one-sided forced functional is the scored cell rescaled by `1/(q²(q²+1))`.** -/
theorem fForced_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    fForced q = -epsFlavourV3 q / (q ^ 2 * (q ^ 2 + 1)) := by
  unfold fForced epsFlavourV3 fE epsN epsP qd2
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  have e2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp; try ring
  rw [e2]
  field_simp
  ring

/-- **`E₀^full·F_forced/m_e = R(q)/(q²(q²+1))`.** -/
theorem qbetaForced_eq (q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : 2 * q - 1 ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    e0TowerOverMe q * fForced q = rClosed q / (q ^ 2 * (q ^ 2 + 1)) := by
  rw [fForced_eq q hq hq2, ← qbetaOverMe_eq q hq hq1 h2 hq2]
  unfold qbetaOverMe
  ring

end Generic

theorem fE_lt_inv_sq {q : ℝ} (hq1 : 1 < q) : fE q < 1 / q ^ 2 := by
  have hq : q ≠ 0 := by positivity
  have h := inv_sq_sub_fE q hq (by positivity)
  have : 0 < (q ^ 2 - 1) / (q ^ 4 * (q ^ 2 + 1)) := by
    apply div_pos (by nlinarith) (by positivity)
  linarith

theorem one_lt_fM {q : ℝ} (hq1 : 1 < q) : 1 < fM q := by
  unfold fM
  rw [one_lt_div (by positivity)]
  have : 1 < q ^ 4 := one_lt_pow₀ hq1 (by norm_num)
  nlinarith

/-- **For every `q` in the range, both unlinked lepton blocks miss the window `(ε_n, ε_p)`.** -/
theorem unlinked_outside_window {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    epsP q (borromeanV3A q) * fE q < epsN q (borromeanV3B q) ∧
      epsP q (borromeanV3A q) < epsP q (borromeanV3A q) * fM q := by
  have hp := QOU.QBeta.OneSidedReading.epsP_V3A_pos hq1 hq2
  have hq0 : 0 < q := by linarith
  rw [QOU.QBeta.OneSidedNonlinearMaps.epsN_V3B_eq hq0.ne']
  constructor
  · have := mul_lt_mul_of_pos_left (fE_lt_inv_sq hq1) hp
    rwa [mul_one_div] at this
  · have := mul_lt_mul_of_pos_left (one_lt_fM hq1) hp
    linarith

/-- **Classical value: `3/8`, half the scored cell's `3/4`.** -/
theorem qbetaForced_one : rClosed (1 : ℝ) / (1 ^ 2 * (1 ^ 2 + 1)) = 3 / 8 := by
  rw [rClosed_one]; norm_num

/-- **The one-sided forced cell is at most `3/8` for every `q ≥ 1`.** -/
theorem qbetaForced_le {q : ℝ} (hq : 1 ≤ q) : rClosed q / (q ^ 2 * (q ^ 2 + 1)) ≤ 3 / 8 := by
  have hR := rClosed_le_three_quarters hq
  have hq2 : 1 ≤ q ^ 2 := one_le_pow₀ hq
  have hd : 2 ≤ q ^ 2 * (q ^ 2 + 1) := by nlinarith
  rw [div_le_iff₀ (by positivity)]
  rcases le_or_gt (rClosed q) 0 with h | h
  · nlinarith
  · nlinarith

end QOU.QBeta.ForcedLeptonFactor
