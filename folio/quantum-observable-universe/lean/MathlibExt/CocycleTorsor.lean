import MathlibExt.StackGerbe
import Mathlib.CategoryTheory.Sites.Sieves

/-!
# Effective descent of torsors: the torsor glued from a 1-cocycle

Beans `qou-t1dx` and `qou-skn4` (parent `qou-533l`), design D3. The open item
recorded there is **effective descent of objects**: gluing an `A`-torsor from a
1-cocycle. This file does that over a small site.

Setting: a small site `(C, J)`, a presheaf of groups `A` that is a `J`-sheaf,
and a family of objects `U : I → C` that covers the final object
(`∀ T, Sieve.ofObjects U T ∈ J T`, Mathlib's `J.CoversTop U`: every object is covered by maps into the `U i`).

* `TorsCocycle A U`: a Čech 1-cocycle of `A` on `U`, in the form Mathlib uses
  for nonabelian `H¹` (`gᵢⱼ` defined on every `V` with maps to `U i` and `U j`,
  natural in `V`, and `gᵢⱼ gⱼₖ = gᵢₖ`).
* `TwistedSection g T`: compatible local data `xᵢ(h, a) ∈ A(V)` for
  `h : V ⟶ T`, `a : V ⟶ U i`, with `xᵢ = gᵢⱼ xⱼ`.
* `twistedPresheaf g`: these sections form a presheaf, and `twistedAction g`
  is the action of `A` by `c · x = x (c|_V)⁻¹`.
* `isSheaf_twistedPresheaf`: it is a `J`-sheaf when `A` is.
* `isPseudoTorsor_twistedAction`, `locallyNonempty_twistedPresheaf`,
  `isMulAction_twistedAction`.
* `cocycleTorsor g : MulSheafTorsor J A`, the **glued torsor**.
* `cocycleSection` and `cocycleSection_transition`: over `U i` the torsor has
  a canonical section `sᵢ`, and over any `V` mapping to `U i` and `U j` the
  restrictions satisfy `sᵢ|_V = gᵢⱼ · sⱼ|_V`. So the transition cocycle of the
  glued torsor, read off from these sections, is the cocycle we started from.

Not done here: the converse half of descent (every torsor that is trivial on
each `U i` is isomorphic to `cocycleTorsor` of its transition cocycle), and
the comparison of `cocycleTorsor` with Mathlib's `H¹` (whose `OneCocycle` uses
`GrpCat`-valued presheaves rather than type-valued ones with group structure).

Everything is sorry-free and generic: `A` is any sheaf of groups on any small
site. Nothing archimedean is used.

## Source

Yekutieli, *Central Extensions of Gerbes* (arXiv 0801.0083, held at
`library/arxiv-0801.0083v4/`), §1–2 (descent for torsors); Giraud, *Cohomologie
non abélienne*, III.2.4.
-/

-- Ref: [yekutieli2010] §1–2, effective descent for torsors

universe w

namespace QOU.MathlibExt.StackGerbe

open CategoryTheory Opposite

variable {C : Type w} [Category.{w} C] {I : Type w} {U : I → C}
variable {A : Cᵒᵖ ⥤ Type w} [∀ T : Cᵒᵖ, Group (A.obj T)]

theorem IsPresheafOfGroups.map_inv (hA : IsPresheafOfGroups A) {T T' : Cᵒᵖ} (f : T ⟶ T')
    (a : A.obj T) : A.map f a⁻¹ = (A.map f a)⁻¹ := by
  rw [eq_inv_iff_mul_eq_one, ← hA.map_mul, inv_mul_cancel, hA.map_one]

variable (A U) in
/-- A **Čech 1-cocycle** of `A` on the family `U`. -/
structure TorsCocycle where
  /-- The transition function `gᵢⱼ` on `V` (given maps `V ⟶ U i`, `V ⟶ U j`). -/
  ev : ∀ (i j : I) ⦃V : C⦄ (_a : V ⟶ U i) (_b : V ⟶ U j), A.obj (op V)
  /-- Naturality in `V`. -/
  ev_precomp : ∀ (i j : I) ⦃V V' : C⦄ (φ : V' ⟶ V) (a : V ⟶ U i) (b : V ⟶ U j),
    A.map φ.op (ev i j a b) = ev i j (φ ≫ a) (φ ≫ b)
  /-- The cocycle identity `gᵢⱼ gⱼₖ = gᵢₖ`. -/
  ev_trans : ∀ (i j k : I) ⦃V : C⦄ (a : V ⟶ U i) (b : V ⟶ U j) (c : V ⟶ U k),
    ev i j a b * ev j k b c = ev i k a c

