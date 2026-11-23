import QOU.Mathlib.HadamardMinimumModulus
import QOU.Mathlib.HadamardQuotient

/-!
# Hadamard's factorisation theorem, assembled

Beans `qou-n4pv` / `qou-kp89`. This file discharges the class
`QOU.Mathlib.HadamardFactorization.HasHadamardFactorization`.

## Proved here (sorry-free, no new axioms)

* **The minimum-modulus degree bound over an arbitrary countable index type.**
  `QOU.Mathlib.HadamardMinimumModulus` proves the degree bound for an infinite
  `ℕ`-indexed zero sequence. The zero enumeration of `QOU.Mathlib.HadamardQuotient`
  is indexed by `zeroIndex f`, which is countable but may be finite or empty. The
  argument does not use infinitude, so it is restated here for `a : ι → ℂ`, `ι`
  countable: partial products along `Finset ι` (`exp_neg_le_norm_canonicalProduct`),
  the Lebesgue-measure choice of separated radii (`exists_separated_radius`, which is
  where countability is used), maximum modulus (`norm_exp_le_of_eq_exp_mul_canonicalProduct`),
  and Borel–Carathéodory + generalised Liouville
  (`exists_polynomial_of_eq_exp_mul_canonicalProduct`). The finite and empty cases are
  covered by the same proof, with no case split.
* **The assembly.** `hadamard_factorization_unconditional_statement`: the exact field
  statement of `HasHadamardFactorization`, from `hadamardQuotient_spec_of_order`
  (`f = q · P`, `q` entire and zero-free), `exists_entire_log` (`q = exp ∘ g`),
  `summable_divisor_mul_rpow_neg` + `summable_zeroSeq_rpow` (convergence exponent), and
  the degree bound above.
* `hadamard_factorization_unconditional : HasHadamardFactorization` (an instance).

## Not proved here

* Nothing about the *genus* being minimal: the genus used is `⌊ρ⌋₊`, which is what the
  class statement asks for (`p ≤ ρ`), not the least admissible genus.
* The constants are explicit and not sharp (inherited from `HadamardMinimumModulus`).

§7c: archimedean (norms, `Real.rpow`, complex analysis on `ℂ`).
-/

open Filter Topology Set Function

namespace QOU.Mathlib.HadamardAssembly

open QOU.Mathlib.HadamardFactorization
open QOU.Mathlib.HadamardMinimumModulus (minModConst two_le_minModConst
  exp_neg_le_norm_weierstrassFactor_div growthD growthD_nonneg exponent_le_growthD
  add_rpow_le_two_rpow_mul)

section General

variable {ι : Type*} {a : ι → ℂ}

