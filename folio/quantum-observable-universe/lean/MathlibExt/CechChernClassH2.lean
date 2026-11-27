import MathlibExt.CechChernClass
import MathlibExt.CechColimitConverse

/-!
# The Čech first Chern class as a cohomology class

Bean `qou-bvxd` (parent `qou-533l`). `MathlibExt.CechChernClass` builds the
first Chern class `c₁ = chernClass γ ξ hξ` of a `U(1)`-valued 1-cocycle `γ` as
an integer **2-cochain**, relative to a local real lift `ξ`. This file promotes
it to a **class**, using the Čech `H²` of `MathlibExt.CechGerbe` (one cover) and
the colimit `Ȟ²` of `MathlibExt.CechColimit` (all open covers), and proves the
class-level forms of the statements that file proves at cochain level.

Everything here is algebra on cochains of the presheaves `C(-,ℤ)`, `C(-,ℝ)`,
`C(-,U(1))`. No analytic input is used beyond what `CechChernClass` already
uses (`exp(2πik) = 1`), and no number enters.

## One cover

* `chernCocycle γ ξ hξ`: `c₁` packaged as a `TwoCocycle U C(-,ℤ)`.
* `chernH2 γ ξ hξ ∈ H2 U C(-,ℤ)`: its class.
* `chernH2_indep_lift`: the class does not depend on the real lift.
* `chernClass_conj`, `chernH2_conj`: **gauge invariance.** If `γ'ᵢⱼ = hᵢ γᵢⱼ hⱼ⁻¹`
  for a 0-cochain `h = exp(i s)` with a real lift `s`, then for the conjugated
  lift `ξ'ᵢⱼ = sᵢ + ξᵢⱼ − sⱼ` the Chern **cochains** of `γ` and `γ'` are equal,
  so their classes agree.
* `chernH2_eq_one_iff`: `c₁ = 1` in `H²` iff `γ = exp(iη)` for a real
  **cocycle** `η` (the class form of `exists_realCocycle_iff`).
* `chernH2_mul`: additivity, `[c₁(γγ')] = [c₁(γ) · c₁(γ')]` for any lifts.

## Kummer, with a cocycle quotient

* `exists_nthRoot_iff_cocycle`: `γ` has an `n`-th root iff `c₁ = δβ · θⁿ` with
  `θ` an integer 2-**cocycle** (not merely a cochain). The improvement over
  `exists_nthRoot_iff` is that `θ` is automatically closed, because `C(T,ℤ)`
  has no `n`-torsion. So the root exists iff `[c₁] ∈ n · H²` on the cover.

## All open covers

* `IsOpenCover`: a `Cover` of `⊤ : Opens X` whose members cover `X`;
  `isCoverDirected_open`: these are directed, via `{Vᵢ ∩ Wⱼ}` (`Cover.inter`).
* `cechChern`: `c₁` in the colimit `Ȟ²(X; C(-,ℤ))` over open covers, with
  `cechChern_indep_lift` and `cechChern_pull` (cover independence).
* `cechChern_eq_one_iff`: the colimit class is trivial iff, on some open
  refinement, `γ` is `exp(iη)` for a real cocycle `η`.

## Relation to `BraidKnotOctonion/CechKummerSurface`

That file (route R3) defines the same cocycle as
`CechGerbe.chernCocycle` for an abstract directed predicate `Cov` and proves
the Kummer class is `κ_*[c₁]`. This file supplies the concrete predicate
`IsOpenCover X` together with its directedness, which `cechClass_eq_one_iff`
needs.

## Not done here

Existence of local real lifts after refinement for an arbitrary cocycle, the
comparison `Ȟ²(X; C(-,ℤ)) ≅ H²(X; ℤ)`, and `c₁ = e = χ` (Poincaré–Hopf) are
still open: see `docs/audits/2026-10-12-t3-d1-chern.md` and bean `qou-bvxd`.
-/

-- Ref: [manuscript] lifting-and-descent, thm:qu-to-qou items 2-3 (Čech c₁ as a class)

open CategoryTheory Opposite TopologicalSpace QOU.CentralExtension.CechGerbe

namespace QOU.CentralExtension

namespace Cech

/-! ### Torsion-freeness of `C(T, ℤ)` -/

