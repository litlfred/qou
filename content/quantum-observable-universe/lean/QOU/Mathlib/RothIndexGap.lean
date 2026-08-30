/-
# Producing `S`: the index gap, converted by `r_h · log q_h ≥ K`

`abs_coeff_translate_add_le_index` (`RothTaylorBound`) reduced step 2's analytic half to a single
unknown: a uniform bound `S` on `∏_h G_h^{n_h − i_h}` over the multi-indices the index hypothesis
lets survive.  This file produces it, and then closes step 2 against `le_index_of_abs_lt`.

## The one conversion the whole step turns on

Two different weightings meet here and neither dominates the other on its own.  The index gap is
**weighted by `1/r_h`** — `idxWeight r n ≥ μ` and `idxWeight r i ≤ ν` give
`∑_h (n_h − i_h)/r_h ≥ μ − ν`, and nothing about `∑_h (n_h − i_h)` itself.  The sizes are
**weighted by `log q_h`** — `∏_h G_h^{n_h−i_h} = exp(−∑_h (n_h−i_h)·T_h)` with `T_h = −log G_h`.

`r_h · T_h ≥ K` is exactly the hypothesis that converts one into the other:

    ∑_h (n_h − i_h)·T_h  =  ∑_h [(n_h − i_h)/r_h] · (r_h·T_h)  ≥  K · ∑_h (n_h − i_h)/r_h
                                                                ≥  K·(μ − ν).

That is Roth's normalisation `r_h·log q_h ≈ L` in the only form the estimate needs, and it is why
the degrees must be chosen from the heights rather than freely — the same fact `RothGammaProducer`
discharges for `Γ_m`'s growth clause.  `S = exp(−K(μ−ν))`.

## Truncated subtraction is free here

`translateMatrix`'s exponents are `n_h ∸ i_h`, not `n_h − i_h`, and truncation only ever raises
them (`sub_le_cast_sub`).  Since `G_h ≤ 1` a larger exponent is a smaller product, so the bound
survives truncation without a case split.  Worth stating because the opposite is easy to assume:
if the estimate had needed an *upper* bound on the exponents, truncation would have been a real
obstruction rather than a convenience.

## What step 2 now rests on

`le_index_rational_of_taylor` is step 2 with one hypothesis left, and that hypothesis is a single
numeric inequality between explicit quantities — no polynomial, no index, no Taylor expansion in
it.  Discharging it is the parameter bookkeeping of step 4: the left side is
`(box)²·H·(2B)^{Σr}·2^{Σr}·exp(−K(μ−ν))` and the right is `∏_h q_h^{−r_h} = exp(−Σ_h r_h log q_h)`,
so with `r_h log q_h ≈ L` it reads `log(box² H (2B)^{Σr} 2^{Σr}) + mL < (2+δ)L(μ−ν)`, which at
`μ ≈ m(½ − ε)` and small `ν` is Roth's inequality and holds for `δ > 0` once `m` is large.  It is
left as a hypothesis rather than discharged here because it belongs with the parameter record, not
with the estimate.
-/
import QOU.Mathlib.RothTaylorBound
import Mathlib.Analysis.SpecialFunctions.Exp

namespace MvPolynomial

open Finset

section Gap

variable {m : ℕ}

/-- Truncated subtraction dominates real subtraction. -/
theorem sub_le_cast_sub (a b : ℕ) : (a : ℝ) - (b : ℝ) ≤ ((a - b : ℕ) : ℝ) := by
  rcases le_or_gt b a with h | h
  · rw [Nat.cast_sub h]
  · have h0 : a - b = 0 := by omega
    have hab : (a : ℝ) ≤ (b : ℝ) := by exact_mod_cast h.le
    rw [h0, Nat.cast_zero]
    linarith

/-- `idxWeight`, cast to `ℝ` and summed over all coordinates. -/
theorem idxWeight_cast (r : Fin m → ℕ) (x : Fin m →₀ ℕ) :
    ((idxWeight r x : ℚ) : ℝ) = ∑ h, ((x h : ℝ) / (r h : ℝ)) := by
  rw [idxWeight_eq_sum_univ]
  push_cast
  rfl

