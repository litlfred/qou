import QOU.MathlibExt.CechEdgeSubdiv
import QOU.MathlibExt.CechSameNerve

/-!
# Subdividing an edge keeps Čech `H²` of the star cover (route R3, step S3c)

A **triangulation** `T : Tri X` of a space `X` is a finite simplicial complex
`T.F` on a vertex type `T.V` with a homeomorphism `T.H : PSpace T.F ≃ₜ X`. Its
**star cover** `fam T` is the family of images of the open stars.

Subdividing an edge `{a, b}` gives a new triangulation `T.subdiv hab` (the
homeomorphism composed with `homeo`). In old barycentric coordinates `p`, its
star cover is obtained from the old one in two moves:

1. shrink `star b` to `{p_a < p_b}`, keeping all other stars (`ostar`); the nerve
   does not change;
2. split `star a = {p_a, p_b > 0} ∪ {p_b < p_a}`.

Every set and every intersection in sight is an admissible linear piece
(`CechPLComplex`), so all families are `ConnFamily`, and `sameNerve_pull_bijective`
and `split_pull_bijective` show that each move is a bijection on `H²`.

## Results, all sorry-free

* `tr`, `connFamily_tr`: transporting a family along a homeomorphism.
* `Reach`, `reach_of_pull`: a family is reached from a base family `U₀` if pulling
  `H²` back along some refinement is a bijection; reachedness propagates.
* `Tri`, `Tri.fam`, `Tri.subdiv`, `Tri.fam_covers`, `Tri.connFamily_fam`.
* `reach_subdiv`: **subdividing an edge keeps the star cover reached.**

## What this does NOT do

It does not control mesh or compare with all open covers (`CechGenus4Good`).
The identification of the genus-4 model with Bring's curve is a citation, and
`hχ` (Poincaré–Hopf) stays a hypothesis. Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S3/S4
-/
open CategoryTheory Opposite TopologicalSpace
open QOU.CentralExtension.CechGerbe

set_option linter.unusedSectionVars false

namespace QOU.CentralExtension.Cech.PL

/-! ### Transport along a homeomorphism -/

section Transport

variable {X Y : Type} [TopologicalSpace X] [TopologicalSpace Y]

/-- The image of an open set under a homeomorphism `H : Y ≃ₜ X`. -/
def tr (H : Y ≃ₜ X) (U : Opens Y) : Opens X :=
  ⟨H.symm ⁻¹' U, U.isOpen.preimage H.symm.continuous⟩

theorem mem_tr {H : Y ≃ₜ X} {U : Opens Y} {x : X} : x ∈ tr H U ↔ H.symm x ∈ U := Iff.rfl

theorem tr_inf (H : Y ≃ₜ X) (U W : Opens Y) : tr H (U ⊓ W) = tr H U ⊓ tr H W := rfl

theorem tr_mono (H : Y ≃ₜ X) {U W : Opens Y} (h : U ≤ W) : tr H U ≤ tr H W :=
  fun _ hx => h hx

theorem tr_sup (H : Y ≃ₜ X) (U W : Opens Y) : tr H (U ⊔ W) = tr H U ⊔ tr H W := by
  ext x; simp [tr]

theorem coe_tr (H : Y ≃ₜ X) (U : Opens Y) : (tr H U : Set X) = H '' (U : Set Y) := by
  show H.symm ⁻¹' _ = _
  rw [Homeomorph.preimage_symm]; rfl

theorem tr_isPreconnected (H : Y ≃ₜ X) {U : Opens Y} (h : IsPreconnected (U : Set Y)) :
    IsPreconnected (tr H U : Set X) := by
  rw [coe_tr]; exact h.image _ H.continuous.continuousOn

theorem tr_nonempty (H : Y ≃ₜ X) (U : Opens Y) :
    (tr H U : Set X).Nonempty ↔ (U : Set Y).Nonempty := by
  rw [coe_tr, Set.image_nonempty]

theorem connFamily_tr {ι : Type} (H : Y ≃ₜ X) {W : ι → Opens Y} (h : ConnFamily W) :
    ConnFamily (fun i => tr H (W i)) :=
  ⟨fun i j k => tr_isPreconnected H (h.pre3 i j k), fun i j => tr_isPreconnected H (h.pre2 i j)⟩

