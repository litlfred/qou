import UGB.GrobnerShirshov.HeckeCompletion
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.IntervalCases

/-!
# Three strands: the defining relations of `H₃(q)` are already a Gröbner–Shirshov basis

`HeckeGS.lean` §4e shows that the defining relations of the Hecke algebra are
**not** a Gröbner–Shirshov basis once there are three generators
(`hecke_not_gs_basis_four`), and `HeckeCompletion.lean` proves that adding the
Bokut–Shiao family repairs this for every number of generators
(`heckeCompleted_isGrobnerShirshovBasis`).

With **two** generators `σ₀, σ₁` — the algebra `H₃(q)` of three strands — no
repair is needed. The completion family then has a single member,
`bokutShiaoRelation 0 1 0`, and it is the negative of the Yang–Baxter rule on
the same leading monomial `σ₁σ₀σ₁`. So the three defining relations

  `σ₀² → (q − q⁻¹)σ₀ + 1`,  `σ₁² → (q − q⁻¹)σ₁ + 1`,  `σ₁σ₀σ₁ → σ₀σ₁σ₀`

(convention D, `(σ − q)(σ + q⁻¹) = 0`, deg-lex with `σ₀ < σ₁`) already form a
Gröbner–Shirshov basis, and the words irreducible for them are exactly the six

  `1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀`,

which is `3! = dim H₃(q)` of them.

## What is proved here

* §1 **Dropping a redundant rule preserves the Gröbner–Shirshov property**
  (`IsGrobnerShirshovBasis.of_proxy`). If every rule of a larger system has a
  stand-in in a smaller sub-system with the same leading monomial and a relation
  that is a scalar multiple, then every reduction in the larger system is a
  reduction in the smaller one, so compositions that resolve in the larger
  system resolve in the smaller one. This is generic in the ground ring and the
  generators.
* §2 `heckeRewritingSystem_two_isGrobnerShirshovBasis`: the uncompleted Hecke
  system on two generators is a Gröbner–Shirshov basis, for every `HeckeParams`.
  With it, `heckeTwo_normalForm_unique`: normal forms are unique up to `CoeffEq`.
* §3 `heckeTwo_irreducible_iff`: a word is irreducible for that system iff it
  is one of the six words above; `standardWordsTwo_length` and
  `standardWordsTwo_nodup` count them. `heckeTwo_normalForm_exists_six`: every
  element reduces to a normal form supported on those six words.
* §4 `NotAGSBasisThree.hecke_not_gs_basis_three` (`H₄(q)`, on `σ₂σ₁σ₂σ₀`) and
  `NotAGSBasisGe3.hecke_not_gs_basis_of_three_le` (every `n ≥ 3`), hence the
  sharp statement `heckeRewritingSystem_isGrobnerShirshovBasis_iff`: the
  defining relations are a Gröbner–Shirshov basis **iff `n ≤ 2`**. (`HeckeGS.lean`
  §4e had the refutation at `n = 4` only.)

All of the above depend on `[propext, Classical.choice, Quot.sound]` only.
The ground ring is `ℝ` with `q > 0, q ≠ 1` because that is how `HeckeParams`
is declared in `HeckeGS.lean`; nothing here uses either inequality, and §1 is
stated over an arbitrary ring.

## What is not proved here

That the six words are **linearly independent in `H₃(q)`**, i.e. that the
quotient has dimension 6. The Gröbner–Shirshov property gives this through the
composition-diamond lemma (Bokut–Chen 2014, Thm 2.x; Bergman 1978, Thm 1.2) once
the quotient algebra is constructed; this folio does not construct it.

## References

- Kang & Lee, *Gröbner–Shirshov bases for irreducible sl_{n+1}-modules*,
  J. Algebra 232 (2000) 1–20, Example 1.11: the GS basis of the type-A Hecke
  algebra, in the normalisation `(T − q)(T + 1) = 0`. Not yet held in
  `library/`; read through an extracted-text fetch only.
- Bokut & Chen, *Gröbner–Shirshov bases and their calculation*, Bull. Math. Sci.
  4 (2014) 325–395 [bokutchen2014].
-/

namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Dropping a redundant rule -/

section Proxy

variable {G : Type u} {k : Type v} [Ring k] [DecidableEq G] {ord : AdmissibleOrder G}

/-- `sys₁` **proxies** `sys₂` when every rule of `sys₂` has a stand-in in `sys₁`
with the same leading monomial whose relation, scaled by some `u`, is the
original relation, coefficient by coefficient. -/
def RuleProxy (ord : AdmissibleOrder G) (sys₁ sys₂ : RewritingSystem G k) : Prop :=
  ∀ r₂ ∈ sys₂.rules, ∃ r₁ ∈ sys₁.rules, ∃ u : k,
    r₁.lm ord = r₂.lm ord ∧ ∀ w, r₂.relation.coeff w = u * r₁.relation.coeff w

/-- `contextMul` commutes with a coefficientwise scalar multiple. -/
theorem contextMul_coeff_of_smul (a b : Monomial G) {f g : AlgElement G k} (u : k)
    (h : ∀ w, f.coeff w = u * g.coeff w) (m : Monomial G) :
    (AlgElement.contextMul a f b).coeff m
      = u * (AlgElement.contextMul a g b).coeff m := by
  show (if a ++ excise a m b ++ b = m then f.coeff (excise a m b) else 0)
     = u * (if a ++ excise a m b ++ b = m then
          g.coeff (excise a m b) else 0)
  split_ifs
  · exact h _
  · rw [mul_zero]

