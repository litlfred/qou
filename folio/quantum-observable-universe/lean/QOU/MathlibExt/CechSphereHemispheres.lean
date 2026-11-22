import QOU.MathlibExt.CechNerveTetrahedron
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Convex.Topology


/-!
# The four-hemisphere cover of the 2-sphere

Surface case of route R3 (C-5a), step C1b. On `S² ⊂ ℝ³` take the four open
hemispheres `{x | 0 < ⟪vᵢ, x⟫}` centred at the vertices `vᵢ = (±1,±1,±1)` of a
regular tetrahedron.

## Results, all sorry-free

* `isPreconnected_cone_inter_sphere`: an open convex cone not containing `0`
  meets the unit sphere in a preconnected set (radial projection).
* `tetCover_hemi`: every intersection of at most three hemispheres is nonempty
  (it contains the antipode of the omitted vertex, normalised) and
  preconnected. So the hemispheres form a `TetCover`.
* `hemi_no_quad`: no point lies in all four, since `∑ vᵢ = 0`.
* `hemi_isOpenCover`: the four hemispheres cover `S²`.
* `cechH2SphereHemiEquiv`: hence `H²` of this cover with discrete abelian
  coefficients `G` is `G`.
* `kummerSurfaceData_sphereHemi`: the cover-level `KummerSurfaceData` on `S²`.

## What this does NOT do

Everything here is **cover-level**: the colimit runs over the single hemisphere
cover, not over all open covers of `S²`. That this cover computes the full `Ȟ²`
(step C2) is open. Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C1
-/

namespace QOU.CentralExtension.Cech
open TopologicalSpace CechGerbe

