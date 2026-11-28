import QOU.FluidDynamics.q_ns_qlegendre_classical_limit
import QOU.FluidDynamics.surreal_enstrophy_finite_modes

/-!
# QOU.FluidDynamics.q_ns_qlegendre_band_edge — where the coupled band ends

The normalised squared raising coupling `Rc q s` depends on the mode index `s` only through
`z = P^{s+1}`, `P = q²`. Written in `(P, z)` it is the rational function
`Rcz P z = (z-1)² P² (Pz-1)⁴ / ((P-1)² (Pz²-1)(P²z²-1)²(P³z²-1))`
(`Rcz_pow_eq_Rc`). In `Rcz` the index is a field element, so an *infinite* index (a
hypernatural `s`, `z = P^{s+1}`) is simply a large `z`. No exponent ranging over the field is
needed, and everything stays algebraic.

**Band-edge theorem** (`Rcz_infinitesimal_iff`). Over a linearly ordered field `K` (possibly a
surreal line), with `P = 1 + δ`, `0 < δ ≤ 1` and `z ≥ 2`:
`Rcz P z` is infinitesimal **iff** `δ·z` is not finite.
The proof is the two-sided estimate `1/(16384 (δz)²) ≤ Rcz P z ≤ 256/(δz)²` (`Rcz_bounds`).

**Reading at `δ` infinitesimal.** The triad coupling of mode `z` is infinitesimal exactly beyond
`z ~ 1/δ`, i.e. `s ~ log(1/δ)/δ`. Every standard mode, and every mode with `δz` finite, stays
coupled (compare `Rc_ge_of_infinitesimal`). This locates the edge of the band of modes the
nonlinearity can reach through this coupling. It says nothing about how much energy actually
reaches the edge, about the `N → ∞` limit, or about the classical PDE. On an archimedean `K`
every element is finite, so the coupling is never infinitesimal there and the statement is
the estimate alone.

## References
- [leitner2026] fluid-dynamics/regularity-breakdown (Part A); appendix-surreals/
  surreal-blowup-calculus; QOU/FluidDynamics/q_ns_qlegendre_classical_limit;
  QOU/FluidDynamics/surreal_enstrophy_finite_modes (infinitesimal calculus).
-/

namespace QOU.FluidDynamics.QLegendreClassical

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2
open QOU.FluidDynamics QOU.FluidDynamics.TriadRaising QOU.FluidDynamics.QLegendreNorm

variable {K : Type*} [Field K]

/-- The coupling in the index-free variable `z = P^{s+1}`. -/
noncomputable def Rcz (P z : K) : K :=
  (z - 1) ^ 2 * P ^ 2 * (P * z - 1) ^ 4 /
    ((P - 1) ^ 2 * (P * z ^ 2 - 1) * (P ^ 2 * z ^ 2 - 1) ^ 2 * (P ^ 3 * z ^ 2 - 1))

