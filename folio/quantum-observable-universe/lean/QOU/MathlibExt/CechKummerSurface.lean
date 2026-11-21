import QOU.MathlibExt.CechColimitConverse
import QOU.MathlibExt.CechChernClass

/-!
# The Kummer class of a surface in the colimit `Ȟ²` (route R3, conditional)

This file puts together the colimit obstruction class of
`QOU.MathlibExt.CechColimit` (G1), its converse in
`QOU.MathlibExt.CechColimitConverse` (G1b), and the cochain-level Kummer
relation `obstrₙ = κ ∘ c₁` of `QOU.MathlibExt.CechChernClass` (T3-D1).

## Built here (sorry-free)

* `TwoCocycle.map`, `CechH2.map`: change of coefficients along a morphism of
  presheaves of groups, on cocycles and on the colimit `Ȟ²`.
* `chernCocycle`: the Čech Chern cochain `c₁(γ)` as a 2-cocycle.
* `cechKummer_eq_map_chern`: in the colimit, the Kummer obstruction class of a
  `U(1)`-cocycle `γ` (the obstruction to an `n`-th root of `γ`) is the image of
  `[c₁(γ)]` under reduction `κ : ℤ → μₙ`. This is the class-level form of
  `kummer_obstruction`.

## Conditional (the hypotheses are named, not proved)

The identification `Ȟ²(S, μₙ) ≅ ℤ/n` and the value `deg c₁(T_S) = χ(S)` are not
in Mathlib: Mathlib has no Čech-to-singular comparison and no surface
cohomology. They enter as the class `KummerSurfaceData` and the explicit
hypothesis `hχ`. Under them:

* `kummer_class_trivial_iff`: the Kummer class of `γ` is trivial iff `n ∣ χ`.
* `exists_nthRoot_on_refinement_iff`: `γ` has an `n`-th root on some finer
  admissible cover iff `n ∣ χ` (uses G1b).
