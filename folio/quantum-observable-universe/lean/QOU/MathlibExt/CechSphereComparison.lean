import QOU.MathlibExt.CechSphereHemispheres
import QOU.MathlibExt.CechGoodRefinement

/-!
# Comparing the hemisphere cover with all open covers of `S²` (C2)

Surface case of route R3 (C-5a), step C2. `CechSphereHemispheres` computes
`H²` of the four-hemisphere cover of `S²` as the coefficient group `G`. Whether
that cover computes the full colimit `Ȟ²` over **all** open covers is step C2.
This file states it as the class `HemiComputesCech` and proves the downstream
step C3 from it. The instance is proved in `CechSphereGood` (steps P1 to P4), so
C2 and C3 hold unconditionally once that file is imported.

## Results, all sorry-free

* `Cech.Cover.inf`, `Cover.infLeft`, `Cover.infRight`: the meet of two covers
  of `⊤`, refining both, and `isOpenCover_inf`.
* `cechClass_one_eq`: the trivial class is the same from any two open covers.
* `HemiComputesCech G` (**C2**): `H2.toCech` from the hemisphere cover is a
  bijection onto `Ȟ²(S², G)`. Stated here, proved in `CechSphereGood`.
* `sphereEquiv`, `sphereEquiv_eq_one_iff`, `sphereEquiv_map`: given C2,
  `Ȟ²(S², G) ≃ G`, natural in `G`.
* `isCoverDirected_isOpenCover`, `hemiComputesCech_of_good`: C2 follows once every
  open cover has a good refinement (see `CechGoodRefinement`).
* `kummerSurfaceData_sphere` (**C3**): `KummerSurfaceData` on `S²` over all
  open covers, for `ℤ` and `μ_n`, from the C2 instances.

## What this does NOT do

It does not prove C2 itself. The proof (`CechSameNerve`, `CechSplit`,
`CechSphereBoxes`, `CechSphereFine`, `CechSphereGood`) avoids Leray: it shrinks
the hemispheres to boxes with the same nerve, splits boxes along overlaps (each
split is a bijection on `H²`), and refines any open cover by the Lebesgue number
lemma.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2/C3
Bean `qou-skn4`.
-/

namespace QOU.CentralExtension.Cech
open CategoryTheory TopologicalSpace CechGerbe

variable {X : Type} [TopologicalSpace X]

/-- The meet of two covers of `⊤ : Opens X`, by pairwise intersections. -/
def Cover.inf (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) : Cover.{0} (⊤ : Opens X) where
  ι := 𝒱.ι × 𝒲.ι
  obj p := 𝒱.obj p.1 ⊓ 𝒲.obj p.2
  arr _ := homOfLE le_top

def Cover.infLeft (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) : (Cover.inf 𝒱 𝒲).Refines 𝒱 where
  r := Prod.fst
  f _ := homOfLE inf_le_left
  w _ := Subsingleton.elim _ _

def Cover.infRight (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) : (Cover.inf 𝒱 𝒲).Refines 𝒲 where
  r := Prod.snd
  f _ := homOfLE inf_le_right
  w _ := Subsingleton.elim _ _

theorem isOpenCover_inf (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) (h𝒱 : IsOpenCover 𝒱)
    (h𝒲 : IsOpenCover 𝒲) : IsOpenCover (Cover.inf 𝒱 𝒲) := by
  intro x _
  obtain ⟨i, hi⟩ := Opens.mem_iSup.1 (h𝒱 (Set.mem_univ x))
  obtain ⟨j, hj⟩ := Opens.mem_iSup.1 (h𝒲 (Set.mem_univ x))
  exact Opens.mem_iSup.2 ⟨(i, j), ⟨hi, hj⟩⟩

/-- Any two open covers have the same trivial class in `Ȟ²`. -/
theorem cechClass_one_eq {G : Type} [TopologicalSpace G] [Group G] [IsTopologicalGroup G]
    (𝒰 𝒱 : Cover.{0} (⊤ : Opens X)) (h𝒰 : IsOpenCover 𝒰) (h𝒱 : IsOpenCover 𝒱) :
    cechClass (Cov := IsOpenCover (X := X)) 𝒰 h𝒰
        (TwoCocycle.one : TwoCocycle 𝒰.obj (contPresheaf X G)) =
      cechClass 𝒱 h𝒱 TwoCocycle.one := by
  rw [← cechClass_one_pull 𝒰 (Cover.inf 𝒰 𝒱) h𝒰 (isOpenCover_inf 𝒰 𝒱 h𝒰 h𝒱) (Cover.infLeft 𝒰 𝒱),
    ← cechClass_one_pull 𝒱 (Cover.inf 𝒰 𝒱) h𝒱 (isOpenCover_inf 𝒰 𝒱 h𝒰 h𝒱) (Cover.infRight 𝒰 𝒱)]

/-- **Step C2** (proved as an instance in `CechSphereGood`). The
four-hemisphere cover computes the full open-cover colimit `Ȟ²(S², G)`: the
canonical map from `H²` of the cover to `Ȟ²` is a bijection. -/
class HemiComputesCech (G : Type) [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G]
    [DiscreteTopology G] : Prop where
  bijective : Function.Bijective
    (H2.toCech (Cov := IsOpenCover (X := S2)) (tetCover hemi) hemi_isOpenCover :
      H2 (tetCover hemi).obj (contPresheaf S2 G) → CechH2 (contPresheaf S2 G) (IsOpenCover (X := S2)))

