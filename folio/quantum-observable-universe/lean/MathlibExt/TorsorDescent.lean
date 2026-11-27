import MathlibExt.CocycleTorsor

/-!
# Effective descent of torsors, converse half: a locally trivial torsor is glued from its cocycle

Beans `qou-t1dx` and `qou-skn4` (parent `qou-533l`), design D3. The gluing half
is `MathlibExt.CocycleTorsor` (`cocycleTorsor g`). This file proves the
converse: every multiplicative `A`-torsor `P` with a section `sᵢ ∈ P(U i)` over
each member of a family `U` covering the final object is isomorphic to the
torsor glued from its own transition cocycle.

* `transition P s`: the cocycle `gᵢⱼ`, the unique element with
  `gᵢⱼ · sⱼ|_V = sᵢ|_V` (`transition_spec`), as a `TorsCocycle U A`
  (naturality from `map_smul`, the cocycle identity from `mul_smul`, both by
  uniqueness).
* `descentMap P s p`: for `p ∈ P(T)`, the twisted section `xᵢ(h, a) = dᵢ⁻¹`
  where `dᵢ · sᵢ|_a = p|_h`.
* `descentMap_natural` (it commutes with restriction) and `descentMap_smul`
  (it is `A`-equivariant).
* `descentMap_injective` and `descentMap_surjective`, hence `descentEquiv`
  and the natural isomorphism `descentIso P s : P ≅ twistedPresheaf (transition P s)`.

With `MathlibExt.CocycleTorsor` this gives both halves of effective descent
for torsors trivialised on a cover: cocycles glue to torsors, and a
trivialised torsor is the torsor of its cocycle. All sorry-free and generic
over a small site.

## Source

Yekutieli, *Central Extensions of Gerbes* (arXiv 0801.0083, held at
`library/arxiv-0801.0083v4/`), §1–2; Giraud, *Cohomologie non abélienne*,
III.2.4.
-/

-- Ref: [yekutieli2010] §1–2, effective descent for torsors (converse)

universe w

namespace QOU.MathlibExt.StackGerbe

open CategoryTheory Opposite

variable {C : Type w} [Category.{w} C] {I : Type w} {U : I → C}
variable {A : Cᵒᵖ ⥤ Type w} [∀ T : Cᵒᵖ, Group (A.obj T)]
variable {J : GrothendieckTopology C}
variable (P : MulSheafTorsor J A) (s : ∀ i, P.carrier.obj (op (U i)))

local notation "act" => P.torsor.action.smul

/-- The unique `c` with `c · y = z` in a pseudo-torsor. -/
noncomputable def torsorQuot {T : Cᵒᵖ} (y z : P.carrier.obj T) : A.obj T :=
  (P.torsor.isPseudoTorsor T y z).exists.choose

theorem torsorQuot_spec {T : Cᵒᵖ} (y z : P.carrier.obj T) : act T (torsorQuot P y z) y = z :=
  (P.torsor.isPseudoTorsor T y z).exists.choose_spec

theorem torsorQuot_eq {T : Cᵒᵖ} {y z : P.carrier.obj T} {c : A.obj T} (h : act T c y = z) :
    torsorQuot P y z = c :=
  ((P.torsor.isPseudoTorsor T y z).unique (torsorQuot_spec P y z) h)

theorem torsorQuot_map {T T' : Cᵒᵖ} (f : T ⟶ T') (y z : P.carrier.obj T) :
    A.map f (torsorQuot P y z) = torsorQuot P (P.carrier.map f y) (P.carrier.map f z) := by
  symm; apply torsorQuot_eq
  rw [← P.torsor.action.map_smul, torsorQuot_spec]

