import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.AlgOps
import UGB.GrobnerShirshov.CompositionLemma
import Mathlib.Data.Real.Basic
import Mathlib.Logic.Function.Basic
import Mathlib.Tactic.Abel
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# The Hecke relations, and why they are not a Gröbner–Shirshov basis

Instantiation of the abstract GS framework for the Hecke algebra `H_n(q)`.

## The headline

`hecke_is_gs_basis` — the axiom that used to sit at §4, asserting that
`heckeRewritingSystem` is a GS basis and citing Bokut & Shiao 2001, Thm 3.5 —
**is false**, and has been deleted. `NotAGSBasis.hecke_not_gs_basis_four`
refutes it at `n = 4` with a machine-checked counterexample: the overlap of
the Yang–Baxter rule `σ₃σ₂σ₃ → σ₂σ₃σ₂` with the far-commutation rule
`σ₃σ₁ → σ₁σ₃` has S-polynomial `σ₂σ₃σ₂σ₁ − σ₃σ₂σ₁σ₃`, and both of those words
are irreducible for the system. So the system is not confluent.

This is the *known* situation for Coxeter presentations: Bokut & Shiao's
theorem produces a GS basis by completing the presentation with the family
`σᵢσᵢ₋₁⋯σⱼσᵢ → σᵢ₋₁σᵢσᵢ₋₁⋯σⱼ`; `heckeRewritingSystem` contains only the
defining relations, so the cited theorem never applied to it. The axiom was
previously *vacuous* (the unrepaired `SingleStepReduction` let everything
reduce to zero) rather than false; repairing the definitions turned it into a
falsehood, which is why it had to go rather than stay as an assumption.

Everything downstream that used it — `heckeCost_well_defined`,
`threading_cost_unique` — now takes the GS property as an explicit hypothesis.

**The completion exists and is proved** (2026-08-24, bean `qou-auq3`).
`HeckeCompletion.lean` adjoins the Bokut–Shiao family to this system and proves
`heckeCompleted_isGrobnerShirshovBasis` for every `n` and every `HeckeParams`,
with no hypothesis and no `sorry`. So the two theorems below are not merely
conditional-and-parked: their completed-system counterparts,
`heckeCompleted_normalForm_unique` and `heckeCompleted_threading_cost_unique`
(§4bx there), hold outright, up to `CoeffEq`, with no axiom beyond Lean's
three: the Diamond Lemma is proved in `DiamondLemma.lean` (2026-11-20).

## Axiom budget

| Item | Status | Justification |
|------|--------|---------------|
| `heckeOrder` | **def** | `mkDegLexOrder` from AlgOps.lean (generic deg-lex) |
| `heckeRewritingSystem` | **def** | Built from `AlgElement.ofTerms`; needs `0 < n`, no sentinel |
| `heckeRelation_lm`, `yangBaxterRelation_lm`, `farCommRelation_lm` | **theorem** | computed leading monomials (§4a) |
| `heckeRewritingSystem_lm_cases` | **theorem** | classification of the system's leading monomials |
| `gs_basis_of_empty_lm` | **theorem** | why the sentinel had to go |
| `one_does_not_reduce_to_zero` | **theorem** | non-degeneracy of the repaired predicate |
| `hecke_not_gs_basis_four` | **theorem** | the refutation (§4e) |
| `embedGenerator`, `braidLettersToAlg`, `braidToAlg`, `augmentedBraidElement`, `heckeCost` | **def** | σ⁻¹ and photon-sign corrected 2026-11-15 (§5) |

No axiom is declared in this file. The framework results it *uses* live in
`Basic.lean` (`normal_form_exists`, `reduction_well_founded` — both theorems)
and `CompositionLemma.lean` (`local_confluence`, `confluence`,
`normal_form_unique` — theorems up to `CoeffEq` since 2026-11-20); the
refutation above depends on none of them.

## References

- Bokut & Shiao, "Gröbner–Shirshov bases for Coxeter groups",
  Comm. Algebra 29 (2001), 4305–4319.
-/


namespace UGB.GrobnerShirshov.Hecke

open UGB.GrobnerShirshov

/-! ## §1  Hecke Generators -/

/-- Generator type for the Hecke algebra `H_n(q)`.
    For `n` strands, there are `n` generators `σ₀,…,σ_{n-1}`. -/
structure HeckeGen (n : ℕ) where
  /-- Generator index (0-based). -/
  index : Fin n
deriving DecidableEq

/-- The rank of a Hecke generator (for deg-lex ordering). -/
def HeckeGen.rank {n : ℕ} (g : HeckeGen n) : ℕ := g.index.val

/-- Shorthand: create a Hecke generator from a natural number index.
    Returns the generator `σ_i` when `i < n`. -/
def σ {n : ℕ} (i : Fin n) : HeckeGen n := ⟨i⟩

/-! ## §2  Admissible Order -/

/-- The rank function for `HeckeGen n` is injective. -/
theorem HeckeGen.rank_injective {n : ℕ} :
    Function.Injective (HeckeGen.rank (n := n)) := by
  intro ⟨a⟩ ⟨b⟩ h
  simp [HeckeGen.rank] at h
  exact congrArg HeckeGen.mk (Fin.ext h)

/-- The deg-lex admissible order on Hecke monomials.
    Constructed via the generic `mkDegLexOrder` from AlgOps.lean,
    reusing the same proof infrastructure as `degLexOrder` for
    `SU2Gen` in NormalForms.lean. -/
noncomputable def heckeOrder (n : ℕ) : AdmissibleOrder (HeckeGen n) :=
  mkDegLexOrder HeckeGen.rank HeckeGen.rank_injective

/-! ## §3  Hecke Parameters -/

/-- Deformation parameter for the Hecke algebra. -/
structure HeckeParams where
  /-- The deformation parameter `q`. -/
  q : ℝ
  /-- `q > 0`. -/
  q_pos : 0 < q
  /-- `q ≠ 1` (non-classical). -/
  q_ne_one : q ≠ 1

/-! ## §4  Hecke Rewriting System (Constructive) -/

/-- The Hecke relation for generator `σᵢ`:
    `σᵢ² - (q - q⁻¹)σᵢ - 1 = 0`, oriented as
    `σᵢ² → (q - q⁻¹)σᵢ + 1`.

    As an `AlgElement`: leading monomial `[σᵢ, σᵢ]` with coefficient 1,
    plus `[σᵢ]` with coefficient `-(q - q⁻¹)`, plus `[]` with
    coefficient `-1`. -/