/-- **The index gap is a lower bound on the weighted degree excess.**  `idxWeight r n ≥ μ` and
`idxWeight r i ≤ ν` give `∑_h (n_h ∸ i_h)/r_h ≥ μ − ν` — truncated subtraction included, because
truncation only raises the exponents. -/
theorem index_gap_le_sum_div (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0) (n i : Fin m →₀ ℕ)
    {μ ν : ℚ} (hμ : μ ≤ idxWeight r n) (hν : idxWeight r i ≤ ν) :
    ((μ : ℝ) - (ν : ℝ)) ≤ ∑ h, (((n h - i h : ℕ) : ℝ) / (r h : ℝ)) := by
  have hμR : ((μ : ℚ) : ℝ) ≤ ∑ h, ((n h : ℝ) / (r h : ℝ)) := by
    rw [← idxWeight_cast]
    exact_mod_cast hμ
  have hνR : (∑ h, ((i h : ℝ) / (r h : ℝ))) ≤ ((ν : ℚ) : ℝ) := by
    rw [← idxWeight_cast]
    exact_mod_cast hν
  have h1 : ((μ : ℝ) - (ν : ℝ))
      ≤ ∑ h, (((n h : ℝ) / (r h : ℝ)) - ((i h : ℝ) / (r h : ℝ))) := by
    rw [Finset.sum_sub_distrib]
    linarith
  refine le_trans h1 (Finset.sum_le_sum (fun h _ => ?_))
  have hrpos : (0 : ℝ) < (r h : ℝ) := by
    exact_mod_cast Nat.pos_of_ne_zero (hr h)
  have hinv : (0 : ℝ) ≤ ((r h : ℝ))⁻¹ := by positivity
  rw [div_sub_div_same, div_eq_mul_inv, div_eq_mul_inv]
  exact mul_le_mul_of_nonneg_right (sub_le_cast_sub _ _) hinv

