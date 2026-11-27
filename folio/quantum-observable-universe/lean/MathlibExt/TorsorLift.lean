import MathlibExt.TorsorDescent

/-!
# Lifting a torsor along a morphism of presheaves of groups

Bean `qou-0xk8` (parent `qou-533l`). Let `π : E ⟶ G` be a morphism of
presheaves of groups on a small site `(C, J)`, and let `P` be a multiplicative
`G`-torsor with a section `sᵢ` over each member of a family `U` that covers the
final object. Yekutieli's Theorem 4.17 asks when `P` comes from an `E`-torsor.
This file proves the torsor-to-cocycle half of that criterion:

* `TorsCocycle.map π e`: the image of an `E`-cocycle under `π`.
* `LiftAlong π P`: an `E`-torsor `Q` with a `π`-equivariant morphism `Q ⟶ P`
  (a reduction of `P` along `π`).
* `twistedMapOf`: the `π`-equivariant morphism between the glued torsors of
  `e` and of any `G`-cocycle that `π e` equals pointwise.
* `transition_map_of_liftAlong`: the sections of `P` coming from sections of a
  reduction `Q` have the transition cocycle `π (transition Q t)`.
* `liftAlongOfCocycle`: conversely, an `E`-cocycle lifting the transition
  cocycle of `P` yields a reduction (the glued torsor of the cocycle, composed
  with the descent isomorphism of `MathlibExt.TorsorDescent`).
* `exists_liftAlong_iff`: **`P` has a reduction along `π` carrying sections to
  `s` iff the transition cocycle of `s` lifts to an `E`-cocycle.**

Combined with `QOU.CentralExtension.PresheafCentralExtension.exists_lift_iff`
(the cocycle lifts iff its obstruction is a coboundary), this is the torsor
form of the lifting criterion, for torsors trivialised on a cover. The gerbe
form (Definition 3.21 and the stack-level Theorem 4.17) is not done here. All
results are sorry-free and generic over a small site; nothing archimedean is
used.

## Source

Yekutieli, *Central Extensions of Gerbes* (arXiv 0801.0083, held at
`library/arxiv-0801.0083v4/`), §4, Thm 4.17 (torsor case); Giraud,
*Cohomologie non abélienne*, III.3.
-/

-- Ref: [yekutieli2010] Thm 4.17 (torsor case)

universe w

namespace QOU.MathlibExt.StackGerbe

open CategoryTheory Opposite

variable {C : Type w} [Category.{w} C] {I : Type w} {U : I → C}
variable {E G : Cᵒᵖ ⥤ Type w} [∀ T : Cᵒᵖ, Group (E.obj T)] [∀ T : Cᵒᵖ, Group (G.obj T)]
variable (π : E ⟶ G) (hπ : ∀ (T : Cᵒᵖ) (x y : E.obj T), π.app T (x * y) = π.app T x * π.app T y)

/-- `π` on sections over `T`, as a group homomorphism. -/
def appHom (T : Cᵒᵖ) : E.obj T →* G.obj T := MonoidHom.mk' (π.app T) (hπ T)

include hπ in
theorem app_inv (T : Cᵒᵖ) (x : E.obj T) : π.app T x⁻¹ = (π.app T x)⁻¹ :=
  (appHom π hπ T).map_inv x

/-- **The image of a cocycle** under `π`: `(π e)ᵢⱼ = π (eᵢⱼ)`. -/
def TorsCocycle.map (e : TorsCocycle U E) : TorsCocycle U G where
  ev i j _ a b := π.app _ (e.ev i j a b)
  ev_precomp i j _ _ φ a b := by rw [← FunctorToTypes.naturality, e.ev_precomp]
  ev_trans i j k _ a b c := by rw [← hπ, e.ev_trans]

theorem TorsCocycle.map_ev (e : TorsCocycle U E) (i j : I) {V : C} (a : V ⟶ U i)
    (b : V ⟶ U j) : (e.map π hπ).ev i j a b = π.app _ (e.ev i j a b) := rfl

variable {J : GrothendieckTopology C}

