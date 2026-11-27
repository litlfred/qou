import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import QOU.FluidDynamics.DECNavierStokes

/-!
# QOU.FluidDynamics.q_ns_alpha_dissipation_bound — the exponent `α` of Part A
# is bounded below by `1` exactly when the energy loss does not vanish

Bean `qou-d2tt` (item 5 of `qou-innq`: the true `α` from the q-NS spectrum).
Owner ruling 2026-11-27: Part A holds its data fixed in the **substrate** layer,
so `q → 1⁺` is a vanishing-viscosity limit `ν_q = (1 − q⁻¹)/2 → 0`.

Part A asks whether `Ω_max(q) ~ (q − 1)^{−α}`. The corpus records two values,
`α = 1` (dissipation closure) and `α = 4/3` (Kolmogorov closure), both heuristic
(`p2-critical-exponent`). This file replaces the dissipation closure by a theorem.
It uses only the energy **equality** `E(T) + 2ν ∫₀ᵀ Ω = E(0)`. That equality is
exact for the semi-discrete q-NS system (`energy_equality` in `DECNavierStokes`),
because the nonlinear term conserves energy. It therefore holds **with** triad
transfer between modes, unlike the per-mode law `modal_inequality` that makes
Part A false (`q_ns_enstrophy_order_parameter`).

## Contents

* `sup_ge_energy_loss` — the mean-value bound
  `sup_{[0,T]} Ω ≥ (E(0) − E(T)) / (2νT)`.
* `sup_ge_energy_loss_nuQ` — at `ν = ν_q`, `sup Ω ≥ δ / ((q − 1) T)` whenever
  the energy loss on `[0, T]` is at least `δ`.
* `alpha_ge_one_of_anomaly` — if the energy loss on a fixed window `[0, T]` stays
  `≥ δ > 0` for every `q ∈ (1, q₀]`, then `(q − 1) · Ω_max(q) ≥ δ / T`, i.e.
  `α ≥ 1`. The dissipation-closure value is the lower edge of what a
  non-vanishing energy loss (a dissipation anomaly) forces.
* `balance_witness` — the hypotheses are consistent: a constant enstrophy with the
  matching energy loss satisfies them, and the bound is attained.

## What this does not show

It does not show that the energy loss stays bounded below as `q → 1⁺`; that is the
dissipation-anomaly question, and it is open. For the linear Stokes family with
`q`-independent data the loss tends to `0`, consistent with Part A failing there.
No upper bound on `α` follows, so the Kolmogorov value `4/3` is neither confirmed
nor excluded. No empirical value enters any proof.
-/

namespace QOU.FluidDynamics.QNsAlphaDissipationBound

open MeasureTheory intervalIntegral

/-- Mean-value bound from the energy equality: if `E(T) + 2ν ∫₀ᵀ Ω = E(0)` and
`Ω ≤ M` on `[0, T]`, then `(E(0) − E(T)) / (2νT) ≤ M`. -/
theorem sup_ge_energy_loss {Ω : ℝ → ℝ} {T ν E₀ E_T M : ℝ} (hT : 0 < T) (hν : 0 < ν)
    (hint : IntervalIntegrable Ω volume 0 T)
    (hbal : E_T + 2 * ν * (∫ t in (0 : ℝ)..T, Ω t) = E₀)
    (hM : ∀ t ∈ Set.Icc (0 : ℝ) T, Ω t ≤ M) :
    (E₀ - E_T) / (2 * ν * T) ≤ M := by
  have hle : (∫ t in (0 : ℝ)..T, Ω t) ≤ ∫ _ in (0 : ℝ)..T, M :=
    integral_mono_on hT.le hint intervalIntegrable_const hM
  rw [intervalIntegral.integral_const, smul_eq_mul, sub_zero] at hle
  rw [div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left hle (by positivity : (0 : ℝ) ≤ 2 * ν)]

/-- `2 ν_q = (q − 1)/q`. -/
theorem two_nuQ (q : ℝ) (hq : q ≠ 0) : 2 * QOU.FluidDynamics.DEC.nuQ q = (q - 1) / q := by
  unfold QOU.FluidDynamics.DEC.nuQ
  field_simp

