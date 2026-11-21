import UGB.GrobnerShirshov.DiamondLemma
import UGB.GrobnerShirshov.NormalFormBasisProof

set_option linter.unusedSectionVars false

/-!
# Splay rewriting systems and their compositions (PBW, Gröbner–Shirshov route)

A **splay rewriting system** has one rule per ordered pair `(a, b)` of
generators with `a ≫ b`:

    a b  ↦  b a + π(a, b),

where `π(a, b)` is an arbitrary element of the free algebra whose monomials all
lie strictly below `a b` in the admissible order. Commutative polynomial blocks
are the case `π = 0`; a Lie algebra is the case where `π(a, b)` is the linear
bracket `Σ_e c^e_{ab} e`; the splay algebras of [leitner2006] are the case where
`π` is the given strong-filtration correction.

**What is proved here.**

* `rule_lm`, `rule_lc` — each rule leads on `a b` with coefficient `1`
  (§1). This is where the filtration hypothesis `π(a, b) < a b` enters.
* `spoly_overlap_eq` — the overlap of the rules for `(a, b)` and `(b, c)`
  is, modulo the span below `a b c`, exactly the *Jacobi element*

      J(a, b, c) = a π(b,c) − π(b,c) a + c π(a,b) − π(a,b) c + π(a,c) b − b π(a,c).

* `compositionsTrivial_iff` — **the composition condition for a splay
  system is the Jacobi condition**: the system has trivial compositions
  (equivalently, is a Gröbner–Shirshov basis, `isGrobnerShirshovBasis_iff`)
  if and only if `J(a, b, c)` lies in the span below `a b c` for every chain
  `a ≫ b ≫ c`. Inclusions and the remaining overlap shapes are vacuous because
  every leading monomial has length `2` and determines its rule.

* `normalFormBasis` — under the Jacobi condition the sorted words are a
  `k`-basis of the quotient (`NormalFormBasis`), via the proved diamond lemma.

So the PBW theorem for a splay system reduces to one statement per triple of
generators. `LiePBW.lean` discharges it for a Lie algebra with a finite ordered
basis, from the Jacobi identity.

No analytic argument is used: this is Bergman's diamond lemma
(`UGB.GrobnerShirshov.Diamond`) applied to an explicit rewriting system.
-/

namespace UGB.GrobnerShirshov.Splay

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond AlgElement

universe u v

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]

/-- **Splay data**: the pairs that carry a rule, the correction `π`, and the
    three hypotheses that make the rules lead where they should. -/
structure SplayData (G : Type u) [DecidableEq G] (k : Type v) [CommRing k]
    (ord : AdmissibleOrder G) where
  /-- The pairs `(a, b)`, `a ≫ b`, that carry a rule `a b ↦ b a + π(a,b)`. -/
  pairs : List (G × G)
  /-- At least one rule. -/
  pairs_ne : pairs ≠ []
  /-- The correction term of each rule. -/
  π : G → G → MA G k
  /-- The swapped word is smaller. -/
  swap_lt : ∀ p ∈ pairs, ord.lt [p.2, p.1] [p.1, p.2]
  /-- **Strong filtration**: every monomial of `π(a, b)` is below `a b`. -/
  pi_lt : ∀ p ∈ pairs, ∀ w ∈ (π p.1 p.2).support,
    ord.lt (FreeMonoid.toList w) [p.1, p.2]
  /-- The rule-carrying relation is transitive (`a ≫ b ≫ c ⇒ a ≫ c`). -/
  trans : ∀ a b c : G, (a, b) ∈ pairs → (b, c) ∈ pairs → (a, c) ∈ pairs

variable {ord : AdmissibleOrder G}

namespace SplayData

variable (d : SplayData G k ord)

/-- The relation `a b − b a − π(a, b)` of a pair, in the monoid algebra. -/
noncomputable def relMA (a b : G) : MA G k := ofW [a, b] - ofW [b, a] - d.π a b

/-- The Jacobi element of a chain `a ≫ b ≫ c`. -/
noncomputable def jacobi (a b c : G) : MA G k :=
  ofW [a] * d.π b c - d.π b c * ofW [a] + ofW [c] * d.π a b - d.π a b * ofW [c]
    + d.π a c * ofW [b] - ofW [b] * d.π a c

theorem pi_apply_self {p : G × G} (hp : p ∈ d.pairs) :
    (d.π p.1 p.2) (FreeMonoid.ofList [p.1, p.2]) = 0 := by
  by_contra h
  have := d.pi_lt p hp _ (Finsupp.mem_support_iff.mpr h)
  rw [FreeMonoid.toList_ofList] at this
  exact ord.irrefl _ this

