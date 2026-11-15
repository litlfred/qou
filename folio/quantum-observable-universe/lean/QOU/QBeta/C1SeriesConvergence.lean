import Mathlib.Tactic
import Mathlib.Analysis.SpecificLimits.Normed

/-!
# Where the C1 series solutions converge

Bean `qou-c1ln` row 3. The connection matrix `P = Y₀⁻¹Y_∞` of the ramified C1
operator is assembled from two series
(`computations/qbeta/c3_w2_c1_pole_divisor.py`):

* the **`0`-side** `∑_k g_k z^k`, with `g₀ = 1`, `g₁ = 0` and

      g_{k+2} = t²p^{2(k+2)} / (t²p^{2(k+2)} + (q−1)tp^{k+2} + (q−1)) · g_k

* the **`∞`-side** `∑_k h_k z^{−k}`, with `h₀ = 1` and a two-term recursion whose
  coefficients carry `p^{−k}` and `p^{−2k}` against a denominator tending to the
  constant `1 − p²`.

Everything downstream — `Y₀`, `Y_∞`, the inverse, the divisor — presupposes that
these converge where they are used. That was numerical. This file derives it.

## What this file proves

* `summable_zeroSideCoeff` — the `0`-side series converges for every `‖z‖ < 1`.
  The ratio tends to `1` like `1 + O(‖p‖^{−k})`, so the coefficients are
  **bounded**, which is all that radius `≥ 1` needs.
* `summable_infSideCoeff` — the `∞`-side series is **entire**: it converges for
  every `u`. The two recursion coefficients vanish geometrically while the
  denominator tends to a nonzero constant.

## Reusable infrastructure

Three of the lemmas are about sequences and say nothing about C1; they are
stated and proved in the general form because Mathlib has none of them:

* `norm_le_of_ratio_le_one_add_geometric` — a two-step recursion whose ratio is
  `1 + O(geometric)` has **bounded** terms. The telescoped product `∏(1 + Cρᵏ)`
  is controlled by `exp (C ∑ ρᵏ) ≤ exp (C/(1−ρ))`.
* `summable_of_norm_coeff_le` — bounded coefficients ⇒ convergence on the open
  unit disc.
* `summable_of_two_step_geometric` — a two-step recursion whose coefficients
  vanish geometrically gives an **entire** series. The majorant is
  `M ∏_{j<k} (cσʲ)` with `σ = √ρ`: the two-step lag costs exactly a square
  root, and `σ² = ρ` is what lets the induction close with a constant `c`
  instead of a `k`-dependent one.

All three take the recursion hypothesis only for `k ≥ K`, since in both C1
applications the estimate only holds once the geometric tail has overtaken the
constant term — for the `∞`-side that is also what keeps the denominator away
from zero.

## What this file does NOT prove — stated so it is not read for more

* **Sharpness of the `0`-side radius.** Proved here is radius `≥ 1`; that it is
  *exactly* `1` needs the mirror-image estimate `‖ratio‖ ≥ 1 − Cρᵏ` and hence
  `∏(1 − Cρᵏ) > 0`, giving a positive lower bound on the even coefficients and
  so divergence for `‖z‖ > 1`. The route is the same shape as the upper bound
  (`1 − x ≥ exp(−2x)` for `0 ≤ x ≤ ½`, from `exp(2x) ≥ 1 + 2x`), and is not
  taken here. Nothing downstream uses sharpness: the singularity's *location*
  is pinned by the `θ_p` zeros, not by this radius.
* ~~**That these series solve the q-difference equation.**~~ **Partly closed
  2026-08-08**: both recursions are now *derived* from the operator — see the
  section at the bottom of this file (`zeroCoeffAt_eq_zero_iff`,
  `infCoeffAt_eq_zero_iff`), with the coefficient collections machine-checked
  symbolically. What is still open is that these series, times their theta
  prefactors, are the *canonical* solutions at `0` and `∞` — the normalisation
  and uniqueness, not the recursion. That is row 4.
* **`Y₀`, `Y_∞`, the inverse, meromorphy** — bean `qou-c1ln` row 4, untouched.

-- Ref: [leitner2026] computations/qbeta/c3_w2_c1_pole_divisor.py
-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
-/

namespace QOU.QBeta.C1Series

/-! General infrastructure — nothing about C1 enters. -/

/-- Partial geometric sums are bounded by `(1-ρ)⁻¹`. -/
private lemma geom_partial_le {ρ : ℝ} (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1) (k : ℕ) :
    ∑ j ∈ Finset.range k, ρ ^ j ≤ (1 - ρ)⁻¹ := by
  have hs : Summable (fun j : ℕ => ρ ^ j) := summable_geometric_of_lt_one hρ0 hρ1
  calc ∑ j ∈ Finset.range k, ρ ^ j
      ≤ ∑' j : ℕ, ρ ^ j := hs.sum_le_tsum _ (fun j _ => pow_nonneg hρ0 j)
    _ = (1 - ρ)⁻¹ := tsum_geometric_of_lt_one hρ0 hρ1

/-- **A two-step recursion whose ratio is `1 + O(geometric)` has bounded terms.**

