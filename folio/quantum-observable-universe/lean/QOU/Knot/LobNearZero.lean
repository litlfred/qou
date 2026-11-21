/-
  Λ NEAR ZERO — the CONSTANT of Euler–Maclaurin — bean `qou-mlgp` (A).

  WHAT THIS PROVES.

      |Λ(b) − (b − b·log(2b))| ≤ b³/3        for 0 < b ≤ 1.

  WHY IT IS THE CRUX.  The Kashaev sum `s_k = −∑_{j≤k} log(2 sin(jπ/N))` is
  turned into an integral by Euler–Maclaurin on `[h, θ]`, `h = π/N`, and the
  closed form of that integral is `Λ(h) − Λ(θ)` plus elementary terms.  The
  `θ` end is harmless; the `h` end carries the whole difficulty, because
  `(1/h)·Λ(h)` is `O(1/h)` and only the *exact* small-`t` behaviour of `Λ`
  makes it cancel against `k·log(2π/N)` and Stirling.  Getting the CONSTANT —
  not merely the rate — is what gap (A) always was.  `−½log(2N sin θ)` is what
  survives the cancellation, and it is visible only at this precision.

  THE PROOF, and why it is not circular.  `Λ' = −log(2 sin)` gives, for
  `0 < ε ≤ b < π`,

      Λ(ε) − Λ(b) = ∫_ε^b log(2 sin t) dt
                  = ∫_ε^b logSinc t dt + ∫_ε^b log(2t) dt

  splitting the integrand at its own singularity: `logSinc t = log(sin t) −
  log t` is BOUNDED (`|logSinc t| ≤ t²/3`, `LogSincNearZero`), and `log(2t)`
  integrates in closed form.  So for every `ε`

      |[Λ(b) − (b − b·log 2b)] − [Λ(ε) + ε·log(2ε) − ε]| ≤ b³/3.

  Letting `ε → 0⁺` kills the second bracket: `Λ` is continuous (Weierstrass
  M-test on the Clausen series — `continuous_Cl_2` below, which the corpus did
  not have) and `x·log x → 0` (`Real.continuous_mul_log`).  No expansion of `Λ`
  is assumed anywhere; the constant is DERIVED from `Λ(0) = 0` plus the
  boundedness of `logSinc`.

  -- Ref: [leitner2026] QOU/Knot/LogSincNearZero.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevReflectionTrapezoid.lean
  -- Ref: [leitner2026] QOU/Archimedean/BlochWignerLobachevsky.lean
-/
import QOU.Knot.LogSincNearZero
import QOU.Knot.KashaevReflectionTrapezoid
import Mathlib.Analysis.Normed.Group.FunctionSeries
import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-! ## Part 1 — `Cl₂` and `Λ` are continuous

The corpus defines `Cl_2` as a `tsum` and proves summability, but never
continuity, which the `ε → 0` limit below needs.  The Weierstrass M-test
applies verbatim: `|sin(nθ)/n²| ≤ 1/n²` uniformly in `θ`. -/

/-- **`Cl₂` is continuous**, by the Weierstrass M-test against `∑ 1/(k+1)²`. -/
theorem continuous_Cl_2 : Continuous Cl_2 := by
  have hsum : Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
    have h : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      Real.summable_one_div_nat_pow.mpr one_lt_two
    have h2 := (summable_nat_add_iff 1).mpr h
    simpa using h2
  have := continuous_tsum
    (f := fun (k : ℕ) (θ : ℝ) => Real.sin (((k : ℝ) + 1) * θ) / ((k : ℝ) + 1) ^ 2)
    (u := fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2)
    (fun k => (Real.continuous_sin.comp (continuous_const.mul continuous_id)).div_const _)
    hsum
    (fun k θ => by
      have hpos : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
      rw [Real.norm_eq_abs, abs_div, abs_of_pos hpos, div_le_div_iff₀ hpos hpos]
      nlinarith [Real.abs_sin_le_one (((k : ℝ) + 1) * θ), hpos])
  exact this

/-- **`Λ` is continuous.**  `Λ(t) = Cl₂(2t)/2`. -/
theorem continuous_Lob : Continuous Lob :=
  (continuous_Cl_2.comp (continuous_const.mul continuous_id)).div_const _

/-! ## Part 2 — splitting the integrand at its own singularity -/

