/-
  The obtuse tiling — assembling the a.e. decomposition (bean `qou-w3eg`, H4-5).

  The ingredients are proved in `ObtuseWedgeDegenerate.lean`; this file is the
  assembly.  Target:

      inscribedTriangle R t α β γ
        =ᵐ (wedgeAt R (t+2γ+α) α ∪ wedgeAt R (t+2γ+2α+β) β)
             \ wedgeAt R (t+γ+π) (π−γ)          (γ obtuse)

  **Both** directions are a.e. rather than strict, over two different null sets:

  * `T \ RHS` is controlled by the wedge EDGE LINES, exactly as in the acute
    `milnorWedges_ae_eq_inscribedTriangle` — lines through the origin, killed by
    `volume_perpLine`.
  * `RHS \ T` is controlled by the `γ`-CHORD LINE.  That is an *affine* line,
    not one through the origin, and `volume_perpLine` does not reach it — hence
    `volume_chordLine` below.  The reason is `gamma_chord_of_mem_alpha`, which
    concludes `≤` and cannot conclude `<`: a point on that chord line is in
    neither side.

  Archimedean (ℝ): `Real.pi`, ordering — §7c.

  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  -- Ref: [manuscript] bean qou-w3eg (H4-5 obtuse)
-/
import QOU.Archimedean.ObtuseWedgeDegenerate

namespace QOU.Archimedean.HyperbolicVolume

open Real Set MeasureTheory

/-- **A chord line is null.**  The companion of `volume_perpLine` for an
*affine* line: `{w | ⟨w,u_φ⟩ = c}` rather than `{w | ⟨w,v_φ⟩ = 0}`.

Two observations make it a corollary rather than a new measure-theoretic
argument.  First, the corresponding line **through the origin** is already a
`perpLine`, at the rotated angle `φ + π/2`:

    −⟨w, (sin(φ+π/2), −cos(φ+π/2))⟩ = −(w₁ cos φ + w₂ sin φ),

so it vanishes exactly where the chord functional does.  Second, the level set
at height `c` is that kernel translated by `c · u_φ`, and `volume` on `ℝ × ℝ` is
translation invariant.  (Mathlib's `Measure.addHaar_affineSubspace` would also
serve, at the cost of packaging the set as an `AffineSubspace`.) -/
theorem volume_chordLine (φ c : ℝ) :
    (volume : Measure (ℝ × ℝ))
        {w : ℝ × ℝ | w.1 * Real.cos φ + w.2 * Real.sin φ = c} = 0 := by
  have hpy := Real.sin_sq_add_cos_sq φ
  -- the translated point's perp-functional at `φ + π/2`, computed once
  have hkey : ∀ w : ℝ × ℝ,
      -((w.1 - c * Real.cos φ) * Real.sin (φ + π / 2))
        + (w.2 - c * Real.sin φ) * Real.cos (φ + π / 2)
      = -(w.1 * Real.cos φ + w.2 * Real.sin φ) + c := by
    intro w
    simp only [Real.sin_add, Real.cos_add, Real.sin_pi_div_two, Real.cos_pi_div_two]
    linear_combination c * hpy
  have hshift : {w : ℝ × ℝ | w.1 * Real.cos φ + w.2 * Real.sin φ = c}
      = (fun w : ℝ × ℝ => w + (-(c * Real.cos φ, c * Real.sin φ))) ⁻¹'
        {w : ℝ × ℝ | -(w.1 * Real.sin (φ + π / 2))
            + w.2 * Real.cos (φ + π / 2) = 0} := by
    ext w
    simp only [Set.mem_setOf_eq, Set.mem_preimage, Prod.fst_add, Prod.snd_add,
      Prod.fst_neg, Prod.snd_neg]
    rw [show w.1 + -(c * Real.cos φ) = w.1 - c * Real.cos φ from by ring,
      show w.2 + -(c * Real.sin φ) = w.2 - c * Real.sin φ from by ring, hkey w]
    constructor <;> intro h <;> linarith
  rw [hshift, measure_preimage_add_right]
  exact volume_perpLine _

