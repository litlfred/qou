import QOU.MathlibExt.CechSubdivMesh
import QOU.MathlibExt.CechGenus4Cover
import QOU.MathlibExt.CechSphereComparison
import QOU.MathlibExt.CechKummerSurface

/-!
# The star cover of the genus-4 surface computes `Ȟ²` (route R3, steps S3–S4)

`CechGenus4Cover` computes `H²` of the open-star cover `U4` of the genus-4
surface `Surf` (the realisation of the 50-face triangulation `face4`) as the
coefficient group `G`. This file shows that this cover computes the colimit
`Ȟ²(Surf, G)` over **all** open covers (S3). It then builds `KummerSurfaceData`
on `Surf` with no hypothesis (S4), in the same way as `kummerSurfaceData_sphere'`
for `S²`.

The proof does not use Leray's theorem. `Surf` is a linear triangulation of
itself (`base`). Longest-edge bisection (`CechSubdivMesh.exists_fine`) produces
star covers with arbitrarily small stars, and each of them is reached from `U4`
by a bijection on `H²` (`CechSubdivCover.reach_subdiv`). By the Lebesgue
number lemma such a star cover refines any open cover, which gives the good
refinements that `toCech_bijective_of_good` needs.

## Results (all sorry-free)

* `base`: the identity linear triangulation of `Surf`, with `base_fam : base.T.fam = U4`.
* `hasGoodRefinement_genus4`: every open cover of `Surf` has a good refinement
  relative to `U4`.
* `toCech_bijective_genus4` (**S3**): `H²(U4) → Ȟ²(Surf, G)` is a bijection.
* `genus4Equiv`, `genus4Equiv_eq_one_iff`, `genus4Equiv_map`: `Ȟ²(Surf, G) ≃ G`,
  detecting the trivial class, natural in `G`.
* `kummerSurfaceData_genus4` (**S4**): `KummerSurfaceData Surf n` over all open
  covers, with no hypothesis.
* `genus4_kummer_trivial_iff`: `bring_kummer_trivial_iff` on `Surf`, with only
  the degree formula `hχ` left as a hypothesis.

## What this does NOT do

* It does not identify `Surf` with Bring's curve. That `face4` triangulates a
  closed orientable surface of genus 4, and that this surface is Bring's curve
  topologically, is a citation, not a theorem proved here.
* It does not prove the degree formula `hχ` of `bring_kummer_trivial_iff`
  (`deg c₁(T_S) = χ(S) = −6`, Poincaré–Hopf). That stays a hypothesis. It also
  does not build the tangent cocycle of `Surf` with local real lifts.

-- Ref: [leitner2026] lifting-and-descent, route R3, surface step S3/S4
-/

open CategoryTheory TopologicalSpace

namespace QOU.CentralExtension.Cech

open CechGerbe

/-- Pushing a cochain forward changes its nerve values by the homomorphism. -/
theorem nval_map {X : Type} [TopologicalSpace X] {G H : Type} [TopologicalSpace G] [CommGroup G]
    [IsTopologicalGroup G] [TopologicalSpace H] [CommGroup H] [IsTopologicalGroup H]
    {ι : Type} {U : ι → Opens X} (φ : G →* H) (hφ : Continuous φ)
    (c : TwoCocycle U (contPresheaf X G)) (i j k : ι) :
    nval (c.map (postcomp X φ hφ)).toTwoCochain i j k = φ (nval c.toTwoCochain i j k) := by
  unfold nval
  split_ifs
  · rfl
  · exact (map_one φ).symm

namespace Genus4

/-! ### `Surf` as a linear triangulation of itself -/

/-- The faces of the genus-4 triangulation, as a finset of faces. -/
def F0 : Finset (Finset (Fin 19)) := Finset.univ.image face4

theorem real4_eq : PL.Real4 F0 = Real4 face4 := by
  ext p
  simp only [PL.Real4, Real4, F0, Finset.mem_image, Finset.mem_univ, true_and, Set.mem_setOf_eq]
  constructor
  · rintro ⟨h0, h1, f, ⟨g, rfl⟩, hf⟩; exact ⟨h0, h1, g, hf⟩
  · rintro ⟨h0, h1, g, hf⟩; exact ⟨h0, h1, _, ⟨g, rfl⟩, hf⟩