theorem ne_of_mem {p : G × G} (hp : p ∈ d.pairs) : p.1 ≠ p.2 := by
  intro h
  have := d.swap_lt p hp
  rw [h] at this
  exact ord.irrefl _ this

theorem relMA_apply_self [Nontrivial k] {p : G × G} (hp : p ∈ d.pairs) :
    d.relMA p.1 p.2 (FreeMonoid.ofList [p.1, p.2]) = 1 := by
  have hne : ([p.2, p.1] : List G) ≠ [p.1, p.2] := by
    intro h; exact d.ne_of_mem hp (List.cons.inj h).1.symm
  rw [relMA, Finsupp.sub_apply, Finsupp.sub_apply, ofW_apply, ofW_apply, if_pos rfl,
    if_neg hne, d.pi_apply_self hp, sub_zero, sub_zero]

variable [Nontrivial k]

/-- The rule of a pair. -/
noncomputable def rule (p : {p : G × G // p ∈ d.pairs}) : ReductionRule G k where
  relation := ofMA (d.relMA p.1.1 p.1.2)
  nonzero := by
    refine ⟨[p.1.1, p.1.2], Finset.mem_image.mpr ⟨FreeMonoid.ofList [p.1.1, p.1.2], ?_, rfl⟩⟩
    rw [Finsupp.mem_support_iff, d.relMA_apply_self p.2]
    exact one_ne_zero

/-- The splay rewriting system. -/
noncomputable def sys : RewritingSystem G k where
  rules := d.pairs.attach.map d.rule
  nonempty := by simpa using d.pairs_ne

theorem mem_sys {r : ReductionRule G k} : r ∈ d.sys.rules ↔ ∃ p, d.rule p = r := by
  simp [sys]

/-! ## §1  Leading monomials -/

theorem rule_lm (p : {p : G × G // p ∈ d.pairs}) :
    (d.rule p).lm ord = [p.1.1, p.1.2] := by
  apply leadingMonomial_eq_of_max
  · refine Finset.mem_image.mpr ⟨FreeMonoid.ofList [p.1.1, p.1.2], ?_, rfl⟩
    rw [Finsupp.mem_support_iff, d.relMA_apply_self p.2]; exact one_ne_zero
  · intro m hm hne
    obtain ⟨w, hw, rfl⟩ := Finset.mem_image.mp hm
    rw [Finsupp.mem_support_iff, ← FreeMonoid.ofList_toList w] at hw
    set m := FreeMonoid.toList w
    rw [relMA, Finsupp.sub_apply, Finsupp.sub_apply, ofW_apply, ofW_apply] at hw
    by_cases h2 : [p.1.2, p.1.1] = m
    · rw [← h2]; exact d.swap_lt _ p.2
    · rw [if_neg (Ne.symm hne), if_neg h2, zero_sub, sub_eq_add_neg, ← neg_add,
        zero_add, neg_ne_zero] at hw
      have := d.pi_lt _ p.2 (FreeMonoid.ofList m) (Finsupp.mem_support_iff.mpr hw)
      rwa [FreeMonoid.toList_ofList] at this

theorem rule_lc (p : {p : G × G // p ∈ d.pairs}) : (d.rule p).lc ord = 1 := by
  show (ofMA (d.relMA p.1.1 p.1.2)).coeff ((d.rule p).lm ord) = 1
  rw [d.rule_lm]
  exact d.relMA_apply_self p.2

theorem lc_isUnit : ∀ r ∈ d.sys.rules, IsUnit (r.lc ord) := by
  intro r hr
  obtain ⟨p, rfl⟩ := d.mem_sys.mp hr
  rw [d.rule_lc]; exact isUnit_one

theorem toMA_rule (p : {p : G × G // p ∈ d.pairs}) :
    toMA (d.rule p).relation = d.relMA p.1.1 p.1.2 := toMA_ofMA _

/-- A rule is determined by its leading monomial. -/
theorem rule_eq_of_lm {p q : {p : G × G // p ∈ d.pairs}}
    (h : (d.rule p).lm ord = (d.rule q).lm ord) : d.rule p = d.rule q := by
  rw [d.rule_lm, d.rule_lm] at h
  obtain ⟨h1, h2⟩ := List.cons.inj h
  obtain ⟨h2, -⟩ := List.cons.inj h2
  have : p = q := Subtype.ext (Prod.ext h1 h2)
  rw [this]

/-! ## §2  The rewrites a chain uses -/

theorem lt_trans' {x y z : Monomial G} (h₁ : ord.lt x y) (h₂ : ord.lt y z) : ord.lt x z :=
  ord.lt_trans h₁ h₂

/-- The member of the system carried by a pair. -/
theorem rule_mem (p : {p : G × G // p ∈ d.pairs}) : d.rule p ∈ d.sys.rules :=
  d.mem_sys.mpr ⟨p, rfl⟩

/-- A rule of the system, placed in context below `v`, lies in `JM v`. -/
theorem jm_rule {v : Monomial G} (p : {p : G × G // p ∈ d.pairs}) (x y : Monomial G)
    (h : ord.lt (x ++ [p.1.1, p.1.2] ++ y) v) :
    JM ord d.sys v (ofW x * d.relMA p.1.1 p.1.2 * ofW y) := by
  rw [← d.toMA_rule]
  refine JM.gen ⟨d.rule p, x, y⟩ (d.rule_mem p) ?_
  show ord.lt (x ++ (d.rule p).lm ord ++ y) v
  rwa [d.rule_lm]

/-! ## §3  The overlap of `(a,b)` and `(b,c)` is the Jacobi element -/

/-- The overlap S-polynomial of `(a, b)` and `(b, c)`, in the monoid algebra. -/
theorem overlap_expr (a b c : G) :
    d.relMA a b * ofW [c] - ofW [a] * d.relMA b c =
      -(ofW [b] * d.relMA a c) - d.relMA b c * ofW [a] + d.relMA a c * ofW [b]
        + ofW [c] * d.relMA a b + d.jacobi a b c := by
  simp only [relMA, jacobi, mul_sub, sub_mul, ← ofW_append]
  simp only [List.cons_append, List.nil_append]
  abel

theorem chain_lts (a b c : G) (hab : (a, b) ∈ d.pairs) (hbc : (b, c) ∈ d.pairs)
    (hac : (a, c) ∈ d.pairs) :
    ord.lt [b, a, c] [a, b, c] ∧ ord.lt [a, c, b] [a, b, c] ∧
      ord.lt [b, c, a] [a, b, c] ∧ ord.lt [c, a, b] [a, b, c] := by
  have h1 : ord.lt [b, a, c] [a, b, c] := by
    simpa using compat (ord := ord) [] [c] (d.swap_lt _ hab)
  have h2 : ord.lt [a, c, b] [a, b, c] := by
    simpa using compat (ord := ord) [a] [] (d.swap_lt _ hbc)
  have h3 : ord.lt [b, c, a] [b, a, c] := by
    simpa using compat (ord := ord) [b] [] (d.swap_lt _ hac)
  have h4 : ord.lt [c, a, b] [a, c, b] := by
    simpa using compat (ord := ord) [] [b] (d.swap_lt _ hac)
  exact ⟨h1, h2, ord.lt_trans h3 h1, ord.lt_trans h4 h2⟩

/-- **The overlap differs from the Jacobi element by the span below `abc`.** -/
theorem overlap_sub_jacobi_mem (a b c : G) (hab : (a, b) ∈ d.pairs)
    (hbc : (b, c) ∈ d.pairs) :
    JM ord d.sys [a, b, c]
      (d.relMA a b * ofW [c] - ofW [a] * d.relMA b c - d.jacobi a b c) := by
  have hac := d.trans a b c hab hbc
  obtain ⟨h1, h2, h3, h4⟩ := d.chain_lts a b c hab hbc hac
  rw [d.overlap_expr, add_sub_cancel_right]
  have g1 := d.jm_rule (v := [a, b, c]) ⟨(a, c), hac⟩ [b] [] (by simpa using h1)
  have g2 := d.jm_rule (v := [a, b, c]) ⟨(b, c), hbc⟩ [] [a] (by simpa using h3)
  have g3 := d.jm_rule (v := [a, b, c]) ⟨(a, c), hac⟩ [] [b] (by simpa using h2)
  have g4 := d.jm_rule (v := [a, b, c]) ⟨(a, b), hab⟩ [c] [] (by simpa using h4)
  simp only [ofW_nil, mul_one, one_mul] at g1 g2 g3 g4
  exact ((((g1.neg).sub g2).add g3).add g4)

/-! ## §4  Classification of compositions -/

theorem lm_length (r : ReductionRule G k) (hr : r ∈ d.sys.rules) : (r.lm ord).length = 2 := by
  obtain ⟨p, rfl⟩ := d.mem_sys.mp hr
  rw [d.rule_lm]; rfl

theorem rule_eq_of_mem_lm {r₁ r₂ : ReductionRule G k} (h₁ : r₁ ∈ d.sys.rules)
    (h₂ : r₂ ∈ d.sys.rules) (h : r₁.lm ord = r₂.lm ord) : r₁ = r₂ := by
  obtain ⟨p, rfl⟩ := d.mem_sys.mp h₁
  obtain ⟨q, rfl⟩ := d.mem_sys.mp h₂
  exact d.rule_eq_of_lm h

/-- **Inclusions are vacuous**: two leading monomials of length `2` can only
    contain one another by being equal, and then the rules agree. -/
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

/-- The S-polynomial of a genuine overlap `(a,b)`, `(b,c)`. -/
theorem toMA_spoly_chain (oc : OverlapComposition G k ord) (h₁ : oc.rule₁ ∈ d.sys.rules)
    (h₂ : oc.rule₂ ∈ d.sys.rules) (a b c : G) (hl : oc.left = [a]) (ho : oc.overlap = [b])
    (hr : oc.right = [c]) :
    ∃ (_ : (a, b) ∈ d.pairs) (_ : (b, c) ∈ d.pairs),
      toMA oc.spoly = d.relMA a b * ofW [c] - ofW [a] * d.relMA b c := by
  obtain ⟨p, hp⟩ := d.mem_sys.mp h₁
  obtain ⟨q, hq⟩ := d.mem_sys.mp h₂
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

/-! ## §5  The composition condition is the Jacobi condition -/

/-- The **Jacobi condition**: for every chain `a ≫ b ≫ c`, the Jacobi element lies in
    the span of the rules placed below `a b c`. -/
def JacobiCondition : Prop :=
  ∀ a b c : G, (a, b) ∈ d.pairs → (b, c) ∈ d.pairs → JM ord d.sys [a, b, c] (d.jacobi a b c)

/-- **PBW, composition step.** A splay system has trivial compositions iff it
    satisfies the Jacobi condition. -/
theorem compositionsTrivial_iff : CompositionsTrivial ord d.sys ↔ d.JacobiCondition := by
  constructor
  · intro ht a b c hab hbc
    -- the overlap of `(a,b)` and `(b,c)`
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
    have := hJ.sub (d.overlap_sub_jacobi_mem a b c hab hbc)
    rwa [sub_sub_cancel] at this
  · intro hjac
    refine ⟨fun oc h₁ h₂ => ?_, fun ic h₁ h₂ => d.inclusion_trivial ic h₁ h₂⟩
    rcases d.overlap_cases oc h₁ h₂ with ⟨hl, hr, he⟩ | ⟨a, b, c, hl, ho, hr⟩
    · rw [toMA_of_isZero (oc.spoly_isZero_of_self he hl hr)]
      exact JM.zero
    · obtain ⟨hab, hbc, he⟩ := d.toMA_spoly_chain oc h₁ h₂ a b c hl ho hr
      have hw : oc.word = [a, b, c] := by
        simp [OverlapComposition.word, hl, ho, hr]
      rw [he, hw]
      have := (d.overlap_sub_jacobi_mem a b c hab hbc).add (hjac a b c hab hbc)
      rwa [sub_add_cancel] at this

/-- **PBW, Gröbner–Shirshov form.** A splay system is a Gröbner–Shirshov basis
    iff it satisfies the Jacobi condition. -/
theorem isGrobnerShirshovBasis_iff :
    IsGrobnerShirshovBasis G k ord d.sys ↔ d.JacobiCondition :=
  (isGrobnerShirshovBasis_iff_compositionsTrivial d.lc_isUnit).trans d.compositionsTrivial_iff

/-! ## §6  The normal-form basis -/

/-- The normal-form monomials of a splay system are the words with no adjacent
    `a b` carrying a rule ("sorted" words). -/
theorem normalFormMonomial_iff (m : Monomial G) :
    NormalFormMonomial ord d.sys m ↔ ∀ p ∈ d.pairs, ¬ [p.1, p.2] <:+: m := by
  constructor
  · intro h p hp
    have := h _ (d.rule_mem ⟨p, hp⟩)
    rwa [d.rule_lm] at this
  · intro h r hr
    obtain ⟨p, rfl⟩ := d.mem_sys.mp hr
    rw [d.rule_lm]
    exact h p.1 p.2

/-- **PBW for a splay system.** Under the Jacobi condition, the classes of the
    sorted words form a `k`-basis of the quotient of the free algebra by the
    splay relations. -/
theorem normalFormBasis [DecidableEq k] (hj : d.JacobiCondition) :
    NormalFormBasis ord d.sys :=
  NFBasis.normalFormBasis_of_isGrobnerShirshovBasis (d.isGrobnerShirshovBasis_iff.mpr hj)
    d.lc_isUnit

end SplayData

end UGB.GrobnerShirshov.Splay
