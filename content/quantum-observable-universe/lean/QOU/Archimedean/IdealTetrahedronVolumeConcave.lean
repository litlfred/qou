/-
  T3-plumbing: the ideal-tetrahedron volume is STRICTLY CONCAVE on the angle
  simplex.  Bean `qou-idvt` T3-plumbing — the piece that turns the already-proved
  negative-definite Hessian (`IdealTetrahedronConcavity.hessian_neg_definite`)
  into the concavity statement that `qou-krvm` (iv) actually asks for.

  WHAT WAS ALREADY DONE, AND WHAT THIS ADDS.

  * `IdealTetrahedronConcavity` (T3-core) proved the 2x2 cotangent Hessian of the
    volume sum is negative definite at every interior point of the simplex — as a
    statement about a matrix of cotangents, deliberately NOT about a function.
  * `LobachevskyDerivative` (T1) proved `Λ'(t) = -log(2 sin t)` and
    `Λ''(t) = -cot t` on `(0, π)`.
  * This file (T3-plumbing) runs the multivariable second-derivative test: the
    Lobachevsky volume `V(α, β) = Λ(α) + Λ(β) + Λ(π-α-β)` is `StrictConcaveOn` the
    open angle simplex `{α > 0, β > 0, α + β < π}`.

  THE ARGUMENT.  There is no multivariable Hessian-test lemma in Mathlib, so the
  concavity is reduced to lines.  Fix a base point `x` and direction `v = y - x`,
  and restrict:

      g(s) = V(x + s·v) = Λ(A s) + Λ(B s) + Λ(C s),
        A s = x₁ + s·v₁,  B s = x₂ + s·v₂,  C s = π - A s - B s.

  Differentiating twice through `Λ'' = -cot`,

      g''(s) = -v₁²·cot(A s) - v₂²·cot(B s) - (v₁+v₂)²·cot(C s),

  which is EXACTLY the negative-definite Hessian quadratic form of
  `hessian_neg_definite` evaluated in the direction `(v₁, v₂)` — an algebraic
  identity, checked by `nlinarith`/`ring`, once
  `(v₁+v₂)²·cot γ = v₁²·cot γ + 2 v₁v₂·cot γ + v₂²·cot γ` is expanded.  So `g''< 0`
  whenever `v ≠ 0`, `g` is strictly concave on `[0,1]` by
  `strictConcaveOn_of_deriv2_neg`, and unpacking that at the endpoints `0, 1`
  gives the defining inequality of `StrictConcaveOn ℝ simplex V`.

  WHAT IS PROVED, AND WHAT IS NOT.

  * PROVED, sorry-free: `tetVol_strictConcaveOn` — the volume sum `V` is strictly
    concave on the open simplex.  Symmetry-invariance (permuting equal angles)
    is immediate: `V` is a symmetric function of `(α, β, γ)`, so any coordinate
    permutation preserving the simplex fixes `V` (`tetVol_symm₁₂` records the
    `α ↔ β` swap; the full `S₃` action follows the same way).  Together these are
    the two properties `qou-krvm` (iv) requires of the volume functional — for
    the tetrahedral case.
  * NOT PROVED, and NOT claimed: T2 — that this `Λ`-sum IS the hyperbolic volume
    of the ideal simplex.  That is a geometric identification (Mostow / the
    Lobachevsky volume formula), not an analytic one, and nothing here supplies
    it.  So this does not by itself close `qou-krvm` (iv); it removes the
    analytic obstruction (concavity + invariance of the sum), leaving only the
    geometric identification T2.

  Archimedean (ℝ): `Λ`, `sin`, `cos`, ordering, second derivatives — §7c.

  -- Ref: [rivin1994] https://doi.org/10.2307/2118572 (strict concavity of the
  --      hyperbolic volume on the angle-structure polytope — qou-krvm (iv))
  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  --      (Lobachevsky function Λ and the ideal-simplex volume Λ(α)+Λ(β)+Λ(γ))
  -- Ref: [thurston1978] Ch. 7 (ideal-simplex volume, Lobachevsky function)
  -- Ref: [manuscript] beans qou-idvt (T3-plumbing), qou-krvm (iv)
-/