/-- **`S = exp(−K(μ−ν))`.**  The conversion the whole step turns on: `r_h·T_h ≥ K` takes the
`1/r_h`-weighted index gap to the `T_h`-weighted size gap.  `T_h` is `−log G_h`, so in the
application `T_h = (2+δ)·log q_h` and `K = (2+δ)·L`. -/
theorem prod_pow_le_exp (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    {G T : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h) (hGT : ∀ h, G h ≤ Real.exp (-(T h)))
    {K : ℝ} (hK0 : 0 ≤ K) (hT : ∀ h, K ≤ T h * (r h : ℝ))
    (n i : Fin m →₀ ℕ) {μ ν : ℚ} (hμ : μ ≤ idxWeight r n) (hν : idxWeight r i ≤ ν) :
    (∏ h, (G h) ^ (n h - i h)) ≤ Real.exp (-(K * ((μ : ℝ) - (ν : ℝ)))) := by
  classical
  have step1 : (∏ h, (G h) ^ (n h - i h))
      ≤ ∏ h, (Real.exp (-(T h))) ^ (n h - i h) :=
    Finset.prod_le_prod (fun h _ => pow_nonneg (hG0 h) _)
      (fun h _ => pow_le_pow_left₀ (hG0 h) (hGT h) _)
  have step2 : (∏ h, (Real.exp (-(T h))) ^ (n h - i h))
      = Real.exp (∑ h, ((n h - i h : ℕ) : ℝ) * (-(T h))) := by
    rw [Real.exp_sum]
    exact Finset.prod_congr rfl (fun h _ => (Real.exp_nat_mul _ _).symm)
  have hkey : K * ((μ : ℝ) - (ν : ℝ)) ≤ ∑ h, ((n h - i h : ℕ) : ℝ) * T h := by
    calc K * ((μ : ℝ) - (ν : ℝ))
        ≤ K * ∑ h, (((n h - i h : ℕ) : ℝ) / (r h : ℝ)) :=
          mul_le_mul_of_nonneg_left (index_gap_le_sum_div r hr n i hμ hν) hK0
      _ = ∑ h, K * (((n h - i h : ℕ) : ℝ) / (r h : ℝ)) := Finset.mul_sum _ _ _
      _ ≤ ∑ h, ((n h - i h : ℕ) : ℝ) * T h := by
          refine Finset.sum_le_sum (fun h _ => ?_)
          have hrpos : (0 : ℝ) < (r h : ℝ) := by
            exact_mod_cast Nat.pos_of_ne_zero (hr h)
          have hq : (0 : ℝ) ≤ ((n h - i h : ℕ) : ℝ) / (r h : ℝ) := by positivity
          have h1 : K * (((n h - i h : ℕ) : ℝ) / (r h : ℝ))
              ≤ (T h * (r h : ℝ)) * (((n h - i h : ℕ) : ℝ) / (r h : ℝ)) :=
            mul_le_mul_of_nonneg_right (hT h) hq
          have h2 : (T h * (r h : ℝ)) * (((n h - i h : ℕ) : ℝ) / (r h : ℝ))
              = ((n h - i h : ℕ) : ℝ) * T h := by
            field_simp
          linarith
  have step3 : (∑ h, ((n h - i h : ℕ) : ℝ) * (-(T h))) ≤ -(K * ((μ : ℝ) - (ν : ℝ))) := by
    have hneg : (∑ h, ((n h - i h : ℕ) : ℝ) * (-(T h)))
        = -∑ h, ((n h - i h : ℕ) : ℝ) * T h := by
      rw [← Finset.sum_neg_distrib]
      exact Finset.sum_congr rfl (fun h _ => by ring)
    rw [hneg]
    linarith
  rw [step2] at step1
  exact le_trans step1 (Real.exp_le_exp.mpr step3)

/-- **The smallness bound, unconditional.**  `abs_coeff_translate_add_le_index` with `S` supplied.
`G_h ≤ 1` is not a hypothesis: it follows from `G_h ≤ exp(−T_h)` and `T_h ≥ K/r_h ≥ 0`. -/
theorem abs_coeff_translate_add_le_exp (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    (α γ : Fin m → ℝ) {G T : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h)
    (hGT : ∀ h, G h ≤ Real.exp (-(T h))) (hγ : ∀ h, |γ h| ≤ G h)
    {K : ℝ} (hK0 : 0 ≤ K) (hT : ∀ h, K ≤ T h * (r h : ℝ))
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |α h| ≤ B)
    {P : MvPolynomial (Fin m) ℝ} (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, |coeff k P| ≤ H)
    {μ ν : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α P)
    (i : Fin m →₀ ℕ) (hi : idxWeight r i ≤ ν) :
    |coeff i (translate (fun j => α j + γ j) P)|
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ)
        * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
            * ((2 : ℝ) ^ (∑ h, r h) * Real.exp (-(K * ((μ : ℝ) - (ν : ℝ)))))) := by
  have hT0 : ∀ h, 0 ≤ T h := by
    intro h
    have hrpos : (0 : ℝ) < (r h : ℝ) := by
      exact_mod_cast Nat.pos_of_ne_zero (hr h)
    nlinarith [hT h, hK0]
  have hG1 : ∀ h, G h ≤ 1 := by
    intro h
    refine le_trans (hGT h) ?_
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by linarith [hT0 h])
  exact abs_coeff_translate_add_le_index r α γ hG0 hG1 hγ hB1 hα hdeg hH hidx i
    (Real.exp_nonneg _)
    (fun n _ hμn => prod_pow_le_exp r hr hG0 hGT hK0 hT n i hμn hi)

end Gap

section Bridge

variable {m : ℕ}