/-- `C(T, ℤ)` (written multiplicatively) has no `n`-torsion, `n ≠ 0`. -/
theorem contInt_pow_injective {T : Type} [TopologicalSpace T] {n : ℕ} (hn : n ≠ 0)
    {f g : C(T, Multiplicative ℤ)} (h : f ^ n = g ^ n) : f = g := by
  apply ContinuousMap.ext
  intro x
  have hx : (f x) ^ n = (g x) ^ n := by
    have := congrArg (fun F : C(T, Multiplicative ℤ) => F x) h
    simpa using this
  apply Multiplicative.toAdd.injective
  have hx' := congrArg Multiplicative.toAdd hx
  rw [toAdd_pow, toAdd_pow, nsmul_eq_mul, nsmul_eq_mul] at hx'
  exact mul_left_cancel₀ (by exact_mod_cast hn) hx'

/-- In a commutative group, if `c = D · tⁿ` on four faces and both `c` and `D`
satisfy the 2-cocycle identity, then so does `tⁿ`. -/
theorem core_pow_cocycle {G : Type*} [CommGroup G] (n : ℕ)
    (c₁ c₂ c₃ c₄ D₁ D₂ D₃ D₄ t₁ t₂ t₃ t₄ : G)
    (h₁ : c₁ = D₁ * t₁ ^ n) (h₂ : c₂ = D₂ * t₂ ^ n) (h₃ : c₃ = D₃ * t₃ ^ n)
    (h₄ : c₄ = D₄ * t₄ ^ n) (hc : c₁ * c₂ = c₃ * c₄) (hD : D₁ * D₂ = D₃ * D₄) :
    (t₁ * t₂) ^ n = (t₃ * t₄) ^ n := by
  have e₁ : t₁ ^ n = D₁⁻¹ * c₁ := by rw [h₁]; group
  have e₂ : t₂ ^ n = D₂⁻¹ * c₂ := by rw [h₂]; group
  have e₃ : t₃ ^ n = D₃⁻¹ * c₃ := by rw [h₃]; group
  have e₄ : t₄ ^ n = D₄⁻¹ * c₄ := by rw [h₄]; group
  rw [mul_pow, mul_pow, e₁, e₂, e₃, e₄]
  calc D₁⁻¹ * c₁ * (D₂⁻¹ * c₂) = (D₁ * D₂)⁻¹ * (c₁ * c₂) := by
        rw [mul_inv]; ac_rfl
    _ = (D₃ * D₄)⁻¹ * (c₃ * c₄) := by rw [hc, hD]
    _ = D₃⁻¹ * c₃ * (D₄⁻¹ * c₄) := by rw [mul_inv]; ac_rfl

/-- The coboundary of a 1-cochain is a 2-cocycle, in a commutative group. -/
theorem core_coboundary_cocycle {G : Type*} [CommGroup G]
    (bij bjk bik bkl bil bjl : G) :
    (bij * bjk * bik⁻¹) * (bik * bkl * bil⁻¹) =
      (bjk * bkl * bjl⁻¹) * (bij * bjl * bil⁻¹) := by
  calc (bij * bjk * bik⁻¹) * (bik * bkl * bil⁻¹)
      = bij * bjk * bkl * bil⁻¹ * (bik⁻¹ * bik) := by ac_rfl
    _ = bij * bjk * bkl * bil⁻¹ * (bjl * bjl⁻¹) := by simp
    _ = (bjk * bkl * bjl⁻¹) * (bij * bjl * bil⁻¹) := by ac_rfl

