import UGB.GrobnerShirshov.DiamondLemma
import UGB.GrobnerShirshov.NormalFormBasisProof
import Mathlib.Tactic.Module

set_option linter.unusedSectionVars false

/-!
# Quadratic rewriting systems: the diamond condition is the triple-overlap condition

A **quadratic rewriting system** has one rule per pair `(a, b)` in a set `P` of
pairs of generators:

    a b  ↦  R(a, b),

where every monomial of `R(a, b)` lies strictly below the word `a b`. It
contains the splay systems of `SplayPBW.lean` (`R(a,b) = cf(a,b) · b a + π(a,b)`)
and also rules that *shorten* a word, such as the multiplication
`e(a) e(b) ↦ μ(a, b)` of a block algebra whose basis elements are letters.
This is the shape of the presentation in Thm. 1.9 of [leitner2006]: within
one commutative formal subgroup two letters multiply to a combination of
letters of the same block, and across blocks two letters commute up to a
correction lying lower in the filtration.

**What is proved here.**

* `rule_lm`, `rule_lc` — each rule leads on `a b` with coefficient `1`.
* `inclusion_trivial` — inclusions are vacuous (every leading word has length 2
  and determines its rule).
* `compositionsTrivial_iff` — **the system has trivial compositions iff, for
  every chain `(a, b), (b, c) ∈ P`,**

      a · R(b, c) − R(a, b) · c  ∈  JM [a, b, c],

  the span of the rules placed strictly below `a b c` (the *triple-overlap
  condition*; these are the ambiguities `S1`–`S3` of [leitner2006, proof of
  Thm. 1.9]).
* `normalFormBasis` — under the triple-overlap condition the words containing
  no `a b` with `(a, b) ∈ P` are a `k`-basis of the quotient, by the proved
  diamond lemma.

No analytic argument is used.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Thm. 1.9 (proof, ambiguities S1–S3).
-/

namespace UGB.GrobnerShirshov.Quadratic

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond AlgElement

universe u v

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]

/-- **Quadratic data**: the pairs that carry a rule, the right-hand sides, and
    the filtration hypothesis. -/
structure QuadData (G : Type u) [DecidableEq G] (k : Type v) [CommRing k]
    (ord : AdmissibleOrder G) where
  /-- The pairs `(a, b)` that carry a rule `a b ↦ R(a, b)`. -/
  pairs : Set (G × G)
  /-- At least one rule. -/
  pairs_ne : pairs.Nonempty
  /-- The right-hand side of each rule. -/
  R : G → G → MA G k
  /-- **Filtration**: every monomial of `R(a, b)` is below `a b`. -/
  R_lt : ∀ p ∈ pairs, ∀ w ∈ (R p.1 p.2).support,
    ord.lt (FreeMonoid.toList w) [p.1, p.2]

variable {ord : AdmissibleOrder G}

namespace QuadData

variable (d : QuadData G k ord)

/-- The relation `a b − R(a, b)` of a pair, in the monoid algebra. -/
noncomputable def relMA (a b : G) : MA G k := ofW [a, b] - d.R a b

/-- The **overlap element** of a chain `(a, b), (b, c)`: `a·R(b,c) − R(a,b)·c`. -/
noncomputable def overlapElt (a b c : G) : MA G k := ofW [a] * d.R b c - d.R a b * ofW [c]

theorem R_apply_self {p : G × G} (hp : p ∈ d.pairs) :
    (d.R p.1 p.2) (FreeMonoid.ofList [p.1, p.2]) = 0 := by
  by_contra h
  have := d.R_lt p hp _ (Finsupp.mem_support_iff.mpr h)
  rw [FreeMonoid.toList_ofList] at this
  exact ord.irrefl _ this

theorem relMA_apply_self {p : G × G} (hp : p ∈ d.pairs) :
    d.relMA p.1 p.2 (FreeMonoid.ofList [p.1, p.2]) = 1 := by
  rw [relMA, Finsupp.sub_apply, ofW_apply, if_pos rfl, d.R_apply_self hp, sub_zero]

variable [Nontrivial k]

