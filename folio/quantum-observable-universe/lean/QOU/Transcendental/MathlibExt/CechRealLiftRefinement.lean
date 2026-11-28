import QOU.Transcendental.MathlibExt.CechLocalLog
import Mathlib.Topology.Compactness.Paracompact
import Mathlib.Topology.ShrinkingLemma

/-!
# Local real lifts after refinement, on paracompact Hausdorff spaces

Bean `qou-bvxd`, open item 4(a′). `MathlibExt.CechChernClass` defines the Čech
first Chern class `c₁(γ)` of a `U(1)`-valued 1-cocycle `γ` relative to a local
real lift `ξ` (`IsRealLift γ ξ`, `exp(iξ) = γ`), which it takes as a
hypothesis. `CechLocalLog` produces such a lift when every transition function
misses a point of the circle (`AvoidsPoints`). This file proves that, on a
paracompact Hausdorff space, **every** `U(1)`-cocycle on an open cover avoids
points, hence has a local real lift, after passing to a finer open cover.
So `c₁` is defined for every `U(1)`-cocycle once the cover is refined.

## The argument

This is the standard argument (Godement, *Topologie algébrique et théorie des
faisceaux*, II.5.10; Serre, FAC §20), reconstructed here. Neither source is
held in `library/`.

1. Take a locally finite precise refinement `vᵢ ⊆ Uᵢ` (`precise_refinement`)
   and shrink it (`exists_iUnion_eq_closure_subset`, using normality) to a
   locally finite cover by closed sets `Fᵢ ⊆ Uᵢ`.
2. For each point `x`, let `S(x) = {i | x ∈ Fᵢ}` (finite). Choose an open
   `Wₓ ∋ x` with (a) `Wₓ ⊆ Uᵢ` for `i ∈ S(x)`; (b) `Wₓ ∩ Fⱼ = ∅` for `j ∉ S(x)`;
   (c) `|γᵢⱼ − γᵢⱼ(x)| < 1/2` on `Wₓ` for `i, j ∈ S(x)`. Each condition is one
   of finitely many neighbourhood conditions at `x`.
3. Refine by `x ↦ Wₓ`, with `τ(x) ∈ S(x)`. If `z ∈ Wₓ ∩ W_y`, pick `k` with
   `z ∈ F_k`. By (b), `k ∈ S(x) ∩ S(y)`, so by (a) both `Wₓ, W_y ⊆ U_k`. On
   `Wₓ ∩ W_y` the cocycle gives `γ_{τx τy} = γ_{τx k} · γ_{k τy}`, and by (c)
   each factor is within `1/2` of a constant `c`, `d`. Therefore the product is
   within `1` of `cd` and never equals `−cd`.

## Results

* `exists_refinement_avoidsPoints`: the refinement and the avoided points.
* `exists_refinement_isRealLift`: on a paracompact Hausdorff space, every
  `U(1)`-cocycle on an open cover admits an open refinement `x ↦ Wₓ ∋ x` on
  which it has a local real lift. Consequently `chernClass` (and its class
  `cechChern` in `Ȟ²`) is defined on the refinement with no lift hypothesis.

Sorry-free. The only analytic input is continuity and the norm on `ℂ`; this
is why the file lives under `QOU/Transcendental/`. No number enters except the
radius `1/2`, a choice that does not affect the resulting class (the class is
lift- and cover-independent, `MathlibExt.CechChernClassH2`).
-/

-- Ref: Godement, Topologie algébrique et théorie des faisceaux (1958), II.5.10;
--      Serre, Faisceaux algébriques cohérents (1955), §20. Neither is held in library/.

open CategoryTheory Opposite TopologicalSpace Filter Topology Set

namespace QOU.CentralExtension

namespace Cech

/-! ### Two elementary facts -/

