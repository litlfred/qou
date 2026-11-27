import QCalculus.HabiroCyclotomicSeries
import QCalculus.HabiroTailStar

/-!
# QCalculus.HabiroDoubleTwist — Kashaev elements of all double twist knots

Bean `qou-28qh`, phase 2 (twist knots via Masbaum, extended to the double twist
family). Over any commutative ring `R`.

## The source formula (cited, not formalized)

For positive integers `m, p`, Lauridsen's cyclotomic expansion (from Habiro and
Masbaum [masbaum2003]), as quoted by Lovejoy–Osburn [lovejoy-osburn,
eqs. (1.1), (1.2)], is

  `J_N(K_(m,p); q) = ∑_{n ≥ 0} (q^{1+N})_n (q^{1-N})_n · q^n · C_m(n) · C_p(n)`,
  `J_N(K_(m,-p); q) = ∑_{n ≥ 0} (q^{1+N})_n (q^{1-N})_n · (-1)^n q^{-n(n+1)/2} · C_m(n) · D_p(n)`,

with the chain sums

  `C_m(n) = ∑_{n = n_m ≥ ⋯ ≥ n_1 ≥ 0} ∏_{i<m} q^{n_i² + n_i} [n_{i+1}; n_i]`,
  `D_p(n) = ∑_{n = s_p ≥ ⋯ ≥ s_1 ≥ 0} ∏_{j<p} q^{-s_j - s_{j+1} s_j} [s_{j+1}; s_j]`.

`K_(1,p)` is the twist knot `K_p`; `K_(1,1)` is a trefoil and `K_(1,-1)` is the
figure-eight. The mirror `q ↦ q⁻¹` covers the remaining signs.

At `q = ζ_N` (a primitive `N`-th root) both `(q^{1±N})_n` become `(ζ;ζ)_n`, so
the Kashaev invariant is the value at `ζ` of the single Habiro element

  `∑_n H_n(q) (q;q)_n (q;q)_n`,

where `H_n` is the coefficient above. This file defines those elements and
proves their algebra. That they equal the colored Jones values is the cited
theorem, not a claim of this file.

## What is proved (sorry-free, any `CommRing R`)

* `chainPos`, `chainNeg`: the chain sums by their one-step recursions, with
  Gaussian binomials `gaussBinom q` (from `QCalculus.HabiroTailStar`).
