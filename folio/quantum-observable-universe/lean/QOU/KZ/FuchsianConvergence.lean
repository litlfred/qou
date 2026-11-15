import QOU.KZ.FuchsianFormal
import Mathlib.Analysis.Normed.Ring.Lemmas
import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Analysis.SpecificLimits.Normed

/-!
# Convergence of the formal Fuchsian solution

Second brick of Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`. The file
`QOU.KZ.FuchsianFormal` builds the unique formal solution `H(z) = ∑ H_k z^k`, `H_0 = 1`, of the
gauge equation `z H' + H A = M H`. Here we show it **converges** wherever `M` does.

## The estimate

Work in a normed `ℝ`-algebra `R`. For `k ≥ 4‖A‖` the indicial operator is uniformly
injective with a `1/k` bound (`norm_le_of_indicial`):

  `k ‖X‖ ≤ 2 ‖k X − ad_A X‖`,

because `‖ad_A X‖ ≤ 2‖A‖‖X‖ ≤ (k/2)‖X‖`. With the recursion this gives
`‖H_k‖ ≤ (2/k) ∑_{j<k} ‖M_{k-j}‖ ‖H_j‖` (`norm_coeff_le`).

Suppose `‖M_m‖ ≤ C ρ^m` for `m ≥ 1`. For `r > 0` with `θ = rρ < 1`, put `h_k = ‖H_k‖ r^k`. Then
`h_k ≤ (2C/k) ∑_{j<k} θ^{k-j} h_j ≤ (2C/k) · θ/(1−θ) · max_{j<k} h_j`, and once
`k (1−θ) ≥ 2Cθ` the factor is `≤ 1`. So `h_k` is bounded (`bounded_weighted`), and
`∑ ‖H_k‖ s^k` converges for every `0 ≤ s < r` (`summable_norm_mul_pow`): **the radius of
convergence of `H` is at least `1/ρ`.** The proof is the classical majorant argument, done without
any complex analysis.

For the three-point KZ system `M_0 = A`, `M_k = −B`, so `C = ‖B‖`, `ρ = 1`, and `H` converges on
`|z| < 1` (`kz_summable`) — the full interval `(0,1)` on which the associator is defined.

## Not here

That `t ↦ H(t) t^A` is differentiable and solves the ODE on `(0,1)`, and `Φ_KZ`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1, §5
-/

namespace QOU.KZ.FuchsianConvergence

open Finset QOU.KZ.FuchsianFormal

variable {R : Type*} [NormedRing R] [NormedAlgebra ℝ R]


theorem natCast_mul_eq_smul (k : ℕ) (X : R) : (k : R) * X = (k : ℝ) • X := by
  rw [Nat.cast_smul_eq_nsmul, nsmul_eq_mul]

omit [NormedAlgebra ℝ R] in
theorem norm_ad_le (A X : R) : ‖ad A X‖ ≤ 2 * ‖A‖ * ‖X‖ := by
  unfold ad
  calc ‖A * X - X * A‖ ≤ ‖A * X‖ + ‖X * A‖ := norm_sub_le _ _
    _ ≤ ‖A‖ * ‖X‖ + ‖X‖ * ‖A‖ := add_le_add (norm_mul_le _ _) (norm_mul_le _ _)
    _ = 2 * ‖A‖ * ‖X‖ := by ring

/-- **Uniform injectivity of the indicial operator for large `k`.** -/
theorem norm_le_of_indicial (A X : R) (k : ℕ) (hk : 4 * ‖A‖ ≤ k) :
    (k : ℝ) * ‖X‖ ≤ 2 * ‖indicial A k X‖ := by
  have h1 : ‖(k : R) * X‖ = k * ‖X‖ := by
    rw [natCast_mul_eq_smul, norm_smul, Real.norm_natCast]
  have h2 : ‖(k : R) * X‖ ≤ ‖indicial A k X‖ + ‖ad A X‖ := by
    unfold indicial
    calc ‖(k : R) * X‖ = ‖((k : R) * X - ad A X) + ad A X‖ := by rw [sub_add_cancel]
      _ ≤ _ := norm_add_le _ _
  have h3 := norm_ad_le A X
  have hX := norm_nonneg X
  nlinarith

