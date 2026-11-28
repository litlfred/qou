import MathlibExt.CechChernClassH2
import QOU.Transcendental.MathlibExt.CechRealLiftRefinement

/-!
# The Čech first Chern class does not depend on the refinement

Bean `qou-bvxd`. `CechRealLiftRefinement` shows that on a paracompact Hausdorff
space every `U(1)`-cocycle `γ` on an open cover `𝒰` has a local real lift on
some open refinement, so `cechChern` (`MathlibExt.CechChernClassH2`) is defined
there. This file shows that the resulting class in `Ȟ²(X; C(-,ℤ))` does not
depend on which refinement and which lift were chosen. So `c₁` is a
well-defined invariant of `γ`.

## The argument

Take two open refinements `𝒱₁, 𝒱₂` of `𝒰` with real lifts `ξ₁, ξ₂` of the
pulled-back cocycles.

1. Pass to the common refinement `𝒲 = {V¹ ∩ V²}` (`cechChern_pull`). There the
   two pullbacks are `γ_{R₁p R₁q}` and `γ_{R₂p R₂q}` for two index maps `R₁, R₂`.
2. **Gauge relation** (`pull_gauge`): `γ_{R₂p R₂q} = h_p · γ_{R₁p R₁q} · h_q⁻¹`
   with `h_p = γ_{R₂p R₁p}`. This is the cocycle identity, used twice.
3. **Local logarithms of `h`** (`exists_refinement_gaugeLift`): each `h_p` is
   within `1/2` of its value at `x` on a neighbourhood of `x`, and so has a
   continuous real logarithm `s` there. Refine to these neighbourhoods. This
   step needs no paracompactness: a 0-cochain has no overlaps to control.
4. Gauge invariance (`chernH2_conj`) gives equal classes on that refinement.

## Results

* `cechChern_indep_refinement`: any space, any open cover `𝒰`, and any two open
  refinements with real lifts give the same class in `Ȟ²`.
* `exists_unique_cechChern`: on a paracompact Hausdorff space, every
  `U(1)`-cocycle `γ` on an open cover has a class `c ∈ Ȟ²` that **every**
  open refinement with a real lift computes.

Sorry-free. It uses continuity and the norm on `ℂ`, hence the location under
`QOU/Transcendental/`.
-/

-- Ref: [manuscript] lifting-and-descent, thm:qu-to-qou item 2 (c₁ well defined on Ȟ¹)

open CategoryTheory Opposite TopologicalSpace Filter Topology QOU.CentralExtension.CechGerbe

namespace QOU.CentralExtension

namespace Cech

variable {X : Type} [TopologicalSpace X]

/-! ### Step 2: the gauge relation between two pullbacks -/

section Gauge

variable {I K : Type} {U : I → Opens X} {W : K → Opens X}
  (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)
  (R₁ R₂ : K → I) (f₁ : ∀ p, W p ⟶ U (R₁ p)) (f₂ : ∀ p, W p ⟶ U (R₂ p))

/-- The gauge 0-cochain `h_p = γ_{R₂p R₁p}` on `W p`. -/
def gauge (p : K) : (contPresheaf X _root_.Circle).obj (op (W p)) :=
  γ.ev (R₂ p) (R₁ p) (f₂ p) (f₁ p)

/-- **The two pullbacks are gauge equivalent**:
`γ_{R₂p R₂q} = h_p · γ_{R₁p R₁q} · h_q⁻¹`. -/
theorem pull_gauge (p q : K) {T : Opens X} (a : T ⟶ W p) (b : T ⟶ W q) :
    (pullOneCocycle U R₂ f₂ γ).ev p q a b =
      (contPresheaf X _root_.Circle).map a.op (gauge γ R₁ R₂ f₁ f₂ p) *
        (pullOneCocycle U R₁ f₁ γ).ev p q a b *
        ((contPresheaf X _root_.Circle).map b.op (gauge γ R₁ R₂ f₁ f₂ q))⁻¹ := by
  simp only [gauge, PresheafOfGroups.OneCochain.ev_precomp]
  change γ.ev (R₂ p) (R₂ q) (a ≫ f₂ p) (b ≫ f₂ q) =
    γ.ev (R₂ p) (R₁ p) (a ≫ f₂ p) (a ≫ f₁ p) * γ.ev (R₁ p) (R₁ q) (a ≫ f₁ p) (b ≫ f₁ q) *
      (γ.ev (R₂ q) (R₁ q) (b ≫ f₂ q) (b ≫ f₁ q))⁻¹
  rw [← γ.ev_symm, γ.ev_trans, γ.ev_trans]

end Gauge

/-! ### Step 3: local logarithms of a 0-cochain after refinement -/