/-- The realisation of `F0` is `Surf`. -/
def H0 : PL.PSpace F0 ≃ₜ Surf := Homeomorph.setCongr real4_eq

/-- The identity triangulation of `Surf`, with vertex `w` at the basis vector `e_w`. -/
def base : PL.GTri (Real4 face4) where
  T := ⟨Fin 19, F0, H0⟩
  P w := Pi.single w 1
  hP q := by
    funext i
    change q.1 i = _
    simp [Pi.single_apply]

theorem base_fam : base.T.fam = U4 := by
  funext v; ext x; rfl

theorem single_sub_sq_le (x y i : Fin 19) :
    ((Pi.single x 1 : Fin 19 → ℝ) i - (Pi.single y 1 : Fin 19 → ℝ) i) ^ 2 ≤
      (Pi.single x 1 : Fin 19 → ℝ) i + (Pi.single y 1 : Fin 19 → ℝ) i := by
  by_cases hx : i = x <;> by_cases hy : i = y
  · subst hx; subst hy; simp
  · subst hx; simp [hy]
  · subst hy; simp [hx]
  · simp [hx, hy]

theorem base_bounded : base.Bounded 2 := by
  intro f _ x _ y _
  calc ∑ i : Fin 19, ((Pi.single x 1 : Fin 19 → ℝ) i - (Pi.single y 1 : Fin 19 → ℝ) i) ^ 2
        ≤ ∑ i : Fin 19, ((Pi.single x 1 : Fin 19 → ℝ) i + (Pi.single y 1 : Fin 19 → ℝ) i) :=
        Finset.sum_le_sum fun i _ => single_sub_sq_le x y i
    _ = 2 := by
        rw [Finset.sum_add_distrib]
        simp [Pi.single_apply]; norm_num

instance : CompactSpace Surf := H0.compactSpace

/-- A point of `Surf`. -/
noncomputable def pt : Surf :=
  H0 ⟨PL.unif (face4 0), PL.unif_mem F0 ⟨fA 0, (mem_face 0).1⟩
    (Finset.mem_image_of_mem _ (Finset.mem_univ 0)) (Finset.Subset.refl _)⟩

/-- The star cover as a cover of `⊤`. -/
def cover4 : Cover.{0} (⊤ : Opens Surf) := ⟨Fin 19, U4, fun _ => homOfLE le_top⟩

theorem cover4_isOpenCover : IsOpenCover cover4 := by
  intro x _
  obtain ⟨v, hv⟩ := U4_covers x
  exact Opens.mem_iSup.2 ⟨v, hv⟩

variable (G : Type) [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G]

theorem reach_base : PL.Reach G U4 base.T.fam := by
  refine PL.reach_congr base_fam.symm ⟨Equiv.refl (Fin 19), fun j => (rfl : U4 j = U4 j).le, ?_⟩
  exact reindex_pull_bijective (Equiv.refl _) (fun _ => rfl) connFamily_star