* `doubleTwistPos m p`, `doubleTwistNeg m p`: elements of `R̂[q]` (indices
  shifted by one: `m = 0` is the paper's `m = 1`).
* `poch_qInv`: `(q⁻¹;q⁻¹)_n = (-1)^n q^{-n(n+1)/2} (q;q)_n`.
* `doubleTwistNeg_zero_zero`: `K_(1,-1)` is `figureEight` of
  `HabiroCyclotomicSeries`, an independent non-vacuity check of the two files.
* `evalRoot_doubleTwistPos`, `evalRoot_doubleTwistNeg`: the Kashaev sums
  `∑_{n<N} H_n(ζ) (ζ;ζ)_n²`, finite and algebraic.

No analytic API, no empirical value.

-- Ref: [masbaum2003]
-- Ref: [lovejoy-osburn]
-- Ref: [habiro2004cyclotomic]
-/

namespace QCalculus.HabiroSeries

open Polynomial Finset QOU.QBeta.HabiroTailStar

variable {R : Type*} [CommRing R]

/-- Gaussian binomials commute with ring maps. -/
theorem map_gaussBinom {A B : Type*} [CommRing A] [CommRing B] (f : A →+* B) (x : A) :
    ∀ n k : ℕ, f (gaussBinom x n k) = gaussBinom (f x) n k
  | 0, 0 => by simp
  | 0, k + 1 => by simp
  | n + 1, 0 => by simp [gaussBinom]
  | n + 1, k + 1 => by
    simp only [gaussBinom, map_add, map_mul, map_pow, map_gaussBinom f x n k,
      map_gaussBinom f x n (k + 1)]

/-- The positive chain sum `C_{m+1}(n)`:
    `C_1 = 1`, `C_{m+2}(n) = ∑_{j ≤ n} q^{j²+j} [n; j] C_{m+1}(j)`. -/
noncomputable def chainPos : ℕ → ℕ → Habiro R
  | 0, _ => 1
  | m + 1, n => ∑ j ∈ range (n + 1), q ^ (j ^ 2 + j) * gaussBinom q n j * chainPos m j

/-- The negative chain sum `D_{p+1}(n)`:
    `D_1 = 1`, `D_{p+2}(n) = ∑_{j ≤ n} q^{-j-nj} [n; j] D_{p+1}(j)`. -/
noncomputable def chainNeg : ℕ → ℕ → Habiro R
  | 0, _ => 1
  | p + 1, n => ∑ j ∈ range (n + 1), qInv ^ (j + n * j) * gaussBinom q n j * chainNeg p j

/-- `H_n` for `K_(m+1, p+1)`: `q^n C_{m+1}(n) C_{p+1}(n)`. -/
noncomputable def coeffPos (m p n : ℕ) : Habiro R :=
  q ^ n * chainPos m n * chainPos p n

/-- `H_n` for `K_(m+1, -(p+1))`: `(-1)^n q^{-n(n+1)/2} C_{m+1}(n) D_{p+1}(n)`. -/
noncomputable def coeffNeg (m p n : ℕ) : Habiro R :=
  (-1) ^ n * qInv ^ (n * (n + 1) / 2) * chainPos m n * chainNeg p n

/-- **Kashaev element of `K_(m+1, p+1)`**: `∑_n H_n (q;q)_n²`. -/
noncomputable def doubleTwistPos (m p : ℕ) : Habiro R :=
  series fun n => coeffPos m p n * poch q n

/-- **Kashaev element of `K_(m+1, -(p+1))`**: `∑_n H_n (q;q)_n²`. -/
noncomputable def doubleTwistNeg (m p : ℕ) : Habiro R :=
  series fun n => coeffNeg m p n * poch q n

/-! ### `(q⁻¹;q⁻¹)_n` in terms of `(q;q)_n` -/

private theorem tri_succ (n : ℕ) : (n + 1) * (n + 1 + 1) / 2 = n * (n + 1) / 2 + (n + 1) := by
  have h : (n + 1) * (n + 1 + 1) = n * (n + 1) + 2 * (n + 1) := by ring
  rw [h, Nat.add_mul_div_left _ _ (by norm_num)]

/-- In any commutative ring, if `a b = 1` then
    `(b;b)_n = (-1)^n b^{n(n+1)/2} (a;a)_n`. -/
theorem poch_of_mul_eq_one {A : Type*} [CommRing A] {a b : A} (hab : a * b = 1) (n : ℕ) :
    poch b n = (-1) ^ n * b ^ (n * (n + 1) / 2) * poch a n := by
  induction n with
  | zero => simp [poch]
  | succ n ih =>
    have hp : b ^ (n + 1) * a ^ (n + 1) = 1 := by rw [← mul_pow, mul_comm, hab, one_pow]
    have hb : poch b (n + 1) = poch b n * (1 - b ^ (n + 1)) := by
      simp only [poch, prod_range_succ]
    have ha : poch a (n + 1) = poch a n * (1 - a ^ (n + 1)) := by
      simp only [poch, prod_range_succ]
    rw [hb, ha, ih, tri_succ, pow_add, pow_succ (-1 : A)]
    linear_combination (-((-1) ^ n * b ^ (n * (n + 1) / 2) * poch a n)) * hp

/-- `(q⁻¹;q⁻¹)_n = (-1)^n q^{-n(n+1)/2} (q;q)_n` in `R̂[q]`. -/
theorem poch_qInv (n : ℕ) :
    poch (qInv : Habiro R) n = (-1) ^ n * qInv ^ (n * (n + 1) / 2) * poch q n :=
  poch_of_mul_eq_one q_mul_qInv n

/-- **Non-vacuity**: `K_(1,-1)` is the figure-eight element. -/
theorem doubleTwistNeg_zero_zero : (doubleTwistNeg 0 0 : Habiro R) = figureEight := by
  unfold doubleTwistNeg figureEight
  congr 1; funext n
  rw [coeffNeg, poch_qInv]
  simp [chainPos, chainNeg]

/-! ### Kashaev values at a root of `Φ_N` -/

section Eval

variable {S : Type*} [CommRing S] [Algebra R S] {N : ℕ} (hN : N ≠ 0) {ζ : S}
  (hζ : aeval ζ (cyclotomic N R) = 0)

theorem evalRoot_doubleTwistPos (m p : ℕ) :
    evalRoot hN ζ hζ (doubleTwistPos m p) =
      ∑ n ∈ range N, evalRoot hN ζ hζ (coeffPos m p n) * (poch ζ n * poch ζ n) := by
  rw [doubleTwistPos, evalRoot_series]
  refine sum_congr rfl fun n _ => ?_
  rw [map_mul, map_poch, evalRoot_q, mul_assoc]

theorem evalRoot_doubleTwistNeg (m p : ℕ) :
    evalRoot hN ζ hζ (doubleTwistNeg m p) =
      ∑ n ∈ range N, evalRoot hN ζ hζ (coeffNeg m p n) * (poch ζ n * poch ζ n) := by
  rw [doubleTwistNeg, evalRoot_series]
  refine sum_congr rfl fun n _ => ?_
  rw [map_mul, map_poch, evalRoot_q, mul_assoc]

/-- The Gaussian binomials evaluate to Gaussian binomials in `ζ`. -/
theorem evalRoot_gaussBinom (n k : ℕ) :
    evalRoot hN ζ hζ (gaussBinom q n k) = gaussBinom ζ n k := by
  rw [map_gaussBinom, evalRoot_q]

end Eval

end QCalculus.HabiroSeries
