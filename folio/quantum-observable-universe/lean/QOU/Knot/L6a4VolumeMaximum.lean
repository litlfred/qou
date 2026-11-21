import QOU.Knot.RivinConcavity
import QOU.Knot.L6a4AngleStructure
import QOU.MathlibExt.ConcaveOnSum
import Mathlib.Analysis.Convex.Deriv

/-!
# QOU.Knot.L6a4VolumeMaximum — the regular octahedron point maximises the L6a4 volume

Bean `qou-krvm` (iv), L6a4 half.

`L6a4AngleStructure` proves the L6a4 (Borromean rings) angle polytope has exactly
one symmetric point, `regularOctahedron` (`1/4` on the 16-orbit, `1/2` on the
8-orbit, in π-units). This file proves that point is the **unique maximiser** of
the Lobachevsky volume functional on the open polytope.

Unlike m004 (`M004VolumeMaximum`) this does **not** follow tetrahedron by
tetrahedron: each tetrahedron sits at `(π/4, π/4, π/2)`, which is not the
single-tetrahedron maximum `(π/3, π/3, π/3)`. The gluing equations are used.

## The argument

1. Along the segment from the octahedron point `p` to any feasible `x`, the
   volume is a sum of eight one-variable functions `tetVolLine`, each concave
   (`RivinConcavity.strictConcaveOn_tetVolLine`, or constant when that
   tetrahedron does not move).
2. Its derivative at `p` is `Σ_j −log(2 sin(π p_j))·π(x_j − p_j)`. At `p` the
   gradient is `−½·log 2` on the 16-orbit and `−log 2` on the 8-orbit, which is
   `−(π log 2 / 2)·(tetrahedron sums) − (π log 2 / 4)·(the four 4-term edge
   equations)` — a combination of the gluing equations, so the derivative is
   **zero** on every feasible direction. That is the first-order condition, and
   it is exactly where the gluing equations enter.
3. A concave function on `[0,1]` with zero derivative at `0` has
   `g(1) ≤ g(0)` (`ConcaveOn.slope_le_deriv`); strictly, when some tetrahedron
   moves (`StrictConcaveOn.slope_lt_deriv`).

**What this is not.** `vol` is DEFINED as the Lobachevsky sum; identifying it with
the hyperbolic volume is `qou-idvt` T2, open. The maximum value `8·(2Λ(π/4)+Λ(π/2))`
is not evaluated here.

Archimedean (ℝ).

-- Ref: [rivin1994] https://doi.org/10.2307/2118572 (volume maximisation on the
--      angle-structure polytope)
-/

namespace QOU.Knot.L6a4VolumeMaximum

open Real Set QOU.Knot.Rivin QOU.Knot.L6a4AngleStructure

/-- Strict positivity of the 24 L6a4 angles — the open polytope. -/
def Positive (x : Pt) : Prop := ∀ i < 24, 0 < x i

/-- The Lobachevsky sum of tetrahedron `t` (angles `3t, 3t+1, 3t+2`, π-units). -/
noncomputable def tetTerm (x : Pt) (t : Fin 8) : ℝ :=
  QOU.Archimedean.Lob (π * x (3 * t.val)) + QOU.Archimedean.Lob (π * x (3 * t.val + 1))
    + QOU.Archimedean.Lob (π * x (3 * t.val + 2))

/-- The L6a4 volume functional: the sum over the eight tetrahedra. -/
noncomputable def vol (x : Pt) : ℝ := ∑ t, tetTerm x t

/-- Tetrahedron `t`'s piece of the segment from `p` to `x`. -/
noncomputable def lineTerm (p x : Pt) (t : Fin 8) (s : ℝ) : ℝ :=
  tetVolLine (π * p (3 * t.val)) (π * p (3 * t.val + 1)) (π * p (3 * t.val + 2))
    (π * (x (3 * t.val) - p (3 * t.val))) (π * (x (3 * t.val + 1) - p (3 * t.val + 1)))
    (π * (x (3 * t.val + 2) - p (3 * t.val + 2))) s

/-- The volume along the segment. -/
noncomputable def line (p x : Pt) (s : ℝ) : ℝ := ∑ t, lineTerm p x t s

theorem line_zero (p x : Pt) : line p x 0 = vol p := by
  simp [line, lineTerm, tetVolLine, vol, tetTerm]

theorem line_one (p x : Pt) : line p x 1 = vol x := by
  have e : ∀ a b : ℝ, π * a + 1 * (π * (b - a)) = π * b := fun a b => by ring
  simp only [line, lineTerm, tetVolLine, vol, tetTerm, e]

/-- Per-tetrahedron sums, for any feasible point. -/
theorem tet_sum {x : Pt} (h : GA x) (t : Fin 8) :
    x (3 * t.val) + x (3 * t.val + 1) + x (3 * t.val + 2) = 1 := by
  fin_cases t
  · exact h.tet0
  · exact h.tet1
  · exact h.tet2
  · exact h.tet3
  · exact h.tet4
  · exact h.tet5
  · exact h.tet6
  · exact h.tet7