If `‖a (k+2)‖ ≤ (1 + Cρᵏ)‖a k‖` for all `k ≥ K`, with `0 ≤ ρ < 1`, then `‖a‖`
is bounded by an explicit constant: the telescoped product `∏(1 + Cρᵏ)` is
controlled by `exp (C ∑ ρᵏ) ≤ exp (C/(1-ρ))`, and the finitely many terms below
the threshold are absorbed into the sum `∑_{j < K+2} ‖a j‖`. -/
theorem norm_le_of_ratio_le_one_add_geometric {a : ℕ → ℂ} {C ρ : ℝ} {K : ℕ}
    (hC : 0 ≤ C) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (h : ∀ k, K ≤ k → ‖a (k + 2)‖ ≤ (1 + C * ρ ^ k) * ‖a k‖) (k : ℕ) :
    ‖a k‖ ≤ (∑ j ∈ Finset.range (K + 2), ‖a j‖) * Real.exp (C * (1 - ρ)⁻¹) := by
  set A : ℝ := ∑ j ∈ Finset.range (K + 2), ‖a j‖ with hA
  have hA0 : 0 ≤ A := Finset.sum_nonneg fun j _ => norm_nonneg _
  -- the sharper, index-dependent bound
  have key : ∀ m : ℕ, ‖a m‖ ≤ A * Real.exp (C * ∑ j ∈ Finset.range m, ρ ^ j) := by
    intro m
    induction m using Nat.strong_induction_on with
    | _ m ih =>
      have hexp1 : (1:ℝ) ≤ Real.exp (C * ∑ j ∈ Finset.range m, ρ ^ j) :=
        Real.one_le_exp (by positivity)
      by_cases hm : m < K + 2
      · have : ‖a m‖ ≤ A :=
          Finset.single_le_sum (f := fun j => ‖a j‖) (fun j _ => norm_nonneg _)
            (Finset.mem_range.mpr hm)
        nlinarith [norm_nonneg (a m)]
      · push_neg at hm
        obtain ⟨n, rfl⟩ : ∃ n, m = n + 2 := ⟨m - 2, by omega⟩
        have hnK : K ≤ n := by omega
        have hstep := h n hnK
        have hIH := ih n (by omega)
        have hfac : (0:ℝ) ≤ 1 + C * ρ ^ n := by positivity
        have hle : (1 : ℝ) + C * ρ ^ n ≤ Real.exp (C * ρ ^ n) := by
          have := Real.add_one_le_exp (C * ρ ^ n)
          linarith
        have hsplit : ∑ j ∈ Finset.range (n + 2), ρ ^ j
            = (∑ j ∈ Finset.range n, ρ ^ j) + ρ ^ n + ρ ^ (n + 1) := by
          rw [Finset.sum_range_succ, Finset.sum_range_succ]
        calc ‖a (n + 2)‖
            ≤ (1 + C * ρ ^ n) * ‖a n‖ := hstep
          _ ≤ Real.exp (C * ρ ^ n)
                * (A * Real.exp (C * ∑ j ∈ Finset.range n, ρ ^ j)) := by
              have h1 : (0:ℝ) ≤ Real.exp (C * ρ ^ n) := (Real.exp_pos _).le
              nlinarith [norm_nonneg (a n), Real.exp_pos (C * ρ ^ n)]
          _ = A * Real.exp (C * ((∑ j ∈ Finset.range n, ρ ^ j) + ρ ^ n)) := by
              rw [mul_add, Real.exp_add]; ring
          _ ≤ A * Real.exp (C * ∑ j ∈ Finset.range (n + 2), ρ ^ j) := by
              rw [hsplit]
              have : C * ((∑ j ∈ Finset.range n, ρ ^ j) + ρ ^ n)
                  ≤ C * ((∑ j ∈ Finset.range n, ρ ^ j) + ρ ^ n + ρ ^ (n + 1)) := by
                have : (0:ℝ) ≤ ρ ^ (n + 1) := pow_nonneg hρ0 _
                nlinarith
              exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr this) hA0
  refine (key k).trans (mul_le_mul_of_nonneg_left ?_ hA0)
  exact Real.exp_le_exp.mpr
    (mul_le_mul_of_nonneg_left (geom_partial_le hρ0 hρ1 k) hC)

/-- **Bounded coefficients ⇒ the power series converges on the open unit disc.**

i.e. radius of convergence `≥ 1`. -/
theorem summable_of_norm_coeff_le {a : ℕ → ℂ} {M : ℝ} (hM : ∀ k, ‖a k‖ ≤ M)
    {z : ℂ} (hz : ‖z‖ < 1) : Summable (fun k => a k * z ^ k) := by
  have hM0 : 0 ≤ M := le_trans (norm_nonneg (a 0)) (hM 0)
  refine Summable.of_norm_bounded (g := fun k => M * ‖z‖ ^ k) ?_ ?_
  · exact (summable_geometric_of_lt_one (norm_nonneg z) hz).mul_left M
  · intro k
    rw [norm_mul, norm_pow]
    exact mul_le_mul_of_nonneg_right (hM k) (pow_nonneg (norm_nonneg z) k)

/-! ### The C1 `0`-side series -/

/-- The `0`-side recursion's ratio, `t²p^{2k} / (t²p^{2k} + (q−1)tp^k + (q−1))`. -/
noncomputable def zeroSideRatio (p q t : ℂ) (k : ℕ) : ℂ :=
  t ^ 2 * p ^ (2 * k) / (t ^ 2 * p ^ (2 * k) + (q - 1) * t * p ^ k + (q - 1))

/-- The relative size of the subleading part of the denominator. -/
noncomputable def zeroSideTail (p q t : ℂ) (k : ℕ) : ℂ :=
  ((q - 1) * t * p ^ k + (q - 1)) / (t ^ 2 * p ^ (2 * k))