/-- **Minimum modulus of the canonical product at a separated point**, arbitrary index
type. -/
theorem exp_neg_le_norm_canonicalProduct (p : ℕ) {σ : ℝ}
    (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ) (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun i => ‖a i‖ ^ (-σ))) {z : ℂ} (hz : 1 / 2 ≤ ‖z‖)
    (hsep : ∀ i, ‖a i‖ ^ (-σ) ≤ ‖z - a i‖) :
    Real.exp (-(minModConst p σ ‖z‖ * (∑' i, ‖a i‖ ^ (-σ)) * ‖z‖ ^ σ))
      ≤ ‖∏' i, weierstrassFactor p (z / a i)‖ := by
  classical
  set K := minModConst p σ ‖z‖
  have hK : 0 ≤ K := le_trans (by norm_num) (two_le_minModConst p hσ0.le hz)
  have hmult := QOU.Mathlib.HadamardQuotient.multipliable_canonicalProduct p ha hσ0 hσp hs z
  have htend := (hmult.hasProd).norm
  refine ge_of_tendsto' htend fun s => ?_
  have hnn : ∀ i, 0 ≤ ‖a i‖ ^ (-σ) := fun i => Real.rpow_nonneg (norm_nonneg _) _
  have hpart : ∑ i ∈ s, ‖a i‖ ^ (-σ) ≤ ∑' i, ‖a i‖ ^ (-σ) :=
    hs.sum_le_tsum _ (fun i _ => hnn i)
  have hrw : ∑ i ∈ s, K * ‖z / a i‖ ^ σ = K * ‖z‖ ^ σ * ∑ i ∈ s, ‖a i‖ ^ (-σ) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [QOU.Mathlib.CanonicalProductGrowth.norm_div_rpow]; ring
  have hc : 0 ≤ K * ‖z‖ ^ σ := mul_nonneg hK (Real.rpow_nonneg (norm_nonneg _) _)
  calc Real.exp (-(K * (∑' i, ‖a i‖ ^ (-σ)) * ‖z‖ ^ σ))
      ≤ Real.exp (∑ i ∈ s, -(K * ‖z / a i‖ ^ σ)) := by
        apply Real.exp_le_exp.mpr
        rw [Finset.sum_neg_distrib, hrw]
        have := mul_le_mul_of_nonneg_left hpart hc
        linarith
    _ = ∏ i ∈ s, Real.exp (-(K * ‖z / a i‖ ^ σ)) := Real.exp_sum _ _
    _ ≤ ∏ i ∈ s, ‖weierstrassFactor p (z / a i)‖ :=
        Finset.prod_le_prod (fun i _ => (Real.exp_pos _).le)
          (fun i _ => exp_neg_le_norm_weierstrassFactor_div p hσ0 hpσ hσp (ha i) hz (hsep i))

/-- **Separated radii exist in every window**, countable index type. -/
theorem exists_separated_radius [Countable ι] {σ : ℝ}
    (hs : Summable (fun i => ‖a i‖ ^ (-σ))) (R : ℝ) :
    ∃ r ∈ Set.Icc R (R + 2 * (∑' i, ‖a i‖ ^ (-σ)) + 1),
      ∀ i, ‖a i‖ ^ (-σ) < |r - ‖a i‖| := by
  set δ : ι → ℝ := fun i => ‖a i‖ ^ (-σ) with hδ
  set S := ∑' i, δ i with hS
  have hδ0 : ∀ i, 0 ≤ δ i := fun i => Real.rpow_nonneg (norm_nonneg _) _
  have hS0 : 0 ≤ S := tsum_nonneg hδ0
  by_contra hcon
  push_neg at hcon
  have hsub : Set.Icc R (R + 2 * S + 1) ⊆ ⋃ i, Set.Icc (‖a i‖ - δ i) (‖a i‖ + δ i) := by
    intro r hr
    obtain ⟨i, hi⟩ := hcon r hr
    refine Set.mem_iUnion.mpr ⟨i, ?_⟩
    have := abs_le.mp hi
    constructor <;> linarith [this.1, this.2]
  have hvol := MeasureTheory.measure_mono (μ := MeasureTheory.volume) hsub
  have hU : MeasureTheory.volume (⋃ i, Set.Icc (‖a i‖ - δ i) (‖a i‖ + δ i))
      ≤ ENNReal.ofReal (2 * S) := by
    refine (MeasureTheory.measure_iUnion_le _).trans ?_
    simp only [Real.volume_Icc]
    have h2 : ∀ i, ‖a i‖ + δ i - (‖a i‖ - δ i) = 2 * δ i := fun i => by ring
    simp only [h2]
    rw [← ENNReal.ofReal_tsum_of_nonneg (fun i => by linarith [hδ0 i]) (hs.mul_left 2),
      tsum_mul_left]
  rw [Real.volume_Icc] at hvol
  have hlt : ENNReal.ofReal (2 * S) < ENNReal.ofReal (R + 2 * S + 1 - R) :=
    (ENNReal.ofReal_lt_ofReal_iff (by linarith)).mpr (by linarith)
  exact absurd (hvol.trans hU) (not_le.mpr hlt)

/-- On a separated circle, every point is separated from every zero. -/
theorem separated_of_norm_eq {σ r : ℝ}
    (hr : ∀ i, ‖a i‖ ^ (-σ) < |r - ‖a i‖|) {z : ℂ} (hz : ‖z‖ = r) (i : ι) :
    ‖a i‖ ^ (-σ) ≤ ‖z - a i‖ := by
  have := abs_norm_sub_norm_le z (a i)
  rw [hz] at this
  linarith [hr i]

/-- **Growth transfer through the canonical product**, countable index type. -/
theorem norm_exp_le_of_eq_exp_mul_canonicalProduct [Countable ι] {f g : ℂ → ℂ} (p : ℕ)
    {ρ σ τ A C : ℝ} (hg : Differentiable ℂ g) (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ)
    (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1) (hs : Summable (fun i => ‖a i‖ ^ (-σ)))
    (hρτ : ρ ≤ τ) (hστ : σ < τ) (hC : 0 < C)
    (hbound : ∀ z, ‖f z‖ ≤ A * Real.exp (C * ‖z‖ ^ ρ))
    (hfac : ∀ z, f z = Complex.exp (g z) * ∏' i, weierstrassFactor p (z / a i)) :
    ∃ A' C' : ℝ, 0 < A' ∧ 0 < C' ∧
      ∀ z, ‖Complex.exp (g z)‖ ≤ A' * Real.exp (C' * ‖z‖ ^ τ) := by
  set S := ∑' i, ‖a i‖ ^ (-σ) with hSdef
  have hS : 0 ≤ S := tsum_nonneg fun i => Real.rpow_nonneg (norm_nonneg _) _
  set M : ℝ := 2 * S + 2 with hM
  have hM0 : 0 ≤ M := by linarith
  set A1 := max A 1 with hA1
  have hA1pos : 0 < A1 := lt_of_lt_of_le one_pos (le_max_right _ _)
  set D := growthD p σ τ C S with hDdef
  have hD : 0 ≤ D := growthD_nonneg p hσ0.le hστ hC.le hS
  have hτ0 : 0 ≤ τ := by linarith
  have h2τ : (0 : ℝ) ≤ 2 ^ τ := Real.rpow_nonneg (by norm_num) τ
  refine ⟨A1 * Real.exp (D * 2 ^ τ * M ^ τ), D * 2 ^ τ + 1,
    mul_pos hA1pos (Real.exp_pos _), by positivity, fun z => ?_⟩
  obtain ⟨r, ⟨hr1, hr2⟩, hsep⟩ := exists_separated_radius hs (max ‖z‖ 1)
  have hrge : 1 ≤ r := le_trans (le_max_right _ _) hr1
  have hzr : ‖z‖ ≤ r := le_trans (le_max_left _ _) hr1
  have hrM : r ≤ ‖z‖ + M := by
    have : max ‖z‖ 1 ≤ ‖z‖ + 1 := max_le (by linarith) (by linarith [norm_nonneg z])
    rw [hM]; linarith
  have hr0 : 0 < r := by linarith
  set B := C * r ^ ρ + minModConst p σ r * S * r ^ σ with hB
  have hcircle : ∀ w ∈ frontier (Metric.ball (0 : ℂ) r),
      ‖Complex.exp (g w)‖ ≤ A1 * Real.exp B := by
    intro w hw
    rw [frontier_ball _ hr0.ne', mem_sphere_zero_iff_norm] at hw
    have hP := exp_neg_le_norm_canonicalProduct p ha hσ0 hpσ hσp hs
      (by rw [hw]; norm_num; linarith) (separated_of_norm_eq hsep hw)
    rw [hw] at hP
    set P := ∏' i, weierstrassFactor p (w / a i)
    set e := ‖Complex.exp (g w)‖
    have he : 0 ≤ e := norm_nonneg _
    have hfw : e * ‖P‖ ≤ A1 * Real.exp (C * r ^ ρ) := by
      have h1 := hbound w
      rw [hfac w, norm_mul, hw] at h1
      exact h1.trans (mul_le_mul_of_nonneg_right (le_max_left _ _) (Real.exp_pos _).le)
    set E := minModConst p σ r * S * r ^ σ
    have hmul : e * Real.exp (-E) ≤ A1 * Real.exp (C * r ^ ρ) :=
      le_trans (mul_le_mul_of_nonneg_left hP he) hfw
    have hEE : Real.exp (-E) * Real.exp E = 1 := by rw [← Real.exp_add]; simp
    calc e = e * Real.exp (-E) * Real.exp E := by rw [mul_assoc, hEE, mul_one]
      _ ≤ A1 * Real.exp (C * r ^ ρ) * Real.exp E :=
          mul_le_mul_of_nonneg_right hmul (Real.exp_pos _).le
      _ = A1 * Real.exp B := by rw [mul_assoc, ← Real.exp_add]
  have hzmem : z ∈ closure (Metric.ball (0 : ℂ) r) := by
    rw [closure_ball _ hr0.ne']; simpa using hzr
  have hmax := Complex.norm_le_of_forall_mem_frontier_norm_le Metric.isBounded_ball
    (hg.cexp.diffContOnCl) hcircle hzmem
  refine hmax.trans ?_
  have hBD : B ≤ D * r ^ τ := exponent_le_growthD p hrge hσ0.le hστ hρτ hC.le hS
  have hrτ : r ^ τ ≤ (‖z‖ + M) ^ τ := Real.rpow_le_rpow hr0.le hrM hτ0
  have hsum := add_rpow_le_two_rpow_mul (norm_nonneg z) hM0 hτ0
  have hzτ : 0 ≤ ‖z‖ ^ τ := Real.rpow_nonneg (norm_nonneg _) τ
  have hfin : B ≤ D * 2 ^ τ * M ^ τ + (D * 2 ^ τ + 1) * ‖z‖ ^ τ := by
    have e1 := mul_le_mul_of_nonneg_left hrτ hD
    have e2 := mul_le_mul_of_nonneg_left hsum hD
    nlinarith
  calc A1 * Real.exp B ≤ A1 * Real.exp (D * 2 ^ τ * M ^ τ + (D * 2 ^ τ + 1) * ‖z‖ ^ τ) :=
        mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hfin) hA1pos.le
    _ = A1 * Real.exp (D * 2 ^ τ * M ^ τ) * Real.exp ((D * 2 ^ τ + 1) * ‖z‖ ^ τ) := by
        rw [Real.exp_add]; ring

/-- **The Hadamard degree bound**, countable (possibly finite or empty) index type. -/
theorem exists_polynomial_of_eq_exp_mul_canonicalProduct [Countable ι] {f g : ℂ → ℂ}
    {ρ : ℝ} (hρ : 0 ≤ ρ) (hf : IsEntireOfOrderLE f ρ) (hg : Differentiable ℂ g)
    (ha : ∀ i, a i ≠ 0) (hs : ∀ σ, ρ < σ → Summable (fun i => ‖a i‖ ^ (-σ)))
    (hfac : ∀ z, f z = Complex.exp (g z) * ∏' i, weierstrassFactor ⌊ρ⌋₊ (z / a i)) :
    ∃ Q : Polynomial ℂ, Q.natDegree ≤ ⌊ρ⌋₊ ∧ ∀ z, g z = Q.eval z := by
  obtain ⟨_, A, C, hC, hbound⟩ := hf
  set p := ⌊ρ⌋₊ with hp
  have hpρ : (p : ℝ) ≤ ρ := Nat.floor_le hρ
  have hρp : ρ < (p : ℝ) + 1 := Nat.lt_floor_add_one ρ
  have key : ∀ τ, ρ < τ → ∃ Q : Polynomial ℂ, (Q.natDegree : ℝ) ≤ τ ∧ ∀ z, g z = Q.eval z := by
    intro τ hτ
    set σ := min (ρ + (τ - ρ) / 2) ((p : ℝ) + 1) with hσ
    have hσρ : ρ < σ := lt_min (by linarith) hρp
    have hστ : σ < τ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
    have hσp : σ ≤ (p : ℝ) + 1 := min_le_right _ _
    have hσ0 : 0 < σ := lt_of_le_of_lt hρ hσρ
    obtain ⟨A', C', hA', hC', hb⟩ := norm_exp_le_of_eq_exp_mul_canonicalProduct p hg ha hσ0
      (le_trans hpρ hσρ.le) hσp (hs σ hσρ) hτ.le hστ hC hbound hfac
    have hτ0 : 0 ≤ τ := by linarith
    obtain ⟨K, hK⟩ := QOU.Mathlib.HadamardZeroFree.exists_norm_le_of_norm_exp_le hg hτ0 hC' hA' hb
    exact QOU.Mathlib.HadamardZeroFree.exists_polynomial_of_norm_le hg hτ0 hK
  obtain ⟨Q, -, hQ⟩ := key (ρ + 1) (by linarith)
  refine ⟨Q, ?_, hQ⟩
  have hdeg : (Q.natDegree : ℝ) ≤ ρ := by
    refine le_of_forall_gt_imp_ge_of_dense fun τ hτ => ?_
    obtain ⟨Q', hQ'deg, hQ'⟩ := key τ hτ
    have heq : Q' = Q := Polynomial.funext fun z => by rw [← hQ' z, hQ z]
    rw [← heq]; exact hQ'deg
  exact Nat.le_floor hdeg

end General

/-! ## The assembly -/

open QOU.Mathlib.HadamardQuotient

/-- **Hadamard's factorisation theorem** (the exact field statement of
`HasHadamardFactorization`). -/
theorem hadamard_factorization_unconditional_statement {f : ℂ → ℂ} {ρ : ℝ}
    (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0) (hρ : 0 ≤ ρ) :
    ∃ (p : ℕ) (g : Polynomial ℂ) (ι : Type) (_ : Countable ι) (a : ι → ℂ),
      (p : ℝ) ≤ ρ ∧
      (g.natDegree : ℝ) ≤ ρ ∧
      (∀ i, a i ≠ 0) ∧
      (∀ i, f (a i) = 0) ∧
      (∀ z, Multipliable (fun i => weierstrassFactor p (z / a i)) ∧
            f z = Complex.exp (g.eval z) * ∏' i, weierstrassFactor p (z / a i)) := by
  obtain ⟨hc, ha, hz, hqd, hq0, hfac⟩ := hadamardQuotient_spec_of_order hf hf0 hρ
  obtain ⟨h, hh, hqh⟩ := QOU.Mathlib.HadamardZeroFree.exists_entire_log hqd hq0
  have hs : ∀ σ, ρ < σ → Summable (fun i : zeroIndex f => ‖zeroSeq f i‖ ^ (-σ)) :=
    fun σ hσ => summable_zeroSeq_rpow hf.1
      (QOU.Mathlib.ExponentOfConvergence.summable_divisor_mul_rpow_neg hf hf0 hρ hσ)
  have hfac' : ∀ z, f z = Complex.exp (h z) *
      ∏' i, weierstrassFactor ⌊ρ⌋₊ (z / zeroSeq f i) := fun z => by
    rw [(hfac z).2, hqh z]
  obtain ⟨Q, hQdeg, hQ⟩ :=
    exists_polynomial_of_eq_exp_mul_canonicalProduct hρ hf hh ha hs hfac'
  have hQdeg' : (Q.natDegree : ℝ) ≤ ρ :=
    le_trans (by exact_mod_cast hQdeg) (Nat.floor_le hρ)
  refine ⟨⌊ρ⌋₊, Q, zeroIndex f, hc, zeroSeq f, Nat.floor_le hρ, hQdeg', ha, hz, fun z => ?_⟩
  refine ⟨(hfac z).1, ?_⟩
  rw [hfac' z, hQ z]

/-- **Hadamard's factorisation theorem**: the class `HasHadamardFactorization` holds. -/
instance hadamard_factorization_unconditional : HasHadamardFactorization :=
  ⟨fun hf hf0 hρ => hadamard_factorization_unconditional_statement hf hf0 hρ⟩

-- Ref: [leitner2026] standard: Conway, Functions of One Complex Variable I, XI §3 (Hadamard's factorization theorem); Titchmarsh, The Theory of Functions, §8.24

end QOU.Mathlib.HadamardAssembly