/-- **`Rcz` is `Rc` at `z = P^{s+1}`.** -/
theorem Rcz_pow_eq_Rc (q : Kˣ) (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (s : ℕ) :
    Rcz ((q : K) * q) (((q : K) * q) ^ (s + 1)) = Rc q s := by
  have h1 : (q : K) * q - 1 ≠ 0 := sub_ne_zero.mpr (by simpa using hp 0)
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hz : ((q : K) * q) ^ (s + 1) ≠ 0 := pow_ne_zero _ (mul_ne_zero hq0 hq0)
  have hqq : (((q⁻¹ : Kˣ) : K)) * (q : K) = 1 := by simp
  have hk : kap q s * (((q⁻¹ : Kˣ) : K)) * ((q : K) * q) ^ (s + 1) =
      jk ((q : K) * q) (s + 1) := by
    unfold kap
    rw [show (((q⁻¹ : Kˣ) : K)) * jk ((q : K) * q) (s + 1) *
          ((((q⁻¹ : Kˣ) : K)) * (((q⁻¹ : Kˣ) : K))) ^ s * (((q⁻¹ : Kˣ) : K)) *
          ((q : K) * q) ^ (s + 1) =
        jk ((q : K) * q) (s + 1) * ((((q⁻¹ : Kˣ) : K)) * (q : K)) ^ (2 * s + 2) by ring,
      hqq, one_pow, mul_one]
  have hkap : kap q s * (((q⁻¹ : Kˣ) : K)) =
      jk ((q : K) * q) (s + 1) / ((q : K) * q) ^ (s + 1) := by
    rw [eq_div_iff hz, hk]
  have hj : jk ((q : K) * q) (s + 1) =
      (((q : K) * q) ^ (s + 1) - 1) / ((q : K) * q - 1) := by
    rw [eq_div_iff h1, pow_sub_one_eq]
  unfold Rc
  rw [hkap, ← nf_eq_nfc hp (s + 1), hj]
  unfold nf Rcz
  field_simp

section Ordered

variable [LinearOrder K] [IsStrictOrderedRing K]

/-- The three `z²`-factors of the denominator, bounded for `1 ≤ P ≤ 2`, `z ≥ 2`. -/
theorem den_factors {P z : K} (hP1 : 1 ≤ P) (hP2 : P ≤ 2) (hz : 2 ≤ z) :
    (3 / 4 * z ^ 2 ≤ P * z ^ 2 - 1 ∧ 3 / 4 * z ^ 2 ≤ P ^ 2 * z ^ 2 - 1 ∧
      3 / 4 * z ^ 2 ≤ P ^ 3 * z ^ 2 - 1) ∧
    (P * z ^ 2 - 1 ≤ 2 * z ^ 2 ∧ P ^ 2 * z ^ 2 - 1 ≤ 4 * z ^ 2 ∧
      P ^ 3 * z ^ 2 - 1 ≤ 8 * z ^ 2) := by
  have hz4 : 4 ≤ z ^ 2 := by nlinarith
  have p2l : 1 ≤ P ^ 2 := one_le_pow₀ hP1
  have p3l : 1 ≤ P ^ 3 := one_le_pow₀ hP1
  have p2u : P ^ 2 ≤ 4 := by nlinarith
  have p3u : P ^ 3 ≤ 8 := by nlinarith
  have hz2 : 0 ≤ z ^ 2 := sq_nonneg z
  refine ⟨⟨?_, ?_, ?_⟩, ?_, ?_, ?_⟩
  · nlinarith [mul_le_mul_of_nonneg_right hP1 hz2]
  · nlinarith [mul_le_mul_of_nonneg_right p2l hz2]
  · nlinarith [mul_le_mul_of_nonneg_right p3l hz2]
  · nlinarith [mul_le_mul_of_nonneg_right hP2 hz2]
  · nlinarith [mul_le_mul_of_nonneg_right p2u hz2]
  · nlinarith [mul_le_mul_of_nonneg_right p3u hz2]

/-- Monotonicity of a product of four nonnegative factors. -/
theorem prod4_le {a b c d a' b' c' d' : K} (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c)
    (hd : 0 ≤ d) (h1 : a ≤ a') (h2 : b ≤ b') (h3 : c ≤ c') (h4 : d ≤ d') :
    a * b * c * d ≤ a' * b' * c' * d' := by
  have e1 := mul_le_mul h1 h2 hb (ha.trans h1)
  have e2 := mul_le_mul e1 h3 hc (mul_nonneg (ha.trans h1) (hb.trans h2))
  exact mul_le_mul e2 h4 hd
    (mul_nonneg (mul_nonneg (ha.trans h1) (hb.trans h2)) (hc.trans h3))

set_option maxHeartbeats 1000000 in
/-- **Two-sided estimate of the coupling** for `0 < δ ≤ 1`, `z ≥ 2`:
`1/(16384 (δz)²) ≤ Rcz (1+δ) z ≤ 256/(δz)²`. -/
theorem Rcz_bounds {δ z : K} (hδ : 0 < δ) (hδ1 : δ ≤ 1) (hz : 2 ≤ z) :
    1 / (16384 * (δ * z) ^ 2) ≤ Rcz (1 + δ) z ∧ Rcz (1 + δ) z ≤ 256 / (δ * z) ^ 2 := by
  have hP1 : 1 ≤ 1 + δ := by linarith
  have hP2 : 1 + δ ≤ 2 := by linarith
  obtain ⟨⟨a1, a2, a3⟩, u1, u2, u3⟩ := den_factors hP1 hP2 hz
  have hz0 : 0 < z := by linarith
  have hm0 : 0 < 3 / 4 * z ^ 2 := by positivity
  have hA : 0 < (1 + δ) * z ^ 2 - 1 := lt_of_lt_of_le hm0 a1
  have hB : 0 < (1 + δ) ^ 2 * z ^ 2 - 1 := lt_of_lt_of_le hm0 a2
  have hC : 0 < (1 + δ) ^ 3 * z ^ 2 - 1 := lt_of_lt_of_le hm0 a3
  have hn1 : z - 1 ≤ (1 + δ) * z - 1 := by nlinarith
  have hn2 : (1 + δ) * z - 1 ≤ 2 * z := by nlinarith
  have hzl : z / 2 ≤ z - 1 := by linarith
  have hzl0 : 0 ≤ z / 2 := by positivity
  have hn0 : 0 ≤ (1 + δ) * z - 1 := by linarith
  have hD : (1 + δ - 1) ^ 2 * ((1 + δ) * z ^ 2 - 1) * ((1 + δ) ^ 2 * z ^ 2 - 1) ^ 2 *
      ((1 + δ) ^ 3 * z ^ 2 - 1) = δ ^ 2 * ((1 + δ) * z ^ 2 - 1) *
      (((1 + δ) ^ 2 * z ^ 2 - 1) * ((1 + δ) ^ 2 * z ^ 2 - 1)) * ((1 + δ) ^ 3 * z ^ 2 - 1) := by
    ring
  have hDpos : 0 < δ ^ 2 * ((1 + δ) * z ^ 2 - 1) *
      (((1 + δ) ^ 2 * z ^ 2 - 1) * ((1 + δ) ^ 2 * z ^ 2 - 1)) * ((1 + δ) ^ 3 * z ^ 2 - 1) := by
    positivity
  have hw : (0 : K) < δ * z := mul_pos hδ hz0
  have hz8 : (0 : K) < δ ^ 2 * z ^ 8 := by positivity
  unfold Rcz
  rw [hD]
  constructor
  · rw [div_le_div_iff₀ (by positivity) hDpos, one_mul]
    have hup := prod4_le (sq_nonneg δ) hA.le (mul_nonneg hB.le hB.le) hC.le le_rfl u1
      (mul_le_mul u2 u2 hB.le (by positivity)) u3
    have hlo : (z / 2) ^ 2 * 1 * (z / 2) ^ 4 ≤
        (z - 1) ^ 2 * (1 + δ) ^ 2 * ((1 + δ) * z - 1) ^ 4 := by
      have e2 := pow_le_pow_left₀ hzl0 hzl 2
      have e4 := pow_le_pow_left₀ hzl0 (hzl.trans hn1) 4
      have hp2 : (1 : K) ≤ (1 + δ) ^ 2 := one_le_pow₀ hP1
      exact mul_le_mul (mul_le_mul e2 hp2 zero_le_one (by positivity)) e4 (by positivity)
        (by positivity)
    have hk : 0 ≤ 16384 * (δ * z) ^ 2 := by positivity
    have heq : δ ^ 2 * (2 * z ^ 2) * (4 * z ^ 2 * (4 * z ^ 2)) * (8 * z ^ 2) =
        16384 * (δ * z) ^ 2 * ((z / 2) ^ 2 * 1 * (z / 2) ^ 4) := by ring
    calc _ ≤ δ ^ 2 * (2 * z ^ 2) * (4 * z ^ 2 * (4 * z ^ 2)) * (8 * z ^ 2) := hup
      _ = 16384 * (δ * z) ^ 2 * ((z / 2) ^ 2 * 1 * (z / 2) ^ 4) := heq
      _ ≤ 16384 * (δ * z) ^ 2 * ((z - 1) ^ 2 * (1 + δ) ^ 2 * ((1 + δ) * z - 1) ^ 4) :=
          mul_le_mul_of_nonneg_left hlo hk
      _ = _ := by ring
  · rw [div_le_div_iff₀ hDpos (by positivity)]
    have hlo := prod4_le (sq_nonneg δ) hm0.le (mul_nonneg hm0.le hm0.le) hm0.le le_rfl a1
      (mul_le_mul a2 a2 hm0.le hB.le) a3
    have hup : (z - 1) ^ 2 * (1 + δ) ^ 2 * ((1 + δ) * z - 1) ^ 4 ≤
        z ^ 2 * 4 * (2 * z) ^ 4 := by
      have e2 := pow_le_pow_left₀ (show (0 : K) ≤ z - 1 by linarith only [hz])
        (sub_le_self z zero_le_one) 2
      have e4 := pow_le_pow_left₀ hn0 hn2 4
      have hp2 : (1 + δ) ^ 2 ≤ 4 := by
        have := pow_le_pow_left₀ (show (0 : K) ≤ 1 + δ by linarith only [hδ]) hP2 2
        norm_num at this ⊢; linarith only [this]
      exact mul_le_mul (mul_le_mul e2 hp2 (by positivity) (by positivity)) e4 (by positivity)
        (by positivity)
    have hk : 0 ≤ (δ * z) ^ 2 := sq_nonneg _
    have eL : z ^ 2 * 4 * (2 * z) ^ 4 * (δ * z) ^ 2 = 64 * (δ ^ 2 * z ^ 8) := by ring
    have eR : 256 * (δ ^ 2 * (3 / 4 * z ^ 2) * (3 / 4 * z ^ 2 * (3 / 4 * z ^ 2)) *
        (3 / 4 * z ^ 2)) = 81 * (δ ^ 2 * z ^ 8) := by ring
    calc _ ≤ z ^ 2 * 4 * (2 * z) ^ 4 * (δ * z) ^ 2 := mul_le_mul_of_nonneg_right hup hk
      _ = 64 * (δ ^ 2 * z ^ 8) := eL
      _ ≤ 81 * (δ ^ 2 * z ^ 8) := mul_le_mul_of_nonneg_right (by norm_num) hz8.le
      _ = 256 * (δ ^ 2 * (3 / 4 * z ^ 2) * (3 / 4 * z ^ 2 * (3 / 4 * z ^ 2)) *
          (3 / 4 * z ^ 2)) := eR.symm
      _ ≤ _ := mul_le_mul_of_nonneg_left hlo (by norm_num)

/-- A positive element that is not finite has an infinitesimal reciprocal. -/
theorem infinitesimal_inv_of_not_finite {w : K} (hw : 0 < w) (h : ¬ IsFinite w) :
    Infinitesimal w⁻¹ := by
  intro n
  have hn : ((n : K) + 1) ≤ w := by
    by_contra hc
    push_neg at hc
    exact h ⟨n + 1, by rw [abs_of_pos hw]; push_cast; exact hc⟩
  rw [abs_of_pos (inv_pos.mpr hw), ← div_eq_mul_inv, div_lt_one hw]
  linarith

/-- **Band-edge theorem.** For `0 < δ ≤ 1` and `z ≥ 2`, the coupling `Rcz (1+δ) z` is
infinitesimal if and only if `δ·z` is not finite. -/
theorem Rcz_infinitesimal_iff {δ z : K} (hδ : 0 < δ) (hδ1 : δ ≤ 1) (hz : 2 ≤ z) :
    Infinitesimal (Rcz (1 + δ) z) ↔ ¬ IsFinite (δ * z) := by
  obtain ⟨hlo, hup⟩ := Rcz_bounds hδ hδ1 hz
  have hw : (0 : K) < δ * z := mul_pos hδ (by linarith)
  have hR0 : 0 < Rcz (1 + δ) z := lt_of_lt_of_le (by positivity) hlo
  constructor
  · rintro hR ⟨n, hn⟩
    rw [abs_of_pos hw] at hn
    have hn0 : (0 : K) < n := hw.trans hn
    have hsq : (δ * z) ^ 2 ≤ (n : K) ^ 2 := pow_le_pow_left₀ hw.le hn.le 2
    have hlo' : 1 / (16384 * (n : K) ^ 2) ≤ Rcz (1 + δ) z :=
      le_trans (one_div_le_one_div_of_le (by positivity) (by linarith)) hlo
    have hkey := hR (16384 * n ^ 2)
    rw [abs_of_pos hR0] at hkey
    push_cast at hkey
    rw [div_le_iff₀ (by positivity)] at hlo'
    linarith
  · intro hnf m
    have hi := infinitesimal_inv_of_not_finite hw hnf
    have hi2 : Infinitesimal ((δ * z)⁻¹ * (δ * z)⁻¹) :=
      hi.mul_finite hi.isFinite
    have hm := hi2 (256 * m)
    rw [abs_of_pos hR0]
    have hpos : 0 < (δ * z)⁻¹ * (δ * z)⁻¹ := by positivity
    rw [abs_of_pos hpos] at hm
    have hup' : Rcz (1 + δ) z ≤ 256 * ((δ * z)⁻¹ * (δ * z)⁻¹) := by
      rw [← mul_inv, ← sq, ← div_eq_mul_inv]; exact hup
    push_cast at hm
    have hm0 : (0 : K) ≤ m := Nat.cast_nonneg m
    nlinarith [mul_le_mul_of_nonneg_left hup' hm0]

end Ordered

end QOU.FluidDynamics.QLegendreClassical
