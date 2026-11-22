import QOU.KZ.AssociatorKZ
import Mathlib.RingTheory.PowerSeries.Basic

/-!
# Shift invariance of the KZ associator

Stage S2 prerequisite of bean `qou-zoyv`. If `z` commutes with `A` and `B`, then
`Φ_KZ(A, B + z) = Φ_KZ(A, B)` and `Φ_KZ(A + z, B) = Φ_KZ(A, B)`.

## Formal part

Write `H` for the coefficient sequence of a formal solution as a power series. The gauge equation
`k H_k + H_k M₀ = ∑_{j ≤ k} M_{k-j} H_j` reads `Θ H + H M₀ = M H` with the Euler operator
`Θ = w d/dw` (`isFormalGauge_iff_euler`), and `Θ` is a derivation
(`euler_mul`). So if `H` solves `kzM0 A B`, `E` solves `kzM0 0 z` (that is, `E = (1 − w)^z`) and `z`
commutes with everything in sight, then the Cauchy product `H E` solves `kzM0 A (B + z)`
(`isFormalGauge_conv`).

Base: generic ring (formal part). Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2, shift invariance)
-/

noncomputable section

namespace QOU.KZ.KZShift

open QOU.KZ.FuchsianFormal PowerSeries

section Formal

variable {R : Type*} [Ring R]

/-- The Euler operator `Θ = w d/dw` on power series. -/
def euler (f : PowerSeries R) : PowerSeries R := mk fun k => (k : R) * coeff k f

theorem coeff_euler (f : PowerSeries R) (k : ℕ) : coeff k (euler f) = (k : R) * coeff k f :=
  coeff_mk _ _

/-- `Θ` is a derivation (no commutativity needed: the integer `k` is central). -/
theorem euler_mul (f g : PowerSeries R) : euler (f * g) = euler f * g + f * euler g := by
  ext k
  simp only [coeff_euler, map_add, coeff_mul, Finset.mul_sum]
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun p hp => ?_
  rw [Finset.mem_antidiagonal] at hp
  rw [← hp, Nat.cast_add, add_mul, mul_assoc]
  congr 1
  rw [← mul_assoc, ← mul_assoc, (Nat.cast_commute p.2 (coeff p.1 f)).eq]

/-- The power series with coefficient sequence `H`. -/
abbrev ser (H : ℕ → R) : PowerSeries R := mk H

theorem coeff_gaugeLHS (M H : ℕ → R) (k : ℕ) :
    coeff k (euler (ser H) + ser H * C (M 0)) = (k : R) * H k + H k * M 0 := by
  simp only [map_add, coeff_euler, coeff_mul_C, ser, coeff_mk]

theorem coeff_ser_mul (M H : ℕ → R) (k : ℕ) :
    coeff k (ser M * ser H) = ∑ j ∈ Finset.range (k + 1), M (k - j) * H j := by
  rw [coeff_mul, ← Finset.Nat.sum_antidiagonal_swap]
  simp only [ser, coeff_mk, Prod.fst_swap, Prod.snd_swap]
  exact Finset.Nat.sum_antidiagonal_eq_sum_range_succ (fun i j => M j * H i) k

theorem isFormalGauge_iff_euler (M H : ℕ → R) :
    IsFormalGauge M H ↔ euler (ser H) + ser H * C (M 0) = ser M * ser H := by
  rw [PowerSeries.ext_iff]
  simp only [coeff_gaugeLHS, coeff_ser_mul]
  rfl

/-- Series whose coefficients commute pairwise commute. -/
theorem ser_mul_comm {f g : ℕ → R} (h : ∀ i j, Commute (f i) (g j)) :
    ser f * ser g = ser g * ser f := by
  ext k
  rw [coeff_mul, coeff_mul, ← Finset.Nat.sum_antidiagonal_swap]
  refine Finset.sum_congr rfl fun p _ => ?_
  simp only [ser, coeff_mk, Prod.fst_swap, Prod.snd_swap]
  exact (h p.2 p.1).eq