/-- The rule of a pair. -/
noncomputable def rule (p : d.pairs) : ReductionRule G k where
  relation := ofMA (d.relMA p.1.1 p.1.2)
  nonzero := by
    refine ⟨[p.1.1, p.1.2], Finset.mem_image.mpr ⟨FreeMonoid.ofList [p.1.1, p.1.2], ?_, rfl⟩⟩
    rw [Finsupp.mem_support_iff, d.relMA_apply_self p.2]
    exact one_ne_zero

/-- The quadratic rewriting system. -/
noncomputable def sys : RewritingSystem G k where
  rules := Set.range d.rule
  nonempty := by
    obtain ⟨p, hp⟩ := d.pairs_ne
    exact ⟨_, ⟨⟨p, hp⟩, rfl⟩⟩

theorem mem_sys {r : ReductionRule G k} : r ∈ d.sys.rules ↔ ∃ p, d.rule p = r := Iff.rfl

theorem rule_mem (p : d.pairs) : d.rule p ∈ d.sys.rules := ⟨p, rfl⟩

theorem rule_lm (p : d.pairs) : (d.rule p).lm ord = [p.1.1, p.1.2] := by
  apply leadingMonomial_eq_of_max
  · refine Finset.mem_image.mpr ⟨FreeMonoid.ofList [p.1.1, p.1.2], ?_, rfl⟩
    rw [Finsupp.mem_support_iff, d.relMA_apply_self p.2]; exact one_ne_zero
  · intro m hm hne
    obtain ⟨w, hw, rfl⟩ := Finset.mem_image.mp hm
    rw [Finsupp.mem_support_iff, ← FreeMonoid.ofList_toList w] at hw
    set m := FreeMonoid.toList w
    rw [relMA, Finsupp.sub_apply, ofW_apply, if_neg (Ne.symm hne), zero_sub, neg_ne_zero] at hw
    have := d.R_lt _ p.2 (FreeMonoid.ofList m) (Finsupp.mem_support_iff.mpr hw)
    rwa [FreeMonoid.toList_ofList] at this

theorem rule_lc (p : d.pairs) : (d.rule p).lc ord = 1 := by
  show (ofMA (d.relMA p.1.1 p.1.2)).coeff ((d.rule p).lm ord) = 1
  rw [d.rule_lm]
  exact d.relMA_apply_self p.2

theorem lc_isUnit : ∀ r ∈ d.sys.rules, IsUnit (r.lc ord) := by
  rintro r ⟨p, rfl⟩
  rw [d.rule_lc]; exact isUnit_one

theorem toMA_rule (p : d.pairs) : toMA (d.rule p).relation = d.relMA p.1.1 p.1.2 := toMA_ofMA _

theorem rule_eq_of_lm {p q : d.pairs} (h : (d.rule p).lm ord = (d.rule q).lm ord) :
    d.rule p = d.rule q := by
  rw [d.rule_lm, d.rule_lm] at h
  obtain ⟨h1, h2⟩ := List.cons.inj h
  obtain ⟨h2, -⟩ := List.cons.inj h2
  have : p = q := Subtype.ext (Prod.ext h1 h2)
  rw [this]

/-- A rule of the system, placed in context below `v`, lies in `JM v`. -/
theorem jm_rule {v : Monomial G} (p : d.pairs) (x y : Monomial G)
    (h : ord.lt (x ++ [p.1.1, p.1.2] ++ y) v) :
    JM ord d.sys v (ofW x * d.relMA p.1.1 p.1.2 * ofW y) := by
  rw [← d.toMA_rule]
  refine JM.gen ⟨d.rule p, x, y⟩ (d.rule_mem p) ?_
  show ord.lt (x ++ (d.rule p).lm ord ++ y) v
  rwa [d.rule_lm]

theorem lm_length (r : ReductionRule G k) (hr : r ∈ d.sys.rules) : (r.lm ord).length = 2 := by
  obtain ⟨p, rfl⟩ := hr
  rw [d.rule_lm]; rfl

