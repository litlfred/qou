import QOU.BraidKnot.AJTrefoil
import QOU.BraidKnot.AJTrefoilRootEval

/-!
# QOU.BraidKnot.AJTrefoilAnnihilation

**The general-`N` trefoil annihilation, assembled from two strictly
smaller cited cores** (beans `6q9g` + `rz8b`).

Unlike `4₁` (order 2, genuine qZeilberger certificate), the trefoil
annihilator is order 1 and the Rosso–Jones tower extends by a SINGLE term
per color, so no telescoping certificate is needed: with
`P(n) = ∑_{j≤n} (−1)^j w^{6j(j+1)} [2j+1]_v` the tower is
`J(n+1) = (−1)^n w^{−6n(n+2)} P(n)/[n+1]_v` (`coloredJonesTrefoil_eq_P_form`,
proved — all quadratic exponents cancel in the operator's ratios), and the
annihilation reduces to two rational identities in `(w, Y = (w²)^N)`
([C1] coefficient cancellation, [C2] boundary), pre-verified exactly in
`computations/aj_trefoil_telescope_assembly_check.py` and proved here
inside the generic case.

## The degenerate colors — an honest finding

`coloredJonesTrefoil` divides by `qInt (w²) N`, which vanishes exactly
when `x = (w⁴)^N = 1` — there the Lean value is the division-by-zero
convention `0`, not the analytic value.  The class field quantifies over
ALL `w ≠ 0`, and it remains TRUE there because the operator's own
coefficients vanish exactly at the junk slots (`a₀` at `x = 1`, `a₁` at
`xq = 1`); the surviving term then needs the **root-of-unity evaluation**
`J = 1` at the neighboring color.  The case split:

* `w⁴ = 1` — every `qInt` collapses and both sides vanish (proved);
* generic (`x ≠ 1`, `xq ≠ 1`) — the [C1]/[C2] computation (proved);
* `x = 1` / `xq = 1` — reduces to the two evaluation cores
  `trefoil_eval_at_root_prev` / `trefoil_eval_at_root_next`
  (`J(N+1) = 1` when `(w⁴)^N = 1`, resp. `J(N) = 1` when `(w⁴)^{N+1} = 1`)
  — root-of-unity periodicity of the Rosso–Jones sum, **proved**
  (sorry-free) via the genuine sum evaluation in
  `QOU.BraidKnot.AJTrefoilRootEval` (reflection + shift reindexings and
  a Gauss-sum block-cancellation collapse), and numerically
  pre-verified to 40 dps in the pre-verification script.

## Base ring (§7c)

Generic `{K : Type*} [Field K]`; no `ℝ`, no ordering.
-/

namespace QOU.BraidKnot.AJTrefoil

open Finset
open QOU.BraidKnot.AJFigureEight

variable {K : Type*} [Field K]

/-- Signed cyclotomic partial sum of the Rosso–Jones tower:
    `P(n) = ∑_{j≤n} (−1)^j w^{6j(j+1)} [2j+1]_{w²}` — all exponents are
    `ℕ`-powers. -/
def trP (w : K) (n : ℕ) : K :=
  ∑ j ∈ Finset.range (n + 1),
    (-1 : K) ^ j * w ^ (6 * (j * (j + 1))) * qInt (w ^ 2) (2 * j + 1)

theorem trP_succ (w : K) (n : ℕ) :
    trP w (n + 1) = trP w n
      + (-1 : K) ^ (n + 1) * w ^ (6 * ((n + 1) * (n + 1 + 1)))
        * qInt (w ^ 2) (2 * (n + 1) + 1) := by
  unfold trP
  rw [Finset.sum_range_succ]

/-- `(−1)^{n−j} = (−1)^n (−1)^j` for `j ≤ n` (over any field). -/
private theorem neg_one_pow_sub {n j : ℕ} (hj : j ≤ n) :
    (-1 : K) ^ (n - j) = (-1 : K) ^ n * (-1 : K) ^ j := by
  have h : (-1 : K) ^ (n - j) * (-1 : K) ^ j = (-1 : K) ^ n := by
    rw [← pow_add, Nat.sub_add_cancel hj]
  have h2 : (-1 : K) ^ j * (-1 : K) ^ j = 1 := by
    rw [← mul_pow]; norm_num
  calc (-1 : K) ^ (n - j)
      = (-1 : K) ^ (n - j) * ((-1 : K) ^ j * (-1 : K) ^ j) := by
        rw [h2, mul_one]
    _ = ((-1 : K) ^ (n - j) * (-1 : K) ^ j) * (-1 : K) ^ j := by ring
    _ = (-1 : K) ^ n * (-1 : K) ^ j := by rw [h]

/-- **P-form of the tower** (pure rearrangement, holds for every
    `w ≠ 0` — no denominator hypotheses):
    `J(n+1) = (−1)^n (w^{6n(n+2)})⁻¹ P(n) / [n+1]_{w²}`. -/
theorem coloredJonesTrefoil_eq_P_form {w : K} (hw : w ≠ 0) (n : ℕ) :
    coloredJonesTrefoil w (n + 1)
      = (-1 : K) ^ n * (w ^ (6 * (n * (n + 2))))⁻¹ * trP w n
          / qInt (w ^ 2) (n + 1) := by
  show w ^ (-(3 : ℤ) * ((n : ℕ) * (n + 2) : ℤ))
      * (∑ j ∈ Finset.range (n + 1),
          (twistEigenvalue w n j) ^ 3 * qInt (w ^ 2) (2 * j + 1))
      / qInt (w ^ 2) (n + 1)
    = (-1 : K) ^ n * (w ^ (6 * (n * (n + 2))))⁻¹ * trP w n
        / qInt (w ^ 2) (n + 1)
  congr 1
  rw [Finset.mul_sum]
  unfold trP
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun j hj => ?_
  have hjn : j ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
  unfold twistEigenvalue
  -- cube of the sign
  have hs : (((-1 : K) ^ (n - j)) : K) ^ 3 = (-1 : K) ^ (n - j) := by
    calc ((-1 : K) ^ (n - j)) ^ 3 = ((-1 : K) ^ 3) ^ (n - j) := by
          rw [← pow_mul, mul_comm, pow_mul]
      _ = (-1 : K) ^ (n - j) := by norm_num
  -- cube of the zpow and merge with the prefactor
  have hz : (w ^ ((2 * j * (j + 1) : ℤ) - (n * (n + 2) : ℤ))) ^ 3
        * w ^ (-(3 : ℤ) * ((n : ℕ) * (n + 2) : ℤ))
      = w ^ (6 * (j * (j + 1))) * (w ^ (6 * (n * (n + 2))))⁻¹ := by
    rw [← zpow_natCast (w ^ ((2 * j * (j + 1) : ℤ) - (n * (n + 2) : ℤ))) 3,
      ← zpow_mul, ← zpow_add₀ hw,
      ← zpow_natCast w (6 * (j * (j + 1))),
      ← zpow_natCast w (6 * (n * (n + 2))),
      ← zpow_neg, ← zpow_add₀ hw]
    congr 1
    push_cast
    ring
  calc w ^ (-(3 : ℤ) * ((n : ℕ) * (n + 2) : ℤ))
        * (((-1 : K) ^ (n - j)
            * w ^ ((2 * j * (j + 1) : ℤ) - (n * (n + 2) : ℤ))) ^ 3
          * qInt (w ^ 2) (2 * j + 1))
      = ((-1 : K) ^ (n - j))
          * ((w ^ ((2 * j * (j + 1) : ℤ) - (n * (n + 2) : ℤ))) ^ 3
            * w ^ (-(3 : ℤ) * ((n : ℕ) * (n + 2) : ℤ)))
          * qInt (w ^ 2) (2 * j + 1) := by
        rw [mul_pow, hs]; ring
    _ = ((-1 : K) ^ n * (-1 : K) ^ j)
          * (w ^ (6 * (j * (j + 1))) * (w ^ (6 * (n * (n + 2))))⁻¹)
          * qInt (w ^ 2) (2 * j + 1) := by
        rw [hz, neg_one_pow_sub hjn]
    _ = (-1 : K) ^ n * (w ^ (6 * (n * (n + 2))))⁻¹
          * ((-1 : K) ^ j * w ^ (6 * (j * (j + 1)))
            * qInt (w ^ 2) (2 * j + 1)) := by
        ring

/-- The `[N+1]_{w²}` denominator is nonzero when `(w⁴)^N = 1` but
    `w⁴ ≠ 1` — its numerator vanishing would force `(w⁴)^{N+1} = 1`,
    hence `w⁴ = 1`. -/
private theorem qInt_succ_ne_zero {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) {N : ℕ}
    (hnext : ((w : K) ^ 4) ^ (N + 1) = 1 → (w : K) ^ 4 = 1) :
    qInt ((w : K) ^ 2) (N + 1) ≠ 0 := by
  intro h
  unfold qInt at h
  rcases div_eq_zero_iff.mp h with hnum | hden
  · have hY : ((w : K) ^ 2) ^ (N + 1) ≠ 0 :=
      pow_ne_zero _ (pow_ne_zero _ hw)
    have h1 : ((w : K) ^ 2) ^ (N + 1) * ((w : K) ^ 2) ^ (N + 1) = 1 := by
      have h2 := sub_eq_zero.mp hnum
      nth_rewrite 2 [h2]
      exact mul_inv_cancel₀ hY
    have h3 : ((w : K) ^ 4) ^ (N + 1) = 1 := by
      rw [show ((w : K) ^ 4) ^ (N + 1)
          = ((w : K) ^ 2) ^ (N + 1) * ((w : K) ^ 2) ^ (N + 1) by
        rw [← mul_pow]; congr 1; ring]
      exact h1
    have h4 := hnext h3
    apply hv
    have h5 : (w : K) ^ 2 * (w : K) ^ 2 = 1 := by
      rw [show (w : K) ^ 2 * (w : K) ^ 2 = w ^ 4 by ring, h4]
    rw [inv_eq_of_mul_eq_one_right h5]
    exact sub_self _
  · exact hv hden

/-- **Evaluation core B (proved): root-of-unity periodicity of the
    Rosso–Jones sum, previous slot.**  When `(w⁴)^N = 1` (but `w⁴ ≠ 1`)
    the tower value at the NEXT color is exactly `1` — the surviving term
    of the annihilation at the degenerate color `x = 1`.  Proved via the
    root evaluation `trP_sum_at_root_self`
    (`QOU.BraidKnot.AJTrefoilRootEval`: reflection + shift +
    Gauss-sum collapse); numerically pre-verified to 40 dps in
    `computations/aj_trefoil_telescope_assembly_check.py` [B core]. -/
theorem trefoil_eval_at_root_prev {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) {N : ℕ} (_hN : 1 ≤ N)
    (hroot : (w ^ 4) ^ N = 1) :
    coloredJonesTrefoil w (N + 1) = 1 := by
  have hsum : trP w N
      = (-1 : K) ^ N * w ^ (6 * (N * (N + 2))) * qInt (w ^ 2) (N + 1) :=
    trP_sum_at_root_self hw hv hroot
  have hq : qInt ((w : K) ^ 2) (N + 1) ≠ 0 := by
    refine qInt_succ_ne_zero hw hv fun h3 => ?_
    rw [pow_succ, hroot, one_mul] at h3
    exact h3
  rw [coloredJonesTrefoil_eq_P_form hw N, hsum, div_eq_iff hq, one_mul]
  have hee : (-1 : K) ^ N * (-1 : K) ^ N = 1 := by
    rw [← mul_pow]; norm_num
  have hE : (w : K) ^ (6 * (N * (N + 2))) ≠ 0 := pow_ne_zero _ hw
  calc (-1 : K) ^ N * ((w : K) ^ (6 * (N * (N + 2))))⁻¹
        * ((-1 : K) ^ N * w ^ (6 * (N * (N + 2))) * qInt ((w : K) ^ 2) (N + 1))
      = ((-1 : K) ^ N * (-1 : K) ^ N)
          * (((w : K) ^ (6 * (N * (N + 2))))⁻¹ * w ^ (6 * (N * (N + 2))))
          * qInt ((w : K) ^ 2) (N + 1) := by ring
    _ = qInt ((w : K) ^ 2) (N + 1) := by
        rw [hee, inv_mul_cancel₀ hE, one_mul, one_mul]

/-- **Evaluation core C (proved): root-of-unity periodicity, next slot.**
    When `(w⁴)^{N+1} = 1` (but `w⁴ ≠ 1`) the tower value at color `N` is
    exactly `1`.  Proved via the offset root evaluation
    `trP_sum_at_root_offset` (`QOU.BraidKnot.AJTrefoilRootEval`);
    numerically pre-verified to 40 dps ([C core]). -/
theorem trefoil_eval_at_root_next {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) {N : ℕ} (hN : 1 ≤ N)
    (hroot : (w ^ 4) ^ (N + 1) = 1) :
    coloredJonesTrefoil w N = 1 := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + 1 := ⟨N - 1, by omega⟩
  have hroot' : ((w : K) ^ 4) ^ (n + 2) = 1 := hroot
  have hsum : trP w n
      = (-1 : K) ^ n * w ^ (6 * (n * (n + 2))) * qInt (w ^ 2) (n + 1) :=
    trP_sum_at_root_offset hw hv hroot'
  have hq : qInt ((w : K) ^ 2) (n + 1) ≠ 0 := by
    refine qInt_succ_ne_zero hw hv fun h3 => ?_
    have h4 := hroot'
    rw [show n + 2 = n + 1 + 1 from rfl, pow_succ, h3, one_mul] at h4
    exact h4
  rw [coloredJonesTrefoil_eq_P_form hw n, hsum, div_eq_iff hq, one_mul]
  have hee : (-1 : K) ^ n * (-1 : K) ^ n = 1 := by
    rw [← mul_pow]; norm_num
  have hE : (w : K) ^ (6 * (n * (n + 2))) ≠ 0 := pow_ne_zero _ hw
  calc (-1 : K) ^ n * ((w : K) ^ (6 * (n * (n + 2))))⁻¹
        * ((-1 : K) ^ n * w ^ (6 * (n * (n + 2))) * qInt ((w : K) ^ 2) (n + 1))
      = ((-1 : K) ^ n * (-1 : K) ^ n)
          * (((w : K) ^ (6 * (n * (n + 2))))⁻¹ * w ^ (6 * (n * (n + 2))))
          * qInt ((w : K) ^ 2) (n + 1) := by ring
    _ = qInt ((w : K) ^ 2) (n + 1) := by
        rw [hee, inv_mul_cancel₀ hE, one_mul, one_mul]

/-! ## The assembled annihilation -/

section Assembly
set_option maxHeartbeats 1600000
set_option maxRecDepth 16384

/-- `w⁴ = 1` collapse: every `qInt (w²) k` is `0` (its denominator
    vanishes), hence every tower value is the junk `0`. -/
private theorem qInt_collapse {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ = 0) :
    ∀ k, qInt (w ^ 2) k = 0 := by
  intro k
  unfold qInt
  rw [hv, div_zero]

private theorem cJ_collapse {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ = 0) :
    ∀ M, coloredJonesTrefoil w M = 0 := by
  intro M
  simp only [coloredJonesTrefoil, qInt_collapse hv, div_zero]

private theorem w4_eq_one {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ = 0) : (w : K) ^ 4 = 1 := by
  have hw2 : (w : K) ^ 2 ≠ 0 := pow_ne_zero _ hw
  have h1 : (w : K) ^ 2 = ((w : K) ^ 2)⁻¹ := sub_eq_zero.mp hv
  have h2 : (w : K) ^ 2 * (w : K) ^ 2 = 1 := by
    nth_rewrite 2 [h1]
    exact mul_inv_cancel₀ hw2
  calc (w : K) ^ 4 = w ^ 2 * w ^ 2 := by ring
    _ = 1 := h2

/-- `[1]_{w²} = 1` when the denominator is nonzero. -/
private theorem qInt_one {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) :
    qInt (w ^ 2) 1 = 1 := by
  unfold qInt
  rw [pow_one]
  exact div_self hv

/-- `J(1) = 1` when `w⁴ ≠ 1`. -/
private theorem cJ_one {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) :
    coloredJonesTrefoil w 1 = 1 := by
  show w ^ (-(3 : ℤ) * ((0 : ℕ) * (0 + 2) : ℤ))
      * (∑ j ∈ Finset.range (0 + 1),
          (twistEigenvalue w 0 j) ^ 3 * qInt (w ^ 2) (2 * j + 1))
      / qInt (w ^ 2) 1 = 1
  rw [Finset.sum_range_one, qInt_one hv]
  unfold twistEigenvalue
  norm_num

/-- **The trefoil annihilation, assembled** — for every `w ≠ 0`, via the
    case split of the module docstring.  The generic case is the
    [C1]/[C2] computation; the degenerate colors route through the two
    cited evaluation cores. -/
theorem trefoilOperator_annihilates {w : K} (hw : w ≠ 0) :
    Annihilates (trefoilOperator (K := K)) (w ^ 4) (coloredJonesTrefoil w) := by
  intro N
  show ∑ j ∈ Finset.range (1 + 1),
      trCoeff j (w ^ 4) ((w ^ 4) ^ N) * coloredJonesTrefoil w (N + j)
    = trRhs (w ^ 4) ((w ^ 4) ^ N)
  rw [Finset.sum_range_succ, Finset.sum_range_one]
  by_cases hv : w ^ 2 - (w ^ 2)⁻¹ = 0
  · -- w⁴ = 1: all towers collapse to 0 and both sides vanish
    rw [cJ_collapse hv, cJ_collapse hv, w4_eq_one hw hv, one_pow]
    show trCoeff 0 1 1 * 0 + trCoeff 1 1 1 * 0 = trRhs 1 1
    simp [trCoeff, trRhs]
  · match N with
    | 0 =>
        have hJ0 : coloredJonesTrefoil w 0 = 0 := by
          show w ^ (-(3 : ℤ) * ((0 - 1 : ℕ) * (0 - 1 + 2) : ℤ))
              * (∑ j ∈ Finset.range ((0 - 1) + 1),
                  (twistEigenvalue w (0 - 1) j) ^ 3 * qInt (w ^ 2) (2 * j + 1))
              / qInt (w ^ 2) 0 = 0
          have h0 : qInt (w ^ 2) 0 = 0 := by
            unfold qInt
            norm_num
          rw [h0, div_zero]
        rw [pow_zero, show (0 + 0 : ℕ) = 0 from rfl,
          show (0 + 1 : ℕ) = 1 from rfl, hJ0, cJ_one hv]
        show trCoeff 0 (w ^ 4) 1 * 0 + trCoeff 1 (w ^ 4) 1 * 1
            = trRhs (w ^ 4) 1
        simp only [trCoeff, trRhs]
        norm_num
    | (M + 1) =>
        by_cases hxB : ((w : K) ^ 4) ^ (M + 1) = 1
        · -- degenerate slot B: a₀ vanishes at x = 1; J(M+2) = 1 by core B
          have hJ := trefoil_eval_at_root_prev hw hv (N := M + 1)
            (by omega) hxB
          rw [hxB, show (M + 1 + 1 : ℕ) = M + 2 from rfl, hJ]
          show trCoeff 0 (w ^ 4) 1 * coloredJonesTrefoil w (M + 1 + 0)
              + trCoeff 1 (w ^ 4) 1 * 1 = trRhs (w ^ 4) 1
          simp only [trCoeff, trRhs]
          norm_num
        · by_cases hxC : ((w : K) ^ 4) ^ (M + 1) * w ^ 4 = 1
          · -- degenerate slot C: a₁ vanishes at xq = 1; J(M+1) = 1 by core C
            have hroot : ((w : K) ^ 4) ^ (M + 1 + 1) = 1 := by
              rw [pow_succ]
              exact hxC
            have hJ := trefoil_eval_at_root_next hw hv (N := M + 1)
              (by omega) hroot
            rw [show (M + 1 + 0 : ℕ) = M + 1 from rfl, hJ]
            have hx : ((w : K) ^ 4) ^ (M + 1) ≠ 0 :=
              pow_ne_zero _ (pow_ne_zero _ hw)
            show trCoeff 0 (w ^ 4) ((w ^ 4) ^ (M + 1)) * 1
                + trCoeff 1 (w ^ 4) ((w ^ 4) ^ (M + 1))
                  * coloredJonesTrefoil w (M + 1 + 1)
              = trRhs (w ^ 4) ((w ^ 4) ^ (M + 1))
            simp only [trCoeff, trRhs]
            rw [hxC]
            have hx2 : (((w : K) ^ 4) ^ (M + 1)) ^ 2 * w ^ 4
                = ((w : K) ^ 4) ^ (M + 1) := by
              calc (((w : K) ^ 4) ^ (M + 1)) ^ 2 * w ^ 4
                  = ((w : K) ^ 4) ^ (M + 1)
                      * (((w : K) ^ 4) ^ (M + 1) * w ^ 4) := by ring
                _ = ((w : K) ^ 4) ^ (M + 1) := by rw [hxC, mul_one]
            rw [hx2, sub_self, mul_zero, neg_zero, zero_div, zero_mul,
              add_zero, mul_one]
            rw [div_eq_div_iff (pow_ne_zero _ hx) (pow_ne_zero _ hx)]
            linear_combination
              ((((w : K) ^ 4) ^ (M + 1) - 1)
                * (((w : K) ^ 4) ^ (M + 1)) ^ 4) * hxC
          · -- generic case A: the [C1]/[C2] computation
            have hw2 : (w : K) ^ 2 ≠ 0 := pow_ne_zero _ hw
            have hYne : ((w : K) ^ 2) ^ (M + 1) ≠ 0 := pow_ne_zero _ hw2
            have e1 : ((w : K) ^ 4) ^ (M + 1) = w ^ (4 * (M + 1)) :=
              (pow_mul w 4 (M + 1)).symm
            have hxY : ((w : K) ^ 4) ^ (M + 1)
                = (((w : K) ^ 2) ^ (M + 1)) ^ 2 := by
              rw [e1, ← pow_mul, ← pow_mul]
              congr 1
              ring
            have hnum1 : ((w : K) ^ 2) ^ (M + 1)
                - (((w : K) ^ 2) ^ (M + 1))⁻¹ ≠ 0 := by
              intro h
              apply hxB
              have h1 := sub_eq_zero.mp h
              have h2 : ((w : K) ^ 2) ^ (M + 1) * ((w : K) ^ 2) ^ (M + 1)
                  = 1 := by
                nth_rewrite 2 [h1]
                exact mul_inv_cancel₀ hYne
              rw [hxY, sq]
              exact h2
            have hnum2 : ((w : K) ^ 2) ^ (M + 1) * w ^ 2
                - (((w : K) ^ 2) ^ (M + 1) * w ^ 2)⁻¹ ≠ 0 := by
              intro h
              apply hxC
              have hY2 : ((w : K) ^ 2) ^ (M + 1) * w ^ 2 ≠ 0 :=
                mul_ne_zero hYne hw2
              have h1 := sub_eq_zero.mp h
              have h2 : (((w : K) ^ 2) ^ (M + 1) * w ^ 2)
                  * (((w : K) ^ 2) ^ (M + 1) * w ^ 2) = 1 := by
                nth_rewrite 2 [h1]
                exact mul_inv_cancel₀ hY2
              have e3 : ((w : K) ^ 4) ^ (M + 1) * w ^ 4
                  = (((w : K) ^ 2) ^ (M + 1) * w ^ 2)
                    * (((w : K) ^ 2) ^ (M + 1) * w ^ 2) := by
                rw [e1, show ((w : K) ^ 2) ^ (M + 1) = w ^ (2 * (M + 1))
                  from (pow_mul w 2 (M + 1)).symm]
                calc (w : K) ^ (4 * (M + 1)) * w ^ 4
                    = w ^ (4 * (M + 1) + 4) := by rw [← pow_add]
                  _ = w ^ (2 * (M + 1)) * w ^ 2
                      * (w ^ (2 * (M + 1)) * w ^ 2) := by
                      rw [← pow_add, ← pow_add]
                      congr 1
                      ring
              rw [e3]
              exact h2
            have hJ1 := coloredJonesTrefoil_eq_P_form hw M
            have hee : ((-1 : K)) ^ (M + 1) * ((-1 : K)) ^ (M + 1) = 1 := by
              rw [← mul_pow]
              norm_num
            have hJ2 : coloredJonesTrefoil w (M + 1 + 1)
                = ((-1 : K) ^ (M + 1) * (w ^ (6 * ((M + 1) * (M + 1 + 2))))⁻¹
                      * trP w M
                    + (w ^ (6 * ((M + 1) * (M + 1 + 2))))⁻¹
                      * (w ^ (6 * ((M + 1) * (M + 1 + 1)))
                        * qInt (w ^ 2) (2 * (M + 1) + 1)))
                  / qInt (w ^ 2) (M + 1 + 1) := by
              rw [coloredJonesTrefoil_eq_P_form hw (M + 1), trP_succ]
              congr 1
              linear_combination
                ((w ^ (6 * ((M + 1) * (M + 1 + 2))))⁻¹
                  * (w ^ (6 * ((M + 1) * (M + 1 + 1)))
                    * qInt (w ^ 2) (2 * (M + 1) + 1))) * hee
            have b1 : (w : K) ^ (6 * ((M + 1) * (M + 1 + 2)))
                = w ^ (6 * (M * (M + 2))) * (((w : K) ^ 2) ^ (M + 1)) ^ 6
                  * w ^ 6 := by
              rw [show (((w : K) ^ 2) ^ (M + 1)) ^ 6 = w ^ (2 * (M + 1) * 6)
                from by rw [← pow_mul, ← pow_mul]; congr 1; ring,
                ← pow_add, ← pow_add]
              congr 1
              ring
            have b2 : (w : K) ^ (6 * ((M + 1) * (M + 1 + 1)))
                = w ^ (6 * (M * (M + 2))) * (((w : K) ^ 2) ^ (M + 1)) ^ 3
                  * w ^ 6 := by
              rw [show (((w : K) ^ 2) ^ (M + 1)) ^ 3 = w ^ (2 * (M + 1) * 3)
                from by rw [← pow_mul, ← pow_mul]; congr 1; ring,
                ← pow_add, ← pow_add]
              congr 1
              ring
            have u1 : qInt ((w : K) ^ 2) (M + 1)
                = (((w : K) ^ 2) ^ (M + 1) - (((w : K) ^ 2) ^ (M + 1))⁻¹)
                  / (w ^ 2 - (w ^ 2)⁻¹) := rfl
            have u2 : qInt ((w : K) ^ 2) (M + 1 + 1)
                = (((w : K) ^ 2) ^ (M + 1) * w ^ 2
                    - (((w : K) ^ 2) ^ (M + 1) * w ^ 2)⁻¹)
                  / (w ^ 2 - (w ^ 2)⁻¹) := by
              unfold qInt
              rw [pow_succ]
            have u3 : qInt ((w : K) ^ 2) (2 * (M + 1) + 1)
                = ((((w : K) ^ 2) ^ (M + 1)) ^ 2 * w ^ 2
                    - ((((w : K) ^ 2) ^ (M + 1)) ^ 2 * w ^ 2)⁻¹)
                  / (w ^ 2 - (w ^ 2)⁻¹) := by
              unfold qInt
              rw [show ((w : K) ^ 2) ^ (2 * (M + 1) + 1)
                  = (((w : K) ^ 2) ^ (M + 1)) ^ 2 * w ^ 2 from by
                rw [show (((w : K) ^ 2) ^ (M + 1)) ^ 2 = w ^ (2 * (M + 1) * 2)
                  from by rw [← pow_mul, ← pow_mul]; congr 1; ring,
                  ← pow_mul, ← pow_add]
                congr 1
                ring]
            -- the nonzero facts in the shapes field_simp's normal form uses
            have hda : (w : K) ^ 4 * w ^ (M * 4) - 1 ≠ 0 := by
              intro h
              apply hxB
              have hsh : ((w : K) ^ 4) ^ (M + 1) = w ^ 4 * w ^ (M * 4) := by
                rw [e1, ← pow_add]
                congr 1
                ring
              rw [hsh]
              linear_combination h
            have hdb : (w : K) ^ 8 * w ^ (M * 4) - 1 ≠ 0 := by
              intro h
              apply hxC
              have hsh : ((w : K) ^ 4) ^ (M + 1) * w ^ 4
                  = w ^ 8 * w ^ (M * 4) := by
                rw [e1, ← pow_add, ← pow_add]
                congr 1
                ring
              rw [hsh]
              linear_combination h
            have hdc : (w : K) ^ 4 - 1 ≠ 0 := by
              intro h
              apply hv
              have hsplit : (w : K) ^ 2 - ((w : K) ^ 2)⁻¹
                  = ((w : K) ^ 4 - 1) * ((w : K) ^ 2)⁻¹ := by
                field_simp
              rw [hsplit, h, zero_mul]
            have hga : (((w : K) ^ 2) ^ (M + 1)) ^ 2 - 1 ≠ 0 := by
              intro h
              apply hxB
              rw [hxY]
              linear_combination h
            have hgb : (w : K) ^ 4 * (((w : K) ^ 2) ^ (M + 1)) ^ 2 - 1 ≠ 0 := by
              intro h
              apply hxC
              rw [hxY]
              linear_combination h
            rw [show (M + 1 + 0 : ℕ) = M + 1 from rfl, hJ1, hJ2, hxY]
            simp only [trCoeff, trRhs]
            rw [u1, u2, u3, b1, b2, pow_succ (-1 : K) M]
            field_simp [hda, hdb, hdc, hga, hgb]
            ring

end Assembly

/-! ## The instance -/

/-- **Strong AJ for the trefoil — fully proved.**  The annihilation
    routes through the assembled case-split proof; the two root-of-unity
    evaluation cores (`trefoil_eval_at_root_prev`/`_next`) are discharged
    by `QOU.BraidKnot.AJTrefoilRootEval`, so no `sorry` remains anywhere
    in the trefoil strong-AJ chain. -/
instance [CharZero K] : StrongAJTrefoil K where
  op := trefoilOperator
  order_eq := rfl
  nontrivial := fun _ hq => trefoilOperator_nontrivial hq
  annihilates := fun _ hw => trefoilOperator_annihilates hw
  unit := trUnit
  unit_nondegenerate := trUnit_nondegenerate
  specializes := trefoilOperator_specializes

end QOU.BraidKnot.AJTrefoil
