/-
# No finite Hecke chart carries `Vol(4₁)/ℏ_q²`, and the canonical infinite one is off by the writhe

Bean `qou-91w7` (open "canonical chart" of the muon carrier); companions
`QOU.Observations.ElectronUnitSplit` and `QOU.Observations.QVolumeCarrier`; audit
`docs/audits/2026-11-22-energy-scale-cal-map.md` §8–9 and the 2026-11-27 addendum.

The carrier asks for a weight ratio `w_μ/w_e ~ V/ℏ_q²` near `q = 1` with `V = Vol(4₁)`.

**1. Finite Hecke charts.** Every convention-D (or HOMFLY-normalised) Markov trace of a word in
`H_n(q)` is an element of `ℚ(q)`: the Ocneanu weights and the seminormal matrices have entries in
`ℚ(q)`, and so does the HOMFLY unknot factor `δ`. So is any finite sum, product or quotient of
such traces, for any braid index. `rational_chart_leading_coeff` shows: if `f = P/Q` with
`P, Q ∈ K[X]` and `(q − 1)² f(q) → V ≠ 0` as `q → 1`, then `V ∈ K`. The `ℏ_q` form is
`rational_chart_leading_coeff_hbar`. Hence a finite Hecke chart with `ℚ`-structure constants that
carried `Vol(4₁)/ℏ_q²` would prove `Vol(4₁) ∈ ℚ` (with algebraic constants: `Vol(4₁)` algebraic).
Both are open problems (irrationality of `L(χ₋₃, 2)`) and believed false. So no finite Hecke chart
can be *shown* to carry the muon; the volume can only enter through an infinite sum or a limit.
This strengthens the "510× short" single-trace observation of audit §8: no finite combination of
traces, at any braid index, does better unless `Vol(4₁)` is rational.

**2. The canonical infinite chart.** The Hecke-side source of the volume is the quantum
dilogarithm `P(z; q) = ∏_{k ≥ 0} (1 − z q⁻ᵏ)` (Kashaev / colored Jones state sums are built from
its factors), with `log P ~ −Li₂(z)/ℏ_q`: the volume enters at order `1/ℏ_q`, in the exponent.
The order-two carrier appears canonically as its `q`-log-derivative ("energy" reading
`w = q ∂_q log Z`): termwise (`qvolume_term_log_deriv`),

  `q ∂_q [−wⁿ/(n(1 − q⁻ⁿ))] |_{w = zq} = zⁿ/(1 − q⁻ⁿ)²`,

which is exactly the summand of the q-volume `G` of `QVolumeCarrier`. So `G(z; q) =
(q ∂_q log P)(zq; q)`: this explains why `G` (and why `ℏ_q = 1 − q⁻¹`) is the right object. The
sum over `n` (uniform convergence) is not formalised here; the probe checks it to 48 digits.

**3. But the same reading fixes the electron at the writhe.** Applied to the electron's own trace
`τ_e = q³(q⁴+1)/(q²+1)²`, the energy reading gives `q ∂_q log τ_e → 3` at `q = 1`
(`tau_electron_log_deriv_at_one`: `τ_e(1) = 1/2`, `τ_e'(1) = 3/2`). The `3` is the writhe of
`σ₀σ₁σ₀`; the Ocneanu factor `y₍₃₎` is bar-invariant and contributes `0`. Then
`energy_reading_carrier`: `ℏ² w_μ/w_e → V/3`, which is not `V` (`energy_reading_ne_carrier`).
Without framing the electron's energy weight vanishes at `q = 1` and the pole order rises to 3.
Dividing by the writhe to get `V` would be a fit and is not done.

Everything is over a generic field or `ℝ`; `Vol(4₁)` enters only as an arbitrary `V ≠ 0`.
No measured value enters.
-/
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Topology.Algebra.Polynomial
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic

namespace QOU.Transcendental.MuonCarrierHeckeObstruction

open Filter Topology Polynomial

/-! ### 1. The rationality obstruction -/

/-- `X − 1` divides a polynomial exactly when `1` is a root. -/
private lemma eval_one_ne_zero_of_not_dvd {K : Type*} [Field K] {P : K[X]}
    (h : ¬ (X - C 1) ∣ P) : P.eval 1 ≠ 0 := by
  intro h0
  exact h (dvd_iff_isRoot.mpr h0)