theorem rule_eq_of_mem_lm {r₁ r₂ : ReductionRule G k} (h₁ : r₁ ∈ d.sys.rules)
    (h₂ : r₂ ∈ d.sys.rules) (h : r₁.lm ord = r₂.lm ord) : r₁ = r₂ := by
  obtain ⟨p, rfl⟩ := h₁
  obtain ⟨q, rfl⟩ := h₂
  exact d.rule_eq_of_lm h

/-- **Inclusions are vacuous.** -/
theorem inclusion_trivial (ic : InclusionComposition G k ord) (h₁ : ic.inner ∈ d.sys.rules)
    (h₂ : ic.outer ∈ d.sys.rules) : JM ord d.sys (ic.outer.lm ord) (toMA ic.spoly) := by
  have hlen := congrArg List.length ic.decomposition
  simp only [List.length_append, d.lm_length _ h₁, d.lm_length _ h₂] at hlen
  have hl : ic.left = [] := List.eq_nil_of_length_eq_zero (by omega)
  have hr : ic.right = [] := List.eq_nil_of_length_eq_zero (by omega)
  have heq : ic.inner = ic.outer :=
    d.rule_eq_of_mem_lm h₁ h₂ (by have := ic.decomposition; rw [hl, hr] at this; simpa using this.symm)
  rw [toMA_of_isZero (ic.spoly_isZero_of_self heq)]
  exact JM.zero

/-- The S-polynomial of a genuine overlap `(a,b)`, `(b,c)` is the overlap element. -/
theorem toMA_spoly_chain (oc : OverlapComposition G k ord) (h₁ : oc.rule₁ ∈ d.sys.rules)
    (h₂ : oc.rule₂ ∈ d.sys.rules) (a b c : G) (hl : oc.left = [a]) (ho : oc.overlap = [b])
    (hr : oc.right = [c]) :
    ∃ (_ : (a, b) ∈ d.pairs) (_ : (b, c) ∈ d.pairs),
      toMA oc.spoly = d.overlapElt a b c := by
  obtain ⟨p, hp⟩ := h₁
  obtain ⟨q, hq⟩ := h₂
  have e1 := oc.lm₁_decomp
  have e2 := oc.lm₂_decomp
  rw [← hp, d.rule_lm, hl, ho] at e1
  rw [← hq, d.rule_lm, ho, hr] at e2
  simp only [List.cons_append, List.nil_append, List.cons.injEq, and_true] at e1 e2
  obtain ⟨⟨p1, p2⟩, hpm⟩ := p
  obtain ⟨⟨q1, q2⟩, hqm⟩ := q
  simp only at e1 e2
  obtain ⟨rfl, rfl⟩ := e1
  obtain ⟨rfl, rfl⟩ := e2
  refine ⟨hpm, hqm, ?_⟩
  rw [toMA_spoly_ov, ← hp, ← hq, d.rule_lc, d.rule_lc, d.toMA_rule, d.toMA_rule, hl, hr,
    one_smul, one_smul]
  simp only [relMA, overlapElt, sub_mul, mul_sub, ← ofW_append, List.cons_append,
    List.nil_append]
  abel

/-- The shape of an overlap of two length-`2` words. -/
theorem overlap_cases (oc : OverlapComposition G k ord) (h₁ : oc.rule₁ ∈ d.sys.rules)
    (h₂ : oc.rule₂ ∈ d.sys.rules) :
    (oc.left = [] ∧ oc.right = [] ∧ oc.rule₁ = oc.rule₂) ∨
      ∃ a b c : G, oc.left = [a] ∧ oc.overlap = [b] ∧ oc.right = [c] := by
  have l1 := congrArg List.length oc.lm₁_decomp
  have l2 := congrArg List.length oc.lm₂_decomp
  rw [d.lm_length _ h₁, List.length_append] at l1
  rw [d.lm_length _ h₂, List.length_append] at l2
  have hon : oc.overlap.length ≠ 0 := fun h => oc.overlap_nonempty (List.eq_nil_of_length_eq_zero h)
  by_cases h2 : oc.overlap.length = 2
  · left
    have hl : oc.left = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hr : oc.right = [] := List.eq_nil_of_length_eq_zero (by omega)
    refine ⟨hl, hr, d.rule_eq_of_mem_lm h₁ h₂ ?_⟩
    rw [oc.lm₁_decomp, oc.lm₂_decomp, hl, hr]; simp
  · right
    obtain ⟨a, ha⟩ := List.length_eq_one_iff.mp (show oc.left.length = 1 by omega)
    obtain ⟨b, hb⟩ := List.length_eq_one_iff.mp (show oc.overlap.length = 1 by omega)
    obtain ⟨c, hc⟩ := List.length_eq_one_iff.mp (show oc.right.length = 1 by omega)
    exact ⟨a, b, c, ha, hb, hc⟩