/-- A step of the larger system is a step of the proxying system. -/
theorem SingleStepReduction.of_proxy {sys₁ sys₂ : RewritingSystem G k}
    (hP : RuleProxy ord sys₁ sys₂) {f g : AlgElement G k}
    (h : SingleStepReduction ord sys₂ f g) : SingleStepReduction ord sys₁ f g := by
  obtain ⟨r₂, hr₂, a, b, c, hne, hc, heq⟩ := h.exists_witness
  obtain ⟨r₁, hr₁, u, hlm, hcoef⟩ := hP r₂ hr₂
  refine ⟨⟨r₁, hr₁, a, b, c * u, ?_, ?_, ?_⟩⟩
  · rw [hlm]; exact hne
  · rw [hlm, ← hc]
    show c * u * r₁.relation.coeff (r₁.lm ord) = c * r₂.relation.coeff (r₂.lm ord)
    rw [hcoef, hlm, mul_assoc]
  · intro m
    rw [heq m]
    simp only [AlgElement.sub_coeff, AlgElement.smul_coeff]
    rw [contextMul_coeff_of_smul a b u hcoef m, mul_assoc]

/-- A run of the larger system is a run of the proxying system. -/
theorem MultiStepReduction.of_proxy {sys₁ sys₂ : RewritingSystem G k}
    (hP : RuleProxy ord sys₁ sys₂) {f g : AlgElement G k}
    (h : MultiStepReduction ord sys₂ f g) : MultiStepReduction ord sys₁ f g := by
  induction h with
  | refl => exact MultiStepReduction.refl _
  | step _ hlast ih => exact MultiStepReduction.step ih (SingleStepReduction.of_proxy hP hlast)

/-- **Dropping redundant rules preserves the Gröbner–Shirshov property.**
If `sys₁ ⊆ sys₂` and every rule of `sys₂` has a proxy in `sys₁`, a
Gröbner–Shirshov basis `sys₂` makes `sys₁` one too: each composition of `sys₁`
is a composition of `sys₂`, its reduction to zero there is a reduction in
`sys₁`, and zero is a normal form for any system. -/
theorem IsGrobnerShirshovBasis.of_proxy {sys₁ sys₂ : RewritingSystem G k}
    (hsub : sys₁.rules ⊆ sys₂.rules) (hP : RuleProxy ord sys₁ sys₂)
    (h : IsGrobnerShirshovBasis G k ord sys₂) : IsGrobnerShirshovBasis G k ord sys₁ := by
  constructor
  · intro oc h₁ h₂
    obtain ⟨nf, hred, hz⟩ := h.overlap_resolves oc (hsub h₁) (hsub h₂)
    exact ⟨nf, ⟨MultiStepReduction.of_proxy hP hred.reduces, isNormalForm_of_isZero hz⟩, hz⟩
  · intro ic h₁ h₂
    obtain ⟨nf, hred, hz⟩ := h.inclusion_resolves ic (hsub h₁) (hsub h₂)
    exact ⟨nf, ⟨MultiStepReduction.of_proxy hP hred.reduces, isNormalForm_of_isZero hz⟩, hz⟩

end Proxy

namespace Hecke

/-! ## §2  The uncompleted system on two generators -/

/-- The uncompleted rules sit inside the completed ones, for every `n`. -/
theorem heckeRules_subset_completed (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    (heckeRewritingSystem n hn hp).rules ⊆ (heckeCompletedRewritingSystem n hn hp).rules := by
  intro r hr
  simp only [heckeRewritingSystem, heckeCompletedRewritingSystem,
    RewritingSystem.mem_ofList_rules, heckeCompletedRules, List.mem_append] at hr ⊢
  exact Or.inl hr

/-- Every Yang–Baxter rule on an adjacent pair is a rule of the system. -/
theorem yangBaxter_mem {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i j : Fin n}
    (h : j.val = i.val + 1) :
    yangBaxterRelation i j ∈ (heckeRewritingSystem n hn hp).rules := by
  refine List.mem_append_left _ (List.mem_append_right _ ?_)
  refine List.mem_flatMap.mpr ⟨i, List.mem_finRange i, ?_⟩
  exact List.mem_filterMap.mpr ⟨j, List.mem_finRange j, by simp [h]⟩

/-- With at most two generators, every rule of the completed system is proxied
by the uncompleted one: a Bokut–Shiao rule `bokutShiaoRelation i' i j` needs
`j ≤ i' < i < n ≤ 2`, so `j = i'`, and at `j = i'` it is `−1` times the
Yang–Baxter rule on the same leading monomial. -/
theorem ruleProxy_of_le_two {n : ℕ} (hn : 0 < n) (h2 : n ≤ 2) (hp : HeckeParams) :
    RuleProxy (heckeOrder n) (heckeRewritingSystem n hn hp)
      (heckeCompletedRewritingSystem n hn hp) := by
  intro r₂ hr₂
  have hr₂' := hr₂
  simp only [heckeCompletedRewritingSystem, RewritingSystem.mem_ofList_rules,
    heckeCompletedRules, List.mem_append] at hr₂'
  rcases hr₂' with hbase | hbs
  · exact ⟨r₂, hbase, 1, rfl, fun w => by rw [one_mul]⟩
  · simp only [List.mem_flatMap, List.mem_filterMap, List.mem_finRange, true_and] at hbs
    obtain ⟨i, i', j, hj⟩ := hbs
    by_cases hc : i'.val + 1 = i.val ∧ j.val ≤ i'.val
    · rw [if_pos hc, Option.some.injEq] at hj
      subst hj
      obtain ⟨hi, hji⟩ := hc
      have hlt := i.isLt
      have hjj : j = i' := Fin.ext (by omega)
      subst hjj
      refine ⟨yangBaxterRelation j i, yangBaxter_mem hn hp hi.symm, -1,
        (bokutShiao_lm_eq_yangBaxter_lm hi).symm, fun w => ?_⟩
      have h := DegenerateYbBs.relations_add_eq_zero hi w
      linarith
    · rw [if_neg hc] at hj
      cases hj

/-- **With at most two generators the defining Hecke relations are a
Gröbner–Shirshov basis**, for every `HeckeParams`. -/
theorem heckeRewritingSystem_isGrobnerShirshovBasis_of_le_two {n : ℕ} (hn : 0 < n)
    (h2 : n ≤ 2) (hp : HeckeParams) :
    IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n) (heckeRewritingSystem n hn hp) :=
  IsGrobnerShirshovBasis.of_proxy (heckeRules_subset_completed n hn hp)
    (ruleProxy_of_le_two hn h2 hp) (heckeCompleted_isGrobnerShirshovBasis hn hp)

