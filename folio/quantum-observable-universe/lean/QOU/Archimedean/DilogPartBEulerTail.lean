import QOU.Archimedean.DilogarithmArchimedeanLimit
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Analysis.Normed.Group.Tannery
import Mathlib.NumberTheory.ZetaValues

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the Euler-tail coefficient limit (V1)

The regularized negative-factor piece of Part B (`W-P2`) reduces, after the
substitution `p = 1/q` (`q→1⁺ ⟺ p→1⁻`) and `m = k − k*`, to the
**Euler-function / Dedekind-eta asymptotic**

`(1−p)·log ∏_{m≥1}(1−pᵐ) → −π²/6`   as `p → 1⁻`.

Via the Lambert series `log ∏(1−pᵐ) = −Σ_{j≥1}(1/j)·pʲ/(1−pʲ)` this is a
Tannery/dominated-convergence limit whose **termwise** input is the coefficient
limit proved here:

`(1−p)·pʲ/(1−pʲ) → 1/j`   as `p → 1⁻`,

after which `Σ_{j≥1} 1/j² = ζ(2) = π²/6` (`hasSum_zeta_two`) supplies the
constant. This is the cheap, load-bearing first brick (V1) of the Part-B
cusp-cancellation attack (`docs/coordination/dilog-part-b-cusp-attack.md`); the
Tannery exchange itself is V2.

The proof is elementary: `1 − pʲ = (1−p)·Σ_{i<j} pⁱ` (`geom_sum_mul`), so the
`(1−p)` cancels and the ratio is `pʲ / Σ_{i<j} pⁱ`, continuous at `p=1` with
value `1/j`.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.QPochhammer

open Filter Topology
open scoped BigOperators

/-- **V1 — Euler-tail termwise coefficient limit.**  As `p → 1⁻`, the `j`-th
    Lambert coefficient `(1−p)·pʲ/(1−pʲ)` tends to `1/j`.  Since
    `1 − pʲ = (1−p)·Σ_{i<j} pⁱ`, the `(1−p)` cancels, leaving `pʲ/Σ_{i<j}pⁱ`,
    whose limit at `p=1` is `1/j` (numerator `→ 1`, denominator `→ j`).  This is
    the termwise input to the Tannery/DCT giving the negative-factor Euler tail
    `(1−p)·log ∏(1−pᵐ) → −π²/6` (Part B, `W-P2`). -/