end Transport

/-! ### Reached families -/

section Reach

variable {X : Type} [TopologicalSpace X] (G : Type) [TopologicalSpace G] [CommGroup G]
  [IsTopologicalGroup G] [DiscreteTopology G] {ι₀ : Type} (U₀ : ι₀ → Opens X)

theorem H2.pull_pull'' {ι κ μ : Type} {U : ι → Opens X} {V : κ → Opens X} {W : μ → Opens X}
    (r : κ → ι) (f : ∀ j, V j ⟶ U (r j)) (r' : μ → κ) (f' : ∀ m, W m ⟶ V (r' m))
    (z : H2 U (contPresheaf X G)) :
    H2.pull r' f' (H2.pull r f z) = H2.pull (r ∘ r') (fun m => f' m ≫ f (r' m)) z := by
  induction z using Quot.ind with
  | mk c => rfl

/-- A family is **reached** from `U₀` if pulling `H²` back from `U₀` along some
refinement is a bijection. -/
def Reach {κ : Type} (W : κ → Opens X) : Prop :=
  ∃ (r : κ → ι₀) (hr : ∀ j, W j ≤ U₀ (r j)),
    Function.Bijective (H2.pull (𝒜 := contPresheaf X G) (U := U₀) r (fun j => homOfLE (hr j)))

variable {G U₀}

theorem reach_of_pull {κ μ : Type} {W : κ → Opens X} {W' : μ → Opens X} (h : Reach G U₀ W)
    (r' : μ → κ) (hr' : ∀ m, W' m ≤ W (r' m))
    (hb : Function.Bijective (H2.pull (𝒜 := contPresheaf X G) (U := W) r'
      (fun m => homOfLE (hr' m)))) : Reach G U₀ W' := by
  obtain ⟨r, hr, hbij⟩ := h
  refine ⟨r ∘ r', fun m => (hr' m).trans (hr _), ?_⟩
  have e : H2.pull (𝒜 := contPresheaf X G) (U := U₀) (r ∘ r')
      (fun m => homOfLE ((hr' m).trans (hr _))) =
      (H2.pull r' (fun m => homOfLE (hr' m))) ∘ (H2.pull r (fun j => homOfLE (hr j))) :=
    funext fun z => (H2.pull_pull'' G _ _ _ _ z).symm
  rw [e]; exact hb.comp hbij

theorem reach_congr {κ : Type} {W W' : κ → Opens X} (e : W = W') (h : Reach G U₀ W) :
    Reach G U₀ W' := e ▸ h

end Reach

/-! ### Triangulations -/

/-- A triangulation of `X`: a realised finite complex homeomorphic to `X`. -/
structure Tri (X : Type) [TopologicalSpace X] where
  V : Type
  [fin : Fintype V]
  [dec : DecidableEq V]
  F : Finset (Finset V)
  H : PSpace F ≃ₜ X

attribute [instance] Tri.fin Tri.dec

variable {X : Type} [TopologicalSpace X]

namespace Tri

/-- The star cover of a triangulation. -/
def fam (T : Tri X) (v : T.V) : Opens X := tr T.H (star T.F v)

theorem connFamily_fam (T : Tri X) : ConnFamily T.fam := connFamily_tr T.H (connFamily_star T.F)

theorem fam_covers (T : Tri X) (x : X) : ∃ v, x ∈ T.fam v := stars_cover T.F (T.H.symm x)

/-- Subdividing the edge `{a, b}`. -/
noncomputable def subdiv (T : Tri X) {a b : T.V} (hab : a ≠ b) : Tri X where
  V := Option T.V
  F := sub T.F a b
  H := (homeo T.F hab).trans T.H

end Tri

/-! ### One subdivision step -/

section Step

variable {V : Type} [Fintype V] [DecidableEq V] (F : Finset (Finset V)) (a b : V)

/-- Coefficients of the form `p_b - p_a`. -/
def lab : V → ℝ := fun w => (if w = b then 1 else 0) - (if w = a then 1 else 0)

theorem lf_lab (hab : a ≠ b) (p : V → ℝ) : lf (lab a b) p = p b - p a := by
  unfold lf lab
  simp only [sub_mul, one_mul, zero_mul, ite_mul, Finset.sum_sub_distrib, Finset.sum_ite_eq',
    Finset.mem_univ, if_true]

/-- Forms attached to a vertex set: `p_b > p_a` when `b ∈ S`. -/
def LS (S : Finset V) : Set (V → ℝ) := if b ∈ S then {lab a b} else ∅

theorem admissible_LS (hab : a ≠ b) (S : Finset V) : Admissible S (LS a b S) := by
  intro ℓ hℓ w hw
  unfold LS at hℓ
  split_ifs at hℓ with hb
  · rw [Set.mem_singleton_iff] at hℓ; subst hℓ
    have hwb : w ≠ b := fun e => hw (e ▸ hb)
    simp only [lab, if_neg hwb]; split_ifs <;> norm_num
  · exact hℓ.elim

/-- The shrunk star cover: `star b` becomes `{p_a < p_b}`. -/
def ostar (w : V) : Opens (PSpace F) :=
  ⟨{x | 0 < x.1 w ∧ (w = b → x.1 a < x.1 b)}, by
    by_cases h : w = b
    · have : {x : PSpace F | 0 < x.1 w ∧ (w = b → x.1 a < x.1 b)} =
          {x | 0 < x.1 w} ∩ {x | x.1 a < x.1 b} := by ext x; simp [h]
      rw [this]
      exact (isOpen_lt continuous_const ((continuous_apply w).comp continuous_subtype_val)).inter
        (isOpen_lt ((continuous_apply a).comp continuous_subtype_val)
          ((continuous_apply b).comp continuous_subtype_val))
    · have : {x : PSpace F | 0 < x.1 w ∧ (w = b → x.1 a < x.1 b)} = {x | 0 < x.1 w} := by
        ext x; simp [h]
      rw [this]
      exact isOpen_lt continuous_const ((continuous_apply w).comp continuous_subtype_val)⟩

theorem mem_ostar {w : V} {x : PSpace F} :
    x ∈ ostar F a b w ↔ 0 < x.1 w ∧ (w = b → x.1 a < x.1 b) := Iff.rfl

theorem ostar_le (w : V) : ostar F a b w ≤ star F w := fun _ hx => hx.1

theorem ostar_inter (hab : a ≠ b) (S : Finset V) :
    {x : PSpace F | ∀ w ∈ S, x ∈ ostar F a b w} = piece F S (LS a b S) := by
  ext x
  simp only [Set.mem_setOf_eq, mem_ostar, piece, LS]
  constructor
  · intro h
    refine ⟨fun w hw => (h w hw).1, fun ℓ hℓ => ?_⟩
    split_ifs at hℓ with hb
    · rw [Set.mem_singleton_iff] at hℓ; subst hℓ
      rw [lf_lab a b hab]; linarith [(h b hb).2 rfl]
    · exact hℓ.elim
  · rintro ⟨h1, h2⟩ w hw
    refine ⟨h1 w hw, fun e => ?_⟩
    subst e
    have := h2 (lab a w) (by simp [hw])
    rw [lf_lab a w hab] at this; linarith

theorem connFamily_ostar (hab : a ≠ b) : ConnFamily (ostar F a b) := by
  constructor
  · intro i j k
    have : ((ostar F a b i ⊓ ostar F a b j ⊓ ostar F a b k : Opens (PSpace F)) : Set (PSpace F)) =
        {x | ∀ w ∈ ({i, j, k} : Finset V), x ∈ ostar F a b w} := by
      ext x; simp [and_assoc]
    rw [this, ostar_inter F a b hab]
    exact piece_isPreconnected F (by simp) (admissible_LS a b hab _)
  · intro i j
    have : ((ostar F a b i ⊓ ostar F a b j : Opens (PSpace F)) : Set (PSpace F)) =
        {x | ∀ w ∈ ({i, j} : Finset V), x ∈ ostar F a b w} := by
      ext x; simp
    rw [this, ostar_inter F a b hab]
    exact piece_isPreconnected F (by simp) (admissible_LS a b hab _)

/-- A point of the shrunk cover over any vertex set lying in a face. -/
theorem ostar_nonempty (hab : a ≠ b) {S : Finset V} (hS : S.Nonempty) {f : Finset V}
    (hf : f ∈ F) (hSf : S ⊆ f) : ∃ x : PSpace F, ∀ w ∈ S, x ∈ ostar F a b w := by
  by_cases hb : b ∈ S
  · let c : V → ℝ := fun w => 1 / 2 * unif S w + if w = b then 1 / 2 else 0
    have hc0 : ∀ w, 0 ≤ c w := fun w => by
      have := unif_nonneg S w; simp only [c]; split_ifs <;> linarith
    have hc1 : ∑ w, c w = 1 := by
      simp only [c, Finset.sum_add_distrib, ← Finset.mul_sum, unif_sum hS, Finset.sum_ite_eq',
        Finset.mem_univ, if_true]
      norm_num
    have hcS : ∀ w, 0 < c w → w ∈ S := by
      intro w hw
      by_cases hwb : w = b
      · exact hwb ▸ hb
      · simp only [c, if_neg hwb, add_zero] at hw
        exact unif_pos_mem (by linarith)
    have hua : unif S a ≤ 1 := by
      unfold unif; split_ifs
      · exact inv_le_one_of_one_le₀ (by exact_mod_cast hS.card_pos)
      · norm_num
    refine ⟨⟨c, hc0, hc1, f, hf, fun w hw => hSf (hcS w hw)⟩, fun w hw => ⟨?_, fun e => ?_⟩⟩
    · have := unif_pos hw; simp only [c]; split_ifs <;> linarith
    · subst e
      simp only [c, if_neg hab, if_pos, add_zero]
      have := unif_pos hw
      linarith
  · refine ⟨⟨unif S, unif_mem F hS hf hSf⟩, fun w hw => ⟨unif_pos hw, fun e => ?_⟩⟩
    exact (hb (e ▸ hw)).elim

end Step

section StepCover

variable {G : Type} [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G]
  {ι₀ : Type} {U₀ : ι₀ → Opens X}

namespace Tri

variable (T : Tri X) {a b : T.V} (hab : a ≠ b)

/-- New star, in old coordinates. -/
def nstar (x : Option T.V) : Opens (PSpace T.F) :=
  ⟨{p | 0 < bwd a b p.1 x}, isOpen_lt continuous_const
    ((continuous_apply x).comp (continuous_bwd.comp continuous_subtype_val))⟩

theorem fam_subdiv (x : Option T.V) : (T.subdiv hab).fam x = tr T.H (T.nstar (a := a) (b := b) x) :=
  rfl

include hab in
theorem nstar_some_ne {w : T.V} (hwa : w ≠ a) :
    T.nstar (a := a) (b := b) (some w) = ostar T.F a b w := by
  ext x
  change 0 < bwd a b x.1 (some w) ↔ 0 < x.1 w ∧ (w = b → x.1 a < x.1 b)
  by_cases hwb : w = b
  · subst hwb
    rw [bwd_b_pos hab]
    have := x.2.1 a
    constructor
    · intro h; exact ⟨by linarith, fun _ => h⟩
    · intro h; exact h.2 rfl
  · rw [bwd_some_pos hwa hwb]; simp [hwb]

include hab in
/-- The new star cover is the split of the shrunk one at `a`. -/
theorem fam_subdiv_eq_split :
    (T.subdiv hab).fam = splitFam (fun w => tr T.H (ostar T.F a b w)) a
      (tr T.H (T.nstar (a := a) (b := b) none)) (tr T.H (T.nstar (a := a) (b := b) (some a))) := by
  funext x
  rw [fam_subdiv]
  cases x with
  | none => rfl
  | some w =>
    by_cases hw : w = a
    · subst hw; simp
    · rw [splitFam_some_ne hw, T.nstar_some_ne hab hw]

include hab in
theorem reach_subdiv (h : Reach G U₀ T.fam) : Reach G U₀ (T.subdiv hab).fam := by
  -- step 1: shrink to `ostar`
  have hO : ConnFamily (fun w => tr T.H (ostar T.F a b w)) :=
    connFamily_tr T.H (connFamily_ostar T.F a b hab)
  have hle : ∀ w, tr T.H (ostar T.F a b w) ≤ T.fam (Equiv.refl T.V w) :=
    fun w => tr_mono T.H (ostar_le T.F a b w)
  have h1 : Reach G U₀ (fun w => tr T.H (ostar T.F a b w)) := by
    refine reach_of_pull h (Equiv.refl T.V) hle ?_
    refine sameNerve_pull_bijective (Equiv.refl T.V) hle T.connFamily_fam hO
      (fun i j k hn => ?_) (fun i j k l hn => ?_)
    · obtain ⟨y, hy⟩ := hn
      have hy' : T.H.symm y ∈ piece T.F {i, j, k} ∅ := by
        rw [← star_inter3]; exact hy
      obtain ⟨f, hf, hSf⟩ := (inter_nonempty_iff T.F (by simp)).1 ⟨_, hy'⟩
      obtain ⟨x, hx⟩ := ostar_nonempty T.F a b hab (S := {i, j, k}) (by simp) hf hSf
      exact ⟨T.H x, by simpa [tr, and_assoc] using hx⟩
    · obtain ⟨y, hy⟩ := hn
      have hy' : T.H.symm y ∈ piece T.F {i, j, k, l} ∅ := by
        rw [← star_inter4]; exact hy
      obtain ⟨f, hf, hSf⟩ := (inter_nonempty_iff T.F (by simp)).1 ⟨_, hy'⟩
      obtain ⟨x, hx⟩ := ostar_nonempty T.F a b hab (S := {i, j, k, l}) (by simp) hf hSf
      exact ⟨T.H x, by simpa [tr, and_assoc] using hx⟩
  -- step 2: split `ostar a = star a`
  have hA : tr T.H (T.nstar (a := a) (b := b) none) ≤ tr T.H (ostar T.F a b a) := by
    refine tr_mono T.H fun x hx => ?_
    have := (bwd_none_pos (a := a) (b := b)).1 hx
    exact ⟨this.1, fun e => (hab e).elim⟩
  have hB : tr T.H (T.nstar (a := a) (b := b) (some a)) ≤ tr T.H (ostar T.F a b a) := by
    refine tr_mono T.H fun x hx => ?_
    have h1 := (bwd_a_pos hab).1 hx
    have := x.2.1 b
    exact ⟨by linarith, fun e => (hab e).elim⟩
  have hcov : tr T.H (ostar T.F a b a) ≤
      tr T.H (T.nstar (a := a) (b := b) none) ⊔ tr T.H (T.nstar (a := a) (b := b) (some a)) := by
    rw [← tr_sup]
    refine tr_mono T.H fun x hx => ?_
    have hxa : 0 < x.1 a := hx.1
    by_cases hb : 0 < x.1 b
    · exact Or.inl ((bwd_none_pos (a := a) (b := b)).2 ⟨hxa, hb⟩)
    · have : x.1 b = 0 := le_antisymm (not_lt.1 hb) (x.2.1 b)
      exact Or.inr ((bwd_a_pos hab).2 (by linarith))
  have hS : ConnFamily (splitFam (fun w => tr T.H (ostar T.F a b w)) a
      (tr T.H (T.nstar (a := a) (b := b) none)) (tr T.H (T.nstar (a := a) (b := b) (some a)))) := by
    rw [← T.fam_subdiv_eq_split hab]; exact (T.subdiv hab).connFamily_fam
  have h2 := reach_of_pull h1 (splitR a)
    (fun x => splitFam_le (U := fun w => tr T.H (ostar T.F a b w)) hA hB x)
    (split_pull_bijective (U := fun w => tr T.H (ostar T.F a b w)) hA hB hcov hO hS)
  exact reach_congr (T.fam_subdiv_eq_split hab).symm h2

end Tri

end StepCover

end QOU.CentralExtension.Cech.PL