/-- **The defining relations of `H₃(q)` are a Gröbner–Shirshov basis.** The
uncompleted Hecke system on two generators, under deg-lex with `σ₀ < σ₁`, for
every `HeckeParams`. Contrast `hecke_not_gs_basis_four` at three generators. -/
theorem heckeRewritingSystem_two_isGrobnerShirshovBasis (hp : HeckeParams) :
    IsGrobnerShirshovBasis (HeckeGen 2) ℝ (heckeOrder 2)
      (heckeRewritingSystem 2 (by norm_num) hp) :=
  heckeRewritingSystem_isGrobnerShirshovBasis_of_le_two (by norm_num) le_rfl hp

/-- Every rule of the two-generator system has a unit leading coefficient. -/
theorem heckeTwo_rules_lc_isUnit (hp : HeckeParams) :
    ∀ r ∈ (heckeRewritingSystem 2 (by norm_num) hp).rules,
      IsUnit (r.lc (heckeOrder 2)) := fun r hr =>
  heckeCompleted_rules_lc_isUnit (by norm_num) hp r
    (heckeRules_subset_completed 2 (by norm_num) hp hr)

/-- **Normal forms in `H₃(q)` are unique** (up to `CoeffEq`), for the three
defining relations alone. -/
theorem heckeTwo_normalForm_unique (hp : HeckeParams) (f nf₁ nf₂ : AlgElement (HeckeGen 2) ℝ)
    (h₁ : ReducesToNF (heckeOrder 2) (heckeRewritingSystem 2 (by norm_num) hp) f nf₁)
    (h₂ : ReducesToNF (heckeOrder 2) (heckeRewritingSystem 2 (by norm_num) hp) f nf₂) :
    AlgElement.CoeffEq nf₁ nf₂ :=
  normal_form_unique (heckeOrder 2) (heckeRewritingSystem 2 (by norm_num) hp)
    (heckeRewritingSystem_two_isGrobnerShirshovBasis hp)
    (noQuasiZerosFree_of_generator ⟨0⟩) (heckeTwo_rules_lc_isUnit hp) f nf₁ nf₂ h₁ h₂

/-! ## §3  The six standard words -/

/-- `σ₀` and `σ₁` as letters of `HeckeGen 2`. -/
abbrev g₀ : HeckeGen 2 := ⟨0⟩
/-- See `g₀`. -/
abbrev g₁ : HeckeGen 2 := ⟨1⟩

/-- The six words irreducible for the three defining relations of `H₃(q)`. -/
def standardWordsTwo : List (Monomial (HeckeGen 2)) :=
  [[], [g₀], [g₁], [g₀, g₁], [g₁, g₀], [g₀, g₁, g₀]]

theorem standardWordsTwo_length : standardWordsTwo.length = 6 := rfl

theorem standardWordsTwo_nodup : standardWordsTwo.Nodup := by decide

/-- The leading monomials of the two-generator system are exactly
`σ₀σ₀`, `σ₁σ₁` and `σ₁σ₀σ₁`. -/
theorem heckeTwo_lm_cases (hp : HeckeParams) (r : ReductionRule (HeckeGen 2) ℝ)
    (hr : r ∈ (heckeRewritingSystem 2 (by norm_num) hp).rules) :
    r.lm (heckeOrder 2) = [g₀, g₀] ∨ r.lm (heckeOrder 2) = [g₁, g₁]
      ∨ r.lm (heckeOrder 2) = [g₁, g₀, g₁] := by
  rcases heckeRewritingSystem_lm_cases (n := 2) (by norm_num) hp r hr with
    ⟨i, h⟩ | ⟨i, j, hj, h⟩ | ⟨i, j, hj, h⟩
  · rw [h]
    fin_cases i
    · exact Or.inl rfl
    · exact Or.inr (Or.inl rfl)
  · rw [h]
    have hi : i = 0 := Fin.ext (by omega)
    have hj' : j = 1 := Fin.ext (by omega)
    subst hi hj'
    exact Or.inr (Or.inr rfl)
  · exact absurd hj (by omega)