/-- **A point of the triangle is never in the subtracted wedge** — and this
direction is STRICT, no null set needed.

`W_sub`'s chord condition is the strict complement of the triangle's `γ`-chord
(see `gamma_chord_of_notMem_sub`), so membership in the triangle refutes it
outright.  This is the cheap half of `T ⊆ RHS`; the other half is the covering
argument, which does need the edge lines. -/
theorem notMem_sub_of_mem_inscribedTriangle {R t α β γ : ℝ}
    {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ) :
    w ∉ wedgeAt R (t + γ + π) (π - γ) := by
  intro hsub
  -- the triangle's γ-chord
  have htri : w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ :=
    hw.1.1
  -- W_sub's chord says the opposite, strictly
  have hs := hsub.1
  have hc : Real.cos (t + γ + π) = -Real.cos (t + γ) := by simp [Real.cos_add]
  have hsn : Real.sin (t + γ + π) = -Real.sin (t + γ) := by simp [Real.sin_add]
  have hcψ : Real.cos (π - γ) = -Real.cos γ := by simp [Real.cos_pi_sub]
  rw [hc, hsn, hcψ] at hs
  linarith

/-! ### The covering — and why the acute sign relation does NOT survive

In the acute case (`inscribedTriangle_subset_milnorWedges_of_ne`) the covering
is carried entirely by `perp_sign_relation`

    sin(2α)·x + sin(2β)·y + sin(2γ)·z = 0,        x = perp_t, y = perp_{t+2γ},
                                                  z = perp_{t+2γ+2α}

whose three coefficients are positive, so the all-positive and all-negative sign
patterns are impossible and the six survivors are exactly the six sectors.

**With `γ` obtuse that argument fails, and not marginally.**  `sin 2γ < 0`
(`sin_two_mul_neg_of_obtuse`), so the relation reads `a·x + b·y = c·z` with
`a, b, c > 0`, which forbids only `(+,+,−)` and `(−,−,+)`.  Of the six
remaining patterns **four** — `(+,+,+)`, `(+,−,+)`, `(+,−,−)`, `(−,−,−)` —
put the point in neither surviving wedge.  So the sign relation alone cannot
close the obtuse covering: it is not that the proof needs adapting, it is that
the fact it establishes is no longer sufficient.

What replaces it is a *stronger* geometric input, and it makes the sign relation
unnecessary rather than merely insufficient: the triangle lies inside the cone
spanned by the two rays `O→V₁` and `O→V₂`, i.e.

    w ∈ T   ⟹   perp_t(w) < 0   and   perp_{t+2γ}(w) > 0.

That is `γ` obtuse saying the circumcentre has left the triangle across the
`γ`-chord `V₁V₂`.  With both of those in hand a single case split on the sign of
`perp_{t+2γ+2α}` finishes: negative puts the point in `W_α`, positive in `W_β`.

Two consequences worth stating, because they are better than the acute case
rather than worse:

* the covering needs **one** edge functional to be nonzero, not three, so this
  direction's null set is a single line rather than three;
* neither bound needs `perp_sign_relation`, `perp_three_angle_relation`, or any
  disjointness — each is a two-term identity against the two chords meeting at
  the vertex in question. -/

/-- **Certificate for the first edge functional**, against the two chords that
meet at the triangle's first vertex `V₁ = R·u_t`.

Writing `P = R − ⟨w,u_t⟩` and `Q = perp_t(w)`, the shift identity
`⟨w,u_{t+φ}⟩ = ⟨w,u_t⟩ cos φ + Q sin φ` turns the two chord slacks into

    F := R cos γ − ⟨w,u_{t+γ}⟩   = P cos γ − Q sin γ      (the γ-chord, V₁V₂)
    G := R cos β − ⟨w,u_{t−β}⟩   = P cos β + Q sin β      (the β-chord, V₃V₁)

