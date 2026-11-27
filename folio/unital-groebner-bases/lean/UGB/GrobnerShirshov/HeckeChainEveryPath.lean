import UGB.GrobnerShirshov.HeckeChainNormalForm
import Mathlib.Tactic.FinCases

/-!
# Every reduction of the block-ordered element uses the Hecke rule only

`HeckeChainNormalForm.lean` proves where the reduction of the block-ordered
element `Ξ = ∏ᵢ ∏_{(c,d) ∈ Lᵢ} (c σᵢ + d)` ends (the chain form) and that the
difference lies in the ideal of the Hecke relations alone. This file settles the
two claims of `prop:tm-gs-normal-form` that file left unformalised.

**1. Every path is Hecke-only** (`chainXi_every_reduction_heckeOnly`). Every word
of `Ξ` has weakly increasing generator indices, and a Hecke step keeps that true:
it replaces `a σᵢσᵢ b` by `a σᵢ b` and `a b`. Every leading word of a
Yang–Baxter, far-commutativity or Bokut–Shiao rule contains a strict descent, so
none of them ever occurs. Hence any reduction sequence of `Ξ` in the completed
system, in any order, is a reduction sequence of the Hecke-only system
`heckeOnlySystem`.

**2. The step count is not a count of single rewriting steps**
(`chainXi_L3_needs_two_steps`). The proposition bounds the reduction by
`C(A − 1, 2)` Hecke steps. At `A = 3`, with every crossing `σ + 1`, that bound is
`C(2, 2) = 1`, but `Ξ` is not normal and no single step of the completed system
from `Ξ` reaches a normal form: `Ξ` has two non-normal words, `σ₀σ₀σ₁` and
`σ₀σ₀`, and one step rewrites one of them. The `C(A − 1, 2)` count is the number
of block multiplications in the transfer-matrix computation (`heckeStepBound` in
`QOU/TransferMatrices/GSNormalForm.lean`), not a bound on rewriting steps.

-- Ref: [leitner2026] folio/quantum-observable-universe/appendix-transfer-matrices/tm-gs-normal-form.md
-/

set_option linter.unusedSectionVars false

namespace UGB.GrobnerShirshov.Diamond

open UGB.GrobnerShirshov AlgElement UGB.GrobnerShirshov.Hecke

section EveryPath

variable {n : ℕ} (hp : HeckeParams)

/-- Every word with non-zero coefficient has weakly increasing generator indices. -/
def WeaklySorted (f : AlgElement (HeckeGen n) ℝ) : Prop :=
  ∀ m, f.coeff m ≠ 0 → m.Pairwise (fun x y : HeckeGen n => x.index ≤ y.index)

theorem contextMul_coeff_ne_zero {G : Type*} [DecidableEq G] {k : Type*} [Ring k]
    {a b m : Monomial G} {f : AlgElement G k} (h : (contextMul a f b).coeff m ≠ 0) :
    ∃ w, f.coeff w ≠ 0 ∧ m = a ++ w ++ b := by
  unfold contextMul at h
  dsimp only at h
  split_ifs at h with he
  · exact ⟨_, h, he.symm⟩
  · exact absurd rfl h

theorem heckeRelation_coeff_ne_zero (i : Fin n) {w : Monomial (HeckeGen n)}
    (h : (heckeRelation i hp).relation.coeff w ≠ 0) :
    w = [⟨i⟩, ⟨i⟩] ∨ w = [⟨i⟩] ∨ w = [] := by
  rw [← toMA_apply, toMA_heckeRelation] at h
  have e1 : sg i * sg i = (ofW [⟨i⟩, ⟨i⟩] : MA (HeckeGen n) ℝ) := by
    rw [sg, ← ofW_append]; rfl
  have e0 : (1 : MA (HeckeGen n) ℝ) = ofW [] := rfl
  rw [e1, e0, Finsupp.sub_apply, Finsupp.sub_apply, Finsupp.smul_apply, smul_eq_mul, sg,
    ofW_apply, ofW_apply, ofW_apply] at h
  by_contra hc
  push_neg at hc
  rw [if_neg (Ne.symm hc.1), if_neg (Ne.symm hc.2.1), if_neg (Ne.symm hc.2.2)] at h
  simp at h