/-- `0`-side coefficients: `g₀ = 1`, `g₁ = 0`, `g_{k+2} = ratio(k+2)·g_k`. -/
noncomputable def zeroSideCoeff (p q t : ℂ) : ℕ → ℂ
  | 0 => 1
  | 1 => 0
  | (k + 2) => zeroSideRatio p q t (k + 2) * zeroSideCoeff p q t k

lemma zeroSideRatio_eq (p q t : ℂ) (ht : t ≠ 0) (hp : p ≠ 0) (k : ℕ) :
    zeroSideRatio p q t k = (1 + zeroSideTail p q t k)⁻¹ := by
  have hN : t ^ 2 * p ^ (2 * k) ≠ 0 := mul_ne_zero (pow_ne_zero _ ht) (pow_ne_zero _ hp)
  have hsplit : (1 : ℂ) + zeroSideTail p q t k
      = (t ^ 2 * p ^ (2 * k) + ((q - 1) * t * p ^ k + (q - 1))) / (t ^ 2 * p ^ (2 * k)) := by
    rw [zeroSideTail]; field_simp
  rw [hsplit, inv_div, zeroSideRatio]
  congr 1
  ring

lemma norm_zeroSideTail_le (p q t : ℂ) (ht : t ≠ 0) (hp : 1 < ‖p‖) (k : ℕ) :
    ‖zeroSideTail p q t k‖ ≤ (‖q - 1‖ / ‖t‖ + ‖q - 1‖ / ‖t‖ ^ 2) * (‖p‖⁻¹) ^ k := by
  have hp0 : (0:ℝ) < ‖p‖ := lt_trans zero_lt_one hp
  have ht0 : (0:ℝ) < ‖t‖ := norm_pos_iff.mpr ht
  have hpk : (0:ℝ) < ‖p‖ ^ k := pow_pos hp0 k
  have hmono : (1:ℝ) ≤ ‖p‖ ^ k := one_le_pow₀ hp.le
  have hnum : ‖(q - 1) * t * p ^ k + (q - 1)‖ ≤ ‖q - 1‖ * ‖t‖ * ‖p‖ ^ k + ‖q - 1‖ := by
    refine (norm_add_le _ _).trans ?_
    rw [norm_mul, norm_mul, norm_pow]
  have hden : ‖t ^ 2 * p ^ (2 * k)‖ = ‖t‖ ^ 2 * (‖p‖ ^ k) ^ 2 := by
    rw [norm_mul, norm_pow, norm_pow, mul_comm 2 k, pow_mul]
  have hstep : ‖zeroSideTail p q t k‖
      ≤ (‖q - 1‖ * ‖t‖ * ‖p‖ ^ k + ‖q - 1‖) / (‖t‖ ^ 2 * (‖p‖ ^ k) ^ 2) := by
    rw [zeroSideTail, norm_div, hden]
    exact div_le_div_of_nonneg_right hnum (by positivity)
  refine hstep.trans ?_
  have hinvp : (‖p‖⁻¹) ^ k = (‖p‖ ^ k)⁻¹ := inv_pow ‖p‖ k
  have hsplit2 : (‖q - 1‖ * ‖t‖ * ‖p‖ ^ k + ‖q - 1‖) / (‖t‖ ^ 2 * (‖p‖ ^ k) ^ 2)
      = ‖q - 1‖ / ‖t‖ * (‖p‖⁻¹) ^ k + ‖q - 1‖ / ‖t‖ ^ 2 * ((‖p‖⁻¹) ^ k) ^ 2 := by
    rw [hinvp]
    field_simp
  rw [hsplit2]
  have hY0 : (0:ℝ) < (‖p‖⁻¹) ^ k := by positivity
  have hY1 : (‖p‖⁻¹) ^ k ≤ 1 := by rw [hinvp]; exact inv_le_one_of_one_le₀ hmono
  have hq : (0:ℝ) ≤ ‖q - 1‖ / ‖t‖ ^ 2 := by positivity
  nlinarith [mul_nonneg hq (mul_nonneg hY0.le (sub_nonneg.mpr hY1))]

lemma norm_zeroSideRatio_le (p q t : ℂ) (ht : t ≠ 0) (hp : p ≠ 0) (k : ℕ)
    (hu : ‖zeroSideTail p q t k‖ ≤ 1 / 2) :
    ‖zeroSideRatio p q t k‖ ≤ 1 + 2 * ‖zeroSideTail p q t k‖ := by
  set u := zeroSideTail p q t k with hudef
  have hge : (1:ℝ) - ‖u‖ ≤ ‖1 + u‖ := by
    have h := norm_sub_norm_le (1 : ℂ) (-u)
    simp only [norm_one, norm_neg, sub_neg_eq_add] at h
    exact h
  have hpos : (0:ℝ) < ‖1 + u‖ := by linarith
  have hmul : 1 ≤ (1 + 2 * ‖u‖) * ‖1 + u‖ := by nlinarith [norm_nonneg u]
  rw [zeroSideRatio_eq p q t ht hp k, norm_inv]
  calc ‖1 + u‖⁻¹ = 1 * ‖1 + u‖⁻¹ := (one_mul _).symm
    _ ≤ ((1 + 2 * ‖u‖) * ‖1 + u‖) * ‖1 + u‖⁻¹ :=
        mul_le_mul_of_nonneg_right hmul (inv_nonneg.mpr hpos.le)
    _ = 1 + 2 * ‖u‖ := by field_simp