/-- **`log(2 sin t) = logSinc t + log(2t)`** on `(0, π)`.  Both `log`s split
because `sin t > 0` and `t > 0` there. -/
theorem log_two_sin_eq_logSinc_add {t : ℝ} (ht : 0 < t) (htpi : t < π) :
    Real.log (2 * Real.sin t) = logSinc t + Real.log (2 * t) := by
  have hs : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi ht htpi
  unfold logSinc
  rw [Real.log_mul two_ne_zero (ne_of_gt hs), Real.log_mul two_ne_zero (ne_of_gt ht)]
  ring

/-- **`∫_a^b log(2t) dt = b·log(2b) − b − (a·log(2a) − a)`** for `0 < a ≤ b`. -/
theorem integral_log_two_mul {a b : ℝ} (ha : 0 < a) (hab : a ≤ b) :
    (∫ t in a..b, Real.log (2 * t))
      = b * Real.log (2 * b) - b - (a * Real.log (2 * a) - a) := by
  have hb : 0 < b := lt_of_lt_of_le ha hab
  have hcong : (∫ t in a..b, Real.log (2 * t))
      = ∫ t in a..b, (Real.log 2 + Real.log t) := by
    refine intervalIntegral.integral_congr (fun t ht => ?_)
    rw [Set.uIcc_of_le hab, Set.mem_Icc] at ht
    exact Real.log_mul two_ne_zero (ne_of_gt (lt_of_lt_of_le ha ht.1))
  rw [hcong, intervalIntegral.integral_add
    (intervalIntegrable_const) (intervalIntegral.intervalIntegrable_log' ..),
    intervalIntegral.integral_const, integral_log,
    Real.log_mul two_ne_zero (ne_of_gt hb), Real.log_mul two_ne_zero (ne_of_gt ha),
    smul_eq_mul]
  ring

/-- `logSinc` is continuous on any `[a,b] ⊂ (0, π)` — it is differentiable
there (`hasDerivAt_logSinc`). -/
theorem continuousOn_logSinc {a b : ℝ} (ha : 0 < a) (hb : b < π) :
    ContinuousOn logSinc (Set.Icc a b) := by
  intro x hx
  rw [Set.mem_Icc] at hx
  exact (hasDerivAt_logSinc (lt_of_lt_of_le ha hx.1)
    (lt_of_le_of_lt hx.2 hb)).continuousAt.continuousWithinAt

/-- **`∫_a^b logSinc = (Λ(a) − Λ(b)) − (b log 2b − b − (a log 2a − a))`**
for `0 < a ≤ b < π`.  This is the FTC step with the singular part removed. -/
theorem integral_logSinc_eq {a b : ℝ} (ha : 0 < a) (hb : b < π) (hab : a ≤ b) :
    (∫ t in a..b, logSinc t)
      = (Lob a - Lob b) - (b * Real.log (2 * b) - b - (a * Real.log (2 * a) - a)) := by
  have hSint : IntervalIntegrable logSinc MeasureTheory.volume a b := by
    apply ContinuousOn.intervalIntegrable
    rw [Set.uIcc_of_le hab]
    exact continuousOn_logSinc ha hb
  have hLint : IntervalIntegrable (fun t => Real.log (2 * t)) MeasureTheory.volume a b := by
    apply ContinuousOn.intervalIntegrable
    intro x hx
    rw [Set.uIcc_of_le hab, Set.mem_Icc] at hx
    have hx0 : (0 : ℝ) < 2 * x := by nlinarith [lt_of_lt_of_le ha hx.1]
    exact ((Real.continuousAt_log (ne_of_gt hx0)).comp
      (continuous_const.mul continuous_id).continuousAt).continuousWithinAt
  have hsplit : (∫ t in a..b, Real.log (2 * Real.sin t))
      = (∫ t in a..b, logSinc t) + ∫ t in a..b, Real.log (2 * t) := by
    rw [← intervalIntegral.integral_add hSint hLint]
    refine intervalIntegral.integral_congr (fun t ht => ?_)
    rw [Set.uIcc_of_le hab, Set.mem_Icc] at ht
    exact log_two_sin_eq_logSinc_add (lt_of_lt_of_le ha ht.1) (lt_of_le_of_lt ht.2 hb)
  have hLob := integral_log_two_sin ha hb hab
  rw [hLob, integral_log_two_mul ha hab] at hsplit
  linarith

/-! ## Part 3 — the constant -/

/-- **Λ near zero, with its constant:** `|Λ(b) − (b − b·log(2b))| ≤ b³/3`
for `0 < b ≤ 1`.

This is the ingredient gap (A) was missing.  Everything else in the Kashaev
expansion is bookkeeping over Euler–Maclaurin and Stirling; this is where the
`−½log(2N sin θ)` constant comes from. -/
theorem abs_Lob_sub_near_zero {b : ℝ} (hb0 : 0 < b) (hb1 : b ≤ 1) :
    |Lob b - (b - b * Real.log (2 * b))| ≤ b ^ 3 / 3 := by
  have hbpi : b < π := lt_of_le_of_lt hb1 (by linarith [Real.two_le_pi])
  -- the `ε`-family, continuous at `0` with value `0`
  set B : ℝ → ℝ := fun ε => Lob ε + ε * Real.log (2 * ε) - ε with hBdef
  have hmulcont : Continuous (fun ε : ℝ => ε * Real.log (2 * ε)) := by
    have hrw : (fun ε : ℝ => ε * Real.log (2 * ε))
        = fun ε : ℝ => ((2 * ε) * Real.log (2 * ε)) / 2 := by
      funext ε; ring
    rw [hrw]
    exact ((Real.continuous_mul_log.comp
      (continuous_const.mul continuous_id))).div_const _
  have hBcont : Continuous B :=
    (continuous_Lob.add hmulcont).sub continuous_id
  have hB0 : B 0 = 0 := by simp [hBdef]
  -- the uniform bound for every `ε ∈ (0, b]`
  have key : ∀ ε ∈ Set.Ioc (0 : ℝ) b,
      |(Lob b - (b - b * Real.log (2 * b))) - B ε| ≤ b ^ 3 / 3 := by
    intro ε hε
    obtain ⟨hε0, hεb⟩ := hε
    have hI := integral_logSinc_eq hε0 hbpi hεb
    have hbound : ‖∫ t in ε..b, logSinc t‖ ≤ (b ^ 2 / 3) * |b - ε| := by
      refine intervalIntegral.norm_integral_le_of_norm_le_const (fun x hx => ?_)
      rw [Set.uIoc_of_le hεb, Set.mem_Ioc] at hx
      have hx0 : 0 < x := lt_trans hε0 hx.1
      have hx1 : x ≤ 1 := le_trans hx.2 hb1
      have := abs_logSinc_le hx0 hx1
      rw [Real.norm_eq_abs]
      nlinarith [sq_nonneg x, sq_nonneg (b - x), hx.2, hx0.le]
    have hlen : |b - ε| ≤ b := by rw [abs_of_nonneg (by linarith)]; linarith
    have hb2 : (0 : ℝ) ≤ b ^ 2 / 3 := by positivity
    have : ‖∫ t in ε..b, logSinc t‖ ≤ b ^ 3 / 3 := by
      refine le_trans hbound ?_
      calc (b ^ 2 / 3) * |b - ε| ≤ (b ^ 2 / 3) * b := by
            exact mul_le_mul_of_nonneg_left hlen hb2
        _ = b ^ 3 / 3 := by ring
    rw [Real.norm_eq_abs] at this
    rw [hI] at this
    rw [hBdef]
    calc |(Lob b - (b - b * Real.log (2 * b)))
            - (Lob ε + ε * Real.log (2 * ε) - ε)|
        = |(Lob ε - Lob b)
            - (b * Real.log (2 * b) - b - (ε * Real.log (2 * ε) - ε))| := by
          rw [abs_sub_comm]; ring_nf
      _ ≤ b ^ 3 / 3 := this
  -- pass to the limit `ε → 0⁺`
  have htend : Filter.Tendsto
      (fun ε => |(Lob b - (b - b * Real.log (2 * b))) - B ε|)
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds |(Lob b - (b - b * Real.log (2 * b))) - B 0|) :=
    ((continuous_abs.comp (continuous_const.sub hBcont)).tendsto 0).mono_left
      nhdsWithin_le_nhds
  have hfinal := le_of_tendsto htend
    (Filter.eventually_of_mem (Ioc_mem_nhdsGT hb0) key)
  rw [hB0, sub_zero] at hfinal
  exact hfinal

end QOU.Knot.FigureEightVolume
