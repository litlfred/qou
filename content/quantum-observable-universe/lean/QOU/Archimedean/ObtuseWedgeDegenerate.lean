/-
  `wedgeAt` is acute-ONLY by construction — the obtuse case cannot be obtained
  by substituting an obtuse half-angle (bean `qou-w3eg`, H4-5).

  WHY THIS FILE EXISTS.  The obtuse case of Milnor's identity needs a
  replacement for the wedge subtending the obtuse angle, and the tempting move
  is to reuse `wedgeAt R θ ψ` at `ψ > π/2` and let the geometry supply Milnor's
  minus sign.  **That does not work, and this file proves why** — so that a
  later agent does not spend a session discovering it.

  `wedgeAt R θ ψ` is
  `{w | ⟨w,u_θ⟩ < R cos ψ ∧ |⟨w,v_θ⟩| < ⟨w,u_θ⟩ · tan ψ}`
  (`OrthoschemeRotation.lean`), whose docstring calls it "the open isoceles
  triangle with apex at the circumcentre, apex angle `2ψ`".  For `ψ ∈ (π/2, π)`
  we have `tan ψ < 0`, and since `|⟨w,v_θ⟩| ≥ 0` the second conjunct forces
  `⟨w,u_θ⟩ < 0`: every point of the set lies **strictly on the far side of the
  circumcentre**, so the set opens away from the apex rather than towards it.
  Together with `⟨w,u_θ⟩ < R cos ψ < 0` (unbounded below) it is not a triangle
  at all.

  So the acuteness hypotheses carried throughout the wedge machinery
  (`hypVolume_chimney_wedgeAt`, `disjoint_wedgeAt_adjacent`, the tiling) are
  **structural, not technical** — they are what make `wedgeAt` denote the object
  its name claims.

  WHAT THE OBTUSE CASE ACTUALLY NEEDS instead: the wedge in the OPPOSITE
  direction with the ACUTE half-angle `π − γ = α + β`, SUBTRACTED —

      inscribedTriangle R t α β γ
        =ᵐ (wedgeAt R (t+2γ+α) α ∪ wedgeAt R (t+2γ+2α+β) β)
             \ wedgeAt R (t+γ+π) (π−γ)

  every half-angle on the right being acute when `γ` is obtuse, which is the
  set-level counterpart of `IdealTetObtuseReduction.lob_sum_eq_reflected`.  That
  identity is measured (zero mismatches over ~117k grid points,
  `computations/milnor_obtuse_wedge_decomposition_probe.py`) and is **not**
  proved here.

  Nothing in this file asserts anything about a volume.

  Archimedean (ℝ): `Real.tan`, `Real.pi`, ordering — §7c.

  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  -- Ref: [manuscript] bean qou-w3eg (H4-5 obtuse)
-/
import QOU.Archimedean.OrthoschemeLambdaSum

namespace QOU.Archimedean.HyperbolicVolume

open Real Set
open QOU.Archimedean

/-- **`tan` is negative on `(π/2, π)`** — `sin > 0` and `cos < 0` there.
Mathlib names the `(-π/2, 0)` case (`Real.tan_neg_of_neg_of_pi_div_two_lt`) but
not this one. -/
theorem tan_neg_of_pi_div_two_lt_of_lt_pi {ψ : ℝ} (h1 : π / 2 < ψ) (h2 : ψ < π) :
    Real.tan ψ < 0 := by
  rw [Real.tan_eq_sin_div_cos]
  exact div_neg_of_pos_of_neg
    (Real.sin_pos_of_pos_of_lt_pi (by linarith [Real.pi_pos]) h2)
    (Real.cos_neg_of_pi_div_two_lt_of_lt h1 (by linarith [Real.pi_pos]))

/-- **At an obtuse half-angle the wedge lies strictly on the FAR side of the
apex.**  The defining inequality `|⟨w,v⟩| < ⟨w,u⟩ · tan ψ` has a non-negative
left side, so it forces `⟨w,u⟩ · tan ψ > 0`; with `tan ψ < 0` that gives
`⟨w,u⟩ < 0`.

This is the precise sense in which `wedgeAt` is acute-only: at `ψ > π/2` it does
not degenerate to something smaller, it moves to the other side of the
circumcentre. -/
theorem wedgeAt_inner_neg_of_obtuse {R θ ψ : ℝ} (h1 : π / 2 < ψ) (h2 : ψ < π)
    {w : ℝ × ℝ} (hw : w ∈ wedgeAt R θ ψ) :
    w.1 * Real.cos θ + w.2 * Real.sin θ < 0 := by
  obtain ⟨-, hside⟩ := hw
  have habs : (0 : ℝ) ≤ |(-(w.1 * Real.sin θ) + w.2 * Real.cos θ)| := abs_nonneg _
  have hprod : 0 < (w.1 * Real.cos θ + w.2 * Real.sin θ) * Real.tan ψ :=
    lt_of_le_of_lt habs hside
  have htan : Real.tan ψ < 0 := tan_neg_of_pi_div_two_lt_of_lt_pi h1 h2
  by_contra hcon
  push_neg at hcon
  nlinarith [hprod, htan, hcon]