/-- An open convex cone not containing `0` meets the unit sphere in a
preconnected set: radial projection maps the cone onto it. -/
theorem isPreconnected_cone_inter_sphere {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {C : Set E} (hC : Convex ℝ C) (h0 : (0 : E) ∉ C)
    (hsm : ∀ x ∈ C, ∀ t : ℝ, 0 < t → t • x ∈ C) :
    IsPreconnected (C ∩ Metric.sphere 0 1) := by
  have himg : (fun x : E => ‖x‖⁻¹ • x) '' C = C ∩ Metric.sphere 0 1 := by
    ext y; constructor
    · rintro ⟨x, hx, rfl⟩
      have hx0 : x ≠ 0 := fun h => h0 (h ▸ hx)
      refine ⟨hsm x hx _ (inv_pos.2 (norm_pos_iff.2 hx0)), ?_⟩
      simp [norm_smul, hx0]
    · rintro ⟨hy, hy1⟩
      have : ‖y‖ = 1 := by simpa using hy1
      exact ⟨y, hy, by simp [this]⟩
  rw [← himg]
  refine hC.isPreconnected.image _ ?_
  refine ContinuousOn.smul (ContinuousOn.inv₀ continuous_norm.continuousOn fun x hx => ?_)
    continuousOn_id
  exact norm_ne_zero_iff.2 (fun h => h0 (h ▸ hx))

/-- The real 2-sphere `S² ⊂ ℝ³`. -/
abbrev S2 : Type := Metric.sphere (0 : EuclideanSpace ℝ (Fin 3)) 1

/-- Signs of the vertices `(±1,±1,±1)` (even number of minus signs) of a regular
tetrahedron. -/
def tsgn : Fin 4 → Fin 3 → ℝ := ![![1, 1, 1], ![1, -1, -1], ![-1, 1, -1], ![-1, -1, 1]]

/-- The linear form `x ↦ ⟪vᵢ, x⟫` for the `i`-th vertex. -/
noncomputable def tfun (i : Fin 4) : EuclideanSpace ℝ (Fin 3) →L[ℝ] ℝ :=
  tsgn i 0 • EuclideanSpace.proj 0 + tsgn i 1 • EuclideanSpace.proj 1 +
    tsgn i 2 • EuclideanSpace.proj 2

theorem tfun_apply (i : Fin 4) (x : EuclideanSpace ℝ (Fin 3)) :
    tfun i x = tsgn i 0 * x 0 + tsgn i 1 * x 1 + tsgn i 2 * x 2 := by
  simp [tfun]

/-- The open hemisphere centred at the `i`-th tetrahedron vertex. -/
def hemi (i : Fin 4) : Opens S2 :=
  ⟨{p | 0 < tfun i p.1}, isOpen_lt continuous_const ((tfun i).continuous.comp continuous_subtype_val)⟩

theorem tfun_sum (x : EuclideanSpace ℝ (Fin 3)) :
    tfun 0 x + tfun 1 x + tfun 2 x + tfun 3 x = 0 := by
  simp only [tfun_apply, tsgn]; simp; ring

/-- No point of the sphere lies in all four hemispheres. -/
theorem hemi_no_quad (p : S2) : ∃ m : Fin 4, p ∉ hemi m := by
  by_contra h
  push_neg at h
  have h0 := h 0; have h1 := h 1; have h2 := h 2; have h3 := h 3
  change 0 < tfun _ _ at h0 h1 h2 h3
  linarith [tfun_sum p.1]

/-- The cone over the triple overlap. -/
def tcone (i j k : Fin 4) : Set (EuclideanSpace ℝ (Fin 3)) :=
  {x | 0 < tfun i x ∧ 0 < tfun j x ∧ 0 < tfun k x}

theorem isPreconnected_tcone_sphere (i j k : Fin 4) :
    IsPreconnected (tcone i j k ∩ Metric.sphere 0 1) := by
  refine isPreconnected_cone_inter_sphere ?_ ?_ ?_
  · have hc : ∀ m, Convex ℝ {x : EuclideanSpace ℝ (Fin 3) | 0 < tfun m x} := fun m =>
      convex_halfSpace_gt (tfun m).toLinearMap.isLinear 0
    exact (hc i).inter ((hc j).inter (hc k))
  · simp [tcone]
  · rintro x ⟨hi, hj, hk⟩ t ht
    simp only [tcone, Set.mem_setOf_eq, map_smul, smul_eq_mul]
    exact ⟨mul_pos ht hi, mul_pos ht hj, mul_pos ht hk⟩

theorem image_hemi3 (i j k : Fin 4) :
    Subtype.val '' ((hemi i ⊓ hemi j ⊓ hemi k : Opens S2) : Set S2) =
      tcone i j k ∩ Metric.sphere 0 1 := by
  ext x
  simp only [Set.mem_image, Opens.coe_inf, Set.mem_inter_iff, SetLike.mem_coe, tcone,
    Set.mem_setOf_eq]
  constructor
  · rintro ⟨p, ⟨⟨hi, hj⟩, hk⟩, rfl⟩
    exact ⟨⟨hi, hj, hk⟩, p.2⟩
  · rintro ⟨⟨hi, hj, hk⟩, hx⟩
    exact ⟨⟨x, hx⟩, ⟨⟨hi, hj⟩, hk⟩, rfl⟩

theorem pre3_hemi (i j k : Fin 4) :
    IsPreconnected ((hemi i ⊓ hemi j ⊓ hemi k : Opens S2) : Set S2) := by
  rw [← Topology.IsInducing.subtypeVal.isPreconnected_image, image_hemi3]
  exact isPreconnected_tcone_sphere i j k

theorem pre2_hemi (i j : Fin 4) :
    IsPreconnected ((hemi i ⊓ hemi j : Opens S2) : Set S2) := by
  have : (hemi i ⊓ hemi j : Opens S2) = hemi i ⊓ hemi j ⊓ hemi j := by
    rw [inf_assoc, inf_idem]
  rw [this]; exact pre3_hemi i j j

theorem exists_fourth : ∀ i j k : Fin 4, ∃ l, l ≠ i ∧ l ≠ j ∧ l ≠ k := by decide

theorem tsgn_dot (m l : Fin 4) (h : m ≠ l) :
    tsgn m 0 * tsgn l 0 + tsgn m 1 * tsgn l 1 + tsgn m 2 * tsgn l 2 = -1 := by
  fin_cases m <;> fin_cases l <;> simp_all [tsgn]

theorem ne3_hemi (i j k : Fin 4) :
    ((hemi i ⊓ hemi j ⊓ hemi k : Opens S2) : Set S2).Nonempty := by
  obtain ⟨l, hi, hj, hk⟩ := exists_fourth i j k
  set v : EuclideanSpace ℝ (Fin 3) := WithLp.toLp 2 (fun a => - tsgn l a)
  have hv : ∀ m, m ≠ l → tfun m v = 1 := fun m hm => by
    simp only [tfun_apply, v, PiLp.toLp_apply]
    linarith [tsgn_dot m l hm]
  have hv0 : v ≠ 0 := fun h => by have := hv i hi.symm; rw [h, map_zero] at this; norm_num at this
  have hn : 0 < ‖v‖⁻¹ := inv_pos.2 (norm_pos_iff.2 hv0)
  refine ⟨⟨‖v‖⁻¹ • v, by simp [norm_smul, hv0]⟩, ?_⟩
  simp only [Opens.coe_inf, Set.mem_inter_iff, SetLike.mem_coe]
  refine ⟨⟨?_, ?_⟩, ?_⟩ <;> change 0 < tfun _ (‖v‖⁻¹ • v) <;>
    rw [map_smul, smul_eq_mul] <;> [rw [hv i hi.symm]; rw [hv j hj.symm]; rw [hv k hk.symm]] <;>
    simpa using hn

/-- **The four open hemispheres form a `TetCover` of the 2-sphere.** -/
theorem tetCover_hemi : TetCover hemi := ⟨ne3_hemi, pre3_hemi, pre2_hemi⟩

/-- The four hemispheres cover the sphere. -/
theorem hemi_isOpenCover : IsOpenCover (tetCover hemi) := by
  intro p _
  refine Opens.mem_iSup.2 ?_
  by_contra h
  push_neg at h
  have hle : ∀ m, tfun m p.1 ≤ 0 := fun m => not_lt.1 (h m)
  have hs := tfun_sum p.1
  have e0 : tfun 0 p.1 = 0 := by linarith [hle 0, hle 1, hle 2, hle 3]
  have e1 : tfun 1 p.1 = 0 := by linarith [hle 0, hle 1, hle 2, hle 3]
  have e2 : tfun 2 p.1 = 0 := by linarith [hle 0, hle 1, hle 2, hle 3]
  have e3 : tfun 3 p.1 = 0 := by linarith [hle 0, hle 1, hle 2, hle 3]
  simp only [tfun_apply, tsgn] at e0 e1 e2 e3
  simp at e0 e1 e2 e3
  have hx : p.1 = 0 := by
    ext a; fin_cases a <;> simp <;> linarith
  have := p.2
  rw [hx] at this
  simp at this

/-- **Cover-level Čech `H²` of the 2-sphere, for the hemisphere cover, is `G`.** -/
noncomputable def cechH2SphereHemiEquiv {G : Type} [TopologicalSpace G] [CommGroup G]
    [IsTopologicalGroup G] [DiscreteTopology G] :
    CechH2 (contPresheaf S2 G) (· = tetCover hemi) ≃ G :=
  cechH2EquivOfEmptyQuad tetCover_hemi hemi_no_quad

/-- The cover-level Kummer surface data on `S²`, from the hemisphere cover. -/
noncomputable def kummerSurfaceData_sphereHemi (n : ℕ) [NeZero n] :
    KummerSurfaceData S2 n (· = tetCover hemi) :=
  kummerSurfaceData_tet tetCover_hemi n

end QOU.CentralExtension.Cech