import Mathlib.Tactic
import Mathlib.Analysis.Calculus.MeanValue
import QOU.Archimedean.LobachevskyDerivative
import QOU.Archimedean.IdealTetrahedronConcavity

namespace QOU.Archimedean

open Real Set
open QOU.Archimedean.IdealTetrahedronConcavity

/-- The Lobachevsky volume of the ideal tetrahedron with angle coordinates
`(p.1, p.2)` (third angle `π - p.1 - p.2`): `V(α,β) = Λ(α) + Λ(β) + Λ(π-α-β)`. -/
noncomputable def tetVol (p : ℝ × ℝ) : ℝ :=
  Lob p.1 + Lob p.2 + Lob (Real.pi - p.1 - p.2)

/-- The open angle simplex `{α > 0, β > 0, α + β < π}` — the interior of the
Casson–Rivin angle-structure polytope for the single ideal tetrahedron. -/
def tetSimplex : Set (ℝ × ℝ) :=
  {p | 0 < p.1 ∧ 0 < p.2 ∧ p.1 + p.2 < Real.pi}

/-- `V` is symmetric under the `α ↔ β` swap.  With the third angle
`γ = π - α - β` also symmetric, this is one generator of the `S₃` symmetry of the
volume; the volume is invariant under every angle permutation. -/
theorem tetVol_symm₁₂ (p : ℝ × ℝ) : tetVol (p.2, p.1) = tetVol p := by
  simp only [tetVol]
  ring_nf

/-- The simplex is convex (a finite intersection of open half-planes). -/
theorem convex_tetSimplex : Convex ℝ tetSimplex := by
  have h1 : Convex ℝ {p : ℝ × ℝ | 0 < p.1} := by
    simpa using (convex_halfSpace_gt (LinearMap.fst ℝ ℝ ℝ) 0)
  have h2 : Convex ℝ {p : ℝ × ℝ | 0 < p.2} := by
    simpa using (convex_halfSpace_gt (LinearMap.snd ℝ ℝ ℝ) 0)
  have h3 : Convex ℝ {p : ℝ × ℝ | p.1 + p.2 < Real.pi} := by
    simpa using
      (convex_halfSpace_lt (LinearMap.fst ℝ ℝ ℝ + LinearMap.snd ℝ ℝ ℝ) Real.pi)
  have hset : tetSimplex = {p : ℝ × ℝ | 0 < p.1} ∩ {p : ℝ × ℝ | 0 < p.2} ∩
      {p : ℝ × ℝ | p.1 + p.2 < Real.pi} := by
    ext p; simp only [tetSimplex, Set.mem_setOf_eq, Set.mem_inter_iff]; tauto
  rw [hset]
  exact (h1.inter h2).inter h3

/-! ## The line restriction and its second derivative -/

/-- The three angle coordinates along the line `s ↦ (x₁ + s v₁, x₂ + s v₂)` all
lie in `(0, π)` — the good set on which `g = V ∘ line` is twice differentiable. -/
def lineGood (x1 x2 v1 v2 : ℝ) (s : ℝ) : Prop :=
  0 < x1 + s * v1 ∧ x1 + s * v1 < Real.pi ∧
  0 < x2 + s * v2 ∧ x2 + s * v2 < Real.pi ∧
  0 < Real.pi - (x1 + s * v1) - (x2 + s * v2) ∧
    Real.pi - (x1 + s * v1) - (x2 + s * v2) < Real.pi

theorem isOpen_lineGood (x1 x2 v1 v2 : ℝ) :
    IsOpen {s : ℝ | lineGood x1 x2 v1 v2 s} := by
  have cA : Continuous fun s : ℝ => x1 + s * v1 := by fun_prop
  have cB : Continuous fun s : ℝ => x2 + s * v2 := by fun_prop
  have cC : Continuous fun s : ℝ => Real.pi - (x1 + s * v1) - (x2 + s * v2) := by
    fun_prop
  have hset : {s : ℝ | lineGood x1 x2 v1 v2 s} =
      (fun s => x1 + s * v1) ⁻¹' Ioo 0 Real.pi ∩
      (fun s => x2 + s * v2) ⁻¹' Ioo 0 Real.pi ∩
      (fun s => Real.pi - (x1 + s * v1) - (x2 + s * v2)) ⁻¹' Ioo 0 Real.pi := by
    ext s
    simp only [lineGood, Set.mem_setOf_eq, Set.mem_inter_iff, Set.mem_preimage,
      Set.mem_Ioo]
    tauto
  rw [hset]
  exact ((cA.isOpen_preimage _ isOpen_Ioo).inter
    (cB.isOpen_preimage _ isOpen_Ioo)).inter (cC.isOpen_preimage _ isOpen_Ioo)

