import QCalculus.HabiroDoubleTwist
import QCalculus.HabiroNewtonLadder

/-!
# QCalculus.HabiroColoredJones — colored Jones from cyclotomic coefficients, for any knot

Bean `qou-28qh`, phase 6.1 (the "every knot" goal). Over any commutative ring `R`.

Habiro's theorem [habiro2008] says that for every knot `K` there are
coefficients `C_n(K) ∈ ℤ[q^{±1}]` with

  `J_N(K; q) = ∑_{n ≥ 0} C_n(K) (q^{1+N}; q)_n (q^{1-N}; q)_n`,

the cyclotomic expansion (normalization of [lovejoy-osburn, (1.1)]; the sum
stops at `n = N - 1` because `(q^{1-N}; q)_n` has the factor `1 - q^0` once
`n ≥ N`). This file takes the coefficients as data, so every statement below
holds for **every knot** for which the expansion is supplied, and needs no
knot-specific computation:

* `coloredJones C N ∈ R̂[q]`: the colour-`N` polynomial built from `C`;
* `kashaevElement C = ∑_n C_n (q;q)_n² ∈ R̂[q]`: one element for all `N`;
* `evalRoot_coloredJones`: **at a root `ζ` of `Φ_N`, the colour-`N` value equals
  the value of `kashaevElement C`.** This is the algebraic content of
  "the Kashaev invariant is the colored Jones polynomial at its own root of
  unity", proved here for any coefficient sequence;
* `CyclotomicExpansion J`: a structure packaging a family `J N` with its
  coefficients; `CyclotomicExpansion.evalRoot_eq` then reads every Kashaev value
  off one Habiro element.
* `coloredJonesAt q qi C N`: the same polynomial in any commutative ring with
  `q · qi = 1`; `coloredJones` is its instance in `R̂[q]`.
* `coloredJones41_eq_coloredJonesAt`: the corpus's `HabiroNewtonLadder.coloredJones41`
  (the figure-eight tower used by the AJ files) is `coloredJonesAt` with the
  figure-eight coefficients `(-1)^n q^{-n(n+1)/2}`, the same coefficients as
  `figureEight`. So the AJ tower and the Kashaev element are one object.
* Instances of the coefficient data from phases 1–2: `doubleTwistPos`,
  `doubleTwistNeg` and `figureEight` are `kashaevElement`s.

What is NOT proved: Habiro's existence theorem itself (that every knot's
colored Jones polynomial admits such `C_n`). That needs the quantum `sl₂`
universal invariant and is the remaining research step of phase 6.

No analytic API, no empirical value.

-- Ref: [habiro2008]
-- Ref: [habiro2004cyclotomic]
-- Ref: [lovejoy-osburn]
-/

namespace QCalculus.HabiroSeries

open Polynomial Finset

variable {R : Type*} [CommRing R]

/-- The colour-`N` cyclotomic polynomial in any commutative ring, with `qi`
    standing for `q⁻¹`: `∑_{n<N} C_n ∏_{k<n} (1 - q^{N+1+k}) (1 - qi^{N-1-k})`. -/
def coloredJonesAt {A : Type*} [CommRing A] (q qi : A) (C : ℕ → A) (N : ℕ) : A :=
  ∑ n ∈ range N, C n * (∏ k ∈ range n, (1 - q ^ (N + 1 + k))) *
    ∏ k ∈ range n, (1 - qi ^ (N - 1 - k))

/-- `(q^{1+N}; q)_n = ∏_{k<n} (1 - q^{N+1+k})`. -/
noncomputable def jonesPos (N n : ℕ) : Habiro R :=
  ∏ k ∈ range n, (1 - q ^ (N + 1 + k))

/-- `(q^{1-N}; q)_n = ∏_{k<n} (1 - q^{-(N-1-k)})` (exact for `n ≤ N`; for `n > N`
    both sides vanish because of the factor `k = N - 1`). -/
