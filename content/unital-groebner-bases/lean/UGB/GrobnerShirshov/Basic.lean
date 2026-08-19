import Mathlib.Order.WellFounded
import Mathlib.Data.Finset.Insert
import Mathlib.Tactic.NoncommRing
import UGB.GrobnerShirshov.Elem

/-!
# Gröbner–Shirshov Bases — Foundational Definitions

This module provides the abstract algebraic framework for Gröbner–Shirshov
(GS) bases in the context of non-commutative algebras presented by
generators and relations.  The key structures are:

1. **Monomial order** — a well-order on monomials compatible with
   multiplication (admissible order).
2. **Rewriting system** — oriented relations `f ↦ f − lm(f)` that
   reduce elements to normal form.
3. **Single-step and multi-step reduction** — formalised as inductive
   relations, enabling proper termination and confluence statements.
4. **S-polynomial (composition)** — the obstruction to confluence;
   the composition lemma asserts all S-polynomials reduce to zero.

The elements themselves, and their arithmetic, live in `Elem.lean`.

## Three repairs (bean qou-auq3)

Earlier versions of this file were degenerate in three separate ways, and the
predicate `IsGrobnerShirshovBasis` consequently held of everything:

1. `leadingMonomial (_ord) f hf := hf.choose` **ignored its order argument**
   and returned an arbitrary element of the support. Every statement phrased
   with it — the composition decompositions, `isNormalForm`,
   `SingleStepReduction` — was therefore about an arbitrary monomial. It is
   now the `ord`-greatest support element (§2), with
   `leadingMonomial_mem_support` and `le_leadingMonomial` exported.
2. `SingleStepReduction` **did not relate `f` to `g`**: its only field asked
   that some rule's leading monomial be an infix of some monomial of `f` and
   that no monomial of `g` exceed it — which `g = 0` satisfies always. It now
   carries the equation `g = f − c • (a · r.relation · b)` (§3).
3. `OverlapComposition.spoly` and `InclusionComposition.spoly` were **free
   fields**, never computed from the rules, so "the S-polynomial reduces to
   zero" constrained nothing. They are now definitions (§4). The composition
   structures also quantified their decomposition over *every* admissible
   order (`lm₁_decomp : ∀ ord, …`), which after repair (1) would have made
   them near-uninhabited and the GS predicate vacuous in the other direction;
   they now take the order as a parameter.

The acceptance test for the repair is `UGB.GrobnerShirshov.Hecke`'s
`one_does_not_reduce_to_zero`: the unit is in normal form for the Hecke system
and is not zero, so "everything reduces to zero" no longer holds.

## References

- [fred2005, §3] — Gröbner–Shirshov basis for `Dist(G)`
- Bokut & Chen, *Gröbner–Shirshov bases and their calculation*,
  Bull. Math. Sci. 4 (2014), 325–395.
- Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978), 178–218.
- Leitner & Pawloski, *Unital Gröbner bases over arbitrary commutative ground
  rings*, arXiv:math/0409565v2 — the "no quasi-zeros" hypothesis of §7.
-/


namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Monomials and Admissible Orders

`Monomial` and `AlgElement` are defined in `Elem.lean`. -/

/-- An **admissible monomial order**: a well-order on monomials that is
    compatible with left and right multiplication (concatenation).

    `lt a b` means `a` is strictly smaller than `b` in the ordering.

    Compatibility: if `a < b` then `c ++ a ++ d < c ++ b ++ d`
    for all monomials `c`, `d`. -/
structure AdmissibleOrder (G : Type u) where
  /-- The strict order relation on monomials. -/
  lt : Monomial G → Monomial G → Prop
  /-- The order is a strict linear order (trichotomy). -/
  trichotomy : ∀ (a b : Monomial G),
    lt a b ∨ a = b ∨ lt b a
  /-- The order is well-founded (every non-empty set has a minimum). -/
  wf : WellFounded lt
  /-- Left compatibility: `a < b → c ++ a < c ++ b`. -/
  left_compat : ∀ (a b c : Monomial G),
    lt a b → lt (c ++ a) (c ++ b)
  /-- Right compatibility: `a < b → a ++ d < b ++ d`. -/
  right_compat : ∀ (a b d : Monomial G),
    lt a b → lt (a ++ d) (b ++ d)

namespace AdmissibleOrder

variable {G : Type u}

/-- An admissible order is asymmetric: well-foundedness forbids `a < b < a`. -/
theorem asymm (ord : AdmissibleOrder G) {a b : Monomial G}
    (hab : ord.lt a b) : ¬ ord.lt b a := by
  intro hba
  have key : ∀ x : Monomial G, Acc ord.lt x → x ≠ a ∧ x ≠ b := by
    intro x hx
    induction hx with
    | intro y _ ih =>
      constructor
      · rintro rfl; exact (ih b hba).2 rfl
      · rintro rfl; exact (ih a hab).1 rfl
  exact (key a (ord.wf.apply a)).1 rfl

/-- An admissible order is irreflexive. -/
theorem irrefl (ord : AdmissibleOrder G) (a : Monomial G) : ¬ ord.lt a a :=
  fun h => ord.asymm h h

/-- An admissible order is transitive.  Trichotomy alone does not give this;
    well-foundedness does, by ruling out the 3-cycle `a < b < c < a`. -/
theorem lt_trans (ord : AdmissibleOrder G) {a b c : Monomial G}
    (hab : ord.lt a b) (hbc : ord.lt b c) : ord.lt a c := by
  rcases ord.trichotomy a c with h | rfl | hca
  · exact h
  · exact absurd hbc (ord.asymm hab)
  · exfalso
    have key : ∀ x : Monomial G, Acc ord.lt x → x ≠ a ∧ x ≠ b ∧ x ≠ c := by
      intro x hx
      induction hx with
      | intro y _ ih =>
        refine ⟨?_, ?_, ?_⟩
        · rintro rfl; exact (ih c hca).2.2 rfl
        · rintro rfl; exact (ih a hab).1 rfl
        · rintro rfl; exact (ih b hbc).2.1 rfl
    exact (key a (ord.wf.apply a)).1 rfl

/-- **The empty word is the minimum of any admissible order.**

    If some `m` were below `[]`, right compatibility would give
    `m ++ x < x` for *every* `x`, and `x ↦ m ++ x` would be an infinite
    descending chain — contradicting well-foundedness. Nothing in the
    structure's fields says this directly; it is forced. -/
theorem not_lt_nil (ord : AdmissibleOrder G) (m : Monomial G) :
    ¬ ord.lt m [] := by
  intro h
  have step : ∀ x : Monomial G, ord.lt (m ++ x) x := by
    intro x
    have := ord.right_compat m [] x h
    simpa using this
  have key : ∀ x : Monomial G, Acc ord.lt x → False := by
    intro x hx
    induction hx with
    | intro y _ ih => exact ih (m ++ y) (step y)
  exact key [] (ord.wf.apply [])