/-- The Cauchy product of coefficient sequences. -/
def conv (H E : ℕ → R) (k : ℕ) : R := ∑ p ∈ Finset.antidiagonal k, H p.1 * E p.2

theorem ser_conv (H E : ℕ → R) : ser (conv H E) = ser H * ser E := by
  ext k; simp [conv, coeff_mul]

theorem ser_kzM0_add (A B z : R) : ser (kzM0 A (B + z)) = ser (kzM0 A B) + ser (kzM0 0 z) := by
  ext k
  rcases k with _ | k <;> simp [kzM0, add_comm]

/-- **Formal shift.** If `H` solves `kzM0 A B` and `E` solves `kzM0 0 z` (so `E = (1 − w)^z`),
with `z` commuting with every `H_k` and every `E_k` commuting with `A`, then the Cauchy product
`H E` solves `kzM0 A (B + z)`. -/
theorem isFormalGauge_conv (A B z : R) (H E : ℕ → R) (hH : IsFormalGauge (kzM0 A B) H)
    (hE : IsFormalGauge (kzM0 0 z) E) (hzH : ∀ k, Commute z (H k))
    (hEA : ∀ k, Commute (E k) A) : IsFormalGauge (kzM0 A (B + z)) (conv H E) := by
  rw [isFormalGauge_iff_euler] at hH hE ⊢
  have hE' : euler (ser E) = ser (kzM0 0 z) * ser E := by
    rw [← hE]; simp [kzM0]
  have hNH : ser H * ser (kzM0 0 z) = ser (kzM0 0 z) * ser H := by
    refine ser_mul_comm fun i j => ?_
    rcases j with _ | j
    · exact Commute.zero_right _
    · exact ((hzH i).symm).neg_right
  have hEC : ser E * C (kzM0 A B 0) = C (kzM0 A B 0) * ser E := by
    ext k; rw [coeff_mul_C, coeff_C_mul]; simp only [ser, coeff_mk]; exact (hEA k).eq
  have h0 : kzM0 A (B + z) 0 = kzM0 A B 0 := rfl
  rw [ser_conv, euler_mul, hE', ser_kzM0_add, h0, mul_assoc (ser H) (ser E), hEC,
    ← mul_assoc (ser H) (ser (kzM0 0 z)), hNH, add_mul, ← mul_assoc (ser (kzM0 A B)), ← hH]
  noncomm_ring

end Formal

section Analytic

open Set Filter Topology QOU.KZ.FuchsianAnalytic QOU.KZ.AssociatorKZ

variable {R : Type*} [NormedRing R] [NormedAlgebra ℝ R] [CompleteSpace R]

/-- The coefficient sequence `1, 0, 0, …`. -/
def delta0 : ℕ → R := fun k => if k = 0 then 1 else 0

omit [CompleteSpace R] in
theorem series_delta0 (t : ℝ) : series (delta0 (R := R)) t = 1 := by
  unfold series
  rw [tsum_eq_single 0 fun k hk => by simp [delta0, hk]]
  simp [delta0]

omit [NormedAlgebra ℝ R] [CompleteSpace R] in
theorem isFormalGauge_delta0 (z : R) : IsFormalGauge (kzM0 z 0) (delta0 (R := R)) := by
  intro k
  rw [Finset.sum_eq_single 0 (fun j _ hj => by simp [delta0, hj]) (by simp)]
  rcases k with _ | k <;> simp [delta0, kzM0]

omit [CompleteSpace R] in
theorem tpow_zero (t : ℝ) : tpow (0 : R) t = 1 := by
  simp [tpow, NormedSpace.exp_zero]

omit [CompleteSpace R] in
theorem tpow_one (z : R) : tpow z 1 = 1 := by
  simp [tpow, NormedSpace.exp_zero]