private theorem pos_on_segment {a u s : ℝ} (ha : 0 < a) (hb : 0 < a + u)
    (hs : s ∈ Icc (0 : ℝ) 1) : 0 < a + s * u := by
  obtain ⟨h0, h1⟩ := hs
  rcases eq_or_lt_of_le h0 with h | h
  · subst h; simpa using ha
  · have e : a + s * u = (1 - s) * a + s * (a + u) := by ring
    rw [e]
    have := mul_nonneg (sub_nonneg.2 h1) ha.le
    have := mul_pos h hb
    linarith

theorem segment_subset {p x : Pt} (hp : Positive p) (hx : Positive x) (t : Fin 8) :
    Icc (0 : ℝ) 1 ⊆ tetLineDomain (π * p (3 * t.val)) (π * p (3 * t.val + 1))
      (π * p (3 * t.val + 2)) (π * (x (3 * t.val) - p (3 * t.val)))
      (π * (x (3 * t.val + 1) - p (3 * t.val + 1)))
      (π * (x (3 * t.val + 2) - p (3 * t.val + 2))) := by
  have ht := t.isLt
  intro s hs
  have key : ∀ k, k < 3 → 0 < π * p (3 * t.val + k) + s * (π * (x (3 * t.val + k)
      - p (3 * t.val + k))) := by
    intro k hk
    refine pos_on_segment (mul_pos pi_pos (hp _ (by omega))) ?_ hs
    have : π * p (3 * t.val + k) + π * (x (3 * t.val + k) - p (3 * t.val + k))
        = π * x (3 * t.val + k) := by ring
    rw [this]; exact mul_pos pi_pos (hx _ (by omega))
  exact ⟨by simpa using key 0 (by norm_num), key 1 (by norm_num), key 2 (by norm_num)⟩

theorem lineTerm_sum {p : Pt} (hp : GA p) (t : Fin 8) :
    π * p (3 * t.val) + π * p (3 * t.val + 1) + π * p (3 * t.val + 2) = π := by
  have := tet_sum hp t; linear_combination π * this

theorem lineTerm_tan {p x : Pt} (hp : GA p) (hx : GA x) (t : Fin 8) :
    π * (x (3 * t.val) - p (3 * t.val)) + π * (x (3 * t.val + 1) - p (3 * t.val + 1))
      + π * (x (3 * t.val + 2) - p (3 * t.val + 2)) = 0 := by
  have h1 := tet_sum hx t; have h2 := tet_sum hp t
  linear_combination π * h1 - π * h2

