import QOU.MathlibExt.PresheafCentralExtensionObstruction

/-!
# Čech-cocycle gerbes and the cocycle-level Yekutieli Theorem 4.17

Tier T3, design D2, of the Yekutieli central-extension-of-gerbes programme (bean
`qou-0xk8`, parent `qou-533l`). Source: Yekutieli, *Central extensions of gerbes*
(`library/arxiv-0801.0083v4/`): the Construction labelled `const1` in §4, Def 4.15, Thm 4.17.

## What is modelled, and what is ASSUMED

A gerbe is **not** formalised here as a stack. We work with its **Čech cocycle
data** relative to a fixed family `U : I → C`, in the 1-cochain formalism of
Mathlib's `CategoryTheory.Sites.NonabelianCohomology.H1`.

* **Abelian banded gerbes.** A gerbe banded by a presheaf of commutative groups
  `𝒜` is represented by a `TwoCocycle U 𝒜`; two such gerbes are equivalent when
  the cocycles differ by a coboundary (`TwoCocycle.Rel`, an equivalence relation,
  `TwoCocycle.equivalence_rel`). `H2 U 𝒜` is the quotient.
* **Gerbes bound by the lien of `𝒢`.** For a central `ζ : 𝒵 ⟶ 𝒢` and a
  2-cocycle `β` of `𝒵`, the gerbe `H_β` is represented by its **global objects
  presented on the cover**: `TwistedCocycle ζ β`, the 1-cochains `g` of `𝒢` with
  `g_ij g_jk = ζ(β_ijk) g_ik`. Isomorphisms of objects are the Mathlib
  `OneCohomologyRelation` (a 0-cochain `h` with `h_i g_ij = g'_ij h_j`), and they
  preserve the twist (`TwistedCocycle.conj`). Cohomologous twists give
  corresponding objects (`TwistedCocycle.retwist`).
* **Central extension of gerbes** (Yekutieli Def 3.21, cocycle form,
  `CentralGerbeExtension`): a central extension `1 → 𝒜 → 𝓔 → 𝒢` of presheaves
  of groups (T2b), together with a lift `ζ̃ : 𝒵 ⟶ 𝓔` of the twist, central in
  `𝓔`. The functor `F : G_β → H_β` is `π_*` (`pushOneCochain`).

**The equivalence "gerbe ≃ its cocycle data on `U`" is ASSUMED, not proved.**
In particular nothing here proves that every gerbe bound by `lien(𝒢)` admits a
twisting cocycle on some cover, that the cocycle model is independent of the
cover up to refinement, or that the objects/isomorphisms of a stack are
recovered from twisted cochains. Gerbes whose band has a non-trivial outer
twisting (`λ_ij ∈ Aut 𝒢|U_ij` non-inner, Giraud's general non-abelian
2-cocycles) are **not covered**. This is the known cost of design D2.

## Results, all sorry-free

