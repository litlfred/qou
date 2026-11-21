/-
  H4-5b: the WEDGE PAIR — two orthoschemes make a Λ.

      H4-3/H4-4   Vol(chimney (orthoBase R ψ) R)  =  ½ Λ(ψ)        [#4842]
      H4-5b       Vol(chimney (wedge R ψ) R)      =    Λ(ψ)        [HERE]

  `wedge R ψ` is the ISOCELES triangle with apex at the circumcentre, apex
  angle `2ψ`, and its two far vertices ON the circle of radius `R` — one of the
  three pieces the inscribed triangle is cut into by joining the circumcentre
  to the vertices.  The perpendicular from the apex to the opposite chord
  bisects it, and the two halves are `orthoBase R ψ` and its mirror image.

  WHY THIS IS THE STEP THAT PRODUCES A WHOLE `Λ`.  Milnor's subdivision cuts
  an inscribed triangle into SIX orthoschemes, which pair up into three
  wedges; each pair contributes `2 · ½Λ = Λ`.  This file is exactly that
  pairing, done once and for the wedge on the positive-`x` axis.  The factor
  `2` is the mirror symmetry, and it is proved (via measure-preservation of
  `(x,y) ↦ (x,−y)`) rather than asserted by symmetry hand-wave.

  THE DECOMPOSITION IS EXACT, NOT A.E.  `wedge` splits as the disjoint union

      orthoBase  ⊔  (reflection ⁻¹' orthoBase)  ⊔  (the open segment y = 0),

  by the sign of `y`.  The middle segment is a genuine part of the open wedge,
  not an artefact: it is where the perpendicular meets the interior.  It is a
  null set (`wedgeSpine_null`), so it contributes nothing — but it is carried
  explicitly rather than quietly dropped.

  WHAT IS NOT CLAIMED.  Still no ideal tetrahedron, still no triangle
  inscribed in the circle.  `hypVolume_chimney_wedge` is a statement about a
  region of `H³` over one Euclidean isoceles triangle.  Assembling three
  wedges at three different axes into `Λ(α)+Λ(β)+Λ(γ)` is H4-5c and is OPEN;
  it needs rotation-invariance of the base integral, which is NOT proved here
  (see the bean, and `qou-w3eg`).

  ON THE OBTUSE CASE — a correction of scope, recorded here because this file
  is where the pairing lives.  Milnor subdivides from the circumcentre only
  "if all three angles are acute", and the corpus has carried that restriction
  as though the RESULT were in doubt for obtuse triangles.  Numerically it is
  not: `Λ(α)+Λ(β)+Λ(γ)` reproduces the base integral over the inscribed
  triangle to `~1e-17` for obtuse triangles and for the right-triangle
  boundary `α = π/2`, the same as for acute ones.  What degenerates in the
  obtuse case is the SUBDIVISION ARGUMENT (the circumcentre leaves the
  triangle and one wedge must enter with a minus sign), not the identity.
  This is a scope-(a) observation about a proof route, not a scope-(b)
  exclusion of anything.

  Archimedean (ℝ): `cos`, `tan`, `abs`, Lebesgue measure, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-5), qou-5gai (H4)
-/

import QOU.Archimedean.OrthoschemePolarReduction

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. Reflection in the `x`-axis

The mirror symmetry that pairs the two halves of a wedge.  It is used twice:
to identify the lower half of the wedge with a preimage of `orthoBase`, and to
transport the integral across.  Both need it to be MEASURE-PRESERVING, which
is where `volume`'s neg-invariance on `ℝ` enters. -/

/-- Reflection in the `x`-axis, as a measurable equivalence. -/
noncomputable def reflY : (ℝ × ℝ) ≃ᵐ (ℝ × ℝ) :=
  MeasurableEquiv.prodCongr (MeasurableEquiv.refl ℝ) (MeasurableEquiv.neg ℝ)

@[simp] theorem reflY_apply (w : ℝ × ℝ) : reflY w = (w.1, -w.2) := rfl

/-- Reflection preserves Lebesgue measure on the plane: the identity on the
first factor, negation on the second, and `volume` on `ℝ` is neg-invariant. -/
theorem measurePreserving_reflY :
    MeasurePreserving reflY (volume : Measure (ℝ × ℝ)) (volume : Measure (ℝ × ℝ)) := by
  have h : MeasurePreserving (Prod.map (id : ℝ → ℝ) (Neg.neg : ℝ → ℝ))
      ((volume : Measure ℝ).prod (volume : Measure ℝ))
      ((volume : Measure ℝ).prod (volume : Measure ℝ)) :=
    (MeasurePreserving.id (volume : Measure ℝ)).prod
      (Measure.measurePreserving_neg (volume : Measure ℝ))
  rw [Measure.volume_eq_prod]
  exact h

/-! ### 2. The wedge, and its split by the sign of `y`

The definition is Cartesian, as `orthoBase`'s is, and for the same reason: a
polar definition would assume the description the computation consumes. -/

/-- **The isoceles wedge** — the OPEN Euclidean triangle with apex at the
origin (the circumcentre), apex angle `2ψ`, and its two far vertices
`(R cos ψ, ± R sin ψ)` on the circle of radius `R`.

One of the three pieces an inscribed triangle is cut into by joining the
circumcentre to its vertices. -/
def wedge (R ψ : ℝ) : Set (ℝ × ℝ) :=
  {w | w.1 < R * Real.cos ψ ∧ |w.2| < w.1 * Real.tan ψ}

/-- **The spine** — where the perpendicular from the apex meets the wedge's
interior.  A genuine part of the open wedge, and the reason the split below
has three pieces rather than two. -/
def wedgeSpine (R ψ : ℝ) : Set (ℝ × ℝ) := Ioo 0 (R * Real.cos ψ) ×ˢ ({0} : Set ℝ)

theorem isOpen_wedge (R ψ : ℝ) : IsOpen (wedge R ψ) := by
  have h₁ : IsOpen {w : ℝ × ℝ | w.1 < R * Real.cos ψ} := isOpen_lt continuous_fst continuous_const
  have h₂ : IsOpen {w : ℝ × ℝ | |w.2| < w.1 * Real.tan ψ} :=
    isOpen_lt continuous_snd.abs (continuous_fst.mul continuous_const)
  simpa [wedge, Set.setOf_and] using h₁.inter h₂

theorem measurableSet_wedge (R ψ : ℝ) : MeasurableSet (wedge R ψ) :=
  (isOpen_wedge R ψ).measurableSet

theorem measurableSet_wedgeSpine (R ψ : ℝ) : MeasurableSet (wedgeSpine R ψ) :=
  measurableSet_Ioo.prod (measurableSet_singleton 0)

/-- The spine is null — a segment in the plane. -/
theorem wedgeSpine_null (R ψ : ℝ) : (volume : Measure (ℝ × ℝ)) (wedgeSpine R ψ) = 0 := by
  rw [wedgeSpine, Measure.volume_eq_prod, Measure.prod_prod, Real.volume_singleton, mul_zero]

/-- Every point of the wedge has positive abscissa.  Not an extra hypothesis:
`|y| < x tan ψ` forces `x tan ψ > 0`, and `tan ψ > 0` on `(0, π/2)`. -/
theorem wedge_fst_pos {R ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) {w : ℝ × ℝ}
    (hw : w ∈ wedge R ψ) : 0 < w.1 := by
  have htan : 0 < Real.tan ψ := Real.tan_pos_of_pos_of_lt_pi_div_two hψ0 hψ
  have h : 0 < w.1 * Real.tan ψ := lt_of_le_of_lt (abs_nonneg _) hw.2
  by_contra hle
  push_neg at hle
  nlinarith

/-- **The wedge splits, exactly, by the sign of `y`.**

    wedge  =  orthoBase  ∪  (reflY ⁻¹' orthoBase)  ∪  spine

Not an a.e. statement: this is a genuine partition of the open wedge into its
upper half, its lower half, and the spine between them. -/
theorem wedge_eq_union {R ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    wedge R ψ = orthoBase R ψ ∪ (reflY ⁻¹' orthoBase R ψ) ∪ wedgeSpine R ψ := by
  have htan : 0 < Real.tan ψ := Real.tan_pos_of_pos_of_lt_pi_div_two hψ0 hψ
  ext w
  constructor
  · intro hw
    have hx : 0 < w.1 := wedge_fst_pos hψ0 hψ hw
    obtain ⟨hxlt, habs⟩ := hw
    rcases lt_trichotomy w.2 0 with hy | hy | hy
    · -- lower half
      refine Or.inl (Or.inr ?_)
      rw [Set.mem_preimage, reflY_apply]
      refine ⟨hx, hxlt, by simpa using hy, ?_⟩
      show -w.2 < w.1 * Real.tan ψ
      rwa [abs_of_neg hy] at habs
    · -- the spine
      exact Or.inr ⟨Set.mem_Ioo.mpr ⟨hx, hxlt⟩, hy⟩
    · -- upper half
      refine Or.inl (Or.inl ⟨hx, hxlt, hy, ?_⟩)
      rwa [abs_of_pos hy] at habs
  · rintro ((⟨hx, hxlt, hy, hylt⟩ | hlow) | ⟨hspine, hy0⟩)
    · exact ⟨hxlt, by rwa [abs_of_pos hy]⟩
    · rw [Set.mem_preimage, reflY_apply] at hlow
      obtain ⟨hx, hxlt, hy, hylt⟩ := hlow
      refine ⟨hxlt, ?_⟩
      have hy' : w.2 < 0 := by simpa using hy
      rwa [abs_of_neg hy']
    · obtain ⟨hx, hxlt⟩ := Set.mem_Ioo.mp hspine
      have : w.2 = 0 := hy0
      refine ⟨hxlt, ?_⟩
      rw [this, abs_zero]
      positivity

/-! ### 3. The two halves carry equal mass

The mirror image of `orthoBase` has the same base integral, because the
integrand depends on `y` only through `y²` and reflection preserves the
measure.  Proved, not waved at. -/

/-- **The lower half of the wedge carries the same base integral as the
upper.**  This is the `2` in `2 · ½Λ = Λ`. -/
theorem lintegral_reflY_orthoBase {R ψ : ℝ} :
    ∫⁻ w in reflY ⁻¹' orthoBase R ψ, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2)))
      = ∫⁻ w in orthoBase R ψ, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) := by
  set g : ℝ × ℝ → ENNReal :=
    fun w => ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) with hg
  -- the integrand is reflection-invariant: it sees `y` only as `y²`
  have hinv : ∀ w : ℝ × ℝ, g (reflY w) = g w := by
    intro w
    simp [hg, reflY_apply]
  calc ∫⁻ w in reflY ⁻¹' orthoBase R ψ, g w
      = ∫⁻ w in reflY ⁻¹' orthoBase R ψ, g (reflY w) := by
        exact (lintegral_congr fun w => hinv w).symm
    _ = ∫⁻ w in orthoBase R ψ, g w :=
        measurePreserving_reflY.setLIntegral_comp_preimage_emb
          reflY.measurableEmbedding g (orthoBase R ψ)

/-! ### 4. `Λ` is non-negative below `π/2`

Needed to add two `ENNReal.ofReal`s: `ofReal` is only additive on non-negative
reals.  It is not a fact about `Λ` pulled from outside — it falls out of the
orthoscheme integral already proved, whose integrand is non-negative on the
whole closed interval (`log u ≤ 0` for `u ∈ [0,1]`, and `u = 0` at the
endpoint, where Lean's `log 0 = 0` makes the bound hold rather than fail). -/

/-- **`0 ≤ Λ(ψ)` for `ψ ∈ (0, π/2)`** — read off `integral_orthoscheme`. -/
theorem Lob_nonneg_of_lt_pi_div_two {ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    0 ≤ Lob ψ := by
  have hπ : 0 < π := Real.pi_pos
  have hnn : ∀ φ ∈ Set.Icc (0:ℝ) ψ, 0 ≤ (-(1/4 : ℝ)) *
      Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2) := by
    intro φ hφ
    obtain ⟨hφ0, hφψ⟩ := hφ
    have hcosφ : 0 < Real.cos φ := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
    have hcosle : Real.cos ψ ≤ Real.cos φ :=
      Real.cos_le_cos_of_nonneg_of_le_pi hφ0 (by linarith) hφψ
    have hcosψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
    have hu0 : 0 ≤ (Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2 :=
      div_nonneg (by nlinarith) (by positivity)
    have hu1 : (Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2 ≤ 1 := by
      rw [div_le_one (by positivity)]
      nlinarith
    have hlog := Real.log_nonpos hu0 hu1
    nlinarith
  have h := intervalIntegral.integral_nonneg (μ := volume) hψ0.le hnn
  rw [integral_orthoscheme hψ0 hψ] at h
  linarith

/-! ### 5. H4-5b — the wedge value -/

/-- The wedge lies strictly inside the disk.

`|y| < x tan ψ` and `x < R cos ψ` give `x² + y² < x²(1 + tan²ψ) = x²/cos²ψ < R²`.
Its two far vertices are ON the circle, but the wedge is open.

No `0 < R` hypothesis: for `R ≤ 0` the wedge is empty (`0 < x < R cos ψ` is
unsatisfiable) and the statement holds vacuously. -/
theorem wedge_subset_disk {R ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∀ w ∈ wedge R ψ, w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
  intro w hw
  have hπ : 0 < π := Real.pi_pos
  have hx : 0 < w.1 := wedge_fst_pos hψ0 hψ hw
  obtain ⟨hxlt, habs⟩ := hw
  have hcosψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hpyth := Real.sin_sq_add_cos_sq ψ
  rw [Real.tan_eq_sin_div_cos] at habs
  -- `|y| cos ψ < x sin ψ`
  have hy' : |w.2| * Real.cos ψ < w.1 * Real.sin ψ := by
    rw [show w.1 * (Real.sin ψ / Real.cos ψ) = w.1 * Real.sin ψ / Real.cos ψ by ring,
      lt_div_iff₀ hcosψ] at habs
    exact habs
  have habs2 : |w.2| ^ 2 = w.2 ^ 2 := sq_abs w.2
  have hsq : w.2 ^ 2 * Real.cos ψ ^ 2 < w.1 ^ 2 * Real.sin ψ ^ 2 := by
    have h := mul_self_lt_mul_self (by positivity : (0:ℝ) ≤ |w.2| * Real.cos ψ) hy'
    nlinarith [h, habs2]
  have hx2 : w.1 ^ 2 < R ^ 2 * Real.cos ψ ^ 2 := by nlinarith
  nlinarith [hsq, hx2, hpyth, sq_nonneg (Real.cos ψ)]

/-- **H4-5b — the base integral over one wedge is `Λ(ψ)`.**

Two orthoschemes, mirror images of each other, plus a null spine. -/
theorem lintegral_wedge {R ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∫⁻ w in wedge R ψ, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2)))
      = ENNReal.ofReal (Lob ψ) := by
  set g : ℝ × ℝ → ENNReal :=
    fun w => ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) with hg
  have hup : MeasurableSet (orthoBase R ψ) := measurableSet_orthoBase R ψ
  have hlow : MeasurableSet (reflY ⁻¹' orthoBase R ψ) := reflY.measurable hup
  have hspine : MeasurableSet (wedgeSpine R ψ) := measurableSet_wedgeSpine R ψ
  -- the two halves are disjoint (opposite signs of `y`), and both miss the spine
  have hdisj₁ : Disjoint (orthoBase R ψ) (reflY ⁻¹' orthoBase R ψ) := by
    rw [Set.disjoint_left]
    rintro w ⟨-, -, hy, -⟩ hw'
    rw [Set.mem_preimage, reflY_apply] at hw'
    have : (0:ℝ) < -w.2 := hw'.2.2.1
    linarith
  have hdisj₂ : Disjoint (orthoBase R ψ ∪ reflY ⁻¹' orthoBase R ψ) (wedgeSpine R ψ) := by
    rw [Set.disjoint_left]
    rintro w (⟨-, -, hy, -⟩ | hw') ⟨-, hy0⟩
    · have hz : w.2 = 0 := Set.mem_singleton_iff.mp hy0
      linarith
    · rw [Set.mem_preimage, reflY_apply] at hw'
      have hneg : (0:ℝ) < -w.2 := hw'.2.2.1
      have hz : w.2 = 0 := Set.mem_singleton_iff.mp hy0
      linarith
  rw [wedge_eq_union hψ0 hψ,
    lintegral_union hspine hdisj₂,
    lintegral_union hlow hdisj₁,
    lintegral_reflY_orthoBase,
    setLIntegral_measure_zero _ _ (wedgeSpine_null R ψ),
    add_zero]
  -- two copies of `½Λ(ψ)`
  have hLnn : (0:ℝ) ≤ Lob ψ / 2 := by
    have := Lob_nonneg_of_lt_pi_div_two hψ0 hψ
    linarith
  rw [← hypVolume_chimney_of_subset_disk hup (orthoBase_subset_disk hR hψ0 hψ),
    hypVolume_chimney_orthoBase hR hψ0 hψ,
    ← ENNReal.ofReal_add hLnn hLnn]
  congr 1
  ring

/-- **The hyperbolic volume of the chimney over one wedge is `Λ(ψ)`.**

The pairing step of Milnor's subdivision, in three dimensions: two mirror
orthoschemes at `½Λ(ψ)` each.  Three such wedges, at three different axes and
with `ψ` the three inscribed angles, would give `Λ(α)+Λ(β)+Λ(γ)` — that
assembly is H4-5c and is OPEN, because moving a wedge off the positive `x`-axis
needs rotation-invariance of the base integral, which is not proved here.

**Still not a statement about an ideal tetrahedron.** -/
theorem hypVolume_chimney_wedge {R ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    hypVolume (chimney (wedge R ψ) R) = ENNReal.ofReal (Lob ψ) := by
  rw [hypVolume_chimney_of_subset_disk (measurableSet_wedge R ψ)
      (wedge_subset_disk hψ0 hψ),
    lintegral_wedge hR hψ0 hψ]

end QOU.Archimedean.HyperbolicVolume
