/-
  Whitehead VC — the saddle-VALUE identity (Clausen), toward discharging the
  `hsaddle` input of `whitehead_vc_of_saddle_value` (bean qou-dw20 / qou-t2sc).

  The saddle sits at `(t*, x*) = (1/2, 1/4)` (validated numerically in
  `computations/whitehead_saddle.py`).  The continuum saddle value is the
  integral

    V = 2π ∫_0^{1/2} [ log 2 + 2 log sin(π(u+1/4)) − log sin(π u) ] du.

  This file proves, sorry-free using `QOU.Knot.Clausen`, that

    V = 4 · clausen(π/2)   ( = 4G = Vol(Whitehead) ),

  the analytic VALUE half of `hsaddle`.  The Riemann-sum → V convergence (the
  other half, via `integral_le_sum_log_sin` / `sum_log_sin_le_integral`) is the
  remaining brick.

  Archimedean (ℝ).  -- Ref: [vanderveen2008] arXiv:math/0611181
-/

/-
**CROSS-REFERENCE (2026-08-19) — a second Whitehead-link VC program exists.**

`QOU/Knot/WhiteheadLinkScaffold.lean` + `QOU/Knot/WhiteheadMajorantRate.lean`
(epic `qou-u1b5`) attack the same theorem from the OPPOSITE end, via the
phase/majorant route:

* this program has the MAGNITUDE — `whitehead_vc_innerSum_half`, sorry-free;
* that one has the PHASES — `‖J_N(W)‖ ≤ majorant`,
  `tendsto_log_whiteheadLinkMajorant_vol` (`→ 4G`), and the residue isolated as
  the conditional class `VdVWhiteheadLemma4` (open: no instance in the corpus).

The gap between the two ends — non-cancellation of the phased outer sum
`Σ_n (2n+1)·χ_{N,n}^{-1}·(Σ_k S_{n,k})` — is exactly what `VdVWhiteheadLemma4`
states. Discharging it is what would join the two halves into the VC for
`J_N(W)` proper. COMPLEMENTARY, not redundant; coordinate before extending.
Audit: `docs/audits/2026-08-19-volume-conjecture-work-overlap-sweep.md`.
-/

import QOU.Knot.Clausen
import QOU.Knot.WhiteheadVolumeConjecture

namespace QOU.Knot.WhiteheadSaddle

open Real
open scoped Real

/-- π-scaled `log(2 sin)` integral: `∫_0^b log(2 sin(π u)) du = -clausen(2πb)/(2π)`
    (substitution `w = π u` in `QOU.Knot.integral_log_two_sin`). -/
theorem integral_log_two_sin_pi (b : ℝ) :
    (∫ u in (0:ℝ)..b, Real.log (2 * Real.sin (π * u)))
      = -QOU.Knot.clausen (2 * (π * b)) / (2 * π) := by
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  rw [intervalIntegral.integral_comp_mul_left (fun w => Real.log (2 * Real.sin w)) hπ,
      mul_zero, QOU.Knot.integral_log_two_sin (π * b), smul_eq_mul]
  field_simp

/-- **Per-term reduction (convergence brick, qou-1gkf).**  Each van der Veen
    kernel factor `2 sin²a / sin b` has log equal to the reduced saddle-integrand
    term `2 log(2 sin a) − log(2 sin b)` (the `log 2` bookkeeping that makes the
    discrete Riemann sum match `saddle_integral`).  Needs `sin a, sin b > 0`
    (holds on the summation range `(k+j)π/N, jπ/N ∈ (0, π)`). -/
theorem log_factor_reduce {a b : ℝ} (ha : 0 < Real.sin a) (hb : 0 < Real.sin b) :
    Real.log (2 * Real.sin a ^ 2 / Real.sin b)
      = 2 * Real.log (2 * Real.sin a) - Real.log (2 * Real.sin b) := by
  have h2 : (2 : ℝ) ≠ 0 := by norm_num
  rw [Real.log_div (by positivity) (ne_of_gt hb),
      Real.log_mul h2 (pow_ne_zero 2 (ne_of_gt ha)), Real.log_pow,
      Real.log_mul h2 (ne_of_gt ha), Real.log_mul h2 (ne_of_gt hb)]
  push_cast
  ring

/-- `log(2 sin(π·))` is interval-integrable (scale `QOU.Knot.intervalIntegrable_log_two_sin`). -/
theorem intervalIntegrable_log_two_sin_pi (a b : ℝ) :
    IntervalIntegrable (fun u => Real.log (2 * Real.sin (π * u))) MeasureTheory.volume a b := by
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  have h := (QOU.Knot.intervalIntegrable_log_two_sin (π * a) (π * b)).comp_mul_left (c := π)
  rwa [mul_div_cancel_left₀ a hπ, mul_div_cancel_left₀ b hπ] at h

/-- `clausen(3π/2) = −clausen(π/2)` (via the `clausen↔Cl_2` bridge + `Cl_2_two_pi_sub`). -/
theorem clausen_three_pi_div_two :
    QOU.Knot.clausen (3 * π / 2) = -QOU.Knot.clausen (π / 2) := by
  have hpi := Real.pi_pos
  have h1 : (3 * π / 2) ∈ Set.Ioo (0:ℝ) (2 * π) := ⟨by linarith, by linarith⟩
  have h2 : (π / 2) ∈ Set.Ioo (0:ℝ) (2 * π) := ⟨by linarith, by linarith⟩
  rw [QOU.Knot.clausen_eq_series h1, QOU.Knot.clausen_eq_series h2,
      show 3 * π / 2 = 2 * π - π / 2 by ring, QOU.Knot.Cl_2_two_pi_sub]

/-- The `−log(2 sin(π u))` piece: `∫_0^{1/2} log(2 sin(π u)) du = 0`
    (`= −clausen(π)/(2π)` and `clausen π = 0`). -/
theorem integral_B_zero :
    (∫ u in (0:ℝ)..(1/2:ℝ), Real.log (2 * Real.sin (π * u))) = 0 := by
  rw [integral_log_two_sin_pi (1/2), show 2 * (π * (1/2:ℝ)) = π by ring,
      QOU.Knot.clausen_pi]
  simp

/-- The shifted `log(2 sin(π(u+¼)))` piece: `∫_0^{1/2} = clausen(π/2)/π`
    (shift to `[¼,¾]`, split, `integral_log_two_sin_pi` at `¾,¼`, antisymmetry). -/
theorem integral_A :
    (∫ u in (0:ℝ)..(1/2:ℝ), Real.log (2 * Real.sin (π * (u + 1/4))))
      = QOU.Knot.clausen (π / 2) / π := by
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  rw [intervalIntegral.integral_comp_add_right
        (fun v => Real.log (2 * Real.sin (π * v))) (1/4),
      show (0:ℝ) + 1/4 = 1/4 by norm_num, show (1/2:ℝ) + 1/4 = 3/4 by norm_num]
  have hadj := intervalIntegral.integral_add_adjacent_intervals
    (intervalIntegrable_log_two_sin_pi 0 (1/4))
    (intervalIntegrable_log_two_sin_pi (1/4) (3/4))
  have hsplit : (∫ v in (1/4:ℝ)..(3/4:ℝ), Real.log (2 * Real.sin (π * v)))
      = (∫ v in (0:ℝ)..(3/4:ℝ), Real.log (2 * Real.sin (π * v)))
        - (∫ v in (0:ℝ)..(1/4:ℝ), Real.log (2 * Real.sin (π * v))) := by linarith
  rw [hsplit, integral_log_two_sin_pi (3/4), integral_log_two_sin_pi (1/4),
      show 2 * (π * (3/4:ℝ)) = 3 * π / 2 by ring,
      show 2 * (π * (1/4:ℝ)) = π / 2 by ring, clausen_three_pi_div_two]
  field_simp
  ring

/-- **Saddle VALUE identity (sorry-free).**  The (log2-reduced) saddle integrand
    integrates to `2·clausen(π/2)/π`, so `2π ×` it `= 4·clausen(π/2) = 4G` — the
    value half of `hsaddle`. -/