/-- The **triple-overlap condition**: for every chain `(a, b), (b, c) ∈ P`, the
    overlap element lies in the span of the rules placed below `a b c`. -/
def OverlapCondition : Prop :=
  ∀ a b c : G, (a, b) ∈ d.pairs → (b, c) ∈ d.pairs → JM ord d.sys [a, b, c] (d.overlapElt a b c)

/-- **The composition condition for a quadratic system is the triple-overlap
    condition.** -/
theorem compositionsTrivial_iff : CompositionsTrivial ord d.sys ↔ d.OverlapCondition := by
  constructor
  · intro ht a b c hab hbc
    let oc : OverlapComposition G k ord :=
      { rule₁ := d.rule ⟨(a, b), hab⟩, rule₂ := d.rule ⟨(b, c), hbc⟩,
        left := [a], overlap := [b], right := [c],
        lm₁_decomp := by rw [d.rule_lm]; rfl,
        lm₂_decomp := by rw [d.rule_lm]; rfl,
        overlap_nonempty := by simp }
    have hJ := ht.overlap oc (d.rule_mem _) (d.rule_mem _)
    obtain ⟨_, _, he⟩ := d.toMA_spoly_chain oc (d.rule_mem _) (d.rule_mem _) a b c rfl rfl rfl
    have hw : oc.word = [a, b, c] := rfl
    rw [he, hw] at hJ
    exact hJ
  · intro hov
    refine ⟨fun oc h₁ h₂ => ?_, fun ic h₁ h₂ => d.inclusion_trivial ic h₁ h₂⟩
    rcases d.overlap_cases oc h₁ h₂ with ⟨hl, hr, he⟩ | ⟨a, b, c, hl, ho, hr⟩
    · rw [toMA_of_isZero (oc.spoly_isZero_of_self he hl hr)]
      exact JM.zero
    · obtain ⟨hab, hbc, he⟩ := d.toMA_spoly_chain oc h₁ h₂ a b c hl ho hr
      have hw : oc.word = [a, b, c] := by
        simp [OverlapComposition.word, hl, ho, hr]
      rw [he, hw]
      exact hov a b c hab hbc

/-- A quadratic system is a Gröbner–Shirshov basis iff the triple-overlap condition holds. -/
theorem isGrobnerShirshovBasis_iff :
    IsGrobnerShirshovBasis G k ord d.sys ↔ d.OverlapCondition :=
  (isGrobnerShirshovBasis_iff_compositionsTrivial d.lc_isUnit).trans d.compositionsTrivial_iff

/-- The normal-form monomials are the words containing no `a b` with `(a, b) ∈ P`. -/
theorem normalFormMonomial_iff (m : Monomial G) :
    NormalFormMonomial ord d.sys m ↔ ∀ p ∈ d.pairs, ¬ [p.1, p.2] <:+: m := by
  constructor
  · intro h p hp
    have := h _ (d.rule_mem ⟨p, hp⟩)
    rwa [d.rule_lm] at this
  · rintro h r ⟨p, rfl⟩
    rw [d.rule_lm]
    exact h p.1 p.2

/-- **PBW for a quadratic system.** Under the triple-overlap condition, the
    classes of the normal words form a `k`-basis of the quotient. -/
theorem normalFormBasis [DecidableEq k] (h : d.OverlapCondition) :
    NormalFormBasis ord d.sys :=
  NFBasis.normalFormBasis_of_isGrobnerShirshovBasis (d.isGrobnerShirshovBasis_iff.mpr h)
    d.lc_isUnit

end QuadData

end UGB.GrobnerShirshov.Quadratic