/-- **Every open cover of `Surf` has a good refinement** relative to the star cover. -/
theorem hasGoodRefinement_genus4 (𝒱 : Cover.{0} (⊤ : Opens Surf)) (h𝒱 : IsOpenCover 𝒱) :
    HasGoodRefinement (IsOpenCover (X := Surf)) cover4 (contPresheaf Surf G) 𝒱 := by
  have hcov : (Set.univ : Set Surf) ⊆ ⋃ i, ((𝒱.obj i : Opens Surf) : Set Surf) := by
    intro x _
    obtain ⟨i, hi⟩ := Opens.mem_iSup.1 (h𝒱 (Set.mem_univ x))
    exact Set.mem_iUnion.2 ⟨i, hi⟩
  obtain ⟨δ, hδ, hleb⟩ := lebesgue_number_lemma_of_metric isCompact_univ
    (fun i => (𝒱.obj i).isOpen) hcov
  have hne : Nonempty 𝒱.ι := by
    obtain ⟨i, -⟩ := Set.mem_iUnion.1 (hcov (Set.mem_univ pt))
    exact ⟨i⟩
  obtain ⟨S, hB, r, hr, hbij⟩ :=
    base.exists_fine (G := G) 2 base_bounded (reach_base G) (show 0 < (δ / 4) ^ 2 by positivity)
  have hδ' : 2 * Real.sqrt ((δ / 4) ^ 2) < δ := by
    rw [Real.sqrt_sq (by positivity)]; linarith
  have hsub : ∀ j, ∃ i, S.T.fam j ≤ 𝒱.obj i := by
    intro j
    by_cases hj : ∃ p, p ∈ S.T.fam j
    · obtain ⟨p, hp⟩ := hj
      obtain ⟨i, hi⟩ := hleb p (Set.mem_univ p)
      refine ⟨i, fun q hq => hi ?_⟩
      rw [Metric.mem_ball]
      exact S.dist_lt_of_mem_fam hB hδ' hq hp
    · push_neg at hj
      exact ⟨hne.some, fun q hq => absurd hq (hj q)⟩
  choose ρ hρ using hsub
  let W : Cover.{0} (⊤ : Opens Surf) := ⟨S.T.V, S.T.fam, fun _ => homOfLE le_top⟩
  have hW : IsOpenCover W := by
    intro x _
    obtain ⟨j, hj⟩ := S.T.fam_covers x
    exact Opens.mem_iSup.2 ⟨j, hj⟩
  exact ⟨W, hW, ⟨⟨ρ, fun j => homOfLE (hρ j), fun _ => Subsingleton.elim _ _⟩⟩,
    ⟨r, fun j => homOfLE (hr j), fun _ => Subsingleton.elim _ _⟩, hbij⟩

/-- **S3: the star cover computes `Ȟ²(Surf, G)`.** -/
theorem toCech_bijective_genus4 :
    Function.Bijective (H2.toCech (Cov := IsOpenCover (X := Surf)) cover4 cover4_isOpenCover :
      H2 cover4.obj (contPresheaf Surf G) → CechH2 (contPresheaf Surf G) (IsOpenCover (X := Surf))) :=
  toCech_bijective_of_good (contPresheaf_comm (X := Surf)) isCoverDirected_isOpenCover
    cover4 cover4_isOpenCover (hasGoodRefinement_genus4 G)

variable {G}

/-- `Ȟ²(Surf, G) ≃ G`. -/
noncomputable def genus4Equiv : CechH2 (contPresheaf Surf G) (IsOpenCover (X := Surf)) ≃ G :=
  (Equiv.ofBijective _ (toCech_bijective_genus4 G)).symm.trans h2Equiv

theorem genus4Equiv_cechClass (c : TwoCocycle U4 (contPresheaf Surf G)) :
    genus4Equiv (cechClass (Cov := IsOpenCover (X := Surf)) cover4 cover4_isOpenCover c) =
      degS c.toTwoCochain := by
  have : cechClass (Cov := IsOpenCover (X := Surf)) cover4 cover4_isOpenCover c =
      H2.toCech cover4 cover4_isOpenCover c.class := rfl
  rw [this]
  simp only [genus4Equiv, Equiv.trans_apply]
  rw [Equiv.ofBijective_symm_apply_apply]
  rfl

theorem genus4Equiv_eq_one_iff (𝒰 : Cover.{0} (⊤ : Opens Surf)) (h𝒰 : IsOpenCover 𝒰)
    (x : CechH2 (contPresheaf Surf G) (IsOpenCover (X := Surf))) :
    genus4Equiv x = 1 ↔ x = cechClass 𝒰 h𝒰 TwoCocycle.one := by
  rw [cechClass_one_eq 𝒰 cover4 h𝒰 cover4_isOpenCover]
  have h1 : genus4Equiv (cechClass (Cov := IsOpenCover (X := Surf)) cover4
      cover4_isOpenCover (TwoCocycle.one : TwoCocycle U4 (contPresheaf Surf G))) = 1 := by
    rw [genus4Equiv_cechClass]; exact degS_one
  rw [← h1]
  exact genus4Equiv.injective.eq_iff

variable {H : Type} [TopologicalSpace H] [CommGroup H] [IsTopologicalGroup H] [DiscreteTopology H]