/-- **A reduction of `P` along `π`**: an `E`-torsor `Q` with a morphism
`Q ⟶ P` satisfying `f (c · q) = π(c) · f(q)`. -/
structure LiftAlong (P : MulSheafTorsor J G) where
  /-- The `E`-torsor. -/
  torsor : MulSheafTorsor J E
  /-- The morphism to `P`. -/
  hom : torsor.carrier ⟶ P.carrier
  /-- Equivariance along `π`. -/
  hom_smul : ∀ (T : Cᵒᵖ) (c : E.obj T) (q : torsor.carrier.obj T),
    hom.app T (torsor.torsor.action.smul T c q) = P.torsor.action.smul T (π.app T c) (hom.app T q)

/-! ### From a reduction to a lift of the cocycle -/

/-- **Reduction ⇒ lifted cocycle.** If `f : Q ⟶ P` is a reduction along `π` and
`tᵢ` are sections of `Q`, the sections `f(tᵢ)` of `P` have transition cocycle
`π (transition Q t)`. -/
theorem transition_map_of_liftAlong {P : MulSheafTorsor J G} (L : LiftAlong π P)
    (t : ∀ i, L.torsor.carrier.obj (op (U i))) (i j : I) {V : C} (a : V ⟶ U i)
    (b : V ⟶ U j) :
    π.app _ ((transition L.torsor t).ev i j a b) =
      (transition P (fun k => L.hom.app _ (t k))).ev i j a b := by
  symm
  apply torsorQuot_eq
  rw [← FunctorToTypes.naturality, ← FunctorToTypes.naturality, ← L.hom_smul,
    transition_spec]

/-! ### From a lifted cocycle to a reduction -/

section Build

variable {e : TorsCocycle U E} {g : TorsCocycle U G}
  (he : ∀ (i j : I) ⦃V : C⦄ (a : V ⟶ U i) (b : V ⟶ U j), π.app _ (e.ev i j a b) = g.ev i j a b)

/-- Apply `π` to a twisted section of `e`, giving a twisted section of `g`. -/
def twistedSectionMap {T : C} (x : TwistedSection e T) : TwistedSection g T where
  val i _ h a := π.app _ (x.val i h a)
  val_precomp i _ _ φ h a := by rw [← FunctorToTypes.naturality, x.val_precomp]
  val_twist i j _ h a b := by rw [x.val_twist i j h a b, hπ, he]

/-- The morphism of glued torsors induced by `π`. -/
def twistedMapOf : twistedPresheaf e ⟶ twistedPresheaf g where
  app T x := twistedSectionMap π hπ he x
  naturality T T' f := by
    funext x
    refine TwistedSection.ext ?_; funext i V h a
    rfl

theorem twistedMapOf_val {T : Cᵒᵖ} (x : (twistedPresheaf e).obj T) (i : I) {V : C}
    (h : V ⟶ T.unop) (a : V ⟶ U i) :
    ((twistedMapOf π hπ he).app T x).val i h a = π.app _ (x.val i h a) := rfl

theorem twistedMapOf_smul (hE : IsPresheafOfGroups E) (hG : IsPresheafOfGroups G) (T : Cᵒᵖ)
    (c : E.obj T) (x : (twistedPresheaf e).obj T) :
    (twistedMapOf π hπ he).app T ((twistedAction e hE).smul T c x) =
      (twistedAction g hG).smul T (π.app T c) ((twistedMapOf π hπ he).app T x) := by
  refine TwistedSection.ext ?_; funext i V h a
  rw [twistedMapOf_val, twistedAction_val, twistedAction_val, twistedMapOf_val, hπ, app_inv π hπ,
    ← FunctorToTypes.naturality]

end Build

variable (P : MulSheafTorsor J G) (s : ∀ i, P.carrier.obj (op (U i)))
variable (hG : IsPresheafOfGroups G) (hU : ∀ T : C, Sieve.ofObjects U T ∈ J T)

theorem descentIso_hom_app (T : Cᵒᵖ) (p : P.carrier.obj T) :
    (descentIso P s hG hU).hom.app T p = descentMap P s hG p := rfl

/-- The inverse of the descent isomorphism is `G`-equivariant. -/
theorem descentIso_inv_smul (T : Cᵒᵖ) (c : G.obj T) (x : (twistedPresheaf (transition P s)).obj T) :
    (descentIso P s hG hU).inv.app T ((twistedAction (transition P s) hG).smul T c x) =
      P.torsor.action.smul T c ((descentIso P s hG hU).inv.app T x) := by
  apply descentMap_injective P s hG hU
  change (descentIso P s hG hU).hom.app T ((descentIso P s hG hU).inv.app T _) =
    descentMap P s hG (P.torsor.action.smul (op T.unop) c _)
  rw [descentMap_smul, FunctorToTypes.inv_hom_id_app_apply]
  exact (congrArg ((twistedAction (transition P s) hG).smul T c)
    (FunctorToTypes.inv_hom_id_app_apply (α := descentIso P s hG hU) (X := T) (x := x))).symm

