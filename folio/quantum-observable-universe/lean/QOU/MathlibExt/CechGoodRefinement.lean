import QOU.MathlibExt.CechColimitConverse

/-!
# Good refinements compute the colimit `Ȟ²` (Leray-type reduction)

Surface case of route R3 (C-5a), step C2, generic part. For a fixed admissible
cover `𝒰₀`, call a cover **good** (relative to `𝒰₀`) if it is admissible,
refines `𝒰₀`, and pulling `H²` back from `𝒰₀` to it is a bijection.

## Results, all sorry-free

* `agrees_step_iff`: "agrees with a fixed cocycle of `𝒰₀` on some common
  refinement" is invariant under each step of the colimit relation (on a
  directed system, for a commutative presheaf).
* `H2.pull_eq_of_refines`, `H2.pull_comp`: on classes, the pullback does not
  depend on the refinement, and pulling along a composite is pulling twice.
* `toCech_bijective_of_good`: if every admissible cover has a good refinement,
  `H²(𝒰₀) → Ȟ²` is a bijection.

So proving `Ȟ² ≅ H²(𝒰₀)` reduces to one cover at a time. It does not say
when good refinements exist; that is the geometric input (Leray).

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
Bean `qou-skn4`.
-/

universe w' w v u

namespace QOU.CentralExtension.CechGerbe

open CategoryTheory Opposite