/-- **The `0`-side power series converges on the open unit disc.**

The radius of convergence of `∑ gₖ zᵏ` is at least `1`. The ratio
`g_{k+2}/g_k = t²p^{2k}/(t²p^{2k} + (q−1)tp^k + (q−1))` tends to `1` like
`1 + O(‖p‖^{-k})`, so the coefficients are bounded, which is all radius `≥ 1`
needs. -/
theorem summable_zeroSideCoeff (p q t : ℂ) (ht : t ≠ 0) (hp : 1 < ‖p‖)
    {z : ℂ} (hz : ‖z‖ < 1) :
    Summable (fun k => zeroSideCoeff p q t k * z ^ k) := by
  have hp0 : p ≠ 0 := by
    intro h; rw [h] at hp; simp at hp; linarith
  set ρ : ℝ := ‖p‖⁻¹ with hρdef
  have hpn : (0:ℝ) < ‖p‖ := lt_trans zero_lt_one hp
  have hρ0 : 0 ≤ ρ := by positivity
  have hρ1 : ρ < 1 := by rw [hρdef, inv_lt_one_iff₀]; right; exact hp
  set C₀ : ℝ := ‖q - 1‖ / ‖t‖ + ‖q - 1‖ / ‖t‖ ^ 2 with hC₀
  have hC₀0 : 0 ≤ C₀ := by
    have : (0:ℝ) < ‖t‖ := norm_pos_iff.mpr ht
    positivity
  -- a threshold beyond which the tail is at most 1/2
  have htend : Filter.Tendsto (fun k : ℕ => C₀ * ρ ^ k) Filter.atTop (nhds 0) := by
    simpa using (tendsto_pow_atTop_nhds_zero_of_lt_one hρ0 hρ1).const_mul C₀
  have hev : ∀ᶠ k in Filter.atTop, C₀ * ρ ^ k < 1 / 2 :=
    htend.eventually (gt_mem_nhds (by norm_num))
  obtain ⟨K, hK⟩ := Filter.eventually_atTop.mp hev
  -- the ratio hypothesis of the general boundedness lemma
  have hstep : ∀ k, K ≤ k →
      ‖zeroSideCoeff p q t (k + 2)‖ ≤ (1 + (2 * C₀) * ρ ^ k) * ‖zeroSideCoeff p q t k‖ := by
    intro k hk
    have htail2 : ‖zeroSideTail p q t (k + 2)‖ ≤ C₀ * ρ ^ (k + 2) :=
      norm_zeroSideTail_le p q t ht hp (k + 2)
    have hsmall : ‖zeroSideTail p q t (k + 2)‖ ≤ 1 / 2 :=
      htail2.trans (le_of_lt (hK (k + 2) (by omega)))
    have hr := norm_zeroSideRatio_le p q t ht hp0 (k + 2) hsmall
    have hmono : ρ ^ (k + 2) ≤ ρ ^ k := pow_le_pow_of_le_one hρ0 hρ1.le (by omega)
    have hrb : ‖zeroSideRatio p q t (k + 2)‖ ≤ 1 + (2 * C₀) * ρ ^ k := by
      have : 2 * ‖zeroSideTail p q t (k + 2)‖ ≤ 2 * (C₀ * ρ ^ (k + 2)) := by linarith
      nlinarith [hC₀0, pow_nonneg hρ0 (k + 2)]
    have heq : zeroSideCoeff p q t (k + 2)
        = zeroSideRatio p q t (k + 2) * zeroSideCoeff p q t k := rfl
    rw [heq, norm_mul]
    exact mul_le_mul_of_nonneg_right hrb (norm_nonneg _)
  have hbdd := norm_le_of_ratio_le_one_add_geometric (a := zeroSideCoeff p q t)
    (C := 2 * C₀) (ρ := ρ) (K := K) (by linarith) hρ0 hρ1 hstep
  exact summable_of_norm_coeff_le hbdd hz

/-! ### Entire series from a two-step recursion with vanishing coefficients -/

/-- **A two-step recursion whose coefficients vanish geometrically is entire.**

If `‖a (k+2)‖ ≤ Dρᵏ · max ‖a (k+1)‖ ‖a k‖` for `k ≥ K`, with `0 < ρ < 1`, then
`∑ aₖ uᵏ` converges for **every** `u` — the radius of convergence is `∞`.

