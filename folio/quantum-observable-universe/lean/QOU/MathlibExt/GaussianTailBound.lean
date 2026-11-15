/-
  THE GAUSSIAN TAIL OUTSIDE A WINDOW.

      ∑_{n∈ℤ} e^{−a(n−c)²}  −  ∑_{|n|≤W} e^{−a(n−c)²}
          ≤  e^{ac²}·e^{−a(W+1)²/4}·(1 + 2σ/(1−σ)),      σ = e^{−a/4}.

  This is the last piece of the window-versus-`ℤ` comparison.  The easy half
  (`∑_{window} ≤ ∑_{ℤ}`) is free from positivity; this is the other half, and
  it is what the LOWER bound on `⟨4₁⟩_N` needs — an upper bound on the window
  sum is not enough to pin a constant.

  **The bound is deliberately crude.**  Three inequalities in a row, each
  giving away a factor:

    * `(n−c)² ≥ n²/2 − c²`, which costs the `e^{ac²}` and forgets that the
      shift `c` is `O(1)` while `n` is large;
    * `n² ≥ (W+1)²/2 + n²/2` for `|n| ≥ W+1`, splitting the decay in two;
    * `n² ≥ |n|`, turning what is left into a geometric series.

  A sharp tail would keep `e^{−a(W+1)²}` rather than `e^{−a(W+1)²/4}`.  It does
  not matter: in the Kashaev application `a ≈ √3π/N` and `W ≈ N^{0.6}`, so
  `a(W+1)²/4 ≈ 1.36·N^{0.2} → ∞` — the tail is beyond super-polynomially small
  either way, and the factor `1/(1−σ) ≈ 4/a ≈ N` it has to beat is nothing.
  Sharpening this would be work spent where no constant is at stake.

  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaBound.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianTiltedSum.lean
-/
import QOU.MathlibExt.GaussianThetaBound

namespace QOU.MathlibExt

open Real

/-- The full two-sided geometric series over `ℤ`: `∑_{n∈ℤ} q^{|n|} = 1 + 2q/(1−q)`.
`hasSum_int_geometric_ne_zero` with the `n = 0` term put back. -/
theorem hasSum_int_geometric {q : ℝ} (hq0 : 0 ≤ q) (hq1 : q < 1) :
    HasSum (fun n : ℤ => q ^ n.natAbs) (1 + 2 * q / (1 - q)) := by
  have h := (hasSum_ite_eq (0 : ℤ) (1 : ℝ)).add
    (hasSum_int_geometric_ne_zero hq0 hq1)
  have heq : (fun n : ℤ => (if n = 0 then (1 : ℝ) else 0)
        + if n = 0 then (0 : ℝ) else q ^ n.natAbs)
      = fun n : ℤ => q ^ n.natAbs := by
    funext n
    by_cases hn : n = 0 <;> simp [hn]
  rwa [heq] at h