/-- Open covers of `⊤ : Opens X` form a directed system. -/
theorem isCoverDirected_isOpenCover : IsCoverDirected (IsOpenCover (X := X)) :=
  fun 𝒱 𝒲 h𝒱 h𝒲 => ⟨Cover.inf 𝒱 𝒲, isOpenCover_inf 𝒱 𝒲 h𝒱 h𝒲,
    ⟨Cover.infLeft 𝒱 𝒲⟩, ⟨Cover.infRight 𝒱 𝒲⟩⟩

/-- **C2 reduced to one cover at a time.** If every open cover of `S²` has a
good refinement relative to the hemisphere cover, then C2 holds. -/
theorem hemiComputesCech_of_good (G : Type) [TopologicalSpace G] [CommGroup G]
    [IsTopologicalGroup G] [DiscreteTopology G]
    (hgood : ∀ 𝒱, IsOpenCover 𝒱 →
      HasGoodRefinement (IsOpenCover (X := S2)) (tetCover hemi) (contPresheaf S2 G) 𝒱) :
    HemiComputesCech G :=
  ⟨toCech_bijective_of_good (contPresheaf_comm (X := S2)) isCoverDirected_isOpenCover
    (tetCover hemi) hemi_isOpenCover hgood⟩

section Conditional

variable {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G]

/-- Conditional on C2: `Ȟ²(S², G) ≃ G`. -/
noncomputable def sphereEquiv [h : HemiComputesCech G] :
    CechH2 (contPresheaf S2 G) (IsOpenCover (X := S2)) ≃ G :=
  (Equiv.ofBijective _ h.bijective).symm.trans (h2EquivOfEmptyQuad tetCover_hemi hemi_no_quad)

theorem sphereEquiv_cechClass [HemiComputesCech G] (c : TwoCocycle hemi (contPresheaf S2 G)) :
    sphereEquiv (cechClass (Cov := IsOpenCover (X := S2)) (tetCover hemi) hemi_isOpenCover c) =
      deg tetCover_hemi c.toTwoCochain := by
  have : cechClass (Cov := IsOpenCover (X := S2)) (tetCover hemi) hemi_isOpenCover c =
      H2.toCech (tetCover hemi) hemi_isOpenCover c.class := rfl
  rw [this]
  simp only [sphereEquiv, Equiv.trans_apply]
  rw [Equiv.ofBijective_symm_apply_apply]
  rfl

theorem sphereEquiv_eq_one_iff [HemiComputesCech G] (𝒰 : Cover.{0} (⊤ : Opens S2))
    (h𝒰 : IsOpenCover 𝒰) (x : CechH2 (contPresheaf S2 G) (IsOpenCover (X := S2))) :
    sphereEquiv x = 1 ↔ x = cechClass 𝒰 h𝒰 TwoCocycle.one := by
  rw [cechClass_one_eq 𝒰 (tetCover hemi) h𝒰 hemi_isOpenCover]
  have h1 : sphereEquiv (cechClass (Cov := IsOpenCover (X := S2)) (tetCover hemi)
      hemi_isOpenCover (TwoCocycle.one : TwoCocycle hemi (contPresheaf S2 G))) = 1 := by
    rw [sphereEquiv_cechClass]; exact deg_one tetCover_hemi
  rw [← h1]
  exact sphereEquiv.injective.eq_iff

variable {H : Type} [TopologicalSpace H] [CommGroup H] [IsTopologicalGroup H] [DiscreteTopology H]

theorem sphereEquiv_map [HemiComputesCech G] [HemiComputesCech H] (φ : G →* H)
    (hφ : Continuous φ) (x : CechH2 (contPresheaf S2 G) (IsOpenCover (X := S2))) :
    sphereEquiv (CechH2.map (postcomp S2 φ hφ) x) = φ (sphereEquiv x) := by
  obtain ⟨z, rfl⟩ := (HemiComputesCech.bijective (G := G)).2 x
  induction z using Quot.ind with
  | mk c =>
    change sphereEquiv (CechH2.map (postcomp S2 φ hφ)
      (cechClass (Cov := IsOpenCover (X := S2)) (tetCover hemi) hemi_isOpenCover c)) =
      φ (sphereEquiv (cechClass (Cov := IsOpenCover (X := S2)) (tetCover hemi)
        hemi_isOpenCover c))
    rw [CechH2.map_cechClass, sphereEquiv_cechClass, sphereEquiv_cechClass, deg_map]

end Conditional

/-- **C3.** Given C2 for `ℤ` and `μₙ` coefficients (proved in `CechSphereGood`),
the 2-sphere carries `KummerSurfaceData` over **all** open covers. -/
noncomputable def kummerSurfaceData_sphere (n : ℕ) [NeZero n]
    [HemiComputesCech (Multiplicative ℤ)] [HemiComputesCech (rootsOfUnityCircle n)] :
    KummerSurfaceData S2 n (IsOpenCover (X := S2)) where
  deg x := Multiplicative.toAdd (sphereEquiv x)
  degN x := ((Multiplicative.toAdd (kappaSection n (sphereEquiv x)) : ℤ) : ZMod n)
  degN_eq_zero_iff 𝒰 h𝒰 x := by
    rw [ZMod.intCast_zmod_eq_zero_iff_dvd, ← kappa_eq_one_iff, kappa_kappaSection,
      sphereEquiv_eq_one_iff]
  degN_map x := by
    rw [sphereEquiv_map (kappa n) (continuous_kappa n)]
    set d := sphereEquiv x
    rw [ZMod.intCast_eq_intCast_iff_dvd_sub]
    have h1 : kappa n (d * (kappaSection n (kappa n d))⁻¹) = 1 := by
      rw [map_mul, map_inv, kappa_kappaSection, mul_inv_cancel]
    rw [kappa_eq_one_iff] at h1
    simpa [toAdd_mul, toAdd_inv, sub_eq_add_neg] using h1


end QOU.CentralExtension.Cech
