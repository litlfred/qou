import QOU.MathlibExt.CechKummerSurface

/-!
# Covers with a dominant member, and `KummerSurfaceData` for a point

Route R3 of the C-5a scoping (`lifting-and-descent`) reduces "the Kummer class of
a surface is trivial iff `n ∣ χ`" to the hypothesis class `KummerSurfaceData`
(`CechKummerSurface`). This file tests that class against the simplest space
where every field can be **proved**, not assumed.

## Results, all sorry-free

* `TwoCocycle.rel_one_of_dominant`: in a thin category (all hom-sets
  subsingletons, e.g. `Opens X`), a 2-cocycle of a commutative presheaf on a
  family with a **dominant** member `U o` (every `U i` maps to `U o`) is a
  coboundary. The witness is the textbook one, `α_ij := c_ijo`; the cocycle
  identity at `(i,j,k,o)` gives `c = δα`.
* `cechClass_eq_one_of_dominant`: in the colimit `Ȟ²`, the class of any cocycle on
  an admissible cover containing a member that receives a map from the covered
  object is trivial.
* `eq_cechClass_one_of_forall_dominant`: if **every** admissible cover has such
  a member, `Ȟ²` is a single point.
* `Cech.kummerSurfaceData_of_forall_dominant`: in that case `KummerSurfaceData`
  holds with both degrees zero.
* `Cech.kummerSurfaceData_point`: for a one-point space and the open-cover
  predicate, every field of `KummerSurfaceData` is discharged.

## What this does NOT do

This is a **consistency check, not the surface case**. It shows the hypotheses
of `KummerSurfaceData` are jointly satisfiable and that `degN_eq_zero_iff` is
provable where `Ȟ²(X, μₙ)` is trivial. For a point the Euler-characteristic
hypothesis `hχ` of `kummer_class_trivial_iff` forces `χ = 0`, so the theorem
there reads "always trivial", which is correct and carries no surface content.

Discharging `KummerSurfaceData` for a closed surface needs `Ȟ²(S, ℤ) ≅ ℤ` and
`Ȟ²(S, μₙ) ≅ ℤ/n` (Čech–singular comparison for good covers plus the
fundamental class); that remains open (bean `qou-skn4`).

-- Ref: [manuscript] lifting-and-descent, route R3 (consistency check)
-/

universe w' w v u

namespace QOU.CentralExtension.CechGerbe

open CategoryTheory Opposite TopologicalSpace

variable {C : Type u} [Category.{v} C] [Quiver.IsThin C]

section Dominant