theorem heckeRelation_mem_two (hp : HeckeParams) (i : Fin 2) :
    heckeRelation i hp ∈ (heckeRewritingSystem 2 (by norm_num) hp).rules := by
  simp only [heckeRewritingSystem, RewritingSystem.mem_ofList_rules, heckeRules,
    List.mem_append, List.mem_map, List.mem_finRange, true_and]
  exact Or.inl (Or.inl ⟨i, rfl⟩)

/-- Avoiding the three leading monomials pins a word to the six standard ones. -/
theorem avoid_iff_mem_standardWordsTwo (m : Monomial (HeckeGen 2)) :
    (¬ [g₀, g₀] <:+: m ∧ ¬ [g₁, g₁] <:+: m ∧ ¬ [g₁, g₀, g₁] <:+: m)
      ↔ m ∈ standardWordsTwo := by
  constructor
  · rintro ⟨h₁, h₂, h₃⟩
    match m with
    | [] => decide
    | [⟨a⟩] => revert h₁ h₂ h₃; revert a; decide
    | [⟨a⟩, ⟨b⟩] => revert h₁ h₂ h₃; revert a b; decide
    | [⟨a⟩, ⟨b⟩, ⟨c⟩] => revert h₁ h₂ h₃; revert a b c; decide
    | ⟨a⟩ :: ⟨b⟩ :: ⟨c⟩ :: ⟨d⟩ :: rest =>
      exfalso
      have hpre : [(⟨a⟩ : HeckeGen 2), ⟨b⟩, ⟨c⟩, ⟨d⟩] <:+:
          (⟨a⟩ :: ⟨b⟩ :: ⟨c⟩ :: ⟨d⟩ :: rest : Monomial (HeckeGen 2)) :=
        (List.prefix_append _ rest).isInfix
      have key : ∀ a b c d : Fin 2,
          [g₀, g₀] <:+: [(⟨a⟩ : HeckeGen 2), ⟨b⟩, ⟨c⟩, ⟨d⟩]
          ∨ [g₁, g₁] <:+: [(⟨a⟩ : HeckeGen 2), ⟨b⟩, ⟨c⟩, ⟨d⟩]
          ∨ [g₁, g₀, g₁] <:+: [(⟨a⟩ : HeckeGen 2), ⟨b⟩, ⟨c⟩, ⟨d⟩] := by decide
      rcases key a b c d with h | h | h
      · exact h₁ (h.trans hpre)
      · exact h₂ (h.trans hpre)
      · exact h₃ (h.trans hpre)
  · intro hm
    simp only [standardWordsTwo, List.mem_cons, List.mem_nil_iff, or_false] at hm
    rcases hm with rfl | rfl | rfl | rfl | rfl | rfl <;> decide

/-- **The irreducible words of `H₃(q)` are exactly the six standard words.**
A word is irreducible for the three defining relations iff it is one of
`1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀`. -/
theorem heckeTwo_irreducible_iff (hp : HeckeParams) (m : Monomial (HeckeGen 2)) :
    (∀ r ∈ (heckeRewritingSystem 2 (by norm_num) hp).rules, ¬ r.lm (heckeOrder 2) <:+: m)
      ↔ m ∈ standardWordsTwo := by
  rw [← avoid_iff_mem_standardWordsTwo]
  constructor
  · intro h
    refine ⟨?_, ?_, ?_⟩
    · have := h _ (heckeRelation_mem_two hp 0)
      rwa [heckeRelation_lm] at this
    · have := h _ (heckeRelation_mem_two hp 1)
      rwa [heckeRelation_lm] at this
    · have := h _ (yangBaxter_mem (n := 2) (by norm_num) hp (i := 0) (j := 1) rfl)
      rwa [yangBaxterRelation_lm 0 1 (by decide)] at this
  · rintro ⟨h₁, h₂, h₃⟩ r hr
    rcases heckeTwo_lm_cases hp r hr with h | h | h <;> rw [h] <;> assumption

/-- **Every element of the free algebra reduces, in `H₃(q)`'s three defining
relations, to a normal form supported on the six standard words.** -/
theorem heckeTwo_normalForm_exists_six (hp : HeckeParams) (f : AlgElement (HeckeGen 2) ℝ) :
    ∃ nf, ReducesToNF (heckeOrder 2) (heckeRewritingSystem 2 (by norm_num) hp) f nf
      ∧ ∀ m, nf.coeff m ≠ 0 → m ∈ standardWordsTwo := by
  obtain ⟨nf, hred⟩ := normal_form_exists (heckeOrder 2)
    (heckeRewritingSystem 2 (by norm_num) hp) (heckeTwo_rules_lc_isUnit hp) f
  exact ⟨nf, hred, fun m hm =>
    (heckeTwo_irreducible_iff hp m).mp fun r hr => hred.is_normal r hr m hm⟩

/-! ## §4  Three generators: the defining relations are not enough

