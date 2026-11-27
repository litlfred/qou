import CompactQuantumMetrics.PickKernelSOS
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
# The Haar moment kernels of `O_q(SU(2))` are weighted sums of squares

Over a linearly ordered field with `0 < q < 1`, everything here is a finite identity
between rational functions of `q`: no series, no limits.

* `lamQ q k = (1 - q²) (-q)^k / (1 - q^(2(k+1)))` are Woronowicz's Haar moments
  `h((βγ)^k)`.
* `GV q d` and `GW q a` are the moments twisted by `α^d δ^d = ∏ (1 + q^(2s+1) ζ)` and
  `δ^a α^a = ∏ (1 + q^(-(2s+1)) ζ)`, defined by the one-step recursions those products
  give. `GV_closed` and `GW_closed` give their closed forms: a positive constant times
  `(-q)^k` (times `q^(2ak)`) over `denQ q (d+1) k = ∏_{m ≤ d} (1 - q^(2(k+1+m)))`.
* `isWSOS_qPick`: for `c₀ ≥ 0` and any `ρ`, the kernel
  `(i, j) ↦ c₀ ρ^(i+j) / denQ q A (i+j+n)` is a weighted sum of squares on every finite
  set of indices. It is a Hadamard product of `A` Pick kernels at the points
  `q^(n+m+2i+1)`, rescaled.
* `lamQ_quadForm_nonneg`: `∑ cᵢ cⱼ λ_{i+j} ≥ 0`, i.e. `h(f(ζ)²) ≥ 0` on the
  weight-zero part.
-/

namespace QOU.AlgebraicSubstrate.HaarKernel

open Finset QOU.AlgebraicSubstrate.PickSOS

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Haar moments `λ_k = (1 - q²) (-q)^k / (1 - q^(2(k+1)))`. -/
def lamQ (q : K) (k : ℕ) : K := (1 - q ^ 2) * (-q) ^ k / (1 - q ^ (2 * (k + 1)))

/-- `∏_{s < d} (1 - q^(2(s+1)))`. -/
def pochQ (q : K) (d : ℕ) : K := ∏ s ∈ range d, (1 - q ^ (2 * (s + 1)))

/-- `∏_{m < A} (1 - q^(2(k+1+m)))`. -/
def denQ (q : K) (A k : ℕ) : K := ∏ m ∈ range A, (1 - q ^ (2 * (k + 1 + m)))

/-- Moments twisted by `α^d δ^d`: `GV (d+1) k = GV d k + q^(2d+1) GV d (k+1)`. -/
def GV (q : K) : ℕ → ℕ → K
  | 0, k => lamQ q k
  | d + 1, k => GV q d k + q ^ (2 * d + 1) * GV q d (k + 1)