/-- The restriction `g(s) = Λ(A s) + Λ(B s) + Λ(C s)` along the line. -/
noncomputable def lineVol (x1 x2 v1 v2 : ℝ) (s : ℝ) : ℝ :=
  Lob (x1 + s * v1) + Lob (x2 + s * v2)
    + Lob (Real.pi - (x1 + s * v1) - (x2 + s * v2))

/-- First derivative of the line restriction on the good set. -/
theorem hasDerivAt_lineVol {x1 x2 v1 v2 : ℝ} {s : ℝ}
    (hs : lineGood x1 x2 v1 v2 s) :
    HasDerivAt (lineVol x1 x2 v1 v2)
      ((-Real.log (2 * Real.sin (x1 + s * v1))) * v1
        + (-Real.log (2 * Real.sin (x2 + s * v2))) * v2
        + (-Real.log (2 * Real.sin (Real.pi - (x1 + s * v1) - (x2 + s * v2))))
            * (-(v1 + v2))) s := by
  obtain ⟨hA0, hAπ, hB0, hBπ, hC0, hCπ⟩ := hs
  have hA : HasDerivAt (fun s : ℝ => x1 + s * v1) v1 s := by
    simpa using ((hasDerivAt_id s).mul_const v1).const_add x1
  have hB : HasDerivAt (fun s : ℝ => x2 + s * v2) v2 s := by
    simpa using ((hasDerivAt_id s).mul_const v2).const_add x2
  have hC : HasDerivAt (fun s : ℝ => Real.pi - (x1 + s * v1) - (x2 + s * v2))
      (-(v1 + v2)) s := by
    have := ((hasDerivAt_const s Real.pi).sub hA).sub hB
    simpa using this
  have LA := (hasDerivAt_Lob hA0 hAπ).comp s hA
  have LB := (hasDerivAt_Lob hB0 hBπ).comp s hB
  have LC := (hasDerivAt_Lob hC0 hCπ).comp s hC
  exact (LA.add LB).add LC