`HeckeGS.lean` §4e refutes the uncompleted system at four generators, on the
word `σ₃σ₂σ₃σ₁`. The same overlap, shifted down by one index, already obstructs
three generators (`H₄(q)`): the Yang–Baxter rule `σ₂σ₁σ₂ → σ₁σ₂σ₁` and the
far-commutation rule `σ₂σ₀ → σ₀σ₂` overlap on `σ₂σ₁σ₂σ₀`, with S-polynomial
`σ₁σ₂σ₁σ₀ − σ₂σ₁σ₀σ₂`, and both words are irreducible. So two generators is
exactly where the defining relations stop being a Gröbner–Shirshov basis. -/

namespace NotAGSBasisThree

theorem hn3 : 0 < 3 := by norm_num

noncomputable def yb : ReductionRule (HeckeGen 3) ℝ := yangBaxterRelation 1 2
noncomputable def fc : ReductionRule (HeckeGen 3) ℝ := farCommRelation 2 0

theorem yb_lm : yb.lm (heckeOrder 3) = [⟨2⟩, ⟨1⟩, ⟨2⟩] :=
  yangBaxterRelation_lm 1 2 (by norm_num)

theorem fc_lm : fc.lm (heckeOrder 3) = [⟨2⟩, ⟨0⟩] :=
  farCommRelation_lm 2 0 (by norm_num)

/-- The overlap composition on the ambient word `σ₂σ₁σ₂σ₀`. -/
noncomputable def oc : OverlapComposition (HeckeGen 3) ℝ (heckeOrder 3) where
  rule₁ := yb
  rule₂ := fc
  left := [⟨2⟩, ⟨1⟩]
  overlap := [⟨2⟩]
  right := [⟨0⟩]
  lm₁_decomp := yb_lm
  lm₂_decomp := fc_lm
  overlap_nonempty := by simp

theorem yb_mem (hp : HeckeParams) : yb ∈ (heckeRewritingSystem 3 hn3 hp).rules :=
  yangBaxter_mem hn3 hp (i := 1) (j := 2) rfl

theorem fc_mem (hp : HeckeParams) : fc ∈ (heckeRewritingSystem 3 hn3 hp).rules := by
  refine List.mem_append_right _ ?_
  refine List.mem_flatMap.mpr ⟨2, List.mem_finRange 2, ?_⟩
  exact List.mem_filterMap.mpr ⟨0, List.mem_finRange 0, rfl⟩

def w₁ : Monomial (HeckeGen 3) := [⟨1⟩, ⟨2⟩, ⟨1⟩, ⟨0⟩]
def w₂ : Monomial (HeckeGen 3) := [⟨2⟩, ⟨1⟩, ⟨0⟩, ⟨2⟩]

theorem yb_lc : yb.lc (heckeOrder 3) = -1 := by
  show yb.relation.coeff (yb.lm (heckeOrder 3)) = -1
  rw [yb_lm]
  simp [yb, yangBaxterRelation, AlgElement.ofTerms_coeff]

theorem fc_lc : fc.lc (heckeOrder 3) = 1 := by
  show fc.relation.coeff (fc.lm (heckeOrder 3)) = 1
  rw [fc_lm]
  simp [fc, farCommRelation, AlgElement.ofTerms_coeff]

theorem spoly_coeff_w₁ : oc.spoly.coeff w₁ = 1 := by
  have h1 : w₁ = [] ++ [⟨1⟩, ⟨2⟩, ⟨1⟩] ++ [⟨0⟩] := by simp [w₁]
  have h2 : (AlgElement.contextMul [⟨2⟩, ⟨1⟩] fc.relation []).coeff w₁ = 0 := by
    refine AlgElement.contextMul_coeff_of_not_shape _ (fun w => ?_)
    simp [w₁]
  simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  show fc.lc (heckeOrder 3) * (AlgElement.contextMul [] yb.relation [⟨0⟩]).coeff w₁
      - yb.lc (heckeOrder 3)
        * (AlgElement.contextMul [⟨2⟩, ⟨1⟩] fc.relation []).coeff w₁ = 1
  rw [h2, fc_lc, yb_lc, h1, AlgElement.contextMul_coeff_middle]
  simp [yb, yangBaxterRelation, AlgElement.ofTerms_coeff]

theorem spoly_support (m : Monomial (HeckeGen 3)) (h : oc.spoly.coeff m ≠ 0) :
    m = w₁ ∨ m = w₂ ∨ m = oc.word := by
  by_cases h1 : (AlgElement.contextMul [] yb.relation [⟨0⟩]).coeff m ≠ 0
  · obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape h1
    have : w = [⟨1⟩, ⟨2⟩, ⟨1⟩] ∨ w = [⟨2⟩, ⟨1⟩, ⟨2⟩] := by
      have := AlgElement.mem_support_of_coeff_ne_zero hwne
      simpa [yb, yangBaxterRelation, AlgElement.ofTerms] using this
    rcases this with rfl | rfl
    · exact Or.inl (by simpa [w₁] using hw)
    · exact Or.inr (Or.inr (by simpa [OverlapComposition.word, oc] using hw))
  · push_neg at h1
    have h2 : (AlgElement.contextMul [⟨2⟩, ⟨1⟩] fc.relation []).coeff m ≠ 0 := by
      intro h2
      apply h
      simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
      show fc.lc (heckeOrder 3) * (AlgElement.contextMul [] yb.relation [⟨0⟩]).coeff m
          - yb.lc (heckeOrder 3)
            * (AlgElement.contextMul [⟨2⟩, ⟨1⟩] fc.relation []).coeff m = 0
      rw [h1, h2]
      ring
    obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape h2
    have : w = [⟨2⟩, ⟨0⟩] ∨ w = [⟨0⟩, ⟨2⟩] := by
      have := AlgElement.mem_support_of_coeff_ne_zero hwne
      simpa [fc, farCommRelation, AlgElement.ofTerms] using this
    rcases this with rfl | rfl
    · exact Or.inr (Or.inr (by simpa [OverlapComposition.word, oc] using hw))
    · exact Or.inr (Or.inl (by simpa [w₂] using hw))