theorem torsorQuot_inv {T : Cᵒᵖ} (y z : P.carrier.obj T) :
    (torsorQuot P y z)⁻¹ = torsorQuot P z y := by
  symm; apply torsorQuot_eq
  nth_rewrite 2 [← torsorQuot_spec P y z]
  rw [← P.isMulAction.mul_smul, inv_mul_cancel, P.isMulAction.one_smul]

variable (hE : IsPresheafOfGroups E) (hEs : Presheaf.IsSheaf J E)

/-- **Lifted cocycle ⇒ reduction.** If an `E`-cocycle `e` satisfies
`π e = transition P s`, the glued torsor of `e`, followed by the descent
isomorphism, is a reduction of `P` along `π`. -/
noncomputable def liftAlongOfCocycle (e : TorsCocycle U E)
    (he : ∀ (i j : I) ⦃V : C⦄ (a : V ⟶ U i) (b : V ⟶ U j),
      π.app _ (e.ev i j a b) = (transition P s).ev i j a b) : LiftAlong π P where
  torsor := cocycleTorsor hE hEs hU e
  hom := twistedMapOf π hπ he ≫ (descentIso P s hG hU).inv
  hom_smul T c q := by
    change (descentIso P s hG hU).inv.app T ((twistedMapOf π hπ he).app T
      ((twistedAction e hE).smul T c q)) = _
    rw [twistedMapOf_smul π hπ he hE hG, descentIso_inv_smul]
    rfl

/-- The reduction `liftAlongOfCocycle` sends the canonical sections of the
glued torsor to the given sections `sᵢ`. -/
theorem liftAlongOfCocycle_section (e : TorsCocycle U E)
    (he : ∀ (i j : I) ⦃V : C⦄ (a : V ⟶ U i) (b : V ⟶ U j),
      π.app _ (e.ev i j a b) = (transition P s).ev i j a b) (i : I) :
    (liftAlongOfCocycle π hπ P s hG hU hE hEs e he).hom.app _ (cocycleSection e i) = s i := by
  change (descentIso P s hG hU).inv.app _ ((twistedMapOf π hπ he).app _ (cocycleSection e i)) = s i
  have key : descentMap P s hG (s i) = (twistedMapOf π hπ he).app _ (cocycleSection e i) := by
    refine TwistedSection.ext ?_; funext k V h a
    rw [descentMap_val, twistedMapOf_val, torsorQuot_inv]
    simp only [cocycleSection, localSection_val, Category.comp_id, he]
    rfl
  rw [← key, ← descentIso_hom_app P s hG hU, FunctorToTypes.hom_inv_id_app_apply]

include hπ hG hU hE hEs in
/-- **Lifting criterion for a trivialised torsor.** `P` has a reduction along
`π` whose sections over the `U i` map to the given `sᵢ` iff the transition
cocycle of the `sᵢ` lifts to an `E`-cocycle. -/
theorem exists_liftAlong_iff :
    (∃ (L : LiftAlong π P) (t : ∀ i, L.torsor.carrier.obj (op (U i))),
        ∀ i, L.hom.app _ (t i) = s i) ↔
      ∃ e : TorsCocycle U E, ∀ (i j : I) ⦃V : C⦄ (a : V ⟶ U i) (b : V ⟶ U j),
        π.app _ (e.ev i j a b) = (transition P s).ev i j a b := by
  constructor
  · rintro ⟨L, t, ht⟩
    refine ⟨transition L.torsor t, fun i j V a b => ?_⟩
    rw [transition_map_of_liftAlong π L t, show (fun k => L.hom.app _ (t k)) = s from funext ht]
  · rintro ⟨e, he⟩
    exact ⟨liftAlongOfCocycle π hπ P s hG hU hE hEs e he, cocycleSection e,
      liftAlongOfCocycle_section π hπ P s hG hU hE hEs e he⟩

end QOU.MathlibExt.StackGerbe