theorem mem_descWord_low {i j : Fin n} (h : j.val ≤ i.val) :
    (⟨j⟩ : HeckeGen n) ∈ descWord i j := by
  simp only [descWord, List.mem_map, List.mem_reverse, List.mem_filter, List.mem_finRange,
    true_and, decide_eq_true_eq, HeckeGen.mk.injEq]
  exact ⟨j, ⟨le_refl _, h⟩, rfl⟩

/-- **Only a Hecke rule can fire on a weakly sorted element.** If a rule of the
    completed system has its leading word inside a weakly sorted word, the rule
    is a Hecke rule: Yang–Baxter, far-commutativity and Bokut–Shiao leading words
    all contain a strict descent. -/
theorem rule_hecke_of_weaklySorted (hn : 0 < n) {r : ReductionRule (HeckeGen n) ℝ}
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) {a b : Monomial (HeckeGen n)}
    (hs : (a ++ r.lm (heckeOrder n) ++ b).Pairwise
      (fun x y : HeckeGen n => x.index ≤ y.index)) :
    ∃ i, r = heckeRelation i hp := by
  have hpw : (r.lm (heckeOrder n)).Pairwise (fun x y : HeckeGen n => x.index ≤ y.index) :=
    hs.sublist (List.infix_append a _ b |>.sublist)
  rcases mem_heckeCompletedRewritingSystem_rules hn hp hr with
    h | ⟨i, j, hij, rfl⟩ | ⟨i, j, hij, rfl⟩ | ⟨i', i, j, hi, hj, rfl⟩
  · exact h
  · rw [yangBaxterRelation_lm i j (by omega)] at hpw
    have := (List.pairwise_cons.mp hpw).1 ⟨i⟩ (by simp)
    simp only [Fin.le_def] at this; omega
  · rw [farCommRelation_lm i j (by omega)] at hpw
    have := (List.pairwise_cons.mp hpw).1 _ (List.mem_singleton_self _)
    simp only [Fin.le_def] at this; omega
  · rw [bokutShiaoRelation_lm hi hj, bsWord₁_cons hi hj] at hpw
    have := (List.pairwise_cons.mp hpw).1 _
      (List.mem_append_left _ (mem_descWord_low hj))
    simp only [Fin.le_def] at this; omega

/-- A step from a weakly sorted element stays weakly sorted. -/
theorem weaklySorted_step (hn : 0 < n) {f g : AlgElement (HeckeGen n) ℝ}
    (hf : WeaklySorted f)
    (h : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp) f g) :
    WeaklySorted g := by
  obtain ⟨r, hr, a, b, c, hne, -, hg⟩ := h.exists_witness
  obtain ⟨i, rfl⟩ := rule_hecke_of_weaklySorted hp hn hr (hf _ hne)
  have hm := hf _ hne
  rw [heckeRelation_lm] at hm
  intro m hm0
  rw [hg m, sub_coeff, smul_coeff] at hm0
  by_cases hfm : f.coeff m = 0
  · rw [hfm, zero_sub, neg_ne_zero] at hm0
    obtain ⟨w, hw, rfl⟩ := contextMul_coeff_ne_zero (right_ne_zero_of_mul hm0)
    rcases heckeRelation_coeff_ne_zero hp i hw with rfl | rfl | rfl
    · exact hm
    · refine hm.sublist ?_
      exact ((List.Sublist.refl a).append (by simp)).append (List.Sublist.refl b)
    · refine hm.sublist ?_
      simp
  · exact hf m hfm

/-- The Hecke rules alone, as a rewriting system. -/
noncomputable def heckeOnlySystem (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    RewritingSystem (HeckeGen n) ℝ :=
  .ofList ((List.finRange n).map (fun i => heckeRelation i hp)) (by
    intro h
    have := congrArg List.length h
    simp at this
    omega)

/-- **Every reduction from a weakly sorted element uses the Hecke rules only.**
    Any reduction sequence in the completed system starting at a weakly sorted
    element is, step by step, a reduction sequence in the Hecke-only system. -/
theorem multiStep_heckeOnly_of_weaklySorted (hn : 0 < n) {f g : AlgElement (HeckeGen n) ℝ}
    (hf : WeaklySorted f)
    (h : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp) f g) :
    MultiStepReduction (heckeOrder n) (heckeOnlySystem n hn hp) f g ∧ WeaklySorted g := by
  induction h with
  | refl => exact ⟨MultiStepReduction.refl _, hf⟩
  | step _ hstep ih =>
    obtain ⟨ih1, ih2⟩ := ih
    refine ⟨MultiStepReduction.step ih1 ⟨?_⟩, weaklySorted_step hp hn ih2 hstep⟩
    obtain ⟨r, hr, a, b, c, hne, hc, hg⟩ := hstep.exists_witness
    obtain ⟨i, rfl⟩ := rule_hecke_of_weaklySorted hp hn hr (ih2 _ hne)
    exact ⟨heckeRelation i hp, List.mem_map.mpr ⟨i, List.mem_finRange _, rfl⟩,
      a, b, c, hne, hc, hg⟩