theorem no_rule_infix (hp : HeckeParams) (r : ReductionRule (HeckeGen 3) ℝ)
    (hr : r ∈ (heckeRewritingSystem 3 hn3 hp).rules) (w : Monomial (HeckeGen 3))
    (hw : w = w₁ ∨ w = w₂) : ¬ (r.lm (heckeOrder 3) <:+: w) := by
  have sq : ∀ i : Fin 3, ¬ (([⟨i⟩, ⟨i⟩] : Monomial (HeckeGen 3)) <:+: w₁)
      ∧ ¬ (([⟨i⟩, ⟨i⟩] : Monomial (HeckeGen 3)) <:+: w₂) := by decide
  have ybw : ∀ i j : Fin 3, j.val = i.val + 1 →
      ¬ (([⟨j⟩, ⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 3)) <:+: w₁)
      ∧ ¬ (([⟨j⟩, ⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 3)) <:+: w₂) := by decide
  have fcw : ∀ i j : Fin 3, j.val + 1 < i.val →
      ¬ (([⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 3)) <:+: w₁)
      ∧ ¬ (([⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 3)) <:+: w₂) := by decide
  rcases heckeRewritingSystem_lm_cases hn3 hp r hr with
    ⟨i, h⟩ | ⟨i, j, hij, h⟩ | ⟨i, j, hij, h⟩ <;> rw [h] <;> rcases hw with rfl | rfl
  · exact (sq i).1
  · exact (sq i).2
  · exact (ybw i j hij).1
  · exact (ybw i j hij).2
  · exact (fcw i j hij).1
  · exact (fcw i j hij).2

theorem spoly_isNormalForm (hp : HeckeParams) :
    isNormalForm (heckeOrder 3) (heckeRewritingSystem 3 hn3 hp) oc.spoly := by
  intro r hr m hm
  rcases spoly_support m hm with rfl | rfl | rfl
  · exact no_rule_infix hp r hr _ (Or.inl rfl)
  · exact no_rule_infix hp r hr _ (Or.inr rfl)
  · exact absurd (OverlapComposition.spoly_coeff_word_eq_zero oc) hm

/-- **The defining relations of `H₄(q)` are not a Gröbner–Shirshov basis.** -/
theorem hecke_not_gs_basis_three (hp : HeckeParams) :
    ¬ IsGrobnerShirshovBasis (HeckeGen 3) ℝ (heckeOrder 3)
        (heckeRewritingSystem 3 hn3 hp) := by
  intro hgs
  obtain ⟨nf, ⟨hred, -⟩, hzero⟩ := hgs.overlap_resolves oc (yb_mem hp) (fc_mem hp)
  have hnfeq : nf = oc.spoly :=
    MultiStepReduction.eq_of_isNormalForm (spoly_isNormalForm hp) hred
  subst hnfeq
  have h0 := hzero w₁
  rw [spoly_coeff_w₁] at h0
  exact one_ne_zero h0

end NotAGSBasisThree

/-! ### Every `n ≥ 3`

The same overlap lives on the first three generators of any `HeckeGen n` with
`3 ≤ n`, and the irreducibility checks reduce to statements about the index
words `[1,2,1,0]` and `[2,1,0,2]` in `ℕ`: a letter of an infix is a letter of the
word, so only indices `0, 1, 2` can occur. -/

namespace NotAGSBasisGe3

variable {n : ℕ} (h3 : 3 ≤ n)

def a₀ : Fin n := ⟨0, by omega⟩
def a₁ : Fin n := ⟨1, by omega⟩
def a₂ : Fin n := ⟨2, by omega⟩

theorem hn (h : 3 ≤ n) : 0 < n := by omega

noncomputable def yb : ReductionRule (HeckeGen n) ℝ := yangBaxterRelation (a₁ h3) (a₂ h3)
noncomputable def fc : ReductionRule (HeckeGen n) ℝ := farCommRelation (a₂ h3) (a₀ h3)

theorem yb_lm : (yb h3).lm (heckeOrder n) = [⟨a₂ h3⟩, ⟨a₁ h3⟩, ⟨a₂ h3⟩] :=
  yangBaxterRelation_lm _ _ (by simp [a₁, a₂])

theorem fc_lm : (fc h3).lm (heckeOrder n) = [⟨a₂ h3⟩, ⟨a₀ h3⟩] :=
  farCommRelation_lm _ _ (by simp [a₀, a₂])