* `obstruction`, `obstruction_spec`: Yekutieli's Construction for `g ∈ H_β(X)`
  with a chosen local lift `ξ` (`π ∘ ξ = g`, Yekutieli's "`cl²_F(j)` is
  defined"): `ξ_ij ξ_jk = ι(c_ijk) ζ̃(β_ijk) ξ_ik`.
* `obstruction_cocycle`: `c` is a Čech 2-cocycle of `𝒜` (the lemma after Yekutieli's Construction, `lem:10` in the held LaTeX).
* `obstruction_lift_change`: changing the local lift changes `c` by a
  coboundary; hence `cl2_indep`: the class `cl2 ∈ H2 U 𝒜` is well defined.
* `exists_lift_iff`, `cl2_eq_one_iff`: **Theorem 4.17, exact form** — `g` is
  `π_* η` for some object `η ∈ G_β(X)` iff `cl²(g) = 1`.
* `exists_iso_lift_iff`: **Theorem 4.17, as stated** — there is `η ∈ G_β(X)`
  with `H_β(X)(F η, g) ≠ ∅` iff `cl²(g) = 1`, under the hypothesis that sections
  of `𝒢` over each `U i` lift to `𝓔` (needed because the cocycle model fixes the
  local objects; Yekutieli instead re-chooses them). The forward direction uses
  it; the backward direction does not.

With `β = 1` this recovers the T2b torsor statement.
-/

-- Ref: [yekutieli2010] https://arxiv.org/abs/0801.0083

universe w' w v u

namespace QOU.CentralExtension.CechGerbe

open CategoryTheory Opposite QOU.CentralExtension

/-! ### Algebraic core with a central twist -/

section Core

variable {A E : Type*} [Group A] [Group E] (ι : A →* E)
  (hcen : ∀ (a : A) (e : E), ι a * e = e * ι a)
include hcen

theorem core_cocycle_tw (hinj : Function.Injective ι)
    (xij xjk xkl xik xjl xil : E) (c₁ c₂ c₃ c₄ : A) (τ₁ τ₂ τ₃ τ₄ : E)
    (hτ₁ : ∀ e : E, τ₁ * e = e * τ₁) (hτ₃ : ∀ e : E, τ₃ * e = e * τ₃)
    (h₁ : xij * xjk = ι c₁ * τ₁ * xik) (h₂ : xik * xkl = ι c₂ * τ₂ * xil)
    (h₃ : xjk * xkl = ι c₃ * τ₃ * xjl) (h₄ : xij * xjl = ι c₄ * τ₄ * xil)
    (hτ : τ₁ * τ₂ = τ₃ * τ₄) :
    c₁ * c₂ = c₃ * c₄ := by
  have l : xij * xjk * xkl = ι (c₁ * c₂) * (τ₁ * τ₂) * xil := by
    calc xij * xjk * xkl = ι c₁ * (τ₁ * (xik * xkl)) := by rw [h₁]; simp only [mul_assoc]
      _ = ι c₁ * ((τ₁ * ι c₂) * (τ₂ * xil)) := by rw [h₂]; simp only [mul_assoc]
      _ = ι (c₁ * c₂) * (τ₁ * τ₂) * xil := by rw [hτ₁, map_mul]; simp only [mul_assoc]
  have r : xij * xjk * xkl = ι (c₃ * c₄) * (τ₃ * τ₄) * xil := by
    calc xij * xjk * xkl = (xij * ι c₃) * (τ₃ * xjl) := by
          rw [mul_assoc, h₃]; simp only [mul_assoc]
      _ = ι c₃ * ((xij * τ₃) * xjl) := by rw [← hcen c₃ xij]; simp only [mul_assoc]
      _ = ι c₃ * (τ₃ * (xij * xjl)) := by rw [← hτ₃ xij]; simp only [mul_assoc]
      _ = ι c₃ * ((τ₃ * ι c₄) * (τ₄ * xil)) := by rw [h₄]; simp only [mul_assoc]
      _ = ι (c₃ * c₄) * (τ₃ * τ₄) * xil := by rw [hτ₃, map_mul]; simp only [mul_assoc]
  have e := l.symm.trans r
  rw [hτ] at e
  exact hinj (mul_right_cancel (mul_right_cancel e))

theorem core_lift_forward_tw (hinj : Function.Injective ι)
    (xij xjk xik hij hjk hik : E) (aij ajk aik c : A) (τ : E)
    (hxij : xij = ι aij * hij) (hxjk : xjk = ι ajk * hjk) (hxik : xik = ι aik * hik)
    (hc : hij * hjk = τ * hik) (hs : xij * xjk = ι c * τ * xik) :
    c = aij * ajk * aik⁻¹ := by
  have key : ι (c * aik) * (τ * hik) = ι (aij * ajk) * (τ * hik) := by
    calc ι (c * aik) * (τ * hik) = ι c * ((ι aik * τ) * hik) := by
          rw [map_mul]; simp only [mul_assoc]
      _ = ι c * τ * (ι aik * hik) := by rw [hcen aik τ]; simp only [mul_assoc]
      _ = xij * xjk := by rw [← hxik, hs]
      _ = ι aij * ((hij * ι ajk) * hjk) := by rw [hxij, hxjk]; simp only [mul_assoc]
      _ = ι (aij * ajk) * (hij * hjk) := by rw [← hcen ajk hij, map_mul]; simp only [mul_assoc]
      _ = ι (aij * ajk) * (τ * hik) := by rw [hc]
  exact eq_mul_inv_of_mul_eq (hinj (mul_right_cancel key))

theorem core_lift_back_tw (hcomm : ∀ x y : A, x * y = y * x)
    (xij xjk xik : E) (aij ajk aik c : A) (τ : E)
    (hs : xij * xjk = ι c * τ * xik) (ha : c = aij * ajk * aik⁻¹) :
    (ι aij⁻¹ * xij) * (ι ajk⁻¹ * xjk) = τ * (ι aik⁻¹ * xik) := by
  have hA : aij⁻¹ * ajk⁻¹ * c = aik⁻¹ := by
    rw [ha, hcomm aij⁻¹ ajk⁻¹]; group
  calc (ι aij⁻¹ * xij) * (ι ajk⁻¹ * xjk)
      = ι aij⁻¹ * ((xij * ι ajk⁻¹) * xjk) := by simp only [mul_assoc]
    _ = ι aij⁻¹ * ι ajk⁻¹ * (xij * xjk) := by rw [← hcen ajk⁻¹ xij]; simp only [mul_assoc]
    _ = ι (aij⁻¹ * ajk⁻¹ * c) * τ * xik := by rw [hs, map_mul, map_mul]; simp only [mul_assoc]
    _ = ι aik⁻¹ * τ * xik := by rw [hA]
    _ = τ * (ι aik⁻¹ * xik) := by rw [hcen]; simp only [mul_assoc]

theorem core_lift_change_tw (hinj : Function.Injective ι)
    (xij xjk xik : E) (tij tjk tik c c' : A) (τ : E)
    (hs : xij * xjk = ι c * τ * xik)
    (hs' : (ι tij * xij) * (ι tjk * xjk) = ι c' * τ * (ι tik * xik)) :
    c' * tik = tij * tjk * c := by
  have key : ι (c' * tik) * (τ * xik) = ι (tij * tjk * c) * (τ * xik) := by
    calc ι (c' * tik) * (τ * xik) = ι c' * ((ι tik * τ) * xik) := by
          rw [map_mul]; simp only [mul_assoc]
      _ = ι c' * τ * (ι tik * xik) := by rw [hcen tik τ]; simp only [mul_assoc]
      _ = (ι tij * xij) * (ι tjk * xjk) := hs'.symm
      _ = ι tij * ((xij * ι tjk) * xjk) := by simp only [mul_assoc]
      _ = ι tij * ι tjk * (xij * xjk) := by rw [← hcen tjk xij]; simp only [mul_assoc]
      _ = ι (tij * tjk * c) * (τ * xik) := by rw [hs, map_mul, map_mul]; simp only [mul_assoc]
  exact hinj (mul_right_cancel key)

end Core

variable {C : Type u} [Category.{v} C] {I : Type w'} {U : I → C}

/-! ### Abelian banded gerbes: Čech 2-cocycles and `H²` -/

/-- A Čech **2-cocycle** of a presheaf of groups `𝒜` on the family `U`: the
cocycle data of a gerbe banded by `𝒜` (when `𝒜` is commutative). -/
structure TwoCocycle (U : I → C) (𝒜 : Cᵒᵖ ⥤ GrpCat.{w}) extends TwoCochain U 𝒜 where
  cocycle (i j k l : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k)
      (d : T ⟶ U l) :
    ev i j k a b c * ev i k l a c d = ev j k l b c d * ev i j l a b d

namespace TwoCocycle

variable {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}

/-- The trivial 2-cocycle (the trivial gerbe). -/
def one : TwoCocycle U 𝒜 where
  ev _ _ _ _ _ _ _ := 1
  ev_precomp _ _ _ _ _ _ _ _ _ := map_one _
  cocycle _ _ _ _ _ _ _ _ _ := rfl

/-- Equivalence of banded gerbes on `U`: the cocycles differ by the coboundary
`α_ij α_jk α_ik⁻¹` of a 1-cochain of `𝒜`. -/
def Rel (c₁ c₂ : TwoCocycle U 𝒜) : Prop :=
  ∃ α : PresheafOfGroups.OneCochain 𝒜 U, ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i)
    (b : T ⟶ U j) (d : T ⟶ U k),
    c₂.ev i j k a b d = c₁.ev i j k a b d * (α.ev i j a b * α.ev j k b d * (α.ev i k a d)⁻¹)

/-- For commutative `𝒜`, `Rel` is an equivalence relation. -/
theorem equivalence_rel (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x) :
    Equivalence (Rel (U := U) (𝒜 := 𝒜)) where
  refl c := ⟨1, fun i j k T a b d => by simp⟩
  symm := by
    rintro c₁ c₂ ⟨α, hα⟩
    refine ⟨α⁻¹, fun i j k T a b d => ?_⟩
    letI : CommGroup (𝒜.obj (op T)) := { (inferInstance : Group _) with mul_comm := hcomm _ }
    simp only [PresheafOfGroups.OneCochain.inv_ev, hα]
    rw [← mul_inv, ← mul_inv, mul_inv_cancel_right]
  trans := by
    rintro c₁ c₂ c₃ ⟨α, hα⟩ ⟨α', hα'⟩
    refine ⟨α * α', fun i j k T a b d => ?_⟩
    letI : CommGroup (𝒜.obj (op T)) := { (inferInstance : Group _) with mul_comm := hcomm _ }
    simp only [PresheafOfGroups.OneCochain.mul_ev, hα', hα]
    simp only [mul_inv_rev, mul_assoc, mul_comm, mul_left_comm]

end TwoCocycle

section H2

variable {𝒜 : Cᵒᵖ ⥤ GrpCat.{w}}

variable (U 𝒜) in
/-- Čech `H²` of `𝒜` on the family `U`: equivalence classes of banded gerbes in
the cocycle model. -/
def H2 := Quot (TwoCocycle.Rel (U := U) (𝒜 := 𝒜))

/-- The class of a 2-cocycle. -/
def TwoCocycle.class (c : TwoCocycle U 𝒜) : H2 U 𝒜 := Quot.mk _ c

instance : One (H2 U 𝒜) where
  one := (TwoCocycle.one : TwoCocycle U 𝒜).class

theorem TwoCocycle.class_eq_iff (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (c₁ c₂ : TwoCocycle U 𝒜) : c₁.class = c₂.class ↔ Rel c₁ c₂ :=
  (equivalence_rel hcomm).quot_mk_eq_iff _ _

/-- A class is trivial iff a representative is a coboundary. -/
theorem TwoCocycle.class_eq_one_iff (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒜.obj T), x * y = y * x)
    (c : TwoCocycle U 𝒜) :
    c.class = 1 ↔ ∃ α : PresheafOfGroups.OneCochain 𝒜 U, ∀ (i j k : I) ⦃T : C⦄
      (a : T ⟶ U i) (b : T ⟶ U j) (d : T ⟶ U k),
      c.ev i j k a b d = α.ev i j a b * α.ev j k b d * (α.ev i k a d)⁻¹ := by
  rw [show (1 : H2 U 𝒜) = (TwoCocycle.one : TwoCocycle U 𝒜).class from rfl, eq_comm,
    TwoCocycle.class_eq_iff hcomm]
  refine exists_congr fun α => forall_congr' fun i => forall_congr' fun j =>
    forall_congr' fun k => forall_congr' fun T => forall_congr' fun a =>
    forall_congr' fun b => forall_congr' fun d => ?_
  change _ = 1 * _ ↔ _
  rw [one_mul]

end H2

/-! ### Gerbes bound by the lien of `𝒢`: twisted cocycles -/

section Twisted

variable {𝒵 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}}

/-- A **`β`-twisted 1-cocycle** of `𝒢`: a global object, presented on the
cover `U`, of the gerbe bound by `lien(𝒢)` whose twisting 2-cocycle is `β`
(valued in `𝒵`, mapped to `𝒢` by `ζ`). For `β = 1` this is a `𝒢`-torsor. -/
structure TwistedCocycle (ζ : 𝒵 ⟶ 𝒢) (β : TwoCochain U 𝒵)
    extends PresheafOfGroups.OneCochain 𝒢 U where
  ev_trans (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    ev i j a b * ev j k b c = ζ.app (op T) (β.ev i j k a b c) * ev i k a c

variable {ζ : 𝒵 ⟶ 𝒢} {β : TwoCochain U 𝒵}

/-- **Isomorphisms preserve the twist.** If `g` is a `β`-twisted cocycle and
the cochain `g'` is isomorphic to it (Mathlib's `OneCohomologyRelation`: a
0-cochain `h` with `h_i g_ij = g'_ij h_j`), then `g'` is `β`-twisted as well, so
the isomorphisms of the gerbe are the `OneCohomologyRelation`s. Needs `ζ`
central. -/
theorem TwistedCocycle.ev_trans_of_rel
    (hζ : ∀ (T : Cᵒᵖ) (z : 𝒵.obj T) (x : 𝒢.obj T), ζ.app T z * x = x * ζ.app T z)
    (g : TwistedCocycle ζ β) (g' : PresheafOfGroups.OneCochain 𝒢 U)
    (h : PresheafOfGroups.ZeroCochain 𝒢 U)
    (hr : PresheafOfGroups.OneCohomologyRelation g.toOneCochain g' h)
    (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    g'.ev i j a b * g'.ev j k b c = ζ.app (op T) (β.ev i j k a b c) * g'.ev i k a c := by
  have e : ∀ (i j : I) (a : T ⟶ U i) (b : T ⟶ U j), g'.ev i j a b =
      𝒢.map a.op (h i) * g.ev i j a b * (𝒢.map b.op (h j))⁻¹ := fun i j a b => by
    rw [hr i j a b]; group
  rw [e i j a b, e j k b c, e i k a c]
  calc 𝒢.map a.op (h i) * g.ev i j a b * (𝒢.map b.op (h j))⁻¹ *
        (𝒢.map b.op (h j) * g.ev j k b c * (𝒢.map c.op (h k))⁻¹)
      = 𝒢.map a.op (h i) * (g.ev i j a b * g.ev j k b c) * (𝒢.map c.op (h k))⁻¹ := by group
    _ = 𝒢.map a.op (h i) * (ζ.app (op T) (β.ev i j k a b c) * g.ev i k a c) *
          (𝒢.map c.op (h k))⁻¹ := by rw [g.ev_trans]
    _ = (𝒢.map a.op (h i) * ζ.app (op T) (β.ev i j k a b c)) * g.ev i k a c *
          (𝒢.map c.op (h k))⁻¹ := by group
    _ = _ := by rw [← hζ]; group

/-- **Cohomologous twists give corresponding objects.** If `β' = β · ∂t` for a
1-cochain `t` of `𝒵`, then `ζ(t) · g` is `β'`-twisted whenever `g` is
`β`-twisted. (Equivalent banded gerbes have corresponding objects.) -/
def TwistedCocycle.retwist
    (hζ : ∀ (T : Cᵒᵖ) (z : 𝒵.obj T) (x : 𝒢.obj T), ζ.app T z * x = x * ζ.app T z)
    (hcomm : ∀ (T : Cᵒᵖ) (x y : 𝒵.obj T), x * y = y * x)
    (g : TwistedCocycle ζ β) (t : PresheafOfGroups.OneCochain 𝒵 U) (β' : TwoCochain U 𝒵)
    (hβ : ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
      β'.ev i j k a b c = β.ev i j k a b c * (t.ev i j a b * t.ev j k b c * (t.ev i k a c)⁻¹)) :
    TwistedCocycle ζ β' where
  ev i j _ a b := ζ.app _ (t.ev i j a b) * g.ev i j a b
  ev_precomp i j T T' φ a b := by
    rw [map_mul, ← NatTrans.naturality_apply, PresheafOfGroups.OneCochain.ev_precomp,
      PresheafOfGroups.OneCochain.ev_precomp]
  ev_trans i j k T a b c := by
    have key : t.ev i j a b * t.ev j k b c * β.ev i j k a b c =
        β'.ev i j k a b c * t.ev i k a c := by
      rw [hβ, hcomm _ _ (β.ev i j k a b c)]; group
    calc ζ.app (op T) (t.ev i j a b) * g.ev i j a b * (ζ.app (op T) (t.ev j k b c) * g.ev j k b c)
        = ζ.app (op T) (t.ev i j a b) * (g.ev i j a b * ζ.app (op T) (t.ev j k b c)) *
            g.ev j k b c := by group
      _ = ζ.app (op T) (t.ev i j a b) * ζ.app (op T) (t.ev j k b c) *
            (g.ev i j a b * g.ev j k b c) := by rw [← hζ]; group
      _ = ζ.app (op T) (t.ev i j a b * t.ev j k b c * β.ev i j k a b c) * g.ev i k a c := by
            rw [g.ev_trans, map_mul, map_mul]; group
      _ = ζ.app (op T) (β'.ev i j k a b c) * (ζ.app (op T) (t.ev i k a c) * g.ev i k a c) := by
            rw [key, map_mul]; group

end Twisted

/-! ### Central extensions of gerbes (cocycle model) -/

/-- A **central extension of gerbes** in the cocycle model (Yekutieli Def 3.21,
restricted to gerbes bound by `lien(𝒢)` with central twist): a central
extension `1 → 𝒜 → 𝓔 → 𝒢` of presheaves of groups, together with a central
lift `ζE : 𝒵 ⟶ 𝓔` of the twisting map `ζG : 𝒵 ⟶ 𝒢`. For a 2-cocycle `β` of
`𝒵`, `G_β = TwistedCocycle ζE β`, `H_β = TwistedCocycle ζG β`, and `F = π_*`
(`pushTw`). -/
structure CentralGerbeExtension (𝒵 𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w})
    extends PresheafCentralExtension 𝒜 𝓔 𝒢 where
  ζE : 𝒵 ⟶ 𝓔
  ζG : 𝒵 ⟶ 𝒢
  fac (T : Cᵒᵖ) (z : 𝒵.obj T) : π.app T (ζE.app T z) = ζG.app T z
  ζE_central (T : Cᵒᵖ) (z : 𝒵.obj T) (e : 𝓔.obj T) : ζE.app T z * e = e * ζE.app T z

namespace CentralGerbeExtension

variable {𝒵 𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}} (X : CentralGerbeExtension 𝒵 𝒜 𝓔 𝒢)

/-- The functor `F = π_* : G_β → H_β` on objects. -/
def pushTw {β : TwoCochain U 𝒵} (η : TwistedCocycle X.ζE β) : TwistedCocycle X.ζG β where
  ev i j _ a b := X.π.app _ (η.ev i j a b)
  ev_precomp i j T T' φ a b := by
    rw [← NatTrans.naturality_apply, PresheafOfGroups.OneCochain.ev_precomp]
  ev_trans i j k T a b c := by
    rw [← map_mul, η.ev_trans, map_mul, X.fac]

variable (β : TwoCocycle U 𝒵) (g : TwistedCocycle X.ζG β.toTwoCochain)
  (ξ : PresheafOfGroups.OneCochain 𝓔 U)
  (hξ : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
    X.π.app (op T) (ξ.ev i j a b) = g.ev i j a b)

include hξ in
theorem defect_mem (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    ∃ x, X.ι.app (op T) x = ξ.ev i j a b * ξ.ev j k b c * (ξ.ev i k a c)⁻¹ *
      (X.ζE.app (op T) (β.ev i j k a b c))⁻¹ := by
  apply (X.exact (op T) _).1
  simp only [map_mul, map_inv, hξ, X.fac, g.ev_trans, mul_inv_cancel_right, mul_inv_cancel]

/-- **Yekutieli's Construction** in the cocycle model: the obstruction
2-cochain of the object `g ∈ H_β(X)` relative to the local lift `ξ`. -/
noncomputable def obstruction : TwoCochain U 𝒜 where
  ev i j k _ a b c := (X.defect_mem β g ξ hξ i j k a b c).choose
  ev_precomp i j k T T' φ a b c := by
    apply X.injective
    rw [NatTrans.naturality_apply, (X.defect_mem β g ξ hξ i j k a b c).choose_spec,
      (X.defect_mem β g ξ hξ i j k (φ ≫ a) (φ ≫ b) (φ ≫ c)).choose_spec,
      ← β.ev_precomp, NatTrans.naturality_apply]
    simp only [map_mul, map_inv, PresheafOfGroups.OneCochain.ev_precomp]

theorem obstruction_spec (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    ξ.ev i j a b * ξ.ev j k b c =
      X.ι.app (op T) ((X.obstruction β g ξ hξ).ev i j k a b c) *
        X.ζE.app (op T) (β.ev i j k a b c) * ξ.ev i k a c := by
  change _ = X.ι.app (op T) (X.defect_mem β g ξ hξ i j k a b c).choose * _ * _
  rw [(X.defect_mem β g ξ hξ i j k a b c).choose_spec]; group

/-- **The obstruction is a Čech 2-cocycle** (the lemma after Yekutieli's Construction, `lem:10` in the held LaTeX). -/
theorem obstruction_cocycle (i j k l : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j)
    (c : T ⟶ U k) (d : T ⟶ U l) :
    (X.obstruction β g ξ hξ).ev i j k a b c * (X.obstruction β g ξ hξ).ev i k l a c d =
      (X.obstruction β g ξ hξ).ev j k l b c d * (X.obstruction β g ξ hξ).ev i j l a b d :=
  core_cocycle_tw (X.ι.app (op T)).hom (X.central _) (X.injective _) _ _ _ _ _ _ _ _ _ _
    _ _ _ _ (X.ζE_central _ _) (X.ζE_central _ _)
    (X.obstruction_spec β g ξ hξ i j k a b c) (X.obstruction_spec β g ξ hξ i k l a c d)
    (X.obstruction_spec β g ξ hξ j k l b c d) (X.obstruction_spec β g ξ hξ i j l a b d)
    (by rw [← map_mul, ← map_mul, β.cocycle])

/-- The obstruction, packaged as a 2-cocycle. -/
noncomputable def obstructionCocycle : TwoCocycle U 𝒜 where
  toTwoCochain := X.obstruction β g ξ hξ
  cocycle := X.obstruction_cocycle β g ξ hξ

/-- **Independence of the local lift**: two local lifts give equivalent
obstruction cocycles. -/
theorem obstruction_lift_change (ξ' : PresheafOfGroups.OneCochain 𝓔 U)
    (hξ' : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      X.π.app (op T) (ξ'.ev i j a b) = g.ev i j a b) :
    TwoCocycle.Rel (X.obstructionCocycle β g ξ hξ) (X.obstructionCocycle β g ξ' hξ') := by
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
  have hs' := X.obstruction_spec β g ξ' hξ' i j k a b c
  rw [ht i j a b, ht j k b c, ht i k a c] at hs'
  have e := core_lift_change_tw (X.ι.app (op T)).hom (X.central _) (X.injective _) _ _ _ _ _ _ _ _
    _ (X.obstruction_spec β g ξ hξ i j k a b c) hs'
  change (X.obstruction β g ξ' hξ').ev i j k a b c =
    (X.obstruction β g ξ hξ).ev i j k a b c * _
  rw [eq_mul_inv_of_mul_eq e, X.comm _ (t.ev i j a b * t.ev j k b c)]
  group

/-- The **obstruction class** `cl²_F(g) ∈ Ȟ²(U, 𝒜)` (Yekutieli Def 4.15). -/
noncomputable def cl2 : H2 U 𝒜 := (X.obstructionCocycle β g ξ hξ).class

/-- The obstruction class does not depend on the local lift. -/
theorem cl2_indep (ξ' : PresheafOfGroups.OneCochain 𝓔 U)
    (hξ' : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      X.π.app (op T) (ξ'.ev i j a b) = g.ev i j a b) :
    X.cl2 β g ξ hξ = X.cl2 β g ξ' hξ' :=
  Quot.sound (X.obstruction_lift_change β g ξ hξ ξ' hξ')

/-- **Theorem 4.17, exact form, cochain level.** `g = π_* η` for an object
`η ∈ G_β(X)` iff the obstruction is a coboundary. -/
theorem exists_lift_iff :
    (∃ η : TwistedCocycle X.ζE β.toTwoCochain, ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i)
        (b : T ⟶ U j), X.π.app (op T) (η.ev i j a b) = g.ev i j a b) ↔
      ∃ α : PresheafOfGroups.OneCochain 𝒜 U, ∀ (i j k : I) ⦃T : C⦄ (a : T ⟶ U i)
        (b : T ⟶ U j) (c : T ⟶ U k),
        (X.obstruction β g ξ hξ).ev i j k a b c =
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
    exact core_lift_forward_tw (X.ι.app (op T)).hom (X.central _) (X.injective _)
      _ _ _ _ _ _ _ _ _ _ _
      (hx i j a b) (hx j k b c) (hx i k a c) (η.ev_trans i j k a b c)
      (X.obstruction_spec β g ξ hξ i j k a b c)
  · rintro ⟨α, hα⟩
    refine ⟨{ ev := fun i j _ a b => X.ι.app _ (α.ev i j a b)⁻¹ * ξ.ev i j a b
              ev_precomp := by
                intro i j T T' φ a b
                rw [map_mul, ← NatTrans.naturality_apply, map_inv,
                  PresheafOfGroups.OneCochain.ev_precomp,
                  PresheafOfGroups.OneCochain.ev_precomp]
              ev_trans := by
                intro i j k T a b c
                exact core_lift_back_tw (X.ι.app (op T)).hom (X.central _)
                  (X.comm _) _ _ _ _ _ _ _ _ (X.obstruction_spec β g ξ hξ i j k a b c)
                  (hα i j k a b c) }, ?_⟩
    intro i j T a b
    have h1 : X.π.app (op T) (X.ι.app (op T) (α.ev i j a b)⁻¹) = 1 :=
      (X.exact _ _).2 ⟨_, rfl⟩
    change X.π.app (op T) (X.ι.app (op T) (α.ev i j a b)⁻¹ * ξ.ev i j a b) = _
    rw [map_mul, h1, one_mul, hξ]

/-- **Theorem 4.17, exact form, class level**: `g` is `F` of an object of
`G_β(X)` iff `cl²_F(g) = 1`. -/
theorem cl2_eq_one_iff :
    X.cl2 β g ξ hξ = 1 ↔
      ∃ η : TwistedCocycle X.ζE β.toTwoCochain, ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i)
        (b : T ⟶ U j), X.π.app (op T) (η.ev i j a b) = g.ev i j a b :=
  (TwoCocycle.class_eq_one_iff X.comm _).trans (X.exists_lift_iff β g ξ hξ).symm

/-- **Theorem 4.17 (Yekutieli), cocycle model.** There is an object
`η ∈ G_β(X)` with `H_β(X)(F η, g) ≠ ∅` iff `cl²_F(g) = 1`, provided sections of
`𝒢` over each member `U i` of the cover lift to `𝓔` (`hsurj`, used only in the
forward direction; it is the price of fixing the local objects in the cocycle
model). -/
theorem exists_iso_lift_iff (hsurj : ∀ i, Function.Surjective (X.π.app (op (U i)))) :
    (∃ (η : TwistedCocycle X.ζE β.toTwoCochain) (h : PresheafOfGroups.ZeroCochain 𝒢 U),
        PresheafOfGroups.OneCohomologyRelation (X.pushTw η).toOneCochain g.toOneCochain h) ↔
      X.cl2 β g ξ hξ = 1 := by
  rw [X.cl2_eq_one_iff]
  constructor
  · rintro ⟨η, h, hr⟩
    choose h' hh' using fun i => hsurj i (h i)
    have hπ : ∀ (i : I) ⦃T : C⦄ (a : T ⟶ U i),
        X.π.app (op T) (𝓔.map a.op (h' i)) = 𝒢.map a.op (h i) := fun i T a => by
      rw [NatTrans.naturality_apply, hh']
    refine ⟨{ ev := fun i j _ a b =>
                𝓔.map a.op (h' i) * η.ev i j a b * (𝓔.map b.op (h' j))⁻¹
              ev_precomp := by
                intro i j T T' φ a b
                simp only [map_mul, map_inv, PresheafOfGroups.OneCochain.ev_precomp, op_comp,
                  Functor.map_comp, GrpCat.comp_apply]
              ev_trans := by
                intro i j k T a b c
                calc 𝓔.map a.op (h' i) * η.ev i j a b * (𝓔.map b.op (h' j))⁻¹ *
                      (𝓔.map b.op (h' j) * η.ev j k b c * (𝓔.map c.op (h' k))⁻¹)
                    = 𝓔.map a.op (h' i) * (η.ev i j a b * η.ev j k b c) *
                        (𝓔.map c.op (h' k))⁻¹ := by group
                  _ = 𝓔.map a.op (h' i) * X.ζE.app (op T) (β.ev i j k a b c) * η.ev i k a c *
                        (𝓔.map c.op (h' k))⁻¹ := by rw [η.ev_trans]; group
                  _ = _ := by rw [← X.ζE_central]; group }, ?_⟩
    intro i j T a b
    change X.π.app (op T)
      (𝓔.map a.op (h' i) * η.ev i j a b * (𝓔.map b.op (h' j))⁻¹) = _
    have hr' := hr i j a b
    change 𝒢.map a.op (h i) * X.π.app (op T) (η.ev i j a b) = g.ev i j a b * 𝒢.map b.op (h j)
      at hr'
    rw [map_mul, map_mul, map_inv, hπ, hπ, hr']
    group
  · rintro ⟨η, hη⟩
    refine ⟨η, 1, fun i j T a b => ?_⟩
    change 𝒢.map a.op 1 * X.π.app (op T) (η.ev i j a b) = g.ev i j a b * 𝒢.map b.op 1
    rw [map_one, map_one, one_mul, mul_one, hη]

end CentralGerbeExtension


end QOU.CentralExtension.CechGerbe
