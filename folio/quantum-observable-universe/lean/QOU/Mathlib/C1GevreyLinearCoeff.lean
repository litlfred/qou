import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# The linear coefficient of the C1 q-Gevrey decay, derived

Bean `qou-z8me` (epic `qou-frzo`). The C1 recurrence of
`computations/qbeta/c3_w2_c1_qborel_singularity.py` is

    [m+2]_q · b_{m+2} = b_{m+1} + b_m,     [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹).

A three-point fit at `m ∈ {600, 700, 800}` gave `−log_q|b_m| ≈ A m² + B m + C`
with `A = 1/4` and `B = 8.00010424`, and the bean asked whether `B` is exactly `8`.

**It is not.** This file proves, for every `q > 1` and every positive solution, that

    −log_q b_m = m²/4 + B·m + o(m),     B = (1 − log_q(q − q⁻¹)) / 2,

so `B` is a function of `q`, not an integer. (At the probe's `q` the closed form
evaluates to `8.0001042395…`, matching the fit; that evaluation is a probe fact and
does not enter any statement here.) The bean's "crude asymptotic gives 7.5" was a
summation slip: the two-step increment is `m + 2 + λ`, `λ = −log_q(q − q⁻¹)`, and
`m²/4 + βm` has increment `m + 1 + 2β`, so `β = (1 + λ)/2`, not `λ/2`.