variable {C : Type u} [Category.{v} C] {X : C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}
  {Cov : Cover.{w'} X → Prop}

/-- The pair `x` **agrees with** the cocycle `z` of `𝒰₀` on some admissible cover
refining both. -/
def CoverCocycle.Agrees (𝒰₀ : Cover.{w'} X) (z : TwoCocycle 𝒰₀.obj 𝒜)
    (x : CoverCocycle 𝒜 Cov) : Prop :=
  ∃ (𝒲 : Cover.{w'} X) (_ : Cov 𝒲) (σ : 𝒲.Refines 𝒰₀) (ρ : 𝒲.Refines x.cov),
    TwoCocycle.Rel (z.pull σ.r σ.f) (x.c.pull ρ.r ρ.f)

variable (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
include hcomm

theorem agrees_step_iff (hdir : IsCoverDirected Cov) (𝒰₀ : Cover.{w'} X)
    (z : TwoCocycle 𝒰₀.obj 𝒜) {x y : CoverCocycle 𝒜 Cov} (hs : CoverCocycle.Step x y) :
    x.Agrees 𝒰₀ z ↔ y.Agrees 𝒰₀ z := by
  cases hs with
  | refine x 𝒱 h𝒱 ρ₀ =>
    constructor
    · rintro ⟨𝒲, h𝒲, σ, ρ, h⟩
      obtain ⟨𝒵, h𝒵, ⟨τ₁⟩, ⟨τ₂⟩⟩ := hdir 𝒲 𝒱 h𝒲 h𝒱
      refine ⟨𝒵, h𝒵, τ₁.comp σ, τ₂, ?_⟩
      have e := TwoCocycle.equivalence_rel (U := 𝒵.obj) hcomm
      have h1 : TwoCocycle.Rel (z.pull (τ₁.comp σ).r (τ₁.comp σ).f)
          (x.c.pull (τ₁.comp ρ).r (τ₁.comp ρ).f) :=
        ((e.symm ((h.pull τ₁.r τ₁.f).of_ev_eq
          (fun _ _ _ _ _ _ _ => TwoCocycle.pull_pull_ev τ₁ ρ _ _ _ _ _ _ _))).of_ev_eq
          (fun _ _ _ _ _ _ _ => TwoCocycle.pull_pull_ev τ₁ σ _ _ _ _ _ _ _)) |> e.symm
      have h2 := pullTwoCocycle_rel_of_two_refinements hcomm x.c (τ₁.comp ρ).r (τ₂.comp ρ₀).r
        (τ₁.comp ρ).f (τ₂.comp ρ₀).f
      exact (e.trans h1 h2).of_ev_eq
        (fun _ _ _ _ _ _ _ => (TwoCocycle.pull_pull_ev τ₂ ρ₀ _ _ _ _ _ _ _).symm)
    · rintro ⟨𝒲, h𝒲, σ, ρ, h⟩
      exact ⟨𝒲, h𝒲, σ, ρ.comp ρ₀,
        h.of_ev_eq (fun _ _ _ _ _ _ _ => TwoCocycle.pull_pull_ev ρ ρ₀ _ _ _ _ _ _ _)⟩
  | coh 𝒰 h𝒰 c₁ c₂ hc =>
    have e := TwoCocycle.equivalence_rel (U := 𝒰.obj) hcomm
    constructor
    · rintro ⟨𝒲, h𝒲, σ, ρ, h⟩
      exact ⟨𝒲, h𝒲, σ, ρ, (TwoCocycle.equivalence_rel hcomm).trans h (hc.pull ρ.r ρ.f)⟩
    · rintro ⟨𝒲, h𝒲, σ, ρ, h⟩
      exact ⟨𝒲, h𝒲, σ, ρ, (TwoCocycle.equivalence_rel hcomm).trans h ((e.symm hc).pull ρ.r ρ.f)⟩

/-- Pulling a class back along two refinements gives the same class. -/
theorem H2.pull_eq_of_refines (𝒲 𝒰 : Cover.{w'} X) (σ σ' : 𝒲.Refines 𝒰) (z : H2 𝒰.obj 𝒜) :
    H2.pull σ.r σ.f z = H2.pull σ'.r σ'.f z := by
  induction z using Quot.ind with
  | mk c =>
    exact (TwoCocycle.class_eq_iff hcomm _ _).2
      (pullTwoCocycle_rel_of_two_refinements hcomm c σ.r σ'.r σ.f σ'.f)

/-- Pulling along a composite is pulling twice, on classes. -/
theorem H2.pull_comp {𝒵 𝒲 𝒰 : Cover.{w'} X} (τ : 𝒵.Refines 𝒲) (σ : 𝒲.Refines 𝒰)
    (z : H2 𝒰.obj 𝒜) :
    H2.pull τ.r τ.f (H2.pull σ.r σ.f z) = H2.pull (τ.comp σ).r (τ.comp σ).f z := by
  induction z using Quot.ind with
  | mk c =>
    exact (TwoCocycle.class_eq_iff hcomm _ _).2 (((TwoCocycle.equivalence_rel hcomm).refl _).of_ev_eq
      (fun _ _ _ _ _ _ _ => TwoCocycle.pull_pull_ev τ σ c _ _ _ _ _ _))

/-- A **good refinement** of `𝒱` relative to `𝒰₀`: an admissible cover refining
`𝒱` and `𝒰₀` such that pulling `H²` back from `𝒰₀` is a bijection. -/
def HasGoodRefinement (Cov : Cover.{w'} X → Prop) (𝒰₀ : Cover.{w'} X) (𝒜 : Cᵒᵖ ⥤ GrpCat.{w})
    (𝒱 : Cover.{w'} X) : Prop :=
  ∃ (𝒲 : Cover.{w'} X) (_ : Cov 𝒲) (_ : Nonempty (𝒲.Refines 𝒱)) (σ : 𝒲.Refines 𝒰₀),
    Function.Bijective (H2.pull (𝒜 := 𝒜) σ.r σ.f)

omit hcomm in
theorem cechClass_eq_cechClass_iff_aux (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (hdir : IsCoverDirected Cov) (𝒰₀ : Cover.{w'} X) (h₀ : Cov 𝒰₀) (c₁ c₂ : TwoCocycle 𝒰₀.obj 𝒜)
    (h : cechClass 𝒰₀ h₀ c₁ = cechClass 𝒰₀ h₀ c₂) :
    ∃ (𝒲 : Cover.{w'} X) (_ : Cov 𝒲) (σ : 𝒲.Refines 𝒰₀),
      TwoCocycle.Rel (c₁.pull σ.r σ.f) (c₂.pull σ.r σ.f) := by
  have key : ∀ a b : CoverCocycle 𝒜 Cov, Relation.EqvGen CoverCocycle.Step a b →
      (a.Agrees 𝒰₀ c₁ ↔ b.Agrees 𝒰₀ c₁) := by
    intro a b hab
    induction hab with
    | rel _ _ hs => exact agrees_step_iff hcomm hdir 𝒰₀ c₁ hs
    | refl => exact Iff.rfl
    | symm _ _ _ ih => exact ih.symm
    | trans _ _ _ _ _ ih₁ ih₂ => exact ih₁.trans ih₂
  have h1 : (⟨𝒰₀, h₀, c₁⟩ : CoverCocycle 𝒜 Cov).Agrees 𝒰₀ c₁ :=
    ⟨𝒰₀, h₀, Cover.Refines.id 𝒰₀, Cover.Refines.id 𝒰₀, (TwoCocycle.equivalence_rel hcomm).refl _⟩
  obtain ⟨𝒲, h𝒲, σ, ρ, hr⟩ := (key _ _ (Quot.eqvGen_exact h)).1 h1
  exact ⟨𝒲, h𝒲, σ, (TwoCocycle.equivalence_rel hcomm).trans hr
    (pullTwoCocycle_rel_of_two_refinements hcomm c₂ ρ.r σ.r ρ.f σ.f)⟩

/-- **Leray-type reduction.** On a directed system of covers, if every admissible
cover has a good refinement relative to `𝒰₀`, then `H²(𝒰₀) → Ȟ²` is a bijection. -/
theorem toCech_bijective_of_good (hdir : IsCoverDirected Cov) (𝒰₀ : Cover.{w'} X)
    (h₀ : Cov 𝒰₀) (hgood : ∀ 𝒱, Cov 𝒱 → HasGoodRefinement Cov 𝒰₀ 𝒜 𝒱) :
    Function.Bijective (H2.toCech (Cov := Cov) 𝒰₀ h₀ : H2 𝒰₀.obj 𝒜 → CechH2 𝒜 Cov) := by
  constructor
  · intro z₁ z₂ h
    induction z₁ using Quot.ind with
    | mk c₁ =>
    induction z₂ using Quot.ind with
    | mk c₂ =>
    obtain ⟨𝒲, h𝒲, σ, hr⟩ := cechClass_eq_cechClass_iff_aux hcomm hdir 𝒰₀ h₀ c₁ c₂ h
    obtain ⟨𝒲', _, ⟨τ⟩, σ', hbij⟩ := hgood 𝒲 h𝒲
    apply hbij.1
    show H2.pull σ'.r σ'.f c₁.class = H2.pull σ'.r σ'.f c₂.class
    rw [H2.pull_eq_of_refines hcomm 𝒲' 𝒰₀ σ' (τ.comp σ), H2.pull_eq_of_refines hcomm 𝒲' 𝒰₀ σ' (τ.comp σ),
      ← H2.pull_comp hcomm, ← H2.pull_comp hcomm]
    congr 1
    exact (TwoCocycle.class_eq_iff hcomm _ _).2 hr
  · intro x
    induction x using Quot.ind with
    | mk y =>
    obtain ⟨𝒱, h𝒱, c⟩ := y
    obtain ⟨𝒲, h𝒲, ⟨τ⟩, σ, hbij⟩ := hgood 𝒱 h𝒱
    obtain ⟨z, hz⟩ := hbij.2 (c.pull τ.r τ.f).class
    refine ⟨z, ?_⟩
    rw [← H2.toCech_pull 𝒰₀ 𝒲 h₀ h𝒲 σ z, hz]
    exact cechClass_pull 𝒱 𝒲 h𝒱 h𝒲 τ c

end QOU.CentralExtension.CechGerbe