theorem saddle_integral :
    (∫ u in (0:ℝ)..(1/2:ℝ),
        (2 * Real.log (2 * Real.sin (π * (u + 1/4)))
          - Real.log (2 * Real.sin (π * u))))
      = 2 * QOU.Knot.clausen (π / 2) / π := by
  have hIntA : IntervalIntegrable
      (fun u => Real.log (2 * Real.sin (π * (u + 1/4)))) MeasureTheory.volume 0 (1/2) := by
    have h := (intervalIntegrable_log_two_sin_pi (1/4) (3/4)).comp_add_right (1/4)
    rw [show (1/4:ℝ) - 1/4 = 0 by norm_num, show (3/4:ℝ) - 1/4 = 1/2 by norm_num] at h
    exact h
  rw [intervalIntegral.integral_sub (hIntA.const_mul 2) (intervalIntegrable_log_two_sin_pi 0 (1/2)),
      intervalIntegral.integral_const_mul, integral_A, integral_B_zero]
  ring

/-- `sin((2k+1)·(π/2)) = (-1)^k` (induction; each step adds `π`, `sin_add_pi`). -/
theorem sin_two_mul_add_one_mul_pi_div_two (k : ℕ) :
    Real.sin ((2 * (k : ℝ) + 1) * (π / 2)) = (-1 : ℝ) ^ k := by
  induction k with
  | zero =>
    simp only [Nat.cast_zero, mul_zero, zero_add, one_mul, Real.sin_pi_div_two, pow_zero]
  | succ m ih =>
    have hstep : (2 * ((m : ℝ) + 1) + 1) * (π / 2)
        = (2 * (m : ℝ) + 1) * (π / 2) + π := by ring
    push_cast
    rw [hstep, Real.sin_add_pi, ih]
    ring

/-- The odd-indexed `Cl_2`-series term (series index `j = 2k+1`) has vanishing
    sine: `sin(((2k+1)+1)·(π/2)) = sin((k+1)π) = 0`. These are the terms dropped
    by the even/odd split in `catalanG_eq_clausen_pi_div_two`. -/
theorem sin_odd_index_vanish (k : ℕ) :
    Real.sin (((2 * (k : ℝ) + 1) + 1) * (π / 2)) = 0 := by
  have h : ((2 * (k : ℝ) + 1) + 1) * (π / 2) = ((k + 1 : ℕ) : ℝ) * π := by
    push_cast; ring
  rw [h, Real.sin_nat_mul_pi]

/-- **catalan bridge (convergence prerequisite, qou-kvvu).**  Catalan's constant
    `G = Σ (-1)ⁿ/(2n+1)²` equals `clausen(π/2)`: the even/odd split of the `Cl_2`
    series drops the even-index (`sin(mπ)=0`) terms and reindexes the odd-index
    terms `sin((2k+1)π/2) = (-1)ᵏ`.  Connects the conditional-VC constant
    `4·catalanG` (`whitehead_vc_of_saddle_value`) to the Clausen value
    `4·clausen(π/2)` produced by `saddle_integral`. -/