variable {I : Type w'} {U : I → C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}

/-- **A cocycle on a family with a dominant member is a coboundary.** In a thin
category, if every `U i` maps to `U o`, then `c` is cohomologous to the trivial
cocycle, via `α_ij := c_ijo`. -/
theorem TwoCocycle.rel_one_of_dominant (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (c : TwoCocycle U 𝒜) (o : I) (s : ∀ i, U i ⟶ U o) :
    TwoCocycle.Rel TwoCocycle.one c := by
  let α : PresheafOfGroups.OneCochain 𝒜 U :=
    { ev := fun i j _ a b => c.ev i j o a b (a ≫ s i)
      ev_precomp := fun i j _ _ φ a b => by
        rw [c.ev_precomp, Category.assoc] }
  refine ⟨α, fun i j k T a b d => ?_⟩
  letI : CommGroup (𝒜.obj (op T)) := { (inferInstance : Group _) with mul_comm := hcomm _ }
  have hb : b ≫ s j = a ≫ s i := Subsingleton.elim _ _
  have hd : d ≫ s k = a ≫ s i := Subsingleton.elim _ _
  show c.ev i j k a b d = 1 * (c.ev i j o a b (a ≫ s i) * c.ev j k o b d (b ≫ s j) *
    (c.ev i k o a d (a ≫ s i))⁻¹)
  have hcoc := c.cocycle i j k o a b d (a ≫ s i)
  rw [hb, one_mul, eq_mul_inv_iff_mul_eq, mul_comm (c.ev i j o _ _ _), hcoc]

end Dominant

section Colimit

variable {X : C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}} {Cov : Cover.{w'} X → Prop}

/-- In the colimit `Ȟ²`, a cocycle on an admissible cover with a member `𝒰.obj o`
receiving a map from `X` has trivial class. -/
theorem cechClass_eq_one_of_dominant (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (𝒰 : Cover.{w'} X) (h𝒰 : Cov 𝒰) (o : 𝒰.ι) (t : X ⟶ 𝒰.obj o) (c : TwoCocycle 𝒰.obj 𝒜) :
    cechClass 𝒰 h𝒰 c = cechClass 𝒰 h𝒰 TwoCocycle.one :=
  (cechClass_eq_of_rel 𝒰 h𝒰 (TwoCocycle.rel_one_of_dominant hcomm c o
    (fun i => 𝒰.arr i ≫ t))).symm

/-- Any cover refines a cover with a member receiving a map from `X`. -/
def Cover.refinesDominant (𝒱 𝒰 : Cover.{w'} X) (o : 𝒰.ι) (t : X ⟶ 𝒰.obj o) :
    𝒱.Refines 𝒰 where
  r _ := o
  f j := 𝒱.arr j ≫ t
  w _ := Subsingleton.elim _ _

/-- **`Ȟ²` is a point when every admissible cover has a dominant member.** -/
theorem eq_cechClass_one_of_forall_dominant
    (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (hdom : ∀ 𝒰 : Cover.{w'} X, Cov 𝒰 → ∃ o, Nonempty (X ⟶ 𝒰.obj o))
    (x : CechH2 𝒜 Cov) (𝒰 : Cover.{w'} X) (h𝒰 : Cov 𝒰) :
    x = cechClass 𝒰 h𝒰 TwoCocycle.one := by
  induction x using Quot.ind with
  | mk y =>
    obtain ⟨𝒱, h𝒱, c⟩ := y
    obtain ⟨o, ⟨t⟩⟩ := hdom 𝒱 h𝒱
    obtain ⟨o', ⟨t'⟩⟩ := hdom 𝒰 h𝒰
    change cechClass 𝒱 h𝒱 c = _
    rw [cechClass_eq_one_of_dominant hcomm 𝒱 h𝒱 o t c,
      cechClass_one_pull 𝒰 𝒱 h𝒰 h𝒱 (Cover.refinesDominant 𝒱 𝒰 o' t')]

end Colimit

end QOU.CentralExtension.CechGerbe

namespace QOU.CentralExtension.Cech

open CategoryTheory Opposite TopologicalSpace CechGerbe

variable {X : Type} [TopologicalSpace X] (n : ℕ) [NeZero n]

/-- **`KummerSurfaceData` with both degrees zero**, whenever every admissible
cover of `X` has a member equal to the whole space. A consistency check on the
hypothesis class, not a surface statement. -/
noncomputable def kummerSurfaceData_of_forall_dominant {Cov : Cover.{0} (⊤ : Opens X) → Prop}
    (hdom : ∀ 𝒰 : Cover.{0} (⊤ : Opens X), Cov 𝒰 → ∃ o, Nonempty ((⊤ : Opens X) ⟶ 𝒰.obj o)) :
    KummerSurfaceData X n Cov where
  deg _ := 0
  degN _ := 0
  degN_eq_zero_iff 𝒰 h𝒰 x :=
    ⟨fun _ => eq_cechClass_one_of_forall_dominant contPresheaf_comm hdom x 𝒰 h𝒰,
      fun _ => rfl⟩
  degN_map _ := by simp

/-- The open-cover predicate on covers of `⊤ : Opens X`: the members cover `X`. -/
def IsOpenCover (𝒰 : Cover.{0} (⊤ : Opens X)) : Prop := ⊤ ≤ ⨆ i, 𝒰.obj i

/-- On a one-point space, every open cover contains the whole space. -/
theorem exists_top_of_isOpenCover [Unique X] (𝒰 : Cover.{0} (⊤ : Opens X))
    (h𝒰 : IsOpenCover 𝒰) : ∃ o, Nonempty ((⊤ : Opens X) ⟶ 𝒰.obj o) := by
  have hx : (default : X) ∈ ⨆ i, 𝒰.obj i := h𝒰 (Set.mem_univ _)
  obtain ⟨o, ho⟩ := Opens.mem_iSup.1 hx
  refine ⟨o, ⟨homOfLE fun y _ => ?_⟩⟩
  rwa [Unique.eq_default y]

/-- **`KummerSurfaceData` for a point**, with every field proved. -/
noncomputable def kummerSurfaceData_point [Unique X] :
    KummerSurfaceData X n IsOpenCover :=
  kummerSurfaceData_of_forall_dominant n fun 𝒰 h𝒰 => exists_top_of_isOpenCover 𝒰 h𝒰

end QOU.CentralExtension.Cech