noncomputable def jonesNeg (N n : ℕ) : Habiro R :=
  ∏ k ∈ range n, (1 - qInv ^ (N - 1 - k))

/-- `(q^{1-N}; q)_n = 0` once `n ≥ N ≥ 1`: this is why the expansion is finite. -/
theorem jonesNeg_eq_zero {N n : ℕ} (hN : N ≠ 0) (hn : N ≤ n) : (jonesNeg N n : Habiro R) = 0 := by
  apply prod_eq_zero (i := N - 1) (mem_range.mpr (by omega))
  rw [Nat.sub_self, pow_zero, sub_self]

/-- **The colour-`N` colored Jones element** `∑_{n<N} C_n (q^{1+N})_n (q^{1-N})_n`. -/
noncomputable def coloredJones (C : ℕ → Habiro R) (N : ℕ) : Habiro R :=
  ∑ n ∈ range N, C n * jonesPos N n * jonesNeg N n

theorem coloredJones_eq_coloredJonesAt (C : ℕ → Habiro R) (N : ℕ) :
    coloredJones C N = coloredJonesAt q qInv C N := rfl

/-- Any longer cut gives the same element (the tail vanishes). -/
theorem coloredJones_eq_sum_of_le (C : ℕ → Habiro R) {N M : ℕ} (hN : N ≠ 0) (hM : N ≤ M) :
    coloredJones C N = ∑ n ∈ range M, C n * jonesPos N n * jonesNeg N n := by
  have htail : ∑ n ∈ Ico N M, C n * jonesPos N n * jonesNeg N n = 0 :=
    sum_eq_zero fun n hn => by rw [jonesNeg_eq_zero hN (mem_Ico.mp hn).1, mul_zero]
  rw [coloredJones, ← sum_range_add_sum_Ico _ hM, htail, add_zero]

/-- Colour `1`: `J_1 = C_0`. With the standard normalization `C_0 = 1`, `J_1 = 1`. -/
theorem coloredJones_one (C : ℕ → Habiro R) : coloredJones C 1 = C 0 := by
  simp [coloredJones, jonesPos, jonesNeg]

/-- **The Kashaev element** `∑_n C_n (q;q)_n²`, one element of `R̂[q]` for all colours. -/
noncomputable def kashaevElement (C : ℕ → Habiro R) : Habiro R :=
  series fun n => C n * poch q n

section Eval

variable {S : Type*} [CommRing S] [Algebra R S] {N : ℕ} (hN : N ≠ 0) {ζ : S}
  (hζ : aeval ζ (cyclotomic N R) = 0)