/-- **The transition cocycle** of the sections `sᵢ`: `gᵢⱼ · sⱼ|_V = sᵢ|_V`. -/
noncomputable def transition : TorsCocycle U A where
  ev i j _ a b := torsorQuot P (P.carrier.map b.op (s j)) (P.carrier.map a.op (s i))
  ev_precomp i j _ _ φ a b := by
    rw [torsorQuot_map]
    simp only [← FunctorToTypes.map_comp_apply, ← op_comp]
  ev_trans i j k _ a b c := by
    symm; apply torsorQuot_eq
    rw [P.isMulAction.mul_smul, torsorQuot_spec, torsorQuot_spec]

theorem transition_spec (i j : I) {V : C} (a : V ⟶ U i) (b : V ⟶ U j) :
    act (op V) ((transition P s).ev i j a b) (P.carrier.map b.op (s j)) =
      P.carrier.map a.op (s i) :=
  torsorQuot_spec P _ _

variable (hA : IsPresheafOfGroups A)

/-- **The descent map** `P(T) → twisted sections`: `xᵢ(h, a) = dᵢ⁻¹`, where
`dᵢ · sᵢ|_a = p|_h`. -/
noncomputable def descentMap {T : C} (p : P.carrier.obj (op T)) :
    TwistedSection (transition P s) T where
  val i _ h a := (torsorQuot P (P.carrier.map a.op (s i)) (P.carrier.map h.op p))⁻¹
  val_precomp i _ _ φ h a := by
    rw [hA.map_inv, torsorQuot_map]
    simp only [← FunctorToTypes.map_comp_apply, ← op_comp]
  val_twist i j _ h a b := by
    -- `dⱼ = dᵢ gᵢⱼ`, so `dᵢ⁻¹ = gᵢⱼ dⱼ⁻¹`.
    have hj : torsorQuot P (P.carrier.map b.op (s j)) (P.carrier.map h.op p) =
        torsorQuot P (P.carrier.map a.op (s i)) (P.carrier.map h.op p) *
          (transition P s).ev i j a b := by
      apply torsorQuot_eq
      rw [P.isMulAction.mul_smul, transition_spec, torsorQuot_spec]
    rw [hj, mul_inv_rev, mul_inv_cancel_left]

theorem descentMap_val {T : C} (p : P.carrier.obj (op T)) (i : I) {V : C} (h : V ⟶ T)
    (a : V ⟶ U i) :
    (descentMap P s hA p).val i h a =
      (torsorQuot P (P.carrier.map a.op (s i)) (P.carrier.map h.op p))⁻¹ := rfl

/-- The descent map commutes with restriction. -/
theorem descentMap_natural {T T' : C} (f : T' ⟶ T) (p : P.carrier.obj (op T)) :
    descentMap P s hA (P.carrier.map f.op p) =
      (twistedPresheaf (transition P s)).map f.op (descentMap P s hA p) := by
  refine TwistedSection.ext ?_; funext i V h a
  rw [twistedPresheaf_map_val, descentMap_val, descentMap_val, ← FunctorToTypes.map_comp_apply]
  rfl

/-- The descent map is `A`-equivariant. -/
theorem descentMap_smul {T : C} (c : A.obj (op T)) (p : P.carrier.obj (op T)) :
    descentMap P s hA (act (op T) c p) =
      (twistedAction (transition P s) hA).smul (op T) c (descentMap P s hA p) := by
  refine TwistedSection.ext ?_; funext i V h a
  rw [twistedAction_val, descentMap_val, descentMap_val, ← mul_inv_rev, inv_inj]
  apply torsorQuot_eq
  rw [P.isMulAction.mul_smul, torsorQuot_spec, P.torsor.action.map_smul]

variable (hU : ∀ T : C, Sieve.ofObjects U T ∈ J T)
include hU

theorem descentMap_injective {T : C} : Function.Injective (descentMap P s hA (T := T)) := by
  intro p q hpq
  have H := (isSheaf_iff_isSheaf_of_type J P.carrier).mp P.torsor.isSheaf _ (hU T)
  apply H.isSeparatedFor.ext
  rintro V h ⟨i, ⟨a⟩⟩
  have e := congrArg (fun z : TwistedSection (transition P s) T => z.val i h a) hpq
  simp only [descentMap_val, inv_inj] at e
  rw [← torsorQuot_spec P (P.carrier.map a.op (s i)) (P.carrier.map h.op p), e,
    torsorQuot_spec]

