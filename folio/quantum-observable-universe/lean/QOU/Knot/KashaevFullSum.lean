/-
  `⟨4₁⟩_N` AGAINST THE GAUSSIAN CLOSED FORM — the whole sum, all four regions.

      | ⟨4₁⟩_N  −  g_{k*}·e^{L²/a}√(π/a) |
          ≤  g_{k*}·( window + below + left + right )

  `Finset.range N` splits at three points:

      [0, w)          below the secant region — step 5, crude and free
      [w, k*−W)       left tail            — step 17, e^{−π(W+1)W/(√3N)}
      [k*−W, k*+W]    the window           — step 16, the only real work
      (k*+W, N)       right tail           — step 17, e^{−√3π(W+1)W/N}

  Only the window carries any of the constant.  The other three are error
  terms that vanish relative to `√N`, which is all that is asked of them — and
  the below-secant region vanishes so violently (`1e-182` of the main term at
  `N = 3841`) that step 5's crude constants there cost nothing whatever.

  The split points are hypotheses, not choices baked in: `w` must sit in the
  secant region (`2N ≤ 3w`) with two steps of clearance below `k*`, and the
  window must fit between `w` and `N`.  A caller picks `w ≈ 2N/3` and
  `W ≈ N^{0.6}`.

  -- Ref: [leitner2026] QOU/Knot/KashaevSaddleWindow.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevBeyondWindow.lean
-/
import QOU.Knot.KashaevBeyondWindow

namespace QOU.Knot.FigureEightVolume

open Real

/-- **`range N` in four pieces.** -/
theorem kashaev_split {N W w : ℕ} (hwW : w ≤ 5 * N / 6 - W)
    (hWN : 5 * N / 6 + W + 1 ≤ N) :
    kashaev N
      = (∑ k ∈ Finset.range w, kashaevProd N k)
        + (∑ k ∈ Finset.Ico w (5 * N / 6 - W), kashaevProd N k)
        + (∑ k ∈ Finset.Icc (5 * N / 6 - W) (5 * N / 6 + W), kashaevProd N k)
        + (∑ k ∈ Finset.Ico (5 * N / 6 + W + 1) N, kashaevProd N k) := by
  have e1 : (∑ k ∈ Finset.Ico 0 w, kashaevProd N k)
        + ∑ k ∈ Finset.Ico w N, kashaevProd N k
      = ∑ k ∈ Finset.Ico 0 N, kashaevProd N k :=
    Finset.sum_Ico_consecutive _ (Nat.zero_le w) (by omega)
  have e2 : (∑ k ∈ Finset.Ico w (5 * N / 6 - W), kashaevProd N k)
        + ∑ k ∈ Finset.Ico (5 * N / 6 - W) N, kashaevProd N k
      = ∑ k ∈ Finset.Ico w N, kashaevProd N k :=
    Finset.sum_Ico_consecutive _ hwW (by omega)
  have e3 : (∑ k ∈ Finset.Ico (5 * N / 6 - W) (5 * N / 6 + W + 1), kashaevProd N k)
        + ∑ k ∈ Finset.Ico (5 * N / 6 + W + 1) N, kashaevProd N k
      = ∑ k ∈ Finset.Ico (5 * N / 6 - W) N, kashaevProd N k :=
    Finset.sum_Ico_consecutive _ (by omega) hWN
  have e4 : Finset.Ico (5 * N / 6 - W) (5 * N / 6 + W + 1)
      = Finset.Icc (5 * N / 6 - W) (5 * N / 6 + W) := by
    ext j
    simp only [Finset.mem_Ico, Finset.mem_Icc]
    omega
  rw [e4] at e3
  unfold kashaev
  rw [Finset.range_eq_Ico, ← e1, ← e2, ← e3, ← Finset.range_eq_Ico]
  ring

/-- **The whole invariant against the closed form.**