The majorant is `M · ∏_{j<k} (c σʲ)` with `σ = √ρ`: the two-step lag costs
exactly a square root, and `σ² = ρ` is what makes the induction close with a
constant `c` rather than a `k`-dependent one. -/
theorem summable_of_two_step_geometric {a : ℕ → ℂ} {D ρ : ℝ} {K : ℕ}
    (hD : 0 < D) (hρ0 : 0 < ρ) (hρ1 : ρ < 1)
    (h : ∀ k, K ≤ k → ‖a (k + 2)‖ ≤ D * ρ ^ k * max ‖a (k + 1)‖ ‖a k‖) (u : ℂ) :
    Summable (fun k => a k * u ^ k) := by
  set σ : ℝ := Real.sqrt ρ with hσdef
  have hσ0 : 0 < σ := Real.sqrt_pos.mpr hρ0
  have hσσ : σ * σ = ρ := Real.mul_self_sqrt hρ0.le
  have hσ1 : σ < 1 := by nlinarith
  set c : ℝ := max 1 (D / σ) with hcdef
  have hc1 : (1:ℝ) ≤ c := le_max_left _ _
  have hc0 : 0 < c := lt_of_lt_of_le zero_lt_one hc1
  have hcσ : D ≤ c * σ := by
    have : D / σ ≤ c := le_max_right _ _
    calc D = (D / σ) * σ := by field_simp
      _ ≤ c * σ := mul_le_mul_of_nonneg_right this hσ0.le
  set P : ℕ → ℝ := fun k => ∏ j ∈ Finset.range k, (c * σ ^ j) with hPdef
  have hP0 : ∀ k, 0 < P k := by
    intro k; rw [hPdef]; exact Finset.prod_pos fun j _ => mul_pos hc0 (pow_pos hσ0 j)
  have hPsucc : ∀ k, P (k + 1) = P k * (c * σ ^ k) := by
    intro k; rw [hPdef]; exact Finset.prod_range_succ _ _
  -- the majorant constant absorbs the terms below the threshold
  set M : ℝ := ∑ j ∈ Finset.range (K + 2), ‖a j‖ / P j with hMdef
  have hM0 : 0 ≤ M :=
    Finset.sum_nonneg fun j _ => div_nonneg (norm_nonneg _) (hP0 j).le
  have hbase : ∀ k, k < K + 2 → ‖a k‖ ≤ M * P k := by
    intro k hk
    have hle : ‖a k‖ / P k ≤ M :=
      Finset.single_le_sum (f := fun j => ‖a j‖ / P j)
        (fun j _ => div_nonneg (norm_nonneg _) (hP0 j).le) (Finset.mem_range.mpr hk)
    rw [div_le_iff₀ (hP0 k)] at hle
    exact hle
  clear_value M P c σ
  clear hMdef hPdef hcdef hσdef
  have key : ∀ k, ‖a k‖ ≤ M * P k := by
    intro k
    induction k using Nat.strong_induction_on with
    | _ k ih =>
      by_cases hk : k < K + 2
      · exact hbase k hk
      · push_neg at hk
        obtain ⟨n, rfl⟩ : ∃ n, k = n + 2 := ⟨k - 2, by omega⟩
        have hnK : K ≤ n := by omega
        have h1 := ih (n + 1) (by omega)
        have h2 := ih n (by omega)
        have hmax : max ‖a (n + 1)‖ ‖a n‖ ≤ M * (P n * max (c * σ ^ n) 1) := by
          rw [max_le_iff]
          refine ⟨?_, ?_⟩
          · calc ‖a (n + 1)‖ ≤ M * P (n + 1) := h1
              _ = M * (P n * (c * σ ^ n)) := by rw [hPsucc]
              _ ≤ M * (P n * max (c * σ ^ n) 1) :=
                  mul_le_mul_of_nonneg_left
                    (mul_le_mul_of_nonneg_left (le_max_left _ _) (hP0 n).le) hM0
          · calc ‖a n‖ ≤ M * P n := h2
              _ = M * (P n * 1) := by ring
              _ ≤ M * (P n * max (c * σ ^ n) 1) :=
                  mul_le_mul_of_nonneg_left
                    (mul_le_mul_of_nonneg_left (le_max_right _ _) (hP0 n).le) hM0
        -- the arithmetic core: D ρⁿ · max(cσⁿ, 1) ≤ (cσⁿ)(cσⁿ⁺¹)
        have hcore : D * ρ ^ n * max (c * σ ^ n) 1 ≤ (c * σ ^ n) * (c * σ ^ (n + 1)) := by
          have hρn : ρ ^ n = (σ ^ n) * (σ ^ n) := by rw [← mul_pow, hσσ]
          have hσn0 : 0 < σ ^ n := pow_pos hσ0 n
          have hσn1 : σ ^ n ≤ 1 := pow_le_one₀ hσ0.le hσ1.le
          rcases le_total (c * σ ^ n) 1 with hcase | hcase
          · rw [max_eq_right hcase, mul_one, hρn, pow_succ]
            have hDc2 : D ≤ c * (c * σ) := by
              nlinarith [mul_le_mul_of_nonneg_left hcσ hc0.le, hc1, hD]
            calc D * (σ ^ n * σ ^ n) ≤ (c * (c * σ)) * (σ ^ n * σ ^ n) :=
                  mul_le_mul_of_nonneg_right hDc2 (by positivity)
              _ = c * σ ^ n * (c * (σ ^ n * σ)) := by ring
          · rw [max_eq_left hcase, hρn, pow_succ]
            have hstep : D * σ ^ n ≤ c * σ := by nlinarith [hD, hσn1, hσn0, hcσ]
            calc D * (σ ^ n * σ ^ n) * (c * σ ^ n)
                = (D * σ ^ n) * (σ ^ n * (c * σ ^ n)) := by ring
              _ ≤ (c * σ) * (σ ^ n * (c * σ ^ n)) :=
                  mul_le_mul_of_nonneg_right hstep (by positivity)
              _ = c * σ ^ n * (c * (σ ^ n * σ)) := by ring
        calc ‖a (n + 2)‖
            ≤ D * ρ ^ n * max ‖a (n + 1)‖ ‖a n‖ := h n hnK
          _ ≤ D * ρ ^ n * (M * (P n * max (c * σ ^ n) 1)) := by
              have : (0:ℝ) ≤ D * ρ ^ n := by positivity
              exact mul_le_mul_of_nonneg_left hmax this
          _ = (M * P n) * (D * ρ ^ n * max (c * σ ^ n) 1) := by ring
          _ ≤ (M * P n) * ((c * σ ^ n) * (c * σ ^ (n + 1))) := by
              exact mul_le_mul_of_nonneg_left hcore (mul_nonneg hM0 (hP0 n).le)
          _ = M * P (n + 2) := by rw [hPsucc, hPsucc]; ring
  -- the majorant is summable, by the ratio test
  have hmaj : Summable (fun k => M * P k * ‖u‖ ^ k) := by
    have htend : Filter.Tendsto (fun k : ℕ => c * σ ^ k * ‖u‖) Filter.atTop (nhds 0) := by
      have := (tendsto_pow_atTop_nhds_zero_of_lt_one hσ0.le hσ1).const_mul c
      simpa using this.mul_const ‖u‖
    have hev : ∀ᶠ k in Filter.atTop, c * σ ^ k * ‖u‖ < 1 / 2 :=
      htend.eventually (gt_mem_nhds (by norm_num))
    refine summable_of_ratio_norm_eventually_le (r := 1 / 2) (by norm_num) ?_
    filter_upwards [hev] with k hk
    have hnn : (0:ℝ) ≤ M * P k * ‖u‖ ^ k :=
      mul_nonneg (mul_nonneg hM0 (hP0 k).le) (pow_nonneg (norm_nonneg u) k)
    have hnn2 : (0:ℝ) ≤ M * P (k + 1) * ‖u‖ ^ (k + 1) :=
      mul_nonneg (mul_nonneg hM0 (hP0 (k + 1)).le) (pow_nonneg (norm_nonneg u) (k + 1))
    rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg hnn, abs_of_nonneg hnn2]
    have hrw : M * P (k + 1) * ‖u‖ ^ (k + 1)
        = (c * σ ^ k * ‖u‖) * (M * P k * ‖u‖ ^ k) := by
      rw [hPsucc, pow_succ]; ring
    rw [hrw]
    exact mul_le_mul_of_nonneg_right hk.le hnn
  refine Summable.of_norm_bounded (g := fun k => M * P k * ‖u‖ ^ k) hmaj ?_
  intro k
  rw [norm_mul, norm_pow]
  exact mul_le_mul_of_nonneg_right (key k) (pow_nonneg (norm_nonneg u) k)

