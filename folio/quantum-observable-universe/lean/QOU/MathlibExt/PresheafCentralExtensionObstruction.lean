import Mathlib.CategoryTheory.Sites.NonabelianCohomology.H1
import Mathlib.Tactic.Group

/-!
# Lifting obstruction for a central extension of presheaves of groups

Tier T2b of the Yekutieli central-extension-of-gerbes programme (bean `qou-533l`,
task `qou-8km0`). It generalises T2a (`QOU.MathlibExt.CechCentralExtensionObstruction`,
constant coefficients) to coefficients that vary over the cover.

## Setting

We use the cochain formalism of Mathlib's
`CategoryTheory.Sites.NonabelianCohomology.H1`: for a presheaf of groups
`F : Cᵒᵖ ⥤ GrpCat` and a family `U : I → C`, a 1-cochain assigns to `i j` and
any `a : T ⟶ U i`, `b : T ⟶ U j` a section over `T`, compatibly with
precomposition. We add the analogous **2-cochains** (`TwoCochain`).

A `PresheafCentralExtension 𝒜 𝓔 𝒢` is a pair of natural transformations
`ι : 𝒜 ⟶ 𝓔`, `π : 𝓔 ⟶ 𝒢` such that, on every object `T`, `ι_T` is injective,
its range is the kernel of `π_T`, and it lands in the centre of `𝓔(T)`. The
groups `𝒜(T)` are commutative. Surjectivity of `π_T` is **not** assumed: a
sheaf epimorphism is only locally surjective.

Let `γ` be a 1-cocycle of `𝒢` (a `𝒢`-torsor) and suppose it **lifts on
overlaps** to a 1-cochain `ξ` of `𝓔`, i.e. `π ∘ ξ = γ`. This hypothesis is the
counterpart of "the obstruction class is defined" in Yekutieli 2010, Thm 4.17
(held at `library/arxiv-0801.0083v4/`). The corpus statement of
`prop:yekutieli-lifting` omits it.

## Results, all sorry-free

* `obstruction` is a `TwoCochain 𝒜 U`: the defect `ξ_ij ξ_jk ξ_ik⁻¹`, taken in
  `𝒜`, and natural in `T`.
* `obstruction_cocycle`: it satisfies the Čech 2-cocycle identity.
* `obstruction_lift_change`: a different local lift `ξ'` changes it by a
  coboundary, so its class does not depend on `ξ`.
* `obstruction_pull`: pulling back along a refinement of the cover pulls the
  obstruction back (`pullOneCochain`, `pullOneCocycle`, `pullTwoCochain`).
* `isCoboundary_obstruction_iff`, `isCoboundary_pull`: whether the obstruction
  class vanishes does not depend on the local lift, and vanishing survives
  refinement.
* `exists_lift_iff`: `γ` lifts to a 1-**cocycle** of `𝓔` iff the obstruction is
  the coboundary `α_ij α_jk α_ik⁻¹` of some 1-cochain `α` of `𝒜`.

The lifting criterion is **derived**, not carried as a structure field as in
`QOU.YekutieliLifting`. This is the obstruction-to-lifting-torsors statement:
one degree above the TODO recorded in Mathlib's `H1` file (lifting a global
section, with obstruction in `H¹`). Gerbes proper (T3) and the general theorem
(T4) remain.
-/

-- Ref: [manuscript] lifting-and-descent, prop:yekutieli-lifting (presheaf coefficients)

universe w' w v u

namespace QOU.CentralExtension

/-! ### Algebraic core over plain groups -/

section Core

variable {A E : Type*} [Group A] [Group E] (ι : A →* E)
  (hinj : Function.Injective ι) (hcen : ∀ (a : A) (e : E), ι a * e = e * ι a)
include hinj hcen

theorem core_cocycle (xij xjk xkl xik xjl xil : E) (c₁ c₂ c₃ c₄ : A)
    (h₁ : xij * xjk = ι c₁ * xik) (h₂ : xik * xkl = ι c₂ * xil)
    (h₃ : xjk * xkl = ι c₃ * xjl) (h₄ : xij * xjl = ι c₄ * xil) :
    c₁ * c₂ = c₃ * c₄ := by
  have l : xij * xjk * xkl = ι (c₁ * c₂) * xil := by
    rw [h₁, mul_assoc, h₂, map_mul, mul_assoc]
  have r : xij * xjk * xkl = ι (c₃ * c₄) * xil := by
    rw [mul_assoc, h₃, ← mul_assoc, ← hcen, mul_assoc, h₄, map_mul, mul_assoc]
  exact hinj (mul_right_cancel (l.symm.trans r))