/-- **The obtuse wedge is disjoint from the closed near half-plane** — the
containment form of the lemma above.  In particular it contains no point of the
ray from the circumcentre in the direction `θ` its name refers to. -/
theorem wedgeAt_subset_far_halfplane_of_obtuse {R θ ψ : ℝ}
    (h1 : π / 2 < ψ) (h2 : ψ < π) :
    wedgeAt R θ ψ ⊆ {w : ℝ × ℝ | w.1 * Real.cos θ + w.2 * Real.sin θ < 0} :=
  fun _ hw => wedgeAt_inner_neg_of_obtuse h1 h2 hw

/-- **The apex itself is not in the obtuse wedge.**  A sanity corollary: the
circumcentre lies in `wedgeAt R θ ψ` for no obtuse `ψ`, whereas for acute `ψ`
the wedge is the isoceles triangle *with apex there*. -/
theorem origin_notMem_wedgeAt_of_obtuse {R θ ψ : ℝ} (h1 : π / 2 < ψ) (h2 : ψ < π) :
    ((0 : ℝ), (0 : ℝ)) ∉ wedgeAt R θ ψ := by
  intro hmem
  have := wedgeAt_inner_neg_of_obtuse h1 h2 hmem
  simp at this

/-! ### Where Milnor's sign enters the corpus's own algebra

`QOU.Archimedean.HyperbolicVolume.perp_sign_relation` (`OrthoschemeTiling.lean`)
states the single linear relation among the three edge functionals, with
coefficients `sin 2α`, `sin 2β`, `sin 2γ`.  **It is proved from `α + β + γ = π`
alone — it carries no acuteness hypothesis** — so it holds verbatim in the
obtuse case.  What acuteness buys is only the *positivity* of those three
coefficients, and its docstring says so: "all POSITIVE for acute angles.  That
positivity is the whole covering argument."

The lemmas below locate the failure exactly: when `γ` is obtuse the relation is
unchanged and **exactly one coefficient turns negative**.  So the obtuse case
does not need a new relation, only a covering argument run against a different
sign pattern — and that lone minus is Milnor's. -/

/-- **`sin 2γ < 0` for an obtuse `γ`.**  `sin (2γ) = 2 sin γ cos γ` with
`sin γ > 0` and `cos γ < 0` on `(π/2, π)`. -/
theorem sin_two_mul_neg_of_obtuse {γ : ℝ} (h1 : π / 2 < γ) (h2 : γ < π) :
    Real.sin (2 * γ) < 0 := by
  rw [Real.sin_two_mul]
  have hs : 0 < Real.sin γ :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [Real.pi_pos]) h2
  have hc : Real.cos γ < 0 :=
    Real.cos_neg_of_pi_div_two_lt_of_lt h1 (by linarith [Real.pi_pos])
  nlinarith [hs, hc]