theorem catalanG_eq_clausen_pi_div_two :
    QOU.Knot.WhiteheadVC.catalanG = QOU.Knot.clausen (π / 2) := by
  have hpi := Real.pi_pos
  -- majorant: `Σ 1/(k+1)²` (the Clausen `continuous_Cl_2` pattern).
  have hmaj : Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
    have h : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      summable_one_div_nat_pow.mpr (by norm_num)
    exact ((summable_nat_add_iff 1).2 h).congr (fun n => by push_cast; ring)
  set g : ℕ → ℝ := fun j => Real.sin (((j : ℝ) + 1) * (π / 2)) / ((j : ℝ) + 1) ^ 2
    with hgdef
  -- termwise reindexing of the even/odd halves
  have heven_eq : ∀ k : ℕ, g (2 * k) = (-1 : ℝ) ^ k / (2 * (k : ℝ) + 1) ^ 2 := by
    intro k
    simp only [hgdef]
    rw [show (((2 * k : ℕ)) : ℝ) + 1 = 2 * (k : ℝ) + 1 by push_cast; ring,
        sin_two_mul_add_one_mul_pi_div_two]
  have hodd_eq : ∀ k : ℕ, g (2 * k + 1) = 0 := by
    intro k
    simp only [hgdef]
    rw [show (((2 * k + 1 : ℕ)) : ℝ) + 1 = (2 * (k : ℝ) + 1) + 1 by push_cast; ring,
        sin_odd_index_vanish, zero_div]
  -- summability of the alternating even half (Catalan) by norm comparison
  have hCat : Summable (fun k : ℕ => (-1 : ℝ) ^ k / (2 * (k : ℝ) + 1) ^ 2) := by
    refine hmaj.of_norm_bounded (fun k => ?_)
    have hk : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
    rw [Real.norm_eq_abs, abs_div, abs_pow, abs_neg, abs_one, one_pow,
        abs_of_pos (by positivity : (0 : ℝ) < (2 * (k : ℝ) + 1) ^ 2)]
    exact one_div_le_one_div_of_le (by positivity) (by nlinarith [hk])
  have heven : Summable (fun k : ℕ => g (2 * k)) :=
    hCat.congr (fun k => (heven_eq k).symm)
  have hodd : Summable (fun k : ℕ => g (2 * k + 1)) :=
    summable_zero.congr (fun k => (hodd_eq k).symm)
  have hcombine := tsum_even_add_odd heven hodd
  have hoddsum : (∑' k : ℕ, g (2 * k + 1)) = 0 := by
    rw [tsum_congr hodd_eq, tsum_zero]
  have hevensum : (∑' k : ℕ, g (2 * k)) = QOU.Knot.WhiteheadVC.catalanG := by
    unfold QOU.Knot.WhiteheadVC.catalanG
    exact tsum_congr heven_eq
  have hCl : QOU.Archimedean.Cl_2 (π / 2) = ∑' k : ℕ, g k := by
    simp only [hgdef, QOU.Archimedean.Cl_2]
  rw [QOU.Knot.clausen_eq_series (θ := π / 2) ⟨by linarith, by linarith⟩,
      hCl, ← hcombine, hevensum, hoddsum, add_zero]

/-! ### Convergence bricks (qou-1gkf) — discharge `hsaddle` = the saddle-term limit. -/

/-- Grid Clausen-primitive `S'(N,K) = (π/N)·Σ_{j=1}^K log(2 sin(jπ/N))` — the
    object `QOU.Knot.abs_deviation_le` bounds by `−clausen(2Kπ/N)/2`. -/
noncomputable def gridPrim (N K : ℕ) : ℝ :=
  (π / N) * ∑ j ∈ Finset.Icc 1 K, Real.log (2 * Real.sin ((j : ℝ) * (π / N)))

/-- **Reindex/telescope brick.** The shifted grid sum equals a gridPrim
    difference: `(π/N)·Σ_{j=1}^n log(2 sin((k+j)π/N)) = S'(k+n) − S'(k)`. -/
theorem gridPrim_shift {N n k : ℕ} :
    (π / N) * ∑ j ∈ Finset.Icc 1 n,
        Real.log (2 * Real.sin (((k : ℝ) + (j : ℝ)) * (π / N)))
      = gridPrim N (k + n) - gridPrim N k := by
  set g : ℕ → ℝ := fun m => Real.log (2 * Real.sin ((m : ℝ) * (π / N))) with hg
  -- reindex m = k + j
  have hreindex : ∑ j ∈ Finset.Icc 1 n,
        Real.log (2 * Real.sin (((k : ℝ) + (j : ℝ)) * (π / N)))
      = ∑ m ∈ Finset.Icc (k + 1) (k + n), g m := by
    rw [← Finset.map_add_left_Icc 1 n k, Finset.sum_map]
    refine Finset.sum_congr rfl (fun j _ => ?_)
    simp only [addLeftEmbedding_apply, hg]
    push_cast; ring_nf
  -- telescope Icc (k+1) (k+n) = Icc 1 (k+n) \ Icc 1 k
  have htel : ∑ m ∈ Finset.Icc (k + 1) (k + n), g m
      = (∑ m ∈ Finset.Icc 1 (k + n), g m) - (∑ m ∈ Finset.Icc 1 k, g m) := by
    rw [eq_sub_iff_add_eq, add_comm,
        ← Nat.Ico_succ_right 1 k, ← Nat.Ico_succ_right (k + 1) (k + n),
        ← Nat.Ico_succ_right 1 (k + n)]
    exact Finset.sum_Ico_consecutive g (by omega) (by omega)
  rw [hreindex, htel, mul_sub]
  simp only [gridPrim, hg]

/-- Both van der Veen sines are positive on the summation range (the two facts
    inside `whiteheadS_factor_pos`, in the `(π/N)`-argument form). -/
theorem whiteheadS_sin_pos {N n k j : ℕ} (hN : 2 ≤ N) (hj1 : 1 ≤ j) (hjn : j ≤ n)
    (hkn : k + n ≤ N - 1) :
    0 < Real.sin (((k : ℝ) + (j : ℝ)) * (π / N))
      ∧ 0 < Real.sin ((j : ℝ) * (π / N)) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hpi := Real.pi_pos
  have hpiN : (0 : ℝ) < π / N := by positivity
  have hj1' : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj1
  have hjN : (j : ℝ) < N := by
    have hjn' : j < N := by omega
    exact_mod_cast hjn'
  have hkjN : (k : ℝ) + (j : ℝ) < N := by
    have h : k + j < N := by omega
    have hc : ((k : ℝ) + (j : ℝ)) = ((k + j : ℕ) : ℝ) := by push_cast; ring
    rw [hc]; exact_mod_cast h
  have hk0 : (0 : ℝ) ≤ (k : ℝ) := by positivity
  refine ⟨Real.sin_pos_of_pos_of_lt_pi ?_ ?_, Real.sin_pos_of_pos_of_lt_pi ?_ ?_⟩
  · exact mul_pos (by linarith) hpiN
  · rw [show ((k : ℝ) + (j : ℝ)) * (π / N) = ((k : ℝ) + (j : ℝ)) * π / N by rw [mul_div_assoc],
        div_lt_iff₀ hNpos]; nlinarith [hkjN, hpi]
  · exact mul_pos (by linarith) hpiN
  · rw [show (j : ℝ) * (π / N) = (j : ℝ) * π / N by rw [mul_div_assoc], div_lt_iff₀ hNpos]
    nlinarith [hjN, hpi]

/-- **Regroup brick (BRICK 1).** `(2π/N)·log S_{n,k} = 4·S'(k+n) − 4·S'(k) − 2·S'(n)`
    (the log2-fold of `whiteheadS_log`, then `gridPrim_shift`). -/
theorem two_pi_log_whiteheadS_eq {N n k : ℕ} (hN : 2 ≤ N) (hkn : k + n ≤ N - 1) :
    (2 * π / N) * Real.log (QOU.Knot.WhiteheadVC.whiteheadS N n k)
      = 4 * gridPrim N (k + n) - 4 * gridPrim N k - 2 * gridPrim N n := by
  have hterm : ∀ a b : ℝ, 0 < Real.sin a → 0 < Real.sin b →
      Real.log 2 + 2 * Real.log (Real.sin a) - Real.log (Real.sin b)
        = 2 * Real.log (2 * Real.sin a) - Real.log (2 * Real.sin b) := by
    intro a b ha hb
    rw [Real.log_mul (by norm_num) (ne_of_gt ha),
        Real.log_mul (by norm_num) (ne_of_gt hb)]; ring
  rw [QOU.Knot.WhiteheadVC.whiteheadS_log hN hkn]
  have hrw : ∑ j ∈ Finset.Icc 1 n,
        (Real.log 2 + 2 * Real.log (Real.sin (((k : ℝ) + j) * π / N))
          - Real.log (Real.sin ((j : ℝ) * π / N)))
      = ∑ j ∈ Finset.Icc 1 n,
          (2 * Real.log (2 * Real.sin (((k : ℝ) + (j : ℝ)) * (π / N)))
            - Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) := by
    refine Finset.sum_congr rfl (fun j hj => ?_)
    obtain ⟨hj1, hjn⟩ := Finset.mem_Icc.mp hj
    obtain ⟨hsa, hsb⟩ := whiteheadS_sin_pos hN hj1 hjn hkn
    rw [show ((k : ℝ) + (j : ℝ)) * π / N = ((k : ℝ) + (j : ℝ)) * (π / N) by rw [mul_div_assoc],
        show (j : ℝ) * π / N = (j : ℝ) * (π / N) by rw [mul_div_assoc]]
    exact hterm _ _ hsa hsb
  rw [hrw, Finset.sum_sub_distrib, ← Finset.mul_sum]
  have hA : (π / N) * ∑ j ∈ Finset.Icc 1 n,
        Real.log (2 * Real.sin (((k : ℝ) + (j : ℝ)) * (π / N)))
      = gridPrim N (k + n) - gridPrim N k := gridPrim_shift
  have hB : (π / N) * ∑ j ∈ Finset.Icc 1 n,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))) = gridPrim N n := rfl
  have key : (2 * π / N) * (2 * (∑ j ∈ Finset.Icc 1 n,
          Real.log (2 * Real.sin (((k : ℝ) + (j : ℝ)) * (π / N))))
        - ∑ j ∈ Finset.Icc 1 n, Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      = 4 * ((π / N) * ∑ j ∈ Finset.Icc 1 n,
            Real.log (2 * Real.sin (((k : ℝ) + (j : ℝ)) * (π / N))))
        - 2 * ((π / N) * ∑ j ∈ Finset.Icc 1 n,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) := by ring
  rw [key, hA, hB]; ring

/-- **gridPrim limit brick (BRICK 2).**  At a moving index `Kseq N` with
    `2·Kseq·(π/N) → θ` and `1 ≤ Kseq ≤ N−1` (eventually), `S'(Kseq) → −clausen(θ)/2`
    — `abs_deviation_le` squeeze + `continuous_clausen` (figure-eight (b)+(c)). -/
theorem gridPrim_tendsto (Kseq : ℕ → ℕ) (θ : ℝ)
    (hK1 : ∀ᶠ N in Filter.atTop, 1 ≤ Kseq N)
    (hKN : ∀ᶠ N in Filter.atTop, Kseq N ≤ N - 1)
    (hgrid : Filter.Tendsto (fun N : ℕ => 2 * ((Kseq N : ℝ) * (π / N)))
        Filter.atTop (nhds θ)) :
    Filter.Tendsto (fun N : ℕ => gridPrim N (Kseq N))
      Filter.atTop (nhds (-QOU.Knot.clausen θ / 2)) := by
  have hcl : Filter.Tendsto
      (fun N : ℕ => -QOU.Knot.clausen (2 * ((Kseq N : ℝ) * (π / N))) / 2)
      Filter.atTop (nhds (-QOU.Knot.clausen θ / 2)) :=
    (((QOU.Knot.continuous_clausen.tendsto θ).comp hgrid).neg).div_const 2
  have hdev : Filter.Tendsto
      (fun N : ℕ => gridPrim N (Kseq N)
        - (-QOU.Knot.clausen (2 * ((Kseq N : ℝ) * (π / N))) / 2))
      Filter.atTop (nhds 0) := by
    refine squeeze_zero_norm' ?_ QOU.Knot.tendsto_master_error
    filter_upwards [hK1, hKN, Filter.eventually_ge_atTop 4] with N hk1 hkN hN4
    rw [Real.norm_eq_abs]
    exact QOU.Knot.abs_deviation_le hN4 hk1 hkN
  have hsum := hdev.add hcl
  rw [zero_add] at hsum
  exact hsum.congr (fun N => by ring)

/-- Grid-point limit helper: integer bounds `a·N − c ≤ b·Kseq ≤ a·N` (b>0) give
    `2·Kseq·(π/N) → 2(a/b)π`.  (The figure-eight (b) squeeze, parameterized.) -/
theorem gridpt_tendsto {a b c : ℕ} (hb : 0 < b) (Kseq : ℕ → ℕ)
    (hlo : ∀ N, a * N ≤ b * Kseq N + c) (hhi : ∀ N, b * Kseq N ≤ a * N) :
    Filter.Tendsto (fun N : ℕ => 2 * ((Kseq N : ℝ) * (π / N)))
      Filter.atTop (nhds (2 * ((a : ℝ) / (b : ℝ)) * π)) := by
  have hb' : (0 : ℝ) < b := by exact_mod_cast hb
  -- prove the b-scaled version → 2aπ (no /b), then divide
  have hscaled : Filter.Tendsto (fun N : ℕ => (b : ℝ) * (2 * ((Kseq N : ℝ) * (π / N))))
      Filter.atTop (nhds (2 * (a : ℝ) * π)) := by
    have hlow : Filter.Tendsto (fun N : ℕ => 2 * (a : ℝ) * π - 2 * (c : ℝ) * (π / N))
        Filter.atTop (nhds (2 * (a : ℝ) * π)) := by
      have h0 : Filter.Tendsto (fun N : ℕ => 2 * (c : ℝ) * (π / N)) Filter.atTop (nhds 0) := by
        have h : Filter.Tendsto (fun N : ℕ => 2 * (c : ℝ) * π / N) Filter.atTop (nhds 0) :=
          tendsto_const_div_atTop_nhds_zero_nat _
        simpa [mul_div_assoc] using h
      have h1 := (tendsto_const_nhds (x := 2 * (a : ℝ) * π)).sub h0
      simpa using h1
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow tendsto_const_nhds ?_ ?_
    · filter_upwards [Filter.eventually_gt_atTop 0] with N hN0
      have hNpos : (0 : ℝ) < N := by exact_mod_cast hN0
      have hh : (0 : ℝ) < π / N := by positivity
      have hfield : (N : ℝ) * (π / N) = π := by field_simp
      have e : (a : ℝ) * N * (π / N) = a * π := by rw [mul_assoc, hfield]
      have hlo' : (a : ℝ) * N ≤ (b : ℝ) * Kseq N + c := by exact_mod_cast hlo N
      nlinarith [mul_le_mul_of_nonneg_right hlo' (le_of_lt hh), e]
    · filter_upwards [Filter.eventually_gt_atTop 0] with N hN0
      have hNpos : (0 : ℝ) < N := by exact_mod_cast hN0
      have hh : (0 : ℝ) < π / N := by positivity
      have hfield : (N : ℝ) * (π / N) = π := by field_simp
      have e : (a : ℝ) * N * (π / N) = a * π := by rw [mul_assoc, hfield]
      have hhi' : (b : ℝ) * Kseq N ≤ (a : ℝ) * N := by exact_mod_cast hhi N
      nlinarith [mul_le_mul_of_nonneg_right hhi' (le_of_lt hh), e]
  have hfin := hscaled.div_const (b : ℝ)
  have htgt : 2 * (a : ℝ) * π / (b : ℝ) = 2 * ((a : ℝ) / (b : ℝ)) * π := by ring
  rw [htgt] at hfin
  exact Filter.Tendsto.congr (fun N => by field_simp) hfin

/-- Derivative of the van der Veen shifted-Clausen difference on `(0,π)`:
    `d/dθ [clausen θ − clausen(θ+π)] = log(2 sin((θ+π)/2)) − log(2 sin(θ/2))`. -/
theorem hasDerivAt_clausen_diff {θ : ℝ} (h0 : 0 < θ) (h2 : θ < π) :
    HasDerivAt (fun t => QOU.Knot.clausen t - QOU.Knot.clausen (t + π))
      (Real.log (2 * Real.sin ((θ + π) / 2)) - Real.log (2 * Real.sin (θ / 2))) θ := by
  have hpi := Real.pi_pos
  have hd1 := QOU.Knot.hasDerivAt_clausen h0 (by linarith)
  have hshift : HasDerivAt (fun s : ℝ => s + π) 1 θ := (hasDerivAt_id θ).add_const π
  have hd2 := (QOU.Knot.hasDerivAt_clausen (θ := θ + π) (by linarith) (by linarith)).comp θ hshift
  have hcomb := hd1.sub (by simpa using hd2)
  convert hcomb using 1; ring

/-- **Upper-envelope global bound (BRICK 4a).**  `clausen θ − clausen(θ+π) ≤
    2·clausen(π/2)` on `[0,π]` — the shifted-integrand max at the saddle
    `θ = π/2` (E2/E3 analogue). -/
theorem clausen_diff_le {θ : ℝ} (h0 : 0 ≤ θ) (h2 : θ ≤ π) :
    QOU.Knot.clausen θ - QOU.Knot.clausen (θ + π) ≤ 2 * QOU.Knot.clausen (π / 2) := by
  have hpi := Real.pi_pos
  set g : ℝ → ℝ := fun t => QOU.Knot.clausen t - QOU.Knot.clausen (t + π) with hgdef
  have hgmax : g (π / 2) = 2 * QOU.Knot.clausen (π / 2) := by
    simp only [hgdef, show π / 2 + π = 3 * π / 2 by ring, clausen_three_pi_div_two]; ring
  have hcont : Continuous g :=
    QOU.Knot.continuous_clausen.sub
      (QOU.Knot.continuous_clausen.comp (continuous_id.add continuous_const))
  have hderivval : ∀ t ∈ Set.Ioo (0 : ℝ) π,
      deriv g t = Real.log (2 * Real.sin ((t + π) / 2)) - Real.log (2 * Real.sin (t / 2)) :=
    fun t ht => (hasDerivAt_clausen_diff ht.1 ht.2).deriv
  -- monotone up to π/2, antitone after
  have hmono : MonotoneOn g (Set.Icc 0 (π / 2)) := by
    refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]; intro t ht
      exact (hasDerivAt_clausen_diff ht.1 (by linarith [ht.2])).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      have hsinpos : 0 < Real.sin (t / 2) :=
        Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.1, ht.2, hpi]) (by linarith [ht.1, ht.2, hpi])
      have hsin : Real.sin (t / 2) ≤ Real.cos (t / 2) := by
        rw [← Real.sin_pi_div_two_sub]
        exact Real.strictMonoOn_sin.monotoneOn
          ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩
          ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩
          (by linarith [ht.1, ht.2, hpi])
      rw [hderivval t ⟨ht.1, by linarith [ht.2, hpi]⟩, sub_nonneg,
          show (t + π) / 2 = t / 2 + π / 2 by ring, Real.sin_add_pi_div_two]
      exact Real.log_le_log (by linarith [hsinpos]) (by linarith [hsin])
  have hanti : AntitoneOn g (Set.Icc (π / 2) π) := by
    refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]; intro t ht
      exact (hasDerivAt_clausen_diff (by linarith [ht.1, ht.2, hpi]) ht.2).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      have hcospos : 0 < Real.cos (t / 2) :=
        Real.cos_pos_of_mem_Ioo ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩
      have hcs : Real.cos (t / 2) ≤ Real.sin (t / 2) := by
        rw [← Real.sin_pi_div_two_sub]
        exact Real.strictMonoOn_sin.monotoneOn
          ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩
          ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩
          (by linarith [ht.1, ht.2, hpi])
      rw [hderivval t ⟨by linarith [ht.1, ht.2, hpi], ht.2⟩, sub_nonpos,
          show (t + π) / 2 = t / 2 + π / 2 by ring, Real.sin_add_pi_div_two]
      exact Real.log_le_log (by linarith [hcospos]) (by linarith [hcs])
  rcases le_total θ (π / 2) with hle | hge
  · calc g θ ≤ g (π / 2) := hmono ⟨h0, hle⟩ ⟨by linarith [hpi], le_refl (π / 2)⟩ hle
      _ = 2 * QOU.Knot.clausen (π / 2) := hgmax
  · calc g θ ≤ g (π / 2) := hanti ⟨le_refl (π / 2), by linarith [hpi]⟩ ⟨hge, h2⟩ hge
      _ = 2 * QOU.Knot.clausen (π / 2) := hgmax