theorem euler_tail_coeff_limit (j : ℕ) (hj : 1 ≤ j) :
    Tendsto (fun p : ℝ => (1 - p) * p ^ j / (1 - p ^ j)) (𝓝[<] 1)
      (𝓝 (1 / (j : ℝ))) := by
  -- On `p < 1` the function equals `pʲ / Σ_{i<j} pⁱ`.
  have hcong : (fun p : ℝ => (1 - p) * p ^ j / (1 - p ^ j))
      =ᶠ[𝓝[<] 1] (fun p : ℝ => p ^ j / ∑ i ∈ Finset.range j, p ^ i) := by
    filter_upwards [self_mem_nhdsWithin] with p hp
    have hp1 : p < 1 := hp
    have hsum : (1 : ℝ) - p ^ j = (1 - p) * ∑ i ∈ Finset.range j, p ^ i := by
      have h2 : (∑ i ∈ Finset.range j, p ^ i) * (p - 1) = p ^ j - 1 :=
        geom_sum_mul p j
      linear_combination h2
    rw [hsum, mul_div_mul_left _ _ (sub_pos.mpr hp1).ne']
  refine Tendsto.congr' hcong.symm ?_
  -- Numerator `pʲ → 1`.
  have hnum : Tendsto (fun p : ℝ => p ^ j) (𝓝[<] (1 : ℝ)) (𝓝 (1 : ℝ)) := by
    have h := (continuous_pow j).tendsto (1 : ℝ)
    simpa using h.mono_left nhdsWithin_le_nhds
  -- Denominator `Σ_{i<j} pⁱ → j`.
  have hden : Tendsto (fun p : ℝ => ∑ i ∈ Finset.range j, p ^ i) (𝓝[<] (1 : ℝ))
      (𝓝 (j : ℝ)) := by
    have hc : Continuous (fun p : ℝ => ∑ i ∈ Finset.range j, p ^ i) :=
      continuous_finset_sum _ (fun i _ => continuous_pow i)
    have h := hc.tendsto (1 : ℝ)
    simp only [one_pow, Finset.sum_const, Finset.card_range, nsmul_eq_mul,
      mul_one] at h
    exact h.mono_left nhdsWithin_le_nhds
  have hjne : (j : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  simpa using hnum.div hden hjne

/-- **V1 — Euler-tail coefficient uniform bound.**  For `0 < p < 1` and `j ≥ 1`,
    `(1−p)·pʲ/(1−pʲ) ≤ 1/j`.  Together with `euler_tail_coeff_limit` (the termwise
    limit `→ 1/j`) this is the second Tannery/dominated-convergence input for
    `W-P2`: the coefficient times `1/j` is dominated by the summable `1/j²`.
    Proof: `(1−p)pʲ/(1−pʲ) = pʲ/Σ_{i<j}pⁱ`, and each of the `j` summands
    `pⁱ (i<j)` is `≥ pʲ`, so `Σ_{i<j}pⁱ ≥ j·pʲ`. -/
theorem euler_tail_coeff_le {j : ℕ} (hj : 1 ≤ j) {p : ℝ} (hp0 : 0 < p)
    (hp1 : p < 1) : (1 - p) * p ^ j / (1 - p ^ j) ≤ 1 / (j : ℝ) := by
  have hspos : 0 < ∑ i ∈ Finset.range j, p ^ i :=
    Finset.sum_pos (fun i _ => pow_pos hp0 i)
      (Finset.nonempty_range_iff.mpr (by omega))
  have hsum : (1 : ℝ) - p ^ j = (1 - p) * ∑ i ∈ Finset.range j, p ^ i := by
    have h2 : (∑ i ∈ Finset.range j, p ^ i) * (p - 1) = p ^ j - 1 :=
      geom_sum_mul p j
    linear_combination h2
  have heq : (1 - p) * p ^ j / (1 - p ^ j) = p ^ j / ∑ i ∈ Finset.range j, p ^ i := by
    rw [hsum, mul_div_mul_left _ _ (sub_pos.mpr hp1).ne']
  have hjpos : (0 : ℝ) < (j : ℝ) := by exact_mod_cast (by omega : (0 : ℕ) < j)
  -- `Σ_{i<j} pⁱ ≥ j·pʲ` since each of the `j` summands is `≥ pʲ`.
  have hbound : (j : ℝ) * p ^ j ≤ ∑ i ∈ Finset.range j, p ^ i := by
    have hterm : ∀ i ∈ Finset.range j, p ^ j ≤ p ^ i := by
      intro i hi
      exact pow_le_pow_of_le_one hp0.le hp1.le (Finset.mem_range.mp hi).le
    have hle := Finset.card_nsmul_le_sum (Finset.range j) (fun i => p ^ i) (p ^ j) hterm
    rwa [Finset.card_range, nsmul_eq_mul] at hle
  rw [heq, div_le_iff₀ hspos]
  calc p ^ j = 1 / (j : ℝ) * ((j : ℝ) * p ^ j) := by field_simp
    _ ≤ 1 / (j : ℝ) * ∑ i ∈ Finset.range j, p ^ i :=
        mul_le_mul_of_nonneg_left hbound (by positivity)

/-- Positivity of the `j`-th Lambert coefficient for `0 < p < 1`, `j ≥ 1`. -/
theorem euler_tail_coeff_nonneg {j : ℕ} (hj : 1 ≤ j) {p : ℝ} (hp0 : 0 < p)
    (hp1 : p < 1) : 0 ≤ (1 - p) * p ^ j / (1 - p ^ j) := by
  have hpj1 : p ^ j < 1 := pow_lt_one₀ hp0.le hp1 (by omega)
  apply div_nonneg (mul_nonneg (by linarith) (by positivity))
  linarith

/-- **V2 (heart) — the Lambert `j`-series limit.**  The negative-factor Euler tail
    in its Lambert form converges to `ζ(2) = π²/6` as `p → 1⁻`:

    `Σ_{j} (1/j)·(1−p)·pʲ/(1−pʲ) → Σ_{j} 1/j² = π²/6`.

    This is Tannery's theorem (`tendsto_tsum_of_dominated_convergence`) applied to
    the two V1 inputs: termwise `(1/j)·(1−p)pʲ/(1−pʲ) → 1/j²`
    (`euler_tail_coeff_limit`), uniformly dominated by the summable `1/j²`
    (`euler_tail_coeff_le` + `euler_tail_coeff_nonneg`), with `Σ 1/j² = π²/6`
    (`hasSum_zeta_two`).  The Lambert rearrangement
    `−log ∏(1−pᵐ) = Σⱼ (1/j)·pʲ/(1−pʲ)` (which turns this into the eta asymptotic
    `(1−p)·log ∏(1−pᵐ) → −π²/6`) is the remaining W-P2 step. -/
theorem euler_tail_jseries_tendsto :
    Tendsto (fun p : ℝ => ∑' j : ℕ, (1 / (j : ℝ)) * ((1 - p) * p ^ j / (1 - p ^ j)))
      (𝓝[<] 1) (𝓝 (Real.pi ^ 2 / 6)) := by
  have hpos : ∀ᶠ p in 𝓝[<] (1 : ℝ), (0 : ℝ) < p := by
    have hmem : Set.Ioi (0 : ℝ) ∈ 𝓝 (1 : ℝ) := Ioi_mem_nhds (by norm_num)
    exact (Filter.eventually_of_mem hmem (fun p hp => Set.mem_Ioi.mp hp)).filter_mono
      nhdsWithin_le_nhds
  rw [← hasSum_zeta_two.tsum_eq]
  refine tendsto_tsum_of_dominated_convergence (bound := fun j : ℕ => 1 / (j : ℝ) ^ 2)
    hasSum_zeta_two.summable ?_ ?_
  · -- termwise limit
    intro j
    rcases Nat.eq_zero_or_pos j with hj0 | hj1
    · subst hj0
      simp only [Nat.cast_zero, one_div, inv_zero, zero_mul, ne_eq, OfNat.ofNat_ne_zero,
        not_false_eq_true, zero_pow]
      simp
    · have hlim := (euler_tail_coeff_limit j hj1).const_mul (1 / (j : ℝ))
      have heq : (1 / (j : ℝ)) * (1 / (j : ℝ)) = 1 / (j : ℝ) ^ 2 := by
        rw [div_mul_div_comm, one_mul, ← pow_two]
      rwa [heq] at hlim
  · -- uniform domination
    filter_upwards [self_mem_nhdsWithin, hpos] with p hp1 hp0
    intro j
    rcases Nat.eq_zero_or_pos j with hj0 | hj1
    · subst hj0; simp
    · have hp1' : p < 1 := hp1
      have hcn := euler_tail_coeff_nonneg hj1 hp0 hp1'
      have hcle := euler_tail_coeff_le hj1 hp0 hp1'
      rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (by positivity) hcn)]
      calc (1 / (j : ℝ)) * ((1 - p) * p ^ j / (1 - p ^ j))
          ≤ (1 / (j : ℝ)) * (1 / (j : ℝ)) := mul_le_mul_of_nonneg_left hcle (by positivity)
        _ = 1 / (j : ℝ) ^ 2 := by rw [div_mul_div_comm, one_mul, ← pow_two]

/-- **V2a — the Lambert rearrangement.**  For `0 < p < 1`, the negative-factor
    Euler tail (in tsum-of-logs form) equals its Lambert `j`-series:

    `Σ'_m −log(1−p^{m+1}) = Σ'_j (1/(j+1))·p^{j+1}/(1−p^{j+1})`.

    A nonneg Fubini (`Summable.tsum_comm`) on `a m j = p^{(m+1)(j+1)}/(j+1)`:
    the row sum is `−log(1−p^{m+1})` (`neg_log_one_sub_hasSum`), the column sum is
    the geometric `(1/(j+1))·p^{j+1}/(1−p^{j+1})`.  Combined with
    `euler_tail_jseries_tendsto` this yields the eta asymptotic
    `(1−p)·Σ'_m −log(1−p^{m+1}) → π²/6`. -/
theorem euler_tail_lambert_rearrange {p : ℝ} (hp0 : 0 < p) (hp1 : p < 1) :
    ∑' m : ℕ, (-Real.log (1 - p ^ (m + 1)))
      = ∑' j : ℕ, (1 / ((j : ℝ) + 1)) * (p ^ (j + 1) / (1 - p ^ (j + 1))) := by
  let a : ℕ → ℕ → ℝ := fun m j => p ^ ((m + 1) * (j + 1)) / ((j : ℝ) + 1)
  have ha : ∀ m j, a m j = p ^ ((m + 1) * (j + 1)) / ((j : ℝ) + 1) := fun _ _ => rfl
  have hann : ∀ m j, 0 ≤ a m j := fun m j =>
    div_nonneg (pow_nonneg hp0.le _) (by positivity)
  -- geometric column value
  have hgeom : ∀ j : ℕ, ∑' m : ℕ, (p ^ (j + 1)) ^ (m + 1)
      = p ^ (j + 1) / (1 - p ^ (j + 1)) := by
    intro j
    have hr1 : p ^ (j + 1) < 1 := pow_lt_one₀ hp0.le hp1 (by omega)
    have hs := (hasSum_geometric_of_lt_one (pow_nonneg hp0.le _) hr1).mul_left (p ^ (j + 1))
    have hfun : (fun n => p ^ (j + 1) * (p ^ (j + 1)) ^ n)
        = (fun n => (p ^ (j + 1)) ^ (n + 1)) := by funext n; rw [← pow_succ']
    rw [hfun] at hs
    rw [hs.tsum_eq, div_eq_mul_inv]
  -- uncurried summability, by comparison with the product-geometric `pᵐ·pʲ`
  have hunc : Summable (Function.uncurry a) := by
    have hgm : Summable (fun x : ℕ × ℕ => p ^ x.1 * p ^ x.2) :=
      Summable.mul_of_nonneg (hasSum_geometric_of_lt_one hp0.le hp1).summable
        (hasSum_geometric_of_lt_one hp0.le hp1).summable
        (fun n => pow_nonneg hp0.le n) (fun n => pow_nonneg hp0.le n)
    refine Summable.of_nonneg_of_le (fun mj => hann mj.1 mj.2) ?_ hgm
    rintro ⟨m, j⟩
    have hle1 : a m j ≤ p ^ ((m + 1) * (j + 1)) := by
      rw [ha]
      exact div_le_self (pow_nonneg hp0.le _)
        (by have := Nat.cast_nonneg (α := ℝ) j; linarith)
    have hle2 : p ^ ((m + 1) * (j + 1)) ≤ p ^ (m + j) :=
      pow_le_pow_of_le_one hp0.le hp1.le (by nlinarith)
    calc Function.uncurry a (m, j) = a m j := rfl
      _ ≤ p ^ ((m + 1) * (j + 1)) := hle1
      _ ≤ p ^ (m + j) := hle2
      _ = p ^ m * p ^ j := pow_add p m j
  -- rows and columns
  have hrow : ∀ m, ∑' j, a m j = -Real.log (1 - p ^ (m + 1)) := by
    intro m
    have hy : |p ^ (m + 1)| < 1 := by
      rw [abs_of_nonneg (pow_nonneg hp0.le _)]; exact pow_lt_one₀ hp0.le hp1 (by omega)
    rw [← (neg_log_one_sub_hasSum hy).tsum_eq]
    exact tsum_congr (fun j => by rw [ha, ← pow_mul])
  have hcol : ∀ j, ∑' m, a m j
      = (1 / ((j : ℝ) + 1)) * (p ^ (j + 1) / (1 - p ^ (j + 1))) := by
    intro j
    have hstep : ∀ m, a m j = (1 / ((j : ℝ) + 1)) * (p ^ (j + 1)) ^ (m + 1) := by
      intro m; rw [ha, mul_comm (m + 1) (j + 1), pow_mul]; ring
    rw [tsum_congr hstep, tsum_mul_left, hgeom j]
  calc ∑' m : ℕ, (-Real.log (1 - p ^ (m + 1)))
      = ∑' m, ∑' j, a m j := tsum_congr (fun m => (hrow m).symm)
    _ = ∑' j, ∑' m, a m j := (hunc.tsum_comm).symm
    _ = ∑' j : ℕ, (1 / ((j : ℝ) + 1)) * (p ^ (j + 1) / (1 - p ^ (j + 1))) :=
        tsum_congr hcol

/-- **V2 (capstone) — the Euler-function / Dedekind-eta asymptotic (`W-P2`).**  The
    negative-factor Euler tail, rescaled by `(1−p)`, converges to `ζ(2) = π²/6`:

    `(1−p)·Σ'_m −log(1−p^{m+1}) → π²/6`   as `p → 1⁻`,

    equivalently `(1−p)·log ∏_{m≥1}(1−pᵐ) → −π²/6` (the classical Hardy–Ramanujan
    eta asymptotic).  Assembles V2a (`euler_tail_lambert_rearrange`) with V2b
    (`euler_tail_jseries_tendsto`): the `(1−p)`-scaled Lambert `j`-series is the
    V2b summand reindexed by the vanishing `j=0` term.  With `p = 1/q`
    (`q→1⁺ ⟺ p→1⁻`) this is exactly the regularized negative-factor piece of
    Part B (`W-P2 → −π²/6`), one of the two halves of `Li₂(x) − π²/3`. -/
theorem euler_tail_asymptotic :
    Tendsto (fun p : ℝ => (1 - p) * ∑' m : ℕ, (-Real.log (1 - p ^ (m + 1))))
      (𝓝[<] 1) (𝓝 (Real.pi ^ 2 / 6)) := by
  have hpos : ∀ᶠ p in 𝓝[<] (1 : ℝ), (0 : ℝ) < p := by
    have hmem : Set.Ioi (0 : ℝ) ∈ 𝓝 (1 : ℝ) := Ioi_mem_nhds (by norm_num)
    exact (Filter.eventually_of_mem hmem (fun p hp => Set.mem_Ioi.mp hp)).filter_mono
      nhdsWithin_le_nhds
  refine euler_tail_jseries_tendsto.congr' ?_
  filter_upwards [self_mem_nhdsWithin, hpos] with p hp1 hp0
  have hp1' : p < 1 := hp1
  have hGsum : Summable
      (fun j : ℕ => (1 / (j : ℝ)) * ((1 - p) * p ^ j / (1 - p ^ j))) := by
    refine Summable.of_nonneg_of_le (fun j => ?_) (fun j => ?_) hasSum_zeta_two.summable
    · rcases Nat.eq_zero_or_pos j with h | h
      · subst h; simp
      · exact mul_nonneg (by positivity) (euler_tail_coeff_nonneg h hp0 hp1')
    · rcases Nat.eq_zero_or_pos j with h | h
      · subst h; simp
      · rw [show (1 : ℝ) / (j : ℝ) ^ 2 = (1 / (j : ℝ)) * (1 / (j : ℝ)) by
              rw [div_mul_div_comm, one_mul, ← pow_two]]
        exact mul_le_mul_of_nonneg_left (euler_tail_coeff_le h hp0 hp1') (by positivity)
  rw [hGsum.tsum_eq_zero_add]
  simp only [Nat.cast_zero, one_div, zero_mul, pow_zero, sub_self, div_zero,
    zero_add]
  rw [euler_tail_lambert_rearrange hp0 hp1', ← tsum_mul_left]
  refine tsum_congr (fun j => ?_)
  push_cast
  ring

end QOU.QPochhammer
