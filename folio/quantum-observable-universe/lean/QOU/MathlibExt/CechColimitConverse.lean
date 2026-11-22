import QOU.MathlibExt.CechColimit
import Mathlib.CategoryTheory.Limits.Shapes.Pullback.HasPullback
import Mathlib.CategoryTheory.Sites.Grothendieck

/-!
# The converse for the colimit `Ȟ²`: trivial class ⇒ lift on a finer cover

Step G1b of the gerbe layer (bean `qou-skn4`), on top of
`QOU.MathlibExt.CechColimit`. All results are sorry-free, and no step is
assumed: the two inputs a filtered colimit needs are both **constructed**.

## Infrastructure built here

* `pullTwoCocycle_rel_of_two_refinements` (**prism homotopy**): two refinement
  maps `𝒲 → 𝒰` pull a 2-cocycle of a commutative presheaf back to
  **cohomologous** 2-cocycles. The homotopy is the classical prism operator
  `h_jk = c(P_j, Q_j, Q_k) − c(P_j, P_k, Q_k)`, and the identity
  `δh = c(Q) − c(P)` uses the cocycle condition three times
  (`core_prism`).
* `Cover.Refines.id`, `Cover.Refines.comp`: refinements compose.
* `Cover.meet`: the **common refinement** of two covers of `X`, built from
  pullbacks `V_j ×_X W_k` in `C` (`[HasPullbacks C]`), with
  `Cover.meetLeft`, `Cover.meetRight`.
* `Cover.generate_meet_mem`: for a Grothendieck topology `J`, if both covers
  generate `J`-covering sieves, so does their meet. So the covers of a site
  form a directed system (`IsCoverDirected`, `isCoverDirected_topology`).

## The converse

* `cechClass_eq_one_iff`: on a directed system of covers, a cocycle's class in
  the colimit is trivial **iff** its pullback to some admissible refinement is
  a coboundary.
* `PresheafCentralExtension.cechObstruction_eq_one_iff`: the `𝒢`-torsor `γ`
  has trivial colimit obstruction class **iff** it lifts to an `𝓔`-torsor on
  some admissible refinement. Together with G1 this is the cover-independent
  form of the lifting criterion.

The method: "becomes a coboundary on some admissible refinement" is a
predicate on cover-cocycle pairs that is invariant, in both directions, under
each generating step of the colimit relation; so it is invariant under its
equivalence closure.
-/

-- Ref: [manuscript] lifting-and-descent, bean qou-skn4 (gerbe layer G1b)

universe w' w v u

namespace QOU.CentralExtension.CechGerbe

open CategoryTheory Opposite Limits QOU.CentralExtension

variable {C : Type u} [Category.{v} C]

/-! ### The prism homotopy -/

/-- The algebraic core of the prism homotopy, in a commutative group. -/
theorem core_prism {G : Type*} [CommGroup G] (Q P A B D E F H K L : G)
    (h1 : A * B = Q * D) (h2 : E * B = F * H) (h3 : P * K = L * H) :
    Q = P * (A * E⁻¹ * (F * L⁻¹) * (D * K⁻¹)⁻¹) := by
  have hQ : Q = A * B * D⁻¹ := (eq_mul_inv_of_mul_eq h1.symm)
  have hB : B = E⁻¹ * (F * H) := eq_inv_mul_of_mul_eq h2
  have hH : H = L⁻¹ * (P * K) := eq_inv_mul_of_mul_eq h3.symm
  rw [hQ, hB, hH]
  simp only [mul_inv_rev, inv_inv]
  ac_rfl

section Homotopy