theorem core_lift_forward (xij xjk xik hij hjk hik : E) (aij ajk aik c : A)
    (hxij : xij = ι aij * hij) (hxjk : xjk = ι ajk * hjk) (hxik : xik = ι aik * hik)
    (hc : hij * hjk = hik) (hs : xij * xjk = ι c * xik) :
    c = aij * ajk * aik⁻¹ := by
  have key : ι (c * aik) * hik = ι (aij * ajk) * hik := by
    calc ι (c * aik) * hik = ι c * xik := by rw [hxik, map_mul, mul_assoc]
      _ = xij * xjk := hs.symm
      _ = ι aij * (hij * ι ajk) * hjk := by rw [hxij, hxjk]; group
      _ = ι (aij * ajk) * (hij * hjk) := by rw [← hcen ajk hij, map_mul]; group
      _ = ι (aij * ajk) * hik := by rw [hc]
  exact eq_mul_inv_of_mul_eq (hinj (mul_right_cancel key))

omit hinj in
theorem core_lift_back (hcomm : ∀ x y : A, x * y = y * x) (xij xjk xik : E) (aij ajk aik c : A)
    (hs : xij * xjk = ι c * xik) (ha : c = aij * ajk * aik⁻¹) :
    (ι aij⁻¹ * xij) * (ι ajk⁻¹ * xjk) = ι aik⁻¹ * xik := by
  have hA : aij⁻¹ * ajk⁻¹ * c = aik⁻¹ := by
    rw [ha, hcomm aij⁻¹ ajk⁻¹]; group
  calc (ι aij⁻¹ * xij) * (ι ajk⁻¹ * xjk)
      = ι aij⁻¹ * ι ajk⁻¹ * (xij * xjk) := by
        rw [mul_assoc, ← mul_assoc xij, ← hcen ajk⁻¹ xij]; group
    _ = ι (aij⁻¹ * ajk⁻¹ * c) * xik := by rw [hs, map_mul, map_mul]; group
    _ = ι aik⁻¹ * xik := by rw [hA]