/-- The support of a product of linear forms `∏ (c σᵢ + d)` over a flat list of
    `(index, pair)` consists of subwords of the index list. -/
theorem support_prod_lin_flat (l : List (Fin n × (ℝ × ℝ))) :
    ∀ x ∈ ((l.map (fun p => lin p.1 p.2)).prod).support,
      (FreeMonoid.toList x).Sublist (l.map (fun p => (⟨p.1⟩ : HeckeGen n))) := by
  classical
  induction l with
  | nil =>
    intro x hx
    rw [List.map_nil, List.prod_nil, MonoidAlgebra.one_def] at hx
    rw [Finset.mem_singleton.mp (Finsupp.support_single_subset hx)]
    simp
  | cons p l ih =>
    intro x hx
    rw [List.map_cons, List.prod_cons] at hx
    obtain ⟨y, hy, z, hz, rfl⟩ := Finset.mem_mul.mp (MonoidAlgebra.support_mul _ _ hx)
    have hz' := ih z hz
    rw [FreeMonoid.toList_mul, List.map_cons]
    have hy' : y = FreeMonoid.ofList [⟨p.1⟩] ∨ y = 1 := by
      rcases Finset.mem_union.mp (Finsupp.support_add hy) with h | h
      · exact Or.inl (Finset.mem_singleton.mp
          (Finsupp.support_single_subset (Finsupp.support_smul h)))
      · have := Finsupp.support_smul h
        rw [MonoidAlgebra.one_def] at this
        exact Or.inr (Finset.mem_singleton.mp (Finsupp.support_single_subset this))
    rcases hy' with rfl | rfl
    · exact hz'.cons₂ _
    · simpa using hz'.cons _

/-- The flat list of crossings of `Ξ`, blocks in increasing index. -/
def chainFlat (L : Fin n → List (ℝ × ℝ)) : List (Fin n × (ℝ × ℝ)) :=
  (List.finRange n).flatMap (fun i => (L i).map (fun p => (i, p)))

theorem chainXi_eq_flat (L : Fin n → List (ℝ × ℝ)) :
    chainXi L = ((chainFlat L).map (fun p => lin p.1 p.2)).prod := by
  rw [chainXi, chainFlat]
  induction (List.finRange n) with
  | nil => simp
  | cons i l ih => simp [List.flatMap_cons, List.prod_append, ih, List.map_map, Function.comp_def]

theorem chainFlat_index_sorted (L : Fin n → List (ℝ × ℝ)) :
    ((chainFlat L).map (fun p => (⟨p.1⟩ : HeckeGen n))).Pairwise
      (fun x y : HeckeGen n => x.index ≤ y.index) := by
  rw [chainFlat, List.map_flatMap, List.pairwise_flatMap]
  refine ⟨fun i _ => ?_, ?_⟩
  · simp only [List.map_map, Function.comp_def, List.pairwise_map]
    exact List.Pairwise.imp (fun _ => le_refl _) (List.pairwise_of_forall (fun _ _ => trivial))
  · refine (List.pairwise_lt_finRange n).imp (fun {a b} hab => ?_)
    intro x hx y hy
    simp only [List.map_map, Function.comp_def, List.mem_map] at hx hy
    obtain ⟨_, _, rfl⟩ := hx
    obtain ⟨_, _, rfl⟩ := hy
    exact le_of_lt hab

/-- `Ξ` is weakly sorted. -/
theorem chainXi_weaklySorted (L : Fin n → List (ℝ × ℝ)) : WeaklySorted (ofMA (chainXi L)) := by
  intro m hm
  have hx : FreeMonoid.ofList m ∈ (chainXi L).support := Finsupp.mem_support_iff.mpr hm
  rw [chainXi_eq_flat] at hx
  have := support_prod_lin_flat (chainFlat L) _ hx
  rw [FreeMonoid.toList_ofList] at this
  exact (chainFlat_index_sorted L).sublist this

