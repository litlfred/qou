/-
  Monotonicity of the Lobachevsky function `Λ`, from the sign of `Λ′`.

  WHY THIS EXISTS.  `qou-52ch` reduces `Vol(4₁) < Vol(5₂)` to a chord bound under
  Rivin concavity, and the chord's far point needs `Λ(a₁) + Λ(a₂) + Λ(a₃) ≥ 0` at
  one specific interior triple.  Using `Lob_pi_sub` to fold the obtuse angle,

      Λ(a₁) + Λ(a₂) + Λ(a₃) = (Λ(a₁) − Λ(a₁ + a₃)) + Λ(a₃),

  so the whole thing follows from `Λ` DECREASING past `π/6` together with the
  corpus's existing `Lob_nonneg_of_lt_pi_div_two`.  No value of `Λ` is needed —
  which is the point of the `qou-52ch` reduction, and would be lost if this were
  done by bounding `Λ` numerically instead.

  THE MATHLIB GAP.  Mathlib has no `Λ`; the corpus supplies it and already proves
  `Λ′(t) = −log(2 sin t)` (`QOU.Knot.Rivin.hasDerivAt_Lob`, sorry-free).  What was
  missing is the one-line consequence: `Λ′ < 0` exactly where `2 sin t > 1`, i.e.
  on `(π/6, 5π/6)`, so `Λ` is strictly decreasing there.

  Archimedean (ℝ): ordering, `sin`, `log` — §7c.

  -- Ref: [milnor1982] Hyperbolic geometry: the first 150 years
  -- Ref: [leitner2026] bean qou-52ch
-/

import QOU.Knot.RivinConcavity
import QOU.Knot.LobNearZero
import QOU.Archimedean.LobachevskyMaximum

namespace QOU.Archimedean.LobMonotonicity

open Real Set QOU.Archimedean

/-- `2 sin t > 1` on `(π/6, 5π/6)` — the exact locus where `Λ′ < 0`. -/
theorem one_lt_two_mul_sin {t : ℝ} (h0 : π / 6 < t) (h1 : t < 5 * π / 6) :
    1 < 2 * Real.sin t := by
  have hpi := Real.pi_pos
  have key : (1 : ℝ) / 2 < Real.sin t := by
    rcases le_or_gt t (π / 2) with h | h
    · -- on the rising branch: `sin` is strictly mono on `[-π/2, π/2]`
      have := Real.strictMonoOn_sin (a := π / 6) (b := t)
        ⟨by linarith, by linarith⟩ ⟨by linarith, by linarith⟩ h0
      rwa [Real.sin_pi_div_six] at this
    · -- past `π/2`, reflect: `sin t = sin (π - t)` and `π - t < 5π/6`
      have hrefl : Real.sin t = Real.sin (π - t) := (Real.sin_pi_sub t).symm
      have := Real.strictMonoOn_sin (a := π / 6) (b := π - t)
        ⟨by linarith, by linarith⟩ ⟨by linarith, by linarith⟩ (by linarith)
      rw [Real.sin_pi_div_six] at this
      linarith [hrefl ▸ this]
  linarith

/-- `Λ′(t) < 0` on `(π/6, 5π/6)`. -/
theorem deriv_Lob_neg {t : ℝ} (h0 : π / 6 < t) (h1 : t < 5 * π / 6) :
    deriv Lob t < 0 := by
  have hpi := Real.pi_pos
  have hd := QOU.Knot.Rivin.hasDerivAt_Lob (t := t) (by linarith) (by linarith)
  rw [hd.deriv]
  have := one_lt_two_mul_sin h0 h1
  have : 0 < Real.log (2 * Real.sin t) := Real.log_pos this
  linarith

/-- **`Λ` is strictly decreasing on `[π/6, 5π/6]`.**

This is the fact `qou-52ch`'s chord argument needs, and it is a statement about
the SIGN of `Λ′`, never about a value of `Λ`. -/
theorem strictAntiOn_Lob :
    StrictAntiOn Lob (Icc (π / 6) (5 * π / 6)) := by
  refine strictAntiOn_of_deriv_neg (convex_Icc _ _)
    (QOU.Knot.FigureEightVolume.continuous_Lob.continuousOn) ?_
  intro x hx
  rw [interior_Icc] at hx
  exact deriv_Lob_neg hx.1 hx.2