/-- Each tetrahedron's piece is concave on the segment. -/
theorem lineTerm_concaveOn {p x : Pt} (hp : GA p) (hx : GA x) (hp' : Positive p)
    (hx' : Positive x) (t : Fin 8) : ConcaveOn ℝ (Icc 0 1) (lineTerm p x t) := by
  by_cases h : π * (x (3 * t.val) - p (3 * t.val)) = 0
      ∧ π * (x (3 * t.val + 1) - p (3 * t.val + 1)) = 0
  · have htan := lineTerm_tan hp hx t
    have hw : π * (x (3 * t.val + 2) - p (3 * t.val + 2)) = 0 := by linarith [h.1, h.2]
    have hc : lineTerm p x t = fun _ => lineTerm p x t 0 := by
      funext s
      simp only [lineTerm, tetVolLine, h.1, h.2, hw, mul_zero]
    rw [hc]; exact concaveOn_const _ (convex_Icc 0 1)
  · exact ((strictConcaveOn_tetVolLine (lineTerm_sum hp t) (lineTerm_tan hp hx t) h).subset
      (segment_subset hp' hx' t) (convex_Icc 0 1)).concaveOn

/-- Derivative of the segment volume at `s = 0`. -/
theorem hasDerivAt_line {p x : Pt} (hp : GA p) (hx : GA x) (hp' : Positive p)
    (hx' : Positive x) :
    HasDerivAt (line p x) (∑ t : Fin 8,
      (-Real.log (2 * Real.sin (π * p (3 * t.val))) * (π * (x (3 * t.val) - p (3 * t.val)))
      + -Real.log (2 * Real.sin (π * p (3 * t.val + 1)))
          * (π * (x (3 * t.val + 1) - p (3 * t.val + 1)))
      + -Real.log (2 * Real.sin (π * p (3 * t.val + 2)))
          * (π * (x (3 * t.val + 2) - p (3 * t.val + 2))))) 0 := by
  have : line p x = ∑ t : Fin 8, lineTerm p x t := by
    funext s; simp [line]
  rw [this]
  refine HasDerivAt.sum fun t _ => ?_
  have h0 : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  have := hasDerivAt_tetVolLine (lineTerm_sum hp t) (lineTerm_tan hp hx t)
    (segment_subset hp' hx' t h0)
  simpa [lineTerm] using this

theorem log_two_sin_quarter : Real.log (2 * Real.sin (π * (1 / 4))) = Real.log 2 / 2 := by
  rw [show π * (1 / 4) = π / 4 by ring, Real.sin_pi_div_four,
    show 2 * (√2 / 2) = √2 by ring, Real.log_sqrt (by norm_num)]

theorem log_two_sin_half : Real.log (2 * Real.sin (π * (1 / 2))) = Real.log 2 := by
  rw [show π * (1 / 2) = π / 2 by ring, Real.sin_pi_div_two, mul_one]

/-- **First-order condition.** At the octahedron point the derivative along every
feasible direction vanishes — a linear combination of the gluing equations. -/
theorem deriv_line_zero {x : Pt} (hx : GA x) (hx' : Positive x) :
    HasDerivAt (line regularOctahedron x) 0 0 := by
  have hp := GA_regularOctahedron
  have hp' : Positive regularOctahedron := by
    intro i _; unfold regularOctahedron; split_ifs <;> norm_num
  have h := hasDerivAt_line hp hx hp' hx'
  convert h using 1
  simp only [Fin.sum_univ_eight, Fin.val_zero, Fin.val_one, Fin.val_two]
  norm_num [regularOctahedron, log_two_sin_quarter, log_two_sin_half]
  linear_combination
    (π * Real.log 2 / 2) * (hx.tet0 + hx.tet1 + hx.tet2 + hx.tet3 + hx.tet4 + hx.tet5
      + hx.tet6 + hx.tet7) + (π * Real.log 2 / 4) * (hx.edge1 + hx.edge2 + hx.edge5 + hx.edge6)

/-- **Existence: the octahedron point maximises the L6a4 volume** on the open
polytope. -/
theorem vol_le_regularOctahedron {x : Pt} (hx : GA x) (hx' : Positive x) :
    vol x ≤ vol regularOctahedron := by
  have hp := GA_regularOctahedron
  have hp' : Positive regularOctahedron := by
    intro i _; unfold regularOctahedron; split_ifs <;> norm_num
  have hcon : ConcaveOn ℝ (Icc 0 1) (line regularOctahedron x) := by
    have := QOU.MathlibExt.ConcaveOn.sum Finset.univ (convex_Icc (0:ℝ) 1)
      (fun t _ => lineTerm_concaveOn hp hx hp' hx' t)
    simpa [line] using this
  have hd := deriv_line_zero hx hx'
  have hsl := hcon.slope_le_deriv ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one
    hd.differentiableAt
  rw [hd.deriv, slope_def_field] at hsl
  rw [← line_one regularOctahedron x, ← line_zero regularOctahedron x]
  linarith [hsl]

/-- **Uniqueness: any feasible point that moves some tetrahedron has strictly smaller
volume.** "Moves tetrahedron `t`" is stated on its first two angles; the third is
then forced by the tetrahedron sum. -/
theorem vol_lt_regularOctahedron {x : Pt} (hx : GA x) (hx' : Positive x) (t : Fin 8)
    (ht : x (3 * t.val) ≠ regularOctahedron (3 * t.val)
      ∨ x (3 * t.val + 1) ≠ regularOctahedron (3 * t.val + 1)) :
    vol x < vol regularOctahedron := by
  classical
  have hp := GA_regularOctahedron
  have hp' : Positive regularOctahedron := by
    intro i _; unfold regularOctahedron; split_ifs <;> norm_num
  have hne : ¬(π * (x (3 * t.val) - regularOctahedron (3 * t.val)) = 0
      ∧ π * (x (3 * t.val + 1) - regularOctahedron (3 * t.val + 1)) = 0) := by
    rintro ⟨h1, h2⟩
    rcases mul_eq_zero.1 h1 with h | h
    · exact pi_ne_zero h
    rcases mul_eq_zero.1 h2 with h' | h'
    · exact pi_ne_zero h'
    rcases ht with ht | ht
    · exact ht (sub_eq_zero.1 h)
    · exact ht (sub_eq_zero.1 h')
  have hstrict : StrictConcaveOn ℝ (Icc 0 1) (line regularOctahedron x) := by
    have := QOU.MathlibExt.StrictConcaveOn.sum_of_mem (Finset.mem_univ t)
      (convex_Icc (0:ℝ) 1)
      ((strictConcaveOn_tetVolLine (lineTerm_sum hp t) (lineTerm_tan hp hx t) hne).subset
        (segment_subset hp' hx' t) (convex_Icc 0 1))
      (fun i _ _ => lineTerm_concaveOn hp hx hp' hx' i)
    simpa [line, lineTerm] using this
  have hd := deriv_line_zero hx hx'
  have hsl := hstrict.slope_lt_deriv ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one
    hd.differentiableAt
  rw [hd.deriv, slope_def_field] at hsl
  rw [← line_one regularOctahedron x, ← line_zero regularOctahedron x]
  linarith [hsl]

end QOU.Knot.L6a4VolumeMaximum