/-! ### The C1 `∞`-side series -/

/-- Denominator of the `∞`-side recursion, `T²p³(1/p)^{2k} + (1−p²)`. -/
noncomputable def infSideDen (p T : ℂ) (k : ℕ) : ℂ :=
  T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * k) + (1 - p ^ 2)

/-- `∞`-side coefficients: `h₀ = 1` and the two-term recursion of
`computations/qbeta/c3_w2_c1_pole_divisor.py`. -/
noncomputable def infSideCoeff (p T : ℂ) : ℕ → ℂ
  | 0 => 1
  | 1 => (-T * (1 - p ^ 2)) / infSideDen p T 1
  | (k + 2) => (-T * (1 - p ^ 2) * (p⁻¹) ^ (k + 1) * infSideCoeff p T (k + 1)
                + T ^ 2 / p * (p⁻¹) ^ (2 * k) * infSideCoeff p T k) / infSideDen p T (k + 2)

private lemma norm_inv_pow (p : ℂ) (m : ℕ) : ‖(p⁻¹) ^ m‖ = (‖p‖⁻¹) ^ m := by
  rw [norm_pow, norm_inv]

/-- **The `∞`-side series is entire.**

The recursion's two coefficients decay like `‖p‖^{-k}` and `‖p‖^{-2k}` while
the denominator tends to the nonzero constant `1 − p²`, so
`summable_of_two_step_geometric` applies: the radius of convergence in `1/z`
is infinite. -/
theorem summable_infSideCoeff (p T : ℂ) (hp : 1 < ‖p‖) (hp2 : p ^ 2 ≠ 1) (u : ℂ) :
    Summable (fun k => infSideCoeff p T k * u ^ k) := by
  have hpn : (0:ℝ) < ‖p‖ := lt_trans zero_lt_one hp
  have hp0 : p ≠ 0 := by intro h; rw [h] at hpn; simp at hpn
  set ρ : ℝ := ‖p‖⁻¹ with hρdef
  have hρ0 : 0 < ρ := by rw [hρdef]; positivity
  have hρ1 : ρ < 1 := by rw [hρdef, inv_lt_one_iff₀]; right; exact hp
  set E : ℝ := ‖1 - p ^ 2‖ with hEdef
  have hE0 : 0 < E := by
    rw [hEdef, norm_pos_iff]
    intro h; exact hp2 (by linear_combination -h)
  -- beyond `K` the denominator is at least `E/2`
  have htend : Filter.Tendsto
      (fun k : ℕ => ‖T‖ ^ 2 * ‖p‖ ^ 3 * ρ ^ (2 * (k + 2))) Filter.atTop (nhds 0) := by
    have h1 : Filter.Tendsto (fun k : ℕ => ρ ^ (2 * (k + 2))) Filter.atTop (nhds 0) := by
      have hr : (0:ℝ) ≤ ρ ^ 2 := by positivity
      have hr1 : ρ ^ 2 < 1 := by nlinarith
      have hbase := tendsto_pow_atTop_nhds_zero_of_lt_one hr hr1
      have heq : ∀ k : ℕ, ρ ^ (2 * (k + 2)) = (ρ ^ 2) ^ k * (ρ ^ 2) ^ 2 := by
        intro k
        rw [← pow_mul, ← pow_mul, ← pow_add]
        congr 1
      simp only [heq]
      simpa using hbase.mul_const ((ρ ^ 2) ^ 2)
    simpa using h1.const_mul (‖T‖ ^ 2 * ‖p‖ ^ 3)
  obtain ⟨K, hK⟩ := Filter.eventually_atTop.mp
    (htend.eventually (gt_mem_nhds (by linarith : (0:ℝ) < E / 2)))
  have hden : ∀ k, K ≤ k → E / 2 ≤ ‖infSideDen p T (k + 2)‖ := by
    intro k hk
    have hsmall : ‖T‖ ^ 2 * ‖p‖ ^ 3 * ρ ^ (2 * (k + 2)) < E / 2 := hK k hk
    have hx : ‖T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * (k + 2))‖
        = ‖T‖ ^ 2 * ‖p‖ ^ 3 * ρ ^ (2 * (k + 2)) := by
      rw [norm_mul, norm_mul, norm_pow, norm_pow, norm_inv_pow]
    have hge := norm_sub_norm_le (1 - p ^ 2) (-(T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * (k + 2))))
    rw [norm_neg, sub_neg_eq_add, hx] at hge
    rw [infSideDen]
    calc E / 2 ≤ E - ‖T‖ ^ 2 * ‖p‖ ^ 3 * ρ ^ (2 * (k + 2)) := by linarith
      _ ≤ ‖1 - p ^ 2 + T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * (k + 2))‖ := hge
      _ = ‖T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * (k + 2)) + (1 - p ^ 2)‖ := by rw [add_comm]
  set D₀ : ℝ := ‖T‖ * E + ‖T‖ ^ 2 / ‖p‖ with hD₀
  have hD₀0 : 0 ≤ D₀ := by rw [hD₀]; positivity
  set D : ℝ := max 1 (2 * D₀ / E) with hDdef
  have hD1 : (1:ℝ) ≤ D := le_max_left _ _
  have hDE : D₀ ≤ D * (E / 2) := by
    have h2 : 2 * D₀ / E ≤ D := le_max_right _ _
    have : (2 * D₀ / E) * (E / 2) = D₀ := by field_simp
    calc D₀ = (2 * D₀ / E) * (E / 2) := this.symm
      _ ≤ D * (E / 2) := mul_le_mul_of_nonneg_right h2 (by linarith)
  refine summable_of_two_step_geometric (D := D) (ρ := ρ) (K := K)
    (by linarith) hρ0 hρ1 ?_ u
  intro k hk
  set mx : ℝ := max ‖infSideCoeff p T (k + 1)‖ ‖infSideCoeff p T k‖ with hmx
  have hmx0 : 0 ≤ mx := le_trans (norm_nonneg _) (le_max_right _ _)
  have hdk : E / 2 ≤ ‖infSideDen p T (k + 2)‖ := hden k hk
  have hdpos : (0:ℝ) < ‖infSideDen p T (k + 2)‖ := by linarith
  have hρk : (0:ℝ) < ρ ^ k := pow_pos hρ0 k
  -- numerator estimate
  have hnum : ‖-T * (1 - p ^ 2) * (p⁻¹) ^ (k + 1) * infSideCoeff p T (k + 1)
      + T ^ 2 / p * (p⁻¹) ^ (2 * k) * infSideCoeff p T k‖ ≤ D₀ * ρ ^ k * mx := by
    refine (norm_add_le _ _).trans ?_
    have h1 : ‖-T * (1 - p ^ 2) * (p⁻¹) ^ (k + 1) * infSideCoeff p T (k + 1)‖
        = ‖T‖ * E * ρ ^ (k + 1) * ‖infSideCoeff p T (k + 1)‖ := by
      rw [norm_mul, norm_mul, norm_mul, norm_neg, norm_inv_pow, hEdef]
    have h2 : ‖T ^ 2 / p * (p⁻¹) ^ (2 * k) * infSideCoeff p T k‖
        = ‖T‖ ^ 2 / ‖p‖ * ρ ^ (2 * k) * ‖infSideCoeff p T k‖ := by
      rw [norm_mul, norm_mul, norm_div, norm_pow, norm_inv_pow]
    rw [h1, h2]
    have e1 : ρ ^ (k + 1) ≤ ρ ^ k := pow_le_pow_of_le_one hρ0.le hρ1.le (by omega)
    have e2 : ρ ^ (2 * k) ≤ ρ ^ k := pow_le_pow_of_le_one hρ0.le hρ1.le (by omega)
    have c1 : ‖infSideCoeff p T (k + 1)‖ ≤ mx := le_max_left _ _
    have c2 : ‖infSideCoeff p T k‖ ≤ mx := le_max_right _ _
    have b1 : ‖T‖ * E * ρ ^ (k + 1) * ‖infSideCoeff p T (k + 1)‖ ≤ (‖T‖ * E) * ρ ^ k * mx := by
      have hc : (0:ℝ) ≤ ‖T‖ * E := by positivity
      have := mul_le_mul e1 c1 (norm_nonneg _) (pow_nonneg hρ0.le k)
      nlinarith [hc, this]
    have b2 : ‖T‖ ^ 2 / ‖p‖ * ρ ^ (2 * k) * ‖infSideCoeff p T k‖
        ≤ (‖T‖ ^ 2 / ‖p‖) * ρ ^ k * mx := by
      have hc : (0:ℝ) ≤ ‖T‖ ^ 2 / ‖p‖ := by positivity
      have := mul_le_mul e2 c2 (norm_nonneg _) (pow_nonneg hρ0.le k)
      nlinarith [hc, this]
    rw [hD₀]
    nlinarith [b1, b2]
  have heq : infSideCoeff p T (k + 2)
      = (-T * (1 - p ^ 2) * (p⁻¹) ^ (k + 1) * infSideCoeff p T (k + 1)
         + T ^ 2 / p * (p⁻¹) ^ (2 * k) * infSideCoeff p T k) / infSideDen p T (k + 2) := rfl
  rw [heq, norm_div, div_le_iff₀ hdpos]
  calc ‖-T * (1 - p ^ 2) * (p⁻¹) ^ (k + 1) * infSideCoeff p T (k + 1)
        + T ^ 2 / p * (p⁻¹) ^ (2 * k) * infSideCoeff p T k‖
      ≤ D₀ * ρ ^ k * mx := hnum
    _ ≤ (D * (E / 2)) * ρ ^ k * mx :=
        mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right hDE hρk.le) hmx0
    _ = (D * ρ ^ k * mx) * (E / 2) := by ring
    _ ≤ (D * ρ ^ k * mx) * ‖infSideDen p T (k + 2)‖ := by
        have : (0:ℝ) ≤ D * ρ ^ k * mx := by
          have : (0:ℝ) ≤ D := by linarith
          positivity
        exact mul_le_mul_of_nonneg_left hdk this