/-- The form the chord argument consumes: folding an obtuse angle with
`Lob_pi_sub` turns the sum into a difference, and this makes it positive. -/
theorem Lob_sub_Lob_add_pos {a c : ℝ}
    (ha : π / 6 < a) (hc : 0 < c) (hac : a + c < 5 * π / 6) :
    0 < Lob a - Lob (a + c) := by
  have hlt : Lob (a + c) < Lob a :=
    strictAntiOn_Lob ⟨le_of_lt ha, by linarith⟩
      ⟨by linarith, le_of_lt hac⟩ (by linarith)
  linarith

/-! ## Nonnegativity of the ideal-tetrahedron Λ-sum

`Λ(α) + Λ(β) + Λ(γ) ≥ 0` whenever `α, β, γ > 0` sum to `π` — i.e. an ideal
tetrahedron's volume is never negative.

The corpus did not have this.  It has `volChart_regular_pos` (one point) and the
maximum theorems; nothing bounded the functional below.  `qou-52ch`'s chord
bound needs it at the far point of the segment.

The proof is elementary rather than going through extreme points of the closed
simplex: at most one angle can exceed `π/2`, and if one does, fold it with
`Lob_pi_sub` and use that **`Λ` is concave on `[0, π/2]` with `Λ 0 = 0`, hence
subadditive there**. -/

open Real Set in
/-- `Λ(π/2) = 0`, since `Cl₂(π) = 0`. -/
theorem Lob_pi_div_two : Lob (π / 2) = 0 := by
  unfold Lob
  rw [show 2 * (π / 2) = π by ring, QOU.Archimedean.Cl_2_pi]
  norm_num

open Real Set in
/-- **`Λ` is concave on `[0, π/2]`** — from `Λ'' = −cot < 0` on the interior,
which the corpus already proves (`deriv_deriv_Lob_neg`). -/
theorem concaveOn_Lob : ConcaveOn ℝ (Icc 0 (π / 2)) Lob := by
  have hpi := Real.pi_pos
  have hint : interior (Icc (0:ℝ) (π / 2)) = Ioo 0 (π / 2) := interior_Icc
  refine concaveOn_of_deriv2_nonpos (convex_Icc _ _)
    QOU.Knot.FigureEightVolume.continuous_Lob.continuousOn ?_ ?_ ?_
  · rw [hint]
    intro x hx
    exact (QOU.Archimedean.differentiableAt_Lob hx.1
      (by linarith [hx.2])).differentiableWithinAt
  · rw [hint]
    intro x hx
    exact (QOU.Archimedean.hasDerivAt_deriv_Lob hx.1
      (by linarith [hx.2])).differentiableAt.differentiableWithinAt
  · intro x hx
    rw [hint] at hx
    simpa [Function.iterate_succ] using
      (QOU.Archimedean.deriv_deriv_Lob_neg hx.1 hx.2).le


open Real Set in
/-- **`Λ ≥ 0` on `[0, π/2]`** — a concave function vanishing at both endpoints
is nonnegative between them, and `Λ 0 = Λ(π/2) = 0`.

Derived here rather than imported: the corpus's `Lob_nonneg_of_lt_pi_div_two`
lives in `QOU.Archimedean.HyperbolicVolume` (`OrthoschemeWedgePair`), whose cone
is the orthoscheme/measure-theory development — far heavier than this one line
needs, and this version also covers the endpoint. -/
theorem Lob_nonneg_of_le_pi_div_two {x : ℝ} (hx0 : 0 ≤ x) (hx : x ≤ π / 2) :
    0 ≤ Lob x := by
  have hpi := Real.pi_pos
  have hzero : (0:ℝ) ∈ Icc (0:ℝ) (π / 2) := ⟨le_refl _, by linarith⟩
  have hhalf : (π / 2) ∈ Icc (0:ℝ) (π / 2) := ⟨by linarith, le_refl _⟩
  have hb : 0 ≤ 2 * x / π := by positivity
  have ha : 0 ≤ 1 - 2 * x / π := by
    rw [sub_nonneg, div_le_one hpi]; linarith
  have hab : (1 - 2 * x / π) + 2 * x / π = 1 := by ring
  have h := concaveOn_Lob.2 hzero hhalf ha hb hab
  have he : (1 - 2 * x / π) • (0:ℝ) + (2 * x / π) • (π / 2) = x := by
    simp only [smul_eq_mul, mul_zero, zero_add]
    field_simp
  rw [he] at h
  simpa [Lob_zero, Lob_pi_div_two, smul_eq_mul] using h