/-- Derivative of the shifted-Clausen difference for a general shift `s` on the
    interior of its domain. -/
theorem hasDerivAt_clausen_diff_shift {θ s : ℝ} (h0 : 0 < θ) (h2 : θ + s < 2 * π)
    (hs : 0 < s) :
    HasDerivAt (fun t => QOU.Knot.clausen t - QOU.Knot.clausen (t + s))
      (Real.log (2 * Real.sin ((θ + s) / 2)) - Real.log (2 * Real.sin (θ / 2))) θ := by
  have hd1 := QOU.Knot.hasDerivAt_clausen h0 (by linarith)
  have hshift : HasDerivAt (fun t : ℝ => t + s) 1 θ := (hasDerivAt_id θ).add_const s
  have hd2 := (QOU.Knot.hasDerivAt_clausen (θ := θ + s) (by linarith) h2).comp θ hshift
  have hcomb := hd1.sub (by simpa using hd2)
  convert hcomb using 1; ring

/-- **Generalized global bound.** `clausen θ − clausen(θ+s) ≤ 2·clausen(π−s/2)`
    (peak at `θ = π−s/2`, value `2·clausen(π−s/2)` via `clausen(π+s/2) =
    −clausen(π−s/2)`), for `0 < s ≤ π`, `0 ≤ θ ≤ 2π−s`. -/
