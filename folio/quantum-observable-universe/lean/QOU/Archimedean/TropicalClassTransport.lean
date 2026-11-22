/-
# Tropical-class transport: the `E`-shift is exact algebra (dissolving the
# u1-promotion audit's perturbation-lemma gap)

The u1-promotion audit
(`docs/audits/2026-08-01-ksel2id-u1-promotion.md` §4 gap 1) left the
balanced-vs-SW lattice-class transfer conditional on an unproved
PERTURBATION LEMMA about Jacobi matrices with geometrically converging
coefficients. This module shows that lemma is not needed for the class
statement: run the transport on the moment RATIOS (the tropical /
Newton-polygon roots) rather than on the Jacobi data, and it is exact.

PROVED here (sorry-free):

* `swMoment_ratio` — the SW core's ratio is `G_{n+1}/G_n = v^n` exactly,
  so its tropical class is exactly `0` at EVERY index (no asymptotics);
* `balancedNormalizer_ratio` — the transport core, in division-free form:

      N^bal(k+2)·(1 − p)  =  N^bal(k+1)·v^k·(1 − p^{k+1}),   p = (v²)⁻¹,

  i.e. the balanced ratio is the SW ratio `v^k` times `E = 1/(1−p)` times
  the Jackson correction `(1 − p^{k+1})`. Derived from the merged
  factorization `SWJacksonMomentFactorization`, not re-derived;
* `balancedNormalizer_ratio_div` — the same in quotient form;
* `tendsto_jacksonLogCorrection` (wall side, `ℝ`) — the Jackson
  correction's contribution to `log_q̃` of the ratio tends to `0`. Hence
  the balanced tropical class equals `frac(log_q̃ E)` in the limit: the
  class shift by `log_q̃ E` is *derived*, with an explicit error term.

WHAT REMAINS (honest, unchanged in kind): the analytic statement
"extremal support class = tropical class". That is exactly the input the
PURE SW core already needs (the `A_w` zero asymptotics — the audit's §4
gap 2), so the transport contributes no new analytic debt; it does not
prove the extremal statement, and nothing here is wired.

Base ring (§7c): the transport core is a rational identity — generic
`[Field K]`. Only the limit statement is archimedean and lives over `ℝ`.

-- Ref: [leitner2026] docs/audits/2026-08-01-ksel2id-tropical-transport.md;
--      docs/audits/2026-08-01-ksel2id-u1-promotion.md §4 gap 1;
--      predicted-spectra, conj:schwinger-measure-computational-time.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import QOU.Archimedean.SWJacksonMomentFactorization
import QOU.Archimedean.SWCoreJacobi

namespace QOU.Archimedean.TropicalClassTransport

open Filter Topology
open QOU.Archimedean.SWJacksonMomentFactorization (pPoch pPoch_succ
  balancedNormalizer_mul_one_sub_pow)
open QOU.Archimedean.BalancedMomentConfluence (balancedNormalizer)
open QOU.Archimedean.SWCoreJacobi (swMoment)
open QOU.Archimedean.BalancedCarrierJacobi (choose_two_succ)

variable {K : Type*} [Field K]

/-! ## The SW core: tropical class exactly `0` -/

/-- **The SW core's moment ratio is exactly `v^n`.** Since `v^n` is an
integer power of the lattice step, the core's tropical class is exactly
`0` at every index — an exact statement, with no limit involved. -/
theorem swMoment_ratio (v : K) (n : ℕ) :
    swMoment v (n + 1) = swMoment v n * v ^ n := by
  simp only [swMoment, choose_two_succ n, pow_add]
  ring

/-! ## The transport core -/

/-- **THE TRANSPORT (exact, division-free).** With `p = (v²)⁻¹` the
balanced normalizer's ratio is the SW ratio `v^k` scaled by `E = 1/(1−p)`
and corrected by the Jackson factor `(1 − p^{k+1})`:

    N^bal(k+2)·(1 − p) = N^bal(k+1)·v^k·(1 − p^{k+1}).