/-- **In an obtuse admissible triple the other two angles are acute.**
`γ > π/2` and `α + β + γ = π` with `β > 0` force `α < π/2`, and symmetrically.
(The corpus already records the `at_most_one_obtuse` half in
`IdealTetObtuseReduction`; this is the quantitative form the sign argument
needs.) -/
theorem acute_of_obtuse_third {α β γ : ℝ} (hα0 : 0 < α) (hβ0 : 0 < β)
    (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    α < π / 2 ∧ β < π / 2 := by
  constructor <;> linarith

/-- **The obtuse sign pattern of `perp_sign_relation`'s coefficients: `+ + −`.**

The relation itself is unchanged (it needs only `α + β + γ = π`); when `γ` is
obtuse exactly one of its three coefficients is negative.  This is the precise
point at which the acute covering argument stops applying, and the precise
origin of the minus sign in Milnor's subdivision. -/
theorem perp_coeff_signs_of_obtuse {α β γ : ℝ} (hα0 : 0 < α) (hβ0 : 0 < β)
    (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    0 < Real.sin (2 * α) ∧ 0 < Real.sin (2 * β) ∧ Real.sin (2 * γ) < 0 := by
  obtain ⟨hα, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  refine ⟨?_, ?_, sin_two_mul_neg_of_obtuse hγ (by linarith)⟩
  · exact Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  · exact Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)

/-! ### The two surviving wedges are disjoint, by the ACUTE lemma unchanged

The point of the whole `π−γ` reformulation is that the obtuse configuration is
built from acute pieces, so the existing acute machinery applies with no new
geometry.  This is the first cash-out: `disjoint_wedgeAt_adjacent` demands
`0 < ψᵢ < π/2` of both wedges, and `acute_of_obtuse_third` supplies exactly
that for `α` and `β`.  The adjacency side condition
`θ₁ + ψ₁ = θ₂ − ψ₂` holds on the nose:

    (t + 2γ + α) + α  =  t + 2γ + 2α  =  (t + 2γ + 2α + β) − β
-/

/-- **In the obtuse configuration the two surviving wedges are disjoint.**
No new argument — the acute `disjoint_wedgeAt_adjacent` applies verbatim,
because `γ` obtuse forces `α` and `β` acute. -/
theorem disjoint_wedgeAt_obtuse_pair {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    Disjoint (wedgeAt R (t + 2 * γ + α) α)
      (wedgeAt R (t + 2 * γ + 2 * α + β) β) := by
  obtain ⟨hα, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  exact disjoint_wedgeAt_adjacent hα0 hα hβ0 hβ (by ring)

/-! ### The missing chord helper: a wedge fits under the chord of any SHRUNK
half-angle, in the correspondingly rotated direction

`wedgeAt_lt_chord_next` / `_prev` place a wedge under the chords of its two
NEIGHBOURS, at directions `θ ± ψ ± ψ'`.  The obtuse decomposition needs
something they cannot give: the chord of a SUB-angle of the wedge's own,
at direction `θ − δ`.  Solving `θ − ψ − ψ' = θ − δ` forces `ψ' = δ − ψ ≤ 0`,
and both existing lemmas require `0 < ψ'` — which is why this step has no
existing helper.

The statement: for `w` in the wedge of half-angle `ψ` about `θ`, and any
`0 ≤ δ ≤ ψ`,

    ⟨w, u_{θ−δ}⟩  <  R cos (ψ − δ).

Sharp at `δ = 0` (the wedge's own chord) and at `δ = ψ`, where the bound `R`
is attained in the limit at the wedge's far vertex on that side.

The certificate is the same shape as the two existing chord lemmas, and it is
*simpler* than theirs: writing `S = ⟨w,u_θ⟩` and `P = ⟨w,v_{θ−ψ}⟩`,

  cos ψ · (R cos(ψ−δ) − ⟨w,u_{θ−δ}⟩)
      = cos(ψ−δ) · (R cos ψ − S)  +  P · sin δ,

which is a pure `ring` identity once the angle-differences are expanded — no
Pythagorean rewrite is needed, unlike `wedgeAt_lt_chord_next`/`_prev`.  Both
summands on the right are non-negative (the first strictly), the first from the
wedge's own chord bound and the second from `wedgeAt_lower`. -/
theorem wedgeAt_lt_chord_shift {R θ ψ δ : ℝ}
    (hψ0 : 0 < ψ) (hψ : ψ < π / 2) (hδ0 : 0 ≤ δ) (hδ : δ ≤ ψ) :
    ∀ w ∈ wedgeAt R θ ψ,
      w.1 * Real.cos (θ - δ) + w.2 * Real.sin (θ - δ) < R * Real.cos (ψ - δ) := by
  intro w hw
  have hπ : 0 < π := Real.pi_pos
  have hcψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hcψ' : 0 < Real.cos (ψ - δ) :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
  have hsδ : 0 ≤ Real.sin δ :=
    Real.sin_nonneg_of_nonneg_of_le_pi hδ0 (by linarith)
  have hP : 0 < -(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ) :=
    wedgeAt_lower hψ0 hψ w hw
  have hG : 0 < R * Real.cos ψ - (w.1 * Real.cos θ + w.2 * Real.sin θ) := by
    have := hw.1; linarith
  have key :
      Real.cos ψ * (R * Real.cos (ψ - δ)
          - (w.1 * Real.cos (θ - δ) + w.2 * Real.sin (θ - δ)))
        = Real.cos (ψ - δ) * (R * Real.cos ψ - (w.1 * Real.cos θ + w.2 * Real.sin θ))
          + (-(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ)) * Real.sin δ := by
    simp only [Real.sin_sub, Real.cos_sub]
    ring
  nlinarith [mul_pos hcψ' hG, mul_nonneg hP.le hsδ]

/-- **The instance the obtuse decomposition needs**, and the reason
`wedgeAt_lt_chord_shift` was written: the subtracted wedge `W_sub` sits under
`W_α`'s chord.

`W_sub = wedgeAt R (t+γ+π) (π−γ)` has half-angle `π−γ = α+β`, and
`t + 2γ + α = (t+γ+π) − β` because `γ = π − α − β`.  So this is the shift
lemma at `δ = β`, whose bound `R cos((α+β) − β) = R cos α` is exactly `W_α`'s
chord.  Both hypotheses come free: `α+β < π/2` because `γ` is obtuse, and
`0 ≤ β ≤ α+β` because `α > 0`. -/
theorem wedgeAt_sub_lt_chord_alpha {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    ∀ w ∈ wedgeAt R (t + γ + π) (π - γ),
      w.1 * Real.cos (t + 2 * γ + α) + w.2 * Real.sin (t + 2 * γ + α)
        < R * Real.cos α := by
  intro w hw
  have hdir : t + 2 * γ + α = (t + γ + π) - β := by linarith
  have hhalf : π - γ = α + β := by linarith
  have h := wedgeAt_lt_chord_shift (R := R) (θ := t + γ + π) (ψ := π - γ) (δ := β)
    (by linarith) (by linarith) hβ0.le (by linarith) w hw
  rw [hdir]
  have hbound : π - γ - β = α := by linarith
  rwa [hbound] at h

end QOU.Archimedean.HyperbolicVolume
