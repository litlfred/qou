import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# Thomae–Jackson Geometric-Grid `q`-Calculus Infrastructure

Over an arbitrary field `R` (§7c generic base-ring discipline, zero `ℝ`), this module provides
reusable forward and backward discrete `q`-calculus on geometric grids `t_k = t₀ * r^k`
(crediting Johannes Thomae 1869 and Frank Hilton Jackson 1910):

1. **Geometric Grid & Step Weights (`geomGrid`, `fwdStep`, `bwdStep`):**
   Forward step `(r - 1) * t_k = t_{k+1} - t_k` and backward step `(1 - r⁻¹) * t_k`, satisfying
   the exact pointwise ratio `bwdStep t₀ r k = r⁻¹ * fwdStep t₀ r k` (`bwdStep_eq_inv_mul_fwdStep`).
2. **Forward & Backward `q`-Derivatives and `q`-Leibniz Product Rules:**
   `qDerivFwd` and `qDerivBwd`, together with unconditional `q`-Leibniz product rules
   (`qDeriv_fwd_mul`, `qDeriv_fwd_mul_symm`, `qDeriv_bwd_mul`).
3. **Both Fundamental Theorems of `q`-Calculus:**
   - `qIntegral_fwd_qDeriv_fwd`: `qIntegralFwd t₀ r N (qDerivFwd r F) = F (t₀ * r^N) - F t₀`.
   - `qIntegral_bwd_qDeriv_bwd`: `qIntegralBwd (r * t₀) r N (qDerivBwd r F) = F (t₀ * r^N) - F t₀`
     (and unshifted `N + 1` form `qIntegral_bwd_qDeriv_bwd_succ`).
4. **Universal Backward-to-Forward Scaling (`qIntegral_bwd_eq_inv_mul_fwd`):**
   `qIntegralBwd t₀ r N f = r⁻¹ * qIntegralFwd t₀ r N f` for **every** integrand `f : R → R`,
   specializing on the proper-time lattice `r = q²` to `q⁻¹ ^ 2 * qIntegralFwd t₀ (q²) N f`
   (`qIntegral_bwd_qSq_eq_q_inv_sq_mul_fwd`).
-/

namespace QOU.MathlibInfra.ThomaeJacksonCalculus

open BigOperators

section CommRingGrid

variable {R : Type*} [CommRing R]

/-- Geometric grid `t_k = t₀ * r^k` (`k : ℕ`). -/
def geomGrid (t0 r : R) (k : ℕ) : R :=
  t0 * r ^ k

/-- Forward geometric step weight `Δ_+ t_k = (r - 1) * t_k`. -/
def fwdStep (t0 r : R) (k : ℕ) : R :=
  (r - 1) * geomGrid t0 r k

theorem geomGrid_zero (t0 r : R) : geomGrid t0 r 0 = t0 := by
  simp [geomGrid]

theorem geomGrid_succ (t0 r : R) (k : ℕ) :
    geomGrid t0 r (k + 1) = r * geomGrid t0 r k := by
  simp only [geomGrid, pow_succ]
  ring

/-- Forward step equals the adjacent grid difference `t_{k+1} - t_k`. -/
theorem fwdStep_eq_sub (t0 r : R) (k : ℕ) :
    fwdStep t0 r k = geomGrid t0 r (k + 1) - geomGrid t0 r k := by
  rw [fwdStep, geomGrid_succ]
  ring

/-- Telescoping sum of forward step weights over `Finset.range N`:
`∑_{k < N} (r - 1) * (t₀ * r^k) = t₀ * r^N - t₀`. -/
theorem sum_fwdStep_eq (t0 r : R) (N : ℕ) :
    (∑ k ∈ Finset.range N, fwdStep t0 r k) = geomGrid t0 r N - t0 := by
  induction N with
  | zero => simp [geomGrid]
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, fwdStep_eq_sub]
    ring

end CommRingGrid

section FieldCalculus

variable {R : Type*} [Field R]

/-- Backward geometric step weight `Δ_- t_k = (1 - r⁻¹) * t_k`. -/
def bwdStep (t0 r : R) (k : ℕ) : R :=
  (1 - r⁻¹) * geomGrid t0 r k