/-- **The binomial series.** If `E` is the normalised formal solution of `kzM0 0 z` (so
`k E_k = −z ∑_{j<k} E_j`), then `∑ t^k E_k = (1 − t)^z` on `(0, 1)`. -/
theorem series_eq_tpow_one_sub (z : R) (E : ℕ → R) (hE0 : E 0 = 1)
    (hE : IsFormalGauge (kzM0 0 z) E) {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    series E t = tpow z (1 - t) := by
  obtain ⟨hu, hΦ⟩ := phiKZ_spec (0 : R) z E delta0 hE0 hE (by simp [delta0])
    (isFormalGauge_delta0 z)
  set Φ := phiKZ (0 : R) z E delta0 hE0 hE (by simp [delta0]) (isFormalGauge_delta0 z)
  have hG₀ : ∀ u, G₀ (0 : R) E u = series E u := fun u => by simp [G₀, tpow_zero]
  have hG₁ : ∀ u, G₁ z (delta0 (R := R)) u = tpow z (1 - u) := fun u => by
    simp [G₁, series_delta0]
  -- continuity at `0`
  have hc₀ : ContinuousAt (series E) 0 :=
    (hasDerivAt_series (boundedOn_kz_solution 0 z E hE0 hE) (t := 0) (by simp)).continuousAt
  have hc₁ : ContinuousAt (fun u : ℝ => tpow z (1 - u) * Φ) 0 := by
    have h1 : ContinuousAt (tpow z) (1 - 0) :=
      (hasDerivAt_tpow z (t := 1 - 0) (by norm_num)).continuousAt
    exact (h1.comp (continuousAt_const.sub continuousAt_id)).mul continuousAt_const
  have hev : series E =ᶠ[𝓝[>] (0 : ℝ)] fun u => tpow z (1 - u) * Φ := by
    filter_upwards [Ioo_mem_nhdsGT (show (0 : ℝ) < 1 by norm_num)] with u hu
    rw [← hG₀, hΦ u hu, hG₁]
  have hlim := tendsto_nhds_unique (hc₀.tendsto.mono_left nhdsWithin_le_nhds)
    ((hc₁.tendsto.mono_left nhdsWithin_le_nhds).congr' hev.symm)
  simp only [series_zero, hE0, sub_zero, tpow_one, one_mul] at hlim
  rw [← hG₀, hΦ t ht, hG₁, ← hlim, mul_one]

omit [NormedAlgebra ℝ R] [CompleteSpace R] in
theorem conv_zero (H E : ℕ → R) (hH : H 0 = 1) (hE : E 0 = 1) : conv H E 0 = 1 := by
  simp [conv, hH, hE]

/-- The Cauchy product of convergent series. -/
theorem series_conv {H E : ℕ → R} (hH : BoundedOn H 1) (hE : BoundedOn E 1) {t : ℝ}
    (ht : |t| < 1) : series (conv H E) t = series H t * series E t := by
  unfold series
  rw [tsum_mul_tsum_eq_tsum_sum_antidiagonal_of_summable_norm (summable_norm_of_bounded hH ht)
    (summable_norm_of_bounded hE ht)]
  refine tsum_congr fun n => ?_
  rw [conv, Finset.smul_sum]
  refine Finset.sum_congr rfl fun p hp => ?_
  rw [Finset.mem_antidiagonal] at hp
  rw [smul_mul_smul_comm, ← pow_add, hp]

omit [NormedAlgebra ℝ R] [CompleteSpace R] in
/-- If `z` commutes with every `H_k`, then `H` solves `kzM0 (B + z) A` iff it solves `kzM0 B A`. -/
theorem isFormalGauge_kzM0_add_left (A B z : R) (H : ℕ → R) (hz : ∀ k, Commute z (H k))
    (hH : IsFormalGauge (kzM0 B A) H) : IsFormalGauge (kzM0 (B + z) A) H := by
  rw [isFormalGauge_iff_euler] at hH ⊢
  have e : ser (kzM0 (B + z) A) = ser (kzM0 B A) + C z := by
    ext k; rcases k with _ | k <;> simp [kzM0]
  have hc : ser H * C z = C z * ser H := by
    ext k; rw [coeff_mul_C, coeff_C_mul]; simp only [ser, coeff_mk]; exact (hz k).eq.symm
  have h0 : kzM0 (B + z) A 0 = kzM0 B A 0 + z := rfl
  rw [e, h0, map_add, mul_add, add_mul, ← hH, hc]
  abel

omit [CompleteSpace R] in
theorem commute_series {c : R} {H : ℕ → R} (h : ∀ k, Commute c (H k)) (t : ℝ) :
    Commute c (series H t) :=
  Commute.tsum_right c fun k => (h k).smul_right _

omit [CompleteSpace R] in
theorem commute_tpow {c X : R} (h : Commute c X) (t : ℝ) : Commute c (tpow X t) :=
  Commute.exp_right ℝ (h.smul_right _)

/-- `Φ_KZ(A, B)` commutes with every `c` commuting with `A`, `B` and the formal solutions. -/
theorem commute_phiKZ (A B c : R) (H₀ H₁ : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁)
    (hA : Commute c A) (hB : Commute c B) (hc₀ : ∀ k, Commute c (H₀ k))
    (hc₁ : ∀ k, Commute c (H₁ k)) : Commute c (phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁) := by
  obtain ⟨-, hΦ⟩ := phiKZ_spec A B H₀ H₁ h₀ hH₀ h₁ hH₁
  set Φ := phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁
  obtain ⟨δ, hδ, hδ1, hu₁⟩ := exists_isUnit_series (boundedOn_kz_solution B A H₁ h₁ hH₁) h₁
  set t := 1 - δ / 2
  have ht : t ∈ Ioo (0 : ℝ) 1 := ⟨by simp only [t]; linarith, by simp only [t]; linarith⟩
  have hU : IsUnit (G₁ B H₁ t) :=
    (hu₁ (1 - t) ⟨by simp only [t]; linarith, by simp only [t]; linarith⟩).mul
      (isUnit_tpow B (1 - t))
  have hc0 : Commute c (G₀ A H₀ t) := (commute_series hc₀ t).mul_right (commute_tpow hA t)
  have hc1 : Commute c (G₁ B H₁ t) :=
    (commute_series hc₁ (1 - t)).mul_right (commute_tpow hB (1 - t))
  have e : G₁ B H₁ t * (c * Φ) = G₁ B H₁ t * (Φ * c) := by
    rw [← mul_assoc, ← hc1.eq, mul_assoc, ← hΦ t ht, hc0.eq, hΦ t ht, mul_assoc]
  exact hU.mul_left_cancel e

/-- **Shift invariance at `1`.** If `z` commutes with `A`, `B` and the formal solutions, then
`Φ_KZ(A, B + z) = Φ_KZ(A, B)`. The normalised solution at `0` of the shifted system is the Cauchy
product of `H₀` with the binomial series `E = (1 − t)^z`; the one at `1` is `H₁` itself. -/
theorem phiKZ_shift_right (A B z : R) (H₀ H₁ E : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁)
    (hE0 : E 0 = 1) (hE : IsFormalGauge (kzM0 0 z) E) (hzA : Commute z A) (hzB : Commute z B)
    (hz₀ : ∀ k, Commute z (H₀ k)) (hz₁ : ∀ k, Commute z (H₁ k)) (hEA : ∀ k, Commute (E k) A) :
    phiKZ A (B + z) (conv H₀ E) H₁ (conv_zero H₀ E h₀ hE0)
        (isFormalGauge_conv A B z H₀ E hH₀ hE hz₀ hEA) h₁
        (isFormalGauge_kzM0_add_left A B z H₁ hz₁ hH₁) =
      phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ := by
  obtain ⟨hu, hΦ⟩ := phiKZ_spec A B H₀ H₁ h₀ hH₀ h₁ hH₁
  set Φ := phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁
  have hzΦ : Commute z Φ := commute_phiKZ A B z H₀ H₁ h₀ hH₀ h₁ hH₁ hzA hzB hz₀ hz₁
  refine ((kz_associator A (B + z) (conv H₀ E) H₁ (conv_zero H₀ E h₀ hE0)
    (isFormalGauge_conv A B z H₀ E hH₀ hE hz₀ hEA) h₁
    (isFormalGauge_kzM0_add_left A B z H₁ hz₁ hH₁)).unique
    (phiKZ_spec _ _ _ _ _ _ _ _) ⟨hu, fun t ht => ?_⟩)
  have hbE := boundedOn_kz_solution 0 z E hE0 hE
  have hb₀ := boundedOn_kz_solution A B H₀ h₀ hH₀
  have hta : |t| < 1 := by rw [abs_of_pos ht.1]; exact ht.2
  have hEAt : Commute (series E t) (tpow A t) := by
    exact commute_tpow (commute_series (fun k => (hEA k).symm) t).symm t
  have hTΦ : Commute (tpow z (1 - t)) Φ := (commute_tpow hzΦ.symm (1 - t)).symm
  have hexp : tpow (B + z) (1 - t) = tpow B (1 - t) * tpow z (1 - t) := by
    simp only [tpow, smul_add]
    exact NormedSpace.exp_add_of_commute ((hzB.symm.smul_left _).smul_right _)
  calc G₀ A (conv H₀ E) t = series H₀ t * tpow A t * series E t := by
        rw [G₀, series_conv hb₀ hbE hta, mul_assoc, hEAt.eq, ← mul_assoc]
    _ = G₁ B H₁ t * Φ * tpow z (1 - t) := by
        rw [← G₀, hΦ t ht, series_eq_tpow_one_sub z E hE0 hE ht]
    _ = G₁ (B + z) H₁ t * Φ := by
        rw [mul_assoc, ← hTΦ.eq, G₁, G₁, hexp, ← mul_assoc, ← mul_assoc]

/-- **Shift invariance at `0`.** If `z` commutes with `A`, `B` and the formal solutions, then
`Φ_KZ(A + z, B) = Φ_KZ(A, B)` (from `phiKZ_shift_right` and the inversion relation). -/
theorem phiKZ_shift_left (A B z : R) (H₀ H₁ E : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁)
    (hE0 : E 0 = 1) (hE : IsFormalGauge (kzM0 0 z) E) (hzA : Commute z A) (hzB : Commute z B)
    (hz₀ : ∀ k, Commute z (H₀ k)) (hz₁ : ∀ k, Commute z (H₁ k)) (hEB : ∀ k, Commute (E k) B) :
    phiKZ (A + z) B H₀ (conv H₁ E) h₀ (isFormalGauge_kzM0_add_left B A z H₀ hz₀ hH₀)
        (conv_zero H₁ E h₁ hE0) (isFormalGauge_conv B A z H₁ E hH₁ hE hz₁ hEB) =
      phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ := by
  have hsh := phiKZ_shift_right B A z H₁ H₀ E h₁ hH₁ h₀ hH₀ hE0 hE hzB hzA hz₁ hz₀ hEB
  have i1 := (phiKZ_swap_mul (A + z) B H₀ (conv H₁ E) h₀
    (isFormalGauge_kzM0_add_left B A z H₀ hz₀ hH₀) (conv_zero H₁ E h₁ hE0)
    (isFormalGauge_conv B A z H₁ E hH₁ hE hz₁ hEB)).2
  have i2 := (phiKZ_swap_mul A B H₀ H₁ h₀ hH₀ h₁ hH₁).1
  rw [hsh] at i1
  calc _ = _ * (phiKZ B A H₁ H₀ h₁ hH₁ h₀ hH₀ * phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁) := by
        rw [i2, mul_one]
    _ = _ := by rw [← mul_assoc, i1, one_mul]

end Analytic

end QOU.KZ.KZShift

end
