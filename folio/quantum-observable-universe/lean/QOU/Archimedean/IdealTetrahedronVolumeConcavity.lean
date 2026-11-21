/-
  T3: the ideal-tetrahedron volume functional is STRICTLY CONCAVE on the open
  angle simplex -- and therefore has at most one maximiser.

  WHAT THIS CLOSES.  Bean `qou-idvt` tiers the ideal-tetrahedron volume gap as
  T1 (the Lobachevsky derivative) -> T2 (the geometric `Vol = Lambda`-sum) ->
  T3 (concavity), and calls T3 "THE PRIZE; T1-T2 are means".  It also records
  why T3 is reachable while T2 is not:

    "concavity of a sum of Lambda over the simplex alpha+beta+gamma = pi is a
     REAL-ANALYSIS statement, not a geometry one, and does not need any
     manifold theory."

  That is exactly what is proved here.  T1 landed in PR #4744
  (`LobachevskyDerivative.lean`: `Lambda'' = -cot`), and
  `IdealTetrahedronConcavity.lean` already had the pointwise Hessian result
  (`hessian_neg_definite`).  What was missing -- the bean calls it
  "T3-plumbing" -- is the step from a negative-definite Hessian to actual
  strict concavity.  This file supplies it.

  THE ARGUMENT.  On the chart `(alpha, beta)` with `gamma = pi - alpha - beta`,
  restrict `V` to a straight segment.  Writing `u, v` for the chart direction,
  the simplex constraint forces the `gamma` direction to be `-u - v`, so T1
  gives

      g''(s) = Lambda''(alpha) u^2 + Lambda''(beta) v^2 + Lambda''(gamma)(u+v)^2
             = -[ cot(alpha) u^2 + cot(beta) v^2 + cot(gamma) (u+v)^2 ]
             = -[ (cot a + cot c) u^2 + 2 cot(c) uv + (cot b + cot c) v^2 ]

  which is PRECISELY the quadratic form `hessian_neg_definite` already proves
  negative.  The pointwise Hessian result is reused verbatim, not redone, and
  Mathlib's `strictConcaveOn_of_deriv2_neg` turns the 1-D restriction into
  strict concavity along every segment -- which IS the definition of strict
  concavity on the simplex.

  WHY THIS IS NOT A GEOMETRIC CLAIM -- read before citing.

  * **T2 IS STILL OPEN, and this file does not touch it.**  `volChart` is
    DEFINED here as the Lambda-sum.  That the Lambda-sum IS the hyperbolic
    volume of the ideal tetrahedron is the geometric identification T2, which
    needs hyperbolic-volume theory Mathlib does not have.  Every statement
    below is a theorem about the function `Lob a + Lob b + Lob (pi - a - b)`,
    and NOTHING here licenses reading it as a statement about hyperbolic
    volume.  The name `volChart` is suggestive; the content is analytic.
  * **`qou-krvm` (iv) is NOT discharged.**  That hypothesis asks for concavity
    AND symmetry-invariance of the volume functional ON THE ANGLE-STRUCTURE
    POLYTOPE of m004 / L6a4.  Those polytopes are 3- and 11-dimensional
    (several tetrahedra glued); this is the SINGLE-tetrahedron simplex.  What
    is supplied is the tetrahedral case of the concavity half -- not the
    polytope statement, and not invariance.
  * **No mass, binding, or substrate claim.**  Nothing here is wired.

  Archimedean (ℝ): ordering, `log`, `sin`, `cos` -- §7c.

  -- Ref: [leitner2026] beans qou-idvt (T3), qou-krvm (iv)
  -- Ref: [thurston1978] Ch. 7 (the volume of an ideal simplex)
-/

import Mathlib.Analysis.Convex.Deriv
import QOU.Archimedean.LobachevskyDerivative
import QOU.Archimedean.IdealTetrahedronConcavity

namespace QOU.Archimedean.IdealTetrahedronConcavity

open QOU.Archimedean Set