The statement is proved for a general offset `k` (recurrence `[m+k]_q b_{m+2} = …`),
giving `B_k = (k − 1 − log_q(q − q⁻¹))/2`; `k = 2` is C1. The offset form is what
lets the solutions with `b₀ = 0` or `b₁ = 0` (the corpus's branches `(1,0)`, `(0,1)`)
be handled by shifting two steps, since they are positive from `m = 2` on.

## Proof shape

1. `r_m = b_{m+1}/b_m` satisfies `r_{m+2} ≤ 1/[m+k+1]_q + q⁻¹·r_m`
   (`ratio_two_step_le`), because `[n]_q·q ≤ [n+1]_q`. A two-step contraction with a
   vanishing forcing term gives `r_m → 0` (`tendsto_zero_of_two_step_contraction`).
2. `b_m/b_{m+2} = [m+k]_q/(1 + r_m)` exactly, and
   `log [n]_q − n log q → −log(q − q⁻¹)`, so the two-step log-increment converges
   (`two_step_increment_tendsto`). This is also the parity-free q-Borel radius.
3. The residual `e_m = −log_q b_m − m²/4 − B m` has `e_{m+2} − e_m → 0`, hence
   `e_m/m → 0` (`div_tendsto_zero_of_two_step_diff`).

## Scope

Positive solutions only. Sign-changing real or complex initial data are not covered
here (the two-step chains decouple asymptotically, so the same `B` is expected, but
that is not proved). Nothing here concerns Stokes data: `B` fixes the q-Borel radius
`q^{B + 1/4}`, not the singularity structure.

No empirical input, no fitted constant: `q` is a free parameter `> 1` throughout.
-/

namespace QOU.Mathlib.C1GevreyLinearCoeff

open Filter Topology Real

/-- The symmetric q-integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`, the convention of the
C1 probe's `_q_int`. -/
noncomputable def qInt (q : ℝ) (n : ℕ) : ℝ := (q ^ n - q⁻¹ ^ n) / (q - q⁻¹)

section Basic

variable {q : ℝ}

theorem sub_inv_pos (hq : 1 < q) : 0 < q - q⁻¹ := by
  have h1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

theorem qInt_pos (hq : 1 < q) {n : ℕ} (hn : 1 ≤ n) : 0 < qInt q n := by
  have hn0 : n ≠ 0 := by omega
  have h1 : 1 < q ^ n := one_lt_pow₀ hq hn0
  have hqi0 : 0 ≤ q⁻¹ := inv_nonneg.mpr (by linarith)
  have h2 : q⁻¹ ^ n < 1 := pow_lt_one₀ hqi0 (inv_lt_one_of_one_lt₀ hq) hn0
  exact div_pos (by linarith) (sub_inv_pos hq)

/-- `[n]_q · q ≤ [n+1]_q`: consecutive q-integers grow by at least a factor `q`. -/
theorem qInt_mul_le_succ (hq : 1 < q) (n : ℕ) : qInt q n * q ≤ qInt q (n + 1) := by
  have hh := sub_inv_pos hq
  have hq0 : 0 < q := by linarith
  have hqi : q⁻¹ ≤ q := by
    have := inv_lt_one_of_one_lt₀ hq
    linarith
  have hpow : 0 ≤ q⁻¹ ^ n := pow_nonneg (inv_nonneg.mpr hq0.le) n
  unfold qInt
  rw [div_mul_eq_mul_div, div_le_div_iff_of_pos_right hh]
  have : q⁻¹ ^ (n + 1) ≤ q * q⁻¹ ^ n := by
    rw [pow_succ']
    exact mul_le_mul_of_nonneg_right hqi hpow
  have e1 : (q ^ n - q⁻¹ ^ n) * q = q ^ n * q - q * q⁻¹ ^ n := by ring
  rw [e1, pow_succ q n]
  linarith

/-- `[n]_q = qⁿ·(1 − (q⁻ⁿ)²)/(q − q⁻¹)`. -/
theorem qInt_eq (hq : 1 < q) (n : ℕ) :
    qInt q n = q ^ n * (1 - (q⁻¹ ^ n) ^ 2) / (q - q⁻¹) := by
  have hq0 : q ≠ 0 := by positivity
  have hqn : q ^ n * q⁻¹ ^ n = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq0, one_pow]
  unfold qInt
  congr 1
  have : q ^ n * (q⁻¹ ^ n) ^ 2 = q⁻¹ ^ n := by
    rw [sq, ← mul_assoc, hqn, one_mul]
  rw [mul_sub, mul_one, this]

theorem tendsto_qInt_atTop (hq : 1 < q) : Tendsto (qInt q) atTop atTop := by
  have hh := sub_inv_pos hq
  have hq0 : 0 < q := by linarith
  have hlow : ∀ n : ℕ, (q ^ n - 1) / (q - q⁻¹) ≤ qInt q n := by
    intro n
    unfold qInt
    have : q⁻¹ ^ n ≤ 1 := pow_le_one₀ (inv_nonneg.mpr hq0.le)
      (inv_lt_one_of_one_lt₀ hq).le
    gcongr
  refine tendsto_atTop_mono hlow ?_
  have h1 : Tendsto (fun n : ℕ => q ^ n - 1) atTop atTop :=
    tendsto_atTop_add_const_right _ (-1)
      (by simpa using tendsto_pow_atTop_atTop_of_one_lt hq)
  exact h1.atTop_div_const hh

/-- `log [n]_q − n·log q → −log(q − q⁻¹)`. -/
theorem tendsto_log_qInt_sub (hq : 1 < q) :
    Tendsto (fun n : ℕ => Real.log (qInt q n) - n * Real.log q) atTop
      (𝓝 (-Real.log (q - q⁻¹))) := by
  have hh := sub_inv_pos hq
  have hq0 : 0 < q := by linarith
  have hqi0 : 0 ≤ q⁻¹ := inv_nonneg.mpr hq0.le
  have hqi1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  -- (q⁻ⁿ)² → 0
  have hsmall : Tendsto (fun n : ℕ => (q⁻¹ ^ n) ^ 2) atTop (𝓝 0) := by
    have := (tendsto_pow_atTop_nhds_zero_of_lt_one hqi0 hqi1).pow 2
    simpa using this
  have hlog1 : Tendsto (fun n : ℕ => Real.log (1 - (q⁻¹ ^ n) ^ 2)) atTop (𝓝 0) := by
    have hc : ContinuousAt Real.log (1 - 0) := by
      apply Real.continuousAt_log; norm_num
    have := hc.tendsto.comp (tendsto_const_nhds.sub hsmall)
    simpa using this
  refine (hlog1.sub_const (Real.log (q - q⁻¹))).congr' ?_ |>.trans (by simp)
  · filter_upwards [eventually_ge_atTop 1] with n hn
    have hn0 : n ≠ 0 := by omega
    have hp : (q⁻¹ ^ n) ^ 2 < 1 := by
      have : q⁻¹ ^ n < 1 := pow_lt_one₀ hqi0 hqi1 hn0
      have h0 : 0 ≤ q⁻¹ ^ n := pow_nonneg hqi0 n
      nlinarith
    have hA : 0 < q ^ n := pow_pos hq0 n
    have hB : 0 < 1 - (q⁻¹ ^ n) ^ 2 := by linarith
    rw [qInt_eq hq n, Real.log_div (by positivity) hh.ne', Real.log_mul hA.ne' hB.ne',
      Real.log_pow]
    ring

end Basic

section Sequences

/-- **One-step contraction with vanishing forcing.** If `0 ≤ y`, `y_{k+1} ≤ ε_k + ρ y_k`
with `0 ≤ ρ < 1` and `ε → 0`, then `y → 0`. -/
theorem tendsto_zero_of_contraction {y ε : ℕ → ℝ} {ρ : ℝ}
    (hy0 : ∀ k, 0 ≤ y k) (hε : Tendsto ε atTop (𝓝 0)) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (h : ∀ k, y (k + 1) ≤ ε k + ρ * y k) : Tendsto y atTop (𝓝 0) := by
  rw [Metric.tendsto_atTop]
  intro δ hδ
  have hδ' : 0 < δ * (1 - ρ) / 2 := by
    have : 0 < 1 - ρ := by linarith
    positivity
  obtain ⟨N, hN⟩ := (Metric.tendsto_atTop.mp hε) _ hδ'
  have hclaim : ∀ j : ℕ, y (N + j) ≤ ρ ^ j * y N + δ / 2 := by
    intro j
    induction j with
    | zero => simp; linarith
    | succ j ih =>
      have hεj : ε (N + j) ≤ δ * (1 - ρ) / 2 := by
        have := hN (N + j) (by omega)
        rw [Real.dist_eq, sub_zero] at this
        exact (le_abs_self _).trans this.le
      have := h (N + j)
      rw [show N + (j + 1) = N + j + 1 by omega, pow_succ]
      nlinarith [mul_le_mul_of_nonneg_left ih hρ0]
  have hpow : Tendsto (fun j : ℕ => ρ ^ j * y N) atTop (𝓝 0) := by
    simpa using (tendsto_pow_atTop_nhds_zero_of_lt_one hρ0 hρ1).mul_const (y N)
  obtain ⟨J, hJ⟩ := (Metric.tendsto_atTop.mp hpow) (δ / 2) (by linarith)
  refine ⟨N + J, fun k hk => ?_⟩
  obtain ⟨j, rfl⟩ : ∃ j, k = N + j := ⟨k - N, by omega⟩
  have h1 := hclaim j
  have h2 := hJ j (by omega)
  rw [Real.dist_eq, sub_zero] at h2 ⊢
  rw [abs_of_nonneg (hy0 _)]
  have := (le_abs_self (ρ ^ j * y N)).trans_lt h2
  linarith

/-- **Two-step contraction with vanishing forcing.** If `0 ≤ x`,
`x_{m+2} ≤ ε_m + ρ x_m` with `0 ≤ ρ < 1` and `ε → 0`, then `x → 0`. -/
theorem tendsto_zero_of_two_step_contraction {x ε : ℕ → ℝ} {ρ : ℝ}
    (hx0 : ∀ m, 0 ≤ x m) (hε : Tendsto ε atTop (𝓝 0)) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (h : ∀ m, x (m + 2) ≤ ε m + ρ * x m) : Tendsto x atTop (𝓝 0) := by
  set w : ℕ → ℝ := fun j => max (x (2 * j)) (x (2 * j + 1)) with hw
  set ε' : ℕ → ℝ := fun j => max (ε (2 * j)) (ε (2 * j + 1)) with hε'
  have hε2 : Tendsto ε' atTop (𝓝 0) := by
    have ha : Tendsto (fun j : ℕ => ε (2 * j)) atTop (𝓝 0) :=
      hε.comp (tendsto_atTop_atTop.2 fun c => ⟨c, fun j hj => by omega⟩)
    have hb : Tendsto (fun j : ℕ => ε (2 * j + 1)) atTop (𝓝 0) :=
      hε.comp (tendsto_atTop_atTop.2 fun c => ⟨c, fun j hj => by omega⟩)
    simpa using ha.max hb
  have hw0 : ∀ j, 0 ≤ w j := fun j => le_max_of_le_left (hx0 _)
  have hwstep : ∀ j, w (j + 1) ≤ ε' j + ρ * w j := by
    intro j
    have e1 : 2 * (j + 1) = 2 * j + 2 := by ring
    simp only [hw, hε']
    rw [e1, show 2 * j + 2 + 1 = (2 * j + 1) + 2 by ring]
    apply max_le
    · calc x (2 * j + 2) ≤ ε (2 * j) + ρ * x (2 * j) := h _
        _ ≤ max (ε (2 * j)) (ε (2 * j + 1)) + ρ * max (x (2 * j)) (x (2 * j + 1)) := by
          gcongr
          · exact le_max_left _ _
          · exact le_max_left _ _
    · calc x (2 * j + 1 + 2) ≤ ε (2 * j + 1) + ρ * x (2 * j + 1) := h _
        _ ≤ max (ε (2 * j)) (ε (2 * j + 1)) + ρ * max (x (2 * j)) (x (2 * j + 1)) := by
          gcongr
          · exact le_max_right _ _
          · exact le_max_right _ _
  have hwt : Tendsto w atTop (𝓝 0) :=
    tendsto_zero_of_contraction hw0 hε2 hρ0 hρ1 hwstep
  have hwt2 : Tendsto (fun m : ℕ => w (m / 2)) atTop (𝓝 0) :=
    hwt.comp (Nat.tendsto_div_const_atTop (by norm_num))
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds hwt2 hx0 ?_
  intro m
  simp only [hw]
  rcases Nat.even_or_odd' m with ⟨j, rfl | rfl⟩
  · rw [show 2 * j / 2 = j by omega]; exact le_max_left _ _
  · rw [show (2 * j + 1) / 2 = j by omega]; exact le_max_right _ _

/-- **Two-step differences vanishing ⇒ sublinear.** If `u_{m+2} − u_m → 0` then
`u_m / m → 0`. -/
theorem div_tendsto_zero_of_two_step_diff {u : ℕ → ℝ}
    (h : Tendsto (fun m => u (m + 2) - u m) atTop (𝓝 0)) :
    Tendsto (fun m : ℕ => u m / m) atTop (𝓝 0) := by
  rw [Metric.tendsto_atTop]
  intro δ hδ
  obtain ⟨N, hN⟩ := (Metric.tendsto_atTop.mp h) (δ / 2) (by linarith)
  set M : ℝ := max |u N| |u (N + 1)| with hM
  have hM0 : 0 ≤ M := le_max_of_le_left (abs_nonneg _)
  have hclaim : ∀ m, N ≤ m → |u m| ≤ M + (m : ℝ) * (δ / 2) := by
    intro m
    induction m using Nat.strong_induction_on with
    | _ m ih =>
      intro hm
      have hδ2 : 0 ≤ (m : ℝ) * (δ / 2) := by positivity
      rcases Nat.lt_or_ge m (N + 2) with hlt | hge
      · have : m = N ∨ m = N + 1 := by omega
        rcases this with rfl | rfl
        · have := le_max_left |u m| |u (m + 1)|; linarith
        · have := le_max_right |u N| |u (N + 1)|; linarith
      · obtain ⟨p, rfl⟩ : ∃ p, m = p + 2 := ⟨m - 2, by omega⟩
        have hp := ih p (by omega) (by omega)
        have hd := hN p (by omega)
        rw [Real.dist_eq, sub_zero] at hd
        have htri : |u (p + 2)| ≤ |u p| + |u (p + 2) - u p| := by
          have := abs_add_le (u p) (u (p + 2) - u p)
          simpa using this
        push_cast
        nlinarith
  -- eventually `M / m < δ/2`
  have hMm : Tendsto (fun m : ℕ => M / (m : ℝ)) atTop (𝓝 0) :=
    tendsto_const_nhds.div_atTop tendsto_natCast_atTop_atTop
  obtain ⟨K, hK⟩ := (Metric.tendsto_atTop.mp hMm) (δ / 2) (by linarith)
  refine ⟨max (max N K) 1, fun m hm => ?_⟩
  have hmN : N ≤ m := le_trans (le_trans (le_max_left _ _) (le_max_left _ _)) hm
  have hmK : K ≤ m := le_trans (le_trans (le_max_right _ _) (le_max_left _ _)) hm
  have hm1 : 1 ≤ m := le_trans (le_max_right _ _) hm
  have hmpos : (0 : ℝ) < m := by exact_mod_cast hm1
  have h1 := hclaim m hmN
  have h2 := hK m hmK
  rw [Real.dist_eq, sub_zero, abs_of_nonneg (by positivity)] at h2
  rw [Real.dist_eq, sub_zero, abs_div, abs_of_pos hmpos, div_lt_iff₀ hmpos]
  rw [div_lt_iff₀ hmpos] at h2
  nlinarith

end Sequences

section C1

variable {q : ℝ} {k : ℕ} {b : ℕ → ℝ}

/-- The C1-type recurrence with offset `k`: `[m+k]_q · b_{m+2} = b_{m+1} + b_m`.
C1 is `k = 2`. -/
def IsC1Solution (q : ℝ) (k : ℕ) (b : ℕ → ℝ) : Prop :=
  ∀ m, qInt q (m + k) * b (m + 2) = b (m + 1) + b m

/-- Step 1 of the proof: `r_{m+2} ≤ 1/[m+k+1]_q + q⁻¹ r_m` for `r_m = b_{m+1}/b_m`. -/
theorem ratio_two_step_le (hq : 1 < q) (hk : 1 ≤ k) (hb : ∀ m, 0 < b m)
    (hrec : IsC1Solution q k b) (m : ℕ) :
    b (m + 3) / b (m + 2) ≤ 1 / qInt q (m + k + 1) + q⁻¹ * (b (m + 1) / b m) := by
  have hq0 : 0 < q := by linarith
  set Q := qInt q (m + k) with hQ
  set Q' := qInt q (m + k + 1) with hQ'
  have hQp : 0 < Q := qInt_pos hq (by omega)
  have hQ'p : 0 < Q' := qInt_pos hq (by omega)
  have hQQ : Q * q ≤ Q' := qInt_mul_le_succ hq (m + k)
  have h0 := hrec m
  have h1 := hrec (m + 1)
  rw [show m + 1 + k = m + k + 1 by omega, show m + 1 + 2 = m + 3 by omega,
    show m + 1 + 1 = m + 2 by omega] at h1
  have hb0 := hb m; have hb1 := hb (m + 1); have hb2 := hb (m + 2); have hb3 := hb (m + 3)
  -- b_{m+3} = (b_{m+2} + b_{m+1}) / Q'
  have e3 : b (m + 3) = (b (m + 2) + b (m + 1)) / Q' := by
    field_simp; linarith
  -- b_{m+1}/b_{m+2} ≤ Q · b_{m+1}/b_m, from Q b_{m+2} ≥ b_m
  have hkey : b (m + 1) / b (m + 2) ≤ Q * (b (m + 1) / b m) := by
    rw [div_le_iff₀ hb2]
    have : b m ≤ Q * b (m + 2) := by linarith
    calc b (m + 1) = b (m + 1) / b m * b m := by field_simp
      _ ≤ b (m + 1) / b m * (Q * b (m + 2)) := by
          gcongr
      _ = Q * (b (m + 1) / b m) * b (m + 2) := by ring
  have hr0 : 0 ≤ b (m + 1) / b m := by positivity
  have hcoef : Q / Q' ≤ q⁻¹ := by
    rw [div_le_iff₀ hQ'p]
    calc Q = q⁻¹ * (Q * q) := by field_simp
      _ ≤ q⁻¹ * Q' := by gcongr
  calc b (m + 3) / b (m + 2) = (1 + b (m + 1) / b (m + 2)) / Q' := by
        rw [e3]; field_simp
    _ ≤ (1 + Q * (b (m + 1) / b m)) / Q' := by gcongr
    _ = 1 / Q' + Q / Q' * (b (m + 1) / b m) := by ring
    _ ≤ 1 / Q' + q⁻¹ * (b (m + 1) / b m) := by gcongr

/-- **The consecutive ratio of a positive C1 solution tends to `0`.** -/
theorem tendsto_ratio_zero (hq : 1 < q) (hk : 1 ≤ k) (hb : ∀ m, 0 < b m)
    (hrec : IsC1Solution q k b) :
    Tendsto (fun m => b (m + 1) / b m) atTop (𝓝 0) := by
  have hq0 : 0 < q := by linarith
  have hε : Tendsto (fun m : ℕ => 1 / qInt q (m + k + 1)) atTop (𝓝 0) := by
    have := (tendsto_qInt_atTop hq).comp (tendsto_add_atTop_nat (k + 1))
    simpa [Function.comp, add_assoc] using this.inv_tendsto_atTop
  refine tendsto_zero_of_two_step_contraction (ρ := q⁻¹)
    (fun m => (div_pos (hb _) (hb _)).le) hε (inv_nonneg.mpr hq0.le)
    (inv_lt_one_of_one_lt₀ hq) ?_
  intro m
  have := ratio_two_step_le hq hk hb hrec m
  simpa [show m + 2 + 1 = m + 3 by omega] using this

/-- **Two-step log-increment (= the parity-free q-Borel radius).**
`log_q b_m − log_q b_{m+2} − (m + k) → −log_q(q − q⁻¹)`. -/
theorem two_step_increment_tendsto (hq : 1 < q) (hk : 1 ≤ k) (hb : ∀ m, 0 < b m)
    (hrec : IsC1Solution q k b) :
    Tendsto (fun m : ℕ => logb q (b m) - logb q (b (m + 2)) - ((m : ℝ) + k)) atTop
      (𝓝 (-logb q (q - q⁻¹))) := by
  have hlq : 0 < Real.log q := Real.log_pos hq
  have hr := tendsto_ratio_zero hq hk hb hrec
  have hlog1 : Tendsto (fun m => Real.log (1 + b (m + 1) / b m)) atTop (𝓝 0) := by
    have hc : ContinuousAt Real.log (1 + 0) := by
      apply Real.continuousAt_log; norm_num
    simpa using hc.tendsto.comp (tendsto_const_nhds.add hr)
  have hQ := (tendsto_log_qInt_sub hq).comp (tendsto_add_atTop_nat k)
  have hsum : Tendsto (fun m : ℕ =>
      ((Real.log (qInt q (m + k)) - ((m + k : ℕ) : ℝ) * Real.log q)
        - Real.log (1 + b (m + 1) / b m)) / Real.log q) atTop
      (𝓝 ((-Real.log (q - q⁻¹) - 0) / Real.log q)) :=
    (hQ.sub hlog1).div_const _
  have hlim : (-Real.log (q - q⁻¹) - 0) / Real.log q = -logb q (q - q⁻¹) := by
    unfold logb; ring
  rw [hlim] at hsum
  refine hsum.congr' ?_
  filter_upwards with m
  have hQp : 0 < qInt q (m + k) := qInt_pos hq (by omega)
  have hb0 := hb m; have hb1 := hb (m + 1); have hb2 := hb (m + 2)
  -- b_{m+2} = b_m (1 + r_m) / [m+k]_q
  have hrel : b (m + 2) = b m * (1 + b (m + 1) / b m) / qInt q (m + k) := by
    have := hrec m
    field_simp
    linarith
  have h1r : 0 < 1 + b (m + 1) / b m := by positivity
  rw [hrel]
  unfold logb
  rw [Real.log_div (by positivity) hQp.ne', Real.log_mul hb0.ne' h1r.ne']
  field_simp
  push_cast
  ring

/-- **The derived linear coefficient** `B_k = (k − 1 − log_q(q − q⁻¹))/2`. -/
noncomputable def linCoeff (q : ℝ) (k : ℕ) : ℝ := ((k : ℝ) - 1 - logb q (q - q⁻¹)) / 2

/-- **Main theorem (bean `qou-z8me`).** For `q > 1` and any positive solution of
`[m+k]_q b_{m+2} = b_{m+1} + b_m` (`k ≥ 1`),

    (−log_q b_m − m²/4) / m  →  (k − 1 − log_q(q − q⁻¹)) / 2.

For C1 (`k = 2`) the linear coefficient is `B = (1 − log_q(q − q⁻¹))/2`: a function
of `q`, not the integer `8`. -/
theorem linear_coeff_tendsto (hq : 1 < q) (hk : 1 ≤ k) (hb : ∀ m, 0 < b m)
    (hrec : IsC1Solution q k b) :
    Tendsto (fun m : ℕ => (-logb q (b m) - (m : ℝ) ^ 2 / 4) / m) atTop
      (𝓝 (linCoeff q k)) := by
  set B := linCoeff q k with hB
  set e : ℕ → ℝ := fun m => -logb q (b m) - (m : ℝ) ^ 2 / 4 - B * m with he
  have hinc := two_step_increment_tendsto hq hk hb hrec
  have hediff : Tendsto (fun m => e (m + 2) - e m) atTop (𝓝 0) := by
    have := hinc.add_const (logb q (q - q⁻¹))
    rw [neg_add_cancel] at this
    refine this.congr' ?_
    filter_upwards with m
    simp only [he, hB, linCoeff]
    push_cast
    ring
  have hediv := div_tendsto_zero_of_two_step_diff hediff
  have := hediv.const_add B
  rw [add_zero] at this
  refine this.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with m hm
  have hm0 : (m : ℝ) ≠ 0 := by
    have : (0 : ℝ) < m := by exact_mod_cast hm
    exact this.ne'
  simp only [he]
  field_simp
  ring

/-- **The C1 case** (`k = 2`): `B = (1 − log_q(q − q⁻¹))/2`. -/
theorem c1_linear_coeff (hq : 1 < q) (hb : ∀ m, 0 < b m) (hrec : IsC1Solution q 2 b) :
    Tendsto (fun m : ℕ => (-logb q (b m) - (m : ℝ) ^ 2 / 4) / m) atTop
      (𝓝 ((1 - logb q (q - q⁻¹)) / 2)) := by
  have := linear_coeff_tendsto hq (by norm_num) hb hrec
  have e : linCoeff q 2 = (1 - logb q (q - q⁻¹)) / 2 := by
    unfold linCoeff; norm_num
  rwa [e] at this

/-- **The quadratic coefficient is `1/4`** (q-Gevrey order `½` in the corpus's
`2·log_q|b_m|/m² → −½` normalisation), as a corollary. -/
theorem quad_coeff_tendsto (hq : 1 < q) (hk : 1 ≤ k) (hb : ∀ m, 0 < b m)
    (hrec : IsC1Solution q k b) :
    Tendsto (fun m : ℕ => -logb q (b m) / (m : ℝ) ^ 2) atTop (𝓝 (1 / 4)) := by
  have hl := linear_coeff_tendsto hq hk hb hrec
  have hinv : Tendsto (fun m : ℕ => (m : ℝ)⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp tendsto_natCast_atTop_atTop
  have := (hl.mul hinv).const_add (1 / 4)
  rw [mul_zero, add_zero] at this
  refine this.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with m hm
  have hm0 : (m : ℝ) ≠ 0 := by
    have : (0 : ℝ) < m := by exact_mod_cast hm
    exact this.ne'
  field_simp
  ring

/-- **Shift.** If `b` solves the offset-`k` recurrence then `m ↦ b (m+2)` solves the
offset-`(k+2)` one. Used to reach the branches with `b₀ = 0` or `b₁ = 0`. -/
theorem IsC1Solution.shift (hrec : IsC1Solution q k b) :
    IsC1Solution q (k + 2) (fun m => b (m + 2)) := by
  intro m
  have := hrec (m + 2)
  simpa [show m + 2 + k = m + (k + 2) by omega, add_assoc] using this

/-- **Initial data with `b₁ ≥ 0` and `b₀ + b₁ > 0` give a solution positive from
`m = 2`** (offset `k ≥ 1`). This covers the corpus branches `(1,0)`, `(0,1)`, `(1,1)`;
`b₀` itself may be negative. -/
theorem pos_of_nonneg_init (hq : 1 < q) (hk : 1 ≤ k) (hrec : IsC1Solution q k b)
    (h1 : 0 ≤ b 1) (h01 : 0 < b 0 + b 1) : ∀ m, 0 < b (m + 2) := by
  have hdiv : ∀ m, b (m + 2) = (b (m + 1) + b m) / qInt q (m + k) := by
    intro m
    have hQ := qInt_pos hq (n := m + k) (by omega)
    have := hrec m
    field_simp
    linarith
  -- b_2 > 0 and b_3 > 0, then induct
  have hb2 : 0 < b 2 := by
    rw [hdiv 0]; exact div_pos (by simpa [add_comm] using h01) (qInt_pos hq (by omega))
  have hb3 : 0 < b 3 := by
    rw [hdiv 1]; exact div_pos (by linarith) (qInt_pos hq (by omega))
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    rcases m with _ | _ | m
    · exact hb2
    · exact hb3
    · rw [hdiv (m + 2)]
      have := ih m (by omega)
      have := ih (m + 1) (by omega)
      exact div_pos (by simpa [add_assoc] using add_pos ‹0 < b (m + 1 + 2)› ‹0 < b (m + 2)›)
        (qInt_pos hq (by omega))

/-- **C1 with `b₁ ≥ 0`, `b₀ + b₁ > 0`** (covers the three corpus branches): the linear
coefficient of `−log_q b_m − m²/4` is `B = (1 − log_q(q − q⁻¹))/2`. -/
theorem c1_linear_coeff_of_nonneg_init (hq : 1 < q) (hrec : IsC1Solution q 2 b)
    (h1 : 0 ≤ b 1) (h01 : 0 < b 0 + b 1) :
    Tendsto (fun m : ℕ => (-logb q (b m) - (m : ℝ) ^ 2 / 4) / m) atTop
      (𝓝 ((1 - logb q (q - q⁻¹)) / 2)) := by
  have hpos := pos_of_nonneg_init hq (by norm_num) hrec h1 h01
  have hs := linear_coeff_tendsto hq (by norm_num) hpos hrec.shift
  -- shifted: (−L(m+2) − m²/4)/m → B + 2/2 ... rewrite to the unshifted sequence
  -- (−L(m+2) − (m+2)²/4)/(m+2) = [(−L(m+2) − m²/4)/m − (m+1)/m] · m/(m+2)
  have hB4 : linCoeff q (2 + 2) = (1 - logb q (q - q⁻¹)) / 2 + 1 := by
    unfold linCoeff; push_cast; ring
  rw [hB4] at hs
  have hfrac : Tendsto (fun m : ℕ => ((m : ℝ) + 1) / m) atTop (𝓝 1) := by
    have : Tendsto (fun m : ℕ => 1 + (m : ℝ)⁻¹) atTop (𝓝 (1 + 0)) :=
      tendsto_const_nhds.add (tendsto_inv_atTop_zero.comp tendsto_natCast_atTop_atTop)
    rw [add_zero] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with m hm
    have : (m : ℝ) ≠ 0 := by have : (0 : ℝ) < m := by exact_mod_cast hm
                             exact this.ne'
    field_simp
  have hratio : Tendsto (fun m : ℕ => (m : ℝ) / ((m : ℝ) + 2)) atTop (𝓝 1) := by
    have : Tendsto (fun m : ℕ => 1 - 2 / ((m : ℝ) + 2)) atTop (𝓝 (1 - 0)) := by
      refine tendsto_const_nhds.sub ?_
      exact tendsto_const_nhds.div_atTop
        (tendsto_atTop_add_const_right _ 2 tendsto_natCast_atTop_atTop)
    rw [sub_zero] at this
    refine this.congr' ?_
    filter_upwards with m
    have : (m : ℝ) + 2 ≠ 0 := by positivity
    field_simp
    ring
  have hcomb := ((hs.sub hfrac).mul hratio)
  rw [show ((1 - logb q (q - q⁻¹)) / 2 + 1 - 1) * 1 = (1 - logb q (q - q⁻¹)) / 2 by ring]
    at hcomb
  -- hcomb is a statement about index m, value at m+2; transport along m ↦ m + 2
  refine (tendsto_add_atTop_iff_nat
    (f := fun m : ℕ => (-logb q (b m) - (m : ℝ) ^ 2 / 4) / m) 2).mp (hcomb.congr' ?_)
  · filter_upwards [eventually_ge_atTop 1] with m hm
    have hm0 : (m : ℝ) ≠ 0 := by
      have : (0 : ℝ) < m := by exact_mod_cast hm
      exact this.ne'
    have hm2 : (m : ℝ) + 2 ≠ 0 := by positivity
    push_cast
    field_simp
    ring

end C1

end QOU.Mathlib.C1GevreyLinearCoeff