open Real Set in
/-- **`Λ` is subadditive on `[0, π/2]`**: concave with `Λ 0 = 0`. -/
theorem Lob_add_le {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b ≤ π / 2) :
    Lob (a + b) ≤ Lob a + Lob b := by
  have hpi := Real.pi_pos
  rcases eq_or_lt_of_le (by linarith : (0:ℝ) ≤ a + b) with h0 | hs
  · have ha0 : a = 0 := by linarith
    have hb0 : b = 0 := by linarith
    simp [ha0, hb0]
  have hmem : a + b ∈ Icc (0:ℝ) (π / 2) := ⟨hs.le, hab⟩
  have hzero : (0:ℝ) ∈ Icc (0:ℝ) (π / 2) := ⟨le_refl _, by linarith⟩
  have key : ∀ c : ℝ, 0 ≤ c → c ≤ a + b →
      (c / (a + b)) * Lob (a + b) ≤ Lob c := by
    intro c hc hcab
    have h1 : 0 ≤ c / (a + b) := div_nonneg hc hs.le
    have h2 : 0 ≤ 1 - c / (a + b) := by
      rw [sub_nonneg, div_le_one hs]; exact hcab
    have h3 : c / (a + b) + (1 - c / (a + b)) = 1 := by ring
    have hcc := concaveOn_Lob.2 hmem hzero h1 h2 h3
    have he : (c / (a + b)) • (a + b) + (1 - c / (a + b)) • (0:ℝ) = c := by
      simp only [smul_eq_mul, mul_zero, add_zero]
      field_simp
    rw [he] at hcc
    simpa [Lob_zero, smul_eq_mul] using hcc
  have k1 := key a ha (by linarith)
  have k2 := key b hb (by linarith)
  have hsum : (a / (a + b)) * Lob (a + b) + (b / (a + b)) * Lob (a + b)
      = Lob (a + b) := by field_simp
  linarith

open Real in
/-- **The ideal-tetrahedron Λ-sum is nonnegative.**

`α, β, γ > 0` summing to `π`.  At most one exceeds `π/2`; if one does, fold it
with `Lob_pi_sub` and apply subadditivity to the other two, whose sum is then
`≤ π/2`. -/
theorem lob_sum_nonneg {α β γ : ℝ} (ha : 0 < α) (hb : 0 < β) (hc : 0 < γ)
    (hsum : α + β + γ = π) : 0 ≤ Lob α + Lob β + Lob γ := by
  have hpi := Real.pi_pos
  have fold : ∀ x y z : ℝ, 0 < x → 0 < y → 0 < z → x + y + z = π → π / 2 < z →
      0 ≤ Lob x + Lob y + Lob z := by
    intro x y z hx hy hz hxyz hzb
    have hxy : x + y ≤ π / 2 := by linarith
    have hz' : Lob z = -Lob (x + y) := by
      have hzz : z = π - (x + y) := by linarith
      rw [hzz, QOU.Archimedean.IdealTetrahedronConcavity.Lob_pi_sub]
    rw [hz']
    have := Lob_add_le hx.le hy.le hxy
    linarith
  rcases lt_or_ge (π / 2) α with h | h
  · have := fold β γ α hb hc ha (by linarith) h; linarith
  rcases lt_or_ge (π / 2) β with h' | h'
  · have := fold α γ β ha hc hb (by linarith) h'; linarith
  rcases lt_or_ge (π / 2) γ with h'' | h''
  · exact fold α β γ ha hb hc hsum h''
  have n1 := Lob_nonneg_of_le_pi_div_two ha.le h
  have n2 := Lob_nonneg_of_le_pi_div_two hb.le h'
  have n3 := Lob_nonneg_of_le_pi_div_two hc.le h''
  linarith

end QOU.Archimedean.LobMonotonicity