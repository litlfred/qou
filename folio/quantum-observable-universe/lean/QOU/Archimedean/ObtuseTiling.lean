/-
  The obtuse tiling — assembling the a.e. decomposition (bean `qou-w3eg`, H4-5).

  The ingredients are proved in `ObtuseWedgeDegenerate.lean`; this file is the
  assembly.  It reaches, for `π/2 < γ`:

      inscribedTriangle R t α β γ
        =ᵐ (wedgeAt R (t+2γ+α) α ∪ wedgeAt R (t+2γ+2α+β) β)
             \ wedgeAt R (t+γ+π) (π−γ)            (`obtuseWedges_ae_eq_…`)

      Vol(chimney (inscribedTriangle R t α β γ) R) = Λ(α) + Λ(β) + Λ(γ)
                                    (`hypVolume_chimney_inscribedTriangle_obtuse`)

  the second being the obtuse counterpart of `hypVolume_chimney_inscribedTriangle`
  (which assumes all three angles acute); the identity itself on an ideal
  tetrahedron (`idealTetVolume_of_vertices_obtuse`); and the RIGHT-ANGLED case
  `γ = π/2` (`…_right`), which completes the coverage.

  **THE IDENTITY IS UNCONDITIONAL** —
  `idealTetVolume_of_vertices_unconditional`, at the end of the file: no
  acuteness, no distinguished angle, no case hypothesis.  Just `0 < α, β, γ` and
  `α + β + γ = π`.

  Getting there needed one step beyond the three cases, and it is worth naming
  because an earlier revision of this header asserted the conclusion without it.
  The three cases are stated with `γ` as the distinguished angle, so a triple
  whose non-acute angle is `α` or `β` satisfies none of them **as written**.
  "Every admissible triple is covered" was therefore a claim about a relabelling
  that had not been taken.

  It is now taken, and it is exact rather than approximate: with `α+β+γ = π` a
  cyclic relabel of the angles plus the matching shift of the base angle names
  the *same three circle points* (the third lands on `t + 2π`), so it is the same
  region — `idealTetrahedron_cyclic`, which in turn is just
  `verticalHalfSpaceThrough_swap`: that half-space is a product of two signed
  areas sharing an edge, and swapping the edge's endpoints negates both.

  This header said otherwise, and was wrong in two independent ways.  It read:
  *"Between them the two cover every triangle except the right-angled one, where
  `γ = π/2` degenerates `W_sub` to a half-plane and the `ψ < π/2` wedge machinery
  fails on both sides."*

  * `W_sub` does **not** degenerate to a half-plane — it degenerates to the EMPTY
    SET (`wedgeAt_pi_div_two_eq_empty`).  Its chord bound `⟨w,u⟩ < R cos(π−γ) = 0`
    cuts away exactly the half-plane its half-turn opening would sweep.
  * Because there is then nothing to subtract, the right-angled case is not the
    hard leftover it was billed as — it is the EASIEST of the three.  It needs no
    subtraction and, unlike the obtuse case, no `γ`-chord null set either: the two
    certificates give that chord strictly.

  Both errors are the same one twice: reasoning about a degeneration from its
  description instead of evaluating it.

  **This header said the opposite twice, and the retraction is the useful part.**
  It read: *"SCOPE — this does not close the obtuse case … `idealTet_eq_chimney`
  still carries `α, β, γ < π/2` and is a set equality — analytic continuation
  cannot supply it, and neither can anything here."*  The premise was checked and
  is false: that theorem's three acuteness hypotheses were **unused**, spent only
  on `X < π` side goals the angle sum already gives.  Dropping them costs three
  edits and closes the case.  The lesson is not about this file — a hypothesis
  inherited down a chain is not evidence that the chain needs it, and I asserted
  the gate twice without reading the proof that was supposed to enforce it.

  **Both** directions of the tiling are a.e. rather than strict, over two
  different null sets:

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
  -- Ref: [leitner2026] bean qou-w3eg (H4-5 obtuse)
-/
import QOU.Archimedean.ObtuseWedgeDegenerate
import QOU.Archimedean.IdealTetObtuseReduction
import QOU.Archimedean.IdealTetEqChimney
import QOU.Archimedean.MostowIdealTetVolume

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
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 ≤ γ)
    (hsum : α + β + γ = π) {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ) :
    -(w.1 * Real.sin t) + w.2 * Real.cos t < 0 := by
  obtain ⟨⟨h₁, -⟩, h₃⟩ := hw
  -- `β < π/2` from `γ ≥ π/2` and the angle sum; `acute_of_obtuse_third` wants
  -- the strict `γ > π/2` and is not needed for this.
  have hβ : β < π / 2 := by linarith
  have hπ : 0 < π := Real.pi_pos
  have hsα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  have hcβ : 0 < Real.cos β := Real.cos_pos_of_mem_Ioo ⟨by linarith, hβ⟩
  have hcγ : Real.cos γ ≤ 0 :=
    Real.cos_nonpos_of_pi_div_two_le_of_le hγ (by linarith)
  have hF : w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ := h₁
  have hG : w.1 * Real.cos (t + 2 * γ + 2 * α + β)
      + w.2 * Real.sin (t + 2 * γ + 2 * α + β) < R * Real.cos β := h₃
  have hcert := perp_start_certificate (R := R) (t := t) hsum w
  have hkey : (-(w.1 * Real.sin t) + w.2 * Real.cos t) * Real.sin α < 0 := by
    rw [hcert]
    nlinarith [mul_nonneg (neg_nonneg.mpr hcγ) (sub_pos.mpr hG).le,
      mul_pos hcβ (sub_pos.mpr hF)]
  by_contra hcon
  push_neg at hcon
  nlinarith [mul_nonneg hcon hsα.le]