/-- If `F` is within `1/2` of `c` on the circle, then `F ≠ −c`. -/
theorem circle_ne_neg (F c : _root_.Circle) (hF : ‖(F : ℂ) - c‖ < 1 / 2) :
    F ≠ _root_.Circle.exp Real.pi * c := by
  have := circle_mul_ne_neg F 1 c 1 hF (by simp)
  simpa using this

theorem expπ_logSection {T : Opens X} (w : _root_.Circle)
    (f : (contPresheaf X _root_.Circle).obj (op T)) (hf : ∀ x, sec f x ≠ w) :
    (expExtension X).π.app (op T) (logSection w f hf) = f := by
  apply ContinuousMap.ext
  intro x
  change _root_.Circle.exp (Multiplicative.toAdd (Multiplicative.ofAdd
    (Circle.localLog w (sec f x)))) = sec f x
  rw [toAdd_ofAdd]
  exact Circle.exp_localLog _ _

/-- **Real logarithms of a 0-cochain after refinement.** For any family of
opens `W` covering `X` and any `U(1)`-valued 0-cochain `h`, there is an open
refinement `x ↦ Nₓ ∋ x` on which every `h` has a continuous real logarithm. -/
theorem exists_refinement_gaugeLift {K : Type} {W : K → Opens X} (hW : ∀ x, ∃ p, x ∈ W p)
    (h : ∀ p, (contPresheaf X _root_.Circle).obj (op (W p))) :
    ∃ (N : X → Opens X) (P : X → K) (g : ∀ x, N x ⟶ W (P x))
      (s : ∀ x, (contPresheaf X (Multiplicative ℝ)).obj (op (N x))),
      (∀ x, x ∈ N x) ∧
        ∀ x, (expExtension X).π.app (op (N x)) (s x) =
          (contPresheaf X _root_.Circle).map (g x).op (h (P x)) := by
  choose P hP using hW
  have hO : ∀ x, ∃ t : Set X, t ⊆ {z | ∃ hz : z ∈ W (P x),
      ‖(sec (h (P x)) ⟨z, hz⟩ : ℂ) - sec (h (P x)) ⟨x, hP x⟩‖ < 1 / 2} ∧ IsOpen t ∧ x ∈ t :=
    fun x => mem_nhds_iff.1 (nhds_close (W (P x)) (sec (h (P x))) ⟨x, hP x⟩)
  choose t ht hto hxt using hO
  let N : X → Opens X := fun x => ⟨t x, hto x⟩
  let g : ∀ x, N x ⟶ W (P x) := fun x => homOfLE fun z hz => (ht x hz).1
  have hf : ∀ x (z : N x),
      sec ((contPresheaf X _root_.Circle).map (g x).op (h (P x))) z ≠
        _root_.Circle.exp Real.pi * sec (h (P x)) ⟨x, hP x⟩ := by
    intro x z
    obtain ⟨_, hz⟩ := ht x z.2
    exact circle_ne_neg _ _ hz
  exact ⟨N, P, g, fun x => logSection _ _ (hf x), hxt, fun x => expπ_logSection _ _ _⟩

/-! ### Step 4: assembly -/

section Indep

variable (𝒰 : Cover.{0} (⊤ : Opens X))
  (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) 𝒰.obj)

