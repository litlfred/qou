/-
  EVERYTHING OUTSIDE THE WINDOW.

  The assembly controls `∑_{|k−k*|≤W} g_k`.  `⟨4₁⟩_N` is the sum over all of
  `[0, N)`, so the rest has to be shown negligible.  It is, and by a wide
  margin: step 5's per-step tail bounds give `g_{k*±d} ≤ g_{k*}·e^{−c d(d−1)/N}`,
  so beyond `|d| > W` every term is under `e^{−c W(W+1)/N}` — and with
  `W ≈ N^{0.6}` that exponent is `≈ N^{0.2}`.

  **The bound here is card × largest term**, not a geometric sum.  A geometric
  sum would give `e^{−cW²/N}/(1−e^{−cW/N})` instead of `N·e^{−cW²/N}`; both are
  crushed by the exponential, and `Finset.sum_le_card_nsmul` costs three lines
  where the geometric series costs thirty.  Nothing that matters is lost —
  the region has to beat `√N`, not `N`.

  The two directions are NOT symmetric.  The right tail runs to `N` with no
  extra condition; the left one only holds inside the secant window `2N ≤ 3k`,
  because that is where step 5's lower-bound chord is valid.  Below `2N/3` the
  sum is handled separately and much more crudely (`KashaevTailBound`'s
  `sum_kashaevProd_below_window_le_argmax`) — crudely enough is enough there,
  since that whole region contributes `O(1)·g_{k*}` against a main term of
  `Θ(√N)·g_{k*}`.

  -- Ref: [leitner2026] QOU/Knot/KashaevTailBound.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevSaddleWindow.lean
-/
import QOU.Knot.KashaevSaddleWindow
import QOU.Knot.KashaevTailBound

namespace QOU.Knot.FigureEightVolume

open Real

/-- `d(d−1) ≥ (W+1)W` once `d ≥ W+1` — the step that turns a per-index tail
bound into a uniform one. -/
theorem mul_pred_le_of_le {W d : ℕ} (hd : W + 1 ≤ d) :
    ((W : ℝ) + 1) * (W : ℝ) ≤ (d : ℝ) * ((d : ℝ) - 1) := by
  have h1 : ((W : ℝ) + 1) ≤ (d : ℝ) := by exact_mod_cast hd
  have h2 : (0 : ℝ) ≤ (W : ℝ) := by positivity
  nlinarith

/-- **The right tail beyond the window.**  Everything from `k* + W + 1` up to
`N`, bounded by `N` copies of the largest term. -/
theorem sum_kashaevProd_right_beyond_le {N W : ℕ} (hN : 6 ≤ N) :
    ∑ k ∈ Finset.Ico (5 * N / 6 + W + 1) N, kashaevProd N k
      ≤ (N : ℝ) * (kashaevProd N (5 * N / 6)
          * Real.exp (-(Real.sqrt 3 * π * ((W : ℝ) + 1) * (W : ℝ) / N))) := by
  have hpi := Real.pi_pos
  have hs3 : (0 : ℝ) ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hgpos := kashaevProd_pos (N := N) (k := 5 * N / 6) (by omega)
  have hbound : ∀ k ∈ Finset.Ico (5 * N / 6 + W + 1) N,
      kashaevProd N k ≤ kashaevProd N (5 * N / 6)
        * Real.exp (-(Real.sqrt 3 * π * ((W : ℝ) + 1) * (W : ℝ) / N)) := by
    intro k hk
    rw [Finset.mem_Ico] at hk
    have hlt : 5 * N / 6 + (k - 5 * N / 6) < N := by omega
    have heq : 5 * N / 6 + (k - 5 * N / 6) = k := by omega
    have h := kashaevProd_right_tail hN (k - 5 * N / 6) hlt
    rw [heq] at h
    refine le_trans h (mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr ?_) hgpos.le)
    have hdW : W + 1 ≤ k - 5 * N / 6 := by omega
    have hmul := mul_pred_le_of_le hdW
    have hnn : (0 : ℝ) ≤ Real.sqrt 3 * π := by positivity
    have hscaled : Real.sqrt 3 * π * (((W : ℝ) + 1) * (W : ℝ))
        ≤ Real.sqrt 3 * π * (((k - 5 * N / 6 : ℕ) : ℝ)
            * (((k - 5 * N / 6 : ℕ) : ℝ) - 1)) :=
      mul_le_mul_of_nonneg_left hmul hnn
    rw [neg_le_neg_iff, div_le_div_iff_of_pos_right hNpos]
    linarith
  have hcard := Finset.sum_le_card_nsmul _ _ _ hbound
  rw [nsmul_eq_mul] at hcard
  refine le_trans hcard (mul_le_mul_of_nonneg_right ?_ (by positivity))
  have : ((Finset.Ico (5 * N / 6 + W + 1) N).card : ℕ) ≤ N := by
    rw [Nat.card_Ico]; omega
  exact_mod_cast this

/-- **The left tail beyond the window**, valid inside the secant region
`2N ≤ 3k` — which is where step 5's lower-bound chord holds and no further. -/
theorem sum_kashaevProd_left_beyond_le {N W w : ℕ} (hN : 6 ≤ N)
    (hw : 2 * N ≤ 3 * w) (hwk : w ≤ 5 * N / 6) :
    ∑ k ∈ Finset.Ico w (5 * N / 6 - W), kashaevProd N k
      ≤ (N : ℝ) * (kashaevProd N (5 * N / 6)
          * Real.exp (-(π * ((W : ℝ) + 1) * (W : ℝ) / (Real.sqrt 3 * N)))) := by
  have hpi := Real.pi_pos
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hgpos := kashaevProd_pos (N := N) (k := 5 * N / 6) (by omega)
  have hbound : ∀ k ∈ Finset.Ico w (5 * N / 6 - W),
      kashaevProd N k ≤ kashaevProd N (5 * N / 6)
        * Real.exp (-(π * ((W : ℝ) + 1) * (W : ℝ) / (Real.sqrt 3 * N))) := by
    intro k hk
    rw [Finset.mem_Ico] at hk
    have hkle : k ≤ 5 * N / 6 := by omega
    have hdle : 5 * N / 6 - k ≤ 5 * N / 6 := by omega
    have heq : 5 * N / 6 - (5 * N / 6 - k) = k := by omega
    have hlo : 2 * N ≤ 3 * (5 * N / 6 - (5 * N / 6 - k)) := by omega
    have h := kashaevProd_left_tail (b := 5 * N / 6) (by omega)
      (by omega) (5 * N / 6 - k) hdle hlo
    rw [heq] at h
    refine le_trans h (mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr ?_) hgpos.le)
    have hdW : W + 1 ≤ 5 * N / 6 - k := by omega
    have hmul := mul_pred_le_of_le hdW
    have hscaled : π * (((W : ℝ) + 1) * (W : ℝ))
        ≤ π * (((5 * N / 6 - k : ℕ) : ℝ) * (((5 * N / 6 - k : ℕ) : ℝ) - 1)) :=
      mul_le_mul_of_nonneg_left hmul hpi.le
    rw [neg_le_neg_iff, div_le_div_iff_of_pos_right (by positivity)]
    linarith
  have hcard := Finset.sum_le_card_nsmul _ _ _ hbound
  rw [nsmul_eq_mul] at hcard
  refine le_trans hcard (mul_le_mul_of_nonneg_right ?_ (by positivity))
  have : ((Finset.Ico w (5 * N / 6 - W)).card : ℕ) ≤ N := by
    rw [Nat.card_Ico]; omega
  exact_mod_cast this

end QOU.Knot.FigureEightVolume