/-- **The triangle lies strictly above the second vertex ray** — the mirror,
from `perp_second_certificate` with `α` acute in place of `β`. -/
theorem perp_second_pos_of_obtuse {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 ≤ γ)
    (hsum : α + β + γ = π) {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ) :
    0 < -(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ) := by
  obtain ⟨⟨h₁, h₂⟩, -⟩ := hw
  have hα : α < π / 2 := by linarith
  have hπ : 0 < π := Real.pi_pos
  have hsβ : 0 < Real.sin β := Real.sin_pos_of_pos_of_lt_pi hβ0 (by linarith)
  have hcα : 0 < Real.cos α := Real.cos_pos_of_mem_Ioo ⟨by linarith, hα⟩
  have hcγ : Real.cos γ ≤ 0 :=
    Real.cos_nonpos_of_pi_div_two_le_of_le hγ (by linarith)
  have hF : w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ := h₁
  have hH : w.1 * Real.cos (t + 2 * γ + α) + w.2 * Real.sin (t + 2 * γ + α)
      < R * Real.cos α := h₂
  have hcert := perp_second_certificate (R := R) (t := t) hsum w
  have hkey : 0 < (-(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ))
      * Real.sin β := by
    rw [hcert]
    nlinarith [mul_pos hcα (sub_pos.mpr hF),
      mul_nonneg (neg_nonneg.mpr hcγ) (sub_pos.mpr hH).le]
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
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 ≤ γ)
    (hsum : α + β + γ = π) {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ)
    (hz : -(w.1 * Real.sin (t + (2 * γ + 2 * α)))
            + w.2 * Real.cos (t + (2 * γ + 2 * α)) ≠ 0) :
    w ∈ wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β := by
  -- `α, β < π/2` needs only `γ ≥ π/2`, so it is derived here rather than via
  -- `acute_of_obtuse_third`, whose hypothesis is strict.
  have hα : α < π / 2 := by linarith
  have hβ : β < π / 2 := by linarith
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

/-- **The subtracted wedge sits inside the union it is subtracted from** — off
the same single edge line.

Without this the set difference `(W_α ∪ W_β) \ W_sub` would be arithmetically
smaller than Milnor's signed sum `W_α + W_β − W_sub`: subtracting a set removes
only the part that was there.  With it, the two agree, and the volume identity
can be read off by additivity rather than by a signed-measure argument.

The proof is the two certificates read BACKWARDS.  `W_sub` is an *acute* wedge —
its half-angle is `π − γ ∈ (0, π/2)` precisely because `γ` is obtuse — so
`wedgeAt_lower` / `_upper` give it the same two cone bounds the triangle has,
`perp_{t+2γ} > 0` and `perp_t < 0`.  What it has instead of the triangle's
`γ`-chord is the OPPOSITE inequality `⟨w,u_{t+γ}⟩ > R cos γ`, and feeding that
sign into

    cos γ·(α-chord slack) = cos α·(γ-chord slack) − perp_{t+2γ}·sin β
    cos γ·(β-chord slack) = perp_t·sin α + cos β·(γ-chord slack)

makes both left sides negative, hence — `cos γ` being negative — both chord
slacks positive.  So a point of `W_sub` satisfies the `α`- and `β`-chords even
though it fails the `γ`-chord, which is exactly the geometry of a circumcentre
that has left the triangle across one edge. -/
theorem wedgeAt_sub_subset_alphaBeta_of_ne {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π)
    {w : ℝ × ℝ} (hw : w ∈ wedgeAt R (t + γ + π) (π - γ))
    (hz : -(w.1 * Real.sin (t + (2 * γ + 2 * α)))
            + w.2 * Real.cos (t + (2 * γ + 2 * α)) ≠ 0) :
    w ∈ wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β := by
  obtain ⟨hα, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  have hπ : 0 < π := Real.pi_pos
  have hsα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  have hsβ : 0 < Real.sin β := Real.sin_pos_of_pos_of_lt_pi hβ0 (by linarith)
  have hcα : 0 < Real.cos α := Real.cos_pos_of_mem_Ioo ⟨by linarith, hα⟩
  have hcβ : 0 < Real.cos β := Real.cos_pos_of_mem_Ioo ⟨by linarith, hβ⟩
  have hcγ : Real.cos γ < 0 := Real.cos_neg_of_pi_div_two_lt_of_lt hγ (by linarith)
  -- `W_sub` is acute: its half-angle is `π − γ`, and `γ` obtuse puts it under `π/2`
  have hψ0 : 0 < π - γ := by linarith
  have hψ : π - γ < π / 2 := by linarith
  -- the two cone bounds, from `W_sub`'s own edges
  have hy : 0 < -(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ) := by
    have h := wedgeAt_lower hψ0 hψ w hw
    rwa [show t + γ + π - (π - γ) = t + 2 * γ by ring] at h
  have hx : -(w.1 * Real.sin t) + w.2 * Real.cos t < 0 := by
    have h := wedgeAt_upper hψ0 hψ w hw
    rwa [show t + γ + π + (π - γ) = t + 2 * π by ring,
      Real.sin_add_two_pi, Real.cos_add_two_pi] at h
  -- and the REVERSED γ-chord, which is `W_sub`'s own chord condition
  have hA : R * Real.cos γ
      - (w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ)) < 0 := by
    have hs := hw.1
    rw [show Real.cos (t + γ + π) = -Real.cos (t + γ) by simp [Real.cos_add],
      show Real.sin (t + γ + π) = -Real.sin (t + γ) by simp [Real.sin_add],
      show Real.cos (π - γ) = -Real.cos γ by simp [Real.cos_pi_sub]] at hs
    linarith
  -- the α-chord, from the second certificate
  have hB : 0 < R * Real.cos α
      - (w.1 * Real.cos (t + 2 * γ + α) + w.2 * Real.sin (t + 2 * γ + α)) := by
    have hcert := perp_second_certificate (R := R) (t := t) hsum w
    nlinarith [mul_neg_of_pos_of_neg hcα hA, mul_pos hy hsβ]
  -- the β-chord, from the first
  have hC : 0 < R * Real.cos β
      - (w.1 * Real.cos (t + 2 * γ + 2 * α + β)
          + w.2 * Real.sin (t + 2 * γ + 2 * α + β)) := by
    have hcert := perp_start_certificate (R := R) (t := t) hsum w
    nlinarith [mul_neg_of_neg_of_pos hx hsα, mul_neg_of_pos_of_neg hcβ hA]
  rcases hz.lt_or_gt with hzs | hzs
  · refine Or.inl (mem_wedgeAt_of_halfplanes hα0 hα (by linarith) ?_ ?_)
    · rw [show t + 2 * γ + α + α = t + (2 * γ + 2 * α) by ring]; exact hzs
    · rw [show t + 2 * γ + α - α = t + 2 * γ by ring]; exact hy
  · refine Or.inr (mem_wedgeAt_of_halfplanes hβ0 hβ (by linarith) ?_ ?_)
    · rw [show t + 2 * γ + 2 * α + β + β = t + 2 * π by linarith,
        Real.sin_add_two_pi, Real.cos_add_two_pi]
      exact hx
    · rw [show t + 2 * γ + 2 * α + β - β = t + (2 * γ + 2 * α) by ring]; exact hzs

