/-
  THE ASSEMBLY, SPECIALISED TO THE KASHAEV VALUES.

  `KashaevWindowAssembly` is stated for abstract `a`, `L`, `B`.  This file
  supplies them:

      a = −π·cot θ_k / N        (positive exactly when `θ_k > π/2`)
      L = log(2 sin θ_k)

  and derives the assembly's per-index hypothesis from step 10's
  `abs_log_kashaevProd_ratio_gaussian`.

  Two things are worth naming.

  **The angular hypotheses are given on ONE interval.**  Step 10 wants
  `1/sin²` and `|cot|` bounded on `uIcc θ_k θ_{k'}`, separately for every `k'`
  in the window.  Asking for them on the single interval
  `[θ_{k−W}, θ_{k+W}]` is enough, since `uIcc` of two of its points lies inside
  it — and it is the only form a caller can actually check.

  **`B` stays abstract.**  It is required only to dominate step 10's per-pair
  bound across the window; computing an explicit maximum is arithmetic in `N`
  and `W` that belongs to the caller.  Lumping it into a closed form would fix
  a particular window scaling into the statement.

  -- Ref: [leitner2026] QOU/Knot/KashaevWindowAssembly.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevRatioExpansion.lean
-/
import QOU.Knot.KashaevWindowAssembly

namespace QOU.Knot.FigureEightVolume

open Real QOU.MathlibExt

/-- The Gaussian coefficient at index `k`: `a = −π·cot θ_k / N`. -/
noncomputable def kashaevGaussCoeff (N k : ℕ) : ℝ :=
  -(π * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)) / (N : ℝ))

/-- The tilt at index `k`: `L = log(2 sin θ_k)`. -/
noncomputable def kashaevTilt (N k : ℕ) : ℝ :=
  Real.log (2 * Real.sin ((k : ℝ) * π / N))

/-- `a > 0` exactly when the angle is past `π/2` — which is where the saddle
`5π/6` lives, and is why the summand is a Gaussian rather than a growing
exponential. -/
theorem kashaevGaussCoeff_pos {N k : ℕ} (hN : 0 < N)
    (hlo : π / 2 < (k : ℝ) * π / N) (hhi : (k : ℝ) * π / N < π) :
    0 < kashaevGaussCoeff N k := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hs : 0 < Real.sin ((k : ℝ) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) hhi
  have hc : Real.cos ((k : ℝ) * π / N) < 0 :=
    Real.cos_neg_of_pi_div_two_lt_of_lt hlo (by linarith)
  unfold kashaevGaussCoeff
  have hdiv : Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N) < 0 :=
    div_neg_of_neg_of_pos hc hs
  have hq : π * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))
      / (N : ℝ) < 0 :=
    div_neg_of_neg_of_pos (mul_neg_of_pos_of_neg hpi hdiv) hNpos
  linarith