omit [DiscreteTopology G] [DiscreteTopology H] in
theorem degS_map (φ : G →* H) (hφ : Continuous φ) (c : TwoCocycle U4 (contPresheaf Surf G)) :
    degS (c.map (postcomp Surf φ hφ)).toTwoCochain = φ (degS c.toTwoCochain) := by
  have e : vals (c.map (postcomp Surf φ hφ)).toTwoCochain =
      fun i j k => (MonoidHom.toAdditive φ) (vals c.toTwoCochain i j k) := by
    funext i j k
    simp only [vals, nval_map]
    rfl
  rw [degS, e, deg_map]
  rfl

theorem genus4Equiv_map (φ : G →* H) (hφ : Continuous φ)
    (x : CechH2 (contPresheaf Surf G) (IsOpenCover (X := Surf))) :
    genus4Equiv (CechH2.map (postcomp Surf φ hφ) x) = φ (genus4Equiv x) := by
  obtain ⟨z, rfl⟩ := (toCech_bijective_genus4 G).2 x
  induction z using Quot.ind with
  | mk c =>
    change genus4Equiv (CechH2.map (postcomp Surf φ hφ)
      (cechClass (Cov := IsOpenCover (X := Surf)) cover4 cover4_isOpenCover c)) =
      φ (genus4Equiv (cechClass (Cov := IsOpenCover (X := Surf)) cover4 cover4_isOpenCover c))
    rw [CechH2.map_cechClass, genus4Equiv_cechClass, genus4Equiv_cechClass, degS_map]

/-- **S4.** The genus-4 surface carries `KummerSurfaceData` over all open covers,
with no hypothesis. -/
noncomputable def kummerSurfaceData_genus4 (n : ℕ) [NeZero n] :
    KummerSurfaceData Surf n (IsOpenCover (X := Surf)) where
  deg x := Multiplicative.toAdd (genus4Equiv x)
  degN x := ((Multiplicative.toAdd (kappaSection n (genus4Equiv x)) : ℤ) : ZMod n)
  degN_eq_zero_iff 𝒰 h𝒰 x := by
    rw [ZMod.intCast_zmod_eq_zero_iff_dvd, ← kappa_eq_one_iff, kappa_kappaSection,
      genus4Equiv_eq_one_iff]
  degN_map x := by
    rw [genus4Equiv_map (kappa n) (continuous_kappa n)]
    set d := genus4Equiv x
    rw [ZMod.intCast_eq_intCast_iff_dvd_sub]
    have h1 : kappa n (d * (kappaSection n (kappa n d))⁻¹) = 1 := by
      rw [map_mul, map_inv, kappa_kappaSection, mul_inv_cancel]
    rw [kappa_eq_one_iff] at h1
    simpa [toAdd_mul, toAdd_inv, sub_eq_add_neg] using h1

/-- **R3 on `Surf`, with only the degree formula as hypothesis.** With the
Kummer data of `kummerSurfaceData_genus4`, if `c₁(γ)` has degree `−6` (for `γ`
the tangent cocycle this is Poincaré–Hopf, not proved here), the Kummer class
of `γ` is trivial iff `n ∣ 6`. -/
theorem genus4_kummer_trivial_iff (n : ℕ) [NeZero n] (𝒰 : Cover.{0} (⊤ : Opens Surf))
    (h𝒰 : IsOpenCover 𝒰)
    (γ : PresheafOfGroups.OneCocycle (contPresheaf Surf Circle) 𝒰.obj)
    (ξ : PresheafOfGroups.OneCochain (contPresheaf Surf (Multiplicative ℝ)) 𝒰.obj)
    (hξ : IsRealLift γ ξ)
    (hχ : (kummerSurfaceData_genus4 n).deg (cechClass 𝒰 h𝒰 (chernCocycle γ ξ hξ)) = -6) :
    (kummerExtension n Surf).cechObstruction 𝒰 h𝒰 γ (localRoot n ξ)
        (localRoot_lift n γ ξ hξ) = cechClass 𝒰 h𝒰 TwoCocycle.one ↔ n ∣ 6 :=
  bring_kummer_trivial_iff (D := kummerSurfaceData_genus4 n) n 𝒰 h𝒰 γ ξ hξ hχ

end Genus4

end QOU.CentralExtension.Cech