noncomputable def heckeRelation {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    ([⟨i⟩, ⟨i⟩], 1),
    ([⟨i⟩], -(hp.q - hp.q⁻¹)),
    ([], -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The Yang–Baxter relation for adjacent generators `σᵢ, σᵢ₊₁`:
    `σᵢσᵢ₊₁σᵢ - σᵢ₊₁σᵢσᵢ₊₁ = 0`, oriented as
    `σᵢσᵢ₊₁σᵢ → σᵢ₊₁σᵢσᵢ₊₁`. -/
noncomputable def yangBaxterRelation {n : ℕ}
    (i : Fin n) (j : Fin n) : ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    ([⟨i⟩, ⟨j⟩, ⟨i⟩], 1),
    ([⟨j⟩, ⟨i⟩, ⟨j⟩], -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The far-commutativity relation for non-adjacent generators:
    `σᵢσⱼ - σⱼσᵢ = 0` when `|i-j| ≥ 2`, oriented so that the
    higher-index generator comes first (lm = `[σᵢ, σⱼ]` with `i > j`). -/
noncomputable def farCommRelation {n : ℕ}
    (i : Fin n) (j : Fin n) : ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    ([⟨i⟩, ⟨j⟩], 1),
    ([⟨j⟩, ⟨i⟩], -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The complete Hecke rewriting system for `H_n(q)`.
    Collects all Hecke, Yang–Baxter, and far-commutativity relations
    for generators `σ₀, …, σ_{n-1}`.

    **Requires `0 < n`, and carries no sentinel rule.** An earlier version
    appended `⟨ofTerms [([], q)], _⟩` to satisfy `RewritingSystem.nonempty` at
    `n = 0`. That rule's support is `{[]}`, so its leading monomial is the empty
    word, and `[] <:+: m` holds for every `m` — which made `isNormalForm` false
    for every element with non-empty support and collapsed the whole GS property
    (`gs_basis_of_empty_lm` below proves the collapse). With `0 < n` the Hecke
    relation for `σ₀` supplies the non-emptiness instead, and every leading
    monomial is a genuine word. `n = 0` is no loss: `H_0(q)` has no generators. -/
noncomputable def heckeRules (n : ℕ) (hp : HeckeParams) :
    List (ReductionRule (HeckeGen n) ℝ) :=
    -- Hecke relations: σᵢ² → (q-q⁻¹)σᵢ + 1 for each i
    (List.finRange n).map (fun i => heckeRelation i hp) ++
    -- Yang–Baxter: σᵢσᵢ₊₁σᵢ → σᵢ₊₁σᵢσᵢ₊₁ for adjacent pairs
    ((List.finRange n).flatMap (fun i =>
      (List.finRange n).filterMap (fun j =>
        if j.val = i.val + 1 then some (yangBaxterRelation i j) else none))) ++
    -- Far-commutativity: σᵢσⱼ → σⱼσᵢ for |i-j| ≥ 2, i > j
    ((List.finRange n).flatMap (fun i =>
      (List.finRange n).filterMap (fun j =>
        if i.val > j.val + 1 then some (farCommRelation i j) else none)))

theorem heckeRules_ne_nil (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    heckeRules n hp ≠ [] := by
    -- `0 < n` makes `finRange n` non-empty, so the Hecke-relation block is too.
    intro h
    have h1 := (List.append_eq_nil_iff.mp h).1
    have h2 := (List.append_eq_nil_iff.mp h1).1
    rw [List.map_eq_nil_iff] at h2
    exact absurd h2 (List.ne_nil_of_length_pos (by rw [List.length_finRange]; exact hn))

/-- The Hecke rewriting system: the finite rule list `heckeRules` as a
    `RewritingSystem`. Requires `0 < n` (see `heckeRules`). -/
noncomputable def heckeRewritingSystem (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    RewritingSystem (HeckeGen n) ℝ :=
  .ofList (heckeRules n hp) (heckeRules_ne_nil n hn hp)

/-! ### Why there is no sentinel rule

The composition lemma is stated in terms of leading monomials, and a rule whose
leading monomial is the **empty word** destroys it. `isNormalForm` asks that no
rule's leading monomial be an infix of any monomial of the element; `[] <:+: m`
holds for every `m`; so with such a rule present *nothing non-zero is ever in
normal form*, and every element reduces to zero. The consequence is proved
below, in general rather than for this system: `gs_basis_of_empty_lm`.

That is why `heckeRewritingSystem` requires `0 < n` and drops the sentinel.
-/

/-! ## §4a  Leading monomials of the three rule families

With `leadingMonomial` repaired (it is now the `ord`-greatest support element,
not an arbitrary one) the leading monomials are computable facts rather than
intentions, and one of them is not what the docstrings said:

* `heckeRelation i` has leading monomial `[σᵢ, σᵢ]` — as intended;
* `farCommRelation i j` (`j < i`) has leading monomial `[σᵢ, σⱼ]` — as intended;
* `yangBaxterRelation i j` (`i < j`) has leading monomial **`[σⱼ, σᵢ, σⱼ]`**,
  not `[σᵢ, σⱼ, σᵢ]`. Deg-lex ranks `σⱼ` above `σᵢ`, so of the two words of
  length 3 the *larger* is the one starting with the larger generator. The
  rule therefore rewrites `σᵢ₊₁σᵢσᵢ₊₁ → σᵢσᵢ₊₁σᵢ`, the reverse of the
  orientation stated in its docstring. The orientation is still admissible
  (the leading monomial dominates the tail); only the prose was wrong. -/

/-- Shorter words are smaller in the deg-lex order. -/
theorem heckeOrder_lt_of_length {n : ℕ} {a b : Monomial (HeckeGen n)}
    (h : a.length < b.length) : (heckeOrder n).lt a b := Or.inl h

/-- Equal-length words compare lexicographically by generator rank. -/
theorem heckeOrder_lt_of_lex {n : ℕ} {a b : Monomial (HeckeGen n)}
    (hlen : a.length = b.length)
    (hlex : List.Lex (fun x y : HeckeGen n => HeckeGen.rank x < HeckeGen.rank y) a b) :
    (heckeOrder n).lt a b := Or.inr ⟨hlen, hlex⟩

/-- `lm(σᵢ² − (q−q⁻¹)σᵢ − 1) = [σᵢ, σᵢ]`. -/
theorem heckeRelation_lm {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    (heckeRelation i hp).lm (heckeOrder n) = [⟨i⟩, ⟨i⟩] := by
  apply leadingMonomial_eq_of_max
  · simp [heckeRelation, AlgElement.ofTerms]
  · intro m hm hne
    simp [heckeRelation, AlgElement.ofTerms] at hm
    rcases hm with rfl | rfl | rfl
    · exact absurd rfl hne
    · exact heckeOrder_lt_of_length (by simp)
    · exact heckeOrder_lt_of_length (by simp)

/-- `lm(σᵢσⱼσᵢ − σⱼσᵢσⱼ) = [σⱼ, σᵢ, σⱼ]` when `i < j` — the *reverse* of the
    orientation claimed by `yangBaxterRelation`'s docstring. -/
theorem yangBaxterRelation_lm {n : ℕ} (i j : Fin n) (hij : i.val < j.val) :
    (yangBaxterRelation i j).lm (heckeOrder n) = [⟨j⟩, ⟨i⟩, ⟨j⟩] := by
  apply leadingMonomial_eq_of_max
  · simp [yangBaxterRelation, AlgElement.ofTerms]
  · intro m hm hne
    simp [yangBaxterRelation, AlgElement.ofTerms] at hm
    rcases hm with rfl | rfl
    · exact heckeOrder_lt_of_lex (by simp)
        (List.Lex.rel (by simpa [HeckeGen.rank] using hij))
    · exact absurd rfl hne

/-- `lm(σᵢσⱼ − σⱼσᵢ) = [σᵢ, σⱼ]` when `j < i`. -/
theorem farCommRelation_lm {n : ℕ} (i j : Fin n) (hij : j.val < i.val) :
    (farCommRelation i j).lm (heckeOrder n) = [⟨i⟩, ⟨j⟩] := by
  apply leadingMonomial_eq_of_max
  · simp [farCommRelation, AlgElement.ofTerms]
  · intro m hm hne
    simp [farCommRelation, AlgElement.ofTerms] at hm
    rcases hm with rfl | rfl
    · exact absurd rfl hne
    · exact heckeOrder_lt_of_lex (by simp)
        (List.Lex.rel (by simpa [HeckeGen.rank] using hij))

/-! ## §4b  Classification of the system's rules, and of their leading monomials

Membership in `heckeRewritingSystem` is three list operations deep: a `map` for
the quadratic family, and for each of the other two a `flatMap` over a
`filterMap` whose `if` carries that family's side condition. Every proof that
begins from `r ∈ rules` has to unpick that, and until now each one did it inline.

`mem_heckeRewritingSystem_rules` does it once, and inverts to the **rule** —
`r = heckeRelation i hp`, not merely `r.lm = [σᵢ, σᵢ]`. The distinction is not
cosmetic. `OverlapComposition.spoly` is computed from `rule.relation` and
`rule.lc`, so an inversion that stops at the leading monomial cannot reach it;
and the *completed* system carries two distinct rules on one leading monomial
(`HeckeCompletion` §4j puts `yangBaxterRelation i' i` and
`bokutShiaoRelation i' i i'` on the same word), so there the lm does not
determine the rule at all. The leading-monomial classification is recovered
below as a corollary. -/

/-- **Every rule of `heckeRewritingSystem` is one of the three relations**, with
its indices and its side condition. This is the inversion of the three `_mem`
lemmas, and unlike `heckeRewritingSystem_lm_cases` it lands on the rule itself,
which is what any statement about `spoly` needs. -/
theorem mem_heckeRewritingSystem_rules {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {r : ReductionRule (HeckeGen n) ℝ}
    (hr : r ∈ (heckeRewritingSystem n hn hp).rules) :
    (∃ i : Fin n, r = heckeRelation i hp)
    ∨ (∃ i j : Fin n, j.val = i.val + 1 ∧ r = yangBaxterRelation i j)
    ∨ (∃ i j : Fin n, j.val + 1 < i.val ∧ r = farCommRelation i j) := by
  simp only [heckeRewritingSystem, RewritingSystem.mem_ofList_rules, heckeRules, List.mem_append, List.mem_map,
    List.mem_flatMap, List.mem_filterMap, List.mem_finRange, true_and] at hr
  rcases hr with (⟨i, hi⟩ | ⟨i, j, hj⟩) | ⟨i, j, hj⟩
  · exact Or.inl ⟨i, hi.symm⟩
  · by_cases hc : j.val = i.val + 1
    · simp only [hc] at hj
      exact Or.inr (Or.inl ⟨i, j, hc, (Option.some.injEq _ _ ▸ hj).symm⟩)
    · simp only [if_neg hc] at hj
      exact Option.noConfusion hj
  · by_cases hc : i.val > j.val + 1
    · simp only [if_pos hc] at hj
      exact Or.inr (Or.inr ⟨i, j, hc, (Option.some.injEq _ _ ▸ hj).symm⟩)
    · simp only [if_neg hc] at hj
      exact Option.noConfusion hj

/-- Every rule of `heckeRewritingSystem` is one of the three families, and its
    leading monomial is the explicit word listed here. -/
theorem heckeRewritingSystem_lm_cases {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeRewritingSystem n hn hp).rules) :
    (∃ i : Fin n, r.lm (heckeOrder n) = [⟨i⟩, ⟨i⟩]) ∨
    (∃ i j : Fin n, j.val = i.val + 1 ∧ r.lm (heckeOrder n) = [⟨j⟩, ⟨i⟩, ⟨j⟩]) ∨
    (∃ i j : Fin n, j.val + 1 < i.val ∧ r.lm (heckeOrder n) = [⟨i⟩, ⟨j⟩]) := by
  rcases mem_heckeRewritingSystem_rules hn hp hr with
    ⟨i, rfl⟩ | ⟨i, j, hj, rfl⟩ | ⟨i, j, hj, rfl⟩
  · exact Or.inl ⟨i, heckeRelation_lm i hp⟩
  · exact Or.inr (Or.inl ⟨i, j, hj, yangBaxterRelation_lm i j (by omega)⟩)
  · exact Or.inr (Or.inr ⟨i, j, hj, farCommRelation_lm i j (by omega)⟩)

/-- No rule of the Hecke system has an empty leading monomial. -/
theorem heckeRewritingSystem_lm_ne_nil {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeRewritingSystem n hn hp).rules) :
    r.lm (heckeOrder n) ≠ [] := by
  rcases heckeRewritingSystem_lm_cases hn hp r hr with
    ⟨i, h⟩ | ⟨i, j, -, h⟩ | ⟨i, j, -, h⟩ <;> rw [h] <;> simp

/-! ## §4c  A rule with empty leading monomial collapses everything -/

/-- **A rule that is a non-zero scalar collapses the GS property.**

If some rule's leading monomial is `[]` and its constant term is invertible —
which is exactly what the removed sentinel `⟨ofTerms [([], q)], _⟩` was — then
*every* element of the free algebra reduces to zero and
`IsGrobnerShirshovBasis` holds for any generators, any order, any rules. The
predicate then distinguishes nothing.

Two remarks on the statement, relative to the version proved against the
*unrepaired* definitions:

* the hypothesis `lc ≠ 0` is new and is needed. Previously
  `SingleStepReduction` imposed no algebraic condition, so a rule with empty
  leading monomial rewrote anything to anything; now a step must subtract an
  actual multiple of the relation, and a relation with vanishing constant term
  subtracts nothing. The removed sentinel satisfies it (`q > 0`).
* the support hypothesis one might expect — that the relation is supported on
  `[]` alone — is *not* needed: `AdmissibleOrder.not_lt_nil` shows the empty
  word is the minimum of every admissible order, so a relation whose leading
  monomial is `[]` has no other monomials at all. -/
theorem gs_basis_of_empty_lm {G : Type*} [DecidableEq G]
    (ord : AdmissibleOrder G) (sys : RewritingSystem G ℝ)
    (r₀ : ReductionRule G ℝ) (hr₀ : r₀ ∈ sys.rules)
    (hlm : r₀.lm ord = []) (hlc : r₀.lc ord ≠ 0) :
    IsGrobnerShirshovBasis G ℝ ord sys := by
  classical
  have hlm' : leadingMonomial ord r₀.relation r₀.nonzero = [] := hlm
  have hlceq : r₀.lc ord = r₀.relation.coeff [] := by
    show r₀.relation.coeff (leadingMonomial ord r₀.relation r₀.nonzero)
      = r₀.relation.coeff []
    rw [hlm']
  -- The relation is a scalar: the empty word is the minimum of any admissible
  -- order, so nothing else can sit in its support.
  have hzero_off : ∀ m : Monomial G, m ≠ [] → r₀.relation.coeff m = 0 := by
    intro m hm
    by_contra hne
    have hlt := lt_leadingMonomial_of_coeff_ne_zero ord r₀.relation r₀.nonzero hne
      (by rw [hlm']; exact hm)
    rw [hlm'] at hlt
    exact ord.not_lt_nil m hlt
  -- Hence `a · r₀ · 1` is the scalar `lc` sitting on the single word `a`.
  have hctx : ∀ a m : Monomial G,
      (AlgElement.contextMul a r₀.relation []).coeff m
        = if m = a then r₀.lc ord else 0 := by
    intro a m
    have hmid := AlgElement.contextMul_coeff_middle a ([] : Monomial G)
      ([] : Monomial G) r₀.relation
    simp only [List.append_nil] at hmid
    by_cases hm : m = a
    · rw [if_pos hm, hm, hmid, hlceq]
    · rw [if_neg hm]
      by_contra hne
      obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape hne
      have hw0 : w = [] := by
        by_contra h0
        exact hwne (hzero_off w h0)
      rw [hw0] at hw
      simp only [List.append_nil] at hw
      exact hm hw
  -- Peel one non-zero coefficient off at a time.
  have key : ∀ (N : ℕ) (f : AlgElement G ℝ),
      (f.support.filter (fun m => f.coeff m ≠ 0)).card ≤ N →
      ∃ nf, MultiStepReduction ord sys f nf ∧ nf.isZero := by
    intro N
    induction N with
    | zero =>
      intro f hcard
      refine ⟨f, MultiStepReduction.refl f, fun m => ?_⟩
      by_contra hne
      have hmem : m ∈ f.support.filter (fun m => f.coeff m ≠ 0) :=
        Finset.mem_filter.mpr ⟨AlgElement.mem_support_of_coeff_ne_zero hne, hne⟩
      rw [Nat.le_zero, Finset.card_eq_zero] at hcard
      rw [hcard] at hmem
      exact Finset.notMem_empty m hmem
    | succ N ih =>
      intro f hcard
      by_cases hz : f.isZero
      · exact ⟨f, MultiStepReduction.refl f, hz⟩
      · obtain ⟨m₀, hm₀⟩ : ∃ m, f.coeff m ≠ 0 := by
          by_contra hcon
          push_neg at hcon
          exact hz hcon
        have hmem₀ : m₀ ∈ f.support.filter (fun m => f.coeff m ≠ 0) :=
          Finset.mem_filter.mpr ⟨AlgElement.mem_support_of_coeff_ne_zero hm₀, hm₀⟩
        have hstep : SingleStepReduction ord sys f (f.eraseCoeff m₀) := by
          refine ⟨r₀, hr₀, m₀, [], f.coeff m₀ / r₀.lc ord, ?_, ?_, ?_⟩
          · rw [hlm]; simpa using hm₀
          · rw [hlm]
            simp only [List.append_nil]
            exact div_mul_cancel₀ _ hlc
          · intro m
            simp only [AlgElement.sub_coeff, AlgElement.smul_coeff, hctx]
            by_cases hm : m = m₀
            · rw [hm, AlgElement.eraseCoeff_self, if_pos rfl,
                div_mul_cancel₀ _ hlc, sub_self]
            · rw [AlgElement.eraseCoeff_of_ne hm, if_neg hm]
              ring
        have hsub : (f.eraseCoeff m₀).support.filter
              (fun m => (f.eraseCoeff m₀).coeff m ≠ 0)
            ⊆ (f.support.filter (fun m => f.coeff m ≠ 0)).erase m₀ := by
          intro m hm
          rw [Finset.mem_filter] at hm
          obtain ⟨hmem, hne⟩ := hm
          have hmne : m ≠ m₀ := by
            intro h
            rw [h] at hne
            exact hne (AlgElement.eraseCoeff_self f m₀)
          rw [AlgElement.eraseCoeff_of_ne hmne] at hne
          exact Finset.mem_erase.mpr ⟨hmne, Finset.mem_filter.mpr ⟨hmem, hne⟩⟩
        have hcard' : ((f.eraseCoeff m₀).support.filter
            (fun m => (f.eraseCoeff m₀).coeff m ≠ 0)).card ≤ N := by
          have h1 := Finset.card_le_card hsub
          have h2 := Finset.card_erase_of_mem hmem₀
          rw [h2] at h1
          have h3 : 0 < (f.support.filter (fun m => f.coeff m ≠ 0)).card :=
            Finset.card_pos.mpr ⟨m₀, hmem₀⟩
          omega
        obtain ⟨nf, hred, hzero⟩ := ih _ hcard'
        exact ⟨nf, MultiStepReduction.head hstep hred, hzero⟩
  have collapse : ∀ f : AlgElement G ℝ,
      ∃ nf, ReducesToNF ord sys f nf ∧ nf.isZero := by
    intro f
    obtain ⟨nf, hred, hzero⟩ := key _ f le_rfl
    exact ⟨nf, ⟨hred, fun r _ m hm => absurd (hzero m) hm⟩, hzero⟩
  exact ⟨fun oc _ _ => collapse oc.spoly, fun ic _ _ => collapse ic.spoly⟩

/-! ## §4d  Non-degeneracy: the repaired predicate has content -/

/-- **The unit does not reduce to zero.**  This is the acceptance test for the
    three repairs of `Basic.lean` (bean qou-auq3): under the old definitions
    every element reduced to zero, so `IsGrobnerShirshovBasis` was satisfied by
    every rewriting system whatsoever. It is not any more. -/
theorem one_does_not_reduce_to_zero (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    ¬ ∃ nf, ReducesToNF (heckeOrder n) (heckeRewritingSystem n hn hp)
        (AlgElement.singleton ([] : Monomial (HeckeGen n))) nf ∧ nf.isZero :=
  one_not_reduces_to_zero (heckeOrder n) (heckeRewritingSystem n hn hp)
    (heckeRewritingSystem_lm_ne_nil hn hp)

/-- The unit is in normal form for the Hecke system. -/
theorem one_isNormalForm (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    isNormalForm (heckeOrder n) (heckeRewritingSystem n hn hp)
      (AlgElement.singleton ([] : Monomial (HeckeGen n))) :=
  isNormalForm_one (heckeOrder n) (heckeRewritingSystem n hn hp)
    (heckeRewritingSystem_lm_ne_nil hn hp)

/-! ## §4e  The Hecke relations are **not** a Gröbner–Shirshov basis

`hecke_is_gs_basis` used to be an axiom here, citing Bokut & Shiao 2001,
Theorem 3.5. With the definitions repaired the statement is not merely
unproved — it is **false**, and the axiom has been removed rather than left in
place. What follows is the machine-checked refutation at `n = 4`.

The obstruction is the overlap between the Yang–Baxter rule for `(σ₂, σ₃)`,
whose leading monomial is `σ₃σ₂σ₃`, and the far-commutation rule for
`(σ₃, σ₁)`, whose leading monomial is `σ₃σ₁`; they share the letter `σ₃`, over
the ambient word `σ₃σ₂σ₃σ₁`. Its S-polynomial is

  `σ₂σ₃σ₂σ₁ − σ₃σ₂σ₁σ₃`,

and **both** words are irreducible for the system: no `σᵢσᵢ`, no
`σᵢ₊₁σᵢσᵢ₊₁`, and no `σᵢσⱼ` with `i > j+1` occurs as a factor of either. So
the S-polynomial is a non-zero normal form, the system is not confluent, and
it is not a GS basis.

This is not a defect of the Hecke deformation: the same overlap obstructs the
Coxeter presentation of `S₄`. Bokut & Shiao's theorem produces a GS basis by
*completing* the presentation — the missing family is exactly
`σᵢσᵢ₋₁⋯σⱼσᵢ → σᵢ₋₁σᵢσᵢ₋₁⋯σⱼ`, of which `σ₃σ₂σ₁σ₃ → σ₂σ₃σ₂σ₁` is the first
instance. `heckeRewritingSystem` contains only the defining relations, so the
theorem does not apply to it. Completing the system is the work that bean
qou-auq3 actually needs; see the bean for the analysis. -/

namespace NotAGSBasis

/-- `0 < 4`, once, so that every statement below is about the same system. -/
theorem hn4 : 0 < 4 := by norm_num

/-- The Yang–Baxter rule for the adjacent pair `(σ₂, σ₃)`; `lm = σ₃σ₂σ₃`. -/
noncomputable def yb : ReductionRule (HeckeGen 4) ℝ := yangBaxterRelation 2 3

/-- The far-commutation rule for `(σ₃, σ₁)`; `lm = σ₃σ₁`. -/
noncomputable def fc : ReductionRule (HeckeGen 4) ℝ := farCommRelation 3 1

theorem yb_lm : yb.lm (heckeOrder 4) = [⟨3⟩, ⟨2⟩, ⟨3⟩] :=
  yangBaxterRelation_lm 2 3 (by norm_num)

theorem fc_lm : fc.lm (heckeOrder 4) = [⟨3⟩, ⟨1⟩] :=
  farCommRelation_lm 3 1 (by norm_num)

/-- The overlap composition on the ambient word `σ₃σ₂σ₃σ₁`. -/
noncomputable def oc : OverlapComposition (HeckeGen 4) ℝ (heckeOrder 4) where
  rule₁ := yb
  rule₂ := fc
  left := [⟨3⟩, ⟨2⟩]
  overlap := [⟨3⟩]
  right := [⟨1⟩]
  lm₁_decomp := yb_lm
  lm₂_decomp := fc_lm
  overlap_nonempty := by simp

theorem yb_mem (hp : HeckeParams) :
    yb ∈ (heckeRewritingSystem 4 hn4 hp).rules := by
  refine List.mem_append_left _ (List.mem_append_right _ ?_)
  refine List.mem_flatMap.mpr ⟨2, List.mem_finRange 2, ?_⟩
  exact List.mem_filterMap.mpr ⟨3, List.mem_finRange 3, rfl⟩

theorem fc_mem (hp : HeckeParams) :
    fc ∈ (heckeRewritingSystem 4 hn4 hp).rules := by
  refine List.mem_append_right _ ?_
  refine List.mem_flatMap.mpr ⟨3, List.mem_finRange 3, ?_⟩
  exact List.mem_filterMap.mpr ⟨1, List.mem_finRange 1, rfl⟩

/-- The two irreducible words the S-polynomial is supported on. -/
def w₁ : Monomial (HeckeGen 4) := [⟨2⟩, ⟨3⟩, ⟨2⟩, ⟨1⟩]
def w₂ : Monomial (HeckeGen 4) := [⟨3⟩, ⟨2⟩, ⟨1⟩, ⟨3⟩]

theorem yb_lc : yb.lc (heckeOrder 4) = -1 := by
  show yb.relation.coeff (yb.lm (heckeOrder 4)) = -1
  rw [yb_lm]
  simp [yb, yangBaxterRelation, AlgElement.ofTerms_coeff]

theorem fc_lc : fc.lc (heckeOrder 4) = 1 := by
  show fc.relation.coeff (fc.lm (heckeOrder 4)) = 1
  rw [fc_lm]
  simp [fc, farCommRelation, AlgElement.ofTerms_coeff]

/-- The S-polynomial has coefficient `1` at `σ₂σ₃σ₂σ₁`: it is not zero. -/
theorem spoly_coeff_w₁ : oc.spoly.coeff w₁ = 1 := by
  have h1 : w₁ = [] ++ [⟨2⟩, ⟨3⟩, ⟨2⟩] ++ [⟨1⟩] := by simp [w₁]
  have h2 : (AlgElement.contextMul [⟨3⟩, ⟨2⟩] fc.relation []).coeff w₁ = 0 := by
    refine AlgElement.contextMul_coeff_of_not_shape _ (fun w => ?_)
    simp [w₁]
  simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  show fc.lc (heckeOrder 4) * (AlgElement.contextMul [] yb.relation [⟨1⟩]).coeff w₁
      - yb.lc (heckeOrder 4)
        * (AlgElement.contextMul [⟨3⟩, ⟨2⟩] fc.relation []).coeff w₁ = 1
  rw [h2, fc_lc, yb_lc, h1, AlgElement.contextMul_coeff_middle]
  simp [yb, yangBaxterRelation, AlgElement.ofTerms_coeff]

/-- Everything the S-polynomial is supported on is one of three words. -/
theorem spoly_support (m : Monomial (HeckeGen 4)) (h : oc.spoly.coeff m ≠ 0) :
    m = w₁ ∨ m = w₂ ∨ m = oc.word := by
  by_cases h1 : (AlgElement.contextMul [] yb.relation [⟨1⟩]).coeff m ≠ 0
  · obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape h1
    have : w = [⟨2⟩, ⟨3⟩, ⟨2⟩] ∨ w = [⟨3⟩, ⟨2⟩, ⟨3⟩] := by
      have := AlgElement.mem_support_of_coeff_ne_zero hwne
      simpa [yb, yangBaxterRelation, AlgElement.ofTerms] using this
    rcases this with rfl | rfl
    · exact Or.inl (by simpa [w₁] using hw)
    · exact Or.inr (Or.inr (by simpa [OverlapComposition.word, oc] using hw))
  · push_neg at h1
    have h2 : (AlgElement.contextMul [⟨3⟩, ⟨2⟩] fc.relation []).coeff m ≠ 0 := by
      intro h2
      apply h
      simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
      show fc.lc (heckeOrder 4) * (AlgElement.contextMul [] yb.relation [⟨1⟩]).coeff m
          - yb.lc (heckeOrder 4)
            * (AlgElement.contextMul [⟨3⟩, ⟨2⟩] fc.relation []).coeff m = 0
      rw [h1, h2]
      ring
    obtain ⟨w, hw, hwne⟩ := AlgElement.contextMul_shape h2
    have : w = [⟨3⟩, ⟨1⟩] ∨ w = [⟨1⟩, ⟨3⟩] := by
      have := AlgElement.mem_support_of_coeff_ne_zero hwne
      simpa [fc, farCommRelation, AlgElement.ofTerms] using this
    rcases this with rfl | rfl
    · exact Or.inr (Or.inr (by simpa [OverlapComposition.word, oc] using hw))
    · exact Or.inr (Or.inl (by simpa [w₂] using hw))

/-! Both words are irreducible.  The three families of leading monomials are
checked against them by `decide`: `σᵢσᵢ` never occurs (no letter repeats
adjacently), `σᵢ₊₁σᵢσᵢ₊₁` never occurs, and `σᵢσⱼ` with `i > j+1` never occurs
(the only descents are by one, except `σ₁σ₃` and `σ₂σ₃`, which ascend). -/

theorem no_sq_infix_w₁ : ∀ i : Fin 4,
    ¬ (([⟨i⟩, ⟨i⟩] : Monomial (HeckeGen 4)) <:+: w₁) := by decide

theorem no_yb_infix_w₁ : ∀ i j : Fin 4, j.val = i.val + 1 →
    ¬ (([⟨j⟩, ⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 4)) <:+: w₁) := by decide

theorem no_fc_infix_w₁ : ∀ i j : Fin 4, j.val + 1 < i.val →
    ¬ (([⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 4)) <:+: w₁) := by decide

theorem no_sq_infix_w₂ : ∀ i : Fin 4,
    ¬ (([⟨i⟩, ⟨i⟩] : Monomial (HeckeGen 4)) <:+: w₂) := by decide

theorem no_yb_infix_w₂ : ∀ i j : Fin 4, j.val = i.val + 1 →
    ¬ (([⟨j⟩, ⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 4)) <:+: w₂) := by decide

theorem no_fc_infix_w₂ : ∀ i j : Fin 4, j.val + 1 < i.val →
    ¬ (([⟨i⟩, ⟨j⟩] : Monomial (HeckeGen 4)) <:+: w₂) := by decide

/-- No rule of the system applies to `σ₂σ₃σ₂σ₁`. -/
theorem no_rule_infix_w₁ (hp : HeckeParams) (r : ReductionRule (HeckeGen 4) ℝ)
    (hr : r ∈ (heckeRewritingSystem 4 hn4 hp).rules) :
    ¬ (r.lm (heckeOrder 4) <:+: w₁) := by
  rcases heckeRewritingSystem_lm_cases hn4 hp r hr with
    ⟨i, h⟩ | ⟨i, j, hij, h⟩ | ⟨i, j, hij, h⟩ <;> rw [h]
  · exact no_sq_infix_w₁ i
  · exact no_yb_infix_w₁ i j hij
  · exact no_fc_infix_w₁ i j hij

/-- No rule of the system applies to `σ₃σ₂σ₁σ₃`. -/
theorem no_rule_infix_w₂ (hp : HeckeParams) (r : ReductionRule (HeckeGen 4) ℝ)
    (hr : r ∈ (heckeRewritingSystem 4 hn4 hp).rules) :
    ¬ (r.lm (heckeOrder 4) <:+: w₂) := by
  rcases heckeRewritingSystem_lm_cases hn4 hp r hr with
    ⟨i, h⟩ | ⟨i, j, hij, h⟩ | ⟨i, j, hij, h⟩ <;> rw [h]
  · exact no_sq_infix_w₂ i
  · exact no_yb_infix_w₂ i j hij
  · exact no_fc_infix_w₂ i j hij

/-- The S-polynomial is a normal form. -/
theorem spoly_isNormalForm (hp : HeckeParams) :
    isNormalForm (heckeOrder 4) (heckeRewritingSystem 4 hn4 hp) oc.spoly := by
  intro r hr m hm
  rcases spoly_support m hm with rfl | rfl | rfl
  · exact no_rule_infix_w₁ hp r hr
  · exact no_rule_infix_w₂ hp r hr
  · exact absurd (OverlapComposition.spoly_coeff_word_eq_zero oc) hm

/-- **The Hecke relations are not a Gröbner–Shirshov basis at `n = 4`.** -/
theorem hecke_not_gs_basis_four (hp : HeckeParams) :
    ¬ IsGrobnerShirshovBasis (HeckeGen 4) ℝ (heckeOrder 4)
        (heckeRewritingSystem 4 hn4 hp) := by
  intro hgs
  obtain ⟨nf, ⟨hred, -⟩, hzero⟩ := hgs.overlap_resolves oc (yb_mem hp) (fc_mem hp)
  have hnfeq : nf = oc.spoly :=
    MultiStepReduction.eq_of_isNormalForm (spoly_isNormalForm hp) hred
  subst hnfeq
  have h0 := hzero w₁
  rw [spoly_coeff_w₁] at h0
  exact one_ne_zero h0

end NotAGSBasis

/-- **The former axiom `hecke_is_gs_basis` is false.**

It asserted `∀ n (hn : 0 < n) (hp : HeckeParams), IsGrobnerShirshovBasis …` for
`heckeRewritingSystem`; `n = 4` refutes it. The axiom has been deleted from
this file: with the repaired definitions it would have made the library
inconsistent, not merely optimistic. -/
theorem hecke_is_gs_basis_false :
    ¬ (∀ (n : ℕ) (hn : 0 < n) (hp : HeckeParams),
        IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n)
          (heckeRewritingSystem n hn hp)) := by
  intro h
  exact NotAGSBasis.hecke_not_gs_basis_four
    ⟨2, by norm_num, by norm_num⟩ (h 4 NotAGSBasis.hn4 ⟨2, by norm_num, by norm_num⟩)

/-- **The former axiom `dist_algebra_gs_basis` is false.**

It asserted that every rewriting system over every field is a
Gröbner–Shirshov basis (its `DistAlgGenerators` argument was unused).
The Hecke system at `n = 4` refutes it. The axiom was deleted from
`UGB.GrobnerShirshov.NormalForms`. -/
theorem dist_algebra_gs_basis_false :
    ¬ (∀ (_dg : DistAlgGenerators) (G : Type) (k : Type) [Field k]
        (ord : AdmissibleOrder G) [DecidableEq G] (sys : RewritingSystem G k),
        IsGrobnerShirshovBasis G k ord sys) := by
  intro h
  exact NotAGSBasis.hecke_not_gs_basis_four ⟨2, by norm_num, by norm_num⟩
    (h ⟨2, Nat.prime_two, 1⟩ _ ℝ _ _)

/-! ## §5  Braid Word Embedding (Constructive) -/

/-- Embed a positive generator `σᵢ` as the singleton monomial `[σᵢ]`. -/
noncomputable def embedPositiveGen {n : ℕ} (i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.singleton [⟨i⟩]

/-- Embed a negative generator `σᵢ⁻¹` via the Hecke relation inverse:
    `σᵢ⁻¹ = σᵢ - (q - q⁻¹)`.

    Derived from `σᵢ² = (q-q⁻¹)σᵢ + 1`: multiplying by `σᵢ⁻¹` gives
    `σᵢ = (q-q⁻¹) + σᵢ⁻¹`, i.e. the skein relation `σᵢ - σᵢ⁻¹ = q - q⁻¹`.
    Check: `σᵢ(σᵢ - (q-q⁻¹)) = σᵢ² - (q-q⁻¹)σᵢ = 1`.

    **Corrected 2026-11-15 (bean `qou-078y`).** This read
    `σᵢ⁻¹ = (q⁻¹ - q)σᵢ + q⁻¹`, whose product with `σᵢ` is
    `(q⁻¹-q)(q-q⁻¹)σᵢ + (q⁻¹-q) + q⁻¹σᵢ`, which is not `1` for any `q ≠ ±1`
    (at `q = 2` it is `-(5/4)σᵢ - 3/2`). -/
noncomputable def embedNegativeGen {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [
    ([⟨i⟩], 1),
    ([], -(hp.q - hp.q⁻¹))
  ]

/-- **The corrected inverse is an inverse.** In any ring, an element `x`
    satisfying the Hecke quadratic `x² = h·x + 1` with `h` commuting with `x`
    is invertible with inverse `x - h`. With `h = q - q⁻¹` this is the formula
    `embedNegativeGen` encodes. -/
theorem hecke_inverse_eq_sub {R : Type*} [Ring R] (x h : R) (hc : Commute x h)
    (hx : x * x = h * x + 1) : x * (x - h) = 1 ∧ (x - h) * x = 1 := by
  constructor
  · rw [mul_sub, hx, hc.eq]; abel
  · rw [sub_mul, hx]; abel

/-- Embed a signed braid generator into `AlgElement`.
    Positive index → singleton monomial.
    Negative index → Hecke inverse.

    Requires `[NeZero n]` so that `_ % n < n` is well-defined. -/
noncomputable def embedGenerator {n : ℕ} [NeZero n]
    (hp : HeckeParams) (g : ℤ) :
    AlgElement (HeckeGen n) ℝ :=
  have hn : 0 < n := Nat.pos_of_ne_zero (NeZero.ne n)
  if g ≥ 0
  then embedPositiveGen ⟨g.toNat % n, Nat.mod_lt _ hn⟩
  else embedNegativeGen ⟨g.natAbs % n, Nat.mod_lt _ hn⟩ hp

/-- Embed a braid word given as explicit letters `(i, sign)` into
    `AlgElement`, `true` = `σᵢ`, `false` = `σᵢ⁻¹`, by left-multiplying each
    generator's embedding successively: for `[l₁, l₂, l₃]` the value is
    `embed(l₁) · embed(l₂) · embed(l₃)`.

    Positive letters are singletons, so the product is `leftMulGen σᵢ`.
    Negative letters are `σᵢ - (q - q⁻¹)`, so the product distributes as
    `σᵢ · acc - (q - q⁻¹) · acc`.

    **This is a product in the FREE algebra.** No Hecke relation is applied, so
    the result is in general not a normal form, and `heckeCost` of it is the
    cost of an unreduced word expansion, not of the Hecke-algebra element. The
    reduced cost is `HeckeReducedCost.IsReducedCost`, which takes the normal
    form in the completed system first. -/
noncomputable def braidLettersToAlg {n : ℕ} (hp : HeckeParams)
    (letters : List (Fin n × Bool)) : AlgElement (HeckeGen n) ℝ :=
  letters.foldr
    (fun l acc =>
      if l.2
      then AlgElement.leftMulGen ⟨l.1⟩ acc
      else
        -- σᵢ⁻¹ · acc = σᵢ · acc - (q - q⁻¹) · acc
        AlgElement.add
          (AlgElement.leftMulGen ⟨l.1⟩ acc)
          (AlgElement.smul (-(hp.q - hp.q⁻¹)) acc))
    (AlgElement.singleton [])

/-- Decode the signed-integer braid encoding: `g ≥ 0` is `σ_{g mod n}`, and
    `g < 0` is `σ_{|g| mod n}⁻¹`.

    **Limitation of this encoding.** `-0 = 0`, so `σ₀⁻¹` has no code: the
    integer `-(0 : ℤ)` decodes to the positive letter `σ₀`. Callers that need
    `σ₀⁻¹` must build letters directly and use `braidLettersToAlg`. -/
def decodeSigned {n : ℕ} [NeZero n] (g : ℤ) : Fin n × Bool :=
  have hn : 0 < n := Nat.pos_of_ne_zero (NeZero.ne n)
  if g ≥ 0
  then (⟨g.toNat % n, Nat.mod_lt _ hn⟩, true)
  else (⟨g.natAbs % n, Nat.mod_lt _ hn⟩, false)

/-- Embed a braid word in the signed-integer encoding (see `decodeSigned`
    for its `σ₀⁻¹` limitation). -/
noncomputable def braidToAlg {n : ℕ} [NeZero n] (hp : HeckeParams)
    (generators : List ℤ) : AlgElement (HeckeGen n) ℝ :=
  braidLettersToAlg hp (generators.map decodeSigned)

/-- The augmented braid element for threading: prepend the photon
    strand above the hadron, then un-braid below.

    `augmentedBraid β_H = σ_n · σ_{n-1} · … · σ₁ · β_H · σ₁⁻¹ · … · σ_n⁻¹`

    In the `B_{n+1}` embedding (generators `σ₀, …, σ_n` indexed by `Fin (n+1)`).

    **Corrected 2026-11-15 (bean `qou-078y`).** The photon letters are now
    built as explicit `(i, sign)` pairs. They were written as signed integers
    `-(i : ℤ)`, and for `i = 0` that is `+0`, so the first un-braiding letter
    came out as the positive `σ₀` instead of `σ₀⁻¹`. The hadron word keeps the
    signed-integer encoding for its callers; see `decodeSigned`. -/
noncomputable def augmentedBraidElement {n : ℕ} (hp : HeckeParams)
    (hadron_generators : List ℤ) : AlgElement (HeckeGen (n + 1)) ℝ :=
  let photon_above : List (Fin (n + 1) × Bool) :=
    (List.finRange (n + 1)).reverse.map (fun i => (i, true))
  let photon_below : List (Fin (n + 1) × Bool) :=
    (List.finRange (n + 1)).map (fun i => (i, false))
  braidLettersToAlg hp
    (photon_above ++ hadron_generators.map decodeSigned ++ photon_below)

/-! ## §6  Hecke Cost (Constructive) -/

/-- The Hecke cost of an element: the sum of absolute values of
    coefficients across the entire support.

    `heckeCost(f) = Σ_{m ∈ supp(f)} |f.coeff(m)|`

    This is well-defined because `support` is a `Finset`. -/
noncomputable def heckeCost {n : ℕ} (f : AlgElement (HeckeGen n) ℝ) : ℝ :=
  f.support.sum (fun m => |f.coeff m|)

/-- The Hecke cost is non-negative. -/
theorem heckeCost_nonneg {n : ℕ} (f : AlgElement (HeckeGen n) ℝ) :
    0 ≤ heckeCost f := by
  unfold heckeCost
  exact Finset.sum_nonneg (fun m _ => abs_nonneg _)

/-- The Hecke cost depends only on the coefficients, not on the (superset)
    `support` field. -/
theorem heckeCost_congr {n : ℕ} {f g : AlgElement (HeckeGen n) ℝ}
    (h : AlgElement.CoeffEq f g) : heckeCost f = heckeCost g := by
  classical
  unfold heckeCost
  have hf : f.support.sum (fun m => |f.coeff m|) =
      (f.support ∪ g.support).sum (fun m => |f.coeff m|) :=
    Finset.sum_subset Finset.subset_union_left
      (fun m _ hm => by rw [f.support_spec m hm, abs_zero])
  have hg : g.support.sum (fun m => |g.coeff m|) =
      (f.support ∪ g.support).sum (fun m => |g.coeff m|) :=
    Finset.sum_subset Finset.subset_union_right
      (fun m _ hm => by rw [g.support_spec m hm, abs_zero])
  rw [hf, hg]
  exact Finset.sum_congr rfl (fun m _ => by rw [h m])

/-! ## §7  Normal Form Uniqueness -/

/-- Normal forms of a Hecke algebra element are unique — **conditionally on
    the system being a GS basis**, which is now an explicit hypothesis rather
    than the deleted axiom. `NotAGSBasis.hecke_not_gs_basis_four` shows the
    hypothesis is unsatisfiable at `n = 4` for `heckeRewritingSystem` as it
    stands, so this statement is vacuous as it applies to *this* system.

    The Bokut–Shiao completion has since been added and proved:
    `HeckeCompletion.heckeCompleted_normalForm_unique` is this statement against
    `heckeCompletedRewritingSystem`, with the hypothesis discharged. Use that
    one; this stays because it is stated at the level the abstract framework
    works at, and because deleting it would erase the record of why the
    uncompleted system cannot support it. -/
theorem heckeCost_well_defined (n : ℕ) (hn : 0 < n) (hp : HeckeParams)
    (hgs : IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n)
      (heckeRewritingSystem n hn hp))
    (hnqz : NoQuasiZerosFree (HeckeGen n) ℝ)
    (hlc : ∀ r ∈ (heckeRewritingSystem n hn hp).rules, IsUnit (r.lc (heckeOrder n)))
    (f : AlgElement (HeckeGen n) ℝ)
    (nf₁ nf₂ : AlgElement (HeckeGen n) ℝ)
    (hred₁ : ReducesToNF (heckeOrder n) (heckeRewritingSystem n hn hp) f nf₁)
    (hred₂ : ReducesToNF (heckeOrder n) (heckeRewritingSystem n hn hp) f nf₂) :
    AlgElement.CoeffEq nf₁ nf₂ :=
  normal_form_unique (heckeOrder n) (heckeRewritingSystem n hn hp) hgs hnqz hlc
    f nf₁ nf₂ hred₁ hred₂

/-- Threading cost uniqueness: two reductions of the same augmented braid
    yield identical normal forms — again **conditionally** on `hgs`, for the
    same reason as `heckeCost_well_defined`, and again vacuous for this system.
    The unconditional form is
    `HeckeCompletion.heckeCompleted_threading_cost_unique`. The "no quasi-zeros"
    hypothesis is discharged here: `HeckeGen (n+1)` has a generator, so the free
    algebra on it has none. -/
theorem threading_cost_unique (n : ℕ) (hp : HeckeParams)
    (hgs : IsGrobnerShirshovBasis (HeckeGen (n + 1)) ℝ (heckeOrder (n + 1))
      (heckeRewritingSystem (n + 1) (Nat.succ_pos n) hp))
    (hlc : ∀ r ∈ (heckeRewritingSystem (n + 1) (Nat.succ_pos n) hp).rules,
      IsUnit (r.lc (heckeOrder (n + 1))))
    (hadron : List ℤ) :
    ∀ (nf₁ nf₂ : AlgElement (HeckeGen (n + 1)) ℝ),
      ReducesToNF (heckeOrder (n + 1)) (heckeRewritingSystem (n + 1) (Nat.succ_pos n) hp)
        (augmentedBraidElement hp hadron) nf₁ →
      ReducesToNF (heckeOrder (n + 1)) (heckeRewritingSystem (n + 1) (Nat.succ_pos n) hp)
        (augmentedBraidElement hp hadron) nf₂ →
      AlgElement.CoeffEq nf₁ nf₂ := by
  intro nf₁ nf₂ h₁ h₂
  exact heckeCost_well_defined (n + 1) (Nat.succ_pos n) hp hgs
    (noQuasiZerosFree_of_generator ⟨0, Nat.succ_pos n⟩) hlc
    (augmentedBraidElement hp hadron) nf₁ nf₂ h₁ h₂

end UGB.GrobnerShirshov.Hecke