/-- The local family `h ↦ xᵢ(h, a)⁻¹ · sᵢ|_a` glued in the surjectivity proof. -/
noncomputable def descentFamily {T : C} (x : TwistedSection (transition P s) T) :
    Presieve.FamilyOfElements P.carrier (Sieve.ofObjects U T).arrows :=
  fun _ h hh => act _ (x.val hh.choose h hh.choose_spec.some)⁻¹
    (P.carrier.map hh.choose_spec.some.op (s hh.choose))

omit hU in
theorem descentFamily_indep {T : C} (x : TwistedSection (transition P s) T) {V : C}
    (h : V ⟶ T) (i j : I) (a : V ⟶ U i) (b : V ⟶ U j) :
    act (op V) (x.val i h a)⁻¹ (P.carrier.map a.op (s i)) =
      act (op V) (x.val j h b)⁻¹ (P.carrier.map b.op (s j)) := by
  rw [← transition_spec P s i j a b, ← P.isMulAction.mul_smul, x.val_twist i j h a b,
    mul_inv_rev, inv_mul_cancel_right]

omit hU in
theorem descentFamily_eq {T : C} (x : TwistedSection (transition P s) T) {V : C} (h : V ⟶ T)
    (hh : (Sieve.ofObjects U T).arrows h) (i : I) (a : V ⟶ U i) :
    descentFamily P s x h hh = act (op V) (x.val i h a)⁻¹ (P.carrier.map a.op (s i)) :=
  descentFamily_indep P s x h _ _ _ _

omit hU in
include hA in
theorem descentFamily_compatible {T : C} (x : TwistedSection (transition P s) T) :
    (descentFamily P s x).Compatible := by
  rw [Presieve.compatible_iff_sieveCompatible]
  intro V W h φ hh
  obtain ⟨i, ⟨a⟩⟩ := hh
  rw [descentFamily_eq P s x (φ ≫ h) _ i (φ ≫ a), descentFamily_eq P s x h ⟨i, ⟨a⟩⟩ i a,
    P.torsor.action.map_smul, hA.map_inv, x.val_precomp, ← FunctorToTypes.map_comp_apply]
  rfl

theorem descentMap_surjective {T : C} : Function.Surjective (descentMap P s hA (T := T)) := by
  intro x
  have H := (isSheaf_iff_isSheaf_of_type J P.carrier).mp P.torsor.isSheaf _ (hU T)
  have hc := descentFamily_compatible P s hA x
  refine ⟨H.amalgamate _ hc, ?_⟩
  refine TwistedSection.ext ?_; funext i V h a
  rw [descentMap_val, H.valid_glue hc h ⟨i, ⟨a⟩⟩, descentFamily_eq P s x h _ i a,
    torsorQuot_eq P rfl, inv_inv]

/-- The descent map as a bijection on sections. -/
noncomputable def descentEquiv (T : C) :
    P.carrier.obj (op T) ≃ TwistedSection (transition P s) T :=
  Equiv.ofBijective _ ⟨descentMap_injective P s hA hU, descentMap_surjective P s hA hU⟩

/-- **Effective descent, converse half.** A multiplicative `A`-torsor with a
section over each `U i` is isomorphic, as a presheaf, to the torsor glued from
its transition cocycle; the isomorphism is `A`-equivariant (`descentMap_smul`). -/
noncomputable def descentIso : P.carrier ≅ twistedPresheaf (transition P s) :=
  NatIso.ofComponents (fun T => (descentEquiv P s hA hU T.unop).toIso) (by
    intro T T' f
    funext p
    exact descentMap_natural P s hA f.unop p)

end QOU.MathlibExt.StackGerbe