/-- **Every reduction of the block-ordered element uses the Hecke rules only.**
    Any reduction sequence of `Ξ` in the completed system — any order of steps,
    any rule chosen at each step — is a reduction sequence in the Hecke-only
    system: no Yang–Baxter, far-commutativity or Bokut–Shiao step ever applies. -/
theorem chainXi_every_reduction_heckeOnly (hn : 0 < n) (L : Fin n → List (ℝ × ℝ))
    {g : AlgElement (HeckeGen n) ℝ}
    (h : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (ofMA (chainXi L)) g) :
    MultiStepReduction (heckeOrder n) (heckeOnlySystem n hn hp) (ofMA (chainXi L)) g :=
  (multiStep_heckeOnly_of_weaklySorted hp hn (chainXi_weaklySorted L) h).1

end EveryPath

/-! ## §3  The step count is not a count of single reduction steps

The proposition bounds the reduction by `C(A − 1, 2)` Hecke steps. That number
counts the block multiplications (one linear form times another, then one use of
the Hecke relation). It does not count the single steps of the rewriting system,
which rewrite one occurrence in one word. At `A = 3` with every crossing equal to
`σ + 1`, `C(A − 1, 2) = 1`, yet no single step from `Ξ` reaches a normal form. -/

section StepCount

variable (hp : HeckeParams)

/-- The `A = 3` crossing data: block `0` has two crossings, block `1` one; each
    crossing is `σᵢ + 1`. -/
def L3 (i : Fin 2) : List (ℝ × ℝ) := if i = 0 then [(1, 1), (1, 1)] else [(1, 1)]

private abbrev g0 : HeckeGen 2 := ⟨0⟩
private abbrev g1 : HeckeGen 2 := ⟨1⟩

theorem chainXi_L3 : chainXi L3 =
    ofW [g0, g0, g1] + ofW [g0, g0] + (2 : ℝ) • ofW [g0, g1] + (2 : ℝ) • ofW [g0]
      + ofW [g1] + ofW [] := by
  have h0 : lin (0 : Fin 2) (1, 1) = ofW [g0] + ofW [] := by simp [lin, sg]; rfl
  have h1 : lin (1 : Fin 2) (1, 1) = ofW [g1] + ofW [] := by simp [lin, sg]; rfl
  have hl : (List.finRange 2) = [0, 1] := by decide
  have e : chainXi L3 = lin (0 : Fin 2) (1, 1) * lin (0 : Fin 2) (1, 1) * lin (1 : Fin 2) (1, 1) := by
    simp [chainXi, hl, L3, mul_assoc]
  rw [e, h0, h1]
  simp only [add_mul, mul_add, ← ofW_append, List.cons_append, List.nil_append,
    List.append_nil]
  module

theorem coeff_L3 (w : Monomial (HeckeGen 2)) : (ofMA (chainXi L3)).coeff w =
    (if [g0, g0, g1] = w then 1 else 0) + (if [g0, g0] = w then 1 else 0)
      + 2 * (if [g0, g1] = w then 1 else 0) + 2 * (if [g0] = w then 1 else 0)
      + (if [g1] = w then 1 else 0) + (if [] = w then 1 else 0) := by
  show (chainXi L3) (FreeMonoid.ofList w) = _
  rw [chainXi_L3]
  rw [Finsupp.add_apply, Finsupp.add_apply, Finsupp.add_apply, Finsupp.add_apply,
    Finsupp.add_apply, Finsupp.smul_apply, Finsupp.smul_apply, smul_eq_mul, smul_eq_mul,
    ofW_apply, ofW_apply, ofW_apply, ofW_apply, ofW_apply, ofW_apply]

theorem mem_of_coeff_L3 {w : Monomial (HeckeGen 2)} (h : (ofMA (chainXi L3)).coeff w ≠ 0) :
    w = [g0, g0, g1] ∨ w = [g0, g0] ∨ w = [g0, g1] ∨ w = [g0] ∨ w = [g1] ∨ w = [] := by
  rw [coeff_L3] at h
  by_contra hc
  push_neg at hc
  obtain ⟨h1, h2, h3, h4, h5, h6⟩ := hc
  rw [if_neg (Ne.symm h1), if_neg (Ne.symm h2), if_neg (Ne.symm h3), if_neg (Ne.symm h4),
    if_neg (Ne.symm h5), if_neg (Ne.symm h6)] at h
  simp at h

