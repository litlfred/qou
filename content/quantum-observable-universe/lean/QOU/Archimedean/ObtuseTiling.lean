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

end QOU.Archimedean.HyperbolicVolume
