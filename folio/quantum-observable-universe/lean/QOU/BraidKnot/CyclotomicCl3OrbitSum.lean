import Mathlib.NumberTheory.ZetaValues
import QOU.Infra.Polylogarithm

/-!
# General Cl_3 orbit sum at every N

Compiled formalisation of `prop:cyclotomic-cl3-orbit-sum-general`.
Sibling docstub at `braids-and-knots/cyclotomic-cl3-orbit-sum-general.lean`.
-/

namespace QOU.BraidKnot.CyclotomicCl3OrbitSum

open QOU.Infra.Polylogarithm

/-- **The `N = 5` closed form** (the Bring / `ζ₅` row of
    `prop:cyclotomic-cl3-orbit-sum-general`): the predicted orbit sum
    evaluates to `-(24/25) · ζ(3)`.

    **Restated 2026-08-21** (vacuity ledger, `proof-no-trivial-true` /
    `reflexive-tautology`).  This read
    `∀ N, 2 ≤ N → cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N zeta3`,
    closed by `rfl` — both binders decoration, the claim holding for every
    `N` and every `zeta3` with or without `2 ≤ N`.  Its own docstring
    conceded the RHS "equals itself by `rfl`", yet the name promised a
    general orbit-sum identity, so a reader grepping for whether that
    identity is established found a green `theorem`.

    What is genuinely derivable here is the arithmetic at the verified
    index — the same computation `defaultTheoremB.value_at_5` performs, so
    it needs no class instance.  The **general-`N`** identification of the
    predicted closed form with the analytic orbit sum `Σ_k Cl₃(2πk/N)` is
    `cl3_orbit_sum` below (proved 2026-11-21). -/
theorem orbit_sum_at_five (zeta3 : ℝ) :
    cl3OrbitSumPredicted 5 zeta3 = -(24 / 25) * zeta3 := by
  unfold cl3OrbitSumPredicted
  field_simp
  ring

/-- Adding the scaled constant to the predicted orbit sum at five cancels to zero (`qou-jtge`). -/
theorem orbit_sum_at_five_add_eq_zero (zeta3 : ℝ) :
    cl3OrbitSumPredicted 5 zeta3 + (24 / 25) * zeta3 = 0 := by
  rw [orbit_sum_at_five zeta3]
  ring


/-- Character sum over `N`-th roots of unity, real part. -/
theorem sum_cos_roots (N m : ℕ) (hN : 1 ≤ N) :
    ∑ k ∈ Finset.range N, Real.cos (2 * Real.pi * k * m / N)
      = if N ∣ m then (N : ℝ) else 0 := by
  have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast (show N ≠ 0 by omega)
  set z : ℂ := Complex.exp (2 * Real.pi * m / N * Complex.I) with hz
  have hterm : ∀ k : ℕ, Real.cos (2 * Real.pi * k * m / N) = (z ^ k).re := by
    intro k
    rw [hz, ← Complex.exp_nat_mul]
    have : (k : ℂ) * (2 * Real.pi * m / N * Complex.I)
        = ((2 * Real.pi * k * m / N : ℝ) : ℂ) * Complex.I := by
      push_cast; ring
    rw [this, Complex.exp_ofReal_mul_I_re]
  simp_rw [hterm]
  rw [← Complex.re_sum]
  by_cases hd : N ∣ m
  · obtain ⟨j, rfl⟩ := hd
    have hz1 : z = 1 := by
      rw [hz, Complex.exp_eq_one_iff]
      refine ⟨j, ?_⟩
      push_cast
      field_simp
    simp [hz1]
  · have hz1 : z ≠ 1 := by
      intro h
      rw [hz, Complex.exp_eq_one_iff] at h
      obtain ⟨n, hn⟩ := h
      have h2 : (m : ℂ) = n * N := by
        have hpi : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
          simp [Real.pi_ne_zero, Complex.I_ne_zero]
        field_simp at hn
        linear_combination hn
      have h3 : (m : ℤ) = n * N := by exact_mod_cast h2
      apply hd
      have : (N : ℤ) ∣ (m : ℤ) := ⟨n, by rw [h3]; ring⟩
      exact_mod_cast this
    have hzN : z ^ N = 1 := by
      rw [hz, ← Complex.exp_nat_mul, Complex.exp_eq_one_iff]
      exact ⟨m, by push_cast; field_simp⟩
    rw [geom_sum_eq hz1, hzN]
    simp [hd]

