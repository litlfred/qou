/-
  THE ASSEMBLY: the Kashaev window sum against the Gaussian closed form.

      | ∑_{|k'−k|≤W} g_{k'}  −  g_k·e^{L²/a}√(π/a) |
          ≤  g_k·( (e^B − 1)(e^{L²/a}√(π/a) + E)  +  E )

  with `E` the window error of `GaussianWindowSum` and `B` the uniform error of
  step 10's ratio expansion.  Everything on the right vanishes relative to the
  main term exactly when `B → 0` and `E/√(π/a) → 0`, which is what steps 10 and
  13 established.

  Three ingredients meet:

    * step 11 (`sum_kashaevProd_window_sandwich`) — the window sum against the
      MODEL sum `∑ e^{T}`, to within `e^{±B}`;
    * step 14 (`sum_Icc_shift_int`) — the model sum reindexed from a `ℕ`-window
      around `k` to a `ℤ`-window around `0`;
    * step 14 (`abs_sum_Icc_tilted_sub_le`) — the reindexed model sum against
      the closed form.

  `a`, `L`, `B` are parameters, not the Kashaev values.  The hypothesis is
  exactly what `abs_log_kashaevProd_ratio_gaussian` delivers, so specialising is
  a matter of supplying `a = π|cot θ_k|/N` and `L = log(2 sin θ_k)` — but the
  assembly itself has no knot in it.

  -- Ref: [leitner2026] QOU/Knot/KashaevWindowSum.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianWindowSum.lean
-/
import QOU.Knot.KashaevWindowIndex

namespace QOU.Knot.FigureEightVolume

open Real QOU.MathlibExt

/-- The window error of `abs_sum_Icc_tilted_sub_le`, named. -/
noncomputable def gaussWindowErr (a L : ℝ) (W : ℕ) : ℝ :=
  Real.exp (L ^ 2 / a)
    * (Real.sqrt (π / a)
         * (2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a))))
       + Real.exp (a * (L / a) ^ 2)
         * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4)
         * (1 + 2 * Real.exp (-a / 4) / (1 - Real.exp (-a / 4))))

/-- Inside a symmetric window that does not run off the bottom of `ℕ`, the
shifted index casts back to the offset.  Without `W ≤ k` this is false —
`Int.toNat` clamps — which is exactly what `sum_Icc_shift_int` needs it for. -/
theorem cast_toNat_shift_sub {W k : ℕ} (hW : W ≤ k) {n : ℤ}
    (hn : n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ)) :
    ((((k : ℤ) + n).toNat : ℕ) : ℝ) - (k : ℝ) = (n : ℝ) := by
  rw [Finset.mem_Icc] at hn
  have hnn : (0 : ℤ) ≤ (k : ℤ) + n := by omega
  have htn : ((((k : ℤ) + n).toNat : ℕ) : ℤ) = (k : ℤ) + n := Int.toNat_of_nonneg hnn
  have hcast : ((((k : ℤ) + n).toNat : ℕ) : ℝ)
      = (((((k : ℤ) + n).toNat : ℕ) : ℤ) : ℝ) := by push_cast; ring
  rw [hcast, htn]
  push_cast
  ring