theorem clausen_diff_le_shift {θ s : ℝ} (hs0 : 0 < s) (hsπ : s ≤ π)
    (h0 : 0 ≤ θ) (h2 : θ ≤ 2 * π - s) :
    QOU.Knot.clausen θ - QOU.Knot.clausen (θ + s) ≤ 2 * QOU.Knot.clausen (π - s / 2) := by
  have hpi := Real.pi_pos
  set g : ℝ → ℝ := fun t => QOU.Knot.clausen t - QOU.Knot.clausen (t + s) with hgdef
  have hgmax : g (π - s / 2) = 2 * QOU.Knot.clausen (π - s / 2) := by
    have hcl : QOU.Knot.clausen (π - s / 2 + s) = -QOU.Knot.clausen (π - s / 2) := by
      rw [show π - s / 2 + s = π + s / 2 by ring,
          QOU.Knot.clausen_eq_series (θ := π + s / 2) ⟨by linarith, by linarith⟩,
          QOU.Knot.clausen_eq_series (θ := π - s / 2) ⟨by linarith, by linarith⟩,
          show (π + s / 2 : ℝ) = 2 * π - (π - s / 2) by ring, QOU.Knot.Cl_2_two_pi_sub]
    simp only [hgdef]; rw [hcl]; ring
  have hcont : Continuous g :=
    QOU.Knot.continuous_clausen.sub
      (QOU.Knot.continuous_clausen.comp (continuous_id.add continuous_const))
  have hderivval : ∀ t ∈ Set.Ioo (0 : ℝ) (2 * π - s),
      deriv g t = Real.log (2 * Real.sin ((t + s) / 2)) - Real.log (2 * Real.sin (t / 2)) :=
    fun t ht => (hasDerivAt_clausen_diff_shift ht.1 (by linarith [ht.2]) hs0).deriv
  have hmono : MonotoneOn g (Set.Icc 0 (π - s / 2)) := by
    refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]; intro t ht
      exact (hasDerivAt_clausen_diff_shift ht.1 (by linarith [ht.2, hpi]) hs0).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      have hs1 : 0 < Real.sin (t / 2) :=
        Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.1, ht.2, hpi]) (by linarith [ht.1, ht.2, hpi])
      have hcmp : Real.sin (t / 2) ≤ Real.sin ((t + s) / 2) := by
        have hsm : Real.sin ((t + s) / 2) - Real.sin (t / 2)
            = 2 * Real.sin (s / 4) * Real.cos (t / 2 + s / 4) := by
          rw [Real.sin_sub_sin, show ((t + s) / 2 - t / 2) / 2 = s / 4 by ring,
              show ((t + s) / 2 + t / 2) / 2 = t / 2 + s / 4 by ring]
        have hsp : 0 < Real.sin (s / 4) :=
          Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
        have hcp : 0 ≤ Real.cos (t / 2 + s / 4) :=
          le_of_lt (Real.cos_pos_of_mem_Ioo ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩)
        nlinarith [hsm, mul_nonneg (mul_nonneg (by norm_num : (0:ℝ) ≤ 2) (le_of_lt hsp)) hcp]
      rw [hderivval t ⟨ht.1, by linarith [ht.2, hpi]⟩, sub_nonneg]
      exact Real.log_le_log (by linarith [hs1]) (by linarith [hcmp])
  have hanti : AntitoneOn g (Set.Icc (π - s / 2) (2 * π - s)) := by
    refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]; intro t ht
      exact (hasDerivAt_clausen_diff_shift (by linarith [ht.1, hpi]) (by linarith [ht.2]) hs0).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      have hs2 : 0 < Real.sin ((t + s) / 2) :=
        Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.1, ht.2, hpi]) (by linarith [ht.1, ht.2, hpi])
      have hcmp : Real.sin ((t + s) / 2) ≤ Real.sin (t / 2) := by
        have hsm : Real.sin (t / 2) - Real.sin ((t + s) / 2)
            = 2 * Real.sin (-(s / 4)) * Real.cos (t / 2 + s / 4) := by
          rw [Real.sin_sub_sin, show (t / 2 - (t + s) / 2) / 2 = -(s / 4) by ring,
              show (t / 2 + (t + s) / 2) / 2 = t / 2 + s / 4 by ring]
        have hsp : Real.sin (-(s / 4)) ≤ 0 := by
          rw [Real.sin_neg]
          exact neg_nonpos_of_nonneg (le_of_lt (Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)))
        have hcp : Real.cos (t / 2 + s / 4) ≤ 0 :=
          Real.cos_nonpos_of_pi_div_two_le_of_le (by linarith [ht.1, hpi]) (by linarith [ht.2, hpi])
        nlinarith [hsm, mul_nonneg
          (neg_nonneg.2 (mul_nonpos_of_nonneg_of_nonpos (by norm_num : (0:ℝ) ≤ 2) hsp))
          (neg_nonneg.2 hcp)]
      rw [hderivval t ⟨by linarith [ht.1, hpi], by linarith [ht.2]⟩, sub_nonpos]
      exact Real.log_le_log (by linarith [hs2]) (by linarith [hcmp])
  rcases le_total θ (π - s / 2) with hle | hge
  · calc g θ ≤ g (π - s / 2) := hmono ⟨h0, hle⟩ ⟨by linarith, le_refl _⟩ hle
      _ = 2 * QOU.Knot.clausen (π - s / 2) := hgmax
  · calc g θ ≤ g (π - s / 2) := hanti ⟨le_refl _, by linarith⟩ ⟨hge, h2⟩ hge
      _ = 2 * QOU.Knot.clausen (π - s / 2) := hgmax

/-- The `abs_deviation_le` master error as a named sequence (= `tendsto_master_error`). -/
noncomputable def devErr (N : ℕ) : ℝ :=
  |(-QOU.Knot.clausen (2 * (π / N)) / 2)| + (π / N) * |Real.log (2 * Real.sin (π / N))|
    + 7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2))

theorem tendsto_devErr : Filter.Tendsto devErr Filter.atTop (nhds 0) :=
  QOU.Knot.tendsto_master_error

theorem gridPrim_le {N K : ℕ} (hN : 4 ≤ N) (hK : 1 ≤ K) (hKN : K ≤ N - 1) :
    gridPrim N K ≤ -QOU.Knot.clausen (2 * ((K : ℝ) * (π / N))) / 2 + devErr N := by
  have h := QOU.Knot.abs_deviation_le hN hK hKN
  rw [abs_le] at h
  simp only [gridPrim, devErr]; linarith [h.2]

theorem gridPrim_ge {N K : ℕ} (hN : 4 ≤ N) (hK : 1 ≤ K) (hKN : K ≤ N - 1) :
    -QOU.Knot.clausen (2 * ((K : ℝ) * (π / N))) / 2 - devErr N ≤ gridPrim N K := by
  have h := QOU.Knot.abs_deviation_le hN hK hKN
  rw [abs_le] at h
  simp only [gridPrim, devErr]; linarith [h.1]

/-- `clausen ≥ 0` on `[0,π]` (the positive lobe): `clausen(0)=clausen(π)=0`,
    increasing to the max at `π/3`, then decreasing. -/