Everything is relative to `g_{k*}`; the four error terms are, in order, the
window's (step 16), the below-secant region's (step 5), the left tail's and
the right tail's (step 17). -/
theorem abs_kashaev_sub_model_le {N W w : ℕ} (hN : 6 ≤ N) (hN4 : 4 ≤ N)
    (hw1 : 6 * w ≤ 5 * N) (hw2 : 2 * N ≤ 3 * w) (hwk : w ≤ 5 * N / 6)
    (hD : 2 ≤ 5 * N / 6 - w) (hwW : w ≤ 5 * N / 6 - W)
    (hWN : 5 * N / 6 + W + 1 ≤ N) (hWk : W ≤ 5 * N / 6)
    (hk1 : 1 ≤ 5 * N / 6 - W)
    (hlo : π / 2 < ((5 * N / 6 : ℕ) : ℝ) * π / N)
    (hhi : ((5 * N / 6 : ℕ) : ℝ) * π / N < π)
    {M K B : ℝ}
    (hmem : ∀ x ∈ Set.Icc (((5 * N / 6 - W : ℕ) : ℝ) * π / N)
        (((5 * N / 6 + W : ℕ) : ℝ) * π / N), 0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.Icc (((5 * N / 6 - W : ℕ) : ℝ) * π / N)
        (((5 * N / 6 + W : ℕ) : ℝ) * π / N), 1 / Real.sin x ^ 2 ≤ M)
    (hK : ∀ x ∈ Set.Icc (((5 * N / 6 - W : ℕ) : ℝ) * π / N)
        (((5 * N / 6 + W : ℕ) : ℝ) * π / N), |Real.cos x / Real.sin x| ≤ K)
    (hB : ∀ k' ∈ Finset.Icc (5 * N / 6 - W) (5 * N / 6 + W),
        logKashaevErr N (5 * N / 6) + logKashaevErr N k'
          + M * π ^ 2 * |(k' : ℝ) - ((5 * N / 6 : ℕ) : ℝ)| ^ 3 / (3 * (N : ℝ) ^ 2)
          + K * π * |(k' : ℝ) - ((5 * N / 6 : ℕ) : ℝ)| / (N : ℝ)
          + M * π ^ 2 * |(k' : ℝ) - ((5 * N / 6 : ℕ) : ℝ)| / (6 * (N : ℝ) ^ 2)
          ≤ B) :
    |kashaev N
        - kashaevProd N (5 * N / 6)
          * (Real.exp (kashaevTilt N (5 * N / 6) ^ 2
                       / kashaevGaussCoeff N (5 * N / 6))
             * Real.sqrt (π / kashaevGaussCoeff N (5 * N / 6)))|
      ≤ kashaevProd N (5 * N / 6)
        * (((Real.exp B - 1)
              * (Real.exp (kashaevTilt N (5 * N / 6) ^ 2
                           / kashaevGaussCoeff N (5 * N / 6))
                   * Real.sqrt (π / kashaevGaussCoeff N (5 * N / 6))
                 + gaussWindowErr (kashaevGaussCoeff N (5 * N / 6))
                     (kashaevTilt N (5 * N / 6)) W)
            + gaussWindowErr (kashaevGaussCoeff N (5 * N / 6))
                (kashaevTilt N (5 * N / 6)) W)
           + ((w : ℝ) / (N : ℝ) ^ 2
              + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
                / (π * ((5 * N / 6 - w : ℕ) : ℝ)
                   * (((5 * N / 6 - w : ℕ) : ℝ) - 1)))
           + (N : ℝ) * Real.exp (-(π * ((W : ℝ) + 1) * (W : ℝ)
                                   / (Real.sqrt 3 * N)))
           + (N : ℝ) * Real.exp (-(Real.sqrt 3 * π * ((W : ℝ) + 1) * (W : ℝ)
                                   / N))) := by
  have hgpos := kashaevProd_pos (N := N) (k := 5 * N / 6) (by omega)
  -- the window, from step 16
  have hwin := abs_sum_kashaevProd_saddle_window_le (N := N) (k := 5 * N / 6)
    (W := W) (by omega) hN4 hWk hk1 (by omega) hlo hhi hmem hM hK hB
  -- the three outside regions
  have hbelow := sum_kashaevProd_below_window_le_argmax hN hw1 hw2 hwk hD
  have hleft := sum_kashaevProd_left_beyond_le (N := N) (W := W) (w := w) hN hw2 hwk
  have hright := sum_kashaevProd_right_beyond_le (N := N) (W := W) hN
  -- and they are all nonnegative
  have nb : (0 : ℝ) ≤ ∑ k ∈ Finset.range w, kashaevProd N k :=
    Finset.sum_nonneg fun k _ => kashaevProd_nonneg N k
  have nl : (0 : ℝ) ≤ ∑ k ∈ Finset.Ico w (5 * N / 6 - W), kashaevProd N k :=
    Finset.sum_nonneg fun k _ => kashaevProd_nonneg N k
  have nr : (0 : ℝ) ≤ ∑ k ∈ Finset.Ico (5 * N / 6 + W + 1) N, kashaevProd N k :=
    Finset.sum_nonneg fun k _ => kashaevProd_nonneg N k
  have hsplit := kashaev_split (N := N) (W := W) (w := w) hwW hWN
  have hrw : kashaev N
        - kashaevProd N (5 * N / 6)
          * (Real.exp (kashaevTilt N (5 * N / 6) ^ 2
                       / kashaevGaussCoeff N (5 * N / 6))
             * Real.sqrt (π / kashaevGaussCoeff N (5 * N / 6)))
      = ((∑ k ∈ Finset.Icc (5 * N / 6 - W) (5 * N / 6 + W), kashaevProd N k)
          - kashaevProd N (5 * N / 6)
            * (Real.exp (kashaevTilt N (5 * N / 6) ^ 2
                         / kashaevGaussCoeff N (5 * N / 6))
               * Real.sqrt (π / kashaevGaussCoeff N (5 * N / 6))))
        + ((∑ k ∈ Finset.range w, kashaevProd N k)
           + (∑ k ∈ Finset.Ico w (5 * N / 6 - W), kashaevProd N k)
           + (∑ k ∈ Finset.Ico (5 * N / 6 + W + 1) N, kashaevProd N k)) := by
    rw [hsplit]; ring
  rw [hrw]
  refine le_trans (abs_add_le _ _) ?_
  rw [abs_of_nonneg (by linarith : (0 : ℝ) ≤
    (∑ k ∈ Finset.range w, kashaevProd N k)
    + (∑ k ∈ Finset.Ico w (5 * N / 6 - W), kashaevProd N k)
    + (∑ k ∈ Finset.Ico (5 * N / 6 + W + 1) N, kashaevProd N k))]
  linarith [hwin, hbelow, hleft, hright]

end QOU.Knot.FigureEightVolume
