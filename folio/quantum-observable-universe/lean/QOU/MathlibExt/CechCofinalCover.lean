import QOU.MathlibExt.CechDominantCover
import Mathlib.Topology.AlexandrovDiscrete

/-!
# A cofinal cover computes the colimit `Ȟ²`

Surface case of route R3 (C-5a), step S1. `KummerSurfaceData` asks for degree
maps on the colimit `Ȟ²` over **all** admissible covers. This file reduces that
colimit to the `H²` of a single cover when one admissible cover refines every
other, and shows that such a cover exists on every finite space: the cover by
minimal open neighbourhoods.

## Results, all sorry-free

* `CechGerbe.toCofinal`: for an admissible cover `𝒰₀` refining every admissible
  cover, the map `Ȟ² → H²(𝒰₀)` pulling a cocycle back to `𝒰₀`. It is well defined
  because two refinements give cohomologous pullbacks (G1b).
* `CechGerbe.cechH2EquivCofinal`: that map is a bijection `Ȟ² ≃ H²(𝒰₀)`, inverse to
  `H2.toCech`.
* `Cech.minimalCover`, `Cech.minimalCover_refines`: on an Alexandrov-discrete
  space (for example any finite space), the cover by the minimal open
  neighbourhoods `nhdsKer {x}` is an open cover refining every open cover.
* `Cech.cechH2EquivMinimal`: hence `Ȟ²(X, 𝒜) ≃ H²(minimal cover, 𝒜)` for every
  commutative presheaf `𝒜`, over the full open-cover colimit.

## What this does NOT do

It does not compute `H²` of any particular space. For a finite model of the
2-sphere, step S2 still has to show that `H²` of the minimal cover is `ℤ` (resp.
`ℤ/n`) and to build the degree maps. Comparing a finite model with the real
sphere (McCord) is not attempted. Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S1
-/

universe w' w v u

namespace QOU.CentralExtension.CechGerbe

open CategoryTheory Opposite