/-- Backward step equals `t_k - r⁻¹ * t_k` (`t_k - t_{k-1}`). -/
theorem bwdStep_eq_sub (t0 r : R) (k : ℕ) :
    bwdStep t0 r k = geomGrid t0 r k - r⁻¹ * geomGrid t0 r k := by
  unfold bwdStep
  ring

/-- **Pointwise Backward-to-Forward Step Scaling:**
Whenever `r ≠ 0`, `(1 - r⁻¹) * t_k = r⁻¹ * ((r - 1) * t_k)`. -/
theorem bwdStep_eq_inv_mul_fwdStep (t0 : R) {r : R} (hr : r ≠ 0) (k : ℕ) :
    bwdStep t0 r k = r⁻¹ * fwdStep t0 r k := by
  unfold bwdStep fwdStep
  have hri : r⁻¹ * r = 1 := inv_mul_cancel₀ hr
  linear_combination geomGrid t0 r k * hri.symm

/-- Telescoping sum of backward step weights over `Finset.range N`:
`∑_{k < N} (1 - r⁻¹) * (t₀ * r^k) = r⁻¹ * (t₀ * r^N - t₀)`. -/
theorem sum_bwdStep_eq (t0 : R) {r : R} (hr : r ≠ 0) (N : ℕ) :
    (∑ k ∈ Finset.range N, bwdStep t0 r k) = r⁻¹ * (geomGrid t0 r N - t0) := by
  calc
    (∑ k ∈ Finset.range N, bwdStep t0 r k)
        = ∑ k ∈ Finset.range N, r⁻¹ * fwdStep t0 r k := by
          refine Finset.sum_congr rfl fun k _ => bwdStep_eq_inv_mul_fwdStep t0 hr k
    _ = r⁻¹ * ∑ k ∈ Finset.range N, fwdStep t0 r k := by rw [← Finset.mul_sum]
    _ = r⁻¹ * (geomGrid t0 r N - t0) := by rw [sum_fwdStep_eq]

/-- Forward `q`-difference derivative `(D_{r,+} F)(x) = (F(r * x) - F(x)) / ((r - 1) * x)`. -/
def qDerivFwd (r : R) (F : R → R) (x : R) : R :=
  (F (r * x) - F x) / ((r - 1) * x)

/-- Backward `q`-difference derivative `(D_{r,-} F)(x) = (F(x) - F(r⁻¹ * x)) / ((1 - r⁻¹) * x)`. -/
def qDerivBwd (r : R) (F : R → R) (x : R) : R :=
  (F x - F (r⁻¹ * x)) / ((1 - r⁻¹) * x)

/-- Finite forward Thomae–Jackson `q`-integral on `t_0, ..., t_{N-1}`:
`I_{r,+}^{[t₀, N]}(f) = ∑_{k < N} f(t₀ * r^k) * ((r - 1) * t₀ * r^k)`. -/
def qIntegralFwd (t0 r : R) (N : ℕ) (f : R → R) : R :=
  ∑ k ∈ Finset.range N, f (geomGrid t0 r k) * fwdStep t0 r k

/-- Finite backward Thomae–Jackson `q`-integral on `t_0, ..., t_{N-1}`:
`I_{r,-}^{[t₀, N]}(f) = ∑_{k < N} f(t₀ * r^k) * ((1 - r⁻¹) * t₀ * r^k)`. -/
def qIntegralBwd (t0 r : R) (N : ℕ) (f : R → R) : R :=
  ∑ k ∈ Finset.range N, f (geomGrid t0 r k) * bwdStep t0 r k