/-- If `F, G ∈ U(1)` are within `1/2` of `c, d ∈ U(1)`, then `FG ≠ −cd`. -/
theorem circle_mul_ne_neg (F G c d : _root_.Circle) (hF : ‖(F : ℂ) - c‖ < 1 / 2)
    (hG : ‖(G : ℂ) - d‖ < 1 / 2) :
    F * G ≠ _root_.Circle.exp Real.pi * (c * d) := by
  intro h
  have h' : ((F * G : _root_.Circle) : ℂ) = -((c : ℂ) * d) := by
    rw [h, _root_.Circle.coe_mul, _root_.Circle.coe_exp, Complex.exp_pi_mul_I]
    push_cast; ring
  have e : (F : ℂ) * G - c * d = F * (G - d) + (F - c) * d := by ring
  have hle : ‖(F : ℂ) * G - c * d‖ < 1 := by
    rw [e]
    calc ‖(F : ℂ) * (G - d) + (F - c) * d‖
        ≤ ‖(F : ℂ) * (G - d)‖ + ‖((F : ℂ) - c) * d‖ := norm_add_le _ _
      _ = ‖(G : ℂ) - d‖ + ‖(F : ℂ) - c‖ := by
          rw [norm_mul, norm_mul, _root_.Circle.norm_coe, _root_.Circle.norm_coe, one_mul,
            mul_one]
      _ < 1 / 2 + 1 / 2 := add_lt_add hG hF
      _ = 1 := by norm_num
  rw [← _root_.Circle.coe_mul, h', show -((c : ℂ) * d) - c * d = -2 * (c * d) by ring,
    norm_mul, norm_mul, _root_.Circle.norm_coe, _root_.Circle.norm_coe] at hle
  norm_num at hle

