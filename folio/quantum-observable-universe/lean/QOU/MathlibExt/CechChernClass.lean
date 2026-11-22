import QOU.MathlibExt.PresheafCentralExtensionObstruction
import Mathlib.Topology.ContinuousMap.Algebra
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Topology.Instances.Int
import Mathlib.Topology.Sets.Opens
import Mathlib.CategoryTheory.Category.Preorder

/-!
# Čech first Chern class and the Kummer relation

Tier T3-D1 of the Yekutieli central-extension programme (bean `qou-bvxd`, parent
`qou-533l`). It instantiates the presheaf lifting obstruction of
`QOU.MathlibExt.PresheafCentralExtensionObstruction` (T2b) on sheaves of continuous
functions on a topological space, and uses it to define a cochain-level Čech
first Chern class of `U(1)`-valued 1-cocycles.

## Generic additions (any site, any presheaves of groups)

* `obstruction_map`: the obstruction is natural under morphisms of central
  extensions (`α` on kernels, `ε` on middle terms, `ι' ∘ α = ε ∘ ι`).
* `obstruction_mul`: for commutative middle and quotient presheaves, the
  obstruction of `γγ'` for the lift `ξξ'` is the product of the obstructions,
  exactly at cochain level.

## Concrete sequences on `Opens X`

* `contPresheaf X G`: `V ↦ C(V, G)` for a topological group `G`.
* `expExtension X`: `0 → C(-,ℤ) →(2π·) C(-,ℝ) →exp(i·) C(-,U(1))`, exact on every
  open set (a continuous real `f` with `exp(if) = 1` is `2π` times a continuous
  integer function). Surjectivity of `exp` on sections is **not** claimed.
* `kummerExtension n X`: `1 → C(-,μₙ) → C(-,U(1)) →(·)ⁿ C(-,U(1))`, exact on every
  open set.

## The Chern class

* `chernClass γ ξ hξ`: for a `U(1)`-valued 1-cocycle `γ` with a local real lift
  `ξ` (`IsRealLift`, an explicit hypothesis), the integer 2-cochain with
  `2π·c₁ᵢⱼₖ = ξᵢⱼ + ξⱼₖ − ξᵢₖ` (`chernClass_formula`).
* `chernClass_cocycle`, `chernClass_lift_change` (lift-independence up to integer
  coboundary), `chernClass_pull` (refinement), `chernClass_mul` (exact
  additivity for product lifts), `chernClass_mul_lift` (additivity up to
  coboundary for any lift), `exists_realCocycle_iff` (`γ` is `exp(iη)` for a
  real **cocycle** `η` iff `c₁` is an integer coboundary).

## The Kummer relation

* `kappa n`: `k ↦ exp(2πik/n)`, with `kappa_eq_one_iff` (`κ k = 1 ↔ n ∣ k`) and
  `kappa_surjective`; hence `μₙ` is finite and discrete.
* `kummer_obstruction`: the `μₙ`-obstruction of `γ` for the local roots
  `exp(iξ/n)` equals `κ ∘ c₁(γ)` — "the Kummer obstruction is `c₁ mod n`" at
  cochain level.
* `exists_nthRoot_iff`: `γ` has an `n`-th root `η` (a `U(1)`-cocycle with
  `ηⁿ = γ`) iff `c₁(γ) = δβ + n·θ` for integer cochains `β`, `θ`.

## Not proved here

Existence of local real lifts (needs a good cover / simply connected overlaps),
passage to Čech cohomology groups and sheaf cohomology, the identification
`c₁ = e = χ` and its degree (Poincaré–Hopf, surface topology): see
`docs/audits/2026-10-12-t3-d1-chern.md` and bean `qou-bvxd`.
-/

-- Ref: [manuscript] lifting-and-descent, thm:qu-to-qou items 2-3 (cochain-level Chern / Kummer)


universe w' w v u

open CategoryTheory Opposite TopologicalSpace

namespace QOU.CentralExtension

/-! ### Generic additions -/

theorem core_mul_defect {E : Type*} [CommGroup E] (x x' y y' z z' : E) :
    x * x' * (y * y') * (z * z')⁻¹ = x * y * z⁻¹ * (x' * y' * z'⁻¹) := by
  simp only [mul_inv]; ac_rfl