/-- Where a Hecke leading word can sit inside a word of `Ξ`. -/
theorem position_L3 {a b : Monomial (HeckeGen 2)} {i : Fin 2}
    (h : (ofMA (chainXi L3)).coeff (a ++ [⟨i⟩, ⟨i⟩] ++ b) ≠ 0) :
    (a = [] ∧ b = [g1] ∧ i = 0) ∨ (a = [] ∧ b = [] ∧ i = 0) := by
  have hm := mem_of_coeff_L3 h
  rcases a with _ | ⟨x, _ | ⟨y, a⟩⟩ <;> rcases b with _ | ⟨z, _ | ⟨u, b⟩⟩ <;>
    fin_cases i <;> simp [g0, g1, HeckeGen.mk.injEq] at hm ⊢
  all_goals first
    | exact hm
    | (have hl := congrArg List.length hm.2.2; simp at hl; omega)
    | (have hl := congrArg List.length hm.2.2; simp at hl)


/-- A word containing `σ₀σ₀` with non-zero coefficient makes an element non-normal. -/
theorem not_normal_of_coeff_L3 (hn : 0 < 2) {g : AlgElement (HeckeGen 2) ℝ}
    {w : Monomial (HeckeGen 2)} (hw : [g0, g0] <:+: w) (hg : g.coeff w ≠ 0) :
    ¬ isNormalForm (heckeOrder 2) (heckeCompletedRewritingSystem 2 hn hp) g := by
  intro hnf
  refine hnf (heckeRelation 0 hp) (heckeRelation_mem hn hp 0) w hg ?_
  rw [heckeRelation_lm]; exact hw

/-- **No single step from `Ξ` (at `A = 3`) reaches a normal form.** `Ξ` is not
    normal, and after any one step of the completed system a word containing
    `σ₀σ₀` still has non-zero coefficient. So every reduction of `Ξ` to normal
    form takes at least two single steps, while `C(A − 1, 2) = C(2, 2) = 1`. -/
theorem chainXi_L3_needs_two_steps (hn : 0 < 2) :
    ¬ isNormalForm (heckeOrder 2) (heckeCompletedRewritingSystem 2 hn hp)
        (ofMA (chainXi L3)) ∧
    ∀ g, SingleStepReduction (heckeOrder 2) (heckeCompletedRewritingSystem 2 hn hp)
        (ofMA (chainXi L3)) g →
      ¬ isNormalForm (heckeOrder 2) (heckeCompletedRewritingSystem 2 hn hp) g := by
  refine ⟨not_normal_of_coeff_L3 hp hn (w := [g0, g0, g1]) ⟨[], [g1], rfl⟩
    (by rw [coeff_L3]; simp), ?_⟩
  intro g hstep
  obtain ⟨r, hr, a, b, c, hne, -, hg⟩ := hstep.exists_witness
  obtain ⟨i, rfl⟩ := rule_hecke_of_weaklySorted hp hn hr (chainXi_weaklySorted L3 _ hne)
  rw [heckeRelation_lm] at hne
  -- a word containing σ₀σ₀ that the step does not touch
  have key : ∀ w : Monomial (HeckeGen 2), w ≠ a ++ [⟨i⟩, ⟨i⟩] ++ b → w ≠ a ++ [⟨i⟩] ++ b →
      w ≠ a ++ b → g.coeff w = (ofMA (chainXi L3)).coeff w := by
    intro w h1 h2 h3
    rw [hg w, sub_coeff, smul_coeff]
    suffices (contextMul a (heckeRelation i hp).relation b).coeff w = 0 by simp [this]
    by_contra hc
    obtain ⟨w', hw', rfl⟩ := contextMul_coeff_ne_zero hc
    rcases heckeRelation_coeff_ne_zero hp i hw' with rfl | rfl | rfl
    · exact h1 rfl
    · exact h2 rfl
    · exact h3 (by simp)
  rcases position_L3 hne with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩
  · refine not_normal_of_coeff_L3 hp hn (w := [g0, g0]) ⟨[], [], rfl⟩ ?_
    rw [key _ (by decide) (by decide) (by decide), coeff_L3]; simp
  · refine not_normal_of_coeff_L3 hp hn (w := [g0, g0, g1]) ⟨[], [g1], rfl⟩ ?_
    rw [key _ (by decide) (by decide) (by decide), coeff_L3]; simp

end StepCount

end UGB.GrobnerShirshov.Diamond