and eliminating `P` gives `Q·sin(β+γ) = G cos γ − F cos β`, which is the
statement below once `sin(β+γ) = sin α` and `t + 2γ + 2α + β = t − β + 2π`.
Note `R` cancels: both sides are `R`-free, and the identity holds for every `w`
and every angle triple summing to `π`, acute or not. -/
theorem perp_start_certificate {R t α β γ : ℝ} (hsum : α + β + γ = π) (w : ℝ × ℝ) :
    (-(w.1 * Real.sin t) + w.2 * Real.cos t) * Real.sin α
      = Real.cos γ * (R * Real.cos β
            - (w.1 * Real.cos (t + 2 * γ + 2 * α + β)
                + w.2 * Real.sin (t + 2 * γ + 2 * α + β)))
        - Real.cos β * (R * Real.cos γ
            - (w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ))) := by
  rw [show t + 2 * γ + 2 * α + β = t - β + 2 * π by linarith,
    Real.cos_add_two_pi, Real.sin_add_two_pi,
    show α = π - (β + γ) by linarith, Real.sin_pi_sub]
  simp only [Real.sin_add, Real.cos_add, Real.sin_sub, Real.cos_sub]
  ring

/-- **Certificate for the second edge functional**, the mirror at
`V₂ = R·u_{t+2γ}`, against the `γ`-chord `V₁V₂` and the `α`-chord `V₂V₃`.

Same elimination in the frame at `s = t + 2γ`, where the two chords sit at
`s − γ` and `s + α`; it yields `perp_s·sin(γ+α) = F cos α − H cos γ` with
`H := R cos α − ⟨w,u_{s+α}⟩`, and `sin(γ+α) = sin β`. -/
theorem perp_second_certificate {R t α β γ : ℝ} (hsum : α + β + γ = π) (w : ℝ × ℝ) :
    (-(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ)) * Real.sin β
      = Real.cos α * (R * Real.cos γ
            - (w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ)))
        - Real.cos γ * (R * Real.cos α
            - (w.1 * Real.cos (t + 2 * γ + α) + w.2 * Real.sin (t + 2 * γ + α))) := by
  rw [show β = π - (γ + α) by linarith, Real.sin_pi_sub,
    -- both chords must be read in the frame at `s = t + 2γ`, at `s − γ` and
    -- `s + α`; left as `t + γ` the two sides expand around different centres
    show t + γ = t + 2 * γ - γ by ring]
  simp only [Real.sin_add, Real.cos_add, Real.sin_sub, Real.cos_sub]
  ring

/-- **The triangle lies strictly below the first vertex ray.**

`cos γ < 0` is the whole content: it flips the first term of
`perp_start_certificate`, and the second is negative anyway because `β` is
acute.  In the acute case both terms have the opposite sign and the conclusion
is false — the circumcentre is then inside the triangle and `perp_t` takes both
signs on it. -/
theorem perp_start_neg_of_obtuse {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ)
    (hsum : α + β + γ = π) {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ) :
    -(w.1 * Real.sin t) + w.2 * Real.cos t < 0 := by
  obtain ⟨⟨h₁, -⟩, h₃⟩ := hw
  obtain ⟨-, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  have hπ : 0 < π := Real.pi_pos
  have hsα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  have hcβ : 0 < Real.cos β := Real.cos_pos_of_mem_Ioo ⟨by linarith, hβ⟩
  have hcγ : Real.cos γ < 0 := Real.cos_neg_of_pi_div_two_lt_of_lt hγ (by linarith)
  have hF : w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ := h₁
  have hG : w.1 * Real.cos (t + 2 * γ + 2 * α + β)
      + w.2 * Real.sin (t + 2 * γ + 2 * α + β) < R * Real.cos β := h₃
  have hcert := perp_start_certificate (R := R) (t := t) hsum w
  have hkey : (-(w.1 * Real.sin t) + w.2 * Real.cos t) * Real.sin α < 0 := by
    rw [hcert]
    nlinarith [mul_pos (neg_pos.mpr hcγ) (sub_pos.mpr hG),
      mul_pos hcβ (sub_pos.mpr hF)]
  by_contra hcon
  push_neg at hcon
  nlinarith [mul_nonneg hcon hsα.le]