/-- Every non-empty finite set of monomials has a greatest element. -/
theorem exists_max (ord : AdmissibleOrder G) (s : Finset (Monomial G)) :
    s.Nonempty → ∃ m ∈ s, ∀ m' ∈ s, ¬ ord.lt m m' := by
  classical
  induction s using Finset.induction_on with
  | empty => intro h; exact absurd h (by simp)
  | @insert a s ha ih =>
    intro _
    rcases s.eq_empty_or_nonempty with rfl | hs'
    · refine ⟨a, Finset.mem_insert_self a ∅, ?_⟩
      intro m' hm'
      have hm'a : m' = a := by simpa using hm'
      subst hm'a
      exact ord.irrefl _
    · obtain ⟨m, hm, hmax⟩ := ih hs'
      rcases ord.trichotomy m a with hma | rfl | ham
      · -- `m < a`: the new element is the greatest.
        refine ⟨a, Finset.mem_insert_self a s, ?_⟩
        intro m' hm' hlt
        rcases Finset.mem_insert.mp hm' with rfl | hm'
        · exact ord.irrefl _ hlt
        · rcases ord.trichotomy m' m with h1 | rfl | h1
          · exact ord.asymm hma (ord.lt_trans hlt h1)
          · exact ord.asymm hma hlt
          · exact hmax m' hm' h1
      · exact absurd hm ha
      · -- `a < m`: the old maximum survives.
        refine ⟨m, Finset.mem_insert_of_mem hm, ?_⟩
        intro m' hm'
        rcases Finset.mem_insert.mp hm' with rfl | hm'
        · exact ord.asymm ham
        · exact hmax m' hm'

end AdmissibleOrder

/-! ## §2  Leading Monomials

**Repair 1.** `leadingMonomial` is the `ord`-greatest element of the support,
not an arbitrary one. -/

/-- The **leading monomial** of a non-zero element with respect to an
    admissible order: the greatest monomial of its support.

    (The support may be a strict superset of the monomials with non-zero
    coefficient — see `Elem.lean` — so the leading monomial may carry
    coefficient `0`. `lt_leadingMonomial_of_coeff_ne_zero` is the statement
    that survives that slack, and it is the one the theory uses.) -/
noncomputable def leadingMonomial {G : Type u} {k : Type v} [Ring k]
    (ord : AdmissibleOrder G)
    (f : AlgElement G k)
    (hf : f.support.Nonempty) : Monomial G :=
  (ord.exists_max f.support hf).choose

/-- The leading monomial is a monomial of the element. -/
theorem leadingMonomial_mem_support {G : Type u} {k : Type v} [Ring k]
    (ord : AdmissibleOrder G) (f : AlgElement G k) (hf : f.support.Nonempty) :
    leadingMonomial ord f hf ∈ f.support :=
  (ord.exists_max f.support hf).choose_spec.1

/-- **Maximality**: no monomial of the element exceeds the leading monomial. -/
theorem le_leadingMonomial {G : Type u} {k : Type v} [Ring k]
    (ord : AdmissibleOrder G) (f : AlgElement G k) (hf : f.support.Nonempty) :
    ∀ m ∈ f.support, ¬ ord.lt (leadingMonomial ord f hf) m :=
  (ord.exists_max f.support hf).choose_spec.2

/-- Every *other* monomial actually occurring in `f` is strictly below the
    leading monomial. -/
theorem lt_leadingMonomial_of_coeff_ne_zero {G : Type u} {k : Type v} [Ring k]
    (ord : AdmissibleOrder G) (f : AlgElement G k) (hf : f.support.Nonempty)
    {m : Monomial G} (hm : f.coeff m ≠ 0) (hne : m ≠ leadingMonomial ord f hf) :
    ord.lt m (leadingMonomial ord f hf) := by
  have hmem := AlgElement.mem_support_of_coeff_ne_zero hm
  rcases ord.trichotomy (leadingMonomial ord f hf) m with h | h | h
  · exact absurd h (le_leadingMonomial ord f hf m hmem)
  · exact absurd h.symm hne
  · exact h

/-- Pinning the leading monomial down: a support element that dominates every
    other support element *is* the leading monomial. -/
theorem leadingMonomial_eq_of_max {G : Type u} {k : Type v} [Ring k]
    (ord : AdmissibleOrder G) (f : AlgElement G k) (hf : f.support.Nonempty)
    (m₀ : Monomial G) (hmem : m₀ ∈ f.support)
    (hmax : ∀ m ∈ f.support, m ≠ m₀ → ord.lt m m₀) :
    leadingMonomial ord f hf = m₀ := by
  by_contra hne
  exact le_leadingMonomial ord f hf m₀ hmem
    (hmax _ (leadingMonomial_mem_support ord f hf) hne)

/-- The **leading coefficient**. -/
noncomputable def leadingCoeff {G : Type u} {k : Type v} [Ring k]
    (ord : AdmissibleOrder G) (f : AlgElement G k) (hf : f.support.Nonempty) : k :=
  f.coeff (leadingMonomial ord f hf)

/-! ## §3  Rewriting System and Reduction Relations -/

/-- A **reduction rule**: an oriented relation `f ↦ f - c·lm(f)` that
    replaces the leading monomial of `f` by its tail.

    In practice, each defining relation of the algebra gives one rule. -/
structure ReductionRule (G : Type u) (k : Type v) [Ring k] where
  /-- The polynomial whose leading term defines the rewrite. -/
  relation : AlgElement G k
  /-- The relation is non-zero. -/
  nonzero : relation.support.Nonempty

/-- The leading monomial of a rule, for a given admissible order. -/
noncomputable abbrev ReductionRule.lm {G : Type u} {k : Type v} [Ring k]
    (r : ReductionRule G k) (ord : AdmissibleOrder G) : Monomial G :=
  leadingMonomial ord r.relation r.nonzero

/-- The leading coefficient of a rule, for a given admissible order. -/
noncomputable abbrev ReductionRule.lc {G : Type u} {k : Type v} [Ring k]
    (r : ReductionRule G k) (ord : AdmissibleOrder G) : k :=
  leadingCoeff ord r.relation r.nonzero

/-- A **rewriting system**: a set of reduction rules. -/
structure RewritingSystem (G : Type u) (k : Type v) [Ring k] where
  /-- The collection of reduction rules. -/
  rules : List (ReductionRule G k)
  /-- The system has at least one rule (non-trivial). -/
  nonempty : rules ≠ []

