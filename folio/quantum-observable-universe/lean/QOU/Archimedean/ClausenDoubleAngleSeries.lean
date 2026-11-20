import Mathlib.Analysis.PSeries
import QOU.Archimedean.ClausenFunctionMathlibFiller

/-!
# QOU.Archimedean.ClausenDoubleAngleSeries — `Cl₂` duplication for every real `θ`

The Clausen duplication identity

  `Cl₂(2θ) = 2·Cl₂(θ) − 2·Cl₂(π − θ)`

is already proved in the corpus on the open interval `(0, π)`
(`QOU.Knot.Cl_2_duplication`, via the integral representation and the
series↔integral bridge). The class `Cl_2_DoubleAngle` in
`predicted-spectra/upstream-mathlib-additions.lean` asks for it at **every**
`θ : ℝ`, which the interval result does not supply.

This file proves the all-`θ` statement directly from the series definition
`Cl₂(θ) = Σ_{k≥0} sin((k+1)θ)/(k+1)²`. No integral and no Fourier theory are used:

* `sin((k+1)(π − θ)) = (−1)^k · sin((k+1)θ)`, so `Cl₂(θ) − Cl₂(π − θ)` keeps only
  the terms with `k` odd, each doubled;
* the odd terms `k = 2m+1` are `sin((m+1)·2θ) / (4(m+1)²)`, which sum to `Cl₂(2θ)/4`.

Every series involved is absolutely summable (`|term| ≤ 1/(k+1)²`).

-- Ref: [zagier1986] D. Zagier, *Hyperbolic manifolds and special values of Dedekind
--   zeta-functions*, Invent. Math. 83 (1986) — Clausen duplication.
-- Ref: [lewin1981] L. Lewin, *Polylogarithms and associated functions*, §4.2.
-/

namespace QOU.Archimedean.ClausenDoubleAngleSeries

open QOU.Archimedean

/-- Every sequence `a k / (k+1)²` with `|a k| ≤ 1` is summable. -/
theorem summable_bounded_div_sq (a : ℕ → ℝ) (ha : ∀ k, |a k| ≤ 1) :
    Summable (fun k : ℕ => a k / ((k : ℝ) + 1) ^ 2) := by
  have hsum : Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
    have h : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      Real.summable_one_div_nat_pow.mpr (by norm_num)
    exact ((summable_nat_add_iff 1).2 h).congr (fun n => by push_cast; ring)
  refine Summable.of_norm_bounded hsum (fun k => ?_)
  rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0 : ℝ) < ((k : ℝ) + 1) ^ 2)]
  gcongr
  exact ha k

theorem summable_sin_term (θ : ℝ) :
    Summable (fun k : ℕ => Real.sin (((k : ℝ) + 1) * θ) / ((k : ℝ) + 1) ^ 2) :=
  summable_bounded_div_sq _ (fun _ => abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩)

/-- `cos(nπ) = (−1)^n`. -/
theorem cos_nat_mul_pi' (n : ℕ) : Real.cos (n * Real.pi) = (-1) ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Nat.cast_succ, add_mul, one_mul, Real.cos_add_pi, ih, pow_succ]
    ring