/-- **The open angle simplex, in the `(alpha, beta)` chart.**
`gamma = pi - alpha - beta` is then automatically positive. -/
def angleSimplex : Set (ℝ × ℝ) :=
  {p | 0 < p.1 ∧ 0 < p.2 ∧ p.1 + p.2 < Real.pi}

/-- **The volume functional in the chart**, DEFINED as the Lobachevsky sum.

A definition, not the geometric volume: identifying it with the hyperbolic
volume of the ideal tetrahedron is `qou-idvt` T2, which is open. -/
noncomputable def volChart (p : ℝ × ℝ) : ℝ :=
  Lob p.1 + Lob p.2 + Lob (Real.pi - p.1 - p.2)

/-- A convex combination of two positives is positive.  Needs the case split:
one of the weights may vanish, so `nlinarith` alone does not see the strictness. -/
private theorem pos_combo {α β x y : ℝ} (hα : 0 ≤ α) (hβ : 0 ≤ β) (hαβ : α + β = 1)
    (hx : 0 < x) (hy : 0 < y) : 0 < α * x + β * y := by
  rcases lt_or_eq_of_le hα with hα' | hα'
  · have h1 : 0 < α * x := mul_pos hα' hx
    have h2 : 0 ≤ β * y := mul_nonneg hβ hy.le
    linarith
  · have hβ1 : β = 1 := by linarith
    have h1 : 0 ≤ α * x := mul_nonneg hα hx.le
    have h2 : 0 < β * y := by rw [hβ1, one_mul]; exact hy
    linarith