omit hinj in
theorem core_lift_change'
    (xij xjk xik : E) (tij tjk tik c c' : A)
    (hs : xij * xjk = ι c * xik)
    (hs' : (ι tij * xij) * (ι tjk * xjk) = ι c' * (ι tik * xik)) :
    ι (c' * tik) * xik = ι (tij * tjk * c) * xik := by
  calc ι (c' * tik) * xik = ι c' * (ι tik * xik) := by rw [map_mul, mul_assoc]
    _ = (ι tij * xij) * (ι tjk * xjk) := hs'.symm
    _ = ι tij * ι tjk * (xij * xjk) := by
        rw [mul_assoc (ι tij), ← mul_assoc xij, ← hcen tjk xij]; group
    _ = ι (tij * tjk * c) * xik := by rw [hs, map_mul, map_mul]; group

end Core

/-! ### Presheaves of groups -/

open CategoryTheory Opposite

variable {C : Type u} [Category.{v} C] {I : Type w'} (U : I → C)

/-- A 2-cochain of a presheaf of groups on the family `U`, in the style of
`PresheafOfGroups.OneCochain`. -/
@[ext]
structure TwoCochain (F : Cᵒᵖ ⥤ GrpCat.{w}) where
  /-- the data of a 2-cochain -/
  ev (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) : F.obj (op T)
  ev_precomp (i j k : I) ⦃T T' : C⦄ (φ : T ⟶ T') (a : T' ⟶ U i) (b : T' ⟶ U j)
      (c : T' ⟶ U k) :
    F.map φ.op (ev i j k a b c) = ev i j k (φ ≫ a) (φ ≫ b) (φ ≫ c)


/-! ### Refinement of covers -/

section Refinement

variable {J : Type w'} {V : J → C} (r : J → I) (f : ∀ j, V j ⟶ U (r j))

/-- Pull a 1-cochain back along a refinement `f : V j ⟶ U (r j)`. -/
def pullOneCochain {F : Cᵒᵖ ⥤ GrpCat.{w}} (ξ : PresheafOfGroups.OneCochain F U) :
    PresheafOfGroups.OneCochain F V where
  ev j j' _ a b := ξ.ev (r j) (r j') (a ≫ f j) (b ≫ f j')
  ev_precomp j j' T T' φ a b := by simp [Category.assoc]

/-- Pull a 1-cocycle back along a refinement. -/
def pullOneCocycle {F : Cᵒᵖ ⥤ GrpCat.{w}} (γ : PresheafOfGroups.OneCocycle F U) :
    PresheafOfGroups.OneCocycle F V where
  toOneCochain := pullOneCochain U r f γ.toOneCochain
  ev_trans _ _ _ _ _ _ _ := γ.ev_trans _ _ _ _ _ _

/-- Pull a 2-cochain back along a refinement. -/
def pullTwoCochain {F : Cᵒᵖ ⥤ GrpCat.{w}} (c : TwoCochain U F) : TwoCochain V F where
  ev j j' j'' _ a b d := c.ev (r j) (r j') (r j'') (a ≫ f j) (b ≫ f j') (d ≫ f j'')
  ev_precomp j j' j'' T T' φ a b d := by rw [c.ev_precomp]; simp [Category.assoc]

end Refinement

/-- A central extension `1 → 𝒜 → 𝓔 → 𝒢` of presheaves of groups, exact and
central on every section group, with `𝒜` commutative. -/
structure PresheafCentralExtension (𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}) where
  ι : 𝒜 ⟶ 𝓔
  π : 𝓔 ⟶ 𝒢
  injective (T : Cᵒᵖ) : Function.Injective (ι.app T)
  exact (T : Cᵒᵖ) (e : 𝓔.obj T) : π.app T e = 1 ↔ ∃ a, ι.app T a = e
  central (T : Cᵒᵖ) (a : 𝒜.obj T) (e : 𝓔.obj T) : ι.app T a * e = e * ι.app T a
  comm (T : Cᵒᵖ) (x y : 𝒜.obj T) : x * y = y * x

namespace PresheafCentralExtension

variable {U}
variable {𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}} (X : PresheafCentralExtension 𝒜 𝓔 𝒢)

variable (γ : PresheafOfGroups.OneCocycle 𝒢 U) (ξ : PresheafOfGroups.OneCochain 𝓔 U)
  (hξ : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
    X.π.app (op T) (ξ.ev i j a b) = γ.ev i j a b)

include hξ in
theorem defect_mem (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    ∃ x, X.ι.app (op T) x = ξ.ev i j a b * ξ.ev j k b c * (ξ.ev i k a c)⁻¹ := by
  apply (X.exact (op T) _).1
  simp only [map_mul, map_inv, hξ, γ.ev_trans, mul_inv_cancel]

/-- The obstruction 2-cochain of `γ` relative to the local lift `ξ`. -/
noncomputable def obstruction : TwoCochain U 𝒜 where
  ev i j k _ a b c := (X.defect_mem γ ξ hξ i j k a b c).choose
  ev_precomp i j k T T' φ a b c := by
    apply X.injective
    rw [NatTrans.naturality_apply, (X.defect_mem γ ξ hξ i j k a b c).choose_spec,
      (X.defect_mem γ ξ hξ i j k (φ ≫ a) (φ ≫ b) (φ ≫ c)).choose_spec]
    simp only [map_mul, map_inv, PresheafOfGroups.OneCochain.ev_precomp]

theorem obstruction_spec (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    ξ.ev i j a b * ξ.ev j k b c =
      X.ι.app (op T) ((X.obstruction γ ξ hξ).ev i j k a b c) * ξ.ev i k a c := by
  have h := (X.defect_mem γ ξ hξ i j k a b c).choose_spec
  change ξ.ev i j a b * ξ.ev j k b c =
    X.ι.app (op T) (X.defect_mem γ ξ hξ i j k a b c).choose * ξ.ev i k a c
  rw [h]; group

/-- **The obstruction is a 2-cocycle.** -/
theorem obstruction_cocycle (i j k l : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j)
    (c : T ⟶ U k) (d : T ⟶ U l) :
    (X.obstruction γ ξ hξ).ev i j k a b c * (X.obstruction γ ξ hξ).ev i k l a c d =
      (X.obstruction γ ξ hξ).ev j k l b c d * (X.obstruction γ ξ hξ).ev i j l a b d := by
  exact core_cocycle (X.ι.app (op T)).hom (X.injective _) (X.central _) _ _ _ _ _ _ _ _ _ _
    (X.obstruction_spec γ ξ hξ i j k a b c) (X.obstruction_spec γ ξ hξ i k l a c d)
    (X.obstruction_spec γ ξ hξ j k l b c d) (X.obstruction_spec γ ξ hξ i j l a b d)

/-- **Independence of the local lift.** Two local lifts `ξ`, `ξ'` of `γ` give
obstructions that differ by the coboundary of a 1-cochain of `𝒜`, so the class
of the obstruction does not depend on the choice. -/
theorem obstruction_lift_change (ξ' : PresheafOfGroups.OneCochain 𝓔 U)
    (hξ' : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      X.π.app (op T) (ξ'.ev i j a b) = γ.ev i j a b) :
    ∃ t : PresheafOfGroups.OneCochain 𝒜 U, ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i)
      (b : T ⟶ U j) (c : T ⟶ U k),
      (X.obstruction γ ξ' hξ').ev i j k a b c =
        (X.obstruction γ ξ hξ).ev i j k a b c *
          (t.ev i j a b * t.ev j k b c * (t.ev i k a c)⁻¹) := by
  have hmem : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      ∃ x, X.ι.app (op T) x = ξ'.ev i j a b * (ξ.ev i j a b)⁻¹ := by
    intro i j T a b
    apply (X.exact (op T) _).1; simp only [map_mul, map_inv, hξ, hξ', mul_inv_cancel]
  let t : PresheafOfGroups.OneCochain 𝒜 U :=
    { ev := fun i j _ a b => (hmem i j a b).choose
      ev_precomp := by
        intro i j T T' φ a b
        apply X.injective
        rw [NatTrans.naturality_apply, (hmem i j a b).choose_spec,
          (hmem i j (φ ≫ a) (φ ≫ b)).choose_spec]
        simp only [map_mul, map_inv, PresheafOfGroups.OneCochain.ev_precomp] }
  have ht : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      ξ'.ev i j a b = X.ι.app (op T) (t.ev i j a b) * ξ.ev i j a b := by
    intro i j T a b
    change _ = X.ι.app (op T) (hmem i j a b).choose * _
    rw [(hmem i j a b).choose_spec]; group
  refine ⟨t, fun i j k T a b c => ?_⟩
  have hs' := X.obstruction_spec γ ξ' hξ' i j k a b c
  rw [ht i j a b, ht j k b c, ht i k a c] at hs'
  have key := core_lift_change' (X.ι.app (op T)).hom (X.central _) _ _ _ _ _ _ _ _
    (X.obstruction_spec γ ξ hξ i j k a b c) hs'
  have e := X.injective _ (mul_right_cancel key)
  rw [eq_mul_inv_of_mul_eq e, X.comm _ (t.ev i j a b * t.ev j k b c)]
  group

/-- **Compatibility with refinement.** Pulling `γ` and its local lift `ξ` back
along a refinement of the cover pulls the obstruction back. -/
theorem obstruction_pull {J : Type w'} {V : J → C} (r : J → I) (f : ∀ j, V j ⟶ U (r j)) :
    X.obstruction (pullOneCocycle U r f γ) (pullOneCochain U r f ξ)
        (fun j j' _ a b => hξ (r j) (r j') (a ≫ f j) (b ≫ f j')) =
      pullTwoCochain U r f (X.obstruction γ ξ hξ) := by
  ext j j' j'' T a b d
  apply X.injective
  exact ((X.defect_mem (pullOneCocycle U r f γ) (pullOneCochain U r f ξ)
      (fun j j' _ a b => hξ (r j) (r j') (a ≫ f j) (b ≫ f j')) j j' j'' a b d).choose_spec).trans
    ((X.defect_mem γ ξ hξ (r j) (r j') (r j'') (a ≫ f j) (b ≫ f j') (d ≫ f j'')).choose_spec).symm

/-- **Lifting criterion.** The `𝒢`-cocycle `γ` lifts to an `𝓔`-cocycle iff its
obstruction (relative to the local lift `ξ`) is a coboundary. -/
theorem exists_lift_iff :
    (∃ η : PresheafOfGroups.OneCocycle 𝓔 U, ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i)
        (b : T ⟶ U j), X.π.app (op T) (η.ev i j a b) = γ.ev i j a b) ↔
      ∃ α : PresheafOfGroups.OneCochain 𝒜 U, ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i)
        (b : T ⟶ U j) (c : T ⟶ U k),
        (X.obstruction γ ξ hξ).ev i j k a b c =
          α.ev i j a b * α.ev j k b c * (α.ev i k a c)⁻¹ := by
  constructor
  · rintro ⟨η, hη⟩
    have hmem : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
        ∃ x, X.ι.app (op T) x = ξ.ev i j a b * (η.ev i j a b)⁻¹ := by
      intro i j T a b
      apply (X.exact (op T) _).1; simp only [map_mul, map_inv, hξ, hη, mul_inv_cancel]
    let α : PresheafOfGroups.OneCochain 𝒜 U :=
      { ev := fun i j _ a b => (hmem i j a b).choose
        ev_precomp := by
          intro i j T T' φ a b
          apply X.injective
          rw [NatTrans.naturality_apply, (hmem i j a b).choose_spec,
            (hmem i j (φ ≫ a) (φ ≫ b)).choose_spec]
          simp only [map_mul, map_inv, PresheafOfGroups.OneCochain.ev_precomp] }
    have hx : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
        ξ.ev i j a b = X.ι.app (op T) (α.ev i j a b) * η.ev i j a b := by
      intro i j T a b
      change _ = X.ι.app (op T) (hmem i j a b).choose * _
      rw [(hmem i j a b).choose_spec]; group
    refine ⟨α, fun i j k T a b c => ?_⟩
    exact core_lift_forward (X.ι.app (op T)).hom (X.injective _) (X.central _) _ _ _ _ _ _ _ _ _ _
      (hx i j a b) (hx j k b c) (hx i k a c) (η.ev_trans i j k a b c)
      (X.obstruction_spec γ ξ hξ i j k a b c)
  · rintro ⟨α, hα⟩
    refine ⟨{ ev := fun i j _ a b => X.ι.app _ (α.ev i j a b)⁻¹ * ξ.ev i j a b
              ev_precomp := by
                intro i j T T' φ a b
                rw [map_mul, ← NatTrans.naturality_apply, map_inv,
                  PresheafOfGroups.OneCochain.ev_precomp,
                  PresheafOfGroups.OneCochain.ev_precomp]
              ev_trans := by
                intro i j k T a b c
                exact core_lift_back (X.ι.app (op T)).hom (X.central _)
                  (X.comm _) _ _ _ _ _ _ _ (X.obstruction_spec γ ξ hξ i j k a b c)
                  (hα i j k a b c) }, ?_⟩
    intro i j T a b
    have h1 : X.π.app (op T) (X.ι.app (op T) (α.ev i j a b)⁻¹) = 1 :=
      (X.exact _ _).2 ⟨_, rfl⟩
    change X.π.app (op T) (X.ι.app (op T) (α.ev i j a b)⁻¹ * ξ.ev i j a b) = _
    rw [map_mul, h1, one_mul, hξ]

/-- A 2-cochain of `𝒜` is a **coboundary** if it is `α_ij α_jk α_ik⁻¹` for a
1-cochain `α` of `𝒜`. -/
def IsCoboundary (c : TwoCochain U 𝒜) : Prop :=
  ∃ α : PresheafOfGroups.OneCochain 𝒜 U, ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i)
    (b : T ⟶ U j) (d : T ⟶ U k), c.ev i j k a b d = α.ev i j a b * α.ev j k b d * (α.ev i k a d)⁻¹

/-- **The vanishing of the obstruction class does not depend on the local
lift.** Both sides are equivalent to the existence of a lift of `γ`. -/
theorem isCoboundary_obstruction_iff (ξ' : PresheafOfGroups.OneCochain 𝓔 U)
    (hξ' : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      X.π.app (op T) (ξ'.ev i j a b) = γ.ev i j a b) :
    IsCoboundary (X.obstruction γ ξ hξ) ↔ IsCoboundary (X.obstruction γ ξ' hξ') :=
  (X.exists_lift_iff γ ξ hξ).symm.trans (X.exists_lift_iff γ ξ' hξ')

/-- **Vanishing is preserved by refinement.** If the obstruction is a coboundary
on the cover `U`, its pullback to a refinement `V` is a coboundary there. -/
theorem isCoboundary_pull {J : Type w'} {V : J → C} (r : J → I) (f : ∀ j, V j ⟶ U (r j))
    {c : TwoCochain U 𝒜} (hc : IsCoboundary c) :
    IsCoboundary (pullTwoCochain U r f c) := by
  obtain ⟨α, hα⟩ := hc
  exact ⟨pullOneCochain U r f α, fun j j' j'' T a b d => hα _ _ _ _ _ _⟩

end PresheafCentralExtension

end QOU.CentralExtension