theorem clausen_nonneg {θ : ℝ} (h0 : 0 ≤ θ) (h2 : θ ≤ π) : 0 ≤ QOU.Knot.clausen θ := by
  have hpi := Real.pi_pos
  have hderiv_nonpos : ∀ t : ℝ, π / 3 ≤ t → t < 2 * π →
      Real.sin (t / 2) ≥ 1 / 2 → deriv QOU.Knot.clausen t ≤ 0 := by
    intro t ht1 ht2 hsin
    rw [(QOU.Knot.hasDerivAt_clausen (by linarith) ht2).deriv]
    exact neg_nonpos_of_nonneg (Real.log_nonneg (by linarith [hsin]))
  have hmono : MonotoneOn QOU.Knot.clausen (Set.Icc 0 (π / 3)) := by
    refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) QOU.Knot.continuous_clausen.continuousOn ?_ ?_
    · rw [interior_Icc]; intro t ht
      exact (QOU.Knot.hasDerivAt_clausen ht.1 (by linarith [ht.2, hpi])).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      rw [(QOU.Knot.hasDerivAt_clausen ht.1 (by linarith [ht.2, hpi])).deriv]
      have hsnn : (0 : ℝ) ≤ Real.sin (t / 2) :=
        Real.sin_nonneg_of_nonneg_of_le_pi (by linarith [ht.1]) (by linarith [ht.2, hpi])
      refine neg_nonneg.2 (Real.log_nonpos (by linarith [hsnn]) ?_)
      have hsm : Real.sin (t / 2) ≤ 1 / 2 := by
        rw [show (1 : ℝ) / 2 = Real.sin (π / 6) by rw [Real.sin_pi_div_six]]
        exact Real.strictMonoOn_sin.monotoneOn ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩
          ⟨by linarith [hpi], by linarith [hpi]⟩ (by linarith [ht.2])
      linarith [hsm]
  have hanti : AntitoneOn QOU.Knot.clausen (Set.Icc (π / 3) π) := by
    refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) QOU.Knot.continuous_clausen.continuousOn ?_ ?_
    · rw [interior_Icc]; intro t ht
      exact (QOU.Knot.hasDerivAt_clausen (by linarith [ht.1, hpi]) (by linarith [ht.2, hpi])).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      refine hderiv_nonpos t (le_of_lt ht.1) (by linarith [ht.2, hpi]) ?_
      have hsm : Real.sin (π / 6) ≤ Real.sin (t / 2) := by
        exact Real.strictMonoOn_sin.monotoneOn ⟨by linarith [hpi], by linarith [hpi]⟩
          ⟨by linarith [ht.1, ht.2, hpi], by linarith [ht.1, ht.2, hpi]⟩ (by linarith [ht.1])
      rw [Real.sin_pi_div_six] at hsm; linarith [hsm]
  rcases le_total θ (π / 3) with hle | hge
  · calc (0 : ℝ) = QOU.Knot.clausen 0 := QOU.Knot.clausen_zero.symm
      _ ≤ QOU.Knot.clausen θ := hmono ⟨le_refl 0, by linarith [hpi]⟩ ⟨h0, hle⟩ h0
  · calc (0 : ℝ) = QOU.Knot.clausen π := QOU.Knot.clausen_pi.symm
      _ ≤ QOU.Knot.clausen θ := hanti ⟨hge, h2⟩ ⟨by linarith [hpi], le_refl π⟩ h2

/-- **Uniform per-term upper bound (BRICK 5a).**  For every valid `k`,
    `(2π/N)·log S_{⌊N/2⌋,k} ≤ 4·clausen(π − ⌊N/2⌋π/N) + clausen(2⌊N/2⌋π/N) +
    10·devErr N` — a `k`-independent RHS (the parity-clean upper envelope via
    `clausen_diff_le_shift` at `s = 2⌊N/2⌋π/N`). -/
theorem two_pi_log_whiteheadS_le {N k : ℕ} (hN : 4 ≤ N) (hk1 : 1 ≤ k)
    (hkn : k + N / 2 ≤ N - 1) :
    (2 * π / N) * Real.log (QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) k)
      ≤ 4 * QOU.Knot.clausen (π - ((N / 2 : ℕ) : ℝ) * (π / N))
        + QOU.Knot.clausen (2 * (((N / 2 : ℕ) : ℝ) * (π / N))) + 10 * devErr N := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hpi := Real.pi_pos
  have hpiN : (0 : ℝ) < π / N := by positivity
  rw [two_pi_log_whiteheadS_eq (by omega) hkn]
  have hg1 := gridPrim_le hN (by omega : 1 ≤ k + N / 2) (by omega : k + N / 2 ≤ N - 1)
  have hg2 := gridPrim_ge hN hk1 (by omega : k ≤ N - 1)
  have hg3 := gridPrim_ge hN (by omega : 1 ≤ N / 2) (by omega : N / 2 ≤ N - 1)
  have harg : (2 : ℝ) * ((((k + N / 2 : ℕ)) : ℝ) * (π / N))
      = 2 * ((k : ℝ) * (π / N)) + 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) := by push_cast; ring
  rw [harg] at hg1
  have hθn_le : 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) ≤ π := by
    have hb : 2 * ((N / 2 : ℕ) : ℝ) ≤ (N : ℝ) := by
      have h := (by omega : 2 * (N / 2) ≤ N)
      calc 2 * ((N / 2 : ℕ) : ℝ) = ((2 * (N / 2) : ℕ) : ℝ) := by push_cast; ring
        _ ≤ (N : ℝ) := by exact_mod_cast h
    have hpiN' : (N : ℝ) * (π / N) = π := by field_simp
    nlinarith [mul_le_mul_of_nonneg_right hb (le_of_lt hpiN), hpiN']
  have hθ_le : 2 * ((k : ℝ) * (π / N)) ≤ 2 * π - 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) := by
    have hkb : (k : ℝ) + ((N / 2 : ℕ) : ℝ) ≤ (N : ℝ) := by
      have h := (by omega : k + N / 2 ≤ N)
      calc (k : ℝ) + ((N / 2 : ℕ) : ℝ) = ((k + N / 2 : ℕ) : ℝ) := by push_cast; ring
        _ ≤ (N : ℝ) := by exact_mod_cast h
    have hpiN' : (N : ℝ) * (π / N) = π := by field_simp
    nlinarith [mul_le_mul_of_nonneg_right hkb (le_of_lt hpiN), hpiN']
  have hn2pos : (0 : ℝ) < ((N / 2 : ℕ) : ℝ) := by exact_mod_cast (by omega : 0 < N / 2)
  have hcds := clausen_diff_le_shift (θ := 2 * ((k : ℝ) * (π / N)))
    (s := 2 * (((N / 2 : ℕ) : ℝ) * (π / N)))
    (mul_pos (by norm_num) (mul_pos hn2pos hpiN)) hθn_le (by positivity) hθ_le
  rw [show π - 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) / 2 = π - ((N / 2 : ℕ) : ℝ) * (π / N) by ring] at hcds
  linarith [hg1, hg2, hg3, hcds]

/-- `devErr N ≥ 0` — every summand of the master error is nonnegative. -/
theorem devErr_nonneg (N : ℕ) : 0 ≤ devErr N := by
  have hpiN : (0 : ℝ) ≤ π / N := div_nonneg Real.pi_pos.le (Nat.cast_nonneg N)
  have hlog2 : (0 : ℝ) ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have h2 : (0 : ℝ) ≤ (π / N) * |Real.log (2 * Real.sin (π / N))| :=
    mul_nonneg hpiN (abs_nonneg _)
  have h3 : (0 : ℝ) ≤ 7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)) := by
    have hh : (0 : ℝ) ≤ (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) :=
      mul_nonneg hpiN (by linarith [abs_nonneg (Real.log (2 * Real.sin (π / N)))])
    linarith
  simp only [devErr]
  linarith [abs_nonneg (-QOU.Knot.clausen (2 * (π / N)) / 2)]

/-- The `k`-independent upper envelope from BRICK 5a, packaged as a named
    sequence.  Its limit is `4·catalanG = 4G` (grid points `⌊N/2⌋π/N → π/2`,
    `2⌊N/2⌋π/N → π`; `devErr → 0`). -/
noncomputable def whiteheadUmax (N : ℕ) : ℝ :=
  4 * QOU.Knot.clausen (π - ((N / 2 : ℕ) : ℝ) * (π / N))
    + QOU.Knot.clausen (2 * (((N / 2 : ℕ) : ℝ) * (π / N))) + 10 * devErr N