/-- A convex combination of two reals below `c` stays strictly below `c`.
Obtained from `pos_combo` applied to the slacks `c - x`, `c - y`. -/
private theorem combo_lt {α β x y c : ℝ} (hα : 0 ≤ α) (hβ : 0 ≤ β) (hαβ : α + β = 1)
    (hx : x < c) (hy : y < c) : α * x + β * y < c := by
  rcases lt_or_eq_of_le hα with hα' | hα'
  · rcases lt_or_eq_of_le hβ with hβ' | hβ'
    · have hc : α * c + β * c = c := by rw [← add_mul, hαβ, one_mul]
      have k1 : α * x < α * c := mul_lt_mul_of_pos_left hx hα'
      have k2 : β * y < β * c := mul_lt_mul_of_pos_left hy hβ'
      linarith
    · have hα1 : α = 1 := by linarith
      rw [hα1, one_mul, ← hβ', zero_mul, add_zero]; exact hx
  · have hβ1 : β = 1 := by linarith
    rw [← hα', zero_mul, hβ1, one_mul, zero_add]; exact hy

theorem angleSimplex_convex : Convex ℝ angleSimplex := by
  rintro p ⟨hp1, hp2, hp3⟩ r ⟨hr1, hr2, hr3⟩ α β hα hβ hαβ
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
  · exact pos_combo hα hβ hαβ hp1 hr1
  · exact pos_combo hα hβ hαβ hp2 hr2
  · have : α * p.1 + β * r.1 + (α * p.2 + β * r.2)
        = α * (p.1 + p.2) + β * (r.1 + r.2) := by ring
    rw [this]
    exact combo_lt hα hβ hαβ hp3 hr3

/-- A point of the simplex has all three angles in `(0, π)`. -/
theorem mem_angleSimplex_lt_pi {p : ℝ × ℝ} (hp : p ∈ angleSimplex) :
    p.1 < Real.pi ∧ p.2 < Real.pi ∧ 0 < Real.pi - p.1 - p.2 := by
  obtain ⟨h1, h2, h3⟩ := hp
  exact ⟨by linarith, by linarith, by linarith⟩

/-- The `AngleTriple` at a point of the open simplex. -/
noncomputable def AngleTriple.ofChart (p : ℝ × ℝ) (hp : p ∈ angleSimplex) : AngleTriple where
  α := p.1
  β := p.2
  γ := Real.pi - p.1 - p.2
  hα := hp.1
  hβ := hp.2.1
  hγ := (mem_angleSimplex_lt_pi hp).2.2
  sum := by ring

/-! ### The one-dimensional restriction along a segment -/

section Segment

variable (a b u v : ℝ)

/-- The parameters at which the segment's three angles are all positive.  Since
they sum to `π`, positivity of all three already forces each to be `< π`. -/
def segSet : Set ℝ :=
  {t | 0 < a + t * u ∧ 0 < b + t * v ∧ 0 < Real.pi - a - b + t * (-u - v)}

theorem segSet_isOpen : IsOpen (segSet a b u v) := by
  have h : segSet a b u v =
      ((fun t : ℝ => a + t * u) ⁻¹' Ioi 0) ∩
        (((fun t : ℝ => b + t * v) ⁻¹' Ioi 0) ∩
          ((fun t : ℝ => Real.pi - a - b + t * (-u - v)) ⁻¹' Ioi 0)) := by
    ext t; simp [segSet]
  rw [h]
  exact (isOpen_Ioi.preimage (by fun_prop)).inter
    ((isOpen_Ioi.preimage (by fun_prop)).inter (isOpen_Ioi.preimage (by fun_prop)))

/-- The volume along the segment. -/
noncomputable def volSeg (s : ℝ) : ℝ :=
  Lob (a + s * u) + Lob (b + s * v) + Lob (Real.pi - a - b + s * (-u - v))

/-- The closed form of its first derivative (`Λ' = -log(2 sin ·)`, T1). -/
noncomputable def dvolSeg (s : ℝ) : ℝ :=
  -(Real.log (2 * Real.sin (a + s * u))) * u +
    -(Real.log (2 * Real.sin (b + s * v))) * v +
      -(Real.log (2 * Real.sin (Real.pi - a - b + s * (-u - v)))) * (-u - v)

variable {a b u v}

/-- Each angle is `< π` on `segSet`, because the three sum to `π`. -/
theorem segSet_lt_pi {s : ℝ} (hs : s ∈ segSet a b u v) :
    a + s * u < Real.pi ∧ b + s * v < Real.pi ∧
      Real.pi - a - b + s * (-u - v) < Real.pi := by
  obtain ⟨h1, h2, h3⟩ := hs
  refine ⟨by nlinarith, by nlinarith, by nlinarith⟩

/-- **First derivative of the restriction.** -/
theorem hasDerivAt_volSeg {s : ℝ} (hs : s ∈ segSet a b u v) :
    HasDerivAt (volSeg a b u v) (dvolSeg a b u v s) s := by
  obtain ⟨h1, h2, h3⟩ := hs
  obtain ⟨p1, p2, p3⟩ := segSet_lt_pi (a := a) (b := b) (u := u) (v := v) ⟨h1, h2, h3⟩
  have e1 : HasDerivAt (fun t : ℝ => a + t * u) u s := by
    simpa using ((hasDerivAt_id s).mul_const u).const_add a
  have e2 : HasDerivAt (fun t : ℝ => b + t * v) v s := by
    simpa using ((hasDerivAt_id s).mul_const v).const_add b
  have e3 : HasDerivAt (fun t : ℝ => Real.pi - a - b + t * (-u - v)) (-u - v) s := by
    simpa using ((hasDerivAt_id s).mul_const (-u - v)).const_add (Real.pi - a - b)
  exact (((hasDerivAt_Lob h1 p1).comp s e1).add
    ((hasDerivAt_Lob h2 p2).comp s e2)).add ((hasDerivAt_Lob h3 p3).comp s e3)

/-- `deriv (volSeg ...)` agrees with the closed form near any good parameter. -/
theorem deriv_volSeg_eventuallyEq {s : ℝ} (hs : s ∈ segSet a b u v) :
    deriv (volSeg a b u v) =ᶠ[nhds s] dvolSeg a b u v := by
  filter_upwards [(segSet_isOpen a b u v).mem_nhds hs] with t ht
  exact (hasDerivAt_volSeg ht).deriv

/-- **Second derivative of the restriction**, via T1's `Λ'' = -cot`. -/
theorem hasDerivAt_dvolSeg {s : ℝ} (hs : s ∈ segSet a b u v) :
    HasDerivAt (dvolSeg a b u v)
      (-(Real.cos (a + s * u) / Real.sin (a + s * u)) * u * u +
        -(Real.cos (b + s * v) / Real.sin (b + s * v)) * v * v +
          -(Real.cos (Real.pi - a - b + s * (-u - v)) /
              Real.sin (Real.pi - a - b + s * (-u - v))) * (-u - v) * (-u - v)) s := by
  obtain ⟨h1, h2, h3⟩ := hs
  obtain ⟨p1, p2, p3⟩ := segSet_lt_pi (a := a) (b := b) (u := u) (v := v) ⟨h1, h2, h3⟩
  have e1 : HasDerivAt (fun t : ℝ => a + t * u) u s := by
    simpa using ((hasDerivAt_id s).mul_const u).const_add a
  have e2 : HasDerivAt (fun t : ℝ => b + t * v) v s := by
    simpa using ((hasDerivAt_id s).mul_const v).const_add b
  have e3 : HasDerivAt (fun t : ℝ => Real.pi - a - b + t * (-u - v)) (-u - v) s := by
    simpa using ((hasDerivAt_id s).mul_const (-u - v)).const_add (Real.pi - a - b)
  -- `Λ'` written as `deriv Lob`, differentiated by T1, then rewritten back
  have k1 : HasDerivAt (fun t : ℝ => -(Real.log (2 * Real.sin (a + t * u))) * u)
      (-(Real.cos (a + s * u) / Real.sin (a + s * u)) * u * u) s := by
    have base : HasDerivAt (fun t : ℝ => deriv Lob (a + t * u))
        (-(Real.cos (a + s * u) / Real.sin (a + s * u)) * u) s := by
      simpa [Function.comp] using (hasDerivAt_deriv_Lob h1 p1).comp s e1
    have heq : (fun t : ℝ => deriv Lob (a + t * u)) =ᶠ[nhds s]
        fun t : ℝ => -(Real.log (2 * Real.sin (a + t * u))) := by
      have hopen : IsOpen {t : ℝ | 0 < a + t * u ∧ a + t * u < Real.pi} := by
        have : {t : ℝ | 0 < a + t * u ∧ a + t * u < Real.pi} =
            (fun t : ℝ => a + t * u) ⁻¹' Ioo 0 Real.pi := by ext t; simp [Ioo]
        rw [this]; exact isOpen_Ioo.preimage (by fun_prop)
      filter_upwards [hopen.mem_nhds (show s ∈ _ from ⟨h1, p1⟩)] with t ht
      exact deriv_Lob ht.1 ht.2
    exact (base.congr_of_eventuallyEq heq.symm).mul_const u
  have k2 : HasDerivAt (fun t : ℝ => -(Real.log (2 * Real.sin (b + t * v))) * v)
      (-(Real.cos (b + s * v) / Real.sin (b + s * v)) * v * v) s := by
    have base : HasDerivAt (fun t : ℝ => deriv Lob (b + t * v))
        (-(Real.cos (b + s * v) / Real.sin (b + s * v)) * v) s := by
      simpa [Function.comp] using (hasDerivAt_deriv_Lob h2 p2).comp s e2
    have heq : (fun t : ℝ => deriv Lob (b + t * v)) =ᶠ[nhds s]
        fun t : ℝ => -(Real.log (2 * Real.sin (b + t * v))) := by
      have hopen : IsOpen {t : ℝ | 0 < b + t * v ∧ b + t * v < Real.pi} := by
        have : {t : ℝ | 0 < b + t * v ∧ b + t * v < Real.pi} =
            (fun t : ℝ => b + t * v) ⁻¹' Ioo 0 Real.pi := by ext t; simp [Ioo]
        rw [this]; exact isOpen_Ioo.preimage (by fun_prop)
      filter_upwards [hopen.mem_nhds (show s ∈ _ from ⟨h2, p2⟩)] with t ht
      exact deriv_Lob ht.1 ht.2
    exact (base.congr_of_eventuallyEq heq.symm).mul_const v
  have k3 : HasDerivAt
      (fun t : ℝ => -(Real.log (2 * Real.sin (Real.pi - a - b + t * (-u - v)))) * (-u - v))
      (-(Real.cos (Real.pi - a - b + s * (-u - v)) /
          Real.sin (Real.pi - a - b + s * (-u - v))) * (-u - v) * (-u - v)) s := by
    have base : HasDerivAt (fun t : ℝ => deriv Lob (Real.pi - a - b + t * (-u - v)))
        (-(Real.cos (Real.pi - a - b + s * (-u - v)) /
            Real.sin (Real.pi - a - b + s * (-u - v))) * (-u - v)) s := by
      simpa [Function.comp] using (hasDerivAt_deriv_Lob h3 p3).comp s e3
    have heq : (fun t : ℝ => deriv Lob (Real.pi - a - b + t * (-u - v))) =ᶠ[nhds s]
        fun t : ℝ => -(Real.log (2 * Real.sin (Real.pi - a - b + t * (-u - v)))) := by
      have hopen : IsOpen {t : ℝ | 0 < Real.pi - a - b + t * (-u - v) ∧
          Real.pi - a - b + t * (-u - v) < Real.pi} := by
        have : {t : ℝ | 0 < Real.pi - a - b + t * (-u - v) ∧
            Real.pi - a - b + t * (-u - v) < Real.pi} =
            (fun t : ℝ => Real.pi - a - b + t * (-u - v)) ⁻¹' Ioo 0 Real.pi := by
          ext t; simp [Ioo]
        rw [this]; exact isOpen_Ioo.preimage (by fun_prop)
      filter_upwards [hopen.mem_nhds (show s ∈ _ from ⟨h3, p3⟩)] with t ht
      exact deriv_Lob ht.1 ht.2
    exact (base.congr_of_eventuallyEq heq.symm).mul_const (-u - v)
  exact (k1.add k2).add k3

/-- **The second derivative is negative** whenever the direction is nonzero.

This is the step that reuses `hessian_neg_definite`: after `w = -u - v` is
substituted, the three `Λ''` terms ARE its quadratic form. -/
theorem deriv2_volSeg_neg {s : ℝ} (hs : s ∈ segSet a b u v) (hne : u ≠ 0 ∨ v ≠ 0) :
    deriv (deriv (volSeg a b u v)) s < 0 := by
  obtain ⟨h1, h2, h3⟩ := hs
  obtain ⟨p1, p2, p3⟩ := segSet_lt_pi (a := a) (b := b) (u := u) (v := v) ⟨h1, h2, h3⟩
  -- rewrite `deriv (volSeg …)` as the closed form near `s`, then differentiate
  have hd : HasDerivAt (deriv (volSeg a b u v))
      (-(Real.cos (a + s * u) / Real.sin (a + s * u)) * u * u +
        -(Real.cos (b + s * v) / Real.sin (b + s * v)) * v * v +
          -(Real.cos (Real.pi - a - b + s * (-u - v)) /
              Real.sin (Real.pi - a - b + s * (-u - v))) * (-u - v) * (-u - v)) s :=
    (hasDerivAt_dvolSeg ⟨h1, h2, h3⟩).congr_of_eventuallyEq
      (deriv_volSeg_eventuallyEq ⟨h1, h2, h3⟩)
  rw [hd.deriv]
  -- the triple at the segment point
  set t : AngleTriple :=
    { α := a + s * u, β := b + s * v, γ := Real.pi - a - b + s * (-u - v)
      hα := h1, hβ := h2, hγ := h3, sum := by ring } with ht
  have key := hessian_neg_definite t (x := u) (y := v) hne
  simp only [ht] at key
  nlinarith [key]

end Segment

/-! ### Strict concavity on the simplex -/

/-- **T3 — the Lobachevsky volume sum is strictly concave on the open angle
simplex.**

Proved by restricting to an arbitrary segment and applying Mathlib's
`strictConcaveOn_of_deriv2_neg` to the restriction, whose second derivative is
the `hessian_neg_definite` quadratic form. -/
theorem strictConcaveOn_volChart : StrictConcaveOn ℝ angleSimplex volChart := by
  refine ⟨angleSimplex_convex, ?_⟩
  rintro p hp r hr hpr α β hα hβ hαβ
  set u := r.1 - p.1 with hu
  set v := r.2 - p.2 with hv
  -- the segment parameters that stay in the simplex
  have hseg : ∀ s : ℝ, (0 ≤ s → s ≤ 1 → s ∈ segSet p.1 p.2 u v) := by
    intro s hs0 hs1
    have hcv := angleSimplex_convex hp hr (a := 1 - s) (b := s)
      (by linarith) hs0 (by ring)
    obtain ⟨c1, c2, c3⟩ := hcv
    simp only [Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul] at c1 c2 c3
    refine ⟨by rw [hu]; nlinarith, by rw [hv]; nlinarith, by rw [hu, hv]; nlinarith⟩
  have hne : u ≠ 0 ∨ v ≠ 0 := by
    by_contra hcon
    push_neg at hcon
    exact hpr (Prod.ext (by rw [hu] at hcon; linarith [hcon.1])
      (by rw [hv] at hcon; linarith [hcon.2]))
  -- strict concavity of the restriction on `[0,1]`
  have hconc : StrictConcaveOn ℝ (Icc (0 : ℝ) 1) (volSeg p.1 p.2 u v) := by
    refine strictConcaveOn_of_deriv2_neg (convex_Icc 0 1) ?_ ?_
    · intro s hs
      exact ((hasDerivAt_volSeg (hseg s hs.1 hs.2)).continuousAt).continuousWithinAt
    · intro s hs
      rw [interior_Icc] at hs
      have := deriv2_volSeg_neg (hseg s (le_of_lt hs.1) (le_of_lt hs.2)) hne
      simpa [Function.iterate_succ, Function.comp] using this
  -- evaluate the segment inequality at the endpoints
  have h0 : volSeg p.1 p.2 u v 0 = volChart p := by
    simp [volSeg, volChart]
  have h1 : volSeg p.1 p.2 u v 1 = volChart r := by
    simp only [volSeg, volChart, one_mul, hu, hv]
    ring_nf
  have hmix : volSeg p.1 p.2 u v β = volChart (α • p + β • r) := by
    simp only [volSeg, volChart, hu, hv, Prod.fst_add, Prod.snd_add,
      Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
    have hα' : α = 1 - β := by linarith
    rw [hα']; ring_nf
  have key := hconc.2
    (show (0 : ℝ) ∈ Icc (0 : ℝ) 1 by rw [mem_Icc]; norm_num)
    (show (1 : ℝ) ∈ Icc (0 : ℝ) 1 by rw [mem_Icc]; norm_num)
    (by norm_num) hα hβ hαβ
  simp only [smul_eq_mul, mul_zero, mul_one, zero_add] at key
  rw [h0, h1, hmix] at key
  simpa using key

/-! ### Non-vacuity

`volChart_maximiser_unique` below would hold vacuously on an empty simplex, and
`strictConcaveOn_volChart` would be content-free.  Both anchor shapes the corpus
actually uses are exhibited as genuine points, so neither is. -/

/-- The regular ideal tetrahedron `(π/3, π/3, π/3)` lies in the open simplex. -/
theorem regular_mem_angleSimplex :
    ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) ∈ angleSimplex :=
  ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩

/-- The octahedral shape `(π/2, π/4, π/4)` — the L6a4 symmetric point, and the
`q → 1` Descartes shape — lies in the open simplex. -/
theorem octahedral_mem_angleSimplex :
    ((Real.pi / 2, Real.pi / 4) : ℝ × ℝ) ∈ angleSimplex :=
  ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩

/-- **At most one maximiser.**  The immediate consequence, and the shape
`qou-krvm` needs on the polytope (there, for the polytope's own functional --
see the header: this is the single-tetrahedron simplex, not that polytope). -/
theorem volChart_maximiser_unique {x y : ℝ × ℝ}
    (hx : IsMaxOn volChart angleSimplex x) (hy : IsMaxOn volChart angleSimplex y)
    (hxs : x ∈ angleSimplex) (hys : y ∈ angleSimplex) : x = y :=
  strictConcaveOn_volChart.eq_of_isMaxOn hx hy hxs hys

end QOU.Archimedean.IdealTetrahedronConcavity