/-- At the q-NS viscosity `ν_q = (1 − q⁻¹)/2`: an energy loss of at least `δ ≥ 0`
on `[0, T]` forces `sup_{[0,T]} Ω ≥ δ / ((q − 1) T)`. -/
theorem sup_ge_energy_loss_nuQ {Ω : ℝ → ℝ} {q T E₀ E_T M δ : ℝ} (hq : 1 < q) (hT : 0 < T)
    (hint : IntervalIntegrable Ω volume 0 T)
    (hbal : E_T + 2 * QOU.FluidDynamics.DEC.nuQ q *
      (∫ t in (0 : ℝ)..T, Ω t) = E₀)
    (hM : ∀ t ∈ Set.Icc (0 : ℝ) T, Ω t ≤ M) (hδ : 0 ≤ δ) (hloss : δ ≤ E₀ - E_T) :
    δ / ((q - 1) * T) ≤ M := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hq1 : (0 : ℝ) < q - 1 := by linarith
  have hν : 0 < QOU.FluidDynamics.DEC.nuQ q := by
    have := two_nuQ q hq0.ne'
    have h2 : 0 < (q - 1) / q := div_pos hq1 hq0
    linarith
  have key := sup_ge_energy_loss hT hν hint hbal hM
  rw [two_nuQ q hq0.ne'] at key
  have hden : (q - 1) / q * T = (q - 1) * T / q := by ring
  rw [hden, div_div_eq_mul_div] at key
  -- key : (E₀ - E_T) * q / ((q - 1) * T) ≤ M
  have hpos : 0 < (q - 1) * T := by positivity
  calc δ / ((q - 1) * T) ≤ (E₀ - E_T) * q / ((q - 1) * T) := by
        apply div_le_div_of_nonneg_right _ hpos.le
        nlinarith
    _ ≤ M := key

/-- **`α ≥ 1` from a dissipation anomaly.** Suppose that for every `q ∈ (1, q₀]`
a trajectory satisfies the energy equality at `ν_q` on a fixed window `[0, T]`,
loses at least `δ > 0` of energy there, and has enstrophy at most `Ωmax q`. Then
`(q − 1) · Ωmax q ≥ δ / T` on `(1, q₀]`. -/
theorem alpha_ge_one_of_anomaly {q₀ T δ : ℝ} (hT : 0 < T) (hδ : 0 < δ)
    (Ω : ℝ → ℝ → ℝ) (E₀ E_T Ωmax : ℝ → ℝ)
    (hint : ∀ q, 1 < q → q ≤ q₀ → IntervalIntegrable (Ω q) volume 0 T)
    (hbal : ∀ q, 1 < q → q ≤ q₀ → E_T q + 2 * QOU.FluidDynamics.DEC.nuQ q *
      (∫ t in (0 : ℝ)..T, Ω q t) = E₀ q)
    (hloss : ∀ q, 1 < q → q ≤ q₀ → δ ≤ E₀ q - E_T q)
    (hmax : ∀ q, 1 < q → q ≤ q₀ → ∀ t ∈ Set.Icc (0 : ℝ) T, Ω q t ≤ Ωmax q) :
    ∀ q, 1 < q → q ≤ q₀ → δ / T ≤ (q - 1) * Ωmax q := by
  intro q hq hq₀
  have h := sup_ge_energy_loss_nuQ hq hT (hint q hq hq₀) (hbal q hq hq₀) (hmax q hq hq₀)
    hδ.le (hloss q hq hq₀)
  have hq1 : (0 : ℝ) < q - 1 := by linarith
  rw [div_le_iff₀ (by positivity)] at h
  rw [div_le_iff₀ hT]
  nlinarith

/-- Non-vacuity: constant enstrophy `c` with energy loss `2ν c T` satisfies the
energy equality, and the mean-value bound is attained (`M = c`). -/
theorem balance_witness (c ν T E₀ : ℝ) (hT : 0 < T) (hν : 0 < ν) :
    (E₀ - 2 * ν * c * T) + 2 * ν * (∫ _ in (0 : ℝ)..T, c) = E₀ ∧
      (E₀ - (E₀ - 2 * ν * c * T)) / (2 * ν * T) = c := by
  refine ⟨?_, ?_⟩
  · rw [intervalIntegral.integral_const, smul_eq_mul, sub_zero]; ring
  · field_simp; ring

end QOU.FluidDynamics.QNsAlphaDissipationBound