variable (g : TorsCocycle U A)

/-- A **twisted section** of the cocycle `g` over `T`. -/
@[ext]
structure TwistedSection (T : C) where
  /-- The local value `xᵢ(h, a)`. -/
  val : ∀ (i : I) ⦃V : C⦄ (_h : V ⟶ T) (_a : V ⟶ U i), A.obj (op V)
  /-- Naturality in `V`. -/
  val_precomp : ∀ (i : I) ⦃V V' : C⦄ (φ : V' ⟶ V) (h : V ⟶ T) (a : V ⟶ U i),
    A.map φ.op (val i h a) = val i (φ ≫ h) (φ ≫ a)
  /-- The twisting rule `xᵢ = gᵢⱼ xⱼ`. -/
  val_twist : ∀ (i j : I) ⦃V : C⦄ (h : V ⟶ T) (a : V ⟶ U i) (b : V ⟶ U j),
    val i h a = g.ev i j a b * val j h b

variable {g}

theorem TwistedSection.val_congr {T : C} (x : TwistedSection g T) (i : I) {V : C}
    {h h' : V ⟶ T} {a a' : V ⟶ U i} (hh : h = h') (ha : a = a') :
    x.val i h a = x.val i h' a' := by subst hh; subst ha; rfl

/-- Restriction of a twisted section along `f : T' ⟶ T`. -/
def TwistedSection.restrict {T T' : C} (f : T' ⟶ T) (x : TwistedSection g T) :
    TwistedSection g T' where
  val i _ h a := x.val i (h ≫ f) a
  val_precomp i _ _ φ h a := by rw [x.val_precomp]; exact x.val_congr i (by simp) rfl
  val_twist i j _ h a b := x.val_twist i j _ a b

variable (g) in
/-- The presheaf of twisted sections. -/
def twistedPresheaf : Cᵒᵖ ⥤ Type w where
  obj T := TwistedSection g T.unop
  map f x := x.restrict f.unop
  map_id _ := by funext x; refine TwistedSection.ext ?_; funext i V h a; exact x.val_congr i (by simp) rfl
  map_comp _ _ := by funext x; refine TwistedSection.ext ?_; funext i V h a; exact x.val_congr i (by simp) rfl