/-- The `ℤ → ℚ → ℝ` transfer for a translated coefficient at a rational point. -/
theorem coeff_translate_cast (β : Fin m → ℚ) (P : MvPolynomial (Fin m) ℤ) (i : Fin m →₀ ℕ) :
    ((coeff i (translate β (map (Int.castRingHom ℚ) P)) : ℚ) : ℝ)
      = coeff i (translate (fun h => ((β h : ℚ) : ℝ)) (map (Int.castRingHom ℝ) P)) := by
  have hmap : map (Rat.castHom ℝ) (map (Int.castRingHom ℚ) P) = map (Int.castRingHom ℝ) P := by
    rw [map_map]
    congr 1
  calc ((coeff i (translate β (map (Int.castRingHom ℚ) P)) : ℚ) : ℝ)
      = coeff i (map (Rat.castHom ℝ) (translate β (map (Int.castRingHom ℚ) P))) := by
        rw [coeff_map]
        rfl
    _ = coeff i (translate (fun h => ((β h : ℚ) : ℝ))
          (map (Rat.castHom ℝ) (map (Int.castRingHom ℚ) P))) := by
        rw [map_translate]
        rfl
    _ = coeff i (translate (fun h => ((β h : ℚ) : ℝ)) (map (Int.castRingHom ℝ) P)) := by
        rw [hmap]

/-- **Step 2, closed modulo one numeric inequality.**  The index of `P` at the rational point is at
least `ν`, given that `P` has index at least `μ` at `α`, that `p_h/q_h` is within `G_h` of `α`, and
that the explicit size bound falls below `1/∏ q_h^{r_h}`.

The last hypothesis is a comparison between explicit quantities — no polynomial, no index, no
expansion — and discharging it is step 4's parameter bookkeeping, not this estimate's job. -/
theorem le_index_rational_of_taylor (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    (pn : Fin m → ℤ) (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0)
    (α : Fin m → ℝ) {G T : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h)
    (hGT : ∀ h, G h ≤ Real.exp (-(T h)))
    (hclose : ∀ h, |(((pn h : ℚ) / (qd h : ℚ) : ℚ) : ℝ) - α h| ≤ G h)
    {K : ℝ} (hK0 : 0 ≤ K) (hT : ∀ h, K ≤ T h * (r h : ℝ))
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |α h| ≤ B)
    (P : MvPolynomial (Fin m) ℤ) (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, |((coeff k P : ℤ) : ℝ)| ≤ H)
    {μ ν : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α (map (Int.castRingHom ℝ) P))
    (hfinal : ((∏ h, (r h + 1) : ℕ) : ℝ)
        * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
            * ((2 : ℝ) ^ (∑ h, r h) * Real.exp (-(K * ((μ : ℝ) - (ν : ℝ))))))
        < 1 / (∏ h, (qd h : ℝ) ^ (r h))) :
    ((ν : ℚ) : WithTop ℚ)
      ≤ index r (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P) := by
  classical
  have hdegR : ∀ h, degreeOf h (map (Int.castRingHom ℝ) P) ≤ r h :=
    fun h => le_trans (degreeOf_map_le _ _ P) (hdeg h)
  have hHR : ∀ k, |coeff k (map (Int.castRingHom ℝ) P)| ≤ H := by
    intro k
    rw [coeff_map]
    exact hH k
  refine le_index_of_abs_lt pn qd hq r P hdeg ν (fun i hi => ?_)
  have hbound := abs_coeff_translate_add_le_exp r hr α
    (fun h => ((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℝ) - α h) hG0 hGT hclose hK0 hT hB1 hα
    hdegR hHR hidx i hi.le
  have hsum : (fun j => α j + (((((pn j : ℚ) / (qd j : ℚ)) : ℚ) : ℝ) - α j))
      = fun h => ((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℝ) := by
    funext j
    ring
  rw [hsum] at hbound
  have hR : |((coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ))
      (map (Int.castRingHom ℚ) P)) : ℚ) : ℝ)| < 1 / (∏ h, (qd h : ℝ) ^ (r h)) := by
    rw [coeff_translate_cast]
    exact lt_of_le_of_lt hbound hfinal
  have hcast : ((1 / (∏ h, (qd h : ℚ) ^ (r h)) : ℚ) : ℝ) = 1 / (∏ h, (qd h : ℝ) ^ (r h)) := by
    push_cast
    ring
  rw [← Rat.cast_abs, ← hcast] at hR
  exact_mod_cast hR