/-- **The coefficient estimate.** For a normalised formal solution and `k ≥ max(1, 4‖A‖)`,
`k ‖H_k‖ ≤ 2 ∑_{j<k} ‖M_{k-j}‖ ‖H_j‖`. -/
theorem norm_coeff_le (M H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge M H) (k : ℕ)
    (hk0 : 0 < k) (hk : 4 * ‖M 0‖ ≤ k) :
    (k : ℝ) * ‖H k‖ ≤ 2 * ∑ j ∈ range k, ‖M (k - j)‖ * ‖H j‖ := by
  have hrec := ((isFormalGauge_iff M H h0).1 hH) k hk0
  calc (k : ℝ) * ‖H k‖ ≤ 2 * ‖indicial (M 0) k (H k)‖ := norm_le_of_indicial _ _ _ hk
    _ = 2 * ‖∑ j ∈ range k, M (k - j) * H j‖ := by rw [hrec]
    _ ≤ 2 * ∑ j ∈ range k, ‖M (k - j) * H j‖ := by gcongr; exact norm_sum_le _ _
    _ ≤ 2 * ∑ j ∈ range k, ‖M (k - j)‖ * ‖H j‖ := by gcongr; exact norm_mul_le _ _

/-- `∑_{j<k} θ^{k-j} ≤ θ/(1−θ)` for `0 ≤ θ < 1`. -/
theorem sum_pow_sub_le (θ : ℝ) (h0 : 0 ≤ θ) (h1 : θ < 1) (k : ℕ) :
    ∑ j ∈ range k, θ ^ (k - j) ≤ θ / (1 - θ) := by
  have e : ∑ j ∈ range k, θ ^ (k - j) = θ * ∑ i ∈ range k, θ ^ i := by
    rw [mul_sum, ← sum_range_reflect]
    refine sum_congr rfl fun j hj => ?_
    have := mem_range.1 hj
    rw [← pow_succ']; congr 1; omega
  have hg : ∑ i ∈ range k, θ ^ i ≤ (1 - θ)⁻¹ := by
    rw [← tsum_geometric_of_lt_one h0 h1]
    exact (summable_geometric_of_lt_one h0 h1).sum_le_tsum _ (fun i _ => pow_nonneg h0 i)
  rw [e, div_eq_mul_inv]
  exact mul_le_mul_of_nonneg_left hg h0

/-- **Boundedness of the weighted coefficients** `‖H_k‖ r^k` when `‖M_m‖ ≤ C ρ^m` and
`r ρ < 1`. -/
theorem bounded_weighted (M H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge M H)
    (C ρ r : ℝ) (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hM : ∀ m, 0 < m → ‖M m‖ ≤ C * ρ ^ m) :
    ∃ D, ∀ k, ‖H k‖ * r ^ k ≤ D := by
  set θ := r * ρ with hθdef
  have hθ0 : 0 ≤ θ := mul_nonneg hr.le hρ
  have h1θ : 0 < 1 - θ := by linarith
  obtain ⟨k1, hk1⟩ := exists_nat_gt (4 * ‖M 0‖ + 2 * C * θ / (1 - θ) + 1)
  set D := ∑ j ∈ range k1, ‖H j‖ * r ^ j with hD
  have hDnn : 0 ≤ D := sum_nonneg fun j _ => by positivity
  refine ⟨D, fun k => ?_⟩
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    by_cases hk : k < k1
    · exact single_le_sum (f := fun j => ‖H j‖ * r ^ j) (fun j _ => by positivity)
        (mem_range.2 hk)
    push_neg at hk
    have hkpos : (0 : ℝ) < k := by
      have : (1 : ℝ) < k1 := by
        have : 0 ≤ 2 * C * θ / (1 - θ) := by positivity
        linarith [norm_nonneg (M 0)]
      exact lt_of_lt_of_le (by linarith) (Nat.cast_le.2 hk)
    have hk0 : 0 < k := by exact_mod_cast hkpos
    have hkbig : 4 * ‖M 0‖ + 2 * C * θ / (1 - θ) ≤ k := by
      have : (k1 : ℝ) ≤ k := Nat.cast_le.2 hk
      linarith
    have hk4 : 4 * ‖M 0‖ ≤ k := by
      have : 0 ≤ 2 * C * θ / (1 - θ) := by positivity
      linarith
    have hkθ : 2 * C * θ / (1 - θ) ≤ k := by linarith [norm_nonneg (M 0)]
    have hest := norm_coeff_le M H h0 hH k hk0 hk4
    -- weight everything by r^k
    have hterm : ∀ j ∈ range k,
        ‖M (k - j)‖ * ‖H j‖ * r ^ k ≤ C * (θ ^ (k - j) * D) := by
      intro j hj
      have hjk := mem_range.1 hj
      have hMj := hM (k - j) (by omega)
      have hrk : r ^ k = r ^ (k - j) * r ^ j := by rw [← pow_add]; congr 1; omega
      calc ‖M (k - j)‖ * ‖H j‖ * r ^ k
          ≤ C * ρ ^ (k - j) * ‖H j‖ * r ^ k := by gcongr
        _ = C * (θ ^ (k - j) * (‖H j‖ * r ^ j)) := by rw [hrk, hθdef, mul_pow]; ring
        _ ≤ C * (θ ^ (k - j) * D) := by gcongr; exact ih j hjk
    have hsum : (k : ℝ) * (‖H k‖ * r ^ k) ≤ 2 * C * D * (θ / (1 - θ)) := by
      calc (k : ℝ) * (‖H k‖ * r ^ k) = ((k : ℝ) * ‖H k‖) * r ^ k := by ring
        _ ≤ (2 * ∑ j ∈ range k, ‖M (k - j)‖ * ‖H j‖) * r ^ k := by gcongr
        _ = 2 * ∑ j ∈ range k, ‖M (k - j)‖ * ‖H j‖ * r ^ k := by rw [mul_assoc, sum_mul]
        _ ≤ 2 * ∑ j ∈ range k, C * (θ ^ (k - j) * D) :=
          mul_le_mul_of_nonneg_left (sum_le_sum hterm) (by norm_num)
        _ = 2 * C * D * ∑ j ∈ range k, θ ^ (k - j) := by
          rw [← mul_sum, ← sum_mul]; ring
        _ ≤ 2 * C * D * (θ / (1 - θ)) := by
          gcongr; exact sum_pow_sub_le θ hθ0 (by linarith) k
    have : 2 * C * D * (θ / (1 - θ)) ≤ (k : ℝ) * D := by
      have : 2 * C * θ / (1 - θ) * D ≤ (k : ℝ) * D := by gcongr
      calc 2 * C * D * (θ / (1 - θ)) = 2 * C * θ / (1 - θ) * D := by ring
        _ ≤ _ := this
    exact le_of_mul_le_mul_left (hsum.trans this) hkpos

/-- **Convergence**: under the hypotheses of `bounded_weighted`, `∑ ‖H_k‖ s^k` converges for
every `0 ≤ s < r`. -/
theorem summable_norm_mul_pow (M H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge M H)
    (C ρ r : ℝ) (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hM : ∀ m, 0 < m → ‖M m‖ ≤ C * ρ ^ m) (s : ℝ) (hs0 : 0 ≤ s) (hs : s < r) :
    Summable fun k => ‖H k‖ * s ^ k := by
  obtain ⟨D, hD⟩ := bounded_weighted M H h0 hH C ρ r hC hρ hr hθ hM
  have hq0 : 0 ≤ s / r := div_nonneg hs0 hr.le
  have hq1 : s / r < 1 := (div_lt_one hr).2 hs
  refine Summable.of_nonneg_of_le (fun k => by positivity) (fun k => ?_)
    ((summable_geometric_of_lt_one hq0 hq1).mul_left D)
  have hrk : 0 < r ^ k := pow_pos hr k
  calc ‖H k‖ * s ^ k = (‖H k‖ * r ^ k) * (s / r) ^ k := by
        rw [div_pow]; field_simp
    _ ≤ D * (s / r) ^ k := by gcongr; exact hD k

/-- **KZ**: the normalised formal solution at `z = 0` of the three-point KZ system converges on
`|z| < 1`, for any residues `A, B` (non-resonance is only needed for existence). -/
theorem kz_summable (A B : R) (H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge (kzM0 A B) H)
    (s : ℝ) (hs0 : 0 ≤ s) (hs : s < 1) :
    Summable fun k => ‖H k‖ * s ^ k := by
  refine summable_norm_mul_pow (kzM0 A B) H h0 hH ‖B‖ 1 ((1 + s) / 2) (norm_nonneg _)
    zero_le_one (by linarith) (by linarith) (fun m hm => ?_) s hs0 (by linarith)
  obtain ⟨m, rfl⟩ : ∃ n, m = n + 1 := ⟨m - 1, by omega⟩
  simp [kzM0]

end QOU.KZ.FuchsianConvergence