@[simp]
theorem twistedPresheaf_map_val {T T' : Cᵒᵖ} (f : T ⟶ T') (x : (twistedPresheaf g).obj T)
    (i : I) {V : C} (h : V ⟶ T'.unop) (a : V ⟶ U i) :
    ((twistedPresheaf g).map f x).val i h a = x.val i (h ≫ f.unop) a := rfl

variable (g) in
/-- The action of `A` on twisted sections: `c · x = x (c|_V)⁻¹`. -/
def twistedAction (hA : IsPresheafOfGroups A) : PresheafAction A (twistedPresheaf g) where
  smul T c x :=
    { val := fun i _ h a => x.val i h a * (A.map h.op c)⁻¹
      val_precomp := fun i _ _ φ h a => by
        rw [hA.map_mul, hA.map_inv, x.val_precomp, ← FunctorToTypes.map_comp_apply]
        rfl
      val_twist := fun i j _ h a b => by rw [x.val_twist i j h a b, mul_assoc] }
  map_smul f c x := by
    refine TwistedSection.ext ?_; funext i V h a
    change x.val i (h ≫ f.unop) a * (A.map (h ≫ f.unop).op c)⁻¹ =
      x.val i (h ≫ f.unop) a * (A.map h.op (A.map f c))⁻¹
    rw [← FunctorToTypes.map_comp_apply]
    rfl

theorem twistedAction_val (hA : IsPresheafOfGroups A) (T : Cᵒᵖ) (c : A.obj T)
    (x : (twistedPresheaf g).obj T) (i : I) {V : C} (h : V ⟶ T.unop) (a : V ⟶ U i) :
    ((twistedAction g hA).smul T c x).val i h a = x.val i h a * (A.map h.op c)⁻¹ := rfl

theorem isMulAction_twistedAction (hA : IsPresheafOfGroups A) :
    (twistedAction g hA).IsMulAction where
  one_smul T x := by
    refine TwistedSection.ext ?_; funext i V h a
    rw [twistedAction_val, hA.map_one, inv_one, mul_one]
  mul_smul T c d x := by
    refine TwistedSection.ext ?_; funext i V h a
    rw [twistedAction_val, twistedAction_val, twistedAction_val, hA.map_mul, mul_inv_rev,
      mul_assoc]

/-! ### Local sections -/

theorem TorsCocycle.ev_self (i : I) {V : C} (a : V ⟶ U i) : g.ev i i a a = 1 := by
  have h := g.ev_trans i i i a a a
  exact mul_eq_left.mp h

/-- Over `V` with a map `a : V ⟶ U i`, the twisted section `xⱼ(h, b) = gⱼᵢ(b, h a)`. -/
def localSection (i : I) {V : C} (a : V ⟶ U i) : TwistedSection g V where
  val j _ h b := g.ev j i b (h ≫ a)
  val_precomp j _ _ φ h b := by rw [g.ev_precomp, Category.assoc]
  val_twist j k _ h b c := (g.ev_trans j k i b c (h ≫ a)).symm

theorem localSection_val (i : I) {V : C} (a : V ⟶ U i) (j : I) {W : C} (h : W ⟶ V)
    (b : W ⟶ U j) : (localSection (g := g) i a).val j h b = g.ev j i b (h ≫ a) := rfl

variable {J : GrothendieckTopology C}

theorem locallyNonempty_twistedPresheaf (hU : ∀ T : C, Sieve.ofObjects U T ∈ J T) :
    LocallyNonempty J (twistedPresheaf g) := by
  intro T
  refine J.superset_covering ?_ (hU T)
  rintro V f ⟨i, ⟨a⟩⟩
  exact ⟨localSection i a⟩

/-! ### The action is simply transitive -/

/-- `yᵢ⁻¹ xᵢ` does not depend on `i`. -/
theorem quot_indep {T : C} (x y : TwistedSection g T) (i j : I) {V : C} (h : V ⟶ T)
    (a : V ⟶ U i) (b : V ⟶ U j) :
    (y.val i h a)⁻¹ * x.val i h a = (y.val j h b)⁻¹ * x.val j h b := by
  rw [x.val_twist i j h a b, y.val_twist i j h a b, mul_inv_rev, mul_assoc,
    inv_mul_cancel_left]

/-- The family `h ↦ yᵢ(h, a)⁻¹ xᵢ(h, a)` on the sieve `Sieve.ofObjects U T`. -/
noncomputable def quotFamily {T : C} (x y : TwistedSection g T) :
    Presieve.FamilyOfElements A (Sieve.ofObjects U T).arrows :=
  fun _ h hh => (y.val hh.choose h hh.choose_spec.some)⁻¹ * x.val hh.choose h hh.choose_spec.some

theorem quotFamily_eq {T : C} (x y : TwistedSection g T) {V : C} (h : V ⟶ T)
    (hh : (Sieve.ofObjects U T).arrows h) (i : I) (a : V ⟶ U i) :
    quotFamily x y h hh = (y.val i h a)⁻¹ * x.val i h a :=
  quot_indep x y _ _ h _ _

theorem quotFamily_compatible (hA : IsPresheafOfGroups A) {T : C} (x y : TwistedSection g T) :
    (quotFamily x y).Compatible := by
  rw [Presieve.compatible_iff_sieveCompatible]
  intro V W h φ hh
  obtain ⟨i, ⟨a⟩⟩ := hh
  rw [quotFamily_eq x y (φ ≫ h) _ i (φ ≫ a), quotFamily_eq x y h ⟨i, ⟨a⟩⟩ i a, hA.map_mul,
    hA.map_inv, x.val_precomp, y.val_precomp]

theorem isPseudoTorsor_twistedAction (hA : IsPresheafOfGroups A) (hAs : Presheaf.IsSheaf J A)
    (hU : ∀ T : C, Sieve.ofObjects U T ∈ J T) : (twistedAction g hA).IsPseudoTorsor := by
  intro T x y
  have H := ((isSheaf_iff_isSheaf_of_type J A).mp hAs) _ (hU T.unop)
  have hc := quotFamily_compatible hA x y
  refine ⟨H.amalgamate _ hc, ?_, ?_⟩
  · refine TwistedSection.ext ?_; funext i V h a
    rw [twistedAction_val, H.valid_glue hc h ⟨i, ⟨a⟩⟩, quotFamily_eq x y h _ i a, mul_inv_rev,
      inv_inv, mul_inv_cancel_left]
  · intro c hcy
    apply H.isSeparatedFor.ext
    rintro V h ⟨i, ⟨a⟩⟩
    rw [H.valid_glue hc h ⟨i, ⟨a⟩⟩, quotFamily_eq x y h _ i a]
    have e := congrArg (fun z : TwistedSection g T.unop => z.val i h a) hcy
    simp only [twistedAction_val] at e
    rw [← e, mul_inv_rev, inv_inv, inv_mul_cancel_right]

/-! ### The presheaf of twisted sections is a sheaf -/

section Sheaf

/-- The local family used to glue a compatible family of twisted sections. -/
noncomputable def glueFamily {T : C} {S : Sieve T}
    (x : Presieve.FamilyOfElements (twistedPresheaf g) S.arrows) (i : I) {W : C}
    (h : W ⟶ T) (a : W ⟶ U i) : Presieve.FamilyOfElements A (S.pullback h).arrows :=
  fun _ k hk => (x (k ≫ h) hk).val i (𝟙 _) (k ≫ a)

theorem family_val_congr {T : C} {S : Sieve T}
    (x : Presieve.FamilyOfElements (twistedPresheaf g) S.arrows) (i : I) {W W' : C}
    {f f' : W ⟶ T} (hf : S.arrows f) (hf' : S.arrows f') (e : f = f') (h : W' ⟶ W)
    (a : W' ⟶ U i) : (x f hf).val i h a = (x f' hf').val i h a := by subst e; rfl

theorem glueFamily_compatible {T : C} {S : Sieve T}
    {x : Presieve.FamilyOfElements (twistedPresheaf g) S.arrows} (hx : x.Compatible) (i : I)
    {W : C} (h : W ⟶ T) (a : W ⟶ U i) : (glueFamily x i h a).Compatible := by
  rw [Presieve.compatible_iff_sieveCompatible]
  intro W' W'' k φ hk
  have hxs := hx.to_sieveCompatible
  simp only [glueFamily]
  have e1 := hxs (k ≫ h) φ hk
  rw [(x (k ≫ h) hk).val_precomp]
  calc (x ((φ ≫ k) ≫ h) _).val i (𝟙 W'') ((φ ≫ k) ≫ a)
      = (x (φ ≫ k ≫ h) (S.downward_closed hk φ)).val i (𝟙 W'') (φ ≫ k ≫ a) :=
        (family_val_congr x i _ _ (Category.assoc _ _ _) _ _).trans
          ((x (φ ≫ k ≫ h) _).val_congr i rfl (Category.assoc _ _ _))
    _ = ((twistedPresheaf g).map φ.op (x (k ≫ h) hk)).val i (𝟙 W'') (φ ≫ k ≫ a) := by
        rw [e1]
    _ = (x (k ≫ h) hk).val i (φ ≫ 𝟙 W') (φ ≫ k ≫ a) := by
        rw [twistedPresheaf_map_val]; exact (x (k ≫ h) hk).val_congr i (by simp) rfl

/-- **Gluing**: the twisted section obtained from a compatible family on a
covering sieve, value by value, by gluing in the sheaf `A`. -/
noncomputable def glueSection (hA : IsPresheafOfGroups A) (hAs : Presieve.IsSheaf J A)
    {T : C} {S : Sieve T} (hS : S ∈ J T)
    {x : Presieve.FamilyOfElements (twistedPresheaf g) S.arrows} (hx : x.Compatible) :
    TwistedSection g T where
  val i _ h a := (hAs _ (J.pullback_stable h hS)).amalgamate _ (glueFamily_compatible hx i h a)
  val_precomp i _ _ φ h a := by
    apply (hAs _ (J.pullback_stable (φ ≫ h) hS)).isSeparatedFor.ext
    intro W'' k hk
    have hk' : (S.pullback h).arrows (k ≫ φ) := by
      change S.arrows ((k ≫ φ) ≫ h); rw [Category.assoc]; exact hk
    rw [← FunctorToTypes.map_comp_apply, ← op_comp, Presieve.IsSheafFor.valid_glue _ _ _ hk',
      Presieve.IsSheafFor.valid_glue _ _ _ hk]
    simp only [glueFamily]
    exact (family_val_congr x i _ _ (Category.assoc _ _ _) _ _).trans
      ((x _ _).val_congr i rfl (Category.assoc _ _ _))
  val_twist i j _ h a b := by
    apply (hAs _ (J.pullback_stable h hS)).isSeparatedFor.ext
    intro W' k hk
    rw [hA.map_mul, Presieve.IsSheafFor.valid_glue _ _ _ hk,
      Presieve.IsSheafFor.valid_glue _ _ _ hk, g.ev_precomp]
    simp only [glueFamily]
    exact (x (k ≫ h) hk).val_twist i j (𝟙 _) (k ≫ a) (k ≫ b)

/-- **The presheaf of twisted sections is a sheaf** when `A` is. -/
theorem isSheaf_twistedPresheaf (hA : IsPresheafOfGroups A) (hAs : Presheaf.IsSheaf J A) :
    Presheaf.IsSheaf J (twistedPresheaf g) := by
  rw [isSheaf_iff_isSheaf_of_type]
  have hAs' := (isSheaf_iff_isSheaf_of_type J A).mp hAs
  intro T S hS
  rw [← Presieve.isSeparatedFor_and_exists_isAmalgamation_iff_isSheafFor]
  refine ⟨?_, ?_⟩
  · intro x t₁ t₂ h₁ h₂
    refine TwistedSection.ext ?_; funext i W h a
    apply (hAs' _ (J.pullback_stable h hS)).isSeparatedFor.ext
    intro W' k hk
    rw [t₁.val_precomp, t₂.val_precomp]
    have e1 := congrArg (fun z : TwistedSection g W' => z.val i (𝟙 W') (k ≫ a)) (h₁ (k ≫ h) hk)
    have e2 := congrArg (fun z : TwistedSection g W' => z.val i (𝟙 W') (k ≫ a)) (h₂ (k ≫ h) hk)
    simp only [twistedPresheaf_map_val, Quiver.Hom.unop_op, Category.id_comp] at e1 e2
    rw [e1, e2]
  · intro x hx
    refine ⟨glueSection hA hAs' hS hx, ?_⟩
    intro V f hf
    refine TwistedSection.ext ?_; funext i W h a
    have hW : (S.pullback (h ≫ f)).arrows (𝟙 W) := by
      change S.arrows (𝟙 W ≫ h ≫ f); rw [Category.id_comp]; exact S.downward_closed hf h
    have e := (hAs' _ (J.pullback_stable (h ≫ f) hS)).valid_glue
      (glueFamily_compatible hx i (h ≫ f) a) (𝟙 W) hW
    rw [op_id, FunctorToTypes.map_id_apply] at e
    have e2 := congrArg (fun z : TwistedSection g W => z.val i (𝟙 W) a)
      (hx.to_sieveCompatible f h hf)
    simp only [twistedPresheaf_map_val, Quiver.Hom.unop_op, Category.id_comp] at e2
    change (glueSection hA hAs' hS hx).val i (h ≫ f) a = (x f hf).val i h a
    refine e.trans ?_
    simp only [glueFamily]
    rw [← e2]
    exact (family_val_congr x i _ _ (Category.id_comp _) _ _).trans
      ((x _ _).val_congr i rfl (Category.id_comp _))

/-! ### The glued torsor -/

/-- **Effective descent**: the multiplicative `A`-torsor glued from a 1-cocycle. -/
noncomputable def cocycleTorsor (hA : IsPresheafOfGroups A) (hAs : Presheaf.IsSheaf J A)
    (hU : ∀ T : C, Sieve.ofObjects U T ∈ J T) (g : TorsCocycle U A) : MulSheafTorsor J A where
  carrier := twistedPresheaf g
  torsor :=
    { action := twistedAction g hA
      isSheaf := isSheaf_twistedPresheaf hA hAs
      isPseudoTorsor := isPseudoTorsor_twistedAction hA hAs hU
      locallyNonempty := locallyNonempty_twistedPresheaf hU }
  isMulAction := isMulAction_twistedAction hA

/-- The canonical section `sᵢ` of the glued torsor over `U i`. -/
def cocycleSection (g : TorsCocycle U A) (i : I) : (twistedPresheaf g).obj (op (U i)) :=
  localSection i (𝟙 (U i))

/-- **The glued torsor has cocycle `g`.** On any `V` with maps `a : V ⟶ U i`
and `b : V ⟶ U j`, the restricted canonical sections satisfy
`sᵢ|_V = gᵢⱼ(a, b) · sⱼ|_V` for the action `c · x = x c⁻¹`. -/
theorem cocycleSection_transition (hA : IsPresheafOfGroups A) (i j : I) {V : C}
    (a : V ⟶ U i) (b : V ⟶ U j) :
    (twistedPresheaf g).map a.op (cocycleSection g i) =
      (twistedAction g hA).smul (op V) (g.ev i j a b)
        ((twistedPresheaf g).map b.op (cocycleSection g j)) := by
  refine TwistedSection.ext ?_; funext k W h c
  rw [twistedAction_val]
  simp only [twistedPresheaf_map_val, Quiver.Hom.unop_op, cocycleSection, localSection_val,
    Category.comp_id]
  rw [g.ev_precomp, ← g.ev_trans k j i c (h ≫ b) (h ≫ a)]
  have hinv : g.ev j i (h ≫ b) (h ≫ a) = (g.ev i j (h ≫ a) (h ≫ b))⁻¹ := by
    rw [eq_inv_iff_mul_eq_one, g.ev_trans, g.ev_self]
  rw [hinv]

end Sheaf

end QOU.MathlibExt.StackGerbe
