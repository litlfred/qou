/-
  H4-5c-i: ROTATION INVARIANCE — the wedge at an arbitrary axis.

      H4-5b   Vol(chimney (wedge R ψ) R)          =  Λ(ψ)     [positive x-axis]
      H4-5c-i Vol(chimney (wedgeAt R θ ψ) R)      =  Λ(ψ)     [any axis θ]

  This is the piece H4-5b named as its blocker.  Milnor's subdivision produces
  three wedges at three DIFFERENT axes; H4-5b evaluates one wedge, but only on
  the positive `x`-axis, because that is where `orthoBase` sits.  Moving it off
  that axis is what this file supplies.

  WHY A DETERMINANT AND NOT AN ISOMETRY.  `ℝ × ℝ` carries the PRODUCT (sup)
  norm, not the Euclidean one, so a rotation is *not* a `LinearIsometryEquiv`
  here and the inner-product-space volume lemmas do not apply.  What is true —
  and is all that volume needs — is that `det = 1`, which is norm-independent.
  So the route is `Measure.map_linearMap_addHaar_eq_smul_addHaar` with
  `det_rotL`, computed through `Module.Basis.finTwoProd` as `cos²θ + sin²θ`.

  THE DEFINITION IS CARTESIAN, as `orthoBase`'s and `wedge`'s are, and for the
  same reason: defining `wedgeAt` as `rotL θ '' wedge` would make the rotation
  a definition rather than a theorem, and the whole point of this file is that
  the rotation is where the content is.  `wedgeAt R θ ψ` is cut out by dot
  products against the rotated frame

      u = (cos θ, sin θ),   v = (−sin θ, cos θ),

  and `wedgeAt_eq_image` is the THEOREM that this is the rotated wedge.  It
  rests on `inner_u_rot` / `inner_v_rot`: rotating by `θ` and then projecting
  onto the `θ`-frame returns the original coordinates.

  WHAT THIS FILE DOES *NOT* DO.  It does not perform Milnor's subdivision —
  that a triangle INSCRIBED in the circle is the union, up to null sets, of
  three `wedgeAt`s whose half-angles are its three inscribed angles and whose
  axes point at the three side-midpoints.  This file removes the
  infrastructural obstacle in front of that step; the step itself is
  `QOU.Archimedean.OrthoschemeTiling`
  (`milnorWedges_ae_eq_inscribedTriangle`, H4-5c-ii(b)), with the Λ-sum on the
  union in `QOU.Archimedean.OrthoschemeLambdaSum` (H4-5c-ii(a)).  Nothing here,
  or there, is a statement about ideal tetrahedra.

  Archimedean (ℝ): `cos`, `sin`, Lebesgue measure, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-5), qou-5gai (H4)
-/

import QOU.Archimedean.OrthoschemeWedgePair

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. Rotation as a linear map, and its determinant -/

/-- **Rotation of the plane by `θ`**, as an `ℝ`-linear map. -/
noncomputable def rotL (θ : ℝ) : (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) where
  toFun w := (w.1 * Real.cos θ - w.2 * Real.sin θ, w.1 * Real.sin θ + w.2 * Real.cos θ)
  map_add' := by intro a b; simp [Prod.ext_iff]; constructor <;> ring
  map_smul' := by intro c a; simp [Prod.ext_iff]; constructor <;> ring

@[simp] theorem rotL_apply (θ : ℝ) (w : ℝ × ℝ) :
    rotL θ w = (w.1 * Real.cos θ - w.2 * Real.sin θ, w.1 * Real.sin θ + w.2 * Real.cos θ) :=
  rfl

/-- **`det(rot θ) = 1`** — the Pythagorean identity, and the only fact about
rotation that Lebesgue measure cares about. -/
theorem det_rotL (θ : ℝ) : LinearMap.det (rotL θ) = 1 := by
  rw [← LinearMap.det_toMatrix (Module.Basis.finTwoProd ℝ), Matrix.det_fin_two]
  simp [LinearMap.toMatrix_apply, rotL]
  nlinarith [Real.sin_sq_add_cos_sq θ]

/-- Rotating by `θ` and then by `−θ` is the identity. -/
theorem rotL_neg_rotL (θ : ℝ) (w : ℝ × ℝ) : rotL (-θ) (rotL θ w) = w := by
  have hpyth := Real.sin_sq_add_cos_sq θ
  simp only [rotL_apply, Real.cos_neg, Real.sin_neg, Prod.ext_iff]
  constructor
  · linear_combination w.1 * hpyth
  · linear_combination w.2 * hpyth