/-- **Single-step reduction**, repaired (repair 2).

    `f → g` when some rule `r ∈ sys` has its leading monomial occurring inside
    a monomial of `f` — say `f` has a non-zero coefficient at `a ++ lm(r) ++ b`
    — and `g` is obtained by subtracting the corresponding multiple of the
    relation:

    `g = f − c • (a · r.relation · b)`,  with  `c · lc(r) = f.coeff(a·lm(r)·b)`.

    The coefficient condition is what makes the step *eliminate* the monomial
    it targets: `g.coeff (a·lm(r)·b) = 0`. Two degenerate readings are excluded
    by it. Without `f.coeff (a·lm(r)·b) ≠ 0` and the equation on `c`, the
    choice `c = 0`, `g = f` would be a legal step, `→` would be reflexive, and
    `CompositionLemma.reduction_well_founded` would be a *false* axiom. And
    the previous version — which asked only that `lm(r)` be an infix of some
    monomial of `f`, with no relation between `f` and `g` at all — admitted
    `g = 0` from any `f` whatsoever.

    Everything is stated on coefficients rather than on the `support` field,
    because that field is only a superset of the true support (see `Elem.lean`)
    and carries no mathematical content. -/
structure SingleStepReduction {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (f g : AlgElement G k) : Prop where
  /-- There exists a rule, an occurrence of its leading monomial inside a
      monomial of `f`, and a coefficient, witnessing the step. -/
  exists_witness :
    ∃ (rule_used : ReductionRule G k),
      rule_used ∈ sys.rules ∧
    ∃ (a b : Monomial G) (c : k),
      f.coeff (a ++ rule_used.lm ord ++ b) ≠ 0 ∧
      c * rule_used.lc ord = f.coeff (a ++ rule_used.lm ord ++ b) ∧
      AlgElement.CoeffEq g
        (AlgElement.sub f
          (AlgElement.smul c (AlgElement.contextMul a rule_used.relation b)))

/-- **A step eliminates the monomial it targets.**  This is what makes the
    repaired reduction relation terminating, and it is the property the
    `reduction_well_founded` axiom of `CompositionLemma.lean` rests on. -/
theorem SingleStepReduction.exists_eliminated {G : Type u} {k : Type v}
    [Ring k] [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g : AlgElement G k} (h : SingleStepReduction ord sys f g) :
    ∃ (r : ReductionRule G k) (a b : Monomial G), r ∈ sys.rules ∧
      f.coeff (a ++ r.lm ord ++ b) ≠ 0 ∧ g.coeff (a ++ r.lm ord ++ b) = 0 := by
  obtain ⟨r, hr, a, b, c, hne, hc, heq⟩ := h.exists_witness
  refine ⟨r, a, b, hr, hne, ?_⟩
  have hc' : c * r.relation.coeff (r.lm ord) = f.coeff (a ++ r.lm ord ++ b) := hc
  have hg := heq (a ++ r.lm ord ++ b)
  simp only [AlgElement.sub_coeff, AlgElement.smul_coeff,
    AlgElement.contextMul_coeff_middle] at hg
  rw [hg, hc', sub_self]

/-- In particular a step changes the element: `g ≠ f` coefficient-wise. -/
theorem SingleStepReduction.not_coeffEq {G : Type u} {k : Type v}
    [Ring k] [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g : AlgElement G k} (h : SingleStepReduction ord sys f g) :
    ¬ AlgElement.CoeffEq g f := by
  obtain ⟨r, a, b, -, hne, hzero⟩ := h.exists_eliminated
  exact fun heq => hne (heq (a ++ r.lm ord ++ b) ▸ hzero)

/-- **Multi-step reduction**: the reflexive transitive closure of
    single-step reduction. -/
inductive MultiStepReduction {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) :
    AlgElement G k → AlgElement G k → Prop where
  /-- Zero steps: `f` reduces to itself. -/
  | refl (f : AlgElement G k) : MultiStepReduction ord sys f f
  /-- Transitivity: if `f →* g` and `g → h`, then `f →* h`. -/
  | step {f g h : AlgElement G k} :
    MultiStepReduction ord sys f g →
    SingleStepReduction ord sys g h →
    MultiStepReduction ord sys f h

/-- A single step in front of a run. -/
theorem MultiStepReduction.head {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g h : AlgElement G k}
    (hstep : SingleStepReduction ord sys f g)
    (hrest : MultiStepReduction ord sys g h) :
    MultiStepReduction ord sys f h := by
  induction hrest with
  | refl => exact MultiStepReduction.step (MultiStepReduction.refl f) hstep
  | step _ hlast ih => exact MultiStepReduction.step ih hlast

/-- Runs compose. -/
theorem MultiStepReduction.trans {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g h : AlgElement G k}
    (h₁ : MultiStepReduction ord sys f g)
    (h₂ : MultiStepReduction ord sys g h) :
    MultiStepReduction ord sys f h := by
  induction h₂ with
  | refl => exact h₁
  | step _ hlast ih => exact MultiStepReduction.step ih hlast

/-- **Head decomposition**: a run is either empty, or a first step followed by a
    run.

    `MultiStepReduction` is generated at the *tail* — `step` appends a step to a
    run — so this is the dual view, and it is the one Newman's lemma needs: the
    induction there is on the source of the fork, so the first step has to be the
    one exposed. -/
theorem MultiStepReduction.cases_head {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g : AlgElement G k} (h : MultiStepReduction ord sys f g) :
    g = f ∨ ∃ a, SingleStepReduction ord sys f a ∧ MultiStepReduction ord sys a g := by
  induction h with
  | refl => exact Or.inl rfl
  | step _ hlast ih =>
    rcases ih with rfl | ⟨a, hfa, hag⟩
    · exact Or.inr ⟨_, hlast, MultiStepReduction.refl _⟩
    · exact Or.inr ⟨a, hfa, MultiStepReduction.step hag hlast⟩

/-- An element is in **normal form** with respect to a rewriting system
    if no leading monomial of any rule divides (appears as a subword of)
    any monomial actually occurring in the element.

    Stated on coefficients, not on the `support` field: an element's normality
    must not depend on the superset chosen to represent it. -/
def isNormalForm {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (f : AlgElement G k) : Prop :=
  ∀ r ∈ sys.rules, ∀ m, f.coeff m ≠ 0 → ¬ (r.lm ord) <:+: m

/-- A normal form admits no reduction step. (The converse needs every rule to
    have an invertible leading coefficient; `isNormalForm` is the divisibility
    condition, which is the standard one for monic rules.) -/
theorem not_singleStep_of_isNormalForm {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f : AlgElement G k} (hnf : isNormalForm ord sys f) (g : AlgElement G k) :
    ¬ SingleStepReduction ord sys f g := by
  rintro ⟨r, hr, a, b, c, hne, -, -⟩
  exact hnf r hr _ hne ⟨a, b, rfl⟩

/-- **The converse, with the hypothesis it actually needs**: if every rule has a
    *unit* leading coefficient, then an element not in normal form admits a step.

    The hypothesis is not cosmetic bookkeeping. `isNormalForm` is a condition on
    **monomials** — no rule's leading monomial is an infix of one carrying a
    non-zero coefficient — whereas taking a step additionally requires solving

    `c · lc(r) = f.coeff (a ++ lm(r) ++ b)`

    for `c`. When `lc(r)` is not invertible those two conditions come apart, and
    an element can be **stuck**: reducible-looking (so not in normal form), yet
    with no reduction available (so unable to reach one). That is not a gap in
    this proof — it is a true statement about the reduction relation, and
    `NormalFormExistsRefutation` exhibits it concretely over `ℤ`. -/
theorem exists_singleStep_of_not_isNormalForm {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f : AlgElement G k} (hnf : ¬ isNormalForm ord sys f) :
    ∃ g, SingleStepReduction ord sys f g := by
  rw [isNormalForm] at hnf
  push_neg at hnf
  obtain ⟨r, hr, m, hm, a, b, hab⟩ := hnf
  subst hab
  obtain ⟨u, hu⟩ := hlc r hr
  refine ⟨AlgElement.sub f (AlgElement.smul (f.coeff (a ++ r.lm ord ++ b) * ↑u⁻¹)
      (AlgElement.contextMul a r.relation b)),
    ⟨r, hr, a, b, f.coeff (a ++ r.lm ord ++ b) * ↑u⁻¹, hm, ?_, fun _ => rfl⟩⟩
  rw [← hu, mul_assoc, Units.inv_mul, mul_one]

/-- An element `f` **reduces to normal form** `nf` if `f →* nf` and
    `nf` is in normal form. -/
structure ReducesToNF {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (f : AlgElement G k)
    (nf : AlgElement G k) : Prop where
  /-- Multi-step reduction from f to nf. -/
  reduces : MultiStepReduction ord sys f nf
  /-- The result is in normal form. -/
  is_normal : isNormalForm ord sys nf

/-- A normal form only reduces to itself. -/
theorem MultiStepReduction.eq_of_isNormalForm {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g : AlgElement G k} (hnf : isNormalForm ord sys f)
    (h : MultiStepReduction ord sys f g) : g = f := by
  induction h with
  | refl => rfl
  | step _ hlast ih =>
    rw [ih] at hlast
    exact absurd hlast (not_singleStep_of_isNormalForm hnf _)

/-! ## §4  S-Polynomials (Compositions)

**Repair 3.** The two composition structures take the admissible order as a
parameter (their decompositions used to be quantified over *all* orders, which
after repair 1 is a condition almost nothing satisfies), and `spoly` is
computed from the rules and contexts instead of being a free field. -/

/-- **Overlap composition** (intersection S-polynomial):
    given two rules whose leading monomials overlap, the S-polynomial
    is the difference of the two ways to reduce the overlap.

    If `lm(f) = a·b` and `lm(g) = b·c` with overlap `b`, then
    `S(f,g) = lc(g)·f·c − lc(f)·a·g` — for monic rules simply `f·c − a·g`.

    The composition lemma states that the rewriting system is a
    Gröbner–Shirshov basis iff every S-polynomial reduces to zero. -/
structure OverlapComposition (G : Type u) (k : Type v) [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G) where
  /-- The first rule. -/
  rule₁ : ReductionRule G k
  /-- The second rule. -/
  rule₂ : ReductionRule G k
  /-- The left context (monomials before the overlap). -/
  left : Monomial G
  /-- The overlap subword. -/
  overlap : Monomial G
  /-- The right context (monomials after the overlap). -/
  right : Monomial G
  /-- The leading monomial of rule₁ decomposes as `left ++ overlap`. -/
  lm₁_decomp : rule₁.lm ord = left ++ overlap
  /-- The leading monomial of rule₂ decomposes as `overlap ++ right`. -/
  lm₂_decomp : rule₂.lm ord = overlap ++ right
  /-- The overlap is non-empty. -/
  overlap_nonempty : overlap ≠ []

/-- The ambient word of an overlap composition: `left ++ overlap ++ right`,
    which is both `lm(rule₁) ++ right` and `left ++ lm(rule₂)`. -/
def OverlapComposition.word {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} (oc : OverlapComposition G k ord) : Monomial G :=
  oc.left ++ oc.overlap ++ oc.right

/-- **The overlap S-polynomial**, computed (no longer a free field):
    `lc₂ • (rule₁ · right) − lc₁ • (left · rule₂)`. -/
noncomputable def OverlapComposition.spoly {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (oc : OverlapComposition G k ord) :
    AlgElement G k :=
  AlgElement.sub
    (AlgElement.smul (oc.rule₂.lc ord)
      (AlgElement.contextMul [] oc.rule₁.relation oc.right))
    (AlgElement.smul (oc.rule₁.lc ord)
      (AlgElement.contextMul oc.left oc.rule₂.relation []))

/-- **A rule composed with itself over its whole leading monomial is vacuous.**

`OverlapComposition` places no condition on `left` or `right`, so `left = right =
[]` — the two rules leading on the *same* word — is a legal composition, and it
is legal in particular when the two rules are the same rule. Then the two halves
of the S-polynomial are literally the same element and it is zero.

Worth having explicitly rather than as an aside: in any completeness proof the
degenerate shapes are as much a proof obligation as the genuine overlaps, and
this discharges every one of them whose two rules coincide. What it does *not*
cover is two **distinct** rules leading on the same word — see
`UGB.GrobnerShirshov.Hecke.DegenerateYbBs`, where that case is inhabited. -/
theorem OverlapComposition.spoly_isZero_of_self {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (oc : OverlapComposition G k ord)
    (hrule : oc.rule₁ = oc.rule₂) (hleft : oc.left = []) (hright : oc.right = []) :
    oc.spoly.isZero := by
  intro m
  simp only [OverlapComposition.spoly, hrule, hleft, hright, AlgElement.sub_coeff,
    AlgElement.smul_coeff, AlgElement.contextMul_nil_nil_coeff, sub_self]

/-- An element that is zero is in normal form: `isNormalForm` only constrains
monomials with a non-zero coefficient, of which there are none. -/
theorem isNormalForm_of_isZero {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k} {f : AlgElement G k}
    (hf : f.isZero) : isNormalForm ord sys f :=
  fun _ _ m hm => absurd (hf m) hm

/-- …so an element that is zero reduces to zero, in no steps. This is the
Gröbner–Shirshov obligation for a composition whose S-polynomial vanishes
outright. -/
theorem reducesToNF_self_of_isZero {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k} {f : AlgElement G k}
    (hf : f.isZero) : ∃ nf, ReducesToNF ord sys f nf ∧ nf.isZero :=
  ⟨f, ⟨MultiStepReduction.refl f, isNormalForm_of_isZero hf⟩, hf⟩

/-- **Inclusion composition**: when the leading monomial of one rule
    entirely contains that of another as a subword.

    If `lm(g) = a ++ lm(f) ++ b`, then `S(f,g) = lc(f)·g − lc(g)·a·f·b`. -/
structure InclusionComposition (G : Type u) (k : Type v) [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G) where
  /-- The inner rule (whose lm is contained). -/
  inner : ReductionRule G k
  /-- The outer rule (whose lm contains the inner). -/
  outer : ReductionRule G k
  /-- Left context. -/
  left : Monomial G
  /-- Right context. -/
  right : Monomial G
  /-- The leading monomial of the outer rule decomposes as
      `left ++ lm(inner) ++ right`. -/
  decomposition : outer.lm ord = left ++ inner.lm ord ++ right

/-- **The inclusion S-polynomial**, computed (no longer a free field):
    `lc(inner) • outer − lc(outer) • (left · inner · right)`. -/
noncomputable def InclusionComposition.spoly {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (ic : InclusionComposition G k ord) :
    AlgElement G k :=
  AlgElement.sub
    (AlgElement.smul (ic.inner.lc ord) ic.outer.relation)
    (AlgElement.smul (ic.outer.lc ord)
      (AlgElement.contextMul ic.left ic.inner.relation ic.right))

/-- **An inclusion whose two contexts are empty is vacuous once the relations are
proportional by the two leading coefficients.**

With `left = right = []` the S-polynomial is `lc(inner) • outer − lc(outer) •
inner`, so it vanishes exactly when the hypothesis below holds coefficient by
coefficient. Both ways a shared leading monomial arises in practice satisfy it:
the two rules are the same rule, or they are negatives of each other with
leading coefficients of opposite sign. -/
theorem InclusionComposition.spoly_isZero_of_scaled {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (ic : InclusionComposition G k ord)
    (hleft : ic.left = []) (hright : ic.right = [])
    (h : ∀ m, ic.inner.lc ord * ic.outer.relation.coeff m
            = ic.outer.lc ord * ic.inner.relation.coeff m) :
    ic.spoly.isZero := by
  intro m
  simp only [InclusionComposition.spoly, hleft, hright, AlgElement.sub_coeff,
    AlgElement.smul_coeff, AlgElement.contextMul_nil_nil_coeff]
  rw [h m, sub_self]

/-- **A rule included in itself is vacuous.** Unlike the overlap case this needs
no hypothesis on the contexts: `decomposition` says `lm = left ++ lm ++ right`,
and lengths force both contexts empty. -/
theorem InclusionComposition.spoly_isZero_of_self {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (ic : InclusionComposition G k ord)
    (hrule : ic.inner = ic.outer) : ic.spoly.isZero := by
  have hlen := congrArg List.length ic.decomposition
  rw [hrule] at hlen
  simp only [List.length_append] at hlen
  refine ic.spoly_isZero_of_scaled (List.eq_nil_of_length_eq_zero (by omega))
    (List.eq_nil_of_length_eq_zero (by omega)) ?_
  intro m
  rw [hrule]

/-! ### §4.1  The leading terms of an S-polynomial cancel

This is the sanity check on the definitions above: an S-polynomial is built so
that the ambient word `left ++ overlap ++ right` — the one monomial both
reductions act on — drops out. Over a commutative ring it drops out exactly. -/

/-- The coefficient of an overlap S-polynomial at the ambient word is
    `lc₂·lc₁ − lc₁·lc₂`. -/
theorem OverlapComposition.spoly_coeff_word {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (oc : OverlapComposition G k ord) :
    oc.spoly.coeff oc.word
      = oc.rule₂.lc ord * oc.rule₁.lc ord - oc.rule₁.lc ord * oc.rule₂.lc ord := by
  have h₁ : oc.word = [] ++ (oc.left ++ oc.overlap) ++ oc.right := by
    simp [OverlapComposition.word]
  have h₂ : oc.word = oc.left ++ (oc.overlap ++ oc.right) ++ [] := by
    simp [OverlapComposition.word, List.append_assoc]
  simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  rw [h₁, AlgElement.contextMul_coeff_middle, ← h₁, h₂,
    AlgElement.contextMul_coeff_middle]
  rw [← oc.lm₁_decomp, ← oc.lm₂_decomp]
  rfl

/-- Over a commutative ring the ambient word cancels outright. -/
theorem OverlapComposition.spoly_coeff_word_eq_zero {G : Type u} {k : Type v}
    [CommRing k] [DecidableEq G] {ord : AdmissibleOrder G}
    (oc : OverlapComposition G k ord) : oc.spoly.coeff oc.word = 0 := by
  rw [oc.spoly_coeff_word, mul_comm, sub_self]

/-- The coefficient of an inclusion S-polynomial at the outer leading monomial
    is `lc(inner)·lc(outer) − lc(outer)·lc(inner)`. -/
theorem InclusionComposition.spoly_coeff_lm {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (ic : InclusionComposition G k ord) :
    ic.spoly.coeff (ic.outer.lm ord)
      = ic.inner.lc ord * ic.outer.lc ord - ic.outer.lc ord * ic.inner.lc ord := by
  simp only [InclusionComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  rw [ic.decomposition, AlgElement.contextMul_coeff_middle, ← ic.decomposition]
  rfl

/-- Over a commutative ring the outer leading monomial cancels outright. -/
theorem InclusionComposition.spoly_coeff_lm_eq_zero {G : Type u} {k : Type v}
    [CommRing k] [DecidableEq G] {ord : AdmissibleOrder G}
    (ic : InclusionComposition G k ord) : ic.spoly.coeff (ic.outer.lm ord) = 0 := by
  rw [ic.spoly_coeff_lm, mul_comm, sub_self]

/-! ## §5  Gröbner–Shirshov Basis (Abstract Definition) -/

/-- A rewriting system is a **Gröbner–Shirshov basis** if every
    S-polynomial (both overlap and inclusion compositions) reduces to
    the zero element under the rewriting system.

    This is the abstract formulation of the composition lemma
    (Shirshov 1962, Bokut 1976, Bergman 1978). -/
structure IsGrobnerShirshovBasis (G : Type u) (k : Type v) [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) : Prop where
  /-- Every overlap S-polynomial reduces to zero. -/
  overlap_resolves : ∀ (oc : OverlapComposition G k ord),
    oc.rule₁ ∈ sys.rules → oc.rule₂ ∈ sys.rules →
    ∃ nf, ReducesToNF ord sys oc.spoly nf ∧ nf.isZero
  /-- Every inclusion S-polynomial reduces to zero. -/
  inclusion_resolves : ∀ (ic : InclusionComposition G k ord),
    ic.inner ∈ sys.rules → ic.outer ∈ sys.rules →
    ∃ nf, ReducesToNF ord sys ic.spoly nf ∧ nf.isZero

/-! ### §5.1  Non-degeneracy

The acceptance test for the three repairs. Under the *old* definitions every
element reduced to zero (`SingleStepReduction` placed no condition on its
target), so `IsGrobnerShirshovBasis` held of every system and every statement
downstream of it was empty. It no longer does: as soon as no rule has an empty
leading monomial, the unit `1` is in normal form and is not zero, so it does
not reduce to zero. -/

/-- The unit is in normal form as soon as no rule's leading monomial is the
    empty word. -/
theorem isNormalForm_one {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    [DecidableEq k] (ord : AdmissibleOrder G) (sys : RewritingSystem G k)
    (h : ∀ r ∈ sys.rules, r.lm ord ≠ []) :
    isNormalForm ord sys (AlgElement.singleton ([] : Monomial G)) := by
  intro r hr m hm hinf
  have hm0 : m = [] := by
    by_contra hne
    exact hm (AlgElement.singleton_coeff_of_ne hne)
  subst hm0
  exact h r hr (List.eq_nil_of_infix_nil hinf)

/-- **`1` does not reduce to `0`.**  So `IsGrobnerShirshovBasis` is not
    satisfied by "everything reduces to zero", which is exactly how the
    unrepaired definitions made it hold of every system. -/
theorem one_not_reduces_to_zero {G : Type u} {k : Type v} [Ring k] [Nontrivial k]
    [DecidableEq G] [DecidableEq k] (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) (h : ∀ r ∈ sys.rules, r.lm ord ≠ []) :
    ¬ ∃ nf, ReducesToNF ord sys (AlgElement.singleton ([] : Monomial G)) nf
        ∧ nf.isZero := by
  rintro ⟨nf, ⟨hred, -⟩, hzero⟩
  have hnf := isNormalForm_one ord sys h
  have hnfeq : nf = AlgElement.singleton ([] : Monomial G) :=
    MultiStepReduction.eq_of_isNormalForm hnf hred
  subst hnfeq
  have h0 := hzero ([] : Monomial G)
  rw [AlgElement.singleton_coeff_self] at h0
  exact one_ne_zero h0

/-- **The repaired predicate is satisfiable, and not only by degenerate
    systems.**  A one-rule system whose leading monomial is a single letter is
    a Gröbner–Shirshov basis: the length of the leading monomial forces every
    composition to have empty contexts, so every S-polynomial is
    `lc • r − lc • r`, which is zero.

    Together with `one_not_reduces_to_zero` this brackets the predicate from
    both sides — it is neither vacuously true (as it was before the repair)
    nor vacuously false. -/
theorem isGrobnerShirshovBasis_of_single_letter_rule {G : Type u} {k : Type v}
    [Ring k] [DecidableEq G] (ord : AdmissibleOrder G) (r : ReductionRule G k)
    (g : G) (hlm : r.lm ord = [g]) :
    IsGrobnerShirshovBasis G k ord ⟨[r], by simp⟩ := by
  constructor
  · intro oc h₁ h₂
    have hr₁ : oc.rule₁ = r := by simpa using h₁
    have hr₂ : oc.rule₂ = r := by simpa using h₂
    have hd₁ : [g] = oc.left ++ oc.overlap := by rw [← hlm, ← hr₁]; exact oc.lm₁_decomp
    have hd₂ : [g] = oc.overlap ++ oc.right := by rw [← hlm, ← hr₂]; exact oc.lm₂_decomp
    have hov : oc.overlap.length ≠ 0 := by
      simpa [List.length_eq_zero_iff] using oc.overlap_nonempty
    have hl₁ := congrArg List.length hd₁
    have hl₂ := congrArg List.length hd₂
    simp only [List.length_cons, List.length_nil, List.length_append] at hl₁ hl₂
    have hleft : oc.left = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hright : oc.right = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hzero : oc.spoly.isZero := by
      intro m
      simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff,
        hleft, hright, hr₁, hr₂]
      exact sub_self _
    exact ⟨oc.spoly, ⟨MultiStepReduction.refl _,
      fun r' _ m hm => absurd (hzero m) hm⟩, hzero⟩
  · intro ic h₁ h₂
    have hr₁ : ic.inner = r := by simpa using h₁
    have hr₂ : ic.outer = r := by simpa using h₂
    have hd : [g] = ic.left ++ [g] ++ ic.right := by
      have h := ic.decomposition
      rw [hr₁, hr₂, hlm] at h
      exact h
    have hl := congrArg List.length hd
    simp only [List.length_cons, List.length_nil, List.length_append] at hl
    have hleft : ic.left = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hright : ic.right = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hzero : ic.spoly.isZero := by
      intro m
      simp only [InclusionComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff,
        hleft, hright, hr₁, hr₂, AlgElement.contextMul_nil_nil_coeff]
      exact sub_self _
    exact ⟨ic.spoly, ⟨MultiStepReduction.refl _,
      fun r' _ m hm => absurd (hzero m) hm⟩, hzero⟩

/-! ## §6  Existence of Normal Forms

**The `normal_form_exists` axiom that used to stand here was FALSE, and is
gone** (bean qou-lzoo). `NormalFormExistsRefutation.normal_form_exists_false`
proves its negation at `G = SU2Gen`, `k = ℤ`, sorry-free and depending on no
framework axiom. The counterexample is the one-rule system with relation `2·K`:
it *is* a Gröbner–Shirshov basis, and the element `K` is **stuck** — not in
normal form, because `isNormalForm` is a condition on monomials and the rule's
leading monomial occurs; yet admitting no step, because a step must also solve
`c · lc(r) = 1` with `lc(r) = 2`, and `2` is not a unit in `ℤ`.

The error was to read termination as "the stuck element is in normal form".
Termination gives only "no infinite reduction sequence"; the two coincide
exactly when every rule has an invertible leading coefficient — the hypothesis
Bergman 1978 Thm 1.2 carries and the axiom dropped. `hgs` was a red herring: the
counterexample satisfies it, so no confluence hypothesis could have rescued it.

`normal_form_exists` is now a **theorem** with that hypothesis, and `reduce` is
built from it, so nothing in the development rests on the false statement. -/

/-- **Termination**: every sequence of single-step reductions is finite.

    Each `SingleStepReduction` strictly decreases the multiset of monomials in
    the support under the Dershowitz–Manna ordering, which inherits
    well-foundedness from `ord.wf`.

    Axiomatised because the proof requires a `Multiset (Monomial G)`
    representation of `AlgElement` support, a proof that a step strictly
    decreases it, and the Dershowitz–Manna theorem — components that need
    subtraction and support extraction not available at this level.

    Lives here rather than in `CompositionLemma` because it is stated purely in
    this file's vocabulary and `normal_form_exists` below needs it.

    Reference: Bergman 1978, §2, proof of Theorem 1.1 (termination). -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 §2 Thm 1.1 (reduction is well-founded / terminating)
axiom reduction_well_founded {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) :
    ∀ (f : AlgElement G k), Acc (fun g h => SingleStepReduction ord sys h g) f

/-- **Existence of normal forms** — the repaired statement, and a theorem.

    Two differences from the axiom this replaces, and both matter:

    1. It carries `hlc`: every rule has a **unit leading coefficient**. Without
       it the statement is false (see the section note).
    2. It does **not** take `hgs`. Existence of normal forms is pure termination
       — reduce until stuck — and has nothing to do with confluence. The axiom's
       `hgs` argument was never used by the content, and carrying it obscured
       that the real missing hypothesis was elsewhere.

    Proof: well-founded induction on `reduction_well_founded`. At `x`, either `x`
    is already normal (done, in zero steps), or
    `exists_singleStep_of_not_isNormalForm` produces a step `x → y`, and the
    induction hypothesis applies at `y` precisely because `x → y`.

    Reference: Bergman 1978, Theorem 1.2 (existence part), where the rules are
    monic — which is what `hlc` restores. -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 Thm 1.2 (existence of normal forms via well-founded reduction, monic rules)
theorem normal_form_exists {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f : AlgElement G k) :
    ∃ (nf : AlgElement G k), ReducesToNF ord sys f nf := by
  induction (reduction_well_founded ord sys f) with
  | intro x _ ih =>
    by_cases hnf : isNormalForm ord sys x
    · exact ⟨x, MultiStepReduction.refl x, hnf⟩
    · obtain ⟨y, hxy⟩ := exists_singleStep_of_not_isNormalForm hlc hnf
      obtain ⟨nf, hred, hnorm⟩ := ih y hxy
      exact ⟨nf, MultiStepReduction.head hxy hred, hnorm⟩

/-- **Reduction function**: select *the* normal form of each element.

    Takes `hlc` (unit leading coefficients) rather than `hgs`: what makes the
    choice possible is existence, which is termination plus invertibility.
    Well-definedness of the *value* — that the choice does not matter — is
    `normal_form_unique`, and that is where `hgs` is genuinely needed. -/
noncomputable def reduce {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) :
    AlgElement G k → AlgElement G k :=
  fun f => (normal_form_exists ord sys hlc f).choose

/-- The reduction function produces normal forms. -/
theorem reduce_is_normal {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f : AlgElement G k) :
    isNormalForm ord sys (reduce ord sys hlc f) :=
  (normal_form_exists ord sys hlc f).choose_spec.is_normal

/-- The reduction function witnesses multi-step reduction. -/
theorem reduce_reduces {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f : AlgElement G k) :
    MultiStepReduction ord sys f (reduce ord sys hlc f) :=
  (normal_form_exists ord sys hlc f).choose_spec.reduces

/-! ## §7  Algebras without quasi-zeros  (bean qou-k6ks)

The folio's chapter carries this hypothesis throughout:

> Throughout, `R` is a commutative ring with unity and `A` is an `R`-algebra
> **without quasi-zeros** (i.e. elements `a ∈ A` such that `b a c = 0` for all
> `b, c ∈ A` not both `1`).

Source: Leitner–Pawloski, *Unital Gröbner Bases over Arbitrary Commutative
Ground Rings*, arXiv:math/0409565v2. In Lean it previously appeared only in
docstrings and on no declaration at all.

It is what stops a reduction from being vacuous: a quasi-zero is annihilated
by every non-trivial context, so an argument of the form "the S-polynomial
reduces to zero, hence the overlap is resolved" would be reading `0 = 0` off
a term that was never there. The hypothesis is threaded through the results
that need it — `local_confluence` and its consequences in
`CompositionLemma.lean` — and discharged where the algebra is concrete. -/

/-- **No quasi-zeros**, in the chapter's wording, for an abstract ring. -/
def NoQuasiZeros (A : Type*) [Ring A] : Prop :=
  ∀ a : A, (∀ b c : A, ¬(b = 1 ∧ c = 1) → b * a * c = 0) → a = 0

/-- Discharged whenever `-1 ≠ 1`: take the context `(b, c) = (1, -1)`.
    (The hypothesis is not idle — `NoQuasiZeros (ZMod 2)` is *false*, since
    every pair `(b,c) ≠ (1,1)` in `ZMod 2` has `b·c = 0`.) -/
theorem noQuasiZeros_of_neg_one_ne_one {A : Type*} [Ring A] (h : (-1 : A) ≠ 1) :
    NoQuasiZeros A := by
  intro a ha
  have := ha 1 (-1) (by rintro ⟨-, h'⟩; exact h h')
  simpa using this

/-- **No quasi-zeros for the free algebra `k⟨G⟩`**, with the contexts `b`, `c`
    taken to be monomials (which span, so this is the chapter's condition) and
    "not both `1`" reading as "not both the empty word". -/
def NoQuasiZerosFree (G : Type u) (k : Type v) [Ring k] [DecidableEq G] : Prop :=
  ∀ f : AlgElement G k,
    (∀ a b : Monomial G, ¬(a = [] ∧ b = []) →
      (AlgElement.contextMul a f b).isZero) → f.isZero

/-- **The free algebra on at least one generator has no quasi-zeros.**
    Left multiplication by a single generator is injective, which is all the
    condition needs. (With `G` empty the free algebra is `k` itself and the
    property can genuinely fail — there is then no non-trivial context at all,
    so the hypothesis of `NoQuasiZerosFree` is vacuous while its conclusion is
    not.) -/
theorem noQuasiZerosFree_of_generator {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] (g : G) : NoQuasiZerosFree G k := by
  intro f hf m
  have h := hf [g] [] (by rintro ⟨h1, -⟩; exact List.cons_ne_nil g [] h1) ([g] ++ m ++ [])
  rwa [AlgElement.contextMul_coeff_middle] at h

/-- **`NoQuasiZerosFree` says exactly `Nonempty G` — and therefore carries no
    algebraic content in this development** (bean qou-k6ks).

    The hypothesis is threaded through `local_confluence` and its consequences to
    record the manuscript's standing assumption. This equivalence measures what
    that threading actually buys, and the answer is: nothing beyond "the
    generating set is non-empty".

    * `←` is `noQuasiZerosFree_of_generator`: one generator gives an injective
      context, which is all the condition asks.
    * `→` is the degenerate direction. With `G` empty every monomial is `[]`, so
      *no* non-trivial context exists, the premise `¬(a = [] ∧ b = [])` is never
      satisfiable, and the condition degenerates to "every element is zero" —
      false for non-trivial `k`. So the property fails precisely when there is
      no generator.

    The reason it cannot do real work here is structural and worth stating:
    Leitner–Pawloski's `A` is the **quotient** `R⟨X⟩/I`, and a quasi-zero is a
    phenomenon of the quotient. This development's Gröbner–Shirshov framework
    works entirely in the free algebra, where — as this theorem shows — the
    condition is automatic. `Quotient.lean` now supplies `QuotAlg`, but only as a
    `Submodule` quotient; there is no ring structure on it yet, so the chapter's
    `NoQuasiZeros` cannot even be *stated* there. That, not the threading, is the
    missing piece. -/
theorem noQuasiZerosFree_iff_nonempty {G : Type u} {k : Type v} [Ring k]
    [Nontrivial k] [DecidableEq G] [DecidableEq k] :
    NoQuasiZerosFree G k ↔ Nonempty G := by
  constructor
  · intro h
    by_contra hemp
    rw [not_nonempty_iff] at hemp
    have hnil : ∀ m : Monomial G, m = [] := by
      intro m
      cases m with
      | nil => rfl
      | cons g _ => exact (hemp.false g).elim
    have hzero := h (AlgElement.singleton ([] : Monomial G))
      (fun a b hab => absurd ⟨hnil a, hnil b⟩ hab)
    have h0 := hzero ([] : Monomial G)
    rw [AlgElement.singleton_coeff_self] at h0
    exact one_ne_zero h0
  · rintro ⟨g⟩
    exact noQuasiZerosFree_of_generator g

/-! ## §6  Reduction respects `CoeffEq`, and negation

Two facts the family theorems keep needing, and one obstacle worth recording.

`AlgElement` is a representation: `CoeffEq` is the equality that means anything.
But `MultiStepReduction.refl` is **syntactic**, so a coefficientwise-equal source
cannot simply be substituted into a chain — `MultiStepReduction f' f` does not
follow from `CoeffEq f' f`. The way through is `congr_source` below, whose
conclusion is a *disjunction*: either the chain restarts at `f'`, or `f'` was
already coefficientwise the chain's endpoint. The `refl` case lands in the second
disjunct, which is exactly what the syntactic constructor costs.

With that, negating a rule of a composition — the `§4j` situation, where the
Yang–Baxter and Bokut–Shiao relations at `j = i − 1` are exact negatives with
opposite leading coefficients — carries a resolution across for free. -/

/-- A step only reads its source through `coeff`, so the source may be replaced
by any coefficientwise-equal element. -/
theorem SingleStepReduction.of_coeffEq_left {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f g f' : AlgElement G k} (hs : SingleStepReduction ord sys f g)
    (hf : AlgElement.CoeffEq f' f) : SingleStepReduction ord sys f' g := by
  obtain ⟨r, hr, a, b, c, hne, hc, hg⟩ := hs.exists_witness
  refine ⟨r, hr, a, b, c, ?_, ?_, ?_⟩
  · rw [hf]; exact hne
  · rw [hf]; exact hc
  · intro m
    rw [hg m]
    simp only [AlgElement.sub_coeff, hf m]

/-- Negating a step negates both ends: run the same rule with `-c`. -/
theorem SingleStepReduction.neg {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k} {f g : AlgElement G k}
    (hs : SingleStepReduction ord sys f g) :
    SingleStepReduction ord sys (AlgElement.neg f) (AlgElement.neg g) := by
  obtain ⟨r, hr, a, b, c, hne, hc, hg⟩ := hs.exists_witness
  refine ⟨r, hr, a, b, -c, ?_, ?_, ?_⟩
  · simpa using hne
  · show -c * r.lc ord = -(f.coeff _)
    rw [neg_mul, hc]
  · intro m
    simp only [AlgElement.neg_coeff]
    rw [hg m]
    simp only [AlgElement.sub_coeff, AlgElement.smul_coeff, AlgElement.neg_coeff]
    noncomm_ring

theorem MultiStepReduction.neg {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k} {f g : AlgElement G k}
    (hm : MultiStepReduction ord sys f g) :
    MultiStepReduction ord sys (AlgElement.neg f) (AlgElement.neg g) := by
  induction hm with
  | refl => exact MultiStepReduction.refl _
  | step _ hlast ih => exact ih.step hlast.neg

/-- **The source of a chain may be replaced up to `CoeffEq`** — or the
replacement was already the endpoint. The disjunction is forced by `refl` being
a syntactic constructor; it is not a weakness of the proof. -/
theorem MultiStepReduction.congr_source {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} {sys : RewritingSystem G k}
    {f nf f' : AlgElement G k} (hm : MultiStepReduction ord sys f nf)
    (hf : AlgElement.CoeffEq f' f) :
    MultiStepReduction ord sys f' nf ∨ AlgElement.CoeffEq f' nf := by
  induction hm with
  | refl => exact Or.inr hf
  | step _ hlast ih =>
    rcases ih with hm' | hce
    · exact Or.inl (hm'.step hlast)
    · exact Or.inl ((MultiStepReduction.refl _).step (hlast.of_coeffEq_left hce))

/-- Reducing to zero transfers along `CoeffEq`. -/
theorem reducesToZero_congr {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k} {f f' : AlgElement G k}
    (h : ∃ nf, ReducesToNF ord sys f nf ∧ nf.isZero)
    (hf : AlgElement.CoeffEq f' f) :
    ∃ nf, ReducesToNF ord sys f' nf ∧ nf.isZero := by
  obtain ⟨nf, ⟨hred, hnorm⟩, hzero⟩ := h
  rcases hred.congr_source hf with hm | hce
  · exact ⟨nf, ⟨hm, hnorm⟩, hzero⟩
  · exact reducesToNF_self_of_isZero (fun m => (hce m).trans (hzero m))

/-- …and along negation. -/
theorem reducesToZero_neg {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    {ord : AdmissibleOrder G} {sys : RewritingSystem G k} {f f' : AlgElement G k}
    (h : ∃ nf, ReducesToNF ord sys f nf ∧ nf.isZero)
    (hf : ∀ m, f'.coeff m = -(f.coeff m)) :
    ∃ nf, ReducesToNF ord sys f' nf ∧ nf.isZero := by
  obtain ⟨nf, ⟨hred, hnorm⟩, hzero⟩ := h
  refine reducesToZero_congr (f := AlgElement.neg f) ⟨AlgElement.neg nf, ⟨hred.neg, ?_⟩, ?_⟩ hf
  · intro r hr m hm
    exact hnorm r hr m (by simpa using hm)
  · intro m; simp [hzero m]

/-- **Negating either rule of an overlap composition negates its S-polynomial.**

`spoly = lc₂ • (rule₁ · right) − lc₁ • (left · rule₂)`, and negating a rule flips
both its relation and its leading coefficient — so the two occurrences of the
sign cancel in one term and reinforce in the other, giving `−spoly` either way.
-/
theorem OverlapComposition.spoly_coeff_neg_rule₁ {G : Type u} {k : Type v} [Ring k]
    [DecidableEq G] {ord : AdmissibleOrder G} (oc oc' : OverlapComposition G k ord)
    (hrel : ∀ w, oc'.rule₁.relation.coeff w = -(oc.rule₁.relation.coeff w))
    (hlc : oc'.rule₁.lc ord = -(oc.rule₁.lc ord))
    (hr₂ : oc'.rule₂ = oc.rule₂) (hl : oc'.left = oc.left) (hr : oc'.right = oc.right)
    (m : Monomial G) :
    oc'.spoly.coeff m = -(oc.spoly.coeff m) := by
  simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  rw [hr₂, hl, hr, hlc, AlgElement.contextMul_coeff_neg [] oc.right hrel m]
  noncomm_ring

end UGB.GrobnerShirshov