variable {I J : Type w'} {U : I → C} {V : J → C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}

/-- The prism 1-cochain comparing two refinements `(r, f)` and `(r', f')`. -/
def prismCochain (c : TwoCocycle U 𝒜) (r r' : J → I) (f : ∀ j, V j ⟶ U (r j))
    (f' : ∀ j, V j ⟶ U (r' j)) : PresheafOfGroups.OneCochain 𝒜 V where
  ev j k _ a b :=
    c.ev (r j) (r' j) (r' k) (a ≫ f j) (a ≫ f' j) (b ≫ f' k) *
      (c.ev (r j) (r k) (r' k) (a ≫ f j) (b ≫ f k) (b ≫ f' k))⁻¹
  ev_precomp j k T T' φ a b := by
    simp only [map_mul, map_inv, TwoCochain.ev_precomp, Category.assoc]

/-- **Prism homotopy.** Two refinement maps pull a 2-cocycle of a commutative
presheaf back to cohomologous 2-cocycles. -/
theorem pullTwoCocycle_rel_of_two_refinements
    (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (c : TwoCocycle U 𝒜) (r r' : J → I) (f : ∀ j, V j ⟶ U (r j))
    (f' : ∀ j, V j ⟶ U (r' j)) :
    TwoCocycle.Rel (c.pull r f) (c.pull r' f') := by
  refine ⟨prismCochain c r r' f f', fun j k l T a b d => ?_⟩
  letI : CommGroup (𝒜.obj (op T)) := { (inferInstance : Group _) with mul_comm := hcomm _ }
  simp only [TwoCocycle.pull_ev, prismCochain]
  exact core_prism _ _ _ _ _ _ _ _ _ _
    (c.cocycle (r j) (r' j) (r' k) (r' l) (a ≫ f j) (a ≫ f' j) (b ≫ f' k) (d ≫ f' l))
    (c.cocycle (r j) (r k) (r' k) (r' l) (a ≫ f j) (b ≫ f k) (b ≫ f' k) (d ≫ f' l))
    (c.cocycle (r j) (r k) (r l) (r' l) (a ≫ f j) (b ≫ f k) (d ≫ f l) (d ≫ f' l))

end Homotopy

/-! ### Small facts about `Rel` -/

section RelFacts

variable {I : Type w'} {U : I → C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}

/-- `Rel` only sees the values of the second cocycle. -/
theorem TwoCocycle.Rel.of_ev_eq {c₁ c₂ c₂' : TwoCocycle U 𝒜} (h : TwoCocycle.Rel c₁ c₂)
    (he : ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (d : T ⟶ U k),
      c₂.ev i j k a b d = c₂'.ev i j k a b d) : TwoCocycle.Rel c₁ c₂' := by
  obtain ⟨α, hα⟩ := h
  exact ⟨α, fun i j k T a b d => by rw [← he, hα]⟩

end RelFacts

/-! ### Composing refinements, and the common refinement from pullbacks -/

/-- The identity refinement. -/
def Cover.Refines.id {X : C} (𝒰 : Cover.{w'} X) : 𝒰.Refines 𝒰 where
  r := fun i => i
  f := fun _ => 𝟙 _
  w := fun _ => Category.id_comp _

/-- Refinements compose. -/
def Cover.Refines.comp {X : C} {𝒲 𝒱 𝒰 : Cover.{w'} X} (σ : 𝒲.Refines 𝒱)
    (ρ : 𝒱.Refines 𝒰) : 𝒲.Refines 𝒰 where
  r := fun j => ρ.r (σ.r j)
  f := fun j => σ.f j ≫ ρ.f (σ.r j)
  w := fun j => by rw [Category.assoc, ρ.w, σ.w]

theorem TwoCocycle.pull_pull_ev {X : C} {𝒲 𝒱 𝒰 : Cover.{w'} X} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}
    (σ : 𝒲.Refines 𝒱) (ρ : 𝒱.Refines 𝒰) (c : TwoCocycle 𝒰.obj 𝒜) (j j' j'' : 𝒲.ι) ⦃T : C⦄
    (a : T ⟶ 𝒲.obj j) (b : T ⟶ 𝒲.obj j') (d : T ⟶ 𝒲.obj j'') :
    ((c.pull ρ.r ρ.f).pull σ.r σ.f).ev j j' j'' a b d =
      (c.pull (σ.comp ρ).r (σ.comp ρ).f).ev j j' j'' a b d := by
  simp [Cover.Refines.comp, Category.assoc]

/-- The common refinement of two covers of `X`: the family of pullbacks
`V_j ×_X W_k`. -/
noncomputable def Cover.meet [HasPullbacks C] {X : C} (𝒱 𝒲 : Cover.{w'} X) : Cover.{w'} X where
  ι := 𝒱.ι × 𝒲.ι
  obj p := pullback (𝒱.arr p.1) (𝒲.arr p.2)
  arr p := pullback.fst _ _ ≫ 𝒱.arr p.1

/-- The meet refines the first cover. -/
noncomputable def Cover.meetLeft [HasPullbacks C] {X : C} (𝒱 𝒲 : Cover.{w'} X) :
    (𝒱.meet 𝒲).Refines 𝒱 where
  r := Prod.fst
  f := fun _ => pullback.fst _ _
  w := fun _ => rfl

/-- The meet refines the second cover. -/
noncomputable def Cover.meetRight [HasPullbacks C] {X : C} (𝒱 𝒲 : Cover.{w'} X) :
    (𝒱.meet 𝒲).Refines 𝒲 where
  r := Prod.snd
  f := fun _ => pullback.snd _ _
  w := fun _ => pullback.condition.symm

/-- The sieve generated by a cover. -/
def Cover.sieve {X : C} (𝒰 : Cover.{w'} X) : Sieve X :=
  Sieve.generate (Presieve.ofArrows 𝒰.obj 𝒰.arr)

/-- The meet's sieve contains the intersection of the two sieves. -/
theorem Cover.sieve_inf_le_meet [HasPullbacks C] {X : C} (𝒱 𝒲 : Cover.{w'} X) :
    𝒱.sieve ⊓ 𝒲.sieve ≤ (𝒱.meet 𝒲).sieve := by
  rintro Y g ⟨⟨Z, h, _, ⟨j⟩, rfl⟩, ⟨Z', h', _, ⟨k⟩, he⟩⟩
  refine ⟨pullback (𝒱.arr j) (𝒲.arr k), pullback.lift h h' he.symm,
    pullback.fst _ _ ≫ 𝒱.arr j, Presieve.ofArrows.mk (j, k), ?_⟩
  simp

/-- For a Grothendieck topology, the meet of two covering covers is covering. -/
theorem Cover.generate_meet_mem [HasPullbacks C] (Jt : GrothendieckTopology C) {X : C}
    (𝒱 𝒲 : Cover.{w'} X) (h𝒱 : 𝒱.sieve ∈ Jt X) (h𝒲 : 𝒲.sieve ∈ Jt X) :
    (𝒱.meet 𝒲).sieve ∈ Jt X :=
  Jt.superset_covering (Cover.sieve_inf_le_meet 𝒱 𝒲) (Jt.intersection_covering h𝒱 h𝒲)

/-- A predicate on covers is **directed** if any two admissible covers have an
admissible common refinement. -/
def IsCoverDirected {X : C} (Cov : Cover.{w'} X → Prop) : Prop :=
  ∀ 𝒱 𝒲 : Cover.{w'} X, Cov 𝒱 → Cov 𝒲 →
    ∃ 𝒵 : Cover.{w'} X, Cov 𝒵 ∧ Nonempty (𝒵.Refines 𝒱) ∧ Nonempty (𝒵.Refines 𝒲)

/-- Admissibility closed under meets gives a directed system. -/
theorem isCoverDirected_of_meet [HasPullbacks C] {X : C} (Cov : Cover.{w'} X → Prop)
    (hmeet : ∀ 𝒱 𝒲, Cov 𝒱 → Cov 𝒲 → Cov (𝒱.meet 𝒲)) : IsCoverDirected Cov :=
  fun 𝒱 𝒲 h𝒱 h𝒲 => ⟨𝒱.meet 𝒲, hmeet 𝒱 𝒲 h𝒱 h𝒲, ⟨𝒱.meetLeft 𝒲⟩, ⟨𝒱.meetRight 𝒲⟩⟩

/-- **The covers of a site are directed.** For a Grothendieck topology on a
category with pullbacks, "generates a covering sieve" is a directed predicate. -/
theorem isCoverDirected_topology [HasPullbacks C] (Jt : GrothendieckTopology C) (X : C) :
    IsCoverDirected (fun 𝒰 : Cover.{w'} X => 𝒰.sieve ∈ Jt X) :=
  isCoverDirected_of_meet _ (fun 𝒱 𝒲 h𝒱 h𝒲 => Cover.generate_meet_mem Jt 𝒱 𝒲 h𝒱 h𝒲)

/-! ### The converse -/

section Converse

variable {X : C} {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}} {Cov : Cover.{w'} X → Prop}

/-- A cover-cocycle pair **becomes trivial** if its pullback to some admissible
refinement is a coboundary. -/
def CoverCocycle.EventuallyTrivial (x : CoverCocycle 𝒜 Cov) : Prop :=
  ∃ (𝒲 : Cover.{w'} X) (_ : Cov 𝒲) (ρ : 𝒲.Refines x.cov),
    TwoCocycle.Rel TwoCocycle.one (x.c.pull ρ.r ρ.f)

variable (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x) (hdir : IsCoverDirected Cov)
include hcomm

theorem eventuallyTrivial_step_iff {x y : CoverCocycle 𝒜 Cov} (hs : CoverCocycle.Step x y)
    (hdir : IsCoverDirected Cov) :
    x.EventuallyTrivial ↔ y.EventuallyTrivial := by
  cases hs with
  | refine x 𝒱 h𝒱 ρ =>
    constructor
    · rintro ⟨𝒲, h𝒲, σ, hσ⟩
      obtain ⟨𝒵, h𝒵, ⟨τ₁⟩, ⟨τ₂⟩⟩ := hdir 𝒲 𝒱 h𝒲 h𝒱
      refine ⟨𝒵, h𝒵, τ₂, ?_⟩
      have e := (TwoCocycle.equivalence_rel (U := 𝒵.obj) hcomm)
      have h1 : TwoCocycle.Rel TwoCocycle.one (x.c.pull (τ₁.comp σ).r (τ₁.comp σ).f) :=
        (hσ.pull τ₁.r τ₁.f).of_ev_eq (fun _ _ _ _ _ _ _ => TwoCocycle.pull_pull_ev τ₁ σ _ _ _ _ _ _ _)
      have h2 := pullTwoCocycle_rel_of_two_refinements hcomm x.c (τ₁.comp σ).r (τ₂.comp ρ).r
        (τ₁.comp σ).f (τ₂.comp ρ).f
      exact (e.trans h1 h2).of_ev_eq
        (fun _ _ _ _ _ _ _ => (TwoCocycle.pull_pull_ev τ₂ ρ _ _ _ _ _ _ _).symm)
    · rintro ⟨𝒲, h𝒲, σ, hσ⟩
      exact ⟨𝒲, h𝒲, σ.comp ρ,
        hσ.of_ev_eq (fun _ _ _ _ _ _ _ => TwoCocycle.pull_pull_ev σ ρ _ _ _ _ _ _ _)⟩
  | coh 𝒰 h𝒰 c₁ c₂ h =>
    have e := (TwoCocycle.equivalence_rel (U := 𝒰.obj) hcomm)
    constructor
    · rintro ⟨𝒲, h𝒲, σ, hσ⟩
      exact ⟨𝒲, h𝒲, σ, (TwoCocycle.equivalence_rel hcomm).trans hσ (h.pull σ.r σ.f)⟩
    · rintro ⟨𝒲, h𝒲, σ, hσ⟩
      exact ⟨𝒲, h𝒲, σ,
        (TwoCocycle.equivalence_rel hcomm).trans hσ ((e.symm h).pull σ.r σ.f)⟩

include hdir in
/-- **The converse, for cocycles.** On a directed system of covers, a cocycle's
class in the colimit `Ȟ²` is trivial iff it becomes a coboundary on some
admissible refinement. -/
theorem cechClass_eq_one_iff (𝒰 : Cover.{w'} X) (h𝒰 : Cov 𝒰) (c : TwoCocycle 𝒰.obj 𝒜) :
    cechClass 𝒰 h𝒰 c = cechClass 𝒰 h𝒰 TwoCocycle.one ↔
      ∃ (𝒲 : Cover.{w'} X) (_ : Cov 𝒲) (ρ : 𝒲.Refines 𝒰),
        TwoCocycle.Rel TwoCocycle.one (c.pull ρ.r ρ.f) := by
  constructor
  · intro h
    have key : ∀ a b : CoverCocycle 𝒜 Cov, Relation.EqvGen CoverCocycle.Step a b →
        (a.EventuallyTrivial ↔ b.EventuallyTrivial) := by
      intro a b hab
      induction hab with
      | rel _ _ hs => exact eventuallyTrivial_step_iff hcomm hs hdir
      | refl => exact Iff.rfl
      | symm _ _ _ ih => exact ih.symm
      | trans _ _ _ _ _ ih₁ ih₂ => exact ih₁.trans ih₂
    have h1 : (⟨𝒰, h𝒰, TwoCocycle.one⟩ : CoverCocycle 𝒜 Cov).EventuallyTrivial :=
      ⟨𝒰, h𝒰, Cover.Refines.id 𝒰, (TwoCocycle.equivalence_rel hcomm).refl _⟩
    exact (key _ _ (Quot.eqvGen_exact h)).2 h1
  · rintro ⟨𝒲, h𝒲, ρ, hρ⟩
    rw [← cechClass_pull 𝒰 𝒲 h𝒰 h𝒲 ρ c, ← cechClass_pull 𝒰 𝒲 h𝒰 h𝒲 ρ TwoCocycle.one]
    exact (cechClass_eq_of_rel 𝒲 h𝒲 hρ).symm

end Converse

end QOU.CentralExtension.CechGerbe

/-! ### The cover-independent lifting criterion -/

namespace QOU.CentralExtension.PresheafCentralExtension

open CategoryTheory Opposite QOU.CentralExtension QOU.CentralExtension.CechGerbe

variable {C : Type u} [Category.{v} C]
variable {X : C} {𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}} (E : PresheafCentralExtension 𝒜 𝓔 𝒢)
variable {Cov : Cover.{w'} X → Prop} (hdir : IsCoverDirected Cov) (𝒰 : Cover.{w'} X) (h𝒰 : Cov 𝒰)
variable (γ : PresheafOfGroups.OneCocycle 𝒢 𝒰.obj) (ξ : PresheafOfGroups.OneCochain 𝓔 𝒰.obj)
  (hξ : ∀ (i j : 𝒰.ι) ⦃T : C⦄ (a : T ⟶ 𝒰.obj i) (b : T ⟶ 𝒰.obj j),
    E.π.app (op T) (ξ.ev i j a b) = γ.ev i j a b)

include hdir in
/-- **Cover-independent lifting criterion.** On a directed system of covers
(for example, the covers of a site with pullbacks, `isCoverDirected_topology`),
the colimit obstruction class of `γ` is trivial iff `γ` lifts to an
`𝓔`-torsor on some admissible refinement. -/
theorem cechObstruction_eq_one_iff :
    E.cechObstruction 𝒰 h𝒰 γ ξ hξ = cechClass 𝒰 h𝒰 TwoCocycle.one ↔
      ∃ (𝒲 : Cover.{w'} X) (_ : Cov 𝒲) (ρ : 𝒲.Refines 𝒰)
        (η : PresheafOfGroups.OneCocycle 𝓔 𝒲.obj), ∀ (j j' : 𝒲.ι) ⦃T : C⦄
          (a : T ⟶ 𝒲.obj j) (b : T ⟶ 𝒲.obj j'),
          E.π.app (op T) (η.ev j j' a b) = (pullOneCocycle 𝒰.obj ρ.r ρ.f γ).ev j j' a b := by
  rw [cechObstruction, cechClass_eq_one_iff E.comm hdir]
  refine exists_congr fun 𝒲 => exists_congr fun h𝒲 => exists_congr fun ρ => ?_
  have hξρ : ∀ (j j' : 𝒲.ι) ⦃T : C⦄ (a : T ⟶ 𝒲.obj j) (b : T ⟶ 𝒲.obj j'),
      E.π.app (op T) ((pullOneCochain 𝒰.obj ρ.r ρ.f ξ).ev j j' a b) =
        (pullOneCocycle 𝒰.obj ρ.r ρ.f γ).ev j j' a b :=
    fun j j' _ a b => hξ (ρ.r j) (ρ.r j') (a ≫ ρ.f j) (b ≫ ρ.f j')
  rw [E.exists_lift_iff (pullOneCocycle 𝒰.obj ρ.r ρ.f γ) (pullOneCochain 𝒰.obj ρ.r ρ.f ξ) hξρ,
    E.obstruction_pull γ ξ hξ ρ.r ρ.f]
  constructor
  · rintro ⟨α, hα⟩
    refine ⟨α, fun j j' j'' T a b d => ?_⟩
    have := hα j j' j'' a b d
    simp only [TwoCocycle.one, one_mul] at this ⊢
    exact this
  · rintro ⟨α, hα⟩
    exact ⟨α, fun j j' j'' T a b d => by
      have := hα j j' j'' a b d
      simp only [TwoCocycle.one, one_mul] at this ⊢
      exact this⟩

end QOU.CentralExtension.PresheafCentralExtension