noncomputable def oc : OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := yb h3
  rule₂ := fc h3
  left := [⟨a₂ h3⟩, ⟨a₁ h3⟩]
  overlap := [⟨a₂ h3⟩]
  right := [⟨a₀ h3⟩]
  lm₁_decomp := yb_lm h3
  lm₂_decomp := fc_lm h3
  overlap_nonempty := by simp

theorem yb_mem (hp : HeckeParams) : yb h3 ∈ (heckeRewritingSystem n (hn h3) hp).rules :=
  yangBaxter_mem (hn h3) hp (by simp [a₁, a₂])

theorem fc_mem (hp : HeckeParams) : fc h3 ∈ (heckeRewritingSystem n (hn h3) hp).rules := by
  refine List.mem_append_right _ ?_
  refine List.mem_flatMap.mpr ⟨a₂ h3, List.mem_finRange _, ?_⟩
  exact List.mem_filterMap.mpr ⟨a₀ h3, List.mem_finRange _, by simp [a₀, a₂, fc]⟩

def w₁ : Monomial (HeckeGen n) := [⟨a₁ h3⟩, ⟨a₂ h3⟩, ⟨a₁ h3⟩, ⟨a₀ h3⟩]
def w₂ : Monomial (HeckeGen n) := [⟨a₂ h3⟩, ⟨a₁ h3⟩, ⟨a₀ h3⟩, ⟨a₂ h3⟩]

theorem a_ne : a₀ h3 ≠ a₁ h3 ∧ a₀ h3 ≠ a₂ h3 ∧ a₁ h3 ≠ a₂ h3 := by
  refine ⟨?_, ?_, ?_⟩ <;> intro h <;> simp [a₀, a₁, a₂, Fin.ext_iff] at h

theorem yb_lc : (yb h3).lc (heckeOrder n) = -1 := by
  show (yb h3).relation.coeff ((yb h3).lm (heckeOrder n)) = -1
  rw [yb_lm]
  have := a_ne h3
  simp [yb, yangBaxterRelation, AlgElement.ofTerms_coeff, this.2.2, this.2.2.symm]

theorem fc_lc : (fc h3).lc (heckeOrder n) = 1 := by
  show (fc h3).relation.coeff ((fc h3).lm (heckeOrder n)) = 1
  rw [fc_lm]
  have := a_ne h3
  simp [fc, farCommRelation, AlgElement.ofTerms_coeff, this.2.1, this.2.1.symm]

theorem spoly_coeff_w₁ : (oc h3).spoly.coeff (w₁ h3) = 1 := by
  have hne := a_ne h3
  have h1 : w₁ h3 = [] ++ [⟨a₁ h3⟩, ⟨a₂ h3⟩, ⟨a₁ h3⟩] ++ [⟨a₀ h3⟩] := by simp [w₁]
  have h2 : (AlgElement.contextMul [⟨a₂ h3⟩, ⟨a₁ h3⟩] (fc h3).relation []).coeff (w₁ h3) = 0 := by
    refine AlgElement.contextMul_coeff_of_not_shape _ (fun w => ?_)
    simp [w₁, hne.2.2]
  simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  show (fc h3).lc (heckeOrder n) * (AlgElement.contextMul [] (yb h3).relation [⟨a₀ h3⟩]).coeff (w₁ h3)
      - (yb h3).lc (heckeOrder n)
        * (AlgElement.contextMul [⟨a₂ h3⟩, ⟨a₁ h3⟩] (fc h3).relation []).coeff (w₁ h3) = 1
  rw [h2, fc_lc, yb_lc, h1, AlgElement.contextMul_coeff_middle]
  simp [yb, yangBaxterRelation, AlgElement.ofTerms_coeff, hne.2.2, hne.2.2.symm]

theorem spoly_support (m : Monomial (HeckeGen n)) (h : (oc h3).spoly.coeff m ≠ 0) :
    m = w₁ h3 ∨ m = w₂ h3 ∨ m = (oc h3).word := by
  by_cases h1 : (AlgElement.contextMul [] (yb h3).relation [⟨a₀ h3⟩]).coeff m ≠ 0
  · obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape h1
    have : w = [⟨a₁ h3⟩, ⟨a₂ h3⟩, ⟨a₁ h3⟩] ∨ w = [⟨a₂ h3⟩, ⟨a₁ h3⟩, ⟨a₂ h3⟩] := by
      have := AlgElement.mem_support_of_coeff_ne_zero hwne
      simpa [yb, yangBaxterRelation, AlgElement.ofTerms] using this
    rcases this with rfl | rfl
    · exact Or.inl (by simpa [w₁] using hw)
    · exact Or.inr (Or.inr (by simpa [OverlapComposition.word, oc] using hw))
  · push_neg at h1
    have h2 : (AlgElement.contextMul [⟨a₂ h3⟩, ⟨a₁ h3⟩] (fc h3).relation []).coeff m ≠ 0 := by
      intro h2
      apply h
      simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
      show (fc h3).lc (heckeOrder n)
            * (AlgElement.contextMul [] (yb h3).relation [⟨a₀ h3⟩]).coeff m
          - (yb h3).lc (heckeOrder n)
            * (AlgElement.contextMul [⟨a₂ h3⟩, ⟨a₁ h3⟩] (fc h3).relation []).coeff m = 0
      rw [h1, h2]
      ring
    obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape h2
    have : w = [⟨a₂ h3⟩, ⟨a₀ h3⟩] ∨ w = [⟨a₀ h3⟩, ⟨a₂ h3⟩] := by
      have := AlgElement.mem_support_of_coeff_ne_zero hwne
      simpa [fc, farCommRelation, AlgElement.ofTerms] using this
    rcases this with rfl | rfl
    · exact Or.inr (Or.inr (by simpa [OverlapComposition.word, oc] using hw))
    · exact Or.inr (Or.inl (by simpa [w₂] using hw))