/-- **Uniform per-term upper bound over the WHOLE range** `0 ≤ k ≤ N-1-⌊N/2⌋`
    (BRICK 5a extended to the `k = 0` maximizer edge via `clausen_nonneg`):
    every term satisfies `(2π/N)·log S_{⌊N/2⌋,k} ≤ whiteheadUmax N`. -/
theorem two_pi_log_whiteheadS_le_all {N k : ℕ} (hN : 4 ≤ N)
    (hkn : k + N / 2 ≤ N - 1) :
    (2 * π / N) * Real.log (QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) k)
      ≤ whiteheadUmax N := by
  rcases Nat.eq_zero_or_pos k with hk0 | hk1
  · -- k = 0 : gridPrim N 0 = 0 collapses the identity to 2·gridPrim N (N/2)
    subst hk0
    have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hpi := Real.pi_pos
    have hpiN : (0 : ℝ) < π / N := by positivity
    rw [two_pi_log_whiteheadS_eq (by omega) hkn]
    have hIcc : Finset.Icc (1 : ℕ) 0 = ∅ := Finset.Icc_eq_empty (by omega)
    have hz : gridPrim N 0 = 0 := by rw [gridPrim, hIcc, Finset.sum_empty, mul_zero]
    simp only [Nat.zero_add]
    rw [hz]
    have hg := gridPrim_le hN (by omega : 1 ≤ N / 2) (by omega : N / 2 ≤ N - 1)
    have hn2pos : (0 : ℝ) < ((N / 2 : ℕ) : ℝ) := by exact_mod_cast (by omega : 0 < N / 2)
    have haN_le : 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) ≤ π := by
      have hb : 2 * ((N / 2 : ℕ) : ℝ) ≤ (N : ℝ) := by
        have h := (by omega : 2 * (N / 2) ≤ N)
        calc 2 * ((N / 2 : ℕ) : ℝ) = ((2 * (N / 2) : ℕ) : ℝ) := by push_cast; ring
          _ ≤ (N : ℝ) := by exact_mod_cast h
      have hpiN' : (N : ℝ) * (π / N) = π := by field_simp
      nlinarith [mul_le_mul_of_nonneg_right hb (le_of_lt hpiN), hpiN']
    have haN_nn : (0 : ℝ) ≤ 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) := by positivity
    have hcl_aN : 0 ≤ QOU.Knot.clausen (2 * (((N / 2 : ℕ) : ℝ) * (π / N))) :=
      clausen_nonneg haN_nn haN_le
    have hP_nn : (0 : ℝ) ≤ π - ((N / 2 : ℕ) : ℝ) * (π / N) := by linarith [haN_le]
    have hP_le : π - ((N / 2 : ℕ) : ℝ) * (π / N) ≤ π := by
      linarith [mul_pos hn2pos hpiN]
    have hcl_P : 0 ≤ QOU.Knot.clausen (π - ((N / 2 : ℕ) : ℝ) * (π / N)) :=
      clausen_nonneg hP_nn hP_le
    have hdev := devErr_nonneg N
    simp only [whiteheadUmax]
    linarith [hg, hcl_P, hcl_aN, hdev]
  · -- k ≥ 1 : BRICK 5a directly
    simp only [whiteheadUmax]
    exact two_pi_log_whiteheadS_le hN hk1 hkn

/-- **Explicit saddle-term convergence (BRICK 3).**  At the saddle
    `(n*, k*) = (⌊N/2⌋, ⌊N/4⌋)`, `(2π/N)·log S_{n*,k*} → 4·catalanG = 4G`. -/
theorem whiteheadS_explicit_saddle_tendsto :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log (QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) (N / 4)))
      Filter.atTop (nhds (4 * QOU.Knot.WhiteheadVC.catalanG)) := by
  have hkn := gridPrim_tendsto (fun N => N / 4 + N / 2) (3 * π / 2)
    (Filter.eventually_atTop.2 ⟨4, fun N hN => by simp only []; omega⟩)
    (Filter.eventually_atTop.2 ⟨4, fun N hN => by simp only []; omega⟩)
    (by
      have h := gridpt_tendsto (a := 3) (b := 4) (c := 5) (by norm_num) (fun N => N / 4 + N / 2)
        (fun N => by simp only []; omega) (fun N => by simp only []; omega)
      have heq : 2 * (((3 : ℕ) : ℝ) / ((4 : ℕ) : ℝ)) * π = 3 * π / 2 := by push_cast; ring
      rwa [heq] at h)
  have hk := gridPrim_tendsto (fun N => N / 4) (π / 2)
    (Filter.eventually_atTop.2 ⟨4, fun N hN => by simp only []; omega⟩)
    (Filter.eventually_atTop.2 ⟨1, fun N hN => by simp only []; omega⟩)
    (by
      have h := gridpt_tendsto (a := 1) (b := 4) (c := 3) (by norm_num) (fun N => N / 4)
        (fun N => by simp only []; omega) (fun N => by simp only []; omega)
      have heq : 2 * (((1 : ℕ) : ℝ) / ((4 : ℕ) : ℝ)) * π = π / 2 := by push_cast; ring
      rwa [heq] at h)
  have hn := gridPrim_tendsto (fun N => N / 2) π
    (Filter.eventually_atTop.2 ⟨2, fun N hN => by simp only []; omega⟩)
    (Filter.eventually_atTop.2 ⟨1, fun N hN => by simp only []; omega⟩)
    (by
      have h := gridpt_tendsto (a := 1) (b := 2) (c := 1) (by norm_num) (fun N => N / 2)
        (fun N => by simp only []; omega) (fun N => by simp only []; omega)
      have heq : 2 * (((1 : ℕ) : ℝ) / ((2 : ℕ) : ℝ)) * π = π := by push_cast; ring
      rwa [heq] at h)
  have hrhs := ((hkn.const_mul 4).sub (hk.const_mul 4)).sub (hn.const_mul 2)
  have hval : (4 : ℝ) * (-QOU.Knot.clausen (3 * π / 2) / 2)
        - 4 * (-QOU.Knot.clausen (π / 2) / 2) - 2 * (-QOU.Knot.clausen π / 2)
      = 4 * QOU.Knot.WhiteheadVC.catalanG := by
    rw [clausen_three_pi_div_two, QOU.Knot.clausen_pi, catalanG_eq_clausen_pi_div_two]; ring
  rw [hval] at hrhs
  refine Filter.Tendsto.congr' ?_ hrhs
  filter_upwards [Filter.eventually_ge_atTop 4] with N hN4
  exact (two_pi_log_whiteheadS_eq (by omega) (by omega)).symm

/-- **The Whitehead Volume Conjecture for the `⌊N/2⌋`-level inner sum**
    (UNCONDITIONAL, sorry-free): `(2π/N)·log(Σ_k S_{⌊N/2⌋,k}) → 4·catalanG = 4G`.

    Squeeze: below by the explicit `k*=⌊N/4⌋` saddle term
    (`whiteheadS_explicit_saddle_tendsto`, BRICK 3), above by the
    `k`-independent envelope `(2π/N)·log N + whiteheadUmax N` (max-term
    `≤ whiteheadUmax N` for every `k` incl. `k=0` via
    `two_pi_log_whiteheadS_le_all`, slack `(2π/N)·log N → 0`), both `→ 4·G`.
    This closes the analytic limit left open in
    `QOU.Knot.WhiteheadVC.whitehead_volume_conjecture` (bean qou-1gkf). -/
