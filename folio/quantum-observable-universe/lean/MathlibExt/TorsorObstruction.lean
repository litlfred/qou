import MathlibExt.TorsorLift
import MathlibExt.PresheafCentralExtensionObstruction

/-!
# The obstruction to lifting a torsor along a central extension

Bean `qou-0xk8` (parent `qou-533l`). Let `1 → 𝒜 → 𝓔 → 𝒢` be a central
extension of presheaves of groups (`PresheafCentralExtension`), and let `P` be
a multiplicative `𝒢`-torsor with a section `sᵢ` over each member of a family
`U` that covers the final object. Suppose the transition cocycle of the `sᵢ`
lifts on overlaps to a 1-cochain `ξ` of `𝓔`. Then:

* `toOneCocycle` / `ofOneCocycle`: the cocycles of `MathlibExt.CocycleTorsor`
  and of Mathlib's `NonabelianCohomology.H1` are the same data.
* `exists_liftAlong_iff_isCoboundary`: **`P` has a reduction along `𝓔 → 𝒢`
  carrying sections to the `sᵢ` iff the obstruction 2-cochain of `ξ` is a
  coboundary.**

This is Yekutieli's Theorem 4.17 for torsors trivialised on a cover, with the
obstruction derived, not assumed. It combines
`MathlibExt.TorsorLift.exists_liftAlong_iff` (reduction ⇔ the cocycle lifts)
with `PresheafCentralExtension.exists_lift_iff` (the cocycle lifts ⇔ the
obstruction is a coboundary). The gerbe form (Definition 3.21) is not done
here. All sorry-free and generic over a small site.

## Source

Yekutieli, *Central Extensions of Gerbes* (arXiv 0801.0083, held at
`library/arxiv-0801.0083v4/`), Thm 4.17 (torsor case).
-/

-- Ref: [yekutieli2010] Thm 4.17 (torsor case)

universe w

namespace QOU.MathlibExt.StackGerbe

open CategoryTheory Opposite QOU.CentralExtension

variable {C : Type w} [Category.{w} C] {I : Type w} {U : I → C}

/-- Sections of `F ⋙ forget` carry the group structure of `F`. -/
instance forgetGroup (F : Cᵒᵖ ⥤ GrpCat.{w}) (T : Cᵒᵖ) : Group ((F ⋙ forget GrpCat).obj T) :=
  inferInstanceAs (Group (F.obj T))

theorem isPresheafOfGroups_forget (F : Cᵒᵖ ⥤ GrpCat.{w}) :
    IsPresheafOfGroups (F ⋙ forget GrpCat) where
  map_mul f a b := (F.map f).hom.map_mul a b
  map_one f := (F.map f).hom.map_one

variable {F : Cᵒᵖ ⥤ GrpCat.{w}}

/-- A cocycle of `MathlibExt.CocycleTorsor` as a Mathlib 1-cocycle. -/
def toOneCocycle (g : TorsCocycle U (F ⋙ forget GrpCat)) : PresheafOfGroups.OneCocycle F U where
  ev := g.ev
  ev_precomp i j _ _ φ a b := g.ev_precomp i j φ a b
  ev_trans := g.ev_trans

/-- A Mathlib 1-cocycle as a cocycle of `MathlibExt.CocycleTorsor`. -/
def ofOneCocycle (γ : PresheafOfGroups.OneCocycle F U) : TorsCocycle U (F ⋙ forget GrpCat) where
  ev := γ.ev
  ev_precomp i j _ _ φ a b := γ.ev_precomp i j φ a b
  ev_trans := γ.ev_trans

variable {𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}} (X : PresheafCentralExtension 𝒜 𝓔 𝒢)

/-- The projection `𝓔 → 𝒢` on underlying presheaves of sets. -/
def projForget : 𝓔 ⋙ forget GrpCat ⟶ 𝒢 ⋙ forget GrpCat :=
  Functor.whiskerRight X.π (forget GrpCat)

theorem projForget_mul (T : Cᵒᵖ) (x y : (𝓔 ⋙ forget GrpCat).obj T) :
    (projForget X).app T (x * y) = (projForget X).app T x * (projForget X).app T y :=
  (X.π.app T).hom.map_mul x y

variable {J : GrothendieckTopology C}
variable (P : MulSheafTorsor J (𝒢 ⋙ forget GrpCat)) (s : ∀ i, P.carrier.obj (op (U i)))
variable (hU : ∀ T : C, Sieve.ofObjects U T ∈ J T) (h𝓔 : Presheaf.IsSheaf J (𝓔 ⋙ forget GrpCat))
variable (ξ : PresheafOfGroups.OneCochain 𝓔 U)
  (hξ : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
    X.π.app (op T) (ξ.ev i j a b) = (toOneCocycle (transition P s)).ev i j a b)

include hU h𝓔 in
/-- **Yekutieli Thm 4.17, torsor case.** A `𝒢`-torsor with sections `sᵢ`
whose transition cocycle lifts on overlaps to `ξ` has a reduction along
`𝓔 → 𝒢` carrying sections to the `sᵢ` iff the obstruction 2-cochain of `ξ`
is a coboundary. -/
theorem exists_liftAlong_iff_isCoboundary :
    (∃ (L : LiftAlong (projForget X) P) (t : ∀ i, L.torsor.carrier.obj (op (U i))),
        ∀ i, L.hom.app _ (t i) = s i) ↔
      PresheafCentralExtension.IsCoboundary
        (X.obstruction (toOneCocycle (transition P s)) ξ hξ) := by
  rw [exists_liftAlong_iff (projForget X) (projForget_mul X) P s
    (isPresheafOfGroups_forget 𝒢) hU (isPresheafOfGroups_forget 𝓔) h𝓔]
  unfold PresheafCentralExtension.IsCoboundary
  rw [← X.exists_lift_iff]
  constructor
  · rintro ⟨e, he⟩
    exact ⟨toOneCocycle e, he⟩
  · rintro ⟨η, hη⟩
    exact ⟨ofOneCocycle η, hη⟩

end QOU.MathlibExt.StackGerbe