/-- **The triangle lies strictly above the second vertex ray** — the mirror,
from `perp_second_certificate` with `α` acute in place of `β`. -/
theorem perp_second_pos_of_obtuse {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ)
    (hsum : α + β + γ = π) {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ) :
    0 < -(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ) := by
  obtain ⟨⟨h₁, h₂⟩, -⟩ := hw
  obtain ⟨hα, -⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  have hπ : 0 < π := Real.pi_pos
  have hsβ : 0 < Real.sin β := Real.sin_pos_of_pos_of_lt_pi hβ0 (by linarith)
  have hcα : 0 < Real.cos α := Real.cos_pos_of_mem_Ioo ⟨by linarith, hα⟩
  have hcγ : Real.cos γ < 0 := Real.cos_neg_of_pi_div_two_lt_of_lt hγ (by linarith)
  have hF : w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ := h₁
  have hH : w.1 * Real.cos (t + 2 * γ + α) + w.2 * Real.sin (t + 2 * γ + α)
      < R * Real.cos α := h₂
  have hcert := perp_second_certificate (R := R) (t := t) hsum w
  have hkey : 0 < (-(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ))
      * Real.sin β := by
    rw [hcert]
    nlinarith [mul_pos hcα (sub_pos.mpr hF),
      mul_pos (neg_pos.mpr hcγ) (sub_pos.mpr hH)]
  by_contra hcon
  push_neg at hcon
  nlinarith [mul_nonneg (neg_nonneg.mpr hcon) hsβ.le]

/-- **THE OBTUSE COVERING.**  A point of the triangle off the single edge line
`perp_{t+2γ+2α} = 0` lies in `W_α` or in `W_β`.

Both cone bounds are already established, so the case split is on that one
functional and each branch is one application of `mem_wedgeAt_of_halfplanes`
(available because `α` and `β` are acute — which is what `γ` obtuse buys).

Compare the acute statement, which needs all THREE edge functionals nonzero. -/
theorem inscribedTriangle_subset_obtuseWedges_of_ne {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ)
    (hsum : α + β + γ = π) {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ)
    (hz : -(w.1 * Real.sin (t + (2 * γ + 2 * α)))
            + w.2 * Real.cos (t + (2 * γ + 2 * α)) ≠ 0) :
    w ∈ wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β := by
  obtain ⟨hα, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  have hπ : 0 < π := Real.pi_pos
  have hx := perp_start_neg_of_obtuse hα0 hβ0 hγ hsum hw
  have hy := perp_second_pos_of_obtuse hα0 hβ0 hγ hsum hw
  obtain ⟨⟨-, h₂⟩, h₃⟩ := hw
  rcases hz.lt_or_gt with hzs | hzs
  · -- `perp_{t+2γ+2α} < 0`: the point is in `W_α`
    refine Or.inl (mem_wedgeAt_of_halfplanes hα0 hα h₂ ?_ ?_)
    · rw [show t + 2 * γ + α + α = t + (2 * γ + 2 * α) by ring]; exact hzs
    · rw [show t + 2 * γ + α - α = t + 2 * γ by ring]; exact hy
  · -- `perp_{t+2γ+2α} > 0`: the point is in `W_β`
    refine Or.inr (mem_wedgeAt_of_halfplanes hβ0 hβ h₃ ?_ ?_)
    · rw [show t + 2 * γ + 2 * α + β + β = t + 2 * π by linarith,
        Real.sin_add_two_pi, Real.cos_add_two_pi]
      exact hx
    · rw [show t + 2 * γ + 2 * α + β - β = t + (2 * γ + 2 * α) by ring]; exact hzs

end QOU.Archimedean.HyperbolicVolume