/-- **The hypothesis bundle is satisfiable and the conclusion is not vacuous.**

Twelve hypotheses, several of them inequalities between constructed quantities, is exactly the
shape in which a theorem can be true because nothing satisfies it.  This discharges every one of
them at `m = 1`, `r = (1)`, `P = x`, `α = 0`, `p/q = 0/1`, `K = 8`, `μ = 1`, `ν = ½`, where
`hfinal` comes down to `16·e^{−4} < 1`.

⚠ What it does **not** show: `γ = β − α` is `0` here, so the Taylor machinery is not exercised.
A witness with `γ ≠ 0` is not available at small `m`: the constants `(box)²·H·(2B)^{Σr}·2^{Σr}`
only fall below `∏ q_h^{−r_h}` when `m` is large and the approximation exceptionally good, which
is Roth's inequality itself and hence step 4's business.  Recorded rather than papered over. -/
theorem le_index_rational_of_taylor_witness :
    (((1 : ℚ) / 2 : ℚ) : WithTop ℚ)
      ≤ index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => ((0 : ℤ) : ℚ) / ((1 : ℕ) : ℚ))
          (map (Int.castRingHom ℚ) (X 0)) := by
  have he1 : (2 : ℝ) < Real.exp 1 := by
    have h := Real.add_one_lt_exp (x := (1 : ℝ)) one_ne_zero
    linarith
  have he4 : (16 : ℝ) < Real.exp 4 := by
    have hpow : Real.exp 4 = (Real.exp 1) ^ (4 : ℕ) := by
      rw [← Real.exp_nat_mul]
      norm_num
    rw [hpow]
    have h2 : ((2 : ℝ)) ^ (4 : ℕ) < (Real.exp 1) ^ (4 : ℕ) :=
      pow_lt_pow_left₀ he1 (by norm_num) (by norm_num)
    norm_num at h2
    linarith
  have hexp : (16 : ℝ) * Real.exp (-4) < 1 := by
    rw [Real.exp_neg]
    rw [mul_inv_lt_iff₀ (Real.exp_pos 4)]
    linarith
  have hmapX : map (Int.castRingHom ℝ) (X 0 : MvPolynomial (Fin 1) ℤ) = X 0 := map_X _ _
  have htr : translate (fun _ : Fin 1 => (0 : ℝ)) (X 0 : MvPolynomial (Fin 1) ℝ) = X 0 := by
    rw [translate, aeval_X]
    simp
  have hidx : ((1 : ℚ) : WithTop ℚ)
      ≤ index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℝ))
          (map (Int.castRingHom ℝ) (X 0)) := by
    rw [le_index_iff]
    intro i hi
    rw [hmapX, htr, support_X, Finset.mem_singleton] at hi
    subst hi
    rw [idxWeight, Finsupp.support_single_ne_zero _ (one_ne_zero)]
    norm_num
  refine le_index_rational_of_taylor (fun _ : Fin 1 => 1) (fun _ => one_ne_zero)
    (fun _ => (0 : ℤ)) (fun _ => (1 : ℕ)) (fun _ => one_ne_zero)
    (fun _ => (0 : ℝ)) (G := fun _ => 0) (T := fun _ => 8)
    (fun _ => le_refl 0) (fun _ => Real.exp_nonneg _) (fun _ => by norm_num)
    (K := 8) (by norm_num) (fun _ => by norm_num)
    (B := 1) (le_refl 1) (fun _ => by norm_num)
    (X 0) (fun h => by rw [degreeOf_X]; split_ifs <;> norm_num)
    (H := 1) (fun k => by rw [coeff_X']; split_ifs <;> norm_num)
    (μ := 1) (ν := 1 / 2) hidx ?_
  simp only [Fin.prod_univ_one, Fin.sum_univ_one]
  norm_num
  linarith [hexp]

end Bridge

end MvPolynomial