/-- Moments twisted by `δ^a α^a`: `GW (a+1) k = GW a k + q^(-(2a+1)) GW a (k+1)`. -/
def GW (q : K) : ℕ → ℕ → K
  | 0, k => lamQ q k
  | a + 1, k => GW q a k + (q ^ (2 * a + 1))⁻¹ * GW q a (k + 1)

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem denQ_succ {q : K} (A k : ℕ) :
    denQ q (A + 1) k = denQ q A k * (1 - q ^ (2 * (k + 1 + A))) := prod_range_succ _ _

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem denQ_succ' {q : K} (A k : ℕ) :
    denQ q (A + 1) k = denQ q A (k + 1) * (1 - q ^ (2 * (k + 1))) := by
  rw [denQ, prod_range_succ', denQ]
  congr 1
  refine prod_congr rfl fun m _ => ?_
  ring_nf

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem pochQ_succ {q : K} (d : ℕ) :
    pochQ q (d + 1) = pochQ q d * (1 - q ^ (2 * (d + 1))) := prod_range_succ _ _

section Pos

variable {q : K} (hq0 : 0 < q) (hq1 : q < 1)
include hq0 hq1

theorem pow_lt_one' {e : ℕ} (he : e ≠ 0) : q ^ e < 1 := pow_lt_one₀ hq0.le hq1 he

theorem one_sub_pow_pos {e : ℕ} (he : e ≠ 0) : 0 < 1 - q ^ e :=
  sub_pos.2 (pow_lt_one' hq0 hq1 he)

theorem denQ_pos (A k : ℕ) : 0 < denQ q A k :=
  prod_pos fun m _ => one_sub_pow_pos hq0 hq1 (by omega)

theorem pochQ_pos (d : ℕ) : 0 < pochQ q d :=
  prod_pos fun s _ => one_sub_pow_pos hq0 hq1 (by omega)

theorem GV_closed (d k : ℕ) :
    GV q d k = (1 - q ^ 2) * pochQ q d * (-q) ^ k / denQ q (d + 1) k := by
  induction d generalizing k with
  | zero => simp [GV, lamQ, pochQ, denQ]
  | succ d ih =>
    rw [GV, ih, ih, pochQ_succ]
    have h1 := denQ_pos hq0 hq1 (d + 1) k
    have h3 := one_sub_pow_pos hq0 hq1 (e := 2 * (k + 1 + (d + 1))) (by omega)
    have h4 := one_sub_pow_pos hq0 hq1 (e := 2 * (k + 1)) (by omega)
    have e2 := denQ_succ' (q := q) (d + 1) k
    rw [denQ_succ] at e2
    have : denQ q (d + 1) (k + 1) = denQ q (d + 1) k * (1 - q ^ (2 * (k + 1 + (d + 1)))) /
        (1 - q ^ (2 * (k + 1))) := by rw [e2]; field_simp
    rw [this, denQ_succ (d + 1) k]
    generalize denQ q (d + 1) k = D at *
    field_simp
    ring

theorem GW_closed (a k : ℕ) :
    GW q a k = (1 - q ^ 2) * q ^ (2 * a) * pochQ q a * (-q) ^ k * q ^ (2 * a * k) /
      denQ q (a + 1) k := by
  induction a generalizing k with
  | zero => simp [GW, lamQ, pochQ, denQ]
  | succ a ih =>
    rw [GW, ih, ih, pochQ_succ]
    have h1 := denQ_pos hq0 hq1 (a + 1) k
    have h3 := one_sub_pow_pos hq0 hq1 (e := 2 * (k + 1 + (a + 1))) (by omega)
    have h4 := one_sub_pow_pos hq0 hq1 (e := 2 * (k + 1)) (by omega)
    have hq := hq0.ne'
    have e2 := denQ_succ' (q := q) (a + 1) k
    rw [denQ_succ] at e2
    have : denQ q (a + 1) (k + 1) = denQ q (a + 1) k * (1 - q ^ (2 * (k + 1 + (a + 1)))) /
        (1 - q ^ (2 * (k + 1))) := by rw [e2]; field_simp
    rw [this, denQ_succ (a + 1) k]
    generalize denQ q (a + 1) k = D at *
    field_simp
    ring

/-- `c₀ ρ^(i+j) / ∏_{m<A} (1 - q^(2(i+j+n+1+m)))` is a weighted sum of squares. -/
theorem isWSOS_qPick (s : Finset ℕ) (A n : ℕ) (ρ : K) {c₀ : K} (hc₀ : 0 ≤ c₀) :
    IsWSOS s fun i j => c₀ * ρ ^ (i + j) / denQ q A (i + j + n) := by
  have hX : ∀ m, ∀ i ∈ s, |q ^ (n + m + 2 * i + 1)| < 1 := fun m i _ => by
    rw [abs_of_pos (pow_pos hq0 _)]
    exact pow_lt_one' hq0 hq1 (by omega)
  have hP := IsWSOS.prod (range A) fun m _ =>
    isWSOS_pick (fun i => q ^ (n + m + 2 * i + 1)) s (hX m)
  refine ((hP.outer fun i => ρ ^ i).const_mul hc₀).congr_on fun i _ j _ => ?_
  simp only [denQ, one_div]
  rw [div_eq_mul_inv, ← prod_inv_distrib, pow_add]
  have : ∀ m ∈ range A, (1 - q ^ (n + m + 2 * i + 1) * q ^ (n + m + 2 * j + 1))⁻¹ =
      (1 - q ^ (2 * (i + j + n + 1 + m)))⁻¹ := fun m _ => by
    rw [← pow_add]; ring_nf
  rw [prod_congr rfl this]
  ring

/-- **Weight-zero positivity**: `∑ cᵢ cⱼ λ_{i+j} ≥ 0`. -/
theorem lamQ_quadForm_nonneg (s : Finset ℕ) (c : ℕ → K) :
    0 ≤ ∑ i ∈ s, ∑ j ∈ s, c i * c j * lamQ q (i + j) := by
  have h := isWSOS_qPick hq0 hq1 s 1 0 (-q) (c₀ := 1 - q ^ 2)
    (one_sub_pow_pos hq0 hq1 (by norm_num)).le
  refine (h.congr_on fun i _ j _ => ?_).quadForm_nonneg c
  simp [lamQ, denQ, mul_div_assoc]

end Pos

end QOU.AlgebraicSubstrate.HaarKernel