/-! ### The two recursions, derived from the operator

Added 2026-08-08 (bean `qou-slvl` item 2). Above, `zeroSideCoeff` and
`infSideCoeff` were *defined* to match `c3_w2_c1_pole_divisor.py`, so the
summability theorems certified convergence of stated sequences rather than of
solutions. Both recursions are now consequences of

    L = (p⁴z² − 1)τ² − (p²−1)τ − (p²−1),   τF(z) = F(pz),  q = p².

Neither side is a bare power series, and the theta prefactors are what make the
brackets polynomial — via the functional equation `θ_p(pw) = w·θ_p(w)`:

* **0-side** `y₀ = e_t(z)·G(z)`, `e_t = θ_p(z)/θ_p(z/t)`, `G = ∑ g_k z^k`. Then
  `τe_t = t·e_t`, so `L y₀ / e_t = (p⁴z²−1)t²τ²G − (p²−1)t·τG − (p²−1)G`, whose
  `z^{k+2}` coefficient is `zeroCoeffAt`.
* **∞-side** `y_∞ = H(z)/θ_p(z/T)`, `H = ∑ h_k z^{-k}`. Then
  `τ[1/θ_p(z/T)] = (T/z)/θ_p(z/T)` and `τ²[…] = T²/(pz²)·/θ_p(z/T)`, and in
  `u = 1/z` the bracket's `u^{k+2}` coefficient is `infCoeffAt`.