/-- Index words: the letters of `w₁`, `w₂` as natural numbers. -/
theorem idx_w₁ : (w₁ h3).map (fun g => g.index.val) = [1, 2, 1, 0] := rfl
theorem idx_w₂ : (w₂ h3).map (fun g => g.index.val) = [2, 1, 0, 2] := rfl

/-- An infix pattern in `ℕ` whose letters are bounded by the word's letters. -/
theorem bounded_of_infix {l w : List ℕ} (h : l <:+: w) (hw : ∀ x ∈ w, x ≤ 2) :
    ∀ x ∈ l, x ≤ 2 := fun x hx => hw x (h.subset hx)

theorem no_rule_infix (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeRewritingSystem n (hn h3) hp).rules) (w : Monomial (HeckeGen n))
    (hw : w = w₁ h3 ∨ w = w₂ h3) : ¬ (r.lm (heckeOrder n) <:+: w) := by
  have hidx : w.map (fun g => g.index.val) = [1, 2, 1, 0]
      ∨ w.map (fun g => g.index.val) = [2, 1, 0, 2] := by
    rcases hw with rfl | rfl
    · exact Or.inl (idx_w₁ h3)
    · exact Or.inr (idx_w₂ h3)
  intro hinf
  have hmap := hinf.map (fun g : HeckeGen n => g.index.val)
  have hb : ∀ x ∈ w.map (fun g => g.index.val), x ≤ 2 := by
    rcases hidx with h | h <;> rw [h] <;> decide
  rcases heckeRewritingSystem_lm_cases (hn h3) hp r hr with
    ⟨i, h⟩ | ⟨i, j, hij, h⟩ | ⟨i, j, hij, h⟩ <;> rw [h] at hmap <;>
    simp only [List.map_cons, List.map_nil] at hmap
  · have hi := bounded_of_infix hmap hb i.val (by simp)
    generalize i.val = x at hmap hi
    interval_cases x <;> rcases hidx with h | h <;> rw [h] at hmap <;> revert hmap <;> decide
  · have hj := bounded_of_infix hmap hb j.val (by simp)
    rw [hij] at hmap hj
    generalize i.val = x at hmap hj
    have : x ≤ 1 := by omega
    interval_cases x <;> rcases hidx with h | h <;> rw [h] at hmap <;> revert hmap <;> decide
  · have hi := bounded_of_infix hmap hb i.val (by simp)
    have hj := bounded_of_infix hmap hb j.val (by simp)
    generalize i.val = x at hmap hi hij
    generalize j.val = y at hmap hj hij
    interval_cases x <;> interval_cases y <;> (try omega) <;>
      rcases hidx with h | h <;> rw [h] at hmap <;> revert hmap <;> decide

theorem spoly_isNormalForm (hp : HeckeParams) :
    isNormalForm (heckeOrder n) (heckeRewritingSystem n (hn h3) hp) (oc h3).spoly := by
  intro r hr m hm
  rcases spoly_support h3 m hm with rfl | rfl | rfl
  · exact no_rule_infix h3 hp r hr _ (Or.inl rfl)
  · exact no_rule_infix h3 hp r hr _ (Or.inr rfl)
  · exact absurd (OverlapComposition.spoly_coeff_word_eq_zero (oc h3)) hm

/-- **With three or more generators the defining Hecke relations are not a
Gröbner–Shirshov basis.** -/
theorem hecke_not_gs_basis_of_three_le (hp : HeckeParams) :
    ¬ IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n)
        (heckeRewritingSystem n (hn h3) hp) := by
  intro hgs
  obtain ⟨nf, ⟨hred, -⟩, hzero⟩ :=
    hgs.overlap_resolves (oc h3) (yb_mem h3 hp) (fc_mem h3 hp)
  have hnfeq : nf = (oc h3).spoly :=
    MultiStepReduction.eq_of_isNormalForm (spoly_isNormalForm h3 hp) hred
  subst hnfeq
  have h0 := hzero (w₁ h3)
  rw [spoly_coeff_w₁] at h0
  exact one_ne_zero h0

end NotAGSBasisGe3

/-- **The defining Hecke relations are a Gröbner–Shirshov basis exactly when
there are at most two generators**, i.e. for `H₂(q)` and `H₃(q)` and for no
larger Hecke algebra of type A. -/
theorem heckeRewritingSystem_isGrobnerShirshovBasis_iff {n : ℕ} (hn : 0 < n)
    (hp : HeckeParams) :
    IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n) (heckeRewritingSystem n hn hp)
      ↔ n ≤ 2 := by
  constructor
  · intro h
    by_contra hc
    exact NotAGSBasisGe3.hecke_not_gs_basis_of_three_le (n := n) (by omega) hp h
  · intro h2
    exact heckeRewritingSystem_isGrobnerShirshovBasis_of_le_two hn h2 hp

end Hecke

end UGB.GrobnerShirshov
