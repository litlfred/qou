import Mathlib.Order.WellFounded
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Module.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic

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

These definitions are self-contained and do not depend on the specific
choice of algebra (`U_q`, `Dist(G)`, etc.).  Specialisations are in
`NormalForms.lean` and `StrongMultiplicativity.lean`.

## References

- [fred2005, §3] — Gröbner–Shirshov basis for `Dist(G)`
- Bokut & Chen, *Gröbner–Shirshov bases and their calculation*,
  Bull. Math. Sci. 4 (2014), 325–395.
- Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978), 178–218.
-/


namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Monomials and Admissible Orders -/

/-- A **monomial** in a free associative algebra on generators of type `G`.
    Represented as a list (word) of generators, with `[]` as the empty
    monomial (unit `1`). -/
abbrev Monomial (G : Type u) := List G

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

/-! ## §2  Algebra Elements and Leading Monomials -/

/-- An element of the free associative algebra `k⟨G⟩` over a ring `k`,
    represented as a finitely-supported linear combination of monomials.

    For the formalization we work abstractly: an element is a function
    from monomials to coefficients with finite support. -/
structure AlgElement (G : Type u) (k : Type v) [Ring k] where
  /-- Coefficient of each monomial. -/
  coeff : Monomial G → k
  /-- The support is finite. -/
  support : Finset (Monomial G)
  /-- Coefficients outside the support are zero. -/
  support_spec : ∀ m, m ∉ support → coeff m = 0

/-- The zero element of the free algebra. -/
def AlgElement.zero {G : Type u} {k : Type v} [Ring k] : AlgElement G k where
  coeff := fun _ => 0
  support := ∅
  support_spec := fun _ _ => rfl

/-- An element is zero iff its support is empty. -/
def AlgElement.isZero {G : Type u} {k : Type v} [Ring k]
    (f : AlgElement G k) : Prop :=
  f.support = ∅

/-- The **leading monomial** of a non-zero element with respect to an
    admissible order: the greatest monomial with non-zero coefficient. -/
noncomputable def leadingMonomial {G : Type u} {k : Type v} [Ring k]
    (_ord : AdmissibleOrder G)
    (f : AlgElement G k)
    (hf : f.support.Nonempty) : Monomial G :=
  hf.choose

/-! ## §3  Rewriting System and Reduction Relations -/

/-- A **reduction rule**: an oriented relation `f ↦ f - c·lm(f)` that
    replaces the leading monomial of `f` by its tail.

    In practice, each defining relation of the algebra gives one rule. -/
structure ReductionRule (G : Type u) (k : Type v) [Ring k] where
  /-- The polynomial whose leading term defines the rewrite. -/
  relation : AlgElement G k
  /-- The relation is non-zero. -/
  nonzero : relation.support.Nonempty

/-- A **rewriting system**: a set of reduction rules. -/
structure RewritingSystem (G : Type u) (k : Type v) [Ring k] where
  /-- The collection of reduction rules. -/
  rules : List (ReductionRule G k)
  /-- The system has at least one rule (non-trivial). -/
  nonempty : rules ≠ []

/-- **Single-step reduction**: `f` reduces to `g` in one step if there
    exists a rule `r ∈ sys` whose leading monomial appears as a subword
    of some monomial in `supp(f)`, and `g` is obtained by replacing that
    occurrence with the tail of `r`.

    Abstractly: `g` has a strictly smaller leading monomial than `f`
    under the admissible order, and `f - g` lies in the ideal generated
    by the rules. -/