That these collections really *are* those coefficients, and that solving them
returns `gc()` and `hc()` verbatim, is machine-checked symbolically in
`computations/qbeta/c3_w2_c1_side_recursions_derived.py` (4/4). The two theorems
below prove, in general, that each collection vanishes iff its recursion holds.

**Still not established**: that these series, times their theta prefactors, are
the *canonical* solutions at `0` and `∞` — that is `qou-c1ln` row 4. What is
established is that the recursions are forced by the operator. -/

section Derived

variable {K : Type*} [Field K]

noncomputable def infCoeffAt (p T : K) (h : ℕ → K) (k : ℕ) : K :=
  T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * (k + 2)) * h (k + 2)
    - T ^ 2 / p * (p⁻¹) ^ (2 * k) * h k
    - (p ^ 2 - 1) * T * (p⁻¹) ^ (k + 1) * h (k + 1)
    - (p ^ 2 - 1) * h (k + 2)

theorem infCoeffAt_eq_zero_iff (p T : K) (h : ℕ → K) (k : ℕ) :
    infCoeffAt p T h k = 0
      ↔ (T ^ 2 * p ^ 3 * (p⁻¹) ^ (2 * (k + 2)) - (p ^ 2 - 1)) * h (k + 2)
          = (p ^ 2 - 1) * T * (p⁻¹) ^ (k + 1) * h (k + 1)
            + T ^ 2 / p * (p⁻¹) ^ (2 * k) * h k := by
  rw [infCoeffAt, ← sub_eq_zero]
  constructor <;> intro h1 <;> linear_combination h1

noncomputable def zeroCoeffAt (p t : K) (g : ℕ → K) (k : ℕ) : K :=
  t ^ 2 * p ^ (2 * (k + 2)) * g k
    - t ^ 2 * p ^ (2 * (k + 2)) * g (k + 2)
    - (p ^ 2 - 1) * t * p ^ (k + 2) * g (k + 2)
    - (p ^ 2 - 1) * g (k + 2)

theorem zeroCoeffAt_eq_zero_iff (p t : K) (g : ℕ → K) (k : ℕ) :
    zeroCoeffAt p t g k = 0
      ↔ (t ^ 2 * p ^ (2 * (k + 2)) + (p ^ 2 - 1) * t * p ^ (k + 2) + (p ^ 2 - 1))
            * g (k + 2)
          = t ^ 2 * p ^ (2 * (k + 2)) * g k := by
  rw [zeroCoeffAt, ← sub_eq_zero]
  constructor <;> intro h1 <;> linear_combination -h1

end Derived

end QOU.QBeta.C1Series