/-- **`c₁` does not depend on the refinement.** Two open refinements of `𝒰`,
each with a local real lift of the pulled-back cocycle, give the same class in
`Ȟ²(X; C(-,ℤ))`. -/
theorem cechChern_indep_refinement
    (𝒱₁ : Cover.{0} (⊤ : Opens X)) (h₁ : IsOpenCover X 𝒱₁) (ρ₁ : 𝒱₁.Refines 𝒰)
    (ξ₁ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒱₁.obj)
    (hξ₁ : IsRealLift (pullOneCocycle 𝒰.obj ρ₁.r ρ₁.f γ) ξ₁)
    (𝒱₂ : Cover.{0} (⊤ : Opens X)) (h₂ : IsOpenCover X 𝒱₂) (ρ₂ : 𝒱₂.Refines 𝒰)
    (ξ₂ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒱₂.obj)
    (hξ₂ : IsRealLift (pullOneCocycle 𝒰.obj ρ₂.r ρ₂.f γ) ξ₂) :
    cechChern 𝒱₁ h₁ _ ξ₁ hξ₁ = cechChern 𝒱₂ h₂ _ ξ₂ hξ₂ := by
  -- Step 1: the common refinement.
  let 𝒲 := Cover.inter 𝒱₁ 𝒱₂
  have h𝒲 : IsOpenCover X 𝒲 := isOpenCover_inter h₁ h₂
  let σ₁ := Cover.interLeft 𝒱₁ 𝒱₂
  let σ₂ := Cover.interRight 𝒱₁ 𝒱₂
  rw [← cechChern_pull 𝒱₁ h₁ _ ξ₁ hξ₁ 𝒲 h𝒲 σ₁, ← cechChern_pull 𝒱₂ h₂ _ ξ₂ hξ₂ 𝒲 h𝒲 σ₂]
  -- Step 3: refine so that the gauge has real logarithms.
  let R₁ : 𝒲.ι → 𝒰.ι := fun p => ρ₁.r (σ₁.r p)
  let R₂ : 𝒲.ι → 𝒰.ι := fun p => ρ₂.r (σ₂.r p)
  let F₁ : ∀ p, 𝒲.obj p ⟶ 𝒰.obj (R₁ p) := fun p => σ₁.f p ≫ ρ₁.f (σ₁.r p)
  let F₂ : ∀ p, 𝒲.obj p ⟶ 𝒰.obj (R₂ p) := fun p => σ₂.f p ≫ ρ₂.f (σ₂.r p)
  obtain ⟨N, P, g, s, hN, hs⟩ :=
    exists_refinement_gaugeLift (W := 𝒲.obj) h𝒲 (gauge γ R₁ R₂ F₁ F₂)
  let 𝒩 : Cover.{0} (⊤ : Opens X) := ⟨X, N, fun _ => homOfLE le_top⟩
  have h𝒩 : IsOpenCover X 𝒩 := fun x => ⟨x, hN x⟩
  let τ : 𝒩.Refines 𝒲 := ⟨P, g, fun _ => Subsingleton.elim _ _⟩
  rw [← cechChern_pull 𝒲 h𝒲 _ _ _ 𝒩 h𝒩 τ, ← cechChern_pull 𝒲 h𝒲 _ _ _ 𝒩 h𝒩 τ]
  -- Step 4: gauge invariance on `𝒩`.
  rw [cechChern_eq_toCech, cechChern_eq_toCech]
  refine congrArg (H2.toCech 𝒩 h𝒩) (chernH2_conj _ _ _ s _ ?_ _ _).symm
  intro x y T a b
  rw [NatTrans.naturality_apply, NatTrans.naturality_apply, hs x, hs y,
    ← ConcreteCategory.comp_apply, ← ConcreteCategory.comp_apply, ← Functor.map_comp,
    ← Functor.map_comp, ← op_comp, ← op_comp]
  exact pull_gauge γ R₁ R₂ F₁ F₂ (P x) (P y) (a ≫ g x) (b ≫ g y)

end Indep

/-! ### `c₁` of every cocycle, on a paracompact Hausdorff space -/

/-- **`c₁` is a well-defined invariant of every `U(1)`-cocycle.** On a
paracompact Hausdorff space, for a `U(1)`-cocycle `γ` on an open cover `𝒰`
there is a class `c ∈ Ȟ²(X; C(-,ℤ))` computed by **every** open refinement
carrying a real lift, and at least one such refinement exists. -/
theorem exists_unique_cechChern [ParacompactSpace X] [T2Space X]
    (𝒰 : Cover.{0} (⊤ : Opens X)) (h𝒰 : IsOpenCover X 𝒰)
    (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) 𝒰.obj) :
    ∃ c : CechH2 (contPresheaf X (Multiplicative ℤ)) (IsOpenCover X),
      (∃ (𝒱 : Cover.{0} (⊤ : Opens X)) (_ : IsOpenCover X 𝒱) (ρ : 𝒱.Refines 𝒰)
        (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒱.obj),
          IsRealLift (pullOneCocycle 𝒰.obj ρ.r ρ.f γ) ξ) ∧
      ∀ (𝒱 : Cover.{0} (⊤ : Opens X)) (h𝒱 : IsOpenCover X 𝒱) (ρ : 𝒱.Refines 𝒰)
        (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) 𝒱.obj)
        (hξ : IsRealLift (pullOneCocycle 𝒰.obj ρ.r ρ.f γ) ξ),
        cechChern 𝒱 h𝒱 _ ξ hξ = c := by
  obtain ⟨V, r, f, hV, ξ, hξ⟩ := exists_refinement_isRealLift h𝒰 γ
  let 𝒱 : Cover.{0} (⊤ : Opens X) := ⟨X, V, fun _ => homOfLE le_top⟩
  have h𝒱 : IsOpenCover X 𝒱 := fun x => ⟨x, hV x⟩
  let ρ : 𝒱.Refines 𝒰 := ⟨r, f, fun _ => Subsingleton.elim _ _⟩
  refine ⟨cechChern 𝒱 h𝒱 _ ξ hξ, ⟨𝒱, h𝒱, ρ, ξ, hξ⟩, ?_⟩
  intro 𝒱' h𝒱' ρ' ξ' hξ'
  exact cechChern_indep_refinement 𝒰 γ 𝒱' h𝒱' ρ' ξ' hξ' 𝒱 h𝒱 ρ ξ hξ

end Cech

end QOU.CentralExtension