/-- For a continuous map `g` on an open set `O`, the points of `O` where `g` is
within `1/2` of `g p` form a neighbourhood of `p` in `X`. -/
theorem nhds_close {X : Type} [TopologicalSpace X] (O : Opens X) (g : C(O, _root_.Circle))
    (p : O) :
    {z : X | ∃ hz : z ∈ O, ‖(g ⟨z, hz⟩ : ℂ) - g p‖ < 1 / 2} ∈ 𝓝 (p : X) := by
  have ho : IsOpen (Subtype.val '' (g ⁻¹' {u : _root_.Circle | ‖(u : ℂ) - g p‖ < 1 / 2})) := by
    refine O.isOpen.isOpenMap_subtype_val _ (IsOpen.preimage g.continuous ?_)
    exact isOpen_lt ((continuous_subtype_val.sub continuous_const).norm) continuous_const
  refine Filter.mem_of_superset (ho.mem_nhds ⟨p, by simp, rfl⟩) ?_
  rintro z ⟨q, hq, rfl⟩
  exact ⟨q.2, hq⟩

variable {X : Type} [TopologicalSpace X] {I : Type} {U : I → Opens X}

/-- The transition function `γᵢⱼ` on the whole overlap `Uᵢ ⊓ Uⱼ`. -/
noncomputable def overlapFn (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)
    (i j : I) : C((U i ⊓ U j : Opens X), _root_.Circle) :=
  sec (γ.ev i j (homOfLE inf_le_left) (homOfLE inf_le_right))

/-- Every restriction of `γᵢⱼ` is a restriction of `overlapFn γ i j`. -/
theorem sec_ev_eq_overlapFn (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)
    (i j : I) {T : Opens X} (a : T ⟶ U i) (b : T ⟶ U j) (t : T) :
    sec (γ.ev i j a b) t = overlapFn γ i j ⟨t.1, a.le t.2, b.le t.2⟩ := by
  have hT : T ≤ U i ⊓ U j := le_inf a.le b.le
  have e := γ.ev_precomp i j (homOfLE hT) (homOfLE inf_le_left) (homOfLE inf_le_right)
  have ha : a = homOfLE hT ≫ homOfLE inf_le_left := rfl
  have hb : b = homOfLE hT ≫ homOfLE inf_le_right := rfl
  rw [ha, hb, ← e]
  rfl

/-! ### The refinement -/

section Refinement

variable [ParacompactSpace X] [T2Space X] (hU : ∀ x : X, ∃ i, x ∈ U i)
  (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)

include hU in
/-- A locally finite cover by closed sets `Fᵢ ⊆ Uᵢ`. -/
theorem exists_closed_shrinking :
    ∃ F : I → Set X, (∀ i, IsClosed (F i)) ∧ (∀ i, F i ⊆ U i) ∧ LocallyFinite F ∧
      ∀ x, ∃ i, x ∈ F i := by
  obtain ⟨v, vo, vc, vlf, vU⟩ := precise_refinement (fun i => (U i : Set X))
    (fun i => (U i).isOpen) (by
      refine eq_univ_of_forall fun x => ?_
      obtain ⟨i, hi⟩ := hU x
      exact mem_iUnion.2 ⟨i, hi⟩)
  obtain ⟨w, wc, wo, wv⟩ := exists_iUnion_eq_closure_subset vo (fun x => vlf.point_finite x) vc
  refine ⟨fun i => closure (w i), fun i => isClosed_closure, fun i => (wv i).trans (vU i),
    vlf.subset wv, fun x => ?_⟩
  have : x ∈ ⋃ i, w i := by rw [wc]; trivial
  obtain ⟨i, hi⟩ := mem_iUnion.1 this
  exact ⟨i, subset_closure hi⟩

variable {F : I → Set X} (Fc : ∀ i, IsClosed (F i)) (FU : ∀ i, F i ⊆ U i)
  (Flf : LocallyFinite F)

omit [ParacompactSpace X] [T2Space X] in
include Fc FU Flf in
/-- **Step 2.** For each point, an open neighbourhood satisfying (a), (b), (c). -/
theorem exists_good_nhd (x : X) :
    ∃ W : Set X, IsOpen W ∧ x ∈ W ∧
      (∀ i, x ∈ F i → W ⊆ U i) ∧
      (∀ j, x ∉ F j → ∀ z ∈ W, z ∉ F j) ∧
      (∀ i j (hi : x ∈ F i) (hj : x ∈ F j), ∀ z ∈ W, ∃ hz : z ∈ U i ⊓ U j,
        ‖(overlapFn γ i j ⟨z, hz⟩ : ℂ) - overlapFn γ i j ⟨x, FU i hi, FU j hj⟩‖ < 1 / 2) := by
  have hS : {i | x ∈ F i}.Finite := Flf.point_finite x
  obtain ⟨N, hN, hNfin⟩ := Flf x
  have h1 : ∀ᶠ z in 𝓝 x, ∀ i ∈ {i | x ∈ F i}, z ∈ U i :=
    (eventually_all_finite hS).2 fun i hi => (U i).isOpen.mem_nhds (FU i hi)
  have h2 : ∀ᶠ z in 𝓝 x, ∀ j ∈ {j | (F j ∩ N).Nonempty}, x ∉ F j → z ∉ F j := by
    refine (eventually_all_finite hNfin).2 fun j _ => ?_
    by_cases hj : x ∈ F j
    · exact Eventually.of_forall fun _ h => absurd hj h
    · exact Eventually.mono ((Fc j).isOpen_compl.mem_nhds hj) fun _ hz _ => hz
  have h3 : ∀ᶠ z in 𝓝 x, ∀ p ∈ {i | x ∈ F i} ×ˢ {i | x ∈ F i}, ∀ (hi : x ∈ F p.1)
      (hj : x ∈ F p.2), ∃ hz : z ∈ U p.1 ⊓ U p.2,
        ‖(overlapFn γ p.1 p.2 ⟨z, hz⟩ : ℂ) -
          overlapFn γ p.1 p.2 ⟨x, FU p.1 hi, FU p.2 hj⟩‖ < 1 / 2 := by
    refine (eventually_all_finite (hS.prod hS)).2 fun p hp => ?_
    have := nhds_close (U p.1 ⊓ U p.2) (overlapFn γ p.1 p.2) ⟨x, FU p.1 hp.1, FU p.2 hp.2⟩
    exact Eventually.mono this fun z hz _ _ => hz
  have hN' : ∀ᶠ z in 𝓝 x, z ∈ N := hN
  obtain ⟨W, hWsub, hWo, hxW⟩ := mem_nhds_iff.1 (((hN'.and h1).and h2).and h3)
  replace hWsub : ∀ z ∈ W, ((z ∈ N ∧ ∀ i ∈ {i | x ∈ F i}, z ∈ U i) ∧
      ∀ j ∈ {j | (F j ∩ N).Nonempty}, x ∉ F j → z ∉ F j) ∧
      ∀ p ∈ {i | x ∈ F i} ×ˢ {i | x ∈ F i}, ∀ (hi : x ∈ F p.1) (hj : x ∈ F p.2),
        ∃ hz : z ∈ U p.1 ⊓ U p.2, ‖(overlapFn γ p.1 p.2 ⟨z, hz⟩ : ℂ) -
          overlapFn γ p.1 p.2 ⟨x, FU p.1 hi, FU p.2 hj⟩‖ < 1 / 2 := fun z hz => hWsub hz
  refine ⟨W, hWo, hxW, fun i hi z hz => (hWsub z hz).1.1.2 i hi, fun j hj z hz hzF => ?_,
    fun i j hi hj z hz => (hWsub z hz).2 (i, j) ⟨hi, hj⟩ hi hj⟩
  exact (hWsub z hz).1.2 j ⟨z, hzF, (hWsub z hz).1.1.1⟩ hj hzF

omit [ParacompactSpace X] [T2Space X] in
include Fc FU Flf in
/-- **Step 3.** Given a locally finite closed cover `Fᵢ ⊆ Uᵢ`, the refinement
`x ↦ Wₓ` makes `γ` avoid points. -/
theorem exists_refinement_avoidsPoints_of_shrinking (hF : ∀ x, ∃ i, x ∈ F i) :
    ∃ (V : X → Opens X) (r : X → I) (f : ∀ x, V x ⟶ U (r x)) (w : X → X → _root_.Circle),
      (∀ x, x ∈ V x) ∧ AvoidsPoints (pullOneCocycle U r f γ) w := by
  choose W Wo xW Wa Wb Wc using exists_good_nhd γ Fc FU Flf
  choose τ hτ using id hF
  let V : X → Opens X := fun x => ⟨W x, Wo x⟩
  let f : ∀ x, V x ⟶ U (τ x) := fun x => homOfLE (Wa x (τ x) (hτ x))
  have key : ∀ x y, ∃ w : _root_.Circle, ∀ ⦃T : Opens X⦄ (a : T ⟶ V x) (b : T ⟶ V y) (t : T),
      sec ((pullOneCocycle U τ f γ).ev x y a b) t ≠ w := by
    intro x y
    by_cases h : ∃ z, z ∈ W x ∧ z ∈ W y
    · obtain ⟨z, hzx, hzy⟩ := h
      obtain ⟨k, hzk⟩ := hF z
      have hkx : x ∈ F k := by
        by_contra hk; exact Wb x k hk z hzx hzk
      have hky : y ∈ F k := by
        by_contra hk; exact Wb y k hk z hzy hzk
      refine ⟨_root_.Circle.exp Real.pi *
        (overlapFn γ (τ x) k ⟨x, FU _ (hτ x), FU k hkx⟩ *
          overlapFn γ k (τ y) ⟨y, FU k hky, FU _ (hτ y)⟩), fun T a b t => ?_⟩
      have htx : t.1 ∈ W x := a.le t.2
      have hty : t.1 ∈ W y := b.le t.2
      let c : T ⟶ U k := homOfLE fun u hu => Wa x k hkx (a.le hu)
      change sec (γ.ev (τ x) (τ y) (a ≫ f x) (b ≫ f y)) t ≠ _
      rw [← γ.ev_trans (τ x) k (τ y) (a ≫ f x) c (b ≫ f y)]
      change sec (γ.ev (τ x) k (a ≫ f x) c) t * sec (γ.ev k (τ y) c (b ≫ f y)) t ≠ _
      rw [sec_ev_eq_overlapFn, sec_ev_eq_overlapFn]
      obtain ⟨_, h1⟩ := Wc x (τ x) k (hτ x) hkx t.1 htx
      obtain ⟨_, h2⟩ := Wc y k (τ y) hky (hτ y) t.1 hty
      exact circle_mul_ne_neg _ _ _ _ h1 h2
    · refine ⟨1, fun T a b t => absurd ⟨t.1, a.le t.2, b.le t.2⟩ h⟩
  choose w hw using key
  exact ⟨V, τ, f, w, xW, fun x y T a b t => hw x y a b t⟩

include hU in
/-- **Local real lifts after refinement.** On a paracompact Hausdorff space,
every `U(1)`-cocycle on an open cover has, on some open refinement `x ↦ Vₓ ∋ x`,
a local real lift `ξ` with `exp(iξ) = γ`. -/
theorem exists_refinement_isRealLift :
    ∃ (V : X → Opens X) (r : X → I) (f : ∀ x, V x ⟶ U (r x)),
      (∀ x, x ∈ V x) ∧
        ∃ ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) V,
          IsRealLift (pullOneCocycle U r f γ) ξ := by
  obtain ⟨F, Fc, FU, Flf, hF⟩ := exists_closed_shrinking hU
  obtain ⟨V, r, f, w, hV, hw⟩ :=
    exists_refinement_avoidsPoints_of_shrinking γ Fc FU Flf hF
  exact ⟨V, r, f, hV, exists_isRealLift_of_avoids _ w hw⟩

end Refinement

end Cech

end QOU.CentralExtension