/-- `sin((k+1)(π − θ)) = (−1)^k · sin((k+1)θ)`. -/
theorem sin_succ_mul_pi_sub (k : ℕ) (θ : ℝ) :
    Real.sin (((k : ℝ) + 1) * (Real.pi - θ)) = (-1) ^ k * Real.sin (((k : ℝ) + 1) * θ) := by
  have hc : ((k : ℝ) + 1) * (Real.pi - θ)
      = ((k + 1 : ℕ) : ℝ) * Real.pi - ((k : ℝ) + 1) * θ := by push_cast; ring
  rw [hc, Real.sin_sub, Real.sin_nat_mul_pi, cos_nat_mul_pi', pow_succ]
  ring

/-- **Clausen duplication, for every real `θ`** (sorry-free, series proof):
    `Cl₂(2θ) = 2·Cl₂(θ) − 2·Cl₂(π − θ)`. -/
theorem Cl_2_double_angle (θ : ℝ) :
    Cl_2 (2 * θ) = 2 * Cl_2 θ - 2 * Cl_2 (Real.pi - θ) := by
  -- `g k` = the `k`-th term of `Cl₂(θ) − Cl₂(π − θ)`
  set f : ℕ → ℝ := fun k => Real.sin (((k : ℝ) + 1) * θ) / ((k : ℝ) + 1) ^ 2 with hf
  set g : ℕ → ℝ := fun k => (1 - (-1) ^ k) * f k with hg
  have hfs : Summable f := summable_sin_term θ
  have hgs : Summable g := by
    refine summable_bounded_div_sq (fun k => (1 - (-1) ^ k) / 2 * Real.sin (((k : ℝ) + 1) * θ))
      (fun k => ?_) |>.mul_left 2 |>.congr (fun k => ?_)
    · dsimp only
      have hs := abs_le.mpr ⟨Real.neg_one_le_sin (((k : ℝ) + 1) * θ), Real.sin_le_one (((k : ℝ) + 1) * θ)⟩
      rcases neg_one_pow_eq_or ℝ k with h | h <;> rw [h]
      · norm_num
      · norm_num; exact hs
    · simp only [hg, hf]; ring
  -- step 1: `Cl₂(θ) − Cl₂(π − θ) = Σ g`
  have h1 : Cl_2 θ - Cl_2 (Real.pi - θ) = ∑' k, g k := by
    have hpi : Cl_2 (Real.pi - θ) = ∑' k, (-1 : ℝ) ^ k * f k := by
      unfold Cl_2
      refine tsum_congr (fun k => ?_)
      rw [sin_succ_mul_pi_sub]; simp only [hf]; ring
    have hps : Summable (fun k => (-1 : ℝ) ^ k * f k) :=
      summable_bounded_div_sq (fun k => (-1) ^ k * Real.sin (((k : ℝ) + 1) * θ))
        (fun k => by rw [abs_mul, abs_pow, abs_neg, abs_one, one_pow, one_mul]
                     exact abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩)
        |>.congr (fun k => by simp only [hf]; ring)
    rw [hpi, show Cl_2 θ = ∑' k, f k from rfl, ← hfs.tsum_sub hps]
    exact tsum_congr (fun k => by simp only [hg]; ring)
  -- step 2: split `Σ g` into even and odd indices; the even part vanishes
  have h2 : ∑' k, g k = ∑' m, g (2 * m + 1) := by
    rw [← tsum_even_add_odd (hgs.comp_injective (fun a b h => by omega))
      (hgs.comp_injective (fun a b h => by omega))]
    have he : ∀ m : ℕ, g (2 * m) = 0 := fun m => by
      simp only [hg, pow_mul, neg_one_sq, one_pow, sub_self, zero_mul]
    simp only [he, tsum_zero, zero_add]
  -- step 3: the odd part is `Cl₂(2θ)/2`
  have h3 : ∑' m, g (2 * m + 1) = Cl_2 (2 * θ) / 2 := by
    have hterm : ∀ m : ℕ, g (2 * m + 1)
        = (1 / 2) * (Real.sin (((m : ℝ) + 1) * (2 * θ)) / ((m : ℝ) + 1) ^ 2) := by
      intro m
      simp only [hg, hf, pow_succ, pow_mul]
      have hm : ((2 * m + 1 : ℕ) : ℝ) + 1 = 2 * ((m : ℝ) + 1) := by push_cast; ring
      rw [hm, show 2 * ((m : ℝ) + 1) * θ = ((m : ℝ) + 1) * (2 * θ) by ring]
      field_simp
      ring
    rw [tsum_congr hterm, tsum_mul_left]
    unfold Cl_2
    ring
  have key := h1.trans (h2.trans h3)
  linarith

end QOU.Archimedean.ClausenDoubleAngleSeries
