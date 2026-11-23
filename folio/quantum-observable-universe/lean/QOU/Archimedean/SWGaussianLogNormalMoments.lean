import Mathlib.Probability.Distributions.Gaussian.Real
import QOU.Archimedean.SWJacksonMomentFactorization

/-!
# The SW-Gaussian factor `G_k = v^{C(k,2)}` as the moments of a log-normal measure

Bean `qou-jbo8`. `QOU.Archimedean.SWJacksonMomentFactorization` proves the moment-level
identity `m_k = G_k · J_k` with `G_k = v^{k(k−1)/2}`, and records that the reading
"`G_k` are the moments of the log-normal `LN(−L/2, L)`, `L = ln v`" was NOT formalized.
This file formalizes it.

The bean said Mathlib v4.24.0 lacks the Gaussian moment-generating function. It does not:
`ProbabilityTheory.mgf_gaussianReal` is in the pinned Mathlib
(`Mathlib/Probability/Distributions/Gaussian/Real.lean`). The bean's probe failed only
because that module's olean was not in the restored cache, so `exact?` could not see it.

* `swGaussian v hv` — the normal law `N(−L/2, L)` with `L = log v`, for `1 ≤ v`
  (so that the variance `L` is nonnegative).
* `swLogNormal v hv` — its push-forward under `exp`, the log-normal `LN(−L/2, L)`.
* `integral_exp_nat_mul_swGaussian` — `E[e^{kX}] = v^{C(k,2)}` for `X ~ N(−L/2, L)`.
* `integral_pow_swLogNormal` — the `k`-th moment of `LN(−L/2, L)` is `v^{C(k,2)} = G_k`.
* `balancedNormalizer_eq_logNormal_moment_mul_jackson` — the factorization
  `m_k = G_k · J_k` with `G_k` written as that log-normal moment (for `1 < v`).

What is still NOT formalized: the determinacy/compact support of the Jackson factor and
the convolution reading (bean `qou-x1rm` and the KSel-2-ID audit).

§7c: archimedean (`Real.log`, `Real.exp`, a measure on `ℝ`), so `ℝ` is genuine.

-- Ref: [christiansen2003sw] SW moment problem; [berg1995] indeterminate moment problems;
--      [leitner2026] docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md §1.
-/

open MeasureTheory ProbabilityTheory Real

namespace QOU.Archimedean.SWGaussianLogNormalMoments

open QOU.Archimedean.SWJacksonMomentFactorization (pPoch balancedNormalizer_eq_gauss_mul_jackson)
open QOU.Archimedean.BalancedMomentConfluence (balancedNormalizer)

/-- The normal law `N(−L/2, L)` with `L = log v`, for `1 ≤ v`. -/
noncomputable def swGaussian (v : ℝ) (hv : 1 ≤ v) : Measure ℝ :=
  gaussianReal (-(log v) / 2) ⟨log v, log_nonneg hv⟩

/-- The log-normal law `LN(−L/2, L)`, `L = log v`: the push-forward of `swGaussian` by `exp`. -/
noncomputable def swLogNormal (v : ℝ) (hv : 1 ≤ v) : Measure ℝ :=
  (swGaussian v hv).map exp

/-- `E[e^{kX}] = v^{C(k,2)}` for `X ~ N(−L/2, L)`, `L = log v`. -/
theorem integral_exp_nat_mul_swGaussian (v : ℝ) (hv : 1 ≤ v) (k : ℕ) :
    ∫ x, exp (k * x) ∂(swGaussian v hv) = v ^ (k.choose 2) := by
  have h := congrFun (mgf_id_gaussianReal (μ := -(log v) / 2) (v := ⟨log v, log_nonneg hv⟩))
    (k : ℝ)
  simp only [mgf, id] at h
  rw [swGaussian, h]
  have hv0 : 0 < v := lt_of_lt_of_le one_pos hv
  rw [← exp_log (pow_pos hv0 (k.choose 2)), log_pow, Nat.cast_choose_two]
  congr 1
  simp only [NNReal.coe_mk]
  ring

/-- **`G_k` is a moment sequence.** The `k`-th moment of the log-normal `LN(−L/2, L)`,
`L = log v`, is `v^{C(k,2)} = v^{k(k−1)/2}`. -/
theorem integral_pow_swLogNormal (v : ℝ) (hv : 1 ≤ v) (k : ℕ) :
    ∫ y, y ^ k ∂(swLogNormal v hv) = v ^ (k.choose 2) := by
  rw [swLogNormal, integral_map measurable_exp.aemeasurable
    (continuous_pow k).aestronglyMeasurable]
  simp_rw [← exp_nat_mul]
  exact integral_exp_nat_mul_swGaussian v hv k

/-- The SW ⊛ Jackson factorization with the Gaussian factor realized as a measure moment:
for `1 < v`, `N^bal(k+1) = (∫ y^k d LN(−L/2, L)) · (p;p)_k / (1 − p)^k`, `p = v⁻²`. -/
theorem balancedNormalizer_eq_logNormal_moment_mul_jackson (v : ℝ) (hv : 1 < v) (k : ℕ) :
    balancedNormalizer v (k + 1)
      = (∫ y, y ^ k ∂(swLogNormal v hv.le))
          * (pPoch (v ^ 2)⁻¹ k / (1 - (v ^ 2)⁻¹) ^ k) := by
  have hv0 : v ≠ 0 := by positivity
  have hp : (1 : ℝ) - (v ^ 2)⁻¹ ≠ 0 := by
    have : (v ^ 2)⁻¹ < 1 := inv_lt_one_of_one_lt₀ (one_lt_pow₀ hv two_ne_zero)
    linarith
  rw [integral_pow_swLogNormal v hv.le k]
  exact balancedNormalizer_eq_gauss_mul_jackson v hv0 hp k

end QOU.Archimedean.SWGaussianLogNormalMoments