/-- **Rotation as a measurable equivalence**, with `rot (−θ)` as inverse. -/
noncomputable def rotE (θ : ℝ) : (ℝ × ℝ) ≃ᵐ (ℝ × ℝ) where
  toFun := rotL θ
  invFun := rotL (-θ)
  left_inv := rotL_neg_rotL θ
  right_inv := by
    intro w
    have h := rotL_neg_rotL (-θ) w
    simpa using h
  measurable_toFun := by
    refine Measurable.prodMk ?_ ?_ <;> fun_prop
  measurable_invFun := by
    refine Measurable.prodMk ?_ ?_ <;> fun_prop

@[simp] theorem rotE_apply (θ : ℝ) (w : ℝ × ℝ) : rotE θ w = rotL θ w := rfl

theorem rotE_injective (θ : ℝ) : Function.Injective (rotL θ) :=
  (rotE θ).injective

/-- **Rotation preserves Lebesgue measure on the plane.**

Via `det = 1`: not via an isometry, because `ℝ × ℝ` does not carry the
Euclidean norm (see the file header). -/
theorem measurePreserving_rotE (θ : ℝ) :
    MeasurePreserving (rotE θ) (volume : Measure (ℝ × ℝ)) (volume : Measure (ℝ × ℝ)) := by
  refine ⟨(rotE θ).measurable, ?_⟩
  have hdet : LinearMap.det (rotL θ) ≠ 0 := by rw [det_rotL]; norm_num
  have h := Measure.map_linearMap_addHaar_eq_smul_addHaar (volume : Measure (ℝ × ℝ)) hdet
  rw [det_rotL] at h
  simpa using h

/-! ### 2. Rotation preserves the integrand

The base integrand `1/(2(R² − x² − y²))` sees the point only through
`x² + y²`, which is exactly what a rotation fixes.  This is why rotation
invariance of the base integral holds for THIS integrand; it is not a formal
consequence of measure-preservation alone. -/

/-- Rotation preserves the squared distance to the origin. -/
theorem rotL_normSq (θ : ℝ) (w : ℝ × ℝ) :
    (rotL θ w).1 ^ 2 + (rotL θ w).2 ^ 2 = w.1 ^ 2 + w.2 ^ 2 := by
  have hpyth := Real.sin_sq_add_cos_sq θ
  simp only [rotL_apply]
  linear_combination (w.1 ^ 2 + w.2 ^ 2) * hpyth

/-- **Rotation invariance of the base integral.**

The hypothesis `hg` is where the integrand's own rotation-invariance is
required; measure-preservation alone would not suffice. -/
theorem lintegral_rotL_image {T : Set (ℝ × ℝ)} (θ : ℝ) {g : ℝ × ℝ → ENNReal}
    (hg : ∀ w, g (rotL θ w) = g w) :
    ∫⁻ w in rotL θ '' T, g w = ∫⁻ w in T, g w := by
  have h := (measurePreserving_rotE θ).setLIntegral_comp_preimage_emb
    (rotE θ).measurableEmbedding g (rotL θ '' T)
  have hpre : (rotE θ) ⁻¹' (rotL θ '' T) = T :=
    Set.preimage_image_eq T (rotE_injective θ)
  rw [hpre] at h
  rw [← h]
  simp only [rotE_apply]
  exact lintegral_congr fun w => hg w

/-! ### 3. The wedge at an arbitrary axis

Cartesian definition, rotation proved. -/

/-- **The wedge with axis direction `θ`** — the open isoceles triangle with
apex at the circumcentre, apex angle `2ψ`, and its axis of symmetry pointing
in direction `θ`.

Cut out by dot products against the rotated frame `u = (cos θ, sin θ)`,
`v = (−sin θ, cos θ)`, so that `wedgeAt R 0 ψ` is `wedge R ψ` on the nose. -/
def wedgeAt (R θ ψ : ℝ) : Set (ℝ × ℝ) :=
  {w | w.1 * Real.cos θ + w.2 * Real.sin θ < R * Real.cos ψ ∧
       |(-(w.1 * Real.sin θ) + w.2 * Real.cos θ)|
         < (w.1 * Real.cos θ + w.2 * Real.sin θ) * Real.tan ψ}

/-- Rotating by `θ`, then projecting on the `θ`-axis, returns the abscissa. -/
theorem inner_u_rotL (θ : ℝ) (w : ℝ × ℝ) :
    (rotL θ w).1 * Real.cos θ + (rotL θ w).2 * Real.sin θ = w.1 := by
  have hpyth := Real.sin_sq_add_cos_sq θ
  simp only [rotL_apply]
  linear_combination w.1 * hpyth