/-! ### The obtuse decomposition -/

/-- **Milnor's obtuse figure**: the two surviving wedges, minus the one the
obtuse angle turns subtractive.

The acute `milnorWedges` is a union of three; here the `γ`-wedge is replaced by
`W_sub = wedgeAt R (t+γ+π) (π−γ)`, which sits on the far side of the `γ`-chord
and enters with a minus sign.  This is a set difference, not a signed sum: the
subtracted wedge is contained in the union up to the chord line, so the
arithmetic of Milnor's signed subdivision is realised set-theoretically. -/
def obtuseWedges (R t α β γ : ℝ) : Set (ℝ × ℝ) :=
  (wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β)
    \ wedgeAt R (t + γ + π) (π - γ)

theorem measurableSet_obtuseWedges (R t α β γ : ℝ) :
    MeasurableSet (obtuseWedges R t α β γ) :=
  ((measurableSet_wedgeAt _ _ _).union (measurableSet_wedgeAt _ _ _)).diff
    (measurableSet_wedgeAt _ _ _)

/-- **The reverse inclusion.**  A point of the obtuse figure off the `γ`-chord
LINE lies in the triangle.

Its own wedge supplies one chord directly and the neighbouring one through
`wedgeAt_lt_chord_next` / `_prev` — both usable because `α` and `β` are acute.
The `γ`-chord is the one that cannot be proved directly (`γ` obtuse puts
`R cos γ < 0`, outside every chord helper's range, and `W_α ⊄ chordHalfplane R
(t+γ) γ` in fact); it is extracted from `w ∉ W_sub` by
`gamma_chord_of_mem_alpha` / `_beta`, which conclude `≤`.  Ruling out the
equality case is exactly the hypothesis `hchord`, and is why this direction is
a.e. rather than strict. -/
theorem obtuseWedges_subset_inscribedTriangle_of_ne {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π)
    {w : ℝ × ℝ} (hw : w ∈ obtuseWedges R t α β γ)
    (hchord : w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) ≠ R * Real.cos γ) :
    w ∈ inscribedTriangle R t α β γ := by
  obtain ⟨hα, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  obtain ⟨hmem, hnot⟩ := hw
  rcases hmem with hwα | hwβ
  · -- in `W_α`: the α-chord is its own, the β-chord is its NEXT neighbour's
    refine ⟨⟨?_, hwα.1⟩, ?_⟩
    · exact lt_of_le_of_ne
        (gamma_chord_of_mem_alpha hα0 hβ0 hγ hsum hwα hnot) hchord
    · have h := wedgeAt_lt_chord_next hα0 hα hβ0 hβ w hwα
      rwa [show t + 2 * γ + α + α + β = t + 2 * γ + 2 * α + β by ring] at h
  · -- in `W_β`: the β-chord is its own, the α-chord is its PREVIOUS neighbour's
    refine ⟨⟨?_, ?_⟩, hwβ.1⟩
    · exact lt_of_le_of_ne
        (gamma_chord_of_mem_beta hα0 hβ0 hγ hsum hwβ hnot) hchord
    · have h := wedgeAt_lt_chord_prev hβ0 hβ hα0 hα w hwβ
      rwa [show t + 2 * γ + 2 * α + β - β - α = t + 2 * γ + α by ring] at h

/-- **THE OBTUSE TILING.**  Milnor's obtuse figure is the inscribed triangle, up
to a null set — the counterpart of `milnorWedges_ae_eq_inscribedTriangle`.

The two directions are controlled by two *different* null sets, and neither is
avoidable:

* `obtuseWedges \ T` sits in the `γ`-chord **line**, an AFFINE line (it does not
  pass through the circumcentre, since `R cos γ ≠ 0`), killed by
  `volume_chordLine`.  `volume_perpLine` cannot reach it.
* `T \ obtuseWedges` sits in the single edge line `perp_{t+2γ+2α} = 0`, through
  the origin, killed by `volume_perpLine`.  The acute statement needs three such
  lines here; the obtuse covering needs one.

`T ∩ W_sub = ∅` is strict (`notMem_sub_of_mem_inscribedTriangle`), so the
subtraction costs no null set of its own. -/
theorem obtuseWedges_ae_eq_inscribedTriangle {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    obtuseWedges R t α β γ
      =ᵐ[(volume : Measure (ℝ × ℝ))] inscribedTriangle R t α β γ := by
  rw [ae_eq_set]
  constructor
  · refine measure_mono_null ?_ (volume_chordLine (t + γ) (R * Real.cos γ))
    intro w hw
    by_contra hcon
    simp only [Set.mem_setOf_eq] at hcon
    exact hw.2 (obtuseWedges_subset_inscribedTriangle_of_ne hα0 hβ0 hγ hsum hw.1 hcon)
  · refine measure_mono_null ?_ (volume_perpLine (t + (2 * γ + 2 * α)))
    intro w hw
    by_contra hcon
    simp only [Set.mem_setOf_eq] at hcon
    exact hw.2 ⟨inscribedTriangle_subset_obtuseWedges_of_ne hα0 hβ0 hγ.le hsum hw.1 hcon,
      notMem_sub_of_mem_inscribedTriangle hw.1⟩

/-! ### The Λ-sum on an obtuse triangle

The set-level tiling above becomes the volume identity by additivity.  The one
thing worth watching is that **the subtraction never happens in `ℝ≥0∞`** — it is
carried out in `ℝ` at the very end.  Rather than computing
`Vol(W_α) + Vol(W_β) − Vol(W_sub)`, which would need truncated subtraction and a
finiteness side-condition at every step, the argument reads the partition the
other way round:

    W_α ∪ W_β  =ᵐ  T ⊔ W_sub          (disjointly)

so `Vol(W_α) + Vol(W_β) = Vol(T) + Vol(W_sub)` is a statement about **sums**, and
`Vol(T)` is recovered by cancelling the finite term `Vol(W_sub)`.  That the
union is a.e. the *disjoint* union of the two is exactly what
`wedgeAt_sub_subset_alphaBeta_of_ne` and `notMem_sub_of_mem_inscribedTriangle`
supply: containment one way, strict disjointness the other. -/

/-- **MILNOR'S Λ-SUM ON AN OBTUSE TRIANGLE.**

    Vol(chimney (inscribedTriangle R t α β γ) R)  =  Λ(α) + Λ(β) + Λ(γ)

for `π/2 < γ` — the obtuse counterpart of `hypVolume_chimney_inscribedTriangle`,
whose hypotheses are `α, β, γ < π/2`.  Together the two cover every triangle
except the right-angled one, where `γ = π/2` makes `W_sub` degenerate to a
half-plane and both statements' wedge machinery (`ψ < π/2`) fails.

`Λ(γ)` is negative here — `γ` obtuse puts `Λ(γ) = −Λ(π−γ)` with `π−γ` acute —
which is the analytic face of Milnor's "one piece enters with a minus sign".
The identity is the same one the acute case proves; only its realisation changes.

Note that no analytic continuation is used, and none of the three angles is
required to be acute in the *statement*: acuteness of `α` and `β` is derived
from `γ` obtuse via `acute_of_obtuse_third`. -/
theorem hypVolume_chimney_inscribedTriangle_obtuse {R t α β γ : ℝ} (hR : 0 < R)
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    hypVolume (chimney (inscribedTriangle R t α β γ) R)
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  obtain ⟨hα, hβ⟩ := acute_of_obtuse_third hα0 hβ0 hγ hsum
  have hπ : 0 < π := Real.pi_pos
  have hψ0 : 0 < π - γ := by linarith
  have hψ : π - γ < π / 2 := by linarith
  have mα := measurableSet_wedgeAt R (t + 2 * γ + α) α
  have mβ := measurableSet_wedgeAt R (t + 2 * γ + 2 * α + β) β
  have ms := measurableSet_wedgeAt R (t + γ + π) (π - γ)
  have mT := measurableSet_inscribedTriangle R t α β γ
  have mO := measurableSet_obtuseWedges R t α β γ
  have hUsub : ∀ w ∈ wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β,
      w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
    rintro w (hw | hw)
    · exact wedgeAt_subset_disk hα0 hα w hw
    · exact wedgeAt_subset_disk hβ0 hβ w hw
  -- (1) the union of the two surviving wedges is a.e. the DISJOINT union `T ⊔ W_sub`
  have hae : (wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β
        : Set (ℝ × ℝ))
      =ᵐ[(volume : Measure (ℝ × ℝ))]
        ((inscribedTriangle R t α β γ ∪ wedgeAt R (t + γ + π) (π - γ)) : Set (ℝ × ℝ)) := by
    rw [ae_eq_set]
    constructor
    · refine measure_mono_null ?_ (volume_chordLine (t + γ) (R * Real.cos γ))
      intro w hw
      by_contra hcon
      simp only [Set.mem_setOf_eq] at hcon
      have hmem : w ∈ obtuseWedges R t α β γ := ⟨hw.1, fun h => hw.2 (Or.inr h)⟩
      exact hw.2 (Or.inl
        (obtuseWedges_subset_inscribedTriangle_of_ne hα0 hβ0 hγ hsum hmem hcon))
    · refine measure_mono_null ?_ (volume_perpLine (t + (2 * γ + 2 * α)))
      intro w hw
      by_contra hcon
      simp only [Set.mem_setOf_eq] at hcon
      rcases hw.1 with hwT | hwS
      · exact hw.2 (inscribedTriangle_subset_obtuseWedges_of_ne hα0 hβ0 hγ.le hsum hwT hcon)
      · exact hw.2 (wedgeAt_sub_subset_alphaBeta_of_ne hα0 hβ0 hγ hsum hwS hcon)
  have hdisjW : Disjoint (wedgeAt R (t + 2 * γ + α) α)
      (wedgeAt R (t + 2 * γ + 2 * α + β) β) :=
    disjoint_wedgeAt_adjacent hα0 hα hβ0 hβ (by ring)
  have hdisjT : Disjoint (inscribedTriangle R t α β γ) (wedgeAt R (t + γ + π) (π - γ)) :=
    Set.disjoint_left.mpr fun _ hw => notMem_sub_of_mem_inscribedTriangle hw
  -- (2) additivity turns that into a statement about SUMS, never a difference
  have key : ENNReal.ofReal (Lob α) + ENNReal.ofReal (Lob β)
      = (∫⁻ w in inscribedTriangle R t α β γ,
            ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))))
        + ENNReal.ofReal (Lob (π - γ)) := by
    have h1 : (∫⁻ w in wedgeAt R (t + 2 * γ + α) α
          ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β,
          ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))))
        = ENNReal.ofReal (Lob α) + ENNReal.ofReal (Lob β) := by
      rw [lintegral_union mβ hdisjW, lintegral_wedgeAt hR hα0 hα,
        lintegral_wedgeAt hR hβ0 hβ]
    have h2 : (∫⁻ w in inscribedTriangle R t α β γ ∪ wedgeAt R (t + γ + π) (π - γ),
          ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))))
        = (∫⁻ w in inscribedTriangle R t α β γ,
              ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))))
          + ENNReal.ofReal (Lob (π - γ)) := by
      rw [lintegral_union ms hdisjT, lintegral_wedgeAt hR hψ0 hψ]
    rw [← h1, ← h2]
    exact setLIntegral_congr hae
  -- (3) the triangle's own volume, via the a.e. tiling (its vertices are ON the
  -- circle, so only an a.e. disk bound is available)
  have hTvol : hypVolume (chimney (inscribedTriangle R t α β γ) R)
      = ∫⁻ w in inscribedTriangle R t α β γ,
          ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) := by
    refine hypVolume_chimney_of_ae_lt mT ?_
    rw [Measure.restrict_congr_set
      (obtuseWedges_ae_eq_inscribedTriangle (R := R) (t := t) hα0 hβ0 hγ hsum).symm]
    exact (ae_restrict_iff' mO).mpr
      (Filter.Eventually.of_forall fun w hw => hUsub w hw.1)
  -- (4) cancel the finite `Vol(W_sub)`; the subtraction happens in ℝ, not ℝ≥0∞
  have na : 0 ≤ Lob α := Lob_nonneg_of_lt_pi_div_two hα0 hα
  have nb : 0 ≤ Lob β := Lob_nonneg_of_lt_pi_div_two hβ0 hβ
  have nc : 0 ≤ Lob (π - γ) := Lob_nonneg_of_lt_pi_div_two hψ0 hψ
  rw [← ENNReal.ofReal_add na nb] at key
  have hsub := ENNReal.sub_eq_of_eq_add ENNReal.ofReal_ne_top key
  -- `lob_sum_eq_reflected` is the corpus's own statement of Milnor's reduction;
  -- its docstring named this geometric realisation as the open step.
  rw [hTvol, lob_sum_eq_reflected hsum, show α + β = π - γ by linarith,
    ENNReal.ofReal_sub _ nc]
  exact hsub.symm

/-! ### The RIGHT-ANGLED case — `γ = π/2`, where there is nothing to subtract

The two theorems above and the acute `hypVolume_chimney_inscribedTriangle` left
exactly one slice uncovered, and this file's header used to say it "degenerates
`W_sub` to a half-plane and the `ψ < π/2` wedge machinery fails on both sides".
Half right. The machinery does fail — but not into a half-plane:

    `wedgeAt R θ (π/2) = ∅`.

Lean's `tan (π/2) = 0` (division by `cos (π/2) = 0`, the junk value), so the
wedge's second condition reads `|⟨w,v_θ⟩| < 0` and no point satisfies it. That is
not a defect of the junk value — it is geometrically right: `W_sub`'s chord
bound is `⟨w,u⟩ < R cos(π−γ) = 0` and its opening is a half-turn, so the
half-plane it would sweep is cut away by its own chord.

So at `γ = π/2` **there is nothing to subtract**, which is the analytic shadow of
`Λ(π/2) = 0`: the circumcentre sits exactly ON the hypotenuse `V₁V₂` (the
`γ`-chord is a diameter), the boundary case between inside and outside, and the
two surviving wedges tile the triangle outright.

The one step that does not survive is the `γ`-chord. Above it is extracted from
`w ∉ W_sub` (`gamma_chord_of_notMem_sub`), and with `W_sub = ∅` that hypothesis
is free and carries no information. It is replaced by the SAME two certificates,
used a third time: at `cos γ = 0` each collapses to a single term,

    perp_{t+2γ}·sin β = cos α·(γ-chord slack)      (so `w ∈ W_α` ⟹ slack > 0)
    perp_t·sin α      = −cos β·(γ-chord slack)     (so `w ∈ W_β` ⟹ slack > 0)

and the chord comes out STRICT rather than `≤`. This direction therefore needs
**no** null set at all — unlike the obtuse case, where the `≤` of
`gamma_chord_of_mem_alpha` is what forces `volume_chordLine`. -/

/-- **A half-angle of `π/2` gives the EMPTY wedge**, not a half-plane.

`Real.tan (π/2) = 0` by Lean's division-by-zero convention, so the wedge's
angular condition is `|⟨w,v_θ⟩| < 0`. -/
theorem wedgeAt_pi_div_two_eq_empty (R θ : ℝ) : wedgeAt R θ (π / 2) = ∅ := by
  ext w
  simp only [wedgeAt, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_and]
  intro _
  rw [Real.tan_pi_div_two, mul_zero]
  exact not_lt.mpr (abs_nonneg _)

/-- **The `γ`-chord for a point of `W_α`, at `γ = π/2`** — strict, and with no
appeal to `W_sub` (which is empty here).  The second certificate at `cos γ = 0`
reads `perp_{t+2γ}·sin β = cos α·(γ-chord slack)`, and `W_α`'s lower edge gives
`perp_{t+2γ} > 0`. -/
theorem gamma_chord_of_mem_alpha_right {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : γ = π / 2) (hsum : α + β + γ = π)
    {w : ℝ × ℝ} (hw : w ∈ wedgeAt R (t + 2 * γ + α) α) :
    w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ := by
  have hπ : 0 < π := Real.pi_pos
  have hα : α < π / 2 := by linarith
  have hsβ : 0 < Real.sin β := Real.sin_pos_of_pos_of_lt_pi hβ0 (by linarith)
  have hcα : 0 < Real.cos α := Real.cos_pos_of_mem_Ioo ⟨by linarith, hα⟩
  have hcγ : Real.cos γ = 0 := by rw [hγ]; exact Real.cos_pi_div_two
  have hlo : 0 < -(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ) := by
    have h := wedgeAt_lower hα0 hα w hw
    rwa [show t + 2 * γ + α - α = t + 2 * γ by ring] at h
  have hcert := perp_second_certificate (R := R) (t := t) hsum w
  rw [hcγ] at hcert ⊢
  rw [mul_zero]
  nlinarith [mul_pos hlo hsβ]

/-- **The `γ`-chord for a point of `W_β`, at `γ = π/2`** — the mirror, from the
FIRST certificate and `W_β`'s upper edge (`perp_t < 0` after the `2π` shift). -/
theorem gamma_chord_of_mem_beta_right {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : γ = π / 2) (hsum : α + β + γ = π)
    {w : ℝ × ℝ} (hw : w ∈ wedgeAt R (t + 2 * γ + 2 * α + β) β) :
    w.1 * Real.cos (t + γ) + w.2 * Real.sin (t + γ) < R * Real.cos γ := by
  have hπ : 0 < π := Real.pi_pos
  have hβ : β < π / 2 := by linarith
  have hsα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  have hcβ : 0 < Real.cos β := Real.cos_pos_of_mem_Ioo ⟨by linarith, hβ⟩
  have hcγ : Real.cos γ = 0 := by rw [hγ]; exact Real.cos_pi_div_two
  have hup : -(w.1 * Real.sin t) + w.2 * Real.cos t < 0 := by
    have h := wedgeAt_upper hβ0 hβ w hw
    rwa [show t + 2 * γ + 2 * α + β + β = t + 2 * π by linarith,
      Real.sin_add_two_pi, Real.cos_add_two_pi] at h
  have hcert := perp_start_certificate (R := R) (t := t) hsum w
  rw [hcγ] at hcert ⊢
  rw [mul_zero]
  nlinarith [mul_pos (neg_pos.mpr hup) hsα]

/-- **THE RIGHT-ANGLED TILING.**  At `γ = π/2` the triangle is a.e. the union of
the two surviving wedges — no subtraction, and only ONE null set (the single edge
line the covering needs), because both chord directions are strict here. -/
theorem union_ae_eq_inscribedTriangle_right {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : γ = π / 2) (hsum : α + β + γ = π) :
    (wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β
        : Set (ℝ × ℝ))
      =ᵐ[(volume : Measure (ℝ × ℝ))] inscribedTriangle R t α β γ := by
  have hπ : 0 < π := Real.pi_pos
  have hα : α < π / 2 := by linarith
  have hβ : β < π / 2 := by linarith
  rw [ae_eq_set]
  constructor
  · -- `W_α ∪ W_β ⊆ T` is STRICT here: each wedge supplies its own chord, its
    -- neighbour's by `wedgeAt_lt_chord_next`/`_prev`, and the γ-chord by the
    -- certificates above.
    refine measure_mono_null (fun w hw => absurd ?_ hw.2) measure_empty
    rcases hw.1 with hwα | hwβ
    · refine ⟨⟨gamma_chord_of_mem_alpha_right hα0 hβ0 hγ hsum hwα, hwα.1⟩, ?_⟩
      have h := wedgeAt_lt_chord_next hα0 hα hβ0 hβ w hwα
      rwa [show t + 2 * γ + α + α + β = t + 2 * γ + 2 * α + β by ring] at h
    · refine ⟨⟨gamma_chord_of_mem_beta_right hα0 hβ0 hγ hsum hwβ, ?_⟩, hwβ.1⟩
      have h := wedgeAt_lt_chord_prev hβ0 hβ hα0 hα w hwβ
      rwa [show t + 2 * γ + 2 * α + β - β - α = t + 2 * γ + α by ring] at h
  · refine measure_mono_null ?_ (volume_perpLine (t + (2 * γ + 2 * α)))
    intro w hw
    by_contra hcon
    simp only [Set.mem_setOf_eq] at hcon
    exact hw.2 (inscribedTriangle_subset_obtuseWedges_of_ne hα0 hβ0
      (le_of_eq hγ.symm) hsum hw.1 hcon)

/-- **MILNOR'S Λ-SUM ON A RIGHT-ANGLED TRIANGLE.**  `Λ(π/2) = 0`, so the
identity is just the two wedge volumes — which is what "nothing to subtract"
means analytically. -/
theorem hypVolume_chimney_inscribedTriangle_right {R t α β γ : ℝ} (hR : 0 < R)
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : γ = π / 2) (hsum : α + β + γ = π) :
    hypVolume (chimney (inscribedTriangle R t α β γ) R)
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  have hπ : 0 < π := Real.pi_pos
  have hα : α < π / 2 := by linarith
  have hβ : β < π / 2 := by linarith
  have mα := measurableSet_wedgeAt R (t + 2 * γ + α) α
  have mβ := measurableSet_wedgeAt R (t + 2 * γ + 2 * α + β) β
  have hae := union_ae_eq_inscribedTriangle_right (R := R) (t := t) hα0 hβ0 hγ hsum
  have hUsub : ∀ w ∈ wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β,
      w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
    rintro w (hw | hw)
    · exact wedgeAt_subset_disk hα0 hα w hw
    · exact wedgeAt_subset_disk hβ0 hβ w hw
  have hres : (volume : Measure (ℝ × ℝ)).restrict (inscribedTriangle R t α β γ)
      = (volume : Measure (ℝ × ℝ)).restrict
          (wedgeAt R (t + 2 * γ + α) α ∪ wedgeAt R (t + 2 * γ + 2 * α + β) β) :=
    Measure.restrict_congr_set hae.symm
  rw [hypVolume_chimney_of_ae_lt (measurableSet_inscribedTriangle R t α β γ)
      (by rw [hres]
          exact (ae_restrict_iff' (mα.union mβ)).mpr
            (Filter.Eventually.of_forall hUsub)),
    setLIntegral_congr hae.symm,
    lintegral_union mβ (disjoint_wedgeAt_adjacent hα0 hα hβ0 hβ (by ring)),
    lintegral_wedgeAt hR hα0 hα, lintegral_wedgeAt hR hβ0 hβ,
    ← ENNReal.ofReal_add (Lob_nonneg_of_lt_pi_div_two hα0 hα)
      (Lob_nonneg_of_lt_pi_div_two hβ0 hβ),
    show Lob α + Lob β + Lob γ = Lob α + Lob β by rw [hγ, Lob_pi_div_two]; ring]

/-- **MILNOR'S IDENTITY FOR A RIGHT-ANGLED IDEAL TETRAHEDRON**, on the
vertex-defined region.  With this the acute, obtuse and right-angled theorems
cover the WHOLE open angle simplex. -/
theorem idealTetVolume_of_vertices_right {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : γ = π / 2) (hsum : α + β + γ = π) :
    hypVolume (idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)))
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  have hγ0 : 0 < γ := by rw [hγ]; positivity
  rw [idealTet_eq_chimney hα0 hβ0 hγ0 hsum]
  exact hypVolume_chimney_inscribedTriangle_right (by norm_num) hα0 hβ0 hγ hsum

/-! ### The obtuse case of Milnor's identity

The chimney statement above becomes a statement about an **ideal tetrahedron**
through `idealTet_eq_chimney`, which identifies the vertex-defined region (an
intersection of four geodesic half-spaces) with the chimney over the inscribed
triangle.

That theorem used to carry `α, β, γ < π/2`, and this file's own header named it
as the reason the obtuse case stayed open — a *set* equality, which no
continuation argument can supply.  **Those hypotheses were unused.**  They were
spent only inside `Real.sin_pos_of_pos_of_lt_pi` side goals of the form `X < π`,
which `α + β + γ = π` already gives from the positivity of the other two; the
whole chain — `inscribedTriangle_vertex_incidence`, `face1`/`face2`/`face3`,
`idealTet_eq_chimney` — is acuteness-free once they are dropped.

So the gate was inherited, not real, and the obtuse case closes here. -/

/-- **MILNOR'S IDENTITY FOR AN OBTUSE IDEAL TETRAHEDRON.**

    Vol(idealTetrahedron P₁ P₂ P₃) = Λ(α) + Λ(β) + Λ(γ)      (π/2 < γ)

the obtuse counterpart of `idealTetVolume_of_vertices`.  The region is the
independently-defined one — the intersection of four geodesic half-spaces built
from the four ideal vertices — not a chimney by fiat.

Together with the acute theorem this covers **every** admissible triple except
the right-angled one, where `γ = π/2` degenerates the subtracted wedge to a
half-plane and the `ψ < π/2` wedge machinery fails on both sides.

`Λ(γ) < 0` here, which is Milnor's "one piece enters with a minus sign"; the
subtraction is realised set-theoretically by `obtuseWedges_ae_eq_inscribedTriangle`
and is carried out in `ℝ`, never in `ℝ≥0∞`.

Closed modulo the same single cited totally-geodesic / normalized-position
identification the acute theorem rests on (File A1's `geodesicPlaneThrough` — a
definition with a citation, not an axiom or `sorry`).  No analytic continuation
is used anywhere, and acuteness of `α` and `β` is derived rather than assumed. -/
theorem idealTetVolume_of_vertices_obtuse {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 < γ) (hsum : α + β + γ = π) :
    hypVolume (idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)))
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  have hγ0 : 0 < γ := lt_trans (by positivity) hγ
  rw [idealTet_eq_chimney hα0 hβ0 hγ0 hsum]
  exact hypVolume_chimney_inscribedTriangle_obtuse (by norm_num) hα0 hβ0 hγ hsum

/-! ### MILNOR'S THEOREM, unconditional — and the gap in "covers the whole simplex"

The three cases above are stated with `γ` as the distinguished angle. A triple
whose non-acute angle is `α` or `β` satisfies none of them as written, so
"every admissible triple is covered" was, strictly, a claim about a relabelling
step that had not been taken. This section takes it.

The relabelling is exact rather than approximate, because the three vertices are
literally the same points. With `α + β + γ = π`,

    Region(α,β,γ) at `t`   has vertices  t, t+2γ, t+2γ+2α
    Region(β,γ,α) at `t+2γ`     "        t+2γ, t+2γ+2α, t+2γ+2α+2β = t+2π

and `t + 2π` is `t` on the circle. So a cyclic relabel of the angles, together
with the matching shift of the base angle, names the *same* ideal tetrahedron —
provided `idealTetrahedron` does not care about the order of its three vertices,
which is `idealTetrahedron_cyclic` below. `Λ(α)+Λ(β)+Λ(γ)` is symmetric outright.

The whole thing rests on one observation: `verticalHalfSpaceThrough b c i` is a
product of two signed areas sharing the edge `b c`, so swapping `b` and `c`
negates both and changes nothing. -/

/-- **The oriented half-space does not care which end of its edge is first.**
Both factors of `sarea b c i * sarea b c (p 0, p 1)` flip under the swap. -/
theorem verticalHalfSpaceThrough_swap (b c i : ℝ × ℝ) :
    verticalHalfSpaceThrough c b i = verticalHalfSpaceThrough b c i := by
  ext p
  simp only [verticalHalfSpaceThrough, Set.mem_setOf_eq, sarea_swap b c i,
    sarea_swap b c (p 0, p 1), neg_mul_neg]

/-- **The ideal tetrahedron is invariant under cycling its vertices.**  Its three
vertical faces are the same three half-spaces, listed in a different order, once
`verticalHalfSpaceThrough_swap` is used to align the two that appear with their
edge reversed. -/
theorem idealTetrahedron_cyclic (P₁ P₂ P₃ : ℝ × ℝ) :
    idealTetrahedron P₂ P₃ P₁ = idealTetrahedron P₁ P₂ P₃ := by
  simp only [idealTetrahedron, verticalHalfSpaceThrough_swap P₁ P₃ P₂,
    verticalHalfSpaceThrough_swap P₁ P₂ P₃]
  ext p
  simp only [Set.mem_inter_iff]
  tauto

/-- `circlePoint` is `2π`-periodic — the step that turns the third relabelled
vertex `t + 2γ + 2α + 2β` back into the first. -/
theorem circlePoint_add_two_pi (R a : ℝ) :
    circlePoint R (a + 2 * π) = circlePoint R a := by
  simp [circlePoint, Real.cos_add_two_pi, Real.sin_add_two_pi]

/-- **The non-acute case in one statement** — obtuse and right-angled together,
`π/2 ≤ γ`. -/
theorem idealTetVolume_of_vertices_nonacute {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ : π / 2 ≤ γ) (hsum : α + β + γ = π) :
    hypVolume (idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)))
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  rcases eq_or_lt_of_le hγ with h | h
  · exact idealTetVolume_of_vertices_right hα0 hβ0 h.symm hsum
  · exact idealTetVolume_of_vertices_obtuse hα0 hβ0 h hsum

/-- **MILNOR'S IDENTITY, UNCONDITIONAL.**

    Vol(idealTetrahedron P₁ P₂ P₃) = Λ(α) + Λ(β) + Λ(γ)

for EVERY positive triple summing to `π` — no acuteness, no distinguished angle,
no case hypothesis at all.  The region is the independently-defined one (four
geodesic half-spaces from the four ideal vertices).

The proof is a four-way split.  All three acute is
`MostowIdealTetVolume.idealTetVolume_of_vertices` (File A4).  `γ` non-acute is
`idealTetVolume_of_vertices_nonacute`.  The other two are that same theorem after
a cyclic relabel, which `idealTetrahedron_cyclic` and `circlePoint_add_two_pi`
show is the identity on the region.  `at_most_one_obtuse` is not needed: the
split is by cases rather than by exclusion, and a triple with two non-acute
angles simply lands in a branch whose hypotheses `linarith` refutes.

Closed modulo the single cited totally-geodesic / normalized-position
identification (File A1's `geodesicPlaneThrough`), which the acute theorem
already rested on; the non-acute cases add nothing to it. -/
theorem idealTetVolume_of_vertices_unconditional {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ) (hsum : α + β + γ = π) :
    hypVolume (idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)))
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  rcases le_or_gt (π / 2) γ with hγ | hγ
  · exact idealTetVolume_of_vertices_nonacute hα0 hβ0 hγ hsum
  rcases le_or_gt (π / 2) α with hα | hα
  · -- relabel `(α,β,γ) ↦ (β,γ,α)` and shift the base angle to `t + 2γ`
    have hregion : idealTetrahedron (circlePoint 1 (t + 2 * γ))
          (circlePoint 1 (t + 2 * γ + 2 * α))
          (circlePoint 1 (t + 2 * γ + 2 * α + 2 * β))
        = idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
            (circlePoint 1 (t + 2 * γ + 2 * α)) := by
      rw [show t + 2 * γ + 2 * α + 2 * β = t + 2 * π by linarith,
        circlePoint_add_two_pi]
      exact idealTetrahedron_cyclic _ _ _
    have := idealTetVolume_of_vertices_nonacute (t := t + 2 * γ) (α := β)
      (β := γ) (γ := α) hβ0 hγ0 hα (by linarith)
    rw [hregion] at this
    rw [this]; ring_nf
  rcases le_or_gt (π / 2) β with hβ | hβ
  · -- relabel twice: `(α,β,γ) ↦ (γ,α,β)`, base angle `t + 2γ + 2α`
    have hregion : idealTetrahedron (circlePoint 1 (t + 2 * γ + 2 * α))
          (circlePoint 1 (t + 2 * γ + 2 * α + 2 * β))
          (circlePoint 1 (t + 2 * γ + 2 * α + 2 * β + 2 * γ))
        = idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
            (circlePoint 1 (t + 2 * γ + 2 * α)) := by
      rw [show t + 2 * γ + 2 * α + 2 * β = t + 2 * π by linarith,
        show t + 2 * π + 2 * γ = (t + 2 * γ) + 2 * π by ring,
        circlePoint_add_two_pi, circlePoint_add_two_pi]
      rw [idealTetrahedron_cyclic, idealTetrahedron_cyclic]
    have := idealTetVolume_of_vertices_nonacute (t := t + 2 * γ + 2 * α) (α := γ)
      (β := α) (γ := β) hγ0 hα0 hβ (by linarith)
    rw [hregion] at this
    rw [this]; ring_nf
  · -- all three acute
    exact MostowIdealTetVolume.idealTetVolume_of_vertices hα0 hβ0 hγ0 hα hβ hγ hsum

end QOU.Archimedean.HyperbolicVolume