/-- Every index in the window has its angle inside the window's angular range.
Monotonicity of `x ↦ xπ/N`, nothing more — but it is what lets one pair of
angular hypotheses serve every `k'`. -/
theorem angle_mem_window {N k W : ℕ} (hN : 0 < N) {k' : ℕ}
    (hk' : k' ∈ Finset.Icc (k - W) (k + W)) :
    ((k' : ℝ) * π / N) ∈ Set.Icc (((k - W : ℕ) : ℝ) * π / N)
      (((k + W : ℕ) : ℝ) * π / N) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hpn : (0 : ℝ) ≤ π / N := by positivity
  rw [Finset.mem_Icc] at hk'
  have h1 : ((k - W : ℕ) : ℝ) ≤ (k' : ℝ) := by exact_mod_cast hk'.1
  have h2 : (k' : ℝ) ≤ ((k + W : ℕ) : ℝ) := by exact_mod_cast hk'.2
  rw [Set.mem_Icc]
  constructor
  · calc ((k - W : ℕ) : ℝ) * π / N = ((k - W : ℕ) : ℝ) * (π / N) := by ring
      _ ≤ (k' : ℝ) * (π / N) := mul_le_mul_of_nonneg_right h1 hpn
      _ = (k' : ℝ) * π / N := by ring
  · calc (k' : ℝ) * π / N = (k' : ℝ) * (π / N) := by ring
      _ ≤ ((k + W : ℕ) : ℝ) * (π / N) := mul_le_mul_of_nonneg_right h2 hpn
      _ = ((k + W : ℕ) : ℝ) * π / N := by ring

/-- **The Kashaev window against the Gaussian closed form.**

The hypotheses are exactly what a caller can check: the window's angular range
sits inside `(0, π)`, `1/sin²` and `|cot|` are bounded there, and `B` dominates
step 10's per-pair bound. -/
theorem abs_sum_kashaevProd_saddle_window_le {N k W : ℕ} (hkN : k < N)
    (hN4 : 4 ≤ N) (hW : W ≤ k) (hk1 : 1 ≤ k - W) (hkWN : k + W < N)
    (hlo : π / 2 < (k : ℝ) * π / N) (hhi : (k : ℝ) * π / N < π)
    {M K B : ℝ}
    (hmem : ∀ x ∈ Set.Icc (((k - W : ℕ) : ℝ) * π / N) (((k + W : ℕ) : ℝ) * π / N),
        0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.Icc (((k - W : ℕ) : ℝ) * π / N) (((k + W : ℕ) : ℝ) * π / N),
        1 / Real.sin x ^ 2 ≤ M)
    (hK : ∀ x ∈ Set.Icc (((k - W : ℕ) : ℝ) * π / N) (((k + W : ℕ) : ℝ) * π / N),
        |Real.cos x / Real.sin x| ≤ K)
    (hB : ∀ k' ∈ Finset.Icc (k - W) (k + W),
        logKashaevErr N k + logKashaevErr N k'
          + M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| ^ 3 / (3 * (N : ℝ) ^ 2)
          + K * π * |(k' : ℝ) - (k : ℝ)| / (N : ℝ)
          + M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| / (6 * (N : ℝ) ^ 2) ≤ B) :
    |(∑ k' ∈ Finset.Icc (k - W) (k + W), kashaevProd N k')
        - kashaevProd N k
          * (Real.exp (kashaevTilt N k ^ 2 / kashaevGaussCoeff N k)
             * Real.sqrt (π / kashaevGaussCoeff N k))|
      ≤ kashaevProd N k
        * ((Real.exp B - 1)
             * (Real.exp (kashaevTilt N k ^ 2 / kashaevGaussCoeff N k)
                  * Real.sqrt (π / kashaevGaussCoeff N k)
                + gaussWindowErr (kashaevGaussCoeff N k) (kashaevTilt N k) W)
           + gaussWindowErr (kashaevGaussCoeff N k) (kashaevTilt N k) W) := by
  have hpi := Real.pi_pos
  have hNz : 0 < N := by omega
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hNz
  have ha := kashaevGaussCoeff_pos hNz hlo hhi
  have hkmem : k ∈ Finset.Icc (k - W) (k + W) := by
    rw [Finset.mem_Icc]; omega
  have hs : ∀ k' ∈ Finset.Icc (k - W) (k + W), k' < N := by
    intro k' hk'
    rw [Finset.mem_Icc] at hk'
    omega
  -- the per-index hypothesis the assembly wants, from step 10
  have hh : ∀ k' ∈ Finset.Icc (k - W) (k + W),
      |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (-(kashaevGaussCoeff N k) * ((k' : ℝ) - (k : ℝ)) ^ 2
           + 2 * kashaevTilt N k * ((k' : ℝ) - (k : ℝ)))| ≤ B := by
    intro k' hk'
    have hk'mem := Finset.mem_Icc.mp hk'
    have hsub := Set.uIcc_subset_Icc (angle_mem_window (W := W) hNz hkmem)
      (angle_mem_window (W := W) hNz hk')
    have hmem' : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N),
        0 < x ∧ x < π := fun x hx => hmem x (hsub hx)
    have hM' : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N),
        1 / Real.sin x ^ 2 ≤ M := fun x hx => hM x (hsub hx)
    have hK' : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N),
        |Real.cos x / Real.sin x| ≤ K := fun x hx => hK x (hsub hx)
    have h10 := abs_log_kashaevProd_ratio_gaussian (by omega : 1 ≤ k) hkN
      (by omega : 1 ≤ k') (hs k' hk') hN4 hmem' hM' hK'
    -- the two ways of writing the target agree
    have htarget : -(kashaevGaussCoeff N k) * ((k' : ℝ) - (k : ℝ)) ^ 2
          + 2 * kashaevTilt N k * ((k' : ℝ) - (k : ℝ))
        = 2 * ((k' : ℝ) - (k : ℝ)) * Real.log (2 * Real.sin ((k : ℝ) * π / N))
          + (π * ((k' : ℝ) - (k : ℝ)) ^ 2 / (N : ℝ))
            * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)) := by
      unfold kashaevGaussCoeff kashaevTilt
      field_simp
      ring
    rw [htarget]
    exact le_trans h10 (hB k' hk')
  exact abs_sum_kashaevProd_window_sub_model_le hkN hW ha hs hh

end QOU.Knot.FigureEightVolume