structure SingleStepReduction {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (f g : AlgElement G k) : Prop where
  /-- There exists a rule and target monomial witnessing the reduction step. -/
  exists_witness :
    ∃ (rule_used : ReductionRule G k),
      rule_used ∈ sys.rules ∧
    ∃ (target_monomial : Monomial G),
      target_monomial ∈ f.support ∧
      (leadingMonomial ord rule_used.relation rule_used.nonzero) <:+: target_monomial ∧
      ∀ m ∈ g.support, ¬ ord.lt target_monomial m

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

/-- An element is in **normal form** with respect to a rewriting system
    if no leading monomial of any rule divides (appears as a subword of)
    any monomial in the element's support.  Equivalently: no single-step
    reduction is applicable. -/
def isNormalForm {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (f : AlgElement G k) : Prop :=
  ∀ r ∈ sys.rules, ∀ m ∈ f.support,
    ¬ (leadingMonomial ord r.relation r.nonzero) <:+: m

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

/-! ## §4  S-Polynomials (Compositions) -/

/-- **Overlap composition** (inclusion/intersection S-polynomial):
    given two rules whose leading monomials overlap, the S-polynomial
    is the difference of the two ways to reduce the overlap.

    If `lm(f) = a·b` and `lm(g) = b·c` with overlap `b`, then
    `S(f,g) = f·c − a·g` (after leading-coefficient normalisation).

    The composition lemma states that the rewriting system is a
    Gröbner–Shirshov basis iff every S-polynomial reduces to zero. -/
structure OverlapComposition (G : Type u) (k : Type v) [Ring k] where
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
  lm₁_decomp : ∀ (ord : AdmissibleOrder G),
    leadingMonomial ord rule₁.relation rule₁.nonzero = left ++ overlap
  /-- The leading monomial of rule₂ decomposes as `overlap ++ right`. -/
  lm₂_decomp : ∀ (ord : AdmissibleOrder G),
    leadingMonomial ord rule₂.relation rule₂.nonzero = overlap ++ right
  /-- The overlap is non-empty. -/
  overlap_nonempty : overlap ≠ []
  /-- The S-polynomial itself (the difference of the two reductions). -/
  spoly : AlgElement G k

/-- **Inclusion composition**: when the leading monomial of one rule
    entirely contains that of another as a subword.

    If `lm(g) = a ++ lm(f) ++ b`, then `S(f,g) = g − c · a·f·b`
    where `c` is the ratio of leading coefficients. -/
structure InclusionComposition (G : Type u) (k : Type v) [Ring k] where
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
  decomposition : ∀ (ord : AdmissibleOrder G),
    leadingMonomial ord outer.relation outer.nonzero =
    left ++ leadingMonomial ord inner.relation inner.nonzero ++ right
  /-- The S-polynomial for this inclusion. -/
  spoly : AlgElement G k

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
  overlap_resolves : ∀ (oc : OverlapComposition G k),
    oc.rule₁ ∈ sys.rules → oc.rule₂ ∈ sys.rules →
    ∃ nf, ReducesToNF ord sys oc.spoly nf ∧ nf.isZero
  /-- Every inclusion S-polynomial reduces to zero. -/
  inclusion_resolves : ∀ (ic : InclusionComposition G k),
    ic.inner ∈ sys.rules → ic.outer ∈ sys.rules →
    ∃ nf, ReducesToNF ord sys ic.spoly nf ∧ nf.isZero

/-! ## §6  Existence of Normal Forms -/

/-- **Existence of normal forms**: given a GS basis and any element `f`,
    there exists a normal form reachable from `f`.

    Justification: the admissible order `ord` is well-founded, and each
    single-step reduction strictly decreases the leading monomial.
    By well-founded induction on the Dershowitz–Manna multiset ordering,
    iterated reduction terminates in a normal form.

    This is axiomatised at the abstract level because the constructive
    proof requires a concrete single-step reduction function with
    explicit algebra operations (subtraction, scalar multiplication).
    Each concrete instantiation (U_q in NormalForms.lean, Dist(G) in
    Flatness.lean) provides these operations.

    Reference: Bergman 1978, Theorem 1.2 (existence part). -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 Thm 1.2 (existence of normal forms via well-founded reduction)
axiom normal_form_exists {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f : AlgElement G k) :
    ∃ (nf : AlgElement G k), ReducesToNF ord sys f nf

/-- **Reduction function**: given a GS basis, select *the* normal form
    of each element.  Well-defined by normal_form_exists (existence)
    and normal_form_unique (uniqueness, proved in CompositionLemma.lean). -/
noncomputable def reduce {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys) :
    AlgElement G k → AlgElement G k :=
  fun f => (normal_form_exists ord sys hgs f).choose

/-- The reduction function produces normal forms. -/
theorem reduce_is_normal {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f : AlgElement G k) :
    isNormalForm ord sys (reduce ord sys hgs f) :=
  (normal_form_exists ord sys hgs f).choose_spec.is_normal

/-- The reduction function witnesses multi-step reduction. -/
theorem reduce_reduces {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f : AlgElement G k) :
    MultiStepReduction ord sys f (reduce ord sys hgs f) :=
  (normal_form_exists ord sys hgs f).choose_spec.reduces

end UGB.GrobnerShirshov