variable {C : Type u} [Category.{v} C] {I : Type w'} {U : I → C}

/-- Push a 1-cochain forward along a morphism of presheaves of groups. -/
def mapOneCochain {F F' : Cᵒᵖ ⥤ GrpCat.{w}} (φ : F ⟶ F')
    (ξ : PresheafOfGroups.OneCochain F U) : PresheafOfGroups.OneCochain F' U where
  ev i j _ a b := φ.app _ (ξ.ev i j a b)
  ev_precomp i j T T' f a b := by
    rw [← NatTrans.naturality_apply, PresheafOfGroups.OneCochain.ev_precomp]

/-- Product of two 1-cocycles with values in a presheaf of commutative groups. -/
def mulOneCocycle {F : Cᵒᵖ ⥤ GrpCat.{w}} (hF : ∀ T (x y : F.obj T), x * y = y * x)
    (γ γ' : PresheafOfGroups.OneCocycle F U) : PresheafOfGroups.OneCocycle F U where
  toOneCochain := γ.toOneCochain * γ'.toOneCochain
  ev_trans i j k T a b c := by
    simp only [PresheafOfGroups.OneCochain.mul_ev]
    rw [← γ.ev_trans i j k a b c, ← γ'.ev_trans i j k a b c]
    letI : CommGroup (F.obj (op T)) := { (inferInstance : Group (F.obj (op T))) with
      mul_comm := hF _ }
    exact mul_mul_mul_comm _ _ _ _

namespace PresheafCentralExtension

variable {𝒜 𝓔 𝒢 : Cᵒᵖ ⥤ GrpCat.{w}} (X : PresheafCentralExtension 𝒜 𝓔 𝒢)
  (γ : PresheafOfGroups.OneCocycle 𝒢 U) (ξ : PresheafOfGroups.OneCochain 𝓔 U)
  (hξ : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
    X.π.app (op T) (ξ.ev i j a b) = γ.ev i j a b)

theorem ι_obstruction (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    X.ι.app (op T) ((X.obstruction γ ξ hξ).ev i j k a b c) =
      ξ.ev i j a b * ξ.ev j k b c * (ξ.ev i k a c)⁻¹ :=
  (X.defect_mem γ ξ hξ i j k a b c).choose_spec

/-- **Naturality in the extension.** A morphism of central extensions whose
kernel part `α` and middle part `ε` commute with the inclusions carries the
obstruction of `ξ` to the obstruction of `ε ∘ ξ` (for any cocycle `γ'` that
`ε ∘ ξ` lifts). -/
theorem obstruction_map {𝒜' 𝓔' 𝒢' : Cᵒᵖ ⥤ GrpCat.{w}}
    (X' : PresheafCentralExtension 𝒜' 𝓔' 𝒢') (α : 𝒜 ⟶ 𝒜') (ε : 𝓔 ⟶ 𝓔')
    (hαε : ∀ (T : Cᵒᵖ) (a : 𝒜.obj T), X'.ι.app T (α.app T a) = ε.app T (X.ι.app T a))
    (γ' : PresheafOfGroups.OneCocycle 𝒢' U)
    (hξ' : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      X'.π.app (op T) ((mapOneCochain ε ξ).ev i j a b) = γ'.ev i j a b)
    (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    (X'.obstruction γ' (mapOneCochain ε ξ) hξ').ev i j k a b c =
      α.app _ ((X.obstruction γ ξ hξ).ev i j k a b c) := by
  apply X'.injective
  rw [hαε, ι_obstruction, ι_obstruction]
  simp only [mapOneCochain, map_mul, map_inv]

/-- **Multiplicativity.** When the middle and quotient presheaves have
commutative section groups, the obstruction of a product of cocycles, for the
product of the local lifts, is the product of the obstructions — exactly, at
cochain level. -/
theorem obstruction_mul (hE : ∀ T (x y : 𝓔.obj T), x * y = y * x)
    (hG : ∀ T (x y : 𝒢.obj T), x * y = y * x)
    (γ' : PresheafOfGroups.OneCocycle 𝒢 U) (ξ' : PresheafOfGroups.OneCochain 𝓔 U)
    (hξ' : ∀ (i j : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      X.π.app (op T) (ξ'.ev i j a b) = γ'.ev i j a b)
    (i j k : I) ⦃T : C⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k) :
    (X.obstruction (mulOneCocycle hG γ γ') (ξ * ξ')
        (fun i j T a b => by
          simp only [PresheafOfGroups.OneCochain.mul_ev, map_mul, hξ, hξ']; rfl)).ev
        i j k a b c =
      (X.obstruction γ ξ hξ).ev i j k a b c * (X.obstruction γ' ξ' hξ').ev i j k a b c := by
  apply X.injective
  rw [map_mul, ι_obstruction, ι_obstruction, ι_obstruction]
  simp only [PresheafOfGroups.OneCochain.mul_ev]
  letI : CommGroup (𝓔.obj (op T)) := { (inferInstance : Group (𝓔.obj (op T))) with
    mul_comm := hE _ }
  exact core_mul_defect _ _ _ _ _ _

end PresheafCentralExtension


/-! ### Presheaves of continuous maps on a topological space -/

namespace Cech

variable (X : Type w) [TopologicalSpace X]

/-- The presheaf of groups `V ↦ C(V, G)` on the opens of `X`, for a topological
group `G`; restriction is precomposition with the inclusion. -/
def contPresheaf (G : Type w) [TopologicalSpace G] [Group G] [IsTopologicalGroup G] :
    (Opens X)ᵒᵖ ⥤ GrpCat.{w} where
  obj V := GrpCat.of C(V.unop, G)
  map {V W} f := GrpCat.ofHom (ContinuousMap.compMonoidHom'
    ⟨Set.inclusion (leOfHom f.unop), continuous_inclusion _⟩)
  map_id _ := by ext; rfl
  map_comp _ _ := by ext; rfl

/-- Postcomposition with a continuous homomorphism, as a morphism of presheaves. -/
def postcomp {G H : Type w} [TopologicalSpace G] [Group G] [IsTopologicalGroup G]
    [TopologicalSpace H] [Group H] [IsTopologicalGroup H] (φ : G →* H) (hφ : Continuous φ) :
    contPresheaf X G ⟶ contPresheaf X H where
  app V := GrpCat.ofHom (φ.compLeftContinuous (α := V.unop) hφ)
  naturality _ _ _ := by ext; rfl

variable {X}

/-- A section of `contPresheaf X G` over `V`, viewed as a continuous map. -/
abbrev sec {G : Type w} [TopologicalSpace G] [Group G] [IsTopologicalGroup G]
    {V : (Opens X)ᵒᵖ} (f : (contPresheaf X G).obj V) : C(V.unop, G) := f

theorem postcomp_apply {G H : Type w} [TopologicalSpace G] [Group G] [IsTopologicalGroup G]
    [TopologicalSpace H] [Group H] [IsTopologicalGroup H] (φ : G →* H) (hφ : Continuous φ)
    (V : (Opens X)ᵒᵖ) (f : (contPresheaf X G).obj V) (x : V.unop) :
    sec ((postcomp X φ hφ).app V f) x = φ (sec f x) := rfl

theorem contPresheaf_comm {G : Type w} [TopologicalSpace G] [CommGroup G]
    [IsTopologicalGroup G] (V : (Opens X)ᵒᵖ) (f g : (contPresheaf X G).obj V) :
    f * g = g * f :=
  ContinuousMap.ext fun x => mul_comm (sec f x) (sec g x)

end Cech

/-! ### The exponential sequence `ℤ → ℝ → U(1)` -/

namespace Cech

/-- `k ↦ 2πk`, written multiplicatively. -/
noncomputable def intToReal : Multiplicative ℤ →* Multiplicative ℝ :=
  AddMonoidHom.toMultiplicative ((AddMonoidHom.mulRight (2 * Real.pi)).comp (Int.castAddHom ℝ))

theorem toAdd_intToReal (k : Multiplicative ℤ) :
    Multiplicative.toAdd (intToReal k) = ((Multiplicative.toAdd k : ℤ) : ℝ) * (2 * Real.pi) := rfl

theorem continuous_intToReal : Continuous intToReal := continuous_of_discreteTopology

/-- `t ↦ exp(it)`, written multiplicatively. -/
noncomputable def realToCircle : Multiplicative ℝ →* Circle where
  toFun t := Circle.exp (Multiplicative.toAdd t)
  map_one' := by simp
  map_mul' a b := by simp [Circle.exp_add]

theorem realToCircle_apply (t : Multiplicative ℝ) :
    realToCircle t = Circle.exp (Multiplicative.toAdd t) := rfl

theorem continuous_realToCircle : Continuous realToCircle :=
  Circle.exp.continuous.comp continuous_toAdd

variable (X : Type) [TopologicalSpace X]

/-- **The exponential sequence** `0 → C(-,ℤ) → C(-,ℝ) → C(-,U(1))` of presheaves on
the opens of `X` (written multiplicatively), with `ℤ → ℝ` the map `k ↦ 2πk` and
`ℝ → U(1)` the map `t ↦ exp(it)`. Exactness is proved on every open set: a
continuous real function with `exp(i f) = 1` is `2π` times a continuous (hence
locally constant) integer-valued function. Surjectivity of `C(V,ℝ) → C(V,U(1))`
is **not** claimed (it fails, e.g., for `V` an annulus). -/
noncomputable def expExtension :
    PresheafCentralExtension (contPresheaf X (Multiplicative ℤ))
      (contPresheaf X (Multiplicative ℝ)) (contPresheaf X Circle) where
  ι := postcomp X intToReal continuous_intToReal
  π := postcomp X realToCircle continuous_realToCircle
  injective T f g h := by
    apply ContinuousMap.ext
    intro x
    have hx : Multiplicative.toAdd (intToReal (sec f x)) =
        Multiplicative.toAdd (intToReal (sec g x)) :=
      congrArg (fun F : C(T.unop, Multiplicative ℝ) => Multiplicative.toAdd (F x)) h
    rw [toAdd_intToReal, toAdd_intToReal] at hx
    have h2 : (2 * Real.pi) ≠ 0 := by positivity
    have h3 : ((Multiplicative.toAdd (sec f x) : ℤ) : ℝ) = (Multiplicative.toAdd (sec g x) : ℤ) :=
      mul_right_cancel₀ h2 hx
    exact Multiplicative.toAdd.injective (by exact_mod_cast h3)
  exact T e := by
    constructor
    · intro he
      have hx : ∀ x : T.unop, ∃ n : ℤ,
          Multiplicative.toAdd (sec e x) = n * (2 * Real.pi) := by
        intro x
        have := congrArg (fun F : C(T.unop, Circle) => F x) he
        exact Circle.exp_eq_one.1 this
      choose n hn using hx
      have hcont : Continuous n := by
        rw [Int.isClosedEmbedding_coe_real.isEmbedding.continuous_iff]
        have : ((↑) ∘ n : T.unop → ℝ) = fun x =>
            Multiplicative.toAdd (sec e x) / (2 * Real.pi) := by
          funext x
          have h2 : (2 * Real.pi) ≠ 0 := by positivity
          simp [hn x, h2]
        rw [this]
        exact (continuous_toAdd.comp (sec e).continuous).div_const _
      refine ⟨(⟨fun x => Multiplicative.ofAdd (n x), continuous_ofAdd.comp hcont⟩ :
        C(T.unop, Multiplicative ℤ)), ?_⟩
      apply ContinuousMap.ext
      intro x
      apply Multiplicative.toAdd.injective
      rw [postcomp_apply, toAdd_intToReal, hn x]
      rfl
    · rintro ⟨a, rfl⟩
      apply ContinuousMap.ext
      intro x
      change realToCircle (intToReal (sec a x)) = 1
      rw [realToCircle_apply, toAdd_intToReal]
      exact Circle.exp_int_mul_two_pi _
  central T a e := contPresheaf_comm T _ _
  comm T x y := contPresheaf_comm T x y

end Cech


/-! ### The Čech first Chern class -/

namespace Cech

variable {X : Type} [TopologicalSpace X] {I : Type} {U : I → Opens X}

/-- A local **real lift** of a `U(1)`-valued 1-cocycle `γ`: a 1-cochain `ξ` of
continuous real functions on the overlaps with `exp(i ξ) = γ`. Such a lift
exists when every overlap admits a continuous logarithm (e.g. for a cover by
opens with simply connected overlaps); that existence statement is **not**
proved here and is an explicit hypothesis. -/
def IsRealLift (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
    (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U) : Prop :=
  ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j),
    (expExtension X).π.app (op T) (ξ.ev i j a b) = γ.ev i j a b

/-- **The Čech first Chern class** (cochain level) of a `U(1)`-valued 1-cocycle
`γ`, relative to a local real lift `ξ`: the obstruction of `γ` for the
exponential sequence. Concretely `2π · c₁ᵢⱼₖ = ξᵢⱼ + ξⱼₖ − ξᵢₖ`. -/
noncomputable def chernClass (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
    (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ : IsRealLift γ ξ) : TwoCochain U (contPresheaf X (Multiplicative ℤ)) :=
  (expExtension X).obstruction γ ξ hξ

variable (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
  (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
  (hξ : IsRealLift γ ξ)

/-- The defining formula: `2π · c₁ᵢⱼₖ(x) = ξᵢⱼ(x) + ξⱼₖ(x) − ξᵢₖ(x)`. -/
theorem chernClass_formula (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j)
    (c : T ⟶ U k) (x : T) :
    ((Multiplicative.toAdd (sec ((chernClass γ ξ hξ).ev i j k a b c) x) : ℤ) : ℝ) *
        (2 * Real.pi) =
      Multiplicative.toAdd (sec (ξ.ev i j a b) x) +
        Multiplicative.toAdd (sec (ξ.ev j k b c) x) -
        Multiplicative.toAdd (sec (ξ.ev i k a c) x) := by
  have h := congrArg (fun F => Multiplicative.toAdd (sec (V := op T) F x))
    ((expExtension X).ι_obstruction γ ξ hξ i j k a b c)
  have e : sec (V := op T) (ξ.ev i j a b * ξ.ev j k b c * (ξ.ev i k a c)⁻¹) x =
      sec (ξ.ev i j a b) x * sec (ξ.ev j k b c) x * (sec (ξ.ev i k a c) x)⁻¹ := rfl
  rw [← toAdd_intToReal]
  refine h.trans ?_
  beta_reduce
  rw [e, toAdd_mul, toAdd_mul, toAdd_inv]
  ring

/-- `c₁` is a Čech 2-cocycle. -/
theorem chernClass_cocycle (i j k l : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j)
    (c : T ⟶ U k) (d : T ⟶ U l) :
    (chernClass γ ξ hξ).ev i j k a b c * (chernClass γ ξ hξ).ev i k l a c d =
      (chernClass γ ξ hξ).ev j k l b c d * (chernClass γ ξ hξ).ev i j l a b d :=
  (expExtension X).obstruction_cocycle γ ξ hξ i j k l a b c d

/-- `c₁` does not depend on the real lift, up to the coboundary of an integer
1-cochain. -/
theorem chernClass_lift_change
    (ξ' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ' : IsRealLift γ ξ') :
    ∃ t : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U,
      ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
        (chernClass γ ξ' hξ').ev i j k a b c =
          (chernClass γ ξ hξ).ev i j k a b c *
            (t.ev i j a b * t.ev j k b c * (t.ev i k a c)⁻¹) :=
  (expExtension X).obstruction_lift_change γ ξ hξ ξ' hξ'

/-- `c₁` is natural under refinement of the cover. -/
theorem chernClass_pull {J : Type} {V : J → Opens X} (r : J → I) (f : ∀ j, V j ⟶ U (r j)) :
    chernClass (pullOneCocycle U r f γ) (pullOneCochain U r f ξ)
        (fun j j' _ a b => hξ (r j) (r j') (a ≫ f j) (b ≫ f j')) =
      pullTwoCochain U r f (chernClass γ ξ hξ) :=
  (expExtension X).obstruction_pull γ ξ hξ r f

/-- **Additivity of `c₁`** (written multiplicatively in `C(-, ℤ)`): for the
product lift, `c₁(γγ') = c₁(γ) + c₁(γ')` exactly at cochain level. -/
theorem chernClass_mul (γ' : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
    (ξ' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ' : IsRealLift γ' ξ') (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j)
    (c : T ⟶ U k) :
    (chernClass (mulOneCocycle (contPresheaf_comm) γ γ') (ξ * ξ')
        (fun i j T a b => by
          simp only [PresheafOfGroups.OneCochain.mul_ev, map_mul, hξ i j a b, hξ' i j a b]
          rfl)).ev i j k a b c =
      (chernClass γ ξ hξ).ev i j k a b c * (chernClass γ' ξ' hξ').ev i j k a b c :=
  (expExtension X).obstruction_mul γ ξ hξ contPresheaf_comm contPresheaf_comm γ' ξ' hξ'
    i j k a b c

/-- **Additivity for arbitrary lifts**: for any real lift `ζ` of `γγ'`, the class
`c₁(γγ')` differs from `c₁(γ) + c₁(γ')` by an integer coboundary. -/
theorem chernClass_mul_lift
    (γ' : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
    (ξ' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ' : IsRealLift γ' ξ')
    (ζ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hζ : IsRealLift (mulOneCocycle (contPresheaf_comm) γ γ') ζ) :
    ∃ t : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U,
      ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
        (chernClass _ ζ hζ).ev i j k a b c =
          (chernClass γ ξ hξ).ev i j k a b c * (chernClass γ' ξ' hξ').ev i j k a b c *
            (t.ev i j a b * t.ev j k b c * (t.ev i k a c)⁻¹) := by
  obtain ⟨t, ht⟩ := chernClass_lift_change (mulOneCocycle (contPresheaf_comm) γ γ') (ξ * ξ')
    (fun i j T a b => by
      simp only [PresheafOfGroups.OneCochain.mul_ev, map_mul, hξ i j a b, hξ' i j a b]
      rfl) ζ hζ
  refine ⟨t, fun i j k T a b c => ?_⟩
  rw [ht, chernClass_mul]

/-- **`c₁` is the obstruction to a global real logarithm**: `γ` lifts to a
1-cocycle of continuous real functions (`exp(iη) = γ`, `η` a cocycle) iff `c₁`
is the coboundary of an integer 1-cochain. -/
theorem exists_realCocycle_iff :
    (∃ η : PresheafOfGroups.OneCocycle (contPresheaf X (Multiplicative ℝ)) U,
        IsRealLift γ η.toOneCochain) ↔
      PresheafCentralExtension.IsCoboundary (chernClass γ ξ hξ) :=
  (expExtension X).exists_lift_iff γ ξ hξ

end Cech


/-! ### The Kummer sequence `μₙ → U(1) →ⁿ U(1)` -/

namespace Cech

variable (n : ℕ)

/-- The `n`-th roots of unity in `U(1)`, as the kernel of `z ↦ zⁿ`. -/
abbrev rootsOfUnityCircle : Subgroup Circle := (powMonoidHom n : Circle →* Circle).ker

theorem mem_rootsOfUnityCircle (z : Circle) : z ∈ rootsOfUnityCircle n ↔ z ^ n = 1 :=
  MonoidHom.mem_ker

variable (X : Type) [TopologicalSpace X]

/-- **The Kummer sequence** `1 → C(-, μₙ) → C(-, U(1)) →ⁿ C(-, U(1))` of presheaves
on the opens of `X`, exact on every open set. -/
noncomputable def kummerExtension :
    PresheafCentralExtension (contPresheaf X (rootsOfUnityCircle n))
      (contPresheaf X Circle) (contPresheaf X Circle) where
  ι := postcomp X (rootsOfUnityCircle n).subtype continuous_subtype_val
  π := postcomp X (powMonoidHom n) (continuous_pow n)
  injective T f g h := by
    apply ContinuousMap.ext
    intro x
    exact Subtype.ext (congrArg (fun F : C(T.unop, Circle) => F x) h)
  exact T e := by
    constructor
    · intro he
      have hx : ∀ x : T.unop, sec e x ∈ rootsOfUnityCircle n := fun x =>
        (mem_rootsOfUnityCircle n _).2 (congrArg (fun F : C(T.unop, Circle) => F x) he)
      exact ⟨(⟨fun x => ⟨sec e x, hx x⟩, (sec e).continuous.subtype_mk _⟩ :
        C(T.unop, rootsOfUnityCircle n)), ContinuousMap.ext fun x => rfl⟩
    · rintro ⟨a, rfl⟩
      apply ContinuousMap.ext
      intro x
      exact (mem_rootsOfUnityCircle n _).1 (sec a x).2
  central T a e := contPresheaf_comm T _ _
  comm T x y := contPresheaf_comm T x y

theorem circle_exp_pow (s : ℝ) (m : ℕ) : Circle.exp s ^ m = Circle.exp (m * s) := by
  induction m with
  | zero => simp
  | succ m ih => rw [pow_succ, ih, ← Circle.exp_add]; push_cast; ring_nf

/-- `t ↦ exp(it/n)`, the `n`-th root of `exp(it)`. -/
noncomputable def rootHom : Multiplicative ℝ →* Circle where
  toFun t := Circle.exp (Multiplicative.toAdd t / n)
  map_one' := by simp
  map_mul' a b := by simp [add_div, Circle.exp_add]

theorem continuous_rootHom : Continuous (rootHom n) :=
  Circle.exp.continuous.comp (continuous_toAdd.div_const _)

variable [NeZero n]

theorem rootHom_pow (t : Multiplicative ℝ) : rootHom n t ^ n = realToCircle t := by
  change Circle.exp (Multiplicative.toAdd t / n) ^ n = Circle.exp (Multiplicative.toAdd t)
  rw [circle_exp_pow, mul_div_cancel₀ _ (Nat.cast_ne_zero.2 (NeZero.ne n))]

/-- `k ↦ exp(2πik/n)`, the reduction `ℤ → ℤ/n ≅ μₙ`. -/
noncomputable def kappa : Multiplicative ℤ →* rootsOfUnityCircle n where
  toFun k := ⟨rootHom n (intToReal k), by
    rw [mem_rootsOfUnityCircle, rootHom_pow, realToCircle_apply, toAdd_intToReal]
    exact Circle.exp_int_mul_two_pi _⟩
  map_one' := by ext1; simp
  map_mul' a b := by ext1; simp

theorem kappa_val (k : Multiplicative ℤ) :
    ((kappa n k : rootsOfUnityCircle n) : Circle) = rootHom n (intToReal k) := rfl

theorem continuous_kappa : Continuous (kappa n) := continuous_of_discreteTopology

/-- `κ(k) = 1` iff `n ∣ k`: `κ` is reduction mod `n`. -/
theorem kappa_eq_one_iff (k : Multiplicative ℤ) :
    kappa n k = 1 ↔ (n : ℤ) ∣ Multiplicative.toAdd k := by
  have hn : (n : ℝ) ≠ 0 := Nat.cast_ne_zero.2 (NeZero.ne n)
  have hpi : (2 * Real.pi) ≠ 0 := by positivity
  rw [← Subtype.coe_inj, kappa_val, OneMemClass.coe_one]
  change Circle.exp (Multiplicative.toAdd (intToReal k) / n) = 1 ↔ _
  rw [toAdd_intToReal, Circle.exp_eq_one]
  constructor
  · rintro ⟨m, hm⟩
    refine ⟨m, ?_⟩
    have : ((Multiplicative.toAdd k : ℤ) : ℝ) = n * m := by
      field_simp at hm; linarith [hm]
    exact_mod_cast this
  · rintro ⟨m, hm⟩
    refine ⟨m, ?_⟩
    rw [hm]; push_cast; field_simp

variable {X} {I : Type} {U : I → Opens X}
  (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
  (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
  (hξ : IsRealLift γ ξ)

/-- The local `n`-th root `exp(iξ/n)` of a real lift `ξ` of `γ`. -/
noncomputable def localRoot : PresheafOfGroups.OneCochain (contPresheaf X Circle) U :=
  mapOneCochain (postcomp X (rootHom n) (continuous_rootHom n)) ξ

include hξ in
theorem localRoot_lift (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) :
    (kummerExtension n X).π.app (op T) ((localRoot n ξ).ev i j a b) = γ.ev i j a b := by
  rw [← hξ i j a b]
  apply ContinuousMap.ext
  intro x
  exact rootHom_pow n _

/-- **Kummer relation (cochain level).** The `μₙ`-obstruction of `γ` for the local
`n`-th roots `exp(iξ/n)` is the reduction mod `n` of the Chern cochain:
`obstrₙ(γ) = κ ∘ c₁(γ)`, with `κ(k) = exp(2πik/n)`. -/
theorem kummer_obstruction (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j)
    (c : T ⟶ U k) :
    ((kummerExtension n X).obstruction γ (localRoot n ξ) (localRoot_lift n γ ξ hξ)).ev
        i j k a b c =
      (postcomp X (kappa n) (continuous_kappa n)).app _ ((chernClass γ ξ hξ).ev i j k a b c) :=
  (expExtension X).obstruction_map γ ξ hξ (kummerExtension n X)
    (postcomp X (kappa n) (continuous_kappa n)) (postcomp X (rootHom n) (continuous_rootHom n))
    (fun _ _ => rfl) γ (localRoot_lift n γ ξ hξ) i j k a b c

omit [NeZero n] in
theorem kummer_π_apply (V : (Opens X)ᵒᵖ) (η : (contPresheaf X Circle).obj V) :
    (kummerExtension n X).π.app V η = η ^ n := rfl

omit [NeZero n] in
theorem roots_pow_eq_one (V : (Opens X)ᵒᵖ) (w : (contPresheaf X (rootsOfUnityCircle n)).obj V) :
    w ^ n = 1 :=
  ContinuousMap.ext fun x => Subtype.ext ((mem_rootsOfUnityCircle n _).1 (sec w x).2)

/-- **`n`-th roots from divisibility.** If `c₁(γ)` is `n`-divisible modulo
integer coboundaries, `c₁ = δβ + n·θ`, then `γ` has an `n`-th root: a
`U(1)`-valued 1-**cocycle** `η` with `ηⁿ = γ`. -/
theorem exists_nthRoot_of_dvd
    (h : ∃ (β : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U)
      (θ : TwoCochain U (contPresheaf X (Multiplicative ℤ))),
      ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
        (chernClass γ ξ hξ).ev i j k a b c =
          β.ev i j a b * β.ev j k b c * (β.ev i k a c)⁻¹ * θ.ev i j k a b c ^ n) :
    ∃ η : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U,
      ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j),
        η.ev i j a b ^ n = γ.ev i j a b := by
  obtain ⟨β, θ, hβθ⟩ := h
  have := ((kummerExtension n X).exists_lift_iff γ (localRoot n ξ)
    (localRoot_lift n γ ξ hξ)).2
    ⟨mapOneCochain (postcomp X (kappa n) (continuous_kappa n)) β, fun i j k T a b c => by
      rw [kummer_obstruction n γ ξ hξ, hβθ, map_mul, map_pow, roots_pow_eq_one, mul_one]
      simp only [mapOneCochain, map_mul, map_inv]⟩
  obtain ⟨η, hη⟩ := this
  exact ⟨η, fun i j T a b => (kummer_π_apply n _ _).symm.trans (hη i j a b)⟩


/-- Every `n`-th root of unity in `U(1)` is `exp(2πik/n)` for some integer `k`. -/
theorem kappa_surjective : Function.Surjective (kappa n) := by
  intro z
  have hn : (n : ℝ) ≠ 0 := Nat.cast_ne_zero.2 (NeZero.ne n)
  have hz : (z : Circle) ^ n = 1 := (mem_rootsOfUnityCircle n _).1 z.2
  set t := Complex.arg (z : Circle)
  have hzt : Circle.exp t = z := Circle.exp_arg z
  rw [← hzt, circle_exp_pow, Circle.exp_eq_one] at hz
  obtain ⟨m, hm⟩ := hz
  refine ⟨Multiplicative.ofAdd m, Subtype.ext ?_⟩
  rw [kappa_val, ← hzt]
  change Circle.exp (Multiplicative.toAdd (intToReal (Multiplicative.ofAdd m)) / n) = _
  rw [toAdd_intToReal, toAdd_ofAdd]
  congr 1
  field_simp
  linarith [hm]

instance : Finite (rootsOfUnityCircle n) := by
  refine Finite.of_surjective (fun r : Fin n => kappa n (Multiplicative.ofAdd (r : ℤ))) ?_
  intro z
  obtain ⟨k, rfl⟩ := kappa_surjective n z
  have hpos : (0 : ℤ) < n := by exact_mod_cast Nat.pos_of_ne_zero (NeZero.ne n)
  set m := Multiplicative.toAdd k
  have h0 : 0 ≤ m % n := Int.emod_nonneg _ hpos.ne'
  have h1 : m % n < n := Int.emod_lt_of_pos _ hpos
  refine ⟨⟨(m % n).toNat, by omega⟩, ?_⟩
  simp only
  rw [Int.toNat_of_nonneg h0]
  have hk : k = Multiplicative.ofAdd (m % n) * Multiplicative.ofAdd (n * (m / n)) := by
    apply Multiplicative.toAdd.injective
    simp only [toAdd_mul, toAdd_ofAdd]
    exact (Int.emod_add_mul_ediv m n).symm
  rw [hk, map_mul, (kappa_eq_one_iff n (Multiplicative.ofAdd ((n : ℤ) * (m / n)))).2
    ⟨m / n, rfl⟩, mul_one]

instance : DiscreteTopology (rootsOfUnityCircle n) := Finite.instDiscreteTopology

/-- A set-theoretic (hence, `μₙ` being discrete, continuous) section of `κ`. -/
noncomputable def kappaSection : rootsOfUnityCircle n → Multiplicative ℤ :=
  Function.surjInv (kappa_surjective n)

theorem kappa_kappaSection (z : rootsOfUnityCircle n) : kappa n (kappaSection n z) = z :=
  Function.surjInv_eq _ z

/-- Lift a `μₙ`-valued 1-cochain to an integer 1-cochain through `κ`. -/
noncomputable def liftRootsCochain
    (α : PresheafOfGroups.OneCochain (contPresheaf X (rootsOfUnityCircle n)) U) :
    PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U where
  ev i j T a b := (⟨kappaSection n, continuous_of_discreteTopology⟩ :
      C(rootsOfUnityCircle n, Multiplicative ℤ)).comp (sec (α.ev i j a b))
  ev_precomp i j T T' φ a b := by
    rw [← α.ev_precomp]; rfl

/-- Integer division by `n`, as a continuous self-map of the discrete group `ℤ`. -/
def divN : C(Multiplicative ℤ, Multiplicative ℤ) :=
  ⟨fun k => Multiplicative.ofAdd (Multiplicative.toAdd k / n), continuous_of_discreteTopology⟩

/-- **Kummer criterion.** `γ` has an `n`-th root — a `U(1)`-valued 1-cocycle `η`
with `ηⁿ = γ` — **iff** `c₁(γ)` is `n`-divisible modulo integer coboundaries,
`c₁ = δβ + n·θ` with `β` an integer 1-cochain and `θ` an integer 2-cochain. -/
theorem exists_nthRoot_iff :
    (∃ η : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U,
      ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j),
        η.ev i j a b ^ n = γ.ev i j a b) ↔
    ∃ (β : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U)
      (θ : TwoCochain U (contPresheaf X (Multiplicative ℤ))),
      ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
        (chernClass γ ξ hξ).ev i j k a b c =
          β.ev i j a b * β.ev j k b c * (β.ev i k a c)⁻¹ * θ.ev i j k a b c ^ n := by
  refine ⟨fun ⟨η, hη⟩ => ?_, exists_nthRoot_of_dvd n γ ξ hξ⟩
  obtain ⟨α, hα⟩ := ((kummerExtension n X).exists_lift_iff γ (localRoot n ξ)
    (localRoot_lift n γ ξ hξ)).1 ⟨η, fun i j T a b => (kummer_π_apply n _ _).trans (hη i j a b)⟩
  set β := liftRootsCochain n α
  -- `d := c₁ · (δβ)⁻¹` is pointwise divisible by `n`.
  let d : ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
      (contPresheaf X (Multiplicative ℤ)).obj (op T) := fun i j k T a b c =>
    (chernClass γ ξ hξ).ev i j k a b c * (β.ev i j a b * β.ev j k b c * (β.ev i k a c)⁻¹)⁻¹
  have hκβ : ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j),
      (postcomp X (kappa n) (continuous_kappa n)).app _ (β.ev i j a b) = α.ev i j a b := by
    intro i j T a b
    exact ContinuousMap.ext fun x => kappa_kappaSection n _
  have hd : ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k)
      (x : T), (n : ℤ) ∣ Multiplicative.toAdd (sec (d i j k a b c) x) := by
    intro i j k T a b c x
    have h1 : (postcomp X (kappa n) (continuous_kappa n)).app _ (d i j k a b c) = 1 := by
      simp only [d, map_mul, map_inv, hκβ]
      rw [← kummer_obstruction n γ ξ hξ, hα]
      group
    rw [← kappa_eq_one_iff]
    exact congrArg (fun F : C(T, rootsOfUnityCircle n) => F x) h1
  let θ : TwoCochain U (contPresheaf X (Multiplicative ℤ)) :=
    { ev := fun i j k T a b c => (divN n).comp (sec (d i j k a b c))
      ev_precomp := by
        intro i j k T T' φ a b c
        have : (contPresheaf X (Multiplicative ℤ)).map φ.op (d i j k a b c) =
            d i j k (φ ≫ a) (φ ≫ b) (φ ≫ c) := by
          simp only [d, map_mul, map_inv, TwoCochain.ev_precomp,
            PresheafOfGroups.OneCochain.ev_precomp]
        rw [← this]; rfl }
  refine ⟨β, θ, fun i j k T a b c => ?_⟩
  have hθ : θ.ev i j k a b c ^ n = d i j k a b c := by
    apply ContinuousMap.ext
    intro x
    apply Multiplicative.toAdd.injective
    change Multiplicative.toAdd ((Multiplicative.ofAdd
      (Multiplicative.toAdd (sec (d i j k a b c) x) / n)) ^ n) = _
    rw [toAdd_pow, toAdd_ofAdd, nsmul_eq_mul, mul_comm]
    exact Int.ediv_mul_cancel (hd i j k a b c x)
  rw [hθ]
  simp only [d]
  rw [contPresheaf_comm _ ((chernClass γ ξ hξ).ev i j k a b c)]
  group

end Cech

end QOU.CentralExtension