variable {X : Type} [TopologicalSpace X] {I : Type} {U : I → Opens X}
variable (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
  (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
  (hξ : IsRealLift γ ξ)

/-! ### The class on one cover -/

/-- `c₁` packaged as a Čech 2-cocycle of `C(-,ℤ)`. -/
noncomputable def chernCocycle : TwoCocycle U (contPresheaf X (Multiplicative ℤ)) where
  toTwoCochain := chernClass γ ξ hξ
  cocycle := chernClass_cocycle γ ξ hξ

/-- **The first Chern class in `H²(U; C(-,ℤ))`.** -/
noncomputable def chernH2 : H2 U (contPresheaf X (Multiplicative ℤ)) :=
  (chernCocycle γ ξ hξ).class

/-- The class does not depend on the local real lift. -/
theorem chernH2_indep_lift
    (ξ' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ' : IsRealLift γ ξ') :
    chernH2 γ ξ' hξ' = chernH2 γ ξ hξ := by
  obtain ⟨t, ht⟩ := chernClass_lift_change γ ξ hξ ξ' hξ'
  exact (Quot.sound ⟨t, ht⟩ : (chernCocycle γ ξ hξ).class = (chernCocycle γ ξ' hξ').class).symm

/-- **`[c₁] = 1` iff `γ` has a global real logarithm**: `γ = exp(iη)` for a real
1-**cocycle** `η` on the cover. -/
theorem chernH2_eq_one_iff :
    chernH2 γ ξ hξ = 1 ↔
      ∃ η : PresheafOfGroups.OneCocycle (contPresheaf X (Multiplicative ℝ)) U,
        IsRealLift γ η.toOneCochain := by
  rw [exists_realCocycle_iff γ ξ hξ]
  exact TwoCocycle.class_eq_one_iff contPresheaf_comm _

/-- **Additivity of `[c₁]`**: for any real lift `ζ` of `γγ'`, the Chern cocycle
of `γγ'` is cohomologous to the product of the Chern cocycles. -/
theorem chernH2_mul (γ' : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
    (ξ' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ' : IsRealLift γ' ξ')
    (ζ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hζ : IsRealLift (mulOneCocycle (contPresheaf_comm) γ γ') ζ) :
    ∃ t : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U,
      ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
        (chernCocycle _ ζ hζ).ev i j k a b c =
          (chernCocycle γ ξ hξ).ev i j k a b c * (chernCocycle γ' ξ' hξ').ev i j k a b c *
            (t.ev i j a b * t.ev j k b c * (t.ev i k a c)⁻¹) :=
  chernClass_mul_lift γ ξ hξ γ' ξ' hξ' ζ hζ

/-! ### Gauge invariance -/

section Conj

variable (s : ∀ i, (contPresheaf X (Multiplicative ℝ)).obj (op (U i)))

/-- The real lift conjugated by a real 0-cochain: `ξ'ᵢⱼ = sᵢ + ξᵢⱼ − sⱼ`. -/
def conjLift : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U where
  ev i j T a b := (contPresheaf X (Multiplicative ℝ)).map a.op (s i) * ξ.ev i j a b *
    ((contPresheaf X (Multiplicative ℝ)).map b.op (s j))⁻¹
  ev_precomp i j T T' φ a b := by
    simp only [map_mul, map_inv, PresheafOfGroups.OneCochain.ev_precomp]
    rw [← ConcreteCategory.comp_apply, ← ConcreteCategory.comp_apply,
      ← Functor.map_comp, ← Functor.map_comp]
    rfl

variable (γ' : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U)
  (hγ' : ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j),
    γ'.ev i j a b = (expExtension X).π.app (op T)
        ((contPresheaf X (Multiplicative ℝ)).map a.op (s i)) * γ.ev i j a b *
      ((expExtension X).π.app (op T) ((contPresheaf X (Multiplicative ℝ)).map b.op (s j)))⁻¹)

include hγ' hξ in
/-- The conjugated lift is a real lift of the conjugated cocycle. -/
theorem isRealLift_conjLift : IsRealLift γ' (conjLift ξ s) := by
  intro i j T a b
  simp only [conjLift, map_mul, map_inv, hξ i j a b, hγ' i j a b]

include hγ' in
/-- **Gauge invariance of `c₁` at cochain level.** Conjugating `γ` by
`h = exp(i s)` and its lift by `s` leaves the Chern 2-cochain unchanged. -/
theorem chernClass_conj :
    chernClass γ' (conjLift ξ s) (isRealLift_conjLift γ ξ hξ s γ' hγ') =
      chernClass γ ξ hξ := by
  ext i j k T a b c
  apply (expExtension X).injective (op T)
  have e1 := (expExtension X).obstruction_spec γ' (conjLift ξ s)
    (isRealLift_conjLift γ ξ hξ s γ' hγ') i j k a b c
  have e2 := (expExtension X).obstruction_spec γ ξ hξ i j k a b c
  rw [← mul_inv_eq_iff_eq_mul] at e1 e2
  change _ = (expExtension X).ι.app (op T) ((expExtension X).obstruction γ' (conjLift ξ s)
    (isRealLift_conjLift γ ξ hξ s γ' hγ') |>.ev i j k a b c) at e1
  change (expExtension X).ι.app (op T) ((expExtension X).obstruction γ' (conjLift ξ s)
    (isRealLift_conjLift γ ξ hξ s γ' hγ') |>.ev i j k a b c) =
    (expExtension X).ι.app (op T) ((expExtension X).obstruction γ ξ hξ |>.ev i j k a b c)
  rw [← e1, ← e2]
  letI : CommGroup ((contPresheaf X (Multiplicative ℝ)).obj (op T)) :=
    { (inferInstance : Group _) with mul_comm := contPresheaf_comm _ }
  simp only [conjLift]
  set Si := (contPresheaf X (Multiplicative ℝ)).map a.op (s i)
  set Sj := (contPresheaf X (Multiplicative ℝ)).map b.op (s j)
  set Sk := (contPresheaf X (Multiplicative ℝ)).map c.op (s k)
  calc Si * ξ.ev i j a b * Sj⁻¹ * (Sj * ξ.ev j k b c * Sk⁻¹) * (Si * ξ.ev i k a c * Sk⁻¹)⁻¹
      = ξ.ev i j a b * ξ.ev j k b c * (ξ.ev i k a c)⁻¹ * ((Si * Si⁻¹) * (Sj * Sj⁻¹) * (Sk * Sk⁻¹)) := by
        rw [mul_inv, mul_inv, inv_inv]; ac_rfl
    _ = ξ.ev i j a b * ξ.ev j k b c * (ξ.ev i k a c)⁻¹ := by simp

include hγ' in
/-- **Gauge invariance of `[c₁]`**: cohomologous `U(1)`-cocycles, related by a
0-cochain with a real lift, have the same Chern class in `H²`. -/
theorem chernH2_conj (ξ'' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
    (hξ'' : IsRealLift γ' ξ'') :
    chernH2 γ' ξ'' hξ'' = chernH2 γ ξ hξ := by
  rw [chernH2_indep_lift γ' (conjLift ξ s) (isRealLift_conjLift γ ξ hξ s γ' hγ') ξ'' hξ'']
  refine Quot.sound ⟨1, fun i j k T a b d => ?_⟩
  change (chernClass γ ξ hξ).ev i j k a b d =
    (chernClass γ' (conjLift ξ s) (isRealLift_conjLift γ ξ hξ s γ' hγ')).ev i j k a b d * _
  rw [chernClass_conj γ ξ hξ s γ' hγ']
  simp

end Conj

/-! ### Kummer with a closed quotient -/

section Kummer

variable (n : ℕ) [NeZero n]

/-- **Kummer criterion, cocycle form.** `γ` has an `n`-th root iff
`c₁ = δβ · θⁿ` with `θ` an integer 2-**cocycle**: the class `[c₁]` is `n` times
a class on the cover. -/
theorem exists_nthRoot_iff_cocycle :
    (∃ η : PresheafOfGroups.OneCocycle (contPresheaf X Circle) U,
      ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j),
        η.ev i j a b ^ n = γ.ev i j a b) ↔
    ∃ (β : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℤ)) U)
      (θ : TwoCocycle U (contPresheaf X (Multiplicative ℤ))),
      ∀ (i j k : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (c : T ⟶ U k),
        (chernClass γ ξ hξ).ev i j k a b c =
          β.ev i j a b * β.ev j k b c * (β.ev i k a c)⁻¹ * θ.ev i j k a b c ^ n := by
  rw [exists_nthRoot_iff n γ ξ hξ]
  constructor
  · rintro ⟨β, θ, hθ⟩
    refine ⟨β, { toTwoCochain := θ, cocycle := ?_ }, hθ⟩
    intro i j k l T a b c d
    letI : CommGroup ((contPresheaf X (Multiplicative ℤ)).obj (op T)) :=
      { (inferInstance : Group _) with mul_comm := contPresheaf_comm _ }
    apply contInt_pow_injective (NeZero.ne n)
    exact core_pow_cocycle n _ _ _ _ _ _ _ _ _ _ _ _
      (hθ i j k a b c) (hθ i k l a c d) (hθ j k l b c d) (hθ i j l a b d)
      (chernClass_cocycle γ ξ hξ i j k l a b c d)
      (core_coboundary_cocycle _ _ _ _ _ _)
  · rintro ⟨β, θ, hθ⟩
    exact ⟨β, θ.toTwoCochain, hθ⟩

end Kummer

/-! ### The colimit over open covers -/

section Colimit

variable (X) in
/-- A cover of `X` by opens: a `Cover` of `⊤ : Opens X` whose members cover
every point. -/
def IsOpenCover (𝒰 : Cover.{0} (⊤ : Opens X)) : Prop :=
  ∀ x : X, ∃ i, x ∈ 𝒰.obj i

/-- The common refinement `{Vᵢ ∩ Wⱼ}` of two families of opens of `X`. -/
def Cover.inter (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) : Cover.{0} (⊤ : Opens X) where
  ι := 𝒱.ι × 𝒲.ι
  obj p := 𝒱.obj p.1 ⊓ 𝒲.obj p.2
  arr _ := homOfLE le_top

/-- `{Vᵢ ∩ Wⱼ}` refines `𝒱`. -/
def Cover.interLeft (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) : (Cover.inter 𝒱 𝒲).Refines 𝒱 where
  r := Prod.fst
  f _ := homOfLE inf_le_left
  w _ := Subsingleton.elim _ _

/-- `{Vᵢ ∩ Wⱼ}` refines `𝒲`. -/
def Cover.interRight (𝒱 𝒲 : Cover.{0} (⊤ : Opens X)) : (Cover.inter 𝒱 𝒲).Refines 𝒲 where
  r := Prod.snd
  f _ := homOfLE inf_le_right
  w _ := Subsingleton.elim _ _

theorem isOpenCover_inter {𝒱 𝒲 : Cover.{0} (⊤ : Opens X)} (h𝒱 : IsOpenCover X 𝒱)
    (h𝒲 : IsOpenCover X 𝒲) : IsOpenCover X (Cover.inter 𝒱 𝒲) := fun x => by
  obtain ⟨i, hi⟩ := h𝒱 x
  obtain ⟨j, hj⟩ := h𝒲 x
  exact ⟨(i, j), ⟨hi, hj⟩⟩

/-- **Open covers are directed** under refinement, by pairwise intersection. -/
theorem isCoverDirected_open : IsCoverDirected (IsOpenCover X) :=
  fun 𝒱 𝒲 h𝒱 h𝒲 => ⟨Cover.inter 𝒱 𝒲, isOpenCover_inter h𝒱 h𝒲,
    ⟨Cover.interLeft 𝒱 𝒲⟩, ⟨Cover.interRight 𝒱 𝒲⟩⟩

variable (𝒰 : Cover.{0} (⊤ : Opens X)) (h𝒰 : IsOpenCover X 𝒰)
  (γ : PresheafOfGroups.OneCocycle (contPresheaf X Circle) 𝒰.obj)
  (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒰.obj)
  (hξ : IsRealLift γ ξ)

/-- **The first Chern class in `Ȟ²(X; C(-,ℤ))`**, the colimit over open covers. -/
noncomputable def cechChern : CechH2 (contPresheaf X (Multiplicative ℤ)) (IsOpenCover X) :=
  (expExtension X).cechObstruction 𝒰 h𝒰 γ ξ hξ

/-- It is the image of `chernH2` under `H2 → Ȟ²`. -/
theorem cechChern_eq_toCech : cechChern 𝒰 h𝒰 γ ξ hξ = H2.toCech 𝒰 h𝒰 (chernH2 γ ξ hξ) := rfl

/-- It does not depend on the local real lift. -/
theorem cechChern_indep_lift
    (ξ' : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒰.obj)
    (hξ' : IsRealLift γ ξ') :
    cechChern 𝒰 h𝒰 γ ξ hξ = cechChern 𝒰 h𝒰 γ ξ' hξ' :=
  (expExtension X).cechObstruction_indep_lift 𝒰 h𝒰 γ ξ hξ ξ' hξ'

/-- **Cover independence**: pulling back to an open refinement gives the same class. -/
theorem cechChern_pull (𝒱 : Cover.{0} (⊤ : Opens X)) (h𝒱 : IsOpenCover X 𝒱)
    (ρ : 𝒱.Refines 𝒰) :
    cechChern 𝒱 h𝒱 (pullOneCocycle 𝒰.obj ρ.r ρ.f γ) (pullOneCochain 𝒰.obj ρ.r ρ.f ξ)
        (fun j j' _ a b => hξ (ρ.r j) (ρ.r j') (a ≫ ρ.f j) (b ≫ ρ.f j')) =
      cechChern 𝒰 h𝒰 γ ξ hξ :=
  (expExtension X).cechObstruction_pull 𝒰 h𝒰 γ ξ hξ 𝒱 h𝒱 ρ

/-- **`c₁ = 0` in `Ȟ²` iff `γ` has a real logarithm after refinement**: on some
open refinement, `γ = exp(iη)` for a real 1-cocycle `η`. -/
theorem cechChern_eq_one_iff :
    cechChern 𝒰 h𝒰 γ ξ hξ = cechClass 𝒰 h𝒰 TwoCocycle.one ↔
      ∃ (𝒲 : Cover.{0} (⊤ : Opens X)) (_ : IsOpenCover X 𝒲) (ρ : 𝒲.Refines 𝒰)
        (η : PresheafOfGroups.OneCocycle (contPresheaf X (Multiplicative ℝ)) 𝒲.obj),
        IsRealLift (pullOneCocycle 𝒰.obj ρ.r ρ.f γ) η.toOneCochain :=
  (expExtension X).cechObstruction_eq_one_iff isCoverDirected_open 𝒰 h𝒰 γ ξ hξ

end Colimit

end Cech

end QOU.CentralExtension