theorem summable_inv_cube : Summable (fun m : ℕ => 1 / (m : ℝ) ^ 3) :=
  Real.summable_one_div_nat_pow.mpr (by norm_num)

theorem tsum_multiples (N : ℕ) (hN : 1 ≤ N) :
    ∑' m : ℕ, (if N ∣ m then 1 / (m : ℝ) ^ 3 else 0)
      = (∑' m : ℕ, 1 / (m : ℝ) ^ 3) / (N : ℝ) ^ 3 := by
  have hinj : Function.Injective (fun j : ℕ => N * j) :=
    fun a b h => Nat.eq_of_mul_eq_mul_left (by omega) h
  have hsupp : Function.support (fun m : ℕ => if N ∣ m then 1 / (m : ℝ) ^ 3 else 0)
      ⊆ Set.range (fun j : ℕ => N * j) := by
    intro m hm
    by_contra h
    apply hm
    have : ¬ N ∣ m := fun ⟨j, hj⟩ => h ⟨j, hj.symm⟩
    simp [this]
  rw [← hinj.tsum_eq hsupp]
  simp only [dvd_mul_right, if_true]
  rw [← tsum_div_const]
  congr 1
  funext j
  push_cast
  have hN0 : (N : ℝ) ≠ 0 := by exact_mod_cast (show N ≠ 0 by omega)
  rcases eq_or_ne (j : ℝ) 0 with h | h
  · simp [h]
  · field_simp

/-- **Theorem B (the `Cl₃` orbit sum), for every `N ≥ 1`.** With
    `Cl₃(θ) = Σ_{m ≥ 1} cos(mθ)/m³` and `ζ(3) = Σ_{m ≥ 1} 1/m³`,
    `Σ_{k=1}^{N-1} Cl₃(2πk/N) = -((N² - 1)/N²)·ζ(3)`. -/
theorem cl3_orbit_sum (N : ℕ) (hN : 1 ≤ N) :
    ∑ k ∈ Finset.Ico 1 N, ∑' m : ℕ, Real.cos (2 * Real.pi * k * m / N) / (m : ℝ) ^ 3
      = cl3OrbitSumPredicted N (∑' m : ℕ, 1 / (m : ℝ) ^ 3) := by
  have hs : ∀ k : ℕ, Summable (fun m : ℕ => Real.cos (2 * Real.pi * k * m / N) / (m : ℝ) ^ 3) := by
    intro k
    refine summable_inv_cube.of_norm_bounded ?_
    intro m
    rw [Real.norm_eq_abs, abs_div, abs_of_nonneg (by positivity : (0:ℝ) ≤ (m:ℝ)^3)]
    rw [one_div]
    exact div_le_div_of_nonneg_right (Real.abs_cos_le_one _) (by positivity) |>.trans_eq (by ring)
  rw [← Summable.tsum_finsetSum (fun k _ => hs k)]
  have hrange : ∀ m : ℕ, ∑ k ∈ Finset.Ico 1 N, Real.cos (2 * Real.pi * k * m / N) / (m : ℝ) ^ 3
      = (N : ℝ) * (if N ∣ m then 1 / (m : ℝ) ^ 3 else 0) - 1 / (m : ℝ) ^ 3 := by
    intro m
    rw [← Finset.sum_div]
    have h := sum_cos_roots N m hN
    rw [Finset.range_eq_Ico, Finset.sum_eq_sum_Ico_succ_bot (by omega)] at h
    simp only [Nat.cast_zero, mul_zero, zero_mul, zero_div, Real.cos_zero] at h
    have h' : ∑ k ∈ Finset.Ico 1 N, Real.cos (2 * Real.pi * k * m / N)
        = (if N ∣ m then (N : ℝ) else 0) - 1 := by
      rw [← h]; simp
    rw [h']
    split_ifs <;> ring
  simp_rw [hrange]
  have hs2 : Summable (fun m : ℕ => if N ∣ m then 1 / (m : ℝ) ^ 3 else 0) := by
    refine summable_inv_cube.of_nonneg_of_le (fun m => ?_) (fun m => ?_)
    · split_ifs <;> positivity
    · split_ifs <;> [exact le_rfl; positivity]
  rw [Summable.tsum_sub (hs2.mul_left _) summable_inv_cube, tsum_mul_left,
    tsum_multiples N hN]
  unfold cl3OrbitSumPredicted
  have hN0 : (N : ℝ) ≠ 0 := by exact_mod_cast (show N ≠ 0 by omega)
  field_simp
  ring

end QOU.BraidKnot.CyclotomicCl3OrbitSum