/-- **Forward `q`-Leibniz Product Rule:**
`D_{r,+}(F * G)(x) = D_{r,+} F(x) * G(x) + F(r * x) * D_{r,+} G(x)`. -/
theorem qDeriv_fwd_mul (r : R) (F G : R → R) (x : R) :
    qDerivFwd r (fun y => F y * G y) x =
      qDerivFwd r F x * G x + F (r * x) * qDerivFwd r G x := by
  unfold qDerivFwd
  rw [div_mul_eq_mul_div, mul_div_assoc', ← add_div]
  congr 1
  ring

/-- Symmetric forward `q`-Leibniz product rule:
`D_{r,+}(F * G)(x) = F(x) * D_{r,+} G(x) + D_{r,+} F(x) * G(r * x)`. -/
theorem qDeriv_fwd_mul_symm (r : R) (F G : R → R) (x : R) :
    qDerivFwd r (fun y => F y * G y) x =
      F x * qDerivFwd r G x + qDerivFwd r F x * G (r * x) := by
  unfold qDerivFwd
  rw [mul_div_assoc', div_mul_eq_mul_div, ← add_div]
  congr 1
  ring

/-- **Backward `q`-Leibniz Product Rule:**
`D_{r,-}(F * G)(x) = D_{r,-} F(x) * G(x) + F(r⁻¹ * x) * D_{r,-} G(x)`. -/
theorem qDeriv_bwd_mul (r : R) (F G : R → R) (x : R) :
    qDerivBwd r (fun y => F y * G y) x =
      qDerivBwd r F x * G x + F (r⁻¹ * x) * qDerivBwd r G x := by
  unfold qDerivBwd
  rw [div_mul_eq_mul_div, mul_div_assoc', ← add_div]
  congr 1
  ring

/-- **Universal Backward-to-Forward Thomae–Jackson Scaling (`I_{r,-} = r⁻¹ * I_{r,+}`):**
For every `r ≠ 0`, `N : ℕ`, and `f : R → R`,
`qIntegralBwd t₀ r N f = r⁻¹ * qIntegralFwd t₀ r N f`. -/
theorem qIntegral_bwd_eq_inv_mul_fwd (t0 : R) {r : R} (hr : r ≠ 0) (N : ℕ) (f : R → R) :
    qIntegralBwd t0 r N f = r⁻¹ * qIntegralFwd t0 r N f := by
  unfold qIntegralBwd qIntegralFwd
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [bwdStep_eq_inv_mul_fwdStep t0 hr k]
  ring

/-- Proper-time lattice specialization (`r = q²`): every backward Jackson sum carries an exact
overall `q⁻²` factor relative to the forward Jackson sum on the same nodes. -/
theorem qIntegral_bwd_qSq_eq_q_inv_sq_mul_fwd (t0 : R) {q : R} (hq : q ≠ 0) (N : ℕ)
    (f : R → R) :
    qIntegralBwd t0 (q ^ 2) N f = q⁻¹ ^ 2 * qIntegralFwd t0 (q ^ 2) N f := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  rw [qIntegral_bwd_eq_inv_mul_fwd t0 hq2 N f, inv_pow]

/-- **Forward Fundamental Theorem of `q`-Calculus:**
Whenever `t₀ ≠ 0`, `r ≠ 0`, and `r ≠ 1`,
`qIntegralFwd t₀ r N (qDerivFwd r F) = F (geomGrid t₀ r N) - F t₀`. -/
theorem qIntegral_fwd_qDeriv_fwd {t0 r : R} (ht0 : t0 ≠ 0) (hr : r ≠ 0) (hr1 : r ≠ 1)
    (N : ℕ) (F : R → R) :
    qIntegralFwd t0 r N (qDerivFwd r F) = F (geomGrid t0 r N) - F t0 := by
  induction N with
  | zero => simp [qIntegralFwd, geomGrid]
  | succ n ih =>
    rw [qIntegralFwd] at ih ⊢
    rw [Finset.sum_range_succ, ih]
    have hgrid_ne : geomGrid t0 r n ≠ 0 := mul_ne_zero ht0 (pow_ne_zero n hr)
    have hstep_ne : (r - 1) * geomGrid t0 r n ≠ 0 := mul_ne_zero (sub_ne_zero.mpr hr1) hgrid_ne
    have hterm : qDerivFwd r F (geomGrid t0 r n) * fwdStep t0 r n =
        F (geomGrid t0 r (n + 1)) - F (geomGrid t0 r n) := by
      unfold qDerivFwd fwdStep
      rw [div_mul_cancel₀ _ hstep_ne, geomGrid_succ]
    rw [hterm]
    ring

/-- **Backward Fundamental Theorem of `q`-Calculus (Interval `[t₀, t₀ * r^N]`):**
Whenever `t₀ ≠ 0`, `r ≠ 0`, and `r ≠ 1`, summing `qDerivBwd r F` over the upper-endpoint
grid `r * t₀, r² * t₀, ..., r^N * t₀` recovers `F (geomGrid t₀ r N) - F t₀`. -/
theorem qIntegral_bwd_qDeriv_bwd {t0 r : R} (ht0 : t0 ≠ 0) (hr : r ≠ 0) (hr1 : r ≠ 1)
    (N : ℕ) (F : R → R) :
    qIntegralBwd (r * t0) r N (qDerivBwd r F) = F (geomGrid t0 r N) - F t0 := by
  have h1r : 1 - r⁻¹ ≠ 0 := by
    intro h0
    have hinv1 : r⁻¹ = 1 := (sub_eq_zero.mp h0).symm
    apply hr1
    calc
      r = r * 1 := (mul_one r).symm
      _ = r * r⁻¹ := by rw [hinv1]
      _ = 1 := mul_inv_cancel₀ hr
  induction N with
  | zero => simp [qIntegralBwd, geomGrid]
  | succ n ih =>
    rw [qIntegralBwd] at ih ⊢
    rw [Finset.sum_range_succ, ih]
    have hgrid_shift : geomGrid (r * t0) r n = geomGrid t0 r (n + 1) := by
      simp only [geomGrid, pow_succ]
      ring
    have hgrid_ne : geomGrid (r * t0) r n ≠ 0 :=
      mul_ne_zero (mul_ne_zero hr ht0) (pow_ne_zero n hr)
    have hstep_ne : (1 - r⁻¹) * geomGrid (r * t0) r n ≠ 0 := mul_ne_zero h1r hgrid_ne
    have hprev : r⁻¹ * geomGrid (r * t0) r n = geomGrid t0 r n := by
      simp only [geomGrid]
      calc
        r⁻¹ * (r * t0 * r ^ n) = (r⁻¹ * r) * (t0 * r ^ n) := by ring
        _ = 1 * (t0 * r ^ n) := by rw [inv_mul_cancel₀ hr]
        _ = t0 * r ^ n := one_mul _
    have hterm : qDerivBwd r F (geomGrid (r * t0) r n) * bwdStep (r * t0) r n =
        F (geomGrid t0 r (n + 1)) - F (geomGrid t0 r n) := by
      unfold qDerivBwd bwdStep
      rw [div_mul_cancel₀ _ hstep_ne, hprev, hgrid_shift]
    rw [hterm]
    ring

/-- Unshifted `N + 1`-node backward Fundamental Theorem of `q`-Calculus on `t₀, ..., t₀ * r^N`:
`qIntegralBwd t₀ r (N + 1) (qDerivBwd r F) = F (geomGrid t₀ r N) - F (r⁻¹ * t₀)`. -/
theorem qIntegral_bwd_qDeriv_bwd_succ {t0 r : R} (ht0 : t0 ≠ 0) (hr : r ≠ 0) (hr1 : r ≠ 1)
    (N : ℕ) (F : R → R) :
    qIntegralBwd t0 r (N + 1) (qDerivBwd r F) = F (geomGrid t0 r N) - F (r⁻¹ * t0) := by
  have ht0' : r⁻¹ * t0 ≠ 0 := mul_ne_zero (inv_ne_zero hr) ht0
  have hmul : r * (r⁻¹ * t0) = t0 := by
    rw [← mul_assoc, mul_inv_cancel₀ hr, one_mul]
  have hmain := qIntegral_bwd_qDeriv_bwd ht0' hr hr1 (N + 1) F
  rw [hmul] at hmain
  have hend : geomGrid (r⁻¹ * t0) r (N + 1) = geomGrid t0 r N := by
    simp only [geomGrid, pow_succ]
    calc
      r⁻¹ * t0 * (r ^ N * r) = (r * (r⁻¹ * t0)) * r ^ N := by ring
      _ = t0 * r ^ N := by rw [hmul]
  rw [hend] at hmain
  exact hmain

end FieldCalculus

end QOU.MathlibInfra.ThomaeJacksonCalculus