/-- …and projecting on the perpendicular returns the ordinate. -/
theorem inner_v_rotL (θ : ℝ) (w : ℝ × ℝ) :
    -((rotL θ w).1 * Real.sin θ) + (rotL θ w).2 * Real.cos θ = w.2 := by
  have hpyth := Real.sin_sq_add_cos_sq θ
  simp only [rotL_apply]
  linear_combination w.2 * hpyth

/-- **The rotated-frame wedge IS the rotated wedge** — the theorem the
Cartesian definition exists in order to make provable. -/
theorem wedgeAt_eq_image (R θ ψ : ℝ) : wedgeAt R θ ψ = rotL θ '' wedge R ψ := by
  ext w
  constructor
  · intro hw
    -- the rotation-back of `w` is the witness; its coordinates ARE the two
    -- dot products, by `inner_u_rotL` / `inner_v_rotL`
    have hrot : rotL θ (rotL (-θ) w) = w := by
      simpa using rotL_neg_rotL (-θ) w
    have hu : w.1 * Real.cos θ + w.2 * Real.sin θ = (rotL (-θ) w).1 := by
      have h := inner_u_rotL θ (rotL (-θ) w); rwa [hrot] at h
    have hv : -(w.1 * Real.sin θ) + w.2 * Real.cos θ = (rotL (-θ) w).2 := by
      have h := inner_v_rotL θ (rotL (-θ) w); rwa [hrot] at h
    refine ⟨rotL (-θ) w, ⟨?_, ?_⟩, hrot⟩
    · rw [← hu]; exact hw.1
    · rw [← hu, ← hv]; exact hw.2
  · rintro ⟨v, hv, rfl⟩
    exact ⟨by rw [inner_u_rotL]; exact hv.1,
      by rw [inner_u_rotL, inner_v_rotL]; exact hv.2⟩

theorem measurableSet_wedgeAt (R θ ψ : ℝ) : MeasurableSet (wedgeAt R θ ψ) := by
  rw [wedgeAt_eq_image]
  exact (rotE θ).measurableEmbedding.measurableSet_image.mpr (measurableSet_wedge R ψ)

/-- The rotated wedge still lies strictly inside the disk — rotation fixes
`x² + y²`. -/
theorem wedgeAt_subset_disk {R θ ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∀ w ∈ wedgeAt R θ ψ, w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
  intro w hw
  rw [wedgeAt_eq_image] at hw
  obtain ⟨v, hv, rfl⟩ := hw
  rw [rotL_normSq]
  exact wedge_subset_disk hψ0 hψ v hv

/-! ### 4. H4-5c-i — the wedge value at any axis -/

/-- The base integrand is rotation-invariant: it sees the point only through
`x² + y²`. -/
theorem baseIntegrand_rotL (R θ : ℝ) (w : ℝ × ℝ) :
    ENNReal.ofReal (1 / (2 * (R ^ 2 - (rotL θ w).1 ^ 2 - (rotL θ w).2 ^ 2)))
      = ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) := by
  have h := rotL_normSq θ w
  have : R ^ 2 - (rotL θ w).1 ^ 2 - (rotL θ w).2 ^ 2 = R ^ 2 - w.1 ^ 2 - w.2 ^ 2 := by linarith
  rw [this]

/-- **The base integral over a wedge at ANY axis is `Λ(ψ)`.** -/
theorem lintegral_wedgeAt {R θ ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∫⁻ w in wedgeAt R θ ψ, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2)))
      = ENNReal.ofReal (Lob ψ) := by
  rw [wedgeAt_eq_image,
    lintegral_rotL_image θ
      (g := fun w => ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))))
      (baseIntegrand_rotL R θ)]
  exact lintegral_wedge hR hψ0 hψ

/-- **The hyperbolic volume of the chimney over a wedge at any axis is `Λ(ψ)`.**

H4-5b's value, freed from the positive `x`-axis.  This is what an assembly of
three wedges at three different axes would consume.

**Still not a statement about an ideal tetrahedron**, and H4-5c is still open:
what remains is showing that a triangle inscribed in the circle *is* the union
of three such wedges up to null sets. -/
theorem hypVolume_chimney_wedgeAt {R θ ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    hypVolume (chimney (wedgeAt R θ ψ) R) = ENNReal.ofReal (Lob ψ) := by
  rw [hypVolume_chimney_of_subset_disk (measurableSet_wedgeAt R θ ψ)
      (wedgeAt_subset_disk hψ0 hψ),
    lintegral_wedgeAt hR hψ0 hψ]

end QOU.Archimedean.HyperbolicVolume