/-- Second derivative of the line restriction on the good set — the
negative-definite Hessian quadratic form in the direction `(v₁, v₂)`. -/
theorem hasDerivAt_deriv_lineVol {x1 x2 v1 v2 : ℝ} {s : ℝ}
    (hs : lineGood x1 x2 v1 v2 s) :
    HasDerivAt (deriv (lineVol x1 x2 v1 v2))
      ((-(Real.cos (x1 + s * v1) / Real.sin (x1 + s * v1)) * v1) * v1
        + (-(Real.cos (x2 + s * v2) / Real.sin (x2 + s * v2)) * v2) * v2
        + (-(Real.cos (Real.pi - (x1 + s * v1) - (x2 + s * v2))
              / Real.sin (Real.pi - (x1 + s * v1) - (x2 + s * v2))) * (-(v1 + v2)))
            * (-(v1 + v2))) s := by
  have hEq : Set.EqOn (deriv (lineVol x1 x2 v1 v2))
      (fun s => (-Real.log (2 * Real.sin (x1 + s * v1))) * v1
        + (-Real.log (2 * Real.sin (x2 + s * v2))) * v2
        + (-Real.log (2 * Real.sin (Real.pi - (x1 + s * v1) - (x2 + s * v2))))
            * (-(v1 + v2)))
      {s : ℝ | lineGood x1 x2 v1 v2 s} := by
    intro s' hs'
    exact (hasDerivAt_lineVol hs').deriv
  obtain ⟨hA0, hAπ, hB0, hBπ, hC0, hCπ⟩ := hs
  have hA : HasDerivAt (fun s : ℝ => x1 + s * v1) v1 s := by
    simpa using ((hasDerivAt_id s).mul_const v1).const_add x1
  have hB : HasDerivAt (fun s : ℝ => x2 + s * v2) v2 s := by
    simpa using ((hasDerivAt_id s).mul_const v2).const_add x2
  have hC : HasDerivAt (fun s : ℝ => Real.pi - (x1 + s * v1) - (x2 + s * v2))
      (-(v1 + v2)) s := by
    have := ((hasDerivAt_const s Real.pi).sub hA).sub hB
    simpa using this
  have DA := ((hasDerivAt_neg_log_two_sin hA0 hAπ).comp s hA).mul_const v1
  have DB := ((hasDerivAt_neg_log_two_sin hB0 hBπ).comp s hB).mul_const v2
  have DC := ((hasDerivAt_neg_log_two_sin hC0 hCπ).comp s hC).mul_const (-(v1 + v2))
  have hsum := (DA.add DB).add DC
  refine hsum.congr_of_eventuallyEq ?_
  exact Filter.eventuallyEq_of_mem
    ((isOpen_lineGood x1 x2 v1 v2).mem_nhds hs) hEq.symm

/-- `deriv (deriv (lineVol …)) s` equals the Hessian quadratic form at direction
`(v₁, v₂)`, and is `< 0` whenever `(v₁, v₂) ≠ 0`. -/
theorem deriv2_lineVol_neg {x1 x2 v1 v2 : ℝ} {s : ℝ}
    (hs : lineGood x1 x2 v1 v2 s) (hv : v1 ≠ 0 ∨ v2 ≠ 0) :
    deriv (deriv (lineVol x1 x2 v1 v2)) s < 0 := by
  obtain ⟨hA0, hAπ, hB0, hBπ, hC0, hCπ⟩ := hs
  -- angle triple at this point of the line
  set α := x1 + s * v1 with hαdef
  set β := x2 + s * v2 with hβdef
  set γ := Real.pi - (x1 + s * v1) - (x2 + s * v2) with hγdef
  have hsum : α + β + γ = Real.pi := by rw [hαdef, hβdef, hγdef]; ring
  let t : AngleTriple := ⟨α, β, γ, hA0, hB0, hC0, hsum⟩
  -- the Hessian form at (v1, v2) is negative
  have hneg := hessian_neg_definite t (x := v1) (y := v2) hv
  -- deriv2 value from `hasDerivAt_deriv_lineVol`
  have hval := (hasDerivAt_deriv_lineVol hs).deriv
  rw [hval]
  -- match the computed second derivative to the Hessian form and conclude
  have ca : t.α = α := rfl
  have cb : t.β = β := rfl
  have cg : t.γ = γ := rfl
  set A := Real.cos α / Real.sin α with hA
  set B := Real.cos β / Real.sin β with hB
  set C := Real.cos γ / Real.sin γ with hC
  -- `hneg` is the Hessian form; rewrite it into the second-derivative shape
  have : (-(A) * v1) * v1 + (-(B) * v2) * v2 + (-(C) * (-(v1 + v2))) * (-(v1 + v2))
      = (-(A + C)) * v1 ^ 2 + 2 * (-(C)) * v1 * v2 + (-(B + C)) * v2 ^ 2 := by
    ring
  rw [this]
  simpa [ca, cb, cg, hA, hB, hC] using hneg

/-- The line restriction is strictly concave on `[0,1]`, provided the whole
segment `s ↦ (x₁+s v₁, x₂+s v₂)` for `s ∈ [0,1]` stays in the good set and the
direction is nonzero. -/
theorem lineVol_strictConcaveOn {x1 x2 v1 v2 : ℝ}
    (hgood : ∀ s ∈ Icc (0 : ℝ) 1, lineGood x1 x2 v1 v2 s)
    (hv : v1 ≠ 0 ∨ v2 ≠ 0) :
    StrictConcaveOn ℝ (Icc (0 : ℝ) 1) (lineVol x1 x2 v1 v2) := by
  refine strictConcaveOn_of_deriv2_neg (convex_Icc 0 1) ?_ ?_
  · -- continuity on [0,1]: differentiable there
    intro s hs
    exact (hasDerivAt_lineVol (hgood s hs)).continuousAt.continuousWithinAt
  · -- second derivative negative on the interior (0,1)
    intro s hs
    rw [interior_Icc] at hs
    have hsg : lineGood x1 x2 v1 v2 s := hgood s (Ioo_subset_Icc_self hs)
    simpa using deriv2_lineVol_neg hsg hv

/-! ## Strict concavity of the volume on the simplex -/

/-- **The Lobachevsky ideal-tetrahedron volume is strictly concave on the open
angle simplex.**  This is the analytic content of `qou-krvm` hypothesis (iv) for
the single-tetrahedron case: the volume functional is strictly concave, hence has
a unique maximiser, on the angle-structure polytope.  Symmetry-invariance is
`tetVol_symm₁₂` (and its `S₃` companions). -/
theorem tetVol_strictConcaveOn : StrictConcaveOn ℝ tetSimplex tetVol := by
  refine ⟨convex_tetSimplex, ?_⟩
  intro x hx y hy hxy a b ha hb hab
  -- direction and base coordinates
  set v1 := y.1 - x.1 with hv1
  set v2 := y.2 - x.2 with hv2
  -- the segment stays in the simplex, hence in the good set, for s ∈ [0,1]
  have hseg : ∀ s ∈ Icc (0 : ℝ) 1, lineGood x.1 x.2 v1 v2 s := by
    intro s hs
    have hs0 : (0 : ℝ) ≤ s := hs.1
    have hs1 : s ≤ 1 := hs.2
    -- (1-s)•x + s•y ∈ tetSimplex by convexity
    have hmem : ((1 - s) • x + s • y) ∈ tetSimplex :=
      convex_tetSimplex hx hy (by linarith) hs0 (by ring)
    -- coordinates of the convex combination equal the affine line
    have e1 : ((1 - s) • x + s • y).1 = x.1 + s * v1 := by
      simp only [Prod.fst_add, Prod.smul_fst, smul_eq_mul, hv1]; ring
    have e2 : ((1 - s) • x + s • y).2 = x.2 + s * v2 := by
      simp only [Prod.snd_add, Prod.smul_snd, smul_eq_mul, hv2]; ring
    obtain ⟨hp1, hp2, hp3⟩ := hmem
    rw [e1] at hp1; rw [e2] at hp2; rw [e1, e2] at hp3
    -- assemble lineGood
    refine ⟨hp1, ?_, hp2, ?_, ?_, ?_⟩
    · linarith
    · linarith
    · linarith
    · have : (0 : ℝ) < x.1 + s * v1 := hp1
      linarith
  -- direction nonzero since x ≠ y
  have hvne : v1 ≠ 0 ∨ v2 ≠ 0 := by
    by_contra h
    push_neg at h
    obtain ⟨h1, h2⟩ := h
    apply hxy
    have hx1 : y.1 = x.1 := by rw [hv1] at h1; linarith
    have hx2 : y.2 = x.2 := by rw [hv2] at h2; linarith
    exact Prod.ext hx1.symm hx2.symm
  -- strict concavity of the 1-D restriction
  have hg := lineVol_strictConcaveOn hseg hvne
  -- apply it at the endpoints 0, 1
  have h01 : (0 : ℝ) ≠ 1 := by norm_num
  have key := hg.2 (Set.left_mem_Icc.mpr (by norm_num)) (Set.right_mem_Icc.mpr (by norm_num))
    h01 ha hb hab
  -- translate the 1-D inequality back to tetVol
  have g0 : lineVol x.1 x.2 v1 v2 0 = tetVol x := by
    simp only [lineVol, tetVol, mul_zero, add_zero]
  have g1 : lineVol x.1 x.2 v1 v2 1 = tetVol y := by
    simp only [lineVol, tetVol, mul_one, hv1, hv2]; ring_nf
  have gb : lineVol x.1 x.2 v1 v2 (a • (0:ℝ) + b • (1:ℝ)) = tetVol (a • x + b • y) := by
    have hb' : a • (0:ℝ) + b • (1:ℝ) = b := by simp
    rw [hb']
    -- x + b•(y-x) = a•x + b•y  (since a = 1 - b)
    have ha' : a = 1 - b := by linarith
    simp only [lineVol, tetVol, smul_eq_mul, Prod.fst_add, Prod.snd_add,
      Prod.smul_fst, Prod.smul_snd, hv1, hv2, ha']
    ring_nf
  rw [g0, g1, gb] at key
  simpa only [smul_eq_mul] using key

end QOU.Archimedean