variable {C : Type u} [Category.{v} C] {X : C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}
  {Cov : Cover.{w'} X → Prop}
  (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
  (𝒰₀ : Cover.{w'} X) (h₀ : Cov 𝒰₀) (cof : ∀ 𝒱, Cov 𝒱 → Nonempty (𝒰₀.Refines 𝒱))

/-- Pull a cover-cocycle back to the cofinal cover, along a chosen refinement. -/
noncomputable def toCofinalAux (x : CoverCocycle 𝒜 Cov) : H2 𝒰₀.obj 𝒜 :=
  let ρ := (cof x.cov x.adm).some
  (x.c.pull ρ.r ρ.f).class

include hcomm in
/-- The class pulled back to `𝒰₀` does not depend on the refinement. -/
theorem pull_class_eq {𝒱 : Cover.{w'} X} (c : TwoCocycle 𝒱.obj 𝒜) (ρ ρ' : 𝒰₀.Refines 𝒱) :
    (c.pull ρ.r ρ.f).class = (c.pull ρ'.r ρ'.f).class :=
  (TwoCocycle.class_eq_iff hcomm _ _).2 (pullTwoCocycle_rel_of_two_refinements hcomm c _ _ _ _)

include hcomm in
theorem toCofinalAux_step {x y : CoverCocycle 𝒜 Cov} (h : CoverCocycle.Step x y) :
    toCofinalAux 𝒰₀ cof x = toCofinalAux 𝒰₀ cof y := by
  cases h with
  | refine x 𝒱 h𝒱 ρ =>
    unfold toCofinalAux
    dsimp only
    set σ := (cof 𝒱 h𝒱).some
    rw [pull_class_eq hcomm 𝒰₀ x.c (cof x.cov x.adm).some (Cover.Refines.comp σ ρ)]
    congr 1
    apply TwoCocycle.ext_cochain
    ext j k l T a b d
    exact (TwoCocycle.pull_pull_ev σ ρ x.c j k l a b d).symm
  | coh 𝒰 h𝒰 c₁ c₂ hr =>
    unfold toCofinalAux
    exact (TwoCocycle.class_eq_iff hcomm _ _).2 (hr.pull _ _)

/-- **The map `Ȟ² → H²(𝒰₀)`** to a cofinal admissible cover. -/
noncomputable def toCofinal : CechH2 𝒜 Cov → H2 𝒰₀.obj 𝒜 :=
  Quot.lift (toCofinalAux 𝒰₀ cof) (fun _ _ h => toCofinalAux_step hcomm 𝒰₀ cof h)

include hcomm in
theorem toCofinal_toCech (z : H2 𝒰₀.obj 𝒜) :
    toCofinal hcomm 𝒰₀ cof (H2.toCech 𝒰₀ h₀ z) = z := by
  induction z using Quot.ind with
  | mk c =>
    show toCofinalAux 𝒰₀ cof ⟨𝒰₀, h₀, c⟩ = c.class
    unfold toCofinalAux
    dsimp only
    rw [pull_class_eq hcomm 𝒰₀ c _ (Cover.Refines.id 𝒰₀)]
    congr 1
    apply TwoCocycle.ext_cochain
    ext j k l T a b d
    simp [Cover.Refines.id]

include hcomm h₀ in
theorem toCech_toCofinal (x : CechH2 𝒜 Cov) :
    H2.toCech 𝒰₀ h₀ (toCofinal hcomm 𝒰₀ cof x) = x := by
  induction x using Quot.ind with
  | mk y =>
    obtain ⟨𝒱, h𝒱, c⟩ := y
    exact cechClass_pull 𝒱 𝒰₀ h𝒱 h₀ _ c

/-- **`Ȟ²` is `H²` of a cofinal cover.** If an admissible cover `𝒰₀` refines every
admissible cover, the colimit `Ȟ²` is in bijection with `H²(𝒰₀)`. -/
noncomputable def cechH2EquivCofinal : CechH2 𝒜 Cov ≃ H2 𝒰₀.obj 𝒜 where
  toFun := toCofinal hcomm 𝒰₀ cof
  invFun := H2.toCech 𝒰₀ h₀
  left_inv := toCech_toCofinal hcomm 𝒰₀ h₀ cof
  right_inv := toCofinal_toCech hcomm 𝒰₀ h₀ cof

end QOU.CentralExtension.CechGerbe

namespace QOU.CentralExtension.Cech

open CategoryTheory TopologicalSpace CechGerbe

variable {X : Type} [TopologicalSpace X] [AlexandrovDiscrete X]

/-- The cover of `⊤ : Opens X` by minimal open neighbourhoods `nhdsKer {x}`. -/
def minimalCover (X : Type) [TopologicalSpace X] [AlexandrovDiscrete X] :
    Cover.{0} (⊤ : Opens X) where
  ι := X
  obj x := ⟨nhdsKer {x}, isOpen_nhdsKer⟩
  arr _ := homOfLE le_top

theorem minimalCover_isOpenCover : IsOpenCover (minimalCover X) := by
  intro y _
  exact Opens.mem_iSup.2 ⟨y, subset_nhdsKer (Set.mem_singleton y)⟩

/-- The minimal cover refines every open cover. -/
theorem minimalCover_refines (𝒱 : Cover.{0} (⊤ : Opens X)) (h𝒱 : IsOpenCover 𝒱) :
    Nonempty ((minimalCover X).Refines 𝒱) := by
  have hx : ∀ x : X, ∃ i, x ∈ 𝒱.obj i := fun x => Opens.mem_iSup.1 (h𝒱 (Set.mem_univ x))
  choose r hr using hx
  exact ⟨{ r := r
           f := fun x => homOfLE (nhdsKer_minimal (Set.singleton_subset_iff.2 (hr x))
             (𝒱.obj (r x)).isOpen)
           w := fun _ => Subsingleton.elim _ _ }⟩

/-- **`Ȟ²` of an Alexandrov-discrete space (e.g. a finite space) over all open
covers is `H²` of its minimal cover.** -/
noncomputable def cechH2EquivMinimal {𝒜 : (Opens X)ᵒᵖ ⥤ GrpCat.{w}}
    (hcomm : ∀ (T : (Opens X)ᵒᵖ) (x y : 𝒜.obj T), x * y = y * x) :
    CechH2 𝒜 (IsOpenCover (X := X)) ≃ H2 (minimalCover X).obj 𝒜 :=
  cechH2EquivCofinal hcomm (minimalCover X) minimalCover_isOpenCover minimalCover_refines

end QOU.CentralExtension.Cech