* `bring_kummer_trivial_iff`: for `χ = −6` (a closed surface of genus 4, such as
  Bring's curve), the class is trivial iff `n ∣ 6`.

What is **not** established: that `KummerSurfaceData` holds for a given
surface, that the transition cocycle of `T_S` admits local real lifts on an
admissible cover, or the degree formula `hχ`. These are classical theorems of
topology (Čech cohomology of a paracompact manifold with constant coefficients,
orientation class, Poincaré–Hopf), recorded here as hypotheses.
-/

-- Ref: [manuscript] lifting-and-descent, route R3 (gerbe of n-th roots of T_S)

universe w' w v u

open CategoryTheory Opposite TopologicalSpace

namespace QOU.CentralExtension.CechGerbe

variable {C : Type u} [Category.{v} C]

/-! ### Change of coefficients -/

section Map

variable {I : Type w'} {U : I → C} {𝒜 𝒜' : Cᵒᵖ ⥤ GrpCat.{w}} (φ : 𝒜 ⟶ 𝒜')

/-- Two 2-cocycles with the same underlying cochain are equal. -/
theorem TwoCocycle.ext_cochain {c d : TwoCocycle U 𝒜} (h : c.toTwoCochain = d.toTwoCochain) :
    c = d := by
  cases c; cases d; subst h; rfl

/-- Push a 2-cocycle forward along a morphism of presheaves of groups. -/
def TwoCocycle.map (c : TwoCocycle U 𝒜) : TwoCocycle U 𝒜' where
  ev i j k _ a b d := φ.app _ (c.ev i j k a b d)
  ev_precomp i j k T T' g a b d := by
    rw [← NatTrans.naturality_apply, TwoCochain.ev_precomp]
  cocycle i j k l _ a b d e := by
    rw [← map_mul, ← map_mul, c.cocycle]

@[simp] theorem TwoCocycle.map_ev (c : TwoCocycle U 𝒜) (i j k : I) ⦃T : C⦄
    (a : T ⟶ U i) (b : T ⟶ U j) (d : T ⟶ U k) :
    (c.map φ).ev i j k a b d = φ.app _ (c.ev i j k a b d) := rfl

theorem TwoCocycle.one_map : (TwoCocycle.one : TwoCocycle U 𝒜).map φ = TwoCocycle.one := by
  apply TwoCocycle.ext_cochain
  ext i j k T a b d
  exact map_one _

/-- Cohomologous cocycles push forward to cohomologous cocycles. -/
theorem TwoCocycle.Rel.map {c₁ c₂ : TwoCocycle U 𝒜} (h : TwoCocycle.Rel c₁ c₂) :
    TwoCocycle.Rel (c₁.map φ) (c₂.map φ) := by
  obtain ⟨α, hα⟩ := h
  refine ⟨mapOneCochain φ α, fun i j k T a b d => ?_⟩
  simp only [TwoCocycle.map_ev, hα, map_mul, map_inv]
  rfl

end Map

section ColimitMap

variable {X : C} {𝒜 𝒜' : Cᵒᵖ ⥤ GrpCat.{w}} {Cov : Cover.{w'} X → Prop} (φ : 𝒜 ⟶ 𝒜')

/-- Push a cocycle on an admissible cover forward. -/
def CoverCocycle.map (x : CoverCocycle 𝒜 Cov) : CoverCocycle 𝒜' Cov :=
  ⟨x.cov, x.adm, x.c.map φ⟩

/-- **Change of coefficients on the colimit `Ȟ²`.** It is well defined because
pushing forward commutes with refinement (definitionally) and preserves the
cohomology relation (`TwoCocycle.Rel.map`). -/
def CechH2.map : CechH2 𝒜 Cov → CechH2 𝒜' Cov :=
  Quot.lift (fun x => Quot.mk _ (x.map φ)) (fun x y h => by
    cases h with
    | refine x 𝒱 h𝒱 ρ => exact Quot.sound (CoverCocycle.Step.refine (x.map φ) 𝒱 h𝒱 ρ)
    | coh 𝒰 h𝒰 c₁ c₂ h => exact Quot.sound (CoverCocycle.Step.coh 𝒰 h𝒰 _ _ (h.map φ)))

@[simp] theorem CechH2.map_cechClass (𝒰 : Cover.{w'} X) (h𝒰 : Cov 𝒰) (c : TwoCocycle 𝒰.obj 𝒜) :
    CechH2.map φ (cechClass 𝒰 h𝒰 c) = cechClass 𝒰 h𝒰 (c.map φ) := rfl

theorem CechH2.map_one (𝒰 : Cover.{w'} X) (h𝒰 : Cov 𝒰) :
    CechH2.map φ (cechClass 𝒰 h𝒰 (TwoCocycle.one : TwoCocycle 𝒰.obj 𝒜)) =
      cechClass 𝒰 h𝒰 TwoCocycle.one := by
  rw [CechH2.map_cechClass, TwoCocycle.one_map]

end ColimitMap

end QOU.CentralExtension.CechGerbe


namespace QOU.CentralExtension.Cech

open CechGerbe

variable {X : Type} [TopologicalSpace X]

/-- The Čech Chern cochain `c₁(γ)` (relative to a real lift `ξ`) as a 2-cocycle. -/
noncomputable def chernCocycle {I : Type} {U : I → Opens X}
    (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
    (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ : IsRealLift γ ξ) : TwoCocycle U (contPresheaf X (Multiplicative ℤ)) where
  toTwoCochain := chernClass γ ξ hξ
  cocycle := chernClass_cocycle γ ξ hξ

variable (n : ℕ) [NeZero n]

/-- Reduction `κ : ℤ → μₙ`, `k ↦ exp(2πik/n)`, as a morphism of presheaves. -/
noncomputable abbrev kappaMap :
    contPresheaf X (Multiplicative ℤ) ⟶ contPresheaf X (rootsOfUnityCircle n) :=
  postcomp X (kappa n) (continuous_kappa n)

variable {Cov : Cover.{0} (⊤ : Opens X) → Prop} (𝒰 : Cover.{0} (⊤ : Opens X)) (h𝒰 : Cov 𝒰)
  (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) 𝒰.obj)
  (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒰.obj)
  (hξ : IsRealLift γ ξ)

/-- **Kummer relation in the colimit `Ȟ²`.** The obstruction class to an `n`-th
root of `γ` is the reduction mod `n` of the Chern class of `γ`. -/
theorem cechKummer_eq_map_chern :
    (kummerExtension n X).cechObstruction 𝒰 h𝒰 γ (localRoot n ξ) (localRoot_lift n γ ξ hξ) =
      CechH2.map (kappaMap n) (cechClass 𝒰 h𝒰 (chernCocycle γ ξ hξ)) := by
  rw [CechH2.map_cechClass]
  unfold PresheafCentralExtension.cechObstruction
  congr 1
  apply TwoCocycle.ext_cochain
  ext i j k T a b c
  exact kummer_obstruction n γ ξ hξ i j k a b c

/-- **Topological input for a closed oriented surface `S` (hypothesis, not
proved).** A degree map on `Ȟ²(S, ℤ)`, a degree map on `Ȟ²(S, μₙ)` that detects
the trivial class (the injectivity half of `Ȟ²(S, μₙ) ≅ ℤ/n`), and compatibility
of the two with reduction mod `n`. For a closed oriented surface these follow
from the comparison of Čech and singular cohomology with constant coefficients
and the orientation class; Mathlib has neither, so they are assumed here. -/
class KummerSurfaceData (X : Type) [TopologicalSpace X] (n : ℕ) [NeZero n]
    (Cov : Cover.{0} (⊤ : Opens X) → Prop) where
  /-- degree on `Ȟ²(S, ℤ)` -/
  deg : CechH2 (contPresheaf X (Multiplicative ℤ)) Cov → ℤ
  /-- degree on `Ȟ²(S, μₙ)` -/
  degN : CechH2 (contPresheaf X (rootsOfUnityCircle n)) Cov → ZMod n
  /-- the `μₙ` degree vanishes exactly on the trivial class -/
  degN_eq_zero_iff : ∀ (𝒰 : Cover.{0} (⊤ : Opens X)) (h𝒰 : Cov 𝒰)
    (x : CechH2 (contPresheaf X (rootsOfUnityCircle n)) Cov),
    degN x = 0 ↔ x = cechClass 𝒰 h𝒰 TwoCocycle.one
  /-- reduction mod `n` commutes with the degrees -/
  degN_map : ∀ x, degN (CechH2.map (kappaMap n) x) = (deg x : ZMod n)

/-- **R3, conditional.** If `c₁(γ)` has degree `χ`, the Kummer class of `γ` is
trivial iff `n ∣ χ`. For `γ` the transition cocycle of the tangent bundle, `χ`
is the Euler characteristic (Poincaré–Hopf, assumed through `hχ`). -/
theorem kummer_class_trivial_iff [D : KummerSurfaceData X n Cov] (χ : ℤ)
    (hχ : D.deg (cechClass 𝒰 h𝒰 (chernCocycle γ ξ hξ)) = χ) :
    (kummerExtension n X).cechObstruction 𝒰 h𝒰 γ (localRoot n ξ) (localRoot_lift n γ ξ hξ) =
      cechClass 𝒰 h𝒰 TwoCocycle.one ↔ (n : ℤ) ∣ χ := by
  rw [cechKummer_eq_map_chern n 𝒰 h𝒰 γ ξ hξ, ← D.degN_eq_zero_iff 𝒰 h𝒰, D.degN_map, hχ,
    ZMod.intCast_zmod_eq_zero_iff_dvd]

/-- **R3 with the converse (G1b).** On a directed system of covers, `γ` has an
`n`-th root `η` (a `U(1)`-cocycle with `ηⁿ = γ`) on some finer admissible cover
iff `n ∣ χ`. -/
theorem exists_nthRoot_on_refinement_iff [D : KummerSurfaceData X n Cov]
    (hdir : IsCoverDirected Cov) (χ : ℤ)
    (hχ : D.deg (cechClass 𝒰 h𝒰 (chernCocycle γ ξ hξ)) = χ) :
    (∃ (𝒲 : Cover.{0} (⊤ : Opens X)) (_ : Cov 𝒲) (ρ : 𝒲.Refines 𝒰)
        (η : PresheafOfGroups.OneCocycle (contPresheaf X Circle) 𝒲.obj),
        ∀ (j j' : 𝒲.ι) ⦃T : Opens X⦄ (a : T ⟶ 𝒲.obj j) (b : T ⟶ 𝒲.obj j'),
          η.ev j j' a b ^ n = (pullOneCocycle 𝒰.obj ρ.r ρ.f γ).ev j j' a b) ↔
      (n : ℤ) ∣ χ := by
  rw [← kummer_class_trivial_iff n 𝒰 h𝒰 γ ξ hξ χ hχ,
    PresheafCentralExtension.cechObstruction_eq_one_iff _ hdir (hξ := localRoot_lift n γ ξ hξ)]
  rfl

/-- **Genus 4 (for example Bring's curve, `χ = 2 − 2·4 = −6`).** The Kummer class
of the tangent cocycle is trivial iff `n ∣ 6`. -/
theorem bring_kummer_trivial_iff [D : KummerSurfaceData X n Cov]
    (hχ : D.deg (cechClass 𝒰 h𝒰 (chernCocycle γ ξ hξ)) = -6) :
    (kummerExtension n X).cechObstruction 𝒰 h𝒰 γ (localRoot n ξ) (localRoot_lift n γ ξ hξ) =
      cechClass 𝒰 h𝒰 TwoCocycle.one ↔ n ∣ 6 := by
  rw [kummer_class_trivial_iff n 𝒰 h𝒰 γ ξ hξ (-6) hχ, dvd_neg]
  exact_mod_cast Iff.rfl

end QOU.CentralExtension.Cech
