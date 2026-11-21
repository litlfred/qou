/-
  **`VOL_4_1 < VOL_5_2`** — the Rivin-concavity chord bound, assembled.

  Bean `qou-52ch`.  Everything below is composition: each input is proved
  elsewhere, and this file only puts them on the same line.

  ═══ THE ARGUMENT ═══

  Along the line through the REGULAR angle triple `(π/3, π/3, π/3)` in the
  direction of the 5₂ triple, `Λ(α)+Λ(β)+Λ(γ)` is strictly concave
  (`QOU.Knot.Rivin.strictConcaveOn_tetVolLine`).  Evaluate at three points:

      t = 0   the regular tetrahedron        f(0) = 3Λ(π/3) = Cl₂(π/3)
      t = 1   the 5₂ tetrahedron             3·f(1) = VOL_5_2
      t = 3   angles 3aᵢ − 2π/3              f(3) ≥ 0

  and `1 = (2/3)·0 + (1/3)·3`, so strict concavity gives

      f(1) > (2/3)·Cl₂(π/3) + (1/3)·f(3) ≥ (2/3)·Cl₂(π/3)

  hence `VOL_5_2 = 3·f(1) > 2·Cl₂(π/3) = VOL_4_1`.

  ═══ WHY `t = 3` IS THE RIGHT FAR POINT, EXACTLY ═══

  Two constraints meet there and neither has slack:

  * the chord weight needs `3·(1 − 1/s) ≥ 2`, i.e. `s ≥ 3`;
  * membership of `s` in `tetLineDomain` needs `π/3 + s(aᵢ − π/3) > 0` for each
    `i`, and at `s = 3` that is exactly `3aᵢ > 2π/3`, i.e. **`aᵢ > 2π/9`** —
    `QOU.Knot.FiveTwoNinthPower.all_angles_gt_two_pi_div_nine`.

  So the angle theorem that arc spent its length proving is precisely the
  domain condition at the one far point the chord can use.

  Strictness is free: `StrictConcaveOn` gives `<`, so `f(3) ≥ 0` suffices and
  no positivity at the far point is needed.

  ═══ WHAT THIS IS NOT ═══

  `VOL_4_1` and `VOL_5_2` are the corpus's *defined* constants — `2·Cl₂(π/3)`
  and `3·D(y₁)`.  That they are the hyperbolic volumes of `S³ ∖ 4₁` and
  `S³ ∖ 5₂` is Thurston hyperbolisation plus Mostow rigidity, which neither
  Mathlib nor QOU has; see `IdealTriangulation`'s header.  This is an
  inequality between two real numbers, not between two manifolds.

  It does, however, replace the `norm_num`-on-truncated-decimals version that
  `MostowRigidity` used to carry — which proved nothing about the exact
  constants at all (bean `qou-f8lit`, PR #6084).

  -- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds
  -- Ref: [leitner2026] bean qou-52ch
-/

import QOU.Knot.FiveTwoNinthPower
import QOU.Knot.FiveTwoAngleSum
import QOU.Archimedean.LobMonotonicity
import QOU.Knot.RivinConcavity

namespace QOU.Knot.FiveTwoVolumeChord

open Real QOU.Archimedean QOU.Knot.FiveTwoVolume QOU.Knot.FiveTwoNinthPower

/-- Shorthand for the three dihedral angles. -/
private noncomputable def a₁ : ℝ := fiveTwoTet.angle₁
private noncomputable def a₂ : ℝ := fiveTwoTet.angle₂
private noncomputable def a₃ : ℝ := fiveTwoTet.angle₃

/-- The direction from the regular triple towards the 5₂ triple. -/
private noncomputable def u : ℝ := a₁ - π / 3
private noncomputable def v : ℝ := a₂ - π / 3
private noncomputable def w : ℝ := a₃ - π / 3

private theorem hsum3 : π / 3 + π / 3 + π / 3 = π := by ring

private theorem htan : u + v + w = 0 := by
  have := fiveTwoTet.angle_sum
  unfold u v w a₁ a₂ a₃
  linarith

private theorem hne : ¬(u = 0 ∧ v = 0) := by
  rintro ⟨hu, hv⟩
  have hw : w = 0 := by have := htan; linarith
  have h3 : a₃ = π / 3 := by unfold w at hw; linarith
  have hlt : fiveTwoTet.angle₃ < π / 4 := by
    rw [← zz_arg_eq_angle₃]; exact zz_arg_lt_pi_div_four
  have := Real.pi_pos
  unfold a₃ at h3
  linarith


/-! ### Domain membership at the two chord endpoints -/

private theorem h0mem :
    (0:ℝ) ∈ QOU.Knot.Rivin.tetLineDomain (π / 3) (π / 3) (π / 3) u v w := by
  have := Real.pi_pos
  refine ⟨by simp; linarith, by simp; linarith, by simp; linarith⟩

/-- **`3 ∈ tetLineDomain` IS the `2π/9` theorem.**  `π/3 + 3(aᵢ − π/3) > 0`
unfolds to `3aᵢ > 2π/3`, i.e. `aᵢ > 2π/9`. -/
private theorem h3mem :
    (3:ℝ) ∈ QOU.Knot.Rivin.tetLineDomain (π / 3) (π / 3) (π / 3) u v w := by
  obtain ⟨g1, g2, g3⟩ := all_angles_gt_two_pi_div_nine
  unfold QOU.Knot.Rivin.tetLineDomain u v w a₁ a₂ a₃
  refine ⟨by linarith, by linarith, by linarith⟩

/-! ### The three evaluations -/

private theorem f0 :
    QOU.Knot.Rivin.tetVolLine (π / 3) (π / 3) (π / 3) u v w 0 = Cl_2 (π / 3) := by
  unfold QOU.Knot.Rivin.tetVolLine
  simp only [zero_mul, add_zero]
  have h := QOU.Archimedean.three_Lob_pi_div_three
  unfold Lob at h ⊢
  linarith

private theorem f1 :
    3 * QOU.Knot.Rivin.tetVolLine (π / 3) (π / 3) (π / 3) u v w 1 = VOL_5_2 := by
  rw [VOL_5_2_eq_three_mul_lob_sum]
  unfold QOU.Knot.Rivin.tetVolLine u v w a₁ a₂ a₃
  norm_num

/-- `f(3) ≥ 0` — the angles there are `3aᵢ − 2π/3`, positive by the `2π/9`
theorem and summing to `π`, so `lob_sum_nonneg` applies. -/
private theorem f3nonneg :
    0 ≤ QOU.Knot.Rivin.tetVolLine (π / 3) (π / 3) (π / 3) u v w 3 := by
  obtain ⟨g1, g2, g3⟩ := all_angles_gt_two_pi_div_nine
  have hs := fiveTwoTet.angle_sum
  have e : ∀ x : ℝ, π / 3 + 3 * (x - π / 3) = 3 * x - 2 * π / 3 := by intro x; ring
  unfold QOU.Knot.Rivin.tetVolLine u v w a₁ a₂ a₃
  rw [e, e, e]
  exact QOU.Archimedean.LobMonotonicity.lob_sum_nonneg
    (by linarith) (by linarith) (by linarith) (by linarith)

/-! ### The chord -/

/-- **`VOL_4_1 < VOL_5_2`.**

Strict concavity along the line, evaluated at `1 = (2/3)·0 + (1/3)·3`. -/
theorem VOL_4_1_lt_VOL_5_2 :
    QOU.Knot.FigureEightVolume.VOL_4_1 < VOL_5_2 := by
  have hconc := QOU.Knot.Rivin.strictConcaveOn_tetVolLine
    (α := π / 3) (β := π / 3) (γ := π / 3) (u := u) (v := v) (w := w)
    hsum3 htan hne
  have hchord := hconc.2 h0mem h3mem (by norm_num)
    (by norm_num : (0:ℝ) < 2 / 3) (by norm_num : (0:ℝ) < 1 / 3) (by norm_num)
  have he : (2 / 3 : ℝ) • (0:ℝ) + (1 / 3 : ℝ) • (3:ℝ) = 1 := by norm_num
  rw [he, f0] at hchord
  have h3 := f3nonneg
  have h1 := f1
  rw [QOU.Knot.FigureEightVolume.VOL_4_1]
  simp only [smul_eq_mul] at hchord
  linarith

end QOU.Knot.FiveTwoVolumeChord