/-- **The model sum, reindexed.**  Both `∑ e^{T}` over the `ℕ`-window and
`∑ e^{−an²+2Ln}` over the `ℤ`-window are the same number. -/
theorem sum_window_model_eq {W k : ℕ} (hW : W ≤ k) (a L : ℝ) :
    (∑ k' ∈ Finset.Icc (k - W) (k + W),
        Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2 + 2 * L * ((k' : ℝ) - (k : ℝ))))
      = ∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
          Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)) := by
  rw [sum_Icc_shift_int hW
    (fun j => Real.exp (-a * ((j : ℝ) - (k : ℝ)) ^ 2 + 2 * L * ((j : ℝ) - (k : ℝ))))]
  refine Finset.sum_congr rfl fun n hn => ?_
  rw [cast_toNat_shift_sub hW hn]

/-- **The assembly.**  The Kashaev window sum against the Gaussian closed form,
with every error explicit. -/
theorem abs_sum_kashaevProd_window_sub_model_le {N k W : ℕ} (hkN : k < N)
    (hW : W ≤ k) {a L B : ℝ} (ha : 0 < a)
    (hs : ∀ k' ∈ Finset.Icc (k - W) (k + W), k' < N)
    (h : ∀ k' ∈ Finset.Icc (k - W) (k + W),
      |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (-a * ((k' : ℝ) - (k : ℝ)) ^ 2 + 2 * L * ((k' : ℝ) - (k : ℝ)))| ≤ B) :
    |(∑ k' ∈ Finset.Icc (k - W) (k + W), kashaevProd N k')
        - kashaevProd N k * (Real.exp (L ^ 2 / a) * Real.sqrt (π / a))|
      ≤ kashaevProd N k
        * ((Real.exp B - 1)
             * (Real.exp (L ^ 2 / a) * Real.sqrt (π / a) + gaussWindowErr a L W)
           + gaussWindowErr a L W) := by
  have hpos := kashaevProd_pos hkN
  -- the window is nonempty, so `B` really does bound something
  have hkmem : k ∈ Finset.Icc (k - W) (k + W) := by
    rw [Finset.mem_Icc]; omega
  have hBnn : 0 ≤ B := le_trans (abs_nonneg _) (h k hkmem)
  have hexpB : (1 : ℝ) ≤ Real.exp B := Real.one_le_exp hBnn
  -- step 11: the window sum against the model sum
  have h11 := sum_kashaevProd_window_sandwich hkN (Finset.Icc (k - W) (k + W)) hs h
  -- step 14: the model sum, reindexed and evaluated
  have hre := sum_window_model_eq hW a L
  have hE : |(∑ k' ∈ Finset.Icc (k - W) (k + W),
        Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2 + 2 * L * ((k' : ℝ) - (k : ℝ))))
      - Real.exp (L ^ 2 / a) * Real.sqrt (π / a)| ≤ gaussWindowErr a L W := by
    rw [hre]
    exact abs_sum_Icc_tilted_sub_le ha W
  have hSnn : (0 : ℝ) ≤ ∑ k' ∈ Finset.Icc (k - W) (k + W),
      Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2 + 2 * L * ((k' : ℝ) - (k : ℝ))) :=
    Finset.sum_nonneg fun _ _ => (Real.exp_pos _).le
  have hEd := abs_le.mp hE
  -- `S ≤ M + E`
  have hSle : (∑ k' ∈ Finset.Icc (k - W) (k + W),
        Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2 + 2 * L * ((k' : ℝ) - (k : ℝ))))
      ≤ Real.exp (L ^ 2 / a) * Real.sqrt (π / a) + gaussWindowErr a L W := by
    linarith [hEd.2]
  -- split off the model discrepancy
  have hsplit : (∑ k' ∈ Finset.Icc (k - W) (k + W), kashaevProd N k')
        - kashaevProd N k * (Real.exp (L ^ 2 / a) * Real.sqrt (π / a))
      = ((∑ k' ∈ Finset.Icc (k - W) (k + W), kashaevProd N k')
          - kashaevProd N k * ∑ k' ∈ Finset.Icc (k - W) (k + W),
              Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2
                        + 2 * L * ((k' : ℝ) - (k : ℝ))))
        + kashaevProd N k
          * ((∑ k' ∈ Finset.Icc (k - W) (k + W),
                Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2
                          + 2 * L * ((k' : ℝ) - (k : ℝ))))
             - Real.exp (L ^ 2 / a) * Real.sqrt (π / a)) := by ring
  rw [hsplit]
  refine le_trans (abs_add_le _ _) ?_
  have hsecond : |kashaevProd N k
        * ((∑ k' ∈ Finset.Icc (k - W) (k + W),
              Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2
                        + 2 * L * ((k' : ℝ) - (k : ℝ))))
           - Real.exp (L ^ 2 / a) * Real.sqrt (π / a))|
      ≤ kashaevProd N k * gaussWindowErr a L W := by
    rw [abs_mul, abs_of_pos hpos]
    exact mul_le_mul_of_nonneg_left hE hpos.le
  -- and the first term, enlarged from `S` to `M + E`
  have hfirst : kashaevProd N k * (Real.exp B - 1)
        * (∑ k' ∈ Finset.Icc (k - W) (k + W),
            Real.exp (-a * ((k' : ℝ) - (k : ℝ)) ^ 2
                      + 2 * L * ((k' : ℝ) - (k : ℝ))))
      ≤ kashaevProd N k * (Real.exp B - 1)
        * (Real.exp (L ^ 2 / a) * Real.sqrt (π / a) + gaussWindowErr a L W) := by
    refine mul_le_mul_of_nonneg_left hSle ?_
    have : (0 : ℝ) ≤ Real.exp B - 1 := by linarith
    positivity
  linarith [h11, hsecond, hfirst]

end QOU.Knot.FigureEightVolume