/-- Factor out the root at `1`: `P = (X − 1)^a · P₁` with `P₁(1) ≠ 0`. -/
private lemma factor_at_one {K : Type*} [Field K] {P : K[X]} (hP : P ≠ 0) :
    ∃ (a : ℕ) (P₁ : K[X]), P = (X - C 1) ^ a * P₁ ∧ P₁.eval 1 ≠ 0 := by
  obtain ⟨P₁, hP₁, hn⟩ := exists_eq_pow_rootMultiplicity_mul_and_not_dvd P hP 1
  exact ⟨_, P₁, hP₁, eval_one_ne_zero_of_not_dvd hn⟩

/-- **The leading Laurent coefficient of a rational chart is in the coefficient field.**
Let `K` be a field with `K → ℝ`, and `f(q) = P(q)/Q(q)` with `P, Q ∈ K[X]`. If
`(q − 1)² f(q) → V` as `q → 1` (`q ≠ 1`) and `V ≠ 0`, then `V` is the image of an element of `K`.
For `K = ℚ` this covers every finite combination of Hecke (Ocneanu / HOMFLY) traces. -/
theorem rational_chart_leading_coeff {K : Type*} [Field K] [Algebra K ℝ]
    (P Q : K[X]) (hQ : Q ≠ 0) (V : ℝ) (hV : V ≠ 0)
    (hlim : Tendsto (fun q : ℝ => (q - 1) ^ 2 * (aeval q P / aeval q Q)) (𝓝[≠] 1) (𝓝 V)) :
    ∃ r : K, algebraMap K ℝ r = V := by
  by_cases hP : P = 0
  · exfalso
    have : Tendsto (fun q : ℝ => (q - 1) ^ 2 * (aeval q P / aeval q Q)) (𝓝[≠] 1) (𝓝 0) := by
      simp [hP]
    exact hV (tendsto_nhds_unique hlim this)
  obtain ⟨a, P₁, hPa, hP₁⟩ := factor_at_one hP
  obtain ⟨b, Q₁, hQb, hQ₁⟩ := factor_at_one hQ
  -- the regular part `g = P₁/Q₁`, continuous at 1 with non-zero value there
  set g : ℝ → ℝ := fun q => aeval q P₁ / aeval q Q₁
  have hinj := (algebraMap K ℝ).injective
  have hP₁' : aeval (1 : ℝ) P₁ ≠ 0 := by
    rw [show (1 : ℝ) = algebraMap K ℝ 1 by simp, aeval_algebraMap_apply_eq_algebraMap_eval]
    exact fun h => hP₁ (hinj (by simpa using h))
  have hQ₁' : aeval (1 : ℝ) Q₁ ≠ 0 := by
    rw [show (1 : ℝ) = algebraMap K ℝ 1 by simp, aeval_algebraMap_apply_eq_algebraMap_eval]
    exact fun h => hQ₁ (hinj (by simpa using h))
  have hg : Tendsto g (𝓝 1) (𝓝 (g 1)) := by
    have hcP : Continuous fun q : ℝ => aeval q P₁ := (Polynomial.continuous_aeval P₁)
    have hcQ : Continuous fun q : ℝ => aeval q Q₁ := (Polynomial.continuous_aeval Q₁)
    exact (hcP.tendsto 1).div (hcQ.tendsto 1) hQ₁'
  have hg1 : g 1 ≠ 0 := div_ne_zero hP₁' hQ₁'
  have hg' : Tendsto g (𝓝[≠] 1) (𝓝 (g 1)) := hg.mono_left nhdsWithin_le_nhds
  -- near 1 (q ≠ 1, Q₁(q) ≠ 0):  (q-1)^b · F(q) = (q-1)^(a+2) · g(q)
  set F : ℝ → ℝ := fun q => (q - 1) ^ 2 * (aeval q P / aeval q Q)
  have hQ₁ev : ∀ᶠ q in 𝓝[≠] (1 : ℝ), aeval q Q₁ ≠ 0 := by
    have hc : Continuous fun q : ℝ => aeval q Q₁ := Polynomial.continuous_aeval Q₁
    exact (nhdsWithin_le_nhds) ((hc.tendsto 1).eventually_ne hQ₁')
  have hne : ∀ᶠ q in 𝓝[≠] (1 : ℝ), q ≠ 1 := self_mem_nhdsWithin
  have hid : ∀ᶠ q in 𝓝[≠] (1 : ℝ), (q - 1) ^ b * F q = (q - 1) ^ (a + 2) * g q := by
    filter_upwards [hQ₁ev, hne] with q hq hq1
    have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
    simp only [F, g, hPa, hQb, map_mul, map_pow, map_sub, aeval_X, map_one]
    field_simp
    ring
  -- compare exponents
  rcases lt_trichotomy (a + 2) b with hlt | heq | hgt
  · -- (q-1)^(b-(a+2)) F = g eventually: LHS → 0, RHS → g 1 ≠ 0
    exfalso
    obtain ⟨k, hk⟩ : ∃ k, b = a + 2 + (k + 1) := ⟨b - (a + 2) - 1, by omega⟩
    have h1 : ∀ᶠ q in 𝓝[≠] (1 : ℝ), (q - 1) ^ (k + 1) * F q = g q := by
      filter_upwards [hid, hne] with q hq hq1
      have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
      rw [hk, pow_add] at hq
      rw [mul_assoc] at hq
      exact mul_left_cancel₀ (pow_ne_zero (a + 2) hq1') hq
    have hz : Tendsto (fun q : ℝ => (q - 1) ^ (k + 1) * F q) (𝓝[≠] 1) (𝓝 (0 * V)) := by
      have h0 : Tendsto (fun q : ℝ => (q - 1) ^ (k + 1)) (𝓝[≠] 1) (𝓝 0) := by
        have : Tendsto (fun q : ℝ => (q - 1) ^ (k + 1)) (𝓝 1) (𝓝 ((1 - 1) ^ (k + 1))) :=
          ((continuous_id.sub continuous_const).pow _).tendsto 1
        simpa using this.mono_left nhdsWithin_le_nhds
      exact h0.mul hlim
    rw [zero_mul] at hz
    exact hg1 (tendsto_nhds_unique (hg'.congr' (h1.mono fun q h => h.symm)) hz)
  · -- equal orders: F = g eventually, V = g 1 = P₁(1)/Q₁(1) ∈ K
    refine ⟨P₁.eval 1 / Q₁.eval 1, ?_⟩
    have h1 : ∀ᶠ q in 𝓝[≠] (1 : ℝ), F q = g q := by
      filter_upwards [hid, hne] with q hq hq1
      have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
      rw [heq] at hq
      exact mul_left_cancel₀ (pow_ne_zero b hq1') hq
    have hVg : V = g 1 := tendsto_nhds_unique hlim (hg'.congr' (h1.mono fun q h => h.symm))
    rw [hVg]
    simp only [g, map_div₀]
    rw [show (1 : ℝ) = algebraMap K ℝ 1 by simp, aeval_algebraMap_apply_eq_algebraMap_eval,
      aeval_algebraMap_apply_eq_algebraMap_eval]
  · -- F = (q-1)^(a+2-b) g eventually → 0, contradicting V ≠ 0
    exfalso
    obtain ⟨k, hk⟩ : ∃ k, a + 2 = b + (k + 1) := ⟨a + 2 - b - 1, by omega⟩
    have h1 : ∀ᶠ q in 𝓝[≠] (1 : ℝ), F q = (q - 1) ^ (k + 1) * g q := by
      filter_upwards [hid, hne] with q hq hq1
      have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
      rw [hk, pow_add, mul_assoc] at hq
      exact mul_left_cancel₀ (pow_ne_zero b hq1') hq
    have hz : Tendsto (fun q : ℝ => (q - 1) ^ (k + 1) * g q) (𝓝[≠] 1) (𝓝 (0 * g 1)) := by
      have h0 : Tendsto (fun q : ℝ => (q - 1) ^ (k + 1)) (𝓝[≠] 1) (𝓝 0) := by
        have : Tendsto (fun q : ℝ => (q - 1) ^ (k + 1)) (𝓝 1) (𝓝 ((1 - 1) ^ (k + 1))) :=
          ((continuous_id.sub continuous_const).pow _).tendsto 1
        simpa using this.mono_left nhdsWithin_le_nhds
      exact h0.mul hg'
    rw [zero_mul] at hz
    exact hV (tendsto_nhds_unique hlim (hz.congr' (h1.mono fun q h => h.symm)))

/-- **The same with the corpus's `ℏ_q = 1 − q⁻¹`.** If `ℏ_q² · P(q)/Q(q) → V ≠ 0` as `q → 1`,
then `V ∈ K`. So a finite Hecke chart with `w_μ/w_e ~ Vol(4₁)/ℏ_q²` forces `Vol(4₁) ∈ K`. -/
theorem rational_chart_leading_coeff_hbar {K : Type*} [Field K] [Algebra K ℝ]
    (P Q : K[X]) (hQ : Q ≠ 0) (V : ℝ) (hV : V ≠ 0)
    (hlim : Tendsto (fun q : ℝ => (1 - q⁻¹) ^ 2 * (aeval q P / aeval q Q)) (𝓝[≠] 1)
      (𝓝 V)) :
    ∃ r : K, algebraMap K ℝ r = V := by
  refine rational_chart_leading_coeff P Q hQ V hV ?_
  have hq2 : Tendsto (fun q : ℝ => q ^ 2) (𝓝[≠] 1) (𝓝 1) := by
    have : Tendsto (fun q : ℝ => q ^ 2) (𝓝 1) (𝓝 ((1 : ℝ) ^ 2)) :=
      (continuous_pow 2).tendsto 1
    simpa using this.mono_left nhdsWithin_le_nhds
  have hprod := hq2.mul hlim
  rw [one_mul] at hprod
  refine hprod.congr' ?_
  have hnz : ∀ᶠ q in 𝓝[≠] (1 : ℝ), q ≠ 0 := by
    have : ∀ᶠ q in 𝓝 (1 : ℝ), q ≠ 0 := eventually_ne_nhds one_ne_zero
    exact nhdsWithin_le_nhds this
  filter_upwards [hnz] with q hq
  field_simp

/-! ### 2. The q-volume is the q-log-derivative of the quantum dilogarithm (termwise) -/

/-- **Termwise `G = q ∂_q log P`.** For `q ≠ 0` with `q⁻ⁿ ≠ 1`, the map
`t ↦ −wⁿ/(n(1 − t⁻ⁿ))` (one term of `log ∏ₖ(1 − w t⁻ᵏ)`) has derivative
`wⁿ t⁻ⁿ⁻¹/(1 − t⁻ⁿ)²` at `t = q`; at `w = zq`, `q` times it is `zⁿ/(1 − q⁻ⁿ)²`,
the summand of the q-volume `G(z; q)`. -/
theorem qvolume_term_log_deriv (z q : ℝ) (n : ℕ) (hn : n ≠ 0) (hq : q ≠ 0)
    (hd : 1 - q⁻¹ ^ n ≠ 0) :
    HasDerivAt (fun t : ℝ => -((z * q) ^ n / (n * (1 - t⁻¹ ^ n))))
      ((z * q) ^ n * q⁻¹ ^ (n + 1) / (1 - q⁻¹ ^ n) ^ 2) q ∧
    q * ((z * q) ^ n * q⁻¹ ^ (n + 1) / (1 - q⁻¹ ^ n) ^ 2) =
      z ^ n / (1 - q⁻¹ ^ n) ^ 2 := by
  have hnR : (n : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  constructor
  · -- d/dt (t⁻¹)^n = n (t⁻¹)^(n-1) · (−t⁻²) = −n t⁻¹^(n+1)
    have hinv : HasDerivAt (fun t : ℝ => t⁻¹) (-(q ^ 2)⁻¹) q := hasDerivAt_inv hq
    have hpow : HasDerivAt (fun t : ℝ => t⁻¹ ^ n) (n * q⁻¹ ^ (n - 1) * -(q ^ 2)⁻¹) q :=
      hinv.pow n
    have hden : HasDerivAt (fun t : ℝ => n * (1 - t⁻¹ ^ n))
        (n * (0 - n * q⁻¹ ^ (n - 1) * -(q ^ 2)⁻¹)) q :=
      ((hasDerivAt_const q (1 : ℝ)).sub hpow).const_mul (n : ℝ)
    have hden0 : (n : ℝ) * (1 - q⁻¹ ^ n) ≠ 0 := mul_ne_zero hnR hd
    have hfrac := (hasDerivAt_const q ((z * q) ^ n)).div hden hden0
    have := hfrac.neg
    convert this using 1
    obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    simp only [Nat.add_sub_cancel]
    set x := q⁻¹ with hx
    have hq2 : (q ^ 2)⁻¹ = x ^ 2 := by rw [hx, inv_pow]
    rw [hq2]
    field_simp
    ring
  · obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    rw [mul_pow, inv_pow]
    field_simp
    ring

/-! ### 3. The energy reading fixes the electron at its writhe -/

/-- The convention-D electron trace `τ_e = q³(q⁴+1)/(q²+1)²` (`E0WeightCandidates.tau_electron`). -/
noncomputable def tauE (q : ℝ) : ℝ := q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- **`τ_e(1) = 1/2`, `τ_e'(1) = 3/2`**, so `q ∂_q log τ_e = 3` at `q = 1`: the writhe of
`σ₀σ₁σ₀`. -/
theorem tau_electron_log_deriv_at_one :
    tauE 1 = 1 / 2 ∧ HasDerivAt tauE (3 / 2) 1 ∧ 1 * (3 / 2) / tauE 1 = (3 : ℝ) := by
  have hv : tauE 1 = 1 / 2 := by norm_num [tauE]
  refine ⟨hv, ?_, by rw [hv]; norm_num⟩
  have hnum : HasDerivAt (fun q : ℝ => q ^ 3 * (q ^ 4 + 1))
      (3 * 1 ^ 2 * (1 ^ 4 + 1) + 1 ^ 3 * (4 * 1 ^ 3 + 0)) 1 := by
    have h3 : HasDerivAt (fun q : ℝ => q ^ 3) (3 * 1 ^ 2) 1 := by
      simpa using hasDerivAt_pow 3 (1 : ℝ)
    have h4 : HasDerivAt (fun q : ℝ => q ^ 4 + 1) (4 * 1 ^ 3 + 0) 1 := by
      simpa using (hasDerivAt_pow 4 (1 : ℝ)).add_const 1
    exact h3.mul h4
  have hden : HasDerivAt (fun q : ℝ => (q ^ 2 + 1) ^ 2) (2 * (1 ^ 2 + 1) * (2 * 1 + 0)) 1 := by
    have h2 : HasDerivAt (fun q : ℝ => q ^ 2 + 1) (2 * 1 + 0) 1 := by
      simpa using (hasDerivAt_pow 2 (1 : ℝ)).add_const 1
    have := h2.pow 2
    simpa [mul_comm, mul_assoc, mul_left_comm] using this
  have := hnum.div hden (by norm_num)
  unfold tauE
  convert this using 1
  norm_num

/-- **The energy reading's carrier is `V/w_e(1)`.** If the electron's weight tends to `we ≠ 0`
and `ℏ² w_μ → V`, then `ℏ² w_μ/w_e → V/we`. With the energy reading `we = 3` (writhe). -/
theorem energy_reading_carrier {α : Type*} {l : Filter α} (h wmu we : α → ℝ) (V e : ℝ)
    (he : e ≠ 0) (hwe : Tendsto we l (𝓝 e))
    (hmu : Tendsto (fun x => h x ^ 2 * wmu x) l (𝓝 V)) :
    Tendsto (fun x => h x ^ 2 * wmu x / we x) l (𝓝 (V / e)) :=
  hmu.div hwe he

/-- **The energy reading misses the carrier by the writhe.** With `w_e → 3` and `V ≠ 0`, the
carrier `ℏ² w_μ/w_e` tends to `V/3 ≠ V`. -/
theorem energy_reading_ne_carrier {α : Type*} {l : Filter α} [l.NeBot] (h wmu we : α → ℝ)
    (V : ℝ) (hV : V ≠ 0) (hwe : Tendsto we l (𝓝 3))
    (hmu : Tendsto (fun x => h x ^ 2 * wmu x) l (𝓝 V)) :
    ¬ Tendsto (fun x => h x ^ 2 * wmu x / we x) l (𝓝 V) := by
  intro hc
  have h1 := energy_reading_carrier h wmu we V 3 (by norm_num) hwe hmu
  have := tendsto_nhds_unique h1 hc
  apply hV
  linarith

end QOU.Transcendental.MuonCarrierHeckeObstruction