theorem whitehead_vc_innerSum_half :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / N) *
        Real.log (QOU.Knot.WhiteheadVC.whiteheadInnerSum N (N / 2)))
      Filter.atTop (nhds (4 * QOU.Knot.WhiteheadVC.catalanG)) := by
  -- grid `2·(⌊N/2⌋·π/N) → π`  (a=1, b=2, c=1)
  have hgrid : Filter.Tendsto (fun N : ℕ => 2 * (((N / 2 : ℕ) : ℝ) * (π / N)))
      Filter.atTop (nhds π) := by
    have h := gridpt_tendsto (a := 1) (b := 2) (c := 1) (by norm_num) (fun N => N / 2)
      (fun N => by simp only []; omega) (fun N => by simp only []; omega)
    have heq : 2 * (((1 : ℕ) : ℝ) / ((2 : ℕ) : ℝ)) * π = π := by push_cast; ring
    rwa [heq] at h
  -- `clausen(2·⌊N/2⌋·π/N) → clausen π`
  have hclA : Filter.Tendsto
      (fun N : ℕ => QOU.Knot.clausen (2 * (((N / 2 : ℕ) : ℝ) * (π / N))))
      Filter.atTop (nhds (QOU.Knot.clausen π)) :=
    (QOU.Knot.continuous_clausen.tendsto π).comp hgrid
  -- `clausen(π − ⌊N/2⌋·π/N) → clausen(π/2)`
  have hargP : Filter.Tendsto (fun N : ℕ => π - ((N / 2 : ℕ) : ℝ) * (π / N))
      Filter.atTop (nhds (π / 2)) := by
    have hhalf : Filter.Tendsto (fun N : ℕ => ((N / 2 : ℕ) : ℝ) * (π / N))
        Filter.atTop (nhds (π / 2)) := (hgrid.div_const 2).congr (fun N => by ring)
    have hd := (tendsto_const_nhds (x := π)).sub hhalf
    rwa [show π - π / 2 = π / 2 from by ring] at hd
  have hclP : Filter.Tendsto
      (fun N : ℕ => QOU.Knot.clausen (π - ((N / 2 : ℕ) : ℝ) * (π / N)))
      Filter.atTop (nhds (QOU.Knot.clausen (π / 2))) :=
    (QOU.Knot.continuous_clausen.tendsto (π / 2)).comp hargP
  -- `whiteheadUmax N → 4·catalanG`
  have hUmax : Filter.Tendsto whiteheadUmax Filter.atTop
      (nhds (4 * QOU.Knot.WhiteheadVC.catalanG)) := by
    have hlim := ((hclP.const_mul 4).add hclA).add (tendsto_devErr.const_mul 10)
    rw [QOU.Knot.clausen_pi, ← catalanG_eq_clausen_pi_div_two,
      show 4 * QOU.Knot.WhiteheadVC.catalanG + 0 + 10 * 0
        = 4 * QOU.Knot.WhiteheadVC.catalanG from by ring] at hlim
    exact hlim.congr (fun N => by simp only [whiteheadUmax])
  -- upper envelope `(2π/N)·log N + whiteheadUmax N → 4·catalanG`
  have hupper : Filter.Tendsto (fun N : ℕ => (2 * π / N) * Real.log N + whiteheadUmax N)
      Filter.atTop (nhds (4 * QOU.Knot.WhiteheadVC.catalanG)) := by
    have h := QOU.Knot.WhiteheadVC.tendsto_slack_zero.add hUmax
    rwa [zero_add] at h
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le'
    whiteheadS_explicit_saddle_tendsto hupper ?_ ?_
  · -- lower: `(2π/N)·log S_{⌊N/2⌋,⌊N/4⌋} ≤ (2π/N)·log(innerSum)`
    filter_upwards [Filter.eventually_ge_atTop 4] with N hN
    have hN2 : 2 ≤ N := by omega
    have hSpos : 0 < QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) (N / 4) :=
      QOU.Knot.WhiteheadVC.whiteheadS_pos hN2 (by omega)
    have hle : QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) (N / 4)
        ≤ QOU.Knot.WhiteheadVC.whiteheadInnerSum N (N / 2) :=
      QOU.Knot.WhiteheadVC.whiteheadS_le_innerSum hN2 (by omega)
    have hscale : (0 : ℝ) ≤ 2 * π / N := by positivity
    exact mul_le_mul_of_nonneg_left (Real.log_le_log hSpos hle) hscale
  · -- upper: `(2π/N)·log(innerSum) ≤ (2π/N)·log N + whiteheadUmax N`
    filter_upwards [Filter.eventually_ge_atTop 4] with N hN
    have hN2 : 2 ≤ N := by omega
    obtain ⟨kmax, hklt, _, hup⟩ :=
      QOU.Knot.WhiteheadVC.whiteheadInnerSum_saddle hN2 (by omega : N / 2 < N)
    have hkmaxrange : kmax + N / 2 ≤ N - 1 := by omega
    have hSkpos : 0 < QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) kmax :=
      QOU.Knot.WhiteheadVC.whiteheadS_pos hN2 (by omega)
    have hinner_pos : 0 < QOU.Knot.WhiteheadVC.whiteheadInnerSum N (N / 2) :=
      QOU.Knot.WhiteheadVC.whiteheadInnerSum_pos hN2 (by omega)
    have hcardpos : (0 : ℝ) < ((N - N / 2 : ℕ) : ℝ) :=
      by exact_mod_cast (by omega : 0 < N - N / 2)
    have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hscale : (0 : ℝ) ≤ 2 * π / N := by positivity
    have hup' : QOU.Knot.WhiteheadVC.whiteheadInnerSum N (N / 2)
        ≤ ((N - N / 2 : ℕ) : ℝ) * QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) kmax := by
      rw [nsmul_eq_mul] at hup; exact hup
    have hlog1 := Real.log_le_log hinner_pos hup'
    rw [Real.log_mul (ne_of_gt hcardpos) (ne_of_gt hSkpos)] at hlog1
    have hstep := mul_le_mul_of_nonneg_left hlog1 hscale
    rw [mul_add] at hstep
    have hslack : (2 * π / N) * Real.log ((N - N / 2 : ℕ) : ℝ)
        ≤ (2 * π / N) * Real.log N :=
      mul_le_mul_of_nonneg_left
        (Real.log_le_log hcardpos (by exact_mod_cast Nat.sub_le N (N / 2))) hscale
    have hterm : (2 * π / N) * Real.log (QOU.Knot.WhiteheadVC.whiteheadS N (N / 2) kmax)
        ≤ whiteheadUmax N := two_pi_log_whiteheadS_le_all hN hkmaxrange
    linarith [hstep, hslack, hterm]

/-
  ROADMAP — remaining bricks to discharge `hsaddle` (all ingredients verified
  present in `QOU.Knot.Clausen`; algebra confirmed to 40 digits in
  `computations/whitehead_saddle.py`).

  (A) VALUE identity  V = 4·clausen(π/2)  ( = 4G ):
      · integrand `log2 + 2 log sin(π(u+¼)) − log sin(π u)` reduces (log-sin =
        log(2 sin) − log2, valid since sin>0 on the ranges) to the log2-free
        `2 log(2 sin(π(u+¼))) − log(2 sin(π u))` — the log2 terms cancel exactly.
      · ∫_0^{1/2} log(2 sin(π u)) du = integral_log_two_sin_pi (1/2)
          = −clausen(π)/(2π) = 0                        [clausen_pi]
      · ∫_0^{1/2} log(2 sin(π(u+¼))) du
          = ∫_{1/4}^{3/4} log(2 sin(π v)) dv            [integral_comp_add_right]
          = integral_log_two_sin_pi (3/4) − integral_log_two_sin_pi (1/4)
                                                        [integral_add_adjacent_intervals,
                                                         + integrability of log(2 sin(π·))]
          = (clausen(π/2) − clausen(3π/2)) / (2π)
      · clausen(3π/2) = clausen(2π − π/2) = Cl_2(2π−π/2) = −Cl_2(π/2)
          = −clausen(π/2)                     [clausen_eqOn_Cl_2 + Cl_2_two_pi_sub]
      ⇒ V = 2π·(2·(2clausen(π/2))/(2π) − 0) = 4·clausen(π/2).

  (B) CONVERGENCE  (2π/N)·log S_{n*,k*} → V, at nseq→N/2, kseq→N/4:
      the log(2 sin) Riemann sum is squeezed between the window integrals via
      integral_le_sum_log_sin / sum_log_sin_le_integral (rising) and the
      _falling variants; master-error → 0 (as in FigureEightVolumeSaddle E5c).

  (A)+(B) discharge the `hsaddle` hypothesis of
  `QOU.Knot.WhiteheadVC.whitehead_vc_of_saddle_value`, closing the unconditional
  Whitehead Volume Conjecture.  -- Ref: [vanderveen2008] arXiv:math/0611181
-/

end QOU.Knot.WhiteheadSaddle