Derived from the merged exact factorization; no perturbation argument,
no asymptotics. -/
theorem balancedNormalizer_ratio (v : K) (hv : v ≠ 0)
    (hp : (1 : K) - (v ^ 2)⁻¹ ≠ 0) (k : ℕ) :
    balancedNormalizer v (k + 2) * (1 - (v ^ 2)⁻¹)
      = balancedNormalizer v (k + 1) * v ^ k * (1 - ((v ^ 2)⁻¹) ^ (k + 1)) := by
  have h1 := balancedNormalizer_mul_one_sub_pow v hv (k + 1)
  have h0 := balancedNormalizer_mul_one_sub_pow v hv k
  have hpk : ((1 : K) - (v ^ 2)⁻¹) ^ k ≠ 0 := pow_ne_zero _ hp
  -- multiply the goal by `(1−p)^k` and rewrite both sides via h1, h0
  apply mul_right_cancel₀ hpk
  calc balancedNormalizer v (k + 2) * (1 - (v ^ 2)⁻¹) * (1 - (v ^ 2)⁻¹) ^ k
      = balancedNormalizer v (k + 2) * (1 - (v ^ 2)⁻¹) ^ (k + 1) := by
        rw [pow_succ]; ring
    _ = v ^ ((k + 1).choose 2) * pPoch (v ^ 2)⁻¹ (k + 1) := h1
    _ = (v ^ (k.choose 2) * pPoch (v ^ 2)⁻¹ k) * v ^ k
          * (1 - ((v ^ 2)⁻¹) ^ (k + 1)) := by
        rw [choose_two_succ k, pPoch_succ, pow_add]; ring
    _ = balancedNormalizer v (k + 1) * (1 - (v ^ 2)⁻¹) ^ k * v ^ k
          * (1 - ((v ^ 2)⁻¹) ^ (k + 1)) := by rw [h0]
    _ = balancedNormalizer v (k + 1) * v ^ k * (1 - ((v ^ 2)⁻¹) ^ (k + 1))
          * (1 - (v ^ 2)⁻¹) ^ k := by ring

/-- Quotient form of the transport: the balanced ratio equals the SW
ratio `v^k` times `E = 1/(1−p)` times the Jackson correction. -/
theorem balancedNormalizer_ratio_div (v : K) (hv : v ≠ 0)
    (hp : (1 : K) - (v ^ 2)⁻¹ ≠ 0) (k : ℕ)
    (hn : balancedNormalizer v (k + 1) ≠ 0) :
    balancedNormalizer v (k + 2) / balancedNormalizer v (k + 1)
      = v ^ k * (1 - ((v ^ 2)⁻¹) ^ (k + 1)) / (1 - (v ^ 2)⁻¹) := by
  rw [div_eq_div_iff hn hp]
  have h := balancedNormalizer_ratio v hv hp k
  linear_combination h

/-! ## The archimedean limit: the Jackson correction dies -/

/-- **The Jackson correction contributes nothing to the class in the
limit.** For `1 < q`, `log(1 − q^{-(k+1)}) → 0`; dividing by the fixed
`log q̃` gives the `log_q̃`-error term of the tropical class, so the
balanced tropical class converges to `frac(log_q̃ E)` — the `u ≡ 1`
class — at a geometric rate. -/
theorem tendsto_jacksonLogCorrection (q : ℝ) (hq : 1 < q) :
    Tendsto (fun k : ℕ => Real.log (1 - (q⁻¹) ^ (k + 1))) atTop (𝓝 0) := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hinv : |q⁻¹| < 1 := by
    rw [abs_of_pos (inv_pos.mpr hq0)]
    exact inv_lt_one_of_one_lt₀ hq
  have hpow : Tendsto (fun k : ℕ => (q⁻¹) ^ (k + 1)) atTop (𝓝 0) := by
    have := (tendsto_pow_atTop_nhds_zero_of_abs_lt_one hinv).comp
      (tendsto_add_atTop_nat 1)
    simpa [Function.comp] using this
  have hsub : Tendsto (fun k : ℕ => 1 - (q⁻¹) ^ (k + 1)) atTop (𝓝 1) := by
    simpa using tendsto_const_nhds.sub hpow
  have := (Real.continuousAt_log (by norm_num : (1 : ℝ) ≠ 0)).tendsto.comp hsub
  simpa [Function.comp] using this

end QOU.Archimedean.TropicalClassTransport