/-- **The tail outside `[−W, W]`.**  Everything the window misses, bounded by a
quantity that is super-polynomially small in `W`. -/
theorem tsum_gaussian_sub_sum_Icc_le {a c : ℝ} (ha : 0 < a) (W : ℕ) :
    (∑' n : ℤ, Real.exp (-a * ((n : ℝ) - c) ^ 2))
        - ∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ), Real.exp (-a * ((n : ℝ) - c) ^ 2)
      ≤ Real.exp (a * c ^ 2) * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4)
        * (1 + 2 * Real.exp (-a / 4) / (1 - Real.exp (-a / 4))) := by
  have hσ0 : 0 < Real.exp (-a / 4) := Real.exp_pos _
  have hσ1 : Real.exp (-a / 4) < 1 := by
    rw [Real.exp_lt_one_iff]; linarith
  have hg := hasSum_gaussian_theta_real a c ha
  -- the window part, as a `HasSum` of the indicator
  have hF : HasSum
      (fun n : ℤ => if n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ)
        then Real.exp (-a * ((n : ℝ) - c) ^ 2) else 0)
      (∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ), Real.exp (-a * ((n : ℝ) - c) ^ 2)) := by
    have hsum : (∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
          if n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ)
            then Real.exp (-a * ((n : ℝ) - c) ^ 2) else 0)
        = ∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ), Real.exp (-a * ((n : ℝ) - c) ^ 2) :=
      Finset.sum_congr rfl fun b hb => by simp [hb]
    rw [← hsum]
    exact hasSum_sum_of_ne_finset_zero fun b hb => by simp [hb]
  have hdiff := hg.sub hF
  have hfun : (fun n : ℤ => Real.exp (-a * ((n : ℝ) - c) ^ 2)
        - if n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ)
            then Real.exp (-a * ((n : ℝ) - c) ^ 2) else 0)
      = fun n : ℤ => if n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ) then 0
          else Real.exp (-a * ((n : ℝ) - c) ^ 2) := by
    funext n
    by_cases hn : n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ) <;> simp [hn]
  rw [hfun] at hdiff
  have hgeo := (hasSum_int_geometric hσ0.le hσ1).mul_left
    (Real.exp (a * c ^ 2) * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4))
  -- pointwise: outside the window the Gaussian is under `C·σ^{|n|}`
  have hpt : ∀ n : ℤ,
      (if n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ) then 0
        else Real.exp (-a * ((n : ℝ) - c) ^ 2))
      ≤ Real.exp (a * c ^ 2) * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4)
        * Real.exp (-a / 4) ^ n.natAbs := by
    intro n
    by_cases hn : n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ)
    · rw [if_pos hn]; positivity
    · rw [if_neg hn]
      -- `|n| ≥ W + 1`
      rw [Finset.mem_Icc] at hn
      push_neg at hn
      have h1 : (W : ℤ) + 1 ≤ |n| := by
        rcases le_or_gt 0 n with hge | hlt
        · have hlow : -(W : ℤ) ≤ n := by omega
          have := hn hlow
          rw [abs_of_nonneg hge]; omega
        · rw [abs_of_neg hlt]; omega
      have hnabs : ((W : ℝ) + 1) ≤ |(n : ℝ)| := by
        have h2 := (Int.cast_le (R := ℝ)).mpr h1
        push_cast at h2
        exact h2
      have hcast : ((n.natAbs : ℕ) : ℝ) = |(n : ℝ)| := by
        rw [Int.cast_natAbs]; push_cast; ring
      have hpow : Real.exp (-a / 4) ^ n.natAbs
          = Real.exp (|(n : ℝ)| * (-a / 4)) := by
        rw [← hcast]; exact (Real.exp_nat_mul _ _).symm
      rw [hpow, ← Real.exp_add, ← Real.exp_add]
      refine Real.exp_le_exp.mpr ?_
      have hsq : ((n : ℝ)) ^ 2 = |(n : ℝ)| ^ 2 := (sq_abs _).symm
      have hW0 : (0 : ℝ) ≤ (W : ℝ) := by positivity
      have hW1 : (1 : ℝ) ≤ (W : ℝ) + 1 := by linarith
      have hmnn : (0 : ℝ) ≤ |(n : ℝ)| := abs_nonneg _
      -- `(W+1)²/4 + |n|/4 ≤ n²/2`, from `|n| ≥ W+1 ≥ 1`
      have hstep : ((W : ℝ) + 1) ^ 2 / 4 + |(n : ℝ)| / 4 ≤ (n : ℝ) ^ 2 / 2 := by
        rw [hsq]
        nlinarith [mul_nonneg (sub_nonneg.mpr hnabs)
            (by linarith : (0 : ℝ) ≤ |(n : ℝ)| + ((W : ℝ) + 1)),
          mul_nonneg hmnn (by linarith : (0 : ℝ) ≤ |(n : ℝ)| - 1)]
      -- `(n−c)² + c² ≥ n²/2`
      have hhalf : (n : ℝ) ^ 2 / 2 - c ^ 2 ≤ ((n : ℝ) - c) ^ 2 := by
        nlinarith [sq_nonneg ((n : ℝ) - 2 * c)]
      have hcomb : (0 : ℝ) ≤ ((n : ℝ) - c) ^ 2 + c ^ 2
          - (((W : ℝ) + 1) ^ 2 / 4 + |(n : ℝ)| / 4) := by linarith
      nlinarith [mul_nonneg ha.le hcomb]
  have hle := hasSum_le hpt hdiff hgeo
  rw [hg.tsum_eq]
  calc (Real.sqrt (π / a)
        * (jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a)).re)
        - ∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ), Real.exp (-a * ((n : ℝ) - c) ^ 2)
      ≤ Real.exp (a * c ^ 2) * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4)
        * (1 + 2 * Real.exp (-a / 4) / (1 - Real.exp (-a / 4))) := hle

end QOU.MathlibExt