private theorem inv_pow_eq {ζ' : S} (hζζ' : ζ * ζ' = 1) (hpow : ζ ^ N = 1) {k : ℕ}
    (hk : k < N) : ζ' ^ (N - 1 - k) = ζ ^ (k + 1) := by
  have h1 : ζ ^ (N - 1 - k) * ζ' ^ (N - 1 - k) = 1 := by rw [← mul_pow, hζζ', one_pow]
  have h2 : ζ ^ (N - 1 - k) * ζ ^ (k + 1) = 1 := by
    rw [← pow_add, show N - 1 - k + (k + 1) = N by omega, hpow]
  calc ζ' ^ (N - 1 - k) = ζ' ^ (N - 1 - k) * (ζ ^ (N - 1 - k) * ζ ^ (k + 1)) := by
        rw [h2, mul_one]
    _ = (ζ ^ (N - 1 - k) * ζ' ^ (N - 1 - k)) * ζ ^ (k + 1) := by ring
    _ = ζ ^ (k + 1) := by rw [h1, one_mul]

theorem evalRoot_jonesPos (n : ℕ) : evalRoot hN ζ hζ (jonesPos N n) = poch ζ n := by
  have hpow := pow_eq_one_of_aeval_cyclotomic hζ
  rw [jonesPos, map_prod (evalRoot hN ζ hζ), poch]
  refine prod_congr rfl fun k _ => ?_
  rw [RingHom.map_sub, RingHom.map_one, RingHom.map_pow, evalRoot_q, show N + 1 + k = N + (k + 1) by ring, pow_add,
    hpow, one_mul]

theorem evalRoot_jonesNeg {n : ℕ} (hn : n ≤ N) : evalRoot hN ζ hζ (jonesNeg N n) = poch ζ n := by
  have hpow := pow_eq_one_of_aeval_cyclotomic hζ
  have hinv := evalRoot_q_mul_qInv hN hζ
  rw [jonesNeg, map_prod (evalRoot hN ζ hζ), poch]
  refine prod_congr rfl fun k hk => ?_
  rw [RingHom.map_sub, RingHom.map_one, RingHom.map_pow, inv_pow_eq hinv hpow (by have := mem_range.mp hk; omega)]

set_option synthInstance.maxHeartbeats 200000 in
/-- **The Kashaev value of the colour-`N` colored Jones element is the value of the
    single Habiro element `kashaevElement C`**, for any coefficients `C`. -/
theorem evalRoot_coloredJones (C : ℕ → Habiro R) :
    evalRoot hN ζ hζ (coloredJones C N) = evalRoot hN ζ hζ (kashaevElement C) := by
  rw [coloredJones, kashaevElement, evalRoot_series, map_sum (evalRoot hN ζ hζ)]
  refine sum_congr rfl fun n hn => ?_
  rw [RingHom.map_mul, RingHom.map_mul, RingHom.map_mul, evalRoot_jonesPos, evalRoot_jonesNeg hN hζ
    (le_of_lt (mem_range.mp hn)), map_poch, evalRoot_q, mul_assoc]

end Eval

/-- **Cyclotomic expansion data** for a family of colored Jones elements `J N`
    (Habiro's theorem supplies one for every knot). -/
structure CyclotomicExpansion (J : ℕ → Habiro R) where
  /-- The cyclotomic coefficients `C_n(K)`. -/
  coeff : ℕ → Habiro R
  /-- Normalization `C_0 = 1`, i.e. `J_1 = 1`. -/
  coeff_zero : coeff 0 = 1
  /-- The expansion at every colour. -/
  expand : ∀ N, J N = coloredJones coeff N

/-- Every Kashaev value of a knot with a cyclotomic expansion is the value of one
    Habiro element. -/
theorem CyclotomicExpansion.evalRoot_eq {J : ℕ → Habiro R} (E : CyclotomicExpansion J)
    {S : Type*} [CommRing S] [Algebra R S] {N : ℕ} (hN : N ≠ 0) {ζ : S}
    (hζ : aeval ζ (cyclotomic N R) = 0) :
    evalRoot hN ζ hζ (J N) = evalRoot hN ζ hζ (kashaevElement E.coeff) := by
  rw [E.expand N, evalRoot_coloredJones]

/-- `J_1 = 1` for every knot with an expansion. -/
theorem CyclotomicExpansion.one {J : ℕ → Habiro R} (E : CyclotomicExpansion J) : J 1 = 1 := by
  rw [E.expand, coloredJones_one, E.coeff_zero]

/-! ### The knots of phases 1–2 are instances -/

theorem doubleTwistPos_eq_kashaevElement (m p : ℕ) :
    (doubleTwistPos m p : Habiro R) = kashaevElement (coeffPos m p) := rfl

theorem doubleTwistNeg_eq_kashaevElement (m p : ℕ) :
    (doubleTwistNeg m p : Habiro R) = kashaevElement (coeffNeg m p) := rfl

theorem figureEight_eq_kashaevElement :
    (figureEight : Habiro R) = kashaevElement (coeffNeg 0 0) := by
  rw [← doubleTwistNeg_zero_zero]; rfl

theorem chainPos_zero_right : ∀ m : ℕ, (chainPos m 0 : Habiro R) = 1
  | 0 => rfl
  | m + 1 => by simp [chainPos, chainPos_zero_right m]

/-- The double twist family from the cited Lauridsen expansion, as cyclotomic data. -/
noncomputable def doubleTwistPosExpansion (m p : ℕ) :
    CyclotomicExpansion (fun N => coloredJones (coeffPos (R := R) m p) N) where
  coeff := coeffPos m p
  coeff_zero := by simp [coeffPos, chainPos_zero_right]
  expand _ := rfl

/-! ### The corpus figure-eight tower is the same object -/

section FigureEightTower

open QOU.BraidKnot.HabiroNewtonLadder

private theorem tri_succ' (n : ℕ) : (n + 1) * (n + 1 + 1) / 2 = n * (n + 1) / 2 + (n + 1) := by
  have h : (n + 1) * (n + 1 + 1) = n * (n + 1) + 2 * (n + 1) := by ring
  rw [h, Nat.add_mul_div_left _ _ (by norm_num)]

private theorem prod_neg_inv_pow {K : Type*} [Field K] (x : K) (k : ℕ) :
    ∏ j ∈ range k, (-(x ^ (j + 1))⁻¹) = (-1) ^ k * x⁻¹ ^ (k * (k + 1) / 2) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [prod_range_succ, ih, tri_succ', pow_succ (-1 : K), inv_pow, inv_pow]
    simp only [pow_add, pow_one, mul_inv]
    ring

private theorem pos_factor {K : Type*} [Field K] {x : K} (hx : x ≠ 0) (N k : ℕ) :
    x ^ (N * k) * ∏ j ∈ range k, (1 - (x ^ (N + 1 + j))⁻¹) =
      (-1) ^ k * x⁻¹ ^ (k * (k + 1) / 2) * ∏ j ∈ range k, (1 - x ^ (N + 1 + j)) := by
  have hc : x ^ (N * k) = ∏ _j ∈ range k, x ^ N := by
    rw [prod_const, card_range, ← pow_mul]
  rw [hc, ← prod_mul_distrib, ← prod_neg_inv_pow, ← prod_mul_distrib]
  refine prod_congr rfl fun j _ => ?_
  have hN : x ^ N ≠ 0 := pow_ne_zero _ hx
  have hj : x ^ (j + 1) ≠ 0 := pow_ne_zero _ hx
  rw [show N + 1 + j = N + (j + 1) by ring, pow_add]
  field_simp
  ring

private theorem neg_factor {K : Type*} [Field K] {x : K} (hx : x ≠ 0) {N j : ℕ} (hj : j < N) :
    1 - x ^ (j + 1) * (x ^ N)⁻¹ = 1 - x⁻¹ ^ (N - 1 - j) := by
  have hsplit : x ^ N = x ^ (N - 1 - j) * x ^ (j + 1) := by
    rw [← pow_add]; congr 1; omega
  have h1 : x ^ (N - 1 - j) ≠ 0 := pow_ne_zero _ hx
  have h2 : x ^ (j + 1) ≠ 0 := pow_ne_zero _ hx
  rw [hsplit, inv_pow]
  field_simp

/-- **`coloredJones41` is the cyclotomic polynomial with the figure-eight
    coefficients** `C_n = (-1)^n q^{-n(n+1)/2}`, over any field. -/
theorem coloredJones41_eq_coloredJonesAt {K : Type*} [Field K] {x : K} (hx : x ≠ 0) (N : ℕ) :
    coloredJones41 x N =
      coloredJonesAt x x⁻¹ (fun n => (-1) ^ n * x⁻¹ ^ (n * (n + 1) / 2)) N := by
  rw [coloredJones41, coloredJonesAt]
  refine sum_congr rfl fun k hk => ?_
  have hkN : k < N := mem_range.mp hk
  rw [habiroTerm, pos_factor hx]
  congr 1
  refine prod_congr rfl fun j hj => ?_
  exact neg_factor hx (lt_trans (mem_range.mp hj) hkN)

end FigureEightTower

end QCalculus.HabiroSeries
