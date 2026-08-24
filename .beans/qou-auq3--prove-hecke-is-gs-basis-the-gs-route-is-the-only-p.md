---
# qou-auq3
title: Prove hecke_is_gs_basis — the GS route is the only path from n<=4 to general n
status: in-progress
type: task
created_at: 2026-08-09T16:10:13Z
updated_at: 2026-08-21T20:56:34Z
---


`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean:156`:

```lean
/-- **Theorem** (Bokut & Shiao 2001, Theorem 3.5):
    The Hecke relations form a GS basis for `H_n(q)`. -/
-- Ref: [bokutchen2014] https://doi.org/10.1007/s13373-014-0054-6
axiom hecke_is_gs_basis (n : ℕ) (hp : HeckeParams) :
    IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n) (heckeRewritingSystem n hp)
```

Everything constructive around it is already there — `heckeOrder` is a `def`
(deg-lex from `AlgOps`), so are `heckeRewritingSystem`, `embedGenerator`,
`braidToAlg`, `heckeCost`. The file's own axiom-budget table lists exactly one
axiom, and this is it. Downstream, `heckeCost_well_defined` and
`threading_cost_unique` inherit it.

## Why this is the highest-value item on the Hecke roadmap

Every concrete rung — `H2`, `H3A`, `H4A` — is a hand-built or generated table at
one `n`. The scoping answer in
`docs/audits/2026-08-09-hecke-infrastructure-what-is-needed.md` is that `n = 4`
is the last level worth building that way: `H₅` is 120 basis elements, `H₁₂` is
479 001 600, and the manuscript's physics lives at `H₆`, `H₉`, `H₁₂`, `H₁₈` and
up to `H₁₂₀`.

A **proved** GS basis is the one route to general `n`. It gives normal forms and
the `n!` count for all `n` at once, and it is the constructive substitute for
Matsumoto / Coxeter word reduction, which Mathlib does not have (rev
`f897ebcf`: `GroupTheory/Coxeter/{Basic,Inversion,Length,Matrix}` exist, Hecke
algebras do not — `find Mathlib -iname "*Hecke*"` returns nothing).

With it, `QOU.Hecke.finrank_of_rank_recursion` and `isHeckeOfFullRank_succ`
(`QOU/Hecke/FullRank.lean`) close the induction: the GS normal forms give the
rung, the tower law gives `n!`.

## Why it cannot simply be imported as-is

The H₃/H₄ work is axiom-clean (`propext, Classical.choice, Quot.sound`), and
`HeckeH4AlgebraLaws` commits to that explicitly — "no axiom, no `sorry`, no
conditional class, no `native_decide`". Importing `hecke_is_gs_basis` would put
an unproved axiom underneath results that currently have none. `qou` does
`require` the UGB package (`lakefile.toml:45`), and exactly one QOU module
imports it (`QOU/PhotonThreading.lean`) — which reads as deliberate quarantine
rather than oversight.

## The work

Discharge the axiom via `UGB.GrobnerShirshov.CompositionLemma`: verify that every
composition (overlap and inclusion) of the Hecke relations is trivial modulo the
system. For type A that is the standard Bokut–Shiao argument — finitely many
overlap types coming from the braid and quadratic relations. `CompositionLemma`
is in the tree for exactly this purpose.

Cross-check available for free: the GS normal forms at `n = 3, 4` must reproduce
the 6- and 24-word bases already committed
(`QOU.Machinery.MarkovTraceOnHecke`, `HeckeH4AlgebraLaws.wordAction`), which were
computed as GB normal forms by `computations/markov/hecke_regular_nf_table.py`.
Two independent derivations of the same word list is a real check on both.

---

## 2026-08-09 — the framework is repaired, and the target turns out to be **false**

`hecke_is_gs_basis` cannot be proved: with `leadingMonomial`,
`SingleStepReduction` and `spoly` repaired, the statement is refutable, and the
refutation is now in the tree. The axiom has been **deleted** rather than left
standing — keeping a provably false axiom would have made every downstream
result meaningless, not merely unproved.

### The counterexample (machine-checked, `n = 4`)

`UGB/GrobnerShirshov/HeckeGS.lean` §4e, namespace `NotAGSBasis`:

```
NotAGSBasis.hecke_not_gs_basis_four (hp : HeckeParams) :
  ¬ IsGrobnerShirshovBasis (HeckeGen 4) ℝ (heckeOrder 4)
      (heckeRewritingSystem 4 hn4 hp)

hecke_is_gs_basis_false :
  ¬ (∀ n (hn : 0 < n) (hp : HeckeParams), IsGrobnerShirshovBasis …)
```

`#print axioms` on both: `[propext, Classical.choice, Quot.sound]`. Neither
depends on `normal_form_exists`, `local_confluence`, `confluence` or
`normal_form_unique` — the refutation is independent of the framework's
remaining axioms.

The obstruction is the overlap of two rules of the system on the word
`σ₃σ₂σ₃σ₁`:

* Yang–Baxter for the adjacent pair `(σ₂,σ₃)`, leading monomial `σ₃σ₂σ₃`;
* far commutation for `(σ₃,σ₁)`, leading monomial `σ₃σ₁`.

Its S-polynomial is `σ₂σ₃σ₂σ₁ − σ₃σ₂σ₁σ₃` (`spoly_coeff_w₁` proves the
coefficient at `σ₂σ₃σ₂σ₁` is `1`; the ambient word cancels by the general
lemma `OverlapComposition.spoly_coeff_word_eq_zero`). Both words are
irreducible: `no_rule_infix_w₁` / `no_rule_infix_w₂` check the three families
of leading monomials — `σᵢσᵢ`, `σᵢ₊₁σᵢσᵢ₊₁`, `σᵢσⱼ` with `i > j+1` — against
each word by `decide`, via the classification lemma
`heckeRewritingSystem_lm_cases`. So the S-polynomial is a non-zero normal
form and the system is not confluent.

Nothing about the `q`-deformation is involved: the same overlap obstructs the
Coxeter presentation of `S₄`. (Checked by hand at `n = 3` and it *is*
confluent there, which is why `H₂`/`H₃` never surfaced this.)

### Why Bokut & Shiao 2001 was cited for something it does not say

Their Theorem 3.5 gives a GS basis for Coxeter groups by **completing** the
presentation. The completion adds the family

    σᵢ σᵢ₋₁ ⋯ σⱼ σᵢ  →  σᵢ₋₁ σᵢ σᵢ₋₁ ⋯ σⱼ        (j < i)

of which `σ₃σ₂σ₁σ₃ → σ₂σ₃σ₂σ₁` is exactly the first instance — the very
S-polynomial above. `heckeRewritingSystem` contains only the defining
relations (quadratic, braid, far commutation), so the cited theorem never
applied to it. **This is the work the bean actually needs**: extend
`heckeRewritingSystem` with that family (indexed by pairs `j < i` in `Fin n`,
so still finite for each `n`), then verify the compositions. The `n!` count
and the normal forms for general `n` follow from the *completed* system, not
from the defining relations.

### One further correction the repair exposed

With `leadingMonomial` actually respecting its order, `yangBaxterRelation i j`
(`i < j`) has leading monomial `[σⱼ, σᵢ, σⱼ]`, **not** `[σᵢ, σⱼ, σᵢ]` as its
docstring claimed: deg-lex ranks `σⱼ` above `σᵢ`. The rule therefore rewrites
`σᵢ₊₁σᵢσᵢ₊₁ → σᵢσᵢ₊₁σᵢ`. The orientation is admissible (the leading monomial
does dominate the tail); only the prose was wrong. Proved as
`yangBaxterRelation_lm`; the companions are `heckeRelation_lm`
(`[σᵢ,σᵢ]`) and `farCommRelation_lm` (`[σᵢ,σⱼ]`, `j < i`).

### The three repairs (`UGB/GrobnerShirshov/`)

1. **`leadingMonomial`** (`Basic.lean` §2) is now the `ord`-greatest support
   element. Getting there needed order theory the structure did not carry:
   `AdmissibleOrder.asymm`, `.irrefl`, `.lt_trans` (trichotomy alone does not
   give transitivity — well-foundedness rules out the 3-cycle), `.exists_max`,
   and `.not_lt_nil` (**the empty word is the minimum of every admissible
   order** — otherwise `x ↦ m ++ x` descends forever). Exports:
   `leadingMonomial_mem_support`, `le_leadingMonomial`,
   `lt_leadingMonomial_of_coeff_ne_zero`, `leadingMonomial_eq_of_max`,
   `leadingCoeff`, and the abbreviations `ReductionRule.lm/.lc`.

2. **`SingleStepReduction`** (`Basic.lean` §3) now carries the algebra:

   ```
   ∃ r ∈ sys.rules, ∃ a b c,
       f.coeff (a ++ r.lm ord ++ b) ≠ 0 ∧
       c * r.lc ord = f.coeff (a ++ r.lm ord ++ b) ∧
       CoeffEq g (f - c • (a · r.relation · b))
   ```

   The two side conditions are not decoration. Without them `c = 0, g = f` is
   a legal step, `→` is reflexive, and `CompositionLemma.reduction_well_founded`
   becomes a **false** axiom. With them every step eliminates the monomial it
   targets — `SingleStepReduction.exists_eliminated` — so the multiset of
   monomials strictly decreases and that axiom is at least true-shaped.

3. **`spoly`** is a definition, not a field (`Basic.lean` §4), and both
   composition structures now take the order as a parameter. They used to
   quantify the decomposition over *every* admissible order (`lm₁_decomp :
   ∀ ord, …`), which after repair 1 would have left them almost uninhabited
   and made the GS predicate vacuous in the *other* direction. New general
   lemmas: `OverlapComposition.spoly_coeff_word` /
   `InclusionComposition.spoly_coeff_lm` (the ambient word contributes
   `lc₂·lc₁ − lc₁·lc₂`) and their `_eq_zero` corollaries over a `CommRing`.

Supporting move: the `AlgElement` arithmetic left `AlgOps.lean` for a new
`Elem.lean`, which `Basic.lean` imports — stating a reduction step needs
subtraction and two-sided multiplication by a monomial, and `AlgOps` imports
`Basic`. Nothing was renamed; `AlgOps` keeps `shortLex_wellFounded` and
`mkDegLexOrder`. New there: `contextMul a f b` (`= a · f · b`, exact because
the contexts are monomials) with `contextMul_coeff_middle` / `_shape`, and
`eraseCoeff`.

### Two definitions changed meaning, deliberately

`AlgElement.isZero` was `support = ∅` and is now `∀ m, coeff m = 0`;
`isNormalForm` quantified over the `support` field and now quantifies over
monomials with non-zero coefficient. The `support` field is only a *superset*
of the true support, so both old forms were statements about a representation
rather than about an element — and with a correct `SingleStepReduction` they
are not merely wrong but fatal: `f - f` carries the support
`f.support ∪ f.support`, so under the old `isZero` **no** S-polynomial could
ever "reduce to zero" and `IsGrobnerShirshovBasis` would have been vacuously
*false*. The predicate is now bracketed on both sides, both machine-checked:

* not vacuously true — `one_not_reduces_to_zero` (`Basic.lean`) and its Hecke
  instance `one_does_not_reduce_to_zero`: as soon as no rule has an empty
  leading monomial, `1` is a normal form and is not `0`;
* not vacuously false — `isGrobnerShirshovBasis_of_single_letter_rule`: a
  one-rule system whose leading monomial is a single letter *is* a GS basis
  (the length forces every composition to have empty contexts).

`gs_basis_of_empty_lm` survives with one added hypothesis, `lc ≠ 0`, and a
real proof (induction on the number of non-zero coefficients, each step
killing one). The hypothesis is needed now that a step must subtract an actual
multiple of the relation, and the deleted sentinel `⟨ofTerms [([], q)], _⟩`
satisfied it (`q > 0`). Its second hypothesis — that the relation is supported
on `[]` alone — is *not* needed: `AdmissibleOrder.not_lt_nil` supplies it.

### State of the build

`lake build` (971 jobs) and `lake build UGB.GrobnerShirshov.HeckeGS` both
green; `QOU.PhotonThreading` still builds against the repaired UGB. No
`sorry`, no `native_decide`, no new axiom anywhere. Every new declaration
`#print axioms`-checks as `[propext, Classical.choice, Quot.sound]`.

### Not done

* The Bokut–Shiao completion itself (the actual path to general `n`).
* The overlap analysis for the *completed* system — the four families listed
  in this bean's original plan are the right enumeration, but they have to be
  checked against the completed rule set, and the far-commutation × braid
  overlap above is precisely the one that fails without it.
* `n ≥ 5`: only `n = 4` is refuted, which is enough to refute the `∀ n`
  statement. The same overlap exists for every `n ≥ 4`; that generalisation is
  not formalised.
* The framework's own axioms (`normal_form_exists`, `reduction_well_founded`,
  `local_confluence`, `confluence`, `normal_form_unique`) are untouched. They
  are now *stated about repaired definitions*, which is a real change in what
  they assert, but they remain assumptions.

---

## 2026-08-09 (later) — the completion family, and one checkable claim about it

New: `UGB/GrobnerShirshov/HeckeCompletion.lean`. Everything below is sorry-free
and `#print axioms`-clean.

### The counterexample *is* the missing rule

This is the fact worth having. §4e refutes the GS property with the
S-polynomial `σ₂σ₃σ₂σ₁ − σ₃σ₂σ₁σ₃`, both words irreducible. The Bokut–Shiao
completion family is `σᵢσᵢ₋₁⋯σⱼσᵢ → σᵢ₋₁σᵢσᵢ₋₁⋯σⱼ`. At `(i, j) = (3, 1)` its two
words are

    bsWord₁ 3 1   = σ₃σ₂σ₁σ₃ = NotAGSBasis.w₂
    bsWord₂ 2 3 1 = σ₂σ₃σ₂σ₁ = NotAGSBasis.w₁

— machine-checked by `decide`, not asserted. So the refuting S-polynomial is,
up to sign, the missing rule itself. `spoly_not_isNormalForm_completed` then
follows: `w₂` carries coefficient `−1` in the S-polynomial (`spoly_coeff_w₂`,
the mirror of §4e's `spoly_coeff_w₁ = 1`) and is `lm(bs31)`, so the
S-polynomial is not a normal form for the completed system. Directly comparable
to `NotAGSBasis.spoly_isNormalForm`, which is the same S-polynomial against the
uncompleted system.

### The family carries no `q`

Worth recording because it is not obvious from the deformed presentation: the
Bokut–Shiao words need **no** deformation term. The identity is a braid-group
identity — `σᵢ` commutes past `σᵢ₋₂ ⋯ σⱼ`, then one braid move — and the
quadratic relation is never used. So `bokutShiaoRelation` is the same two-term
shape as `yangBaxterRelation`, which it subsumes at `j = i − 1`.

### Indices without `Fin` arithmetic

`bokutShiaoRelation i' i j` takes `i'` standing for `i − 1`, with the relation
`i'.val + 1 = i.val` carried on the enumeration in
`heckeCompletedRewritingSystem` rather than by subtracting inside `Fin n`.
`descWord i j` is built by filtering `List.finRange n` on `j ≤ k ≤ i` and
reversing. Both choices keep every word free of subtraction and every
membership proof in the same `flatMap`/`filterMap` shape §4 already uses —
`bs31_mem` is three `refine`s.

### NOT done, and neither is small

* **The general leading monomial — DONE (2026-08-09, §4h).**
  `bokutShiaoRelation_lm : lm (bokutShiaoRelation i' i j) = bsWord₁ i j`, from
  `descWord_cons : descWord i j = ⟨i⟩ :: descWord i' j`, both axiom-clean. The
  prediction held exactly: with the cons lemma **no length computation was
  needed**. Both words acquire a visible common tail — `σᵢ :: (w ++ [σᵢ])` versus
  `σᵢ₋₁ :: σᵢ :: w` with the same `w` — so lengths agree by `simp` and the
  comparison is one `List.Lex.rel` on the first letter.

  `descWord_cons` is a statement about `List.finRange n` being
  `Pairwise (· < ·)`: once the head is `i` every later index exceeds it and both
  filters annihilate the tail; before the head is reached the two predicates
  agree, because `a < i = i' + 1` forces `a ≤ i'`. Two traps worth recording —
  `subst` on `i = a` eliminates `a`, so the head branch is stated in `i`; and
  `List.filter_cons_of_pos` will not fire against a lambda predicate, so the
  proof goes through `List.filter_cons` + `decide_eq_true_eq` + `if_pos/if_neg`.

  This is step 1 of the path to `H_k` for `k > 4`; next is
  `heckeCompletedRewritingSystem_lm_cases`, the completed-system analogue of
  `heckeRewritingSystem_lm_cases`.
* **That the completed system is a GS basis.** This is the whole of Bokut &
  Shiao's theorem. The new family overlaps *itself*, so the composition
  analysis is over a strictly larger set than the four families listed in this
  bean's original plan. Resolving the one overlap that refutes the uncompleted
  system is necessary, not sufficient, and nothing here claims otherwise.

### Build-config hazard found on the way

`ugb`'s `lean_lib` has **no `globs`**, so `lake build` in that project builds
only `UGB.lean` and what it transitively imports. `UGB.GrobnerShirshov.HeckeGS`
is imported by nothing in UGB — it is reached only because
`QOU/PhotonThreading.lean` imports it and `qou` requires `ugb` by path. So the
Hecke GS work has never been covered by UGB's own `lake build`, and
`HeckeCompletion` would not be either. Measured: 26 modules, 24 reachable from
the root, the 2 unreachable ones being exactly `HeckeGS` and `HeckeCompletion`.
Same class of problem as qou-rc7b, and the same fix — `globs = ["UGB", "UGB.+"]`.


## 2026-08-09 (later still) — step 2: the completed system's rules are classified

`heckeCompletedRewritingSystem_lm_cases` — the analogue of
`heckeRewritingSystem_lm_cases` for the completed system. Every rule is one of
**four** families and its leading monomial is explicit:

| family | leading monomial |
|---|---|
| quadratic | `[σᵢ, σᵢ]` |
| Yang–Baxter (`j = i+1`) | `[σⱼ, σᵢ, σⱼ]` |
| far-commutation (`j+1 < i`) | `[σᵢ, σⱼ]` |
| **Bokut–Shiao** (`i'+1 = i`, `j ≤ i'`) | **`bsWord₁ i j`** |

The first three are the original classification verbatim — the completed system
keeps every original rule, so `List.mem_append` hands them straight over. The
fourth needed `bokutShiaoRelation_lm` from step 1, which is why the general
leading monomial had to come first.

Also `heckeCompletedRewritingSystem_lm_ne_nil`: no rule has an empty leading
monomial. That is not decoration — `gs_basis_of_empty_lm` proves an empty leading
monomial collapses the whole GS property, and it was the defect behind the
removed sentinel. Re-established for the larger rule set. `bsWord₁ i j` ends in
`σᵢ`, so it is never empty.

Both axiom-clean, file warning-free.

### Why this is the gate for everything downstream

§4e's irreducibility machinery — `no_rule_infix_w₁`, `no_sq_infix_w₁`,
`no_rule_infix_w₂` and the rest — all dispatch on the *classification*. None of
that can be redone against the completed system without this. So the next step,
the overlap analysis for the completed rule set, now has its foundation.

### Ordering trap

`bokutShiaoRelation_lm` lives in §4h, so a §4i that uses it must come after §4h,
not before §4g. Lean reports it as `Unknown identifier`, which reads like a typo
rather than a section-ordering mistake.


## …and the refuting overlap now **resolves**, not merely reduces

`spoly_not_isNormalForm_completed` said only that the S-polynomial is no longer
irreducible. The Gröbner–Shirshov condition asks for more — that it reduces to
**zero** — and `refuting_overlap_resolves` proves it does, in a **single step**.

The reason is worth seeing, because it is the sharpest form of "the counterexample
is the missing rule":

    oc.spoly       =  w₁ − w₂        (§4e: coeff w₁ = 1, coeff w₂ = −1)
    bs31.relation  =  w₂ − w₁        (bsWord₁ 3 1 = w₂, bsWord₂ 2 3 1 = w₁)

They are exact negatives. One application of `bs31` in **empty context** with
coefficient `−1` annihilates the S-polynomial outright. The obstruction and its
repair are the same two words with opposite signs.

Supporting: `bs31_lc = 1`; `three_words_distinct` (`w₁`, `w₂` and the ambient
`σ₃σ₂σ₃σ₁` are pairwise distinct — needed so the coefficient bookkeeping does not
collide); `spoly_add_relation_eq_zero`, coefficient-by-coefficient cancellation
over the three-word support that §4e's `spoly_support` pins down.

Contrast `NotAGSBasis.spoly_isNormalForm`: the *same* S-polynomial against the
uncompleted system, where no rule applies at all. The pair of theorems is the
before/after of the completion at the one place the refutation lives.

All axiom-clean, file warning-free.

### Placement traps (two now, same family)

Lean reports both as `Unknown identifier`, which reads like a typo:

* a section using `bokutShiaoRelation_lm` (§4h) must come **after** §4h;
* a section using `bs31` / `w₁` / `w₂` / `oc` must be **inside** `namespace
  Completion`, not after `end Completion`.


## §4j — the family subsumes Yang–Baxter

At `j = i − 1` the Bokut–Shiao words *are* the braid words:

    bsWord₁ i i'   = σᵢ σᵢ₋₁ σᵢ        (`bsWord₁_at_pred`)
    bsWord₂ i' i i' = σᵢ₋₁ σᵢ σᵢ₋₁      (`bsWord₂_at_pred`)

so `bokutShiaoRelation i' i i'` is `yangBaxterRelation i' i` up to the sign
convention (`bokutShiaoRelation_at_pred`), and the two share a leading monomial
(`bokutShiao_lm_eq_yangBaxter_lm`).

**Why this matters for the overlap analysis ahead.** It means YB × BS overlaps
are a *special case* of BS × BS, not a separate family to enumerate. The
composition set for the completed system is smaller than a naive four-families
count suggests.

Needed `descWord_self : descWord i i = [σᵢ]`, proved via `filter_desc_self` —
the same `Pairwise (· < ·)` induction as `filter_desc_cons`, and worth having
separately since it is the base case of the descending words.

### An asymmetry worth keeping

`bsWord₂_at_pred` needs **no** relation between `i'` and `i`. `bsWord₂ i' i j`
is `σᵢ₋₁ σᵢ` followed by `descWord i' j`, so at `j = i'` the tail collapses by
`descWord_self` whatever `i` is. Only the *left* word needs `i' + 1 = i`, since
that is where `descWord_cons` is used. The linter caught the unused hypothesis;
it was carrying a false suggestion that both sides need the relation.

### The recorded trap caught me anyway

`filter_desc_self`'s head branch was written with `a.val` after `subst`, exactly
the mistake this bean already records for `filter_desc_cons`. Writing the trap
down did not stop me repeating it — the fix is that the head branch of any such
induction must be stated in `i`, because `subst` on `i = a` eliminates `a`.

## §4k — the overlap set, counted

The estimate ("four families, and the new family overlaps itself") was a shape.
It is now a number, kernel-checked with no `native_decide`:

    16 rules
    13 distinct leading monomials     (the three lost are the Yang–Baxter words)
    58 overlap shapes                 at n = 4
       13 degenerate (left = right = [], lm₁ = lm₂)
       45 with both contexts non-empty — `NotAGSBasis.oc` is one of these

The move that makes it computable: an `OverlapComposition` is pinned by
`(left, overlap, right)` alone — the *rules* never enter, only their leading
monomials, and `Monomial (HeckeGen n)` is `List` of a `DecidableEq` type. So

* `quadLMs / yangBaxterLMs / farCommLMs / bokutShiaoLMs` — the four families as
  explicit word lists. The Bokut–Shiao rule is indexed by `(i', i, j)` but its
  leading monomial depends only on `(i, j)`, and `i' + 1 = i ∧ j ≤ i'` collapses
  to `j < i`, so the list has exactly one entry per rule.
* `completedLMWords` / `completedLMSet` (its `dedup`).
* `heckeCompletedRewritingSystem_lm_mem` — soundness: every rule leads on a word
  in the list. This is `_lm_cases` with the existentials discharged into list
  membership, and it is what makes the count a statement about the rule set
  rather than about a list someone typed.
* `overlapTriples` — the shapes, computed.
* `mem_overlapTriples` — the bridge. Stated on **words**, not on compositions, so
  it covers a composition of *any two rules* with those leading monomials,
  including two distinct rules leading on the same word.

The five counts depend on **no axioms at all** (`#print axioms`: "does not depend
on any axioms") — pure kernel computation.

### Why the degenerate shapes are kept

`OverlapComposition` places no condition on `left` or `right`. `left = right = []`
is therefore a legal composition, and §4j makes it an *inhabited* one: the
Yang–Baxter and Bokut–Shiao rules at `j = i − 1` lead on the same word. Dropping
the degenerate shapes would have silently dropped a real obligation.

## §4l — the degenerate shapes resolve

Two mechanisms, both machine-checked:

* `OverlapComposition.spoly_isZero_of_self` (framework, `Basic.lean` §4) — a rule
  composed with itself over its whole leading monomial has S-polynomial the
  difference of an element with itself. Nothing Hecke-specific, so it lives with
  `spoly`.
* `DegenerateYbBs.{ybBs,bsYb}Overlap_spoly_isZero` — the Yang–Baxter and
  Bokut–Shiao relations are **exact negatives**, and their leading coefficients
  are `−1` and `+1` (deg-lex picks the word starting with the larger generator,
  which is the *subtracted* term in `yangBaxterRelation` and the *added* term in
  `bokutShiaoRelation`). So

      lc₂ • YB − lc₁ • BS  =  1 • YB − (−1) • BS  =  YB + BS  =  0

  identically, in both orderings of the pair. Not "reduces to zero" — zero.

Supporting, in the framework: `isNormalForm_of_isZero` (a zero element is in
normal form vacuously) and `reducesToNF_self_of_isZero`, which turns "the
S-polynomial vanishes" straight into the Gröbner–Shirshov obligation.

**What is not proved.** That these two mechanisms *cover* all thirteen degenerate
shapes. That needs the rule-level converse of `_lm_cases` — at each of the ten
singleton words the only rule is the obvious one, and at the three coincident
words the only distinct pair is YB/BS. The covering claim is true at n = 4 and is
stated as prose in the §4l docstring, explicitly flagged as unproved.

## What remains for the completeness proof

The 45 non-degenerate shapes. §4g does one of them (`NotAGSBasis.oc`, the very
overlap that refutes the *un*completed system). The remaining 44 are the work,
and `mem_overlapTriples` is how any of them gets connected back to a composition
of actual rules.

## §4m — two structural facts, and the inclusion half

Both decided by the kernel at n = 4.

* `overlapTriples_four_proper_overlap_length_one` — **every proper overlap is a
  single letter.** Not one of the 45 non-degenerate shapes overlaps in two or
  more generators. The reason is visible in the four families: every leading
  monomial is descending after its first letter (`σᵢσᵢ`, `σⱼσᵢσⱼ` with `j = i+1`,
  `σᵢσⱼ` with `j < i`, `bsWord₁`), so a suffix of length ≥ 2 ends low-then-high
  while every prefix of length ≥ 2 starts high-then-low. Only one letter can be
  both. Every composition is "`lm₁` ends with `x`, `lm₂` begins with `x`".
* `completedLMSet_four_infix_antichain` — **no leading monomial is a proper
  factor of another.**

The antichain settles the **inclusion half** of `IsGrobnerShirshovBasis`
structurally. `inclusion_contexts_empty` proves that *every* inclusion
composition of the completed system at n = 4 has both contexts empty and equal
leading monomials — with **no hypothesis about which rules are involved**,
because `decomposition` exhibits `inner.lm` as an infix of `outer.lm` and lengths
do the rest. So the inclusion half is exactly the shared-leading-monomial case,
which is handled by

* `InclusionComposition.spoly_isZero_of_self` (framework) — no context hypothesis
  needed there either: `lm = left ++ lm ++ right` forces both empty.
* `InclusionComposition.spoly_isZero_of_scaled` (framework) — the general form,
  `lc(inner) • outer = lc(outer) • inner` coefficientwise.
* `DegenerateYbBs.{ybBs,bsYb}Inclusion_spoly_isZero` — the YB/BS pair, via
  `relations_add_eq_zero`.

Cross-check worth noting: the antichain *implies* there are no shapes with one
context empty and the other not (`left = []` would make `a` a proper prefix of
`b`). And indeed 13 + 45 = 58 exactly — the enumeration has no third kind.

## Computational discharge of the whole n = 4 obligation set

`computations/hecke_gs_confluence_n4.py` →
`computations/hecke-gs-confluence-n4.witness.json`.

Exact over ℤ[h] with `h = q − q⁻¹` a free symbol; **no float is formed anywhere**
(verified: 0 raw floats in the witness). Builds the 16 rules to mirror the Lean
definitions one-for-one — the correspondence table is in the script docstring and
is the thing to check if the witness is ever doubted.

    rules                          16
    distinct leading monomials     13
    overlap shapes                 58   (13 degenerate, 45 proper)
    overlap compositions           92   failing: 0
    inclusion compositions         22   failing: 0
    proper-overlap reduction steps 428  (max chain 25)

**Every composition resolves.** So the completed system *is* confluent at n = 4,
and the Lean obligation set is known to be reachable rather than hoped to be.
The witness independently reproduces 13 / 58 / 13 / 45 — the same numbers Lean's
kernel decided by a completely different route.

It is a **witness, not a proof**, and the bean should not be read as if the
theorem were formalised. What it buys:

* No counterexample is lurking. Before this, "the completed system is a GS basis
  at n = 4" was Bokut & Shiao's claim specialised by hand.
* A cost estimate for the Lean side: **428 single reduction steps** across the 70
  proper-overlap compositions, max chain 25, histogram concentrated at 3 and 8.
* A blueprint: each chain entry is `(target monomial, rule, left, right,
  coefficient)`, which is exactly the data a `SingleStepReduction` witness needs.

### Cheap cases the witness identifies

* **4 compositions have S-polynomial identically zero**: the quadratic
  self-overlaps `σᵢσᵢσᵢ` (`Q_i` against itself, left = overlap = right = `[σᵢ]`).
  Reason: `heckeRelation i` is a polynomial in the single generator `σᵢ`, so
  left- and right-multiplication by `σᵢ` agree on every monomial of it. Not yet
  formalised — the obstacle is purely that `contextMul` is defined through
  `excise`, so a general-`m` case split is needed rather than a rewrite.
* **5 compositions resolve in one step**, all of the same shape as the §4g one:
  `Y12×F20`, `B121×F20`, `Y23×F31`, `B232×F31` (→ `B120`/`B231`) and
  `B231×F30` (→ `B230`). Braid-word-against-far-commutation, repaired by a single
  Bokut–Shiao rule.

## Revised remaining work

*Closed*: the inclusion half at n = 4 (structurally, down to the same covering
claim as §4l), the 13 degenerate overlap shapes, and 1 of the 45 proper shapes
(#4879's `refuting_overlap_resolves`).

*Open*: 44 proper overlap shapes at n = 4 ≈ 420 reduction steps, then the whole
of general `n`.

## §4n — the quadratic self-overlap, for every n

The 4 identically-zero compositions the witness flagged are now proved, and
proved **generally in n**, not at n = 4:

* `AlgElement.contextMul_gen_comm` (framework, `Elem.lean`) — if every monomial
  of `f` commutes with `x` *as a word* (`w ++ [x] = [x] ++ w`), then
  `contextMul [] f [x] = contextMul [x] f []`. Proof is two applications of
  `contextMul_shape` in opposite directions; no case split on the shape of `m`,
  which is what made the direct attempt through `excise` unpleasant.
* `heckeRelation_coeff_comm` — every monomial of the quadratic relation is a
  power of the one generator `σᵢ` (`σᵢσᵢ`, `σᵢ`, the empty word), so it commutes
  with `σᵢ`.
* `quadSelfOverlap` / `_spoly_isZero` / `_resolves` — the composition of the
  quadratic rule with itself over `σᵢσᵢσᵢ`, S-polynomial identically zero.

By §4m this is the *only* way the quadratic family meets itself: the overlap must
be a single letter, and `σᵢσᵢ` has just the one proper suffix.

### Trap

`rw` closes a goal by `rfl` only at *reducible* transparency, so
`[σᵢ,σᵢ] ++ [σᵢ] = [σᵢ] ++ [σᵢ,σᵢ]` — true by `rfl` at default transparency —
is left open after the rewrite that produces it. Four goals in this section
failed that way; each needed an explicit `; rfl`. Reads as "unsolved goals" on a
line that looks finished.

## §4o — Bokut–Shiao against far-commutation, as a family

§4g's `refuting_overlap_resolves` is one composition at `(i,j) = (3,1)`, proved by
`decide` on concrete words. It is not isolated: it is the `n = 4`, `j = i−1`
instance of a family that resolves for every `n`, and the family is now proved.

**The shape.** `bsWord₁ i j` ends in `σᵢ`; `farCommRelation i j₀` begins with
`σᵢ`. They overlap in that one letter (§4m: every proper overlap is one letter),
over `descWord i j ++ [σᵢ, σ_{j₀}]`, with `j₀ + 1 = j` — the far-commutation rule
extends the descending run by exactly one step.

**Why it resolves.** The ambient word cancels *identically*:
`bsWord₁ i j ++ [σ_{j₀}]` **is** `descWord i j ++ [σᵢ, σ_{j₀}]`, so no
word-distinctness argument is needed anywhere in the proof. What survives is
turned into the Bokut–Shiao words one index lower by `descWord_snoc`:

    descWord i j ++ [σ_{j₀}] ++ [σᵢ]  =  descWord i j₀ ++ [σᵢ]  =  bsWord₁ i j₀
    bsWord₂ i' i j ++ [σ_{j₀}]                                  =  bsWord₂ i' i j₀

So the S-polynomial **is** `bokutShiaoRelation i' i j₀`, and one application of
that rule in empty context annihilates it. *The obstruction at depth `j` is
repaired by the rule at depth `j−1`: the family completes itself downwards.*

`YangBaxterFarComm.oc` is the same composition with `yangBaxterRelation i' i` in
place of `bokutShiaoRelation i' i i'` — §4j puts them on the same leading
monomial, so the completed system carries two rules in this shape and both are
obligations. They differ by a sign and nothing else, so the S-polynomial is the
negative and the same rule kills it with coefficient `−1`.
`Completion.refuting_overlap_resolves` is *this* one at `(i',i,j₀) = (2,3,1)`.

### New infrastructure

* `AlgElement.contextMul_ofTerms_pair_coeff` (framework, `Elem.lean`) — a
  two-term relation in context is the same two terms in context. **Every** rule
  in this presentation is two-term and every S-polynomial is two such
  context-multiplications, so this is the lemma that stops each composition
  re-deriving the `excise` case split. It is what made §4o mechanical, and it is
  reusable for all 40 remaining shapes.
* `filter_desc_snoc` / `descWord_snoc` — the bottom-end mirror of §4h's
  `filter_desc_cons` / `descWord_cons`.
* `bokutShiaoRelation_lc = 1`, `farCommRelation_lc = 1`, and
  `bokutShiaoRelation_mem` (the general form of `Completion.bs31_mem`).

### Coverage at n = 4

The witness listed 5 single-step compositions.  `BokutShiaoFarComm.oc` covers
`B121×F20`, `B232×F31`, `B231×F30`; `YangBaxterFarComm.oc` covers `Y12×F20` and
`Y23×F31` (the latter being §4g's, now subsumed by a general theorem). All 5.

### Running total, of the 45 proper shapes at n = 4

    4   quadratic self-overlap        §4n, general in n, spoly identically zero
    5   BS/YB against far-commutation §4o, general in n, one step
    ---
    9   proved
    36  remaining

## CLAIM

`in-progress`, branch `claude/gs-completed-lm-cases`, PR #4892.

Claimed late: §4k–§4p and `computations/hecke_gs_confluence_n4.py` were all
written while this bean still said `todo`. Recorded here rather than quietly
fixed — that gap is exactly what a sibling session would have collided with.

## §4p — any two-term rule against the quadratic rule: 12 compositions, 3 steps

§4n resolves in *no* steps and §4o in *one*. This is the first family needing a
real reduction chain, and it is the largest single block left.

**The observation that makes it one family.** Every two-term rule of the
completed system has its two words in **cyclic position** — leading monomial
`u' ++ [σₓ]`, other word `σ_y :: u'`, the *same* `u'`:

    farCommRelation i j        u' = [σᵢ]           x = j   y = j    c =  1
    yangBaxterRelation i' i    u' = [σᵢ, σᵢ₋₁]     x = i   y = i−1  c = −1
    bokutShiaoRelation i' i j  u' = descWord i j   x = i   y = i−1  c =  1

The last because `descWord i j = σᵢ :: descWord i₋₁ j` (§4h), so
`bsWord₂ i' i j = σᵢ₋₁ :: descWord i j`. Nothing else about the rule is used —
the family theorem takes `r` abstractly.

**The chain.** The leading monomial ends in `σₓ`, so it meets `σₓσₓ` in that one
letter (§4m), over `u' ++ [σₓ, σₓ]`. The ambient word cancels and

    spoly = c · [ −(σ_y :: u' ++ [σₓ]) + h·(u' ++ [σₓ]) + u' ]

1. `σ_y :: u' ++ [σₓ]` **is** `σ_y ·(leading monomial)`, so `r` applies in the
   context `(σ_y, ε)` → `σ_yσ_y u'`;
2. which begins `σ_yσ_y`, so the quadratic rule **at `y`** applies — *a different
   generator from the one the composition is about*, which is precisely why this
   needs a chain rather than a one-rule annihilation — leaving `h·(σ_y :: u') + u'`;
3. what is left is `h` times `r`'s own relation, killed by `r` in empty context.

**Step 3 needs `h ≠ 0`**, and that is where `HeckeParams` finally earns its
`q > 0 ∧ q ≠ 1`: `HeckeParams.h_ne_zero`. The composition does **not** resolve at
`q = 1`. Worth stating plainly — it is the first place in this arc where the
deformation is load-bearing rather than carried along.

### Two things the proof taught

* **Only three conditions need words distinguished.** Every `CoeffEq` in the
  chain holds *unconditionally*: the cancellations are between coefficients and
  do not care whether two words happen to coincide. Only the three "the targeted
  coefficient is non-zero" side conditions need distinctness, and two of those
  are lengths. The third — leading monomial vs the other word, same length — is
  `word_ne`, derived from `lc = c ≠ 0`: were they equal the terms would cancel
  and the leading coefficient would be `0`.
* **`ofTerms` is a representation, not an element.** `yangBaxterRelation` lists
  its two terms in the opposite order to the family's normal form, and
  `ofTerms [a,b] ≠ ofTerms [b,a]` as *values* (different `support`, different
  `coeff` term) though they denote the same element. So `hrel` is stated
  **coefficientwise**, and `AlgElement.contextMul_coeff_congr` carries that
  through `contextMul`. Stating it structurally would have silently excluded
  Yang–Baxter from its own family.

### New framework lemmas (`Elem.lean`)

* `AlgElement.contextMul_ofTerms_coeff` — general `L`, subsuming the pair version
  §4o introduced; needed because the quadratic rule has **three** terms.
* `AlgElement.contextMul_coeff_congr` — `contextMul` respects `CoeffEq`.

### Coverage

`CyclicQuad.{farComm,yangBaxter,bokutShiao}_quad_resolves` are the three
instances; together they are the 12 three-step compositions the witness listed
(`Y01×Q1`, `B010×Q1`, `Y12×Q2`, `B121×Q2`, `Y23×Q3`, `B232×Q3`, `F20×Q0`,
`F30×Q0`, `F31×Q1`, `B120×Q2`, `B230×Q3`, `B231×Q3`).

## Running total at n = 4 — counted at *rule* level, which is what the GS
## predicate quantifies over

    overlap compositions      92
      degenerate              22   §4l  (all, modulo the covering claim)
      quadratic self-overlap   4   §4n  general in n
      BS/YB × far-commutation  5   §4o  general in n
      cyclic × quadratic      12   §4p  general in n
      ---------------------------
      proved                  43
      remaining               49

    inclusion compositions    22   §4m  (all, modulo the same covering claim)

In *shape* terms (58 shapes: 13 degenerate + 45 proper) that is 13 + 16 = 29 of
58. The two counts differ because three words carry two rules each (§4j), and
the rule-level count is the honest one.

The remaining 49 are the 4-, 5-, 6-, 8-, 9-, 10-, 12-, 15-, 19- and 25-step
chains: `Q × R` (the mirror of §4p, and *not* symmetric to it — the quadratic
rule on the left produces a different chain), then BS × BS and BS × F at
`j₀ ≥ j`.

## RELEASED 2026-08-10 — PR #4892 merged, claim dropped

Merged to main as `1d3f71c43c` (rebase). Landed: §4k enumeration, §4l degenerate
shapes, §4m the inclusion half + the two structural facts, §4n quadratic
self-overlap, §4o BS/YB × far-commutation, §4p cyclic × quadratic, and
`computations/hecke_gs_confluence_n4.py`.

Rule-level at n = 4: **43 of 92 overlap compositions and 22 of 22 inclusion
compositions proved.** §4n/§4o/§4p are general in `n`.

Back to `todo` — I stepped off to qou-x64l, so this is claimable. **Next step,
for whoever takes it:** `Q × R`, the mirror of §4p. It is *not* symmetric to
§4p — the quadratic rule on the **left** gives a different chain (the surviving
term is `[σₓ] ++ v` rather than `v ++ [σₓ]`), so it needs its own theorem, not a
corollary. 9 rule-level compositions, also 3 steps each, and the cyclic-position
hypothesis it needs is the *other* one: `v = u'' ++ [σ_z]` where `u = σₓ :: u''`,
which holds for far-commutation and Yang–Baxter but **not** for general
Bokut–Shiao — which is why `Q2 × B120` is 8 steps, not 3.

`AlgElement.contextMul_ofTerms_coeff` and `contextMul_coeff_congr` are already in
place and are what make each such family mechanical.

## CLAIM 2026-08-15 — §4q, the `Q × R` mirror

`in-progress`, branch `claude/auq3-quad-left-family`. Re-claimed by the agent
that released it on 2026-08-10; nothing advanced here in between
(`HeckeCompletion.lean` is unchanged at 1550 lines, §4e–§4p).

Context for the gap: I stepped off to qou-x64l, was away five days, and in that
time a sibling finished x64l from my pushed branch — `H4GeneratorAction.lean`
landed verbatim, `H4WordAction.lean` and `H4Cyclicity.lean` completed the route,
and the eight `MarkovTraceH4Gram*` modules are deleted. A stale claim should not
block someone who can finish the work, and it didn't. Recorded because the
claim/report discipline is only worth anything if the misses are written down
too.

## §4q — the quadratic rule on the **left**, and why it is not §4p's corollary

`CyclicQuadLeft`. Nine rule-level compositions, three steps each, general in `n`.

The two families need **opposite** cyclic-position hypotheses:

    §4p    lm r = u' ++ [σₓ]   other word   σ_y :: u'
    §4q    lm r = σₓ :: u''    other word   u'' ++ [σ_z]

Both hold for far-commutation and Yang–Baxter. Only §4p's holds for a general
Bokut–Shiao rule, because `bsWord₂ i' i j = σᵢ₋₁ :: descWord i j` puts the extra
letter on the **left**. So §4q reaches Bokut–Shiao only at `j = i − 1`, where §4j
identifies it with Yang–Baxter — and that is not cosmetic: it is exactly why
`Q2 × B120` is an **eight**-step composition and is *not* covered here. The
prediction recorded when this bean was released ("holds for far-commutation and
Yang–Baxter but not for general Bokut–Shiao") is confirmed by the proof needing
`le_refl` in the Bokut–Shiao instance.

The chain mirrors §4p with the ends swapped: `r` in context `(ε, σ_z)`, then the
quadratic rule **at `z`** in context `(u'', ε)`, then `r` in empty context on
`−h` times its own relation. Step 3 needs `h ≠ 0` again.

### One thing that differed from §4p in practice

`simp` normalises `(σₓ :: u'') ++ [σ_z]` to `σₓ :: (u'' ++ [σ_z])`, so the
word-inequality hypotheses have to be **stated in cons-normal form** and supplied
in the `Ne.symm` orientation — the filter condition that needs discharging is
`u'' = <long word>`, not the reverse. Stated the §4p way they are silently
unused and the coefficient goals stay open. Two of the three `ofTerms_coeff`
side conditions needed this.

And the `rw`-closes-only-at-reducible-transparency trap struck a third time, in
`quad_bokutShiao_resolves`: `[σᵢ', σᵢ] ++ [σᵢ']` and `[σᵢ', σᵢ, σᵢ']` need an
explicit `rfl` after the rewrite.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × far-commutation  5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      ---------------------------
      proved                  52
      remaining               40

    inclusion compositions    22   §4m   (all)

That is every 0-, 1- and 3-step composition the `n = 4` confluence witness
lists. What remains starts at four steps: `Q × B` for general Bokut–Shiao
(8 steps), then BS × BS and BS × far-commutation at `j₀ ≥ j`, up to the 25-step
chain.

## Correction — `Q2 × B120` is **4** steps, not 8

The §4q note above says eight. The witness says **four**, and the pattern is
`3 + (i' − j)`:

    Q1 × B010  j = i'      3 steps   (covered by §4q)
    Q2 × B121  j = i'      3
    Q3 × B232  j = i'      3
    Q2 × B120  i' − j = 1  4
    Q3 × B231  i' − j = 1  4
    Q3 × B230  i' − j = 2  5

So `Q × B` beyond §4q is **three** compositions, not a large block, and it is a
family with a *variable-length* chain — an induction on `i' − j`, not a fixed
three-step script. The qualitative claim §4q makes (Bokut–Shiao only fits at
`j = i − 1`) stands; the number attached to it was wrong.

## Where the remaining 40 actually are

    B × B   14        Y × B    6        B × Y    6
    B × F    5        Q × B    3        Y × Y    3
    Y × F    1        F × Y    1        F × B    1

**Seventeen of the forty involve a Yang–Baxter rule**, and §4j makes every such
rule the exact negative of a Bokut–Shiao rule at `j = i − 1`, with the opposite
leading coefficient. So they are not independent work — they are the same
compositions with a sign.

Two ways to cash that in, and it is worth recording that the *first* one already
suffices:

1. **Abstraction over the rule.** §4o/§4p/§4q are stated for an abstract
   two-term rule and instantiated three times each; the Yang–Baxter instance
   costs ~10 lines and no new mathematics. Any B-family theorem written the same
   way gets its Y-variants the same way.
2. **§6, the negation transfer** (below) — which makes them free rather than
   cheap, and is general.

## §6 — reduction respects `CoeffEq`, and negation (`Basic.lean`)

    SingleStepReduction.of_coeffEq_left      source may be swapped up to CoeffEq
    SingleStepReduction.neg                  run the same rule with −c
    MultiStepReduction.neg
    MultiStepReduction.congr_source          the disjunctive form — see below
    reducesToZero_congr / reducesToZero_neg
    OverlapComposition.spoly_coeff_neg_rule₁ negating a rule negates the spoly
    AlgElement.contextMul_coeff_neg          (`Elem.lean`)

### The obstacle, which is structural and not a proof weakness

`AlgElement` is a representation and `CoeffEq` is the equality that means
anything — but **`MultiStepReduction.refl` is syntactic**. So
`MultiStepReduction f' f` does *not* follow from `CoeffEq f' f`, and a
coefficientwise-equal source cannot simply be substituted into a chain.

`congr_source` gets through by concluding a **disjunction**:

    MultiStepReduction ord sys f' nf  ∨  CoeffEq f' nf

The `refl` case lands in the second disjunct; the `step` case either extends a
chain that already restarted at `f'`, or — when the previous stage only gave
`CoeffEq f' g` — restarts it with `of_coeffEq_left` on the last step. That
disjunction is exactly what the syntactic constructor costs, and
`reducesToZero_congr` absorbs it because a `CoeffEq` to a zero endpoint is
itself a resolution.

### Two tactic notes

`ring` is the wrong tactic here: `k` is only a `Ring`, and `ring` needs
commutativity, so it reports "made no progress" on goals that are true. The
import is `Mathlib.Tactic.NoncommRing` and the tactic is `noncomm_ring`. Second,
`show` cannot open `OverlapComposition.spoly` — it is not definitionally
transparent enough — so the S-polynomial has to be unfolded with
`simp only [OverlapComposition.spoly, …]` instead.

### QOU build check on §6 — red, and not from this change

`Basic.lean` is reached by `QOU/PhotonThreading.lean`, so §6 forced a full QOU
rebuild. It **failed**, on `QOU/SchurWeyl/QJucysMurphy.lean`.

Not caused here. That module's import closure is six QOU modules plus Mathlib
and contains **no UGB module at all**, while this branch's diff is one bean plus
three UGB files. A module that does not import a changed file compiles
identically, so the failure is main's.

Filed as **qou-yzl8** rather than fixed: `QJucysMurphy.lean` belongs to
`qou-ck0g`, in-progress under another session. Six `ring`-on-a-noncommutative-
algebra sites — the same trap §6 hit twenty minutes earlier, which is why it was
recognisable on sight. UGB itself is green (1212 jobs).

## §4r — the braid self-overlap `σᵢσᵢ₋₁σᵢσᵢ₋₁σᵢ`: setup landed, chain derived

The largest single block left: **twelve** of the forty. Three words carry it
(`10101`, `21212`, `32323`) and each carries **two** rules with that leading
monomial (§4j), so four ordered rule-pairs per word — `Y×Y`, `Y×B`, `B×Y`, `B×B`,
three of each. Stated for an abstract pair `r₁, r₂` it covers all twelve at once
and generally in `n`. They are twelve of the thirteen 8-step compositions in the
witness; the thirteenth (`B230 × F31`) is unrelated.

### Landed

`BraidSelfOverlap.oc` and **`oc_spoly_coeff`** — axiom-clean, UGB green
(1212 jobs). The S-polynomial is **two terms**, and the leading coefficients
enter only through their product, because the ambient word is reached from both
sides and cancels:

    spoly = c₁c₂ · ( σᵢσᵢ₋₁σᵢ₋₁σᵢσᵢ₋₁  −  σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁σᵢ )

### The chain, derived from the confluence engine

Eight steps. `I = σᵢ`, `J = σᵢ₋₁`, `K = c₁c₂`:

| # | target | rule | context | coefficient |
|---|---|---|---|---|
| 1 | `IJJIJ` | `Q_{i-1}` | `(I ∣ IJ)` | `K` |
| 2 | `JIJJI` | `Q_{i-1}` | `(JI ∣ I)` | `−K` |
| 3 | `IJIJ` | `r₁` | `(ε ∣ J)` | `K·h·c₁` |
| 4 | `JIJI` | `r₁` | `(J ∣ ε)` | `−K·h·c₁` |
| 5 | `JIJJ` | `Q_{i-1}` | `(JI ∣ ε)` | `K·h` |
| 6 | `JJIJ` | `Q_{i-1}` | `(ε ∣ IJ)` | `−K·h` |
| 7 | `IIJ` | `Q_i` | `(ε ∣ J)` | `K` |
| 8 | `JII` | `Q_i` | `(J ∣ ε)` | `−K` |

and the intermediate elements, which is the part worth having written down:

    F₀ = K·IJJIJ − K·JIJJI
    F₁ = K·IIJ + Kh·IJIJ − K·JIJJI
    F₂ = K·IIJ + Kh·IJIJ − K·JII − Kh·JIJI
    F₃ = K·IIJ − K·JII + Kh·JIJJ − Kh·JIJI
    F₄ = K·IIJ − K·JII + Kh·JIJJ − Kh·JJIJ
    F₅ = K·IIJ − K·JII + Kh·JI + Kh²·JIJ − Kh·JJIJ
    F₆ = K·IIJ − K·JII + Kh·JI − Kh·IJ
    F₇ = K·J + Kh·JI − K·JII
    F₈ = 0

**No intermediate exceeds five terms**, and `h²` appears in exactly one (`F₅`)
before cancelling at step 6. Four applications of the quadratic rule at `i − 1`,
two of the braid rule itself, two of the quadratic rule at `i`.

### Two hypotheses the chain forces

* **`c₁ · c₁ = 1`** for steps 3 and 4. The step coefficient must satisfy
  `c₃ · lc(r₁) = K·h` with `lc(r₁) = c₁`, and there is no division in a `Ring` —
  so `c₃ = K·h·c₁` works only when `c₁² = 1`. Both instances have `c = ±1`, so
  this costs nothing, but it has to be a hypothesis rather than an afterthought.
* **`h ≠ 0`** for steps 3–6, as in §4p and §4q.

### Why the chain is recorded rather than the steps written

Eight `SingleStepReduction`s against five-term intermediates is roughly 2.5× §4p,
and generating them inline made each element appear three times (source, target,
coefficient lemma) — unreadable. The next pass should name `F₀ … F₈` as
definitions first and generate against those. The table above is the
specification; it came from the engine, so it is a check on the Lean rather than
a guess the Lean would have to discover.

### §4r complete — the chain and all four instances

`chainStep1 … chainStep8`, `oc_reduces_to_zero`, and the four instances
`yb_yb_resolves`, `yb_bs_resolves`, `bs_yb_resolves`, `bs_bs_resolves`.
UGB green (1212 jobs), warning-free, axiom-clean.

`reducesToZero_congr` (§6) makes the last join — the chain runs on the explicit
element `F₀`, and `oc_spoly_coeff` says the S-polynomial is coefficientwise `F₀`.
Built for the negation transfer; this is where it first pays, and it is why the
chain can be stated on explicit elements instead of on `oc.spoly`.

**Three build facts, none visible from the statement:**

* **Heartbeats are budgeted per declaration.** Eight steps against five-term
  elements do not fit one 200 000 budget — the single theorem timed out at
  `elaborator` and again at `whnf`. Split into eight top-level theorems, each
  fits comfortably. Same lesson as the H₄ generator tables; second time it has
  cost a build.
* **Steps 3 and 4 leave goals `ring` cannot close**, because they hold only
  modulo `c₁ * c₁ = 1`: after `ring_nf` the terms carry `c₁ ^ 3`. Derive
  `hc3 : c₁ ^ 3 = c₁` and rewrite before the final `ring`. `linear_combination`
  is the natural tactic and is **not in scope in this file** — `Mathlib.Tactic`
  reaches `ring` but not it.
* **`F₀` does not mention `hp`** (it carries no `h`), so `variable`-driven
  binders gave it a different signature from `F₁ … F₇` and every call site
  mismatched. Made explicit and named `_hp`.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × far-commutation  5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      braid self-overlap      12   §4r   general in n
      ---------------------------
      proved                  64
      remaining               28

    inclusion compositions    22   §4m   (all)

## Build-cache note (2026-08-15)

Checked the cache mechanism after being pointed at it. `lake-cache/qou-v4-24-0`
is restored automatically on SessionStart by
`scripts/lean-cache-restore.sh` — which is **why** the UGB rebuilds in this
session cost 12–16 s rather than a Mathlib build. Nothing here needed reseeding
for that reason.

Two things worth recording:

* `scripts/lean-olean-cache-seed.sh` **excludes paper oleans by default**
  (`SEED_PAPER=1` opts in) precisely because they go stale the moment Mathlib is
  rebuilt. So seeding this branch's UGB oleans would be wrong — they are branch
  state, not main.
* The expensive thing this session did that a sibling would repeat is **not**
  UGB: it is the **full QOU rebuild** (5407 modules, ~40 min), triggered because
  `QOU/PhotonThreading.lean` imports UGB, so any edit to
  `UGB/GrobnerShirshov/Basic.lean` or `Elem.lean` invalidates the whole QOU
  tree. §6 touched both. Worth knowing before editing UGB's lower layers:
  a leaf-only change (`HeckeCompletion.lean`) costs 13 s, a `Basic.lean` change
  costs ~40 min downstream.

A production reseed is a force-push to a shared branch, so it is not something
to do unilaterally mid-arc — flagged to the owner rather than done.

## §4s — Bokut–Shiao against far-commutation at the **same** index (3 compositions)

The other neighbour of §4o. §4o puts the far-commutation rule one index *below*
the Bokut–Shiao rule's bottom (`j₀ + 1 = j`) and resolves in one step, because
the S-polynomial **is** the Bokut–Shiao rule at `j₀`. Here the two rules share
their bottom index, and that changes the shape completely: `descWord i j` already
ends in `σⱼ`, so both surviving terms end in `σⱼσⱼ` and the quadratic rule has to
fire twice before the family's own rules can.

Writing `jp` for `j + 1`, so `descWord i j = descWord i jp ++ [σⱼ]`:

    spoly = descWord i jp ++ [σⱼ, σⱼ, σᵢ]  −  bsWord₂ i' i jp ++ [σⱼ, σⱼ]

| # | target | rule | context | coefficient |
|---|---|---|---|---|
| 1 | first term | `Q_j` | `(descWord i jp ∣ σᵢ)` | `1` |
| 2 | second term | `Q_j` | `(bsWord₂ i' i jp ∣ ε)` | `−1` |
| 3 | `bsWord₁ i j` | Bokut–Shiao at `j` | `(ε ∣ ε)` | `h` |
| 4 | `bsWord₁ i jp` | Bokut–Shiao at `jp` | `(ε ∣ ε)` | `1` |

so the `h` term the two squares leave behind is the Bokut–Shiao relation at `j`
and the constant term is the one at `jp` — §4o's downward self-completion again,
reached through the quadratic rule instead of directly. General in `n`;
sorry-free (`propext, Classical.choice, Quot.sound` only).

**The side condition is not an extra hypothesis.** Step 4 needs
`bokutShiaoRelation i' i jp` to *be* a rule, i.e. `j + 1 ≤ i − 1`, which is
exactly the condition for `σᵢσⱼ` to be a far-commutation word in the first place.
At `j = i − 1` there is no composition here to resolve — `σᵢσᵢ₋₁` is a braid
word, and that case is §4r's. So `resolves` takes the far-commutation side
condition `j + 1 < i` and nothing else.

**What made it cheap.** Every word in the chain is `descWord i jp` prefixed or
suffixed, and `descWord_cons` says `descWord i jp` begins with `σᵢ` while every
`bsWord₂`-side word begins with `σᵢ₋₁`. One `head_ne` lemma (plus its symmetric
form) discharges every distinctness obligation except a single length count.
That is why this is 4 steps of ~15 lines each and §4r was 8 of ~25: §4r's words
are five explicit letters with no structural handle.

Four steps, four declarations — the per-declaration heartbeat budget again,
applied pre-emptively this time rather than after a timeout.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × far-comm (j₀+1=j) 5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      braid self-overlap      12   §4r   general in n
      BS × far-comm (same j)   3   §4s   general in n
      ---------------------------
      proved                  67
      remaining               25

    inclusion compositions    22   §4m   (all)

Re-derived independently from `hecke-gs-confluence-n4.witness.json` by
classifying all 92 records against the sections rather than by adding up what
each section claims — the two agree, including the fact that §4q reaches
Bokut–Shiao only at `j = i − 1` (3 of the 12 `Q × ?` shapes stay open).

**The remaining 25, by chain length** (all from the witness):

    4–5 steps    Q × B at j < i−1                         3    steps 3 + (i′−j)
    6–8 steps    BS/YB × F and F × BS/YB at j₀ ≢ j        5
    9–25 steps   BS/YB × BS/YB                           17

The 3 `Q × B` are the cheapest thing left and the natural next target: they are
§4q's missing instances, and §4q already says why they cost `3 + (i′−j)` rather
than 3 — `bsWord₂` puts its extra letter on the left, so the `u'' ++ [σ_z]`
hypothesis fails and the chain has to walk `descWord i j` down one letter at a
time. Variable-length in `i′−j`, so it needs induction over the descending run,
which is the first place in this arc a fixed script will not do.

## §4t — the quadratic rule against a **general** Bokut–Shiao rule (3 compositions)

§4q's missing instances, and the first family in this arc whose chain length is
**not constant**. §4q reaches the quadratic-on-the-left composition for
far-commutation, Yang–Baxter and Bokut–Shiao at `j = i − 1`, and says exactly why
the general Bokut–Shiao rule is not among them: `bsWord₂ i' i j = σᵢ₋₁ :: descWord i j`
puts the extra letter on the **left**, so for `j < i − 1` there is no `σ_z`
closing the cycle. That prediction — "8 steps rather than 3" in §4q's prose — was
half right; the engine says `3 + |v|` where `v = descWord i−2 j`, i.e. `4, 4, 5`
at `n = 4`.

Writing `v` for `descWord i−2 j`, so `descWord i' j = σᵢ₋₁ :: v`:

    spoly = σᵢ σᵢ₋₁ σᵢ σᵢ₋₁ v  −  h · bsWord₁ i j  −  σᵢ₋₁ v σᵢ

| # | target | rule | context | coefficient |
|---|---|---|---|---|
| 1 | `σᵢσᵢ₋₁σᵢσᵢ₋₁v` | Yang–Baxter | `(ε ∣ σᵢ₋₁ v)` | `−1` |
| 2 | `σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁v` | `Q_{i−1}` | `(σᵢ₋₁σᵢ ∣ v)` | `1` |
| 3 | `bsWord₁ i j` | Bokut–Shiao at `j` | `(ε ∣ ε)` | `−h` |
| 4… | — | far-commutation | walking | `1` |

After three fixed steps what is left is `σᵢ₋₁ σᵢ v − σᵢ₋₁ v σᵢ`: one generator on
the wrong side of `v`. Every letter of `v` has index at most `i − 2`, so each is
a far-commutation partner of `σᵢ`, and the tail of the chain walks `σᵢ` across
`v` one letter at a time until the two terms coincide and cancel.

**`farComm_transport` is the reusable part.** Stated for an arbitrary word `w`
and an arbitrary left context `a` rather than for `descWord`:

    (∀ y ∈ w, y.index + 1 < x)  →
      c·(a σₓ w) − c·(a w σₓ)  →*  (coefficientwise zero)   in |w| steps

The induction is on `w`, and the left context has to be a parameter because it
grows: the letter just passed becomes part of the context for the next step. The
17 open `B × B` compositions all end in the same kind of tail, so this should pay
again rather than being one-family scaffolding.

Two things that made it go in one build:

* **State the stages over `v`, not over `descWord i' j`.** With every word an
  explicit cons-list over one shared `v`, all but one distinctness obligation is
  a length count on `List.length_cons` / `List.length_append`; the exception is
  `bsWord₁` against `bsWord₂`, same length, separated by the first letter.
* **`obtain ⟨yi⟩ := y` in the induction step.** `farCommRelation x y.index` has
  leading monomial `[σₓ, σ_{y.index}]`, which is *defeq* but not *syntactically*
  `[σₓ, y]` — enough to make `split_ifs` treat one word as two. Destructing the
  generator first makes the letter literally `⟨yi⟩` everywhere.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × far-comm (j₀+1=j) 5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      braid self-overlap      12   §4r   general in n
      BS × far-comm (same j)   3   §4s   general in n
      quadratic × general BS   3   §4t   general in n
      ---------------------------
      proved                  70
      remaining               22

    inclusion compositions    22   §4m   (all)

**The remaining 22**, re-derived from the witness:

    6–8 steps    BS/YB × F at j₀ < j, and F × BS/YB      5
    9–25 steps   BS/YB × BS/YB                          17

Next: the 5 mixed far-commutation shapes at `j₀ < j` (6–8 steps). They are the
same "letter on the wrong side of a descending run" situation §4t just solved, so
`farComm_transport` should carry most of them; `F × BS/YB` is the one with the
far-commutation rule on the *left*, which is a different overlap and may need the
mirror transport (moving a letter leftwards). After that, the 17 `B × B`, whose
25-step worst case is the largest single obligation in the file.

## §4u — far-commutation on the **left**, against Bokut–Shiao or Yang–Baxter (2)

§4o, §4s and §4t all put the far-commutation rule on the *right* of the
composition. This is the other side: `farCommRelation x m` leads on `σₓσ_m`, a
Bokut–Shiao or Yang–Baxter rule leads on a word beginning with `σ_m`, and they
overlap in that letter. Writing the second rule as `c·(σ_m :: u'') − c·w₂`:

    spoly = c · (σₓ :: w₂)  −  c · (σ_m :: σₓ :: u'')

`m + 1 < x` is the far-commutation side condition, and **no letter of either
word has index above `m`** — so `σₓ` commutes with everything in sight and is
simply a passenger in both terms. Two transports and one rule application:

| phase | term | steps |
|---|---|---|
| 1 | `σₓ :: w₂` → `w₂ ++ [σₓ]` | `\|w₂\|` |
| 2 | `σ_m :: σₓ :: u''` → `σ_m :: (u'' ++ [σₓ])` | `\|u''\|` |
| 3 | the rule, in the context `(ε ∣ σₓ)` | `1` |

After phase 2 the second term is the rule's leading monomial with `σₓ` appended,
so one application turns it into `w₂ ++ [σₓ]` and the terms cancel. Both `n = 4`
instances are 6 steps. Stated for an abstract rule in that two-word shape, so
Bokut–Shiao and Yang–Baxter are two instantiations — §4j's doubling again.

**The transport needed a bystander, and needed it in both list slots.**
`farComm_transport` (§4t) moves a generator in an element whose *other* term is
the transport's own destination, so the two cancel at the end. Here the other
term is a bystander that must be carried untouched, and the step's
"targeted coefficient is non-zero" condition needs it told apart from every
intermediate word. Hence `farComm_transport_snd` / `_fst` — the same induction
with the bystander in the second and the first slot.

Both slots are genuinely required and this is not an accident of presentation:
each phase transports a *different* term, so whichever slot phase 1 leaves the
moving term in, phase 2 needs the other. `MultiStepReduction` composes only up to
syntactic equality of the joining element (`refl` is the constructor), so the
list order cannot be permuted mid-chain. §6 has `SingleStepReduction.of_coeffEq_left`
and a disjunctive `MultiStepReduction.congr_source` but no target-side twin, and
adding one would not have helped: a `refl` run has nothing to retarget.

The collision hypothesis is phrased over splittings —
`∀ u v, u ++ v = w → p ≠ a ++ (u ++ (σₓ :: v))` — because that enumerates exactly
the words the run passes through. It specialises cleanly under the induction
(prepend the crossed letter to `u`) and at both call sites it is discharged by a
first-letter comparison.

Two build notes:

* **`simp` normalises `(q :: t) ++ [σₓ]` to `q :: (t ++ [σₓ])`**, so a
  distinctness hypothesis stated in the first form is silently unused and the
  goal survives. Same lesson as the §4r word-inequality one; state such
  hypotheses in cons-normal form.
* **`omega` will not reduce `(⟨m⟩ : HeckeGen n).index.val` to `m.val`.** It is
  definitional, but omega's preprocessing does not do projection-of-constructor,
  so every such goal needs a `show m.val ≤ …` first. Cost three separate errors
  in one build.
* **Implicit arguments behind a `refine` hole**: `q` and `t` appear only in
  `hrel`, which was left as `?_`, so they could not be inferred and the whole
  `refine` failed to unify. Pass them by name.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × far-comm (j₀+1=j) 5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      braid self-overlap      12   §4r   general in n
      BS × far-comm (same j)   3   §4s   general in n
      quadratic × general BS   3   §4t   general in n
      far-comm × BS/YB         2   §4u   general in n
      ---------------------------
      proved                  72
      remaining               20

    inclusion compositions    22   §4m   (all)

**The remaining 20:**

    3    BS/YB × F with j₀ neither j nor j−1     6, 6, 8 steps
    17   BS/YB × BS/YB                           9 … 25 steps

The 3 are two different situations, and neither is §4s or §4o:

* `j₀ + 1 < j` (Y23×F30, B232×F30) — `σ_{j₀}` is *below* the whole descending
  run, so it commutes past all of it. This is a transport again, but the
  **mirror** one: the small letter moves *left* through big ones, where §4t/§4u
  move a big letter right through small ones. Same rule, opposite role in it.
  It also needs a right context, which neither current transport carries.
* `j < j₀` (B230×F31) — `σ_{j₀}` lands *inside* the run's index range, so it does
  not commute past `σ_{j₀±1}`. The engine's chain shows why: the tail of the
  first term is `descWord j₀ j ++ [σ_{j₀}] = bsWord₁ j₀ j`, so the Bokut–Shiao
  rule at the *inner* index fires first and the family is genuinely nested.

So the honest next step is the mirror transport (with a right context), which
closes 2 of the 3 and is also what the long `B × B` tails will want; `j < j₀` is
its own small family.

## §4v — Bokut–Shiao / Yang–Baxter against far-commutation **below** the run (2)

The third regime of `BS/YB × farCommRelation i j₀`, and with it the
far-commutation block is finished bar one composition. The three regimes by where
`j₀` sits relative to the run `descWord i j`:

    j₀ + 1 = j     §4o   1 step    the S-polynomial *is* the rule one index lower
    j₀ = j         §4s   4 steps   a square at each end
    j₀ + 1 < j     §4v   6 steps   σ_{j₀} is below the run and commutes past it
    j < j₀         open  8 steps   σ_{j₀} lands *inside* the run's index range

For `j₀ + 1 < j` every letter of the run has index at least `j > j₀ + 1`, so the
stray `σ_{j₀}` in each term of

    spoly = c · (descWord i j ++ [σ_{j₀}, σᵢ])  −  c · (w₂ ++ [σ_{j₀}])

commutes all the way to the front. Two transports (`|descWord i j|` and `|w₂|`
steps) then one application of the rule in the context `(σ_{j₀} ∣ ε)`, and the
terms cancel. Every side condition in the whole section reduces to two letter
inequalities, `q ≠ σᵢ` and `q ≠ σ_{j₀}`, where `q` is the first letter of the
rule's other word.

**The mirror transport is a genuinely different lemma.** §4t and §4u move a
*big* generator rightwards through small ones; §4v moves a *small* generator
leftwards through big ones. The rewrite is the same rule `σ_aσ_b → σ_bσ_a`, but
the moving letter is the second factor of the leading monomial instead of the
first, so the induction recurses at the other end of the word, appends its step
with `MultiStepReduction.step` rather than `.head`, and needs a **right** context
that neither earlier transport carries.

**It also fixes §4u's list-slot duplication.** `farComm_transport_left` puts the
moving term at an arbitrary position `L₁ ++ (·) :: L₂` of the `ofTerms` list, so
one lemma serves both phases where §4u needed `_snd` and `_fst`. The enabler is
`ofTerms_coeff_mid`: the coefficient of a singled-out term when no other term
carries its word, proved by `List.filter_eq_nil_iff` on the two flanking lists.
The step's `CoeffEq` goal then goes through unchanged — after `List.filter_append`
and `List.sum_append` the two flanking sums are atoms and `ring` closes over
them. **If the `B × B` block needs a transport, use this form, not §4u's.**

Two build notes:

* `intro u v _` discarded the splitting hypothesis in one collision proof, and
  the `u = []` branch genuinely needs it — it is what says the remaining word is
  the bystander's. Cost one error; the fix is `intro u v huv` and `subst`.
* `rw` closes by `rfl` only at *reducible* transparency, so
  `rw [yangBaxterRelation_lm …]` does not finish `[σᵢ,σᵢ₋₁,σᵢ] = [σᵢ,σᵢ₋₁] ++ [σᵢ]`.
  Fifth time this has come up in this arc.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × F (j₀+1=j)       5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      braid self-overlap      12   §4r   general in n
      BS × F (j₀=j)            3   §4s   general in n
      quadratic × general BS   3   §4t   general in n
      far-comm × BS/YB         2   §4u   general in n
      BS/YB × F (j₀+1<j)       2   §4v   general in n
      ---------------------------
      proved                  74
      remaining               18

    inclusion compositions    22   §4m   (all)

**The remaining 18:**

    1    BS/YB × F with j < j₀   (B230 × F31)          8 steps
    17   BS/YB × BS/YB                                 9 … 25 steps

The single `j < j₀` composition is its own small family and is *not* a transport:
`σ_{j₀}` lands inside the run's index range, so it does not commute past
`σ_{j₀±1}`. The engine's chain shows what happens instead — the tail of the first
term is `descWord j₀ j ++ [σ_{j₀}] = bsWord₁ j₀ j`, so the Bokut–Shiao rule at the
*inner* index `j₀` fires first, and the family is nested rather than flat. Worth
doing next precisely because it is small and closes the entire far-commutation
block, leaving `B × B` as the single remaining shape.

## §4w — far-commutation **inside** the descending run (1) — the F block is closed

The fourth and last position `j₀` can take relative to `descWord i j`. With it
every composition involving a far-commutation rule is proved, and **`B × B` is
the only shape left**.

    j₀ + 1 = j     §4o   1 step    the S-polynomial *is* the rule one index lower
    j₀ = j         §4s   4 steps   a square at each end
    j₀ + 1 < j     §4v   6 steps   below the run: transport
    j < j₀         §4w   8 steps   inside the run: nested

Here `σ_{j₀}` is a letter the run already contains, so it does **not** commute
past `σ_{j₀±1}` and no transport applies to it directly. Splitting the run at
`j₀`,

    descWord i j = descWord i j₀₊ ++ (σ_{j₀} :: descWord j₀' j)

the first term of the S-polynomial ends in `descWord j₀ j ++ [σ_{j₀}]`, which is
`bsWord₁ j₀ j` — the Bokut–Shiao word at the **inner** index. So the inner rule
fires first, and what it leaves, `σ_{j₀'} σ_{j₀} descWord j₀' j`, has its lead
letter `σ_{j₀'}` *below* everything above it, which is now a transport. Same in
the second term. Five stages: inner rule, transport, inner rule, transport, outer
rule.

**The regime that creates the nesting also rules out the doubling.** `j < j₀` and
`j₀ + 1 < i` force `j < j₀ ≤ i − 2 < i − 1`, so `j ≠ i − 1` and Yang–Baxter never
leads on `bsWord₁ i j`. Unlike §4r, §4u and §4v there is no second instance —
this is the only family in the arc where the §4j doubling does not appear, and it
is a consequence of the side conditions rather than a case distinction.

The composition is §4v's, so `CyclicFarCommLow.oc` and its S-polynomial are
reused verbatim; only the chain is new. `farComm_transport_left` is reused for
both transports at different positions of the term list, which is what the
`L₁ ++ (·) :: L₂` form was for.

**`descWord_split` is the new word identity** and the one most likely to be
wanted again: `descWord i j = descWord i k ++ descWord k' j` for any interior
split `k' + 1 = k`. Proved by walking the bottom index down with `descWord_snoc`,
so the induction is on the gap `k' − j` and not on `List.finRange` — much shorter
than the filter-level argument `filter_desc_cons` / `filter_desc_snoc` use.

Build notes — every one of these has now cost a build more than once:

* **`₊` is not a valid Lean identifier character.** `j₀₊` in a `variable` line
  fails to parse and every downstream reference cascades into nonsense errors.
  Second time in this arc (§4s was the first). Subscript *digits* and the
  subscript letters are fine; subscript operators are not.
* **`omega` will not reduce `(⟨j.val + 1, h⟩ : Fin n).val`.** It shows up in the
  counterexample as an opaque atom. Every such goal needs `show j.val + 1 ≤ …`
  first — three errors in one build here.
* **`rw` closes by `rfl` only at *reducible* transparency**, and `List.append` on
  a cons needs default. Four sites in this section.
* **State word-inequality hypotheses in cons-normal form**, because that is what
  `simp` leaves the goal in; otherwise the hypothesis is silently unused and the
  goal survives.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n   general in n
      BS/YB × F (j₀+1=j)       5   §4o   general in n
      cyclic × quadratic      12   §4p   general in n
      quadratic × cyclic       9   §4q   general in n
      braid self-overlap      12   §4r   general in n
      BS × F (j₀=j)            3   §4s   general in n
      quadratic × general BS   3   §4t   general in n
      far-comm × BS/YB         2   §4u   general in n
      BS/YB × F (j₀+1<j)       2   §4v   general in n
      BS/YB × F (j < j₀)       1   §4w   general in n
      ---------------------------
      proved                  75
      remaining               17   all BS/YB × BS/YB

    inclusion compositions    22   §4m   (all)

**The last shape.** All 17 are `bokutShiaoRelation i' i j₁ × bokutShiaoRelation i' i j₂`
(with Yang–Baxter standing in at `j = i − 1`), overlapping in the single trailing
`σᵢ`. The S-polynomial is

    spoly = c₁c₂ · ( descWord i j₁ ++ bsWord₂ i' i j₂  −  bsWord₂ i' i j₁ ++ descWord i' j₂ ++ [σᵢ] )

and the chains run 9 to 25 steps — the 25 being `B230 × B230`, the largest single
obligation in the file. This is the block to design carefully rather than attack:
the tooling now in place is `farComm_transport` (rightwards), `farComm_transport_left`
(leftwards, any list position), `descWord_split`, `descWord_index_le/_ge`, and the
`ofTerms_coeff_mid` singling-out lemma. Worth extracting the 17 chains from the
engine first and looking for the common skeleton before writing any Lean.

## §4x — Bokut–Shiao against the braid word (6) — the first `B × B` column

`B × B` is not one family. Writing `a = i − j₁`, `b = i − j₂` for the two depths,
the engine's chain length depends only on `(a, b)`:

    (1,1) → 8    §4r   the braid self-overlap
    (a,1) → 9    §4x   this section, flat in a
    (1,2) → 10       (1,3) → 12
    (a,2) → 15       (2,3) → 19       (3,3) → 25

This is the column `b = 1` — the second rule leads on the braid word `σᵢσᵢ₋₁σᵢ`.

**Both terms reduce to one word.** With `E = descWord i−1 j₁`, so
`descWord i j₁ = σᵢ :: E`:

    spoly = c₂ · ( σᵢ E σᵢ₋₁ σᵢ σᵢ₋₁  −  σᵢ₋₁ σᵢ E σᵢ₋₁ σᵢ )   →*   0

via the common endpoint `σᵢ₋₂ σᵢ₋₁ σᵢ₋₂ σᵢ E`, five steps down the first term and
four down the second. Only three rules occur: Bokut–Shiao at `(i−2, i−1, j₁)`,
far-commutation `σᵢσᵢ₋₂`, and the outer rule itself; the branches differ only in
their last step, term 1 commuting `σᵢ` past `σᵢ₋₂` and term 2 straightening
`σᵢ₋₁σᵢ₋₂σᵢ₋₁`. Nine steps regardless of `a`, which is why this column is flat.

`c₂` is the second rule's leading coefficient — `1` for Bokut–Shiao at `j = i−1`,
`−1` for Yang–Baxter, the §4j pair. The **first** rule cannot double: `j₁ ≤ i−2`
makes its leading monomial strictly longer than the braid word.

**Every distinctness in the section is a first-letter comparison** among
`σᵢ, σᵢ₋₁, σᵢ₋₂`. The nine stages begin `σᵢ σᵢ σᵢ₋₂ σᵢ₋₂ σᵢ₋₂` and
`σᵢ₋₁ σᵢ₋₁ σᵢ₋₁ σᵢ₋₁` against passengers beginning `σᵢ₋₁` then `σᵢ₋₂`. No length
count and no word-uniqueness argument anywhere.

**`monicStep` is the reusable piece, and the one to build the rest of `B × B`
on.** Every rule the chain applies is monic and every stage is two terms, so one
lemma discharges all nine steps:

    monicStep hn hp r hr hrel hlm hLR L₁ L₂ a b W W' c hc hW hW' hne

It takes the stage words `W`, `W'` as *arbitrary*, tied to the rule's two words
by equations `W = a ++ L ++ b`, `W' = a ++ R ++ b` — which is what lets
consecutive steps compose without their context decompositions having to agree
syntactically, the thing that would otherwise force one bespoke theorem per step.
It is stated in the same `L₁ ++ (·) :: L₂` list-position-general form as
`farComm_transport_left`, so steps 1–5 move the first term and 6–9 the second
with no duplication. Each of the nine steps is then ~12 lines of arguments, and
the two `by simp` word equations are the only real content.

Two build notes:

* **`j₁` is not inferable from `oc`'s type** — it appears only inside the
  structure's fields, so `oc r₂ hi (by omega) hlm₂` leaves it a metavariable and
  the `by omega` fails against a goal containing `?m`. Pass `(j₁ := j₁)`. The
  omega counterexample naming a variable `↑↑(?m.85 nf)` is the tell.
* `BraidSelfOverlap.bs_hrel` takes `i' i` explicitly (they come from the
  namespace's `variable` line) where `bs_hlm` does not; the error surfaces as
  "`hi` … expected to have type `Fin ?m`".

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n
      BS/YB × F (j₀+1=j)       5   §4o
      cyclic × quadratic      12   §4p
      quadratic × cyclic       9   §4q
      braid self-overlap      12   §4r
      BS × F (j₀=j)            3   §4s
      quadratic × general BS   3   §4t
      far-comm × BS/YB         2   §4u
      BS/YB × F (j₀+1<j)       2   §4v
      BS/YB × F (j < j₀)       1   §4w
      BS × braid (b = 1)       6   §4x
      ---------------------------
      proved                  81   all general in n
      remaining               11

    inclusion compositions    22   §4m   (all)

**The remaining 11**, all `B × B` with `b ≥ 2`:

    (1,2)  4  10 steps    Y23×B231, B232×B231, Y12×B120, B121×B120
    (1,3)  2  12 steps    Y23×B230, B232×B230
    (2,2)  2  15 steps    B120×B120, B231×B231
    (3,2)  1  15 steps    B230×B231
    (2,3)  1  19 steps    B231×B230
    (3,3)  1  25 steps    B230×B230

The natural next column is `a = 1` (rows (1,2) and (1,3), six compositions, 10
and 12 steps) — the mirror of §4x with the braid word on the *left* of the
composition. Note it is **not** flat in `b`: 10 vs 12, so unlike §4x the chain
grows with the second depth and will need an induction or a transport rather than
a fixed script. The `(a,b)` both ≥ 2 corner (the last 5, up to 25 steps) is the
hardest and should come last.

## §4y — the `a = 1` row of `B × B`: designed and verified against the engine,
## transport proved, chain **not yet written**

Status: `farComm_transport_right` is proved and in the file; the eleven stages
and eight fixed steps below are derived and checked step-by-step against the
`n = 4` engine traces for both `B121 × B120` (b = 2) and `B232 × B230` (b = 3),
but are **not yet Lean**. Recorded here so the next session starts from the
design rather than re-deriving it.

**The row.** `a = 1` means `j₁ = i − 1`, so `rule₁` leads on the braid word
`σᵢσᵢ₋₁σᵢ` — and therefore doubles (Yang–Baxter or Bokut–Shiao at `j = i−1`,
leading coefficient `c₁ = ∓1`). `rule₂ = bokutShiaoRelation i' i j₂` is monic and
`j₂ ≤ i − 2`. With `T = descWord i−2 j₂` (so `descWord i' j₂ = σᵢ₋₁ :: T`):

    spoly = c₁ · ( σᵢ σᵢ₋₁ σᵢ₋₁ σᵢ σᵢ₋₁ T  −  σᵢ₋₁ σᵢ σᵢ₋₁ σᵢ₋₁ T σᵢ )

Both terms carry a **square** `σᵢ₋₁σᵢ₋₁`, which is why this row involves the
quadratic rule where §4x did not, and why `h` and `h²` appear. The chain is
**8 + 2|T| steps**, i.e. `8 + 2(b−1)` — *not* flat in `b`, unlike §4x's column.

| # | target | rule | context | coeff |
|---|---|---|---|---|
| 1 | `σᵢσᵢ₋₁σᵢ₋₁σᵢσᵢ₋₁T` | `Q_{i−1}` | `(σᵢ ∣ σᵢσᵢ₋₁T)` | `c₁` |
| 2 | `σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁Tσᵢ` | `Q_{i−1}` | `(σᵢ₋₁σᵢ ∣ Tσᵢ)` | `−c₁` |
| 3 | `σᵢσᵢ₋₁σᵢσᵢ₋₁T` | `BS(i−1,i,i−1)` | `(ε ∣ σᵢ₋₁T)` | `c₁h` |
| 4 | `σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁T` | `Q_{i−1}` | `(σᵢ₋₁σᵢ ∣ T)` | `c₁h` |
| 5 | `σᵢ₋₁σᵢσᵢ₋₁Tσᵢ` | `rule₂` | `(σᵢ₋₁ ∣ ε)` | `−c₁h` |
| 6 | `σᵢ₋₁σᵢ₋₁σᵢσᵢ₋₁T` | `Q_{i−1}` | `(ε ∣ σᵢσᵢ₋₁T)` | `−c₁h` |
| 7 | `σᵢσᵢσᵢ₋₁T` | `Q_i` | `(ε ∣ σᵢ₋₁T)` | `c₁` |
| 8… | `σᵢ` across `T` | far-comm | rightward transport | `−c₁` |
| … | `σᵢ₋₁Tσᵢσᵢ` | `Q_i` | `(σᵢ₋₁T ∣ ε)` | `−c₁` |
| … | `σᵢ` across `T` | far-comm | rightward transport | `c₁h` |

Two cancellations carry the proof: the `h²` terms `σᵢ₋₁σᵢσᵢ₋₁T` cancel at step 6,
and `σᵢσᵢ₋₁T` cancels at step 7. The eleven stages, in order, are

    S0  c₁·σᵢσᵢ₋₁σᵢ₋₁σᵢσᵢ₋₁T                −c₁·σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁Tσᵢ
    S1  +c₁h·σᵢσᵢ₋₁σᵢσᵢ₋₁T, c₁·σᵢσᵢσᵢ₋₁T
    S2  … −c₁h·σᵢ₋₁σᵢσᵢ₋₁Tσᵢ, −c₁·σᵢ₋₁σᵢTσᵢ
    S3  σᵢσᵢ₋₁σᵢσᵢ₋₁T ↦ σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁T
    S4  (5 terms; h² appears)
    S5  σᵢ₋₁σᵢσᵢ₋₁Tσᵢ ↦ σᵢ₋₁σᵢ₋₁σᵢσᵢ₋₁T
    S6  (h² cancels) → 4 terms
    S7  → c₁h·σᵢ₋₁σᵢT, c₁·σᵢ₋₁T, −c₁·σᵢ₋₁σᵢTσᵢ
    S8  → … −c₁·σᵢ₋₁Tσᵢσᵢ
    S9  → c₁h·σᵢ₋₁σᵢT, −c₁h·σᵢ₋₁Tσᵢ
    S10 → c₁h·σᵢ₋₁Tσᵢ, −c₁h·σᵢ₋₁Tσᵢ   (coefficientwise zero)

**Why `monicStep` does not apply.** It is for a rule with *two* words; `Q_i` has
three (`σᵢσᵢ`, `σᵢ`, `1`). Five of the eight fixed steps are quadratic, so they
need bespoke `hv` and `CoeffEq` proofs in the §4r style — and the stages merge
terms that a generic lemma would leave separate (the `h²` cancellation), so a
three-word generic step lemma would not help either: its target list is
determined, and these stages are deliberately the merged form.

Estimated size: eleven stage definitions, eight bespoke steps with up to five
terms and four distinctness obligations each, two transport applications, the
S-polynomial, the assembly and two instances — roughly §4r plus §4x together.
That is why it is recorded rather than half-written.

**What is proved this turn.** `farComm_transport_right` — the rightward transport
at an arbitrary list position, the mirror of `farComm_transport_left`. With it,
every transport in the file is an instance of one of two lemmas at an arbitrary
position; §4t's and §4u's narrower versions remain only because they are already
used. It is what steps 8… and the last block above need, since at those stages
the element has three terms and neither of the older bystander forms fits.

## Running total at n = 4, rule level (unchanged this turn)

      proved                  81   all general in n
      remaining               11   all BS × BS with b ≥ 2

    inclusion compositions    22   §4m   (all)

Next: write §4y's chain from the table above. The remaining five after it are the
`a, b ≥ 2` corner — `(2,2)` ×2, `(3,2)`, `(2,3)`, `(3,3)` at 15, 15, 19, 25 steps
— which should be attacked only once §4y's skeleton exists, since the 25-step
`B230 × B230` is the largest single obligation in the arc.

## §4y — the `a = 1` row of `B × B` (6) — **written and proved**

The design recorded last turn, now Lean. Eleven stages, eight bespoke steps, two
transports, general in `n`, sorry-free. It went in essentially as designed:
steps 1–4 built first try, steps 5–8 with the transports and both instances built
first try. That is what the turn spent on deriving and engine-checking the chain
bought.

`a = 1` is `j₁ = i − 1`, so `rule₁` leads on the braid word and doubles (§4j);
`rule₂ = bokutShiaoRelation i' i j₂` is monic and `j₂ ≤ i − 2`, so it cannot.
With `T = descWord i−2 j₂`:

    spoly = c · ( σᵢ σᵢ₋₁ σᵢ₋₁ σᵢ σᵢ₋₁ T  −  σᵢ₋₁ σᵢ σᵢ₋₁ σᵢ₋₁ T σᵢ )

Both terms carry a **square** `σᵢ₋₁σᵢ₋₁`, so unlike §4x this row runs through the
quadratic rule and picks up `h` and `h²`. Two cancellations carry it: the `h²`
terms `σᵢ₋₁σᵢσᵢ₋₁T` cancel at step 6, and `σᵢσᵢ₋₁T` at step 7, taking the element
from five terms back down to three. Then `σᵢ` crosses `T` twice — `8 + 2(b−1)`
steps in all, matching the engine's 10 and 12 at `b = 2, 3`.

**Both transports were already in the file, and they are different lemmas.** The
first has two bystanders (`v7`, `v10`) and needs the list-position-general
`farComm_transport_right` proved last turn; its collision hypothesis is pure
length arithmetic, `t+3` against `t+2` and `t+1`. The second, after the
cancellations, has the moving term and its own destination and nothing else —
which is exactly §4t's original cancelling `farComm_transport`, used unchanged.
Worth noting because it is the first place the *older, narrower* transport was
the right tool and the general one would have needed a collision proof that is
false at the final stage.

**Distinctness is almost all lengths.** The thirteen words have lengths
`t+5, t+4, t+3, t+2, t+1` over the shared tail, so a `congrArg List.length` plus
`omega` discharges most obligations; three go by first letter and one — step 4,
`σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁T` against `σᵢ₋₁σᵢσᵢ₋₁(T ++ [σᵢ])`, same length and same first
three letters — by the fourth, which is why `descWord_head` had to be proved:
`T` must be exhibited as `σᵢ₋₂ :: T'`.

`descWord_head` — the run begins with its top index whenever non-empty — is the
new general word lemma, by cases on `j = i` (`descWord_self`) and `j < i`
(`descWord_cons` at `i − 1`). It is the third such lemma after `descWord_cons`,
`descWord_snoc` and `descWord_split`, and the natural one to reach for whenever a
distinctness argument needs to see a run's head.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n
      BS/YB × F (j₀+1=j)       5   §4o
      cyclic × quadratic      12   §4p
      quadratic × cyclic       9   §4q
      braid self-overlap      12   §4r
      BS × F (j₀=j)            3   §4s
      quadratic × general BS   3   §4t
      far-comm × BS/YB         2   §4u
      BS/YB × F (j₀+1<j)       2   §4v
      BS/YB × F (j < j₀)       1   §4w
      BS × braid (b = 1)       6   §4x
      braid × BS (a = 1)       6   §4y
      ---------------------------
      proved                  87   all general in n
      remaining                5

    inclusion compositions    22   §4m   (all)

**The last five**, the `a, b ≥ 2` corner — both rules at general depth, neither
on the braid word:

    (2,2)  B120×B120, B231×B231   15 steps
    (3,2)  B230×B231              15
    (2,3)  B231×B230              19
    (3,3)  B230×B230              25

Both rules are now Bokut–Shiao proper (no Yang–Baxter doubling: `a, b ≥ 2` puts
both leading monomials longer than the braid word), so this is **one** family
with two independent depths rather than four. The S-polynomial is

    spoly = descWord i j₁ ++ bsWord₂ i' i j₂  −  bsWord₂ i' i j₁ ++ descWord i' j₂ ++ [σᵢ]

i.e. `D₁ σᵢ₋₁ σᵢ E₂ − σᵢ₋₁ D₁ E₂ σᵢ` with `D₁ = descWord i j₁`, `E₂ = descWord i' j₂`
— visibly symmetric in the two depths, which §4x and §4y were not (each had one
depth pinned at 1). The 15/15/19/25 counts suggest the chain length grows in both
`a` and `b`, so expect two nested transports or an induction on one depth with
the other abstract. Extract all five chains and look for the two-parameter
skeleton before writing anything, exactly as this turn did for the `b = 1`
column and the `a = 1` row.

## §4z — both depths at `i − 2` (2) — the first corner case

The corner `a = b = 2`, i.e. `j₁ = j₂ = i − 2`: the Bokut–Shiao rule against
**itself** at a proper overlap, the analogue of §4r one level down. Because
`a, b ≥ 2` puts both leading monomials strictly longer than the braid word,
neither rule can be Yang–Baxter — no §4j doubling, one composition per `i`, so
this is `B120 × B120` and `B231 × B231` at `n = 4`.

**Everything is explicit and there are no transports.** Both depths pinned at
`i − 2` make `descWord i j₁ = σᵢσᵢ₋₁σᵢ₋₂` and `descWord i−1 j₂ = σᵢ₋₁σᵢ₋₂`, so
every word is a literal five-, six- or seven-letter list in three generators and
there is no run left to cross. That is exactly why this was the corner to do
first; the remaining three reintroduce the runs and with them the transports.

    spoly = σᵢσᵢ₋₁σᵢ₋₂σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₂  −  σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₂σᵢ₋₁σᵢ₋₂σᵢ

Fifteen steps, and **thirteen of them apply a two-word monic rule** — the braid
rule at `(i−2,i−1)`, the braid rule at `(i−1,i)`, far-commutation `σᵢσᵢ₋₂`, and
the rule itself — so `monicStep` discharges each in a dozen lines. Only steps 4
and 7 are quadratic and written out. This is the first section where the §4x
investment in `monicStep` paid at scale: the thirteen applications were generated
mechanically from a table of `(rule, a, b, W, W')` and every one went through
unchanged.

`h` enters at the two quadratic steps and leaves at step 11, where
`σᵢ₋₂σᵢ₋₁σᵢσᵢ₋₂σᵢ₋₁σᵢ₋₂` and `σᵢ₋₂σᵢ₋₁σᵢ₋₂σᵢσᵢ₋₁σᵢ₋₂` carry `h` with opposite
signs and cancel. The pair is **kept in the term list rather than merged**,
because `monicStep` produces the unmerged list and merging would need a step of
its own; carrying it costs nothing since the surviving stages are still separated
by length or third letter.

Build note: the only failures were four more `rw`-does-not-close-by-`rfl`
(sixth occurrence in this arc) — everything else built first try.

## Running total at n = 4, rule level

    overlap compositions      92
      degenerate              22   §4l
      quadratic self-overlap   4   §4n
      BS/YB × F (j₀+1=j)       5   §4o
      cyclic × quadratic      12   §4p
      quadratic × cyclic       9   §4q
      braid self-overlap      12   §4r
      BS × F (j₀=j)            3   §4s
      quadratic × general BS   3   §4t
      far-comm × BS/YB         2   §4u
      BS/YB × F (j₀+1<j)       2   §4v
      BS/YB × F (j < j₀)       1   §4w
      BS × braid (b = 1)       6   §4x
      braid × BS (a = 1)       6   §4y
      BS × BS (a = b = 2)      2   §4z
      ---------------------------
      proved                  89   all general in n
      remaining                3

    inclusion compositions    22   §4m   (all)

**The last three**, all `B × B` with the depths unequal or both at 3:

    (3,2)  B230 × B231   15 steps
    (2,3)  B231 × B230   19
    (3,3)  B230 × B230   25

These are the general two-depth case, `spoly = D₁ σᵢ₋₁ σᵢ E₂ − σᵢ₋₁ D₁ E₂ σᵢ`
with `D₁ = descWord i j₁`, `E₂ = descWord i−1 j₂` both of arbitrary length. The
right frame is probably to prove it for abstract `D₁`, `E₂` with the runs crossed
by transports, rather than three more explicit chains — §4z is the `|D₁| = 3`,
`|E₂| = 2` instance of it, and its fifteen steps should reappear as the skeleton
with transports inserted where the runs are longer. Note `(3,2)` is also 15 steps
like `(2,2)`, which supports that reading: lengthening `D₁` alone does not add
steps, only lengthening `E₂` does — compare `(2,2) → (2,3)`, 15 → 19.

## §4aa — depths `i−3` and `i−2` (1) — and a correction on the corner's shape

`(a, b) = (3, 2)`. Taken next because **nothing in it is quadratic**: all fifteen
steps apply a two-word monic rule and every stage has exactly two terms, so
`monicStep` discharges the whole chain and `h` never appears. Six rules occur —
Bokut–Shiao at `(i−2,i−1,i−3)`, the braid rule at `(i−3,i−2)`, the three
far-commutations `σᵢσᵢ₋₂`, `σᵢσᵢ₋₃`, `σᵢ₋₁σᵢ₋₃`, and the composition's own first
rule — over four generators:

    spoly = x y z w y x y z  −  y x y z w y z x

with `x = σᵢ`, `y = σᵢ₋₁`, `z = σᵢ₋₂`, `w = σᵢ₋₃`. Nine steps take the second
term to `z y z w x y z w`, six take the first to the same word.

**Correction: there is no shorter chain to find.** Last turn I suggested the
three remaining corner cases would come out as §4z's skeleton with transports
inserted, and derived a candidate chain of `2a+1` and `a+b+1` steps — 10 for
`(2,2)` against the engine's 15. That is wrong. Reducing the two terms
*separately* to normal form takes

    (2,2)  7 + 8 = 15     (3,2)  8 + 7 = 15
    (2,3)  9 + 10 = 19    (3,3)  12 + 13 = 25

exactly the engine's totals. So the S-polynomial's chain **is** the two
reductions laid end to end, with no shared intermediate to cut, and the earlier
derivation had a step in the wrong direction — it transported a generator
leftwards past a letter where the rewrite only goes rightwards. Worth recording
because the same mistake is easy to repeat: `farCommRelation` orients
`σᵢσⱼ → σⱼσᵢ` with the *larger* index first, so the big letter moves right and
only right.

It also means the corner is **not** one family with a uniform chain in `(a, b)` —
`(2,2)` needs the quadratic rule twice and `(3,2)` not at all, at the same length
of 15. Each corner case is its own explicit chain.

## Running total at n = 4, rule level

      proved                  90   all general in n
      remaining                2

    inclusion compositions    22   §4m   (all)

**The last two:**

    (2,3)  B231 × B230   19 steps
    (3,3)  B230 × B230   25 steps

Both are mechanical now: extract the chain, classify each step's rule as monic or
quadratic, and generate. `(3,3)` at 25 steps is the largest single obligation in
the arc. The generator script pattern used for §4z and §4aa — a table of
`(rule, a, b, W, W')` per step, expanded into `monicStep` applications, with the
quadratic steps written by hand — is what makes them tractable; both sections
went in with only a hypothesis-order slip and lint to fix.

**Scope note, for whoever picks this up.** These counts are the `n = 4`
enumeration, which is what `§4k` computes and what the bean has tracked
throughout. Every *family* is proved general in `n`, but the corner sections
§4z, §4aa and the two remaining are general in `n` at **fixed depths** — `(a,b)`
pinned. Closing all 92 therefore settles `n = 4` and every family that occurs
there; the general-`n` theorem additionally needs the corner for arbitrary
`(a, b)`, which is still open and is the one genuinely unfinished piece of
mathematics rather than of bookkeeping.

## §4ab, §4ac — the last two, and **92 of 92**

`(2,3)` at nineteen steps and `(3,3)` at twenty-five. With them every overlap
composition of the `n = 4` enumeration is closed, and every inclusion composition
was already closed structurally by §4m.

`(2,3)` is **not** `(3,2)` transposed. §4aa needs no quadratic rule and runs in
fifteen steps; `(2,3)` needs two and runs in nineteen. The two depths enter the
S-polynomial in different positions — `D₁ σᵢ₋₁ σᵢ E₂ − σᵢ₋₁ D₁ E₂ σᵢ` — so
swapping them is not a symmetry of the problem, and the four corner cases really
are four separate chains.

`(3,3)` is §4z one level deeper and inherits its shape exactly: two quadratic
steps, `h` entering there and cancelling in the middle, everything else monic.
Its length is not extra difficulty — 12 + 13 = 25, the sum of the two separate
reductions, as for every corner case.

**The one real bug, and it is a trap worth naming.** Both sections were generated
from the engine's traces, and the engine picks whichever rule leads on the target
word — often `Y..`, the Yang–Baxter rule, whose **leading coefficient is −1**. I
substituted the Bokut–Shiao rule at the same leading monomial (§4j: they share
it) because `monicStep` needs a monic rule — but kept the engine's step
coefficients, which are computed against `lc = −1`. Every substituted step then
had the wrong sign. The fix is a rule, not a patch: **for a monic rule the step
coefficient is exactly the target term's coefficient in the source stage**, so
read it off the stage rather than the trace. §4aa was accidentally right because
its generator assigned coefficients by position; §4z likewise.

    generated sections   §4z  §4aa  §4ab  §4ac
    steps                 15    15    19    25
    monic (via monicStep) 13    15    17    23
    quadratic (by hand)    2     0     2     2

## FINAL — n = 4, rule level

    overlap compositions      92        proved 92, remaining 0
    inclusion compositions    22   §4m  (all)

    §4l  22   §4n   4   §4o   5   §4p  12   §4q   9   §4r  12
    §4s   3   §4t   3   §4u   2   §4v   2   §4w   1   §4x   6
    §4y   6   §4z   2   §4aa  1   §4ab  1   §4ac  1

`HeckeCompletion.lean` is 8000 lines, sorry-free, and every `resolves` depends on
`propext, Classical.choice, Quot.sound` and nothing else.

## What this does and does not settle

**Settles:** every composition of the completed Hecke rewriting system at `n = 4`
resolves, and all but the four corner families are proved for *every* `n` — the
statements are general, the `n = 4` enumeration only tells us which shapes occur.

**Does not settle:** the general-`n` theorem. Two gaps remain, and they are
different in kind:

1. **The corner at arbitrary depths.** §4z, §4aa, §4ab, §4ac are general in `n`
   but at *fixed* `(a, b)` — `(2,2)`, `(3,2)`, `(2,3)`, `(3,3)`. At `n ≥ 5` the
   corner has cases with `a` or `b` ≥ 4 that no section covers. This is the
   genuinely unfinished mathematics: the chains are not uniform in `(a, b)` —
   `(2,2)` needs the quadratic rule twice and `(3,2)` not at all at the same
   length — so a general treatment needs a real idea, not more generation.
2. **The enumeration itself.** §4k computes the overlap shapes by `decide` at
   `n = 4`. A general-`n` statement needs `overlapTriples` characterised
   abstractly, not enumerated.

Next session should start from (1): extract the `a = 4` chains by extending the
confluence engine past `n = 4`, and look for the pattern across `(2,2), (3,2),
(4,2)` and `(2,2), (2,3), (2,4)` before writing anything.

## Beyond n = 4 — the corner has **two regimes**, and confluence holds to n = 12

With all 92 compositions closed at `n = 4`, the open piece was the corner at
arbitrary depths (§4z/§4aa/§4ab/§4ac are general in `n` but at fixed `(a,b)`).
Rather than guess at it again, I measured it: re-parametrised the confluence
engine by rank — `N` is a module constant, so re-running `build_rules()` is the
whole change — and swept.

**Confluence holds at every rank from 2 to 12**, zero failing compositions:

     n   rules  overlap  inclusion   max chain
     4      16       92         22          25
     6      36      272         46          51
     8      64      604         78          85
    10     100     1136        118         127
    12     144     1916        166         177

That is 8992 overlap and 1010 inclusion compositions across the range, all
reducing to zero. It takes about 25 seconds.

**The corner splits into two regimes.** Writing `a = i − j₁`, `b = i − j₂`:

    a ≤ b   steps = 2ab − a² + 5a + 1   quadratic rule used twice
    a > b   steps = b² + 3b + 5         quadratic rule not used at all

Exact on all 325 corner cases across `n = 5..9` and every `i` — no step-count or
quadratic-count mismatch anywhere. Two things fall out:

* **The `a > b` regime does not depend on `a`.** Extra depth in the *first* rule
  adds no work at all, which is why `(3,2)`, `(4,2)` and `(5,2)` are every one of
  them fifteen steps. §4aa observed this for one pair without seeing it was a
  law.
* **The longest chain at rank `n` is the deepest corner**, `a = b = n − 1`,
  giving `n² + 3n − 3` — matching the observed maximum at every rank from 3 to 12.
  So the corner is not merely the last family, it is the *hardest* one, and its
  cost grows quadratically in the rank.

That last point settles the shape of the remaining work. The chain length is
**quadratic in the depths**, so no fixed script can cover the corner: a general
proof needs an induction on both depths with the two regimes separated, and the
regimes differ in kind — one uses the quadratic rule, the other never does. This
also explains, after the fact, why the four fixed-depth sections looked so
unalike: `(2,2)` and `(3,3)` sit on the diagonal (`a = b`, quadratic used),
`(3,2)` sits strictly below it (never used), and `(2,3)` above.

New artifact: `computations/hecke_gs_confluence_range.py` and its witness, which
asserts all five facts above and fails if any of them stops holding. It imports
the `n = 4` engine unchanged rather than copying it, so the two cannot drift.

## Where the arc stands

**Done.** All 92 overlap and all 22 inclusion compositions at `n = 4`, in Lean,
sorry-free. Every family general in `n` except the corner. Confluence verified
computationally to `n = 12`, with the corner's cost characterised exactly.

**Open, in order of size:**

1. **The corner at arbitrary `(a, b)`** — a genuine induction, two regimes, with
   the `a > b` regime the easier one to attempt first since it ignores `a`
   entirely and never touches the quadratic rule. The `a ≤ b` regime is the one
   whose length is quadratic in both depths.
2. **The shape enumeration for general `n`** — §4k computes `overlapTriples` by
   `decide` at `n = 4`; a general theorem needs it characterised abstractly. The
   rank sweep gives the target numbers (shapes `= (n−1)(n+2)/2 · …`, see the
   witness's `ranks` array) but not the characterisation.

## §4ad — the first depth-general corner: the whole `b = 2` column

The `a > b` regime's step count ignores `a`, and the natural guess was that the
extra depth rides along inertly. It does, and now that is proved rather than
measured.

**What varies with `a`, mechanically checked.** Abstracting the contiguous
relative block `[b+2 .. a]` of the descending run to a single symbol `T` and
comparing the resulting symbolic chains: for `b = 2, 3, 4` the stage words are
**identical** for every `a ≥ b+2`, step for step, coefficient for coefficient.
So each column stabilises at `a = b+2`, with `a = b+1` a special case below it.
(An earlier probe printed "DIFF" for these — that comparison keyed on rule
*names*, which embed the run's bottom index and so never compare equal across
`a`. The words, which is what matters, never differed.)

**The Lean statement.** `BokutShiaoCornerDepth.resolves`, hypothesis `j ≤ i − 3`
and nothing else about the depth. Fifteen steps, all monic, `h` never appears.
Writing `x, y, z, u` for `σᵢ … σᵢ₋₃` and `E = descWord (i−3) j`, every one of the
seventeen words is `(explicit prefix) ++ E ++ (explicit suffix)`, and `E` is
never inspected — not by a rule, not by a distinctness obligation. Eight of the
fifteen steps do not even take the depth hypothesis (their binder is `_hj`): the
three far-commutations and the fixed-depth Bokut–Shiao at `(i−2, i−1, i−3)` are
depth-blind, and the other seven carry it only to split the run's top letters
off via `descWord_cons`.

**It subsumes §4aa.** §4aa is the case `j = i − 3`, where `E = [σᵢ₋₃]`. §4aa is
kept rather than deleted because its chain is a genuinely different one: at that
depth the rule used at steps 5 and 13 degenerates to the braid word, and the
confluence engine picks the Yang–Baxter rule sharing that leading monomial —
leading coefficient `−1`, which is why §4aa reads differently step for step.
Both rules are in the completed system; both chains are valid. Using the
Bokut–Shiao form throughout is what makes one chain serve every depth, since
`monicStep` wants a monic rule.

**Build lessons.**

* `rfl` will not close `W = a ++ L ++ b` when `b = []` and the word ends in an
  abstract tail: `List.append` recurses on its *first* argument, so `E ++ []`
  is stuck where `E` is a variable. Nine of thirty context obligations failed on
  exactly this. `simp [<word>]` closes all thirty; explicit-list sections like
  §4aa never hit it because nothing there is stuck.
* Where the abstract tail sits only to the *right* of explicit letters,
  everything to its left still reduces, so all the other equalities are
  definitional. Placing `E` in one slot in every word — always
  `prefix ++ E ++ suffix` — is what keeps the whole section in that regime.

**Where this leaves the corner.** The `b = 2` column is closed for all `a ≥ 3`.
Remaining: the columns `b ≥ 3` (each stabilising at `a = b+2`, and nesting —
`b = 3`'s stabilised chain extends `b = 2`'s by a block `B_{i-4} F F F` inserted
after the first far-commutation run, `b = 4` extends it again, which is what an
induction on `b` would have to formalise), the special cases `a = b+1`, and the
whole `a ≤ b` regime where the quadratic rule appears twice and the length is
quadratic in both depths.

### The shape of the induction on `b` (read off the `b = 3` chain)

The columns nest, and now concretely. Writing rules in relative notation, the
stabilised chains are

    b = 2:  B21 F02 │ B21 F02 B32 F13 F03                      │ B10 B21ᵥ │ B10 B21 F02 B32 F13 F03
    b = 3:  B21 F02 │ B21 F02 B32 F13 F03 ⟨B43 F24 F14 F04⟩    │ B10 B21ᵥ │ B10 B21 F02 B32 F13 F03 ⟨B43 F24 F14 F04⟩

Each increment of `b` inserts the same kind of block **twice**, once per term of
the S-polynomial: one Bokut–Shiao step at the next generator down, then a run of
far-commutations carrying the newly exposed letter leftwards past the whole
prefix. The block for `b` has length `b + 1`, so

    steps(b) = steps(b−1) + 2(b + 1),   steps(2) = 15   ⟹   b² + 3b + 5  ✓

matching the fitted closed form. `b = 4` adds `B54 F35 F25 F15 F05` and comes
out at 33, as measured.

The far-commutation run is not new work: it is exactly a leftward transport of a
single generator past a descending run, which is `farComm_transport_left` from
§4v. What §4ad did with fifteen explicit `monicStep`s, the induction has to do
with a transport lemma instead, because the block length grows with `b`. The
words also need a *second* abstract run (the `b`-side one) alongside `E`, so the
`prefix ++ E ++ suffix` discipline becomes `prefix ++ E ++ mid ++ F ++ suffix`.
That is the next piece of work, and it closes the whole `a > b` regime at once
rather than one column at a time.

## §4ae — the `b = 3` column, and the generator behind both

`BokutShiaoCornerDepth3.resolves`: hypothesis `j ≤ i − 4`, twenty-three steps,
all monic, `h` absent, every word `(explicit prefix) ++ E ++ (explicit suffix)`
with `E = descWord i₄ j` never inspected. Sorry-free, standard axioms, full
library builds. Generators are named `i₀ … i₄` by distance below the top rather
than by primes — five levels of `'` was past the point of legibility.

**The cost of one more level, exactly.** Side by side with §4ad:

    b = 2:  B₂₁ F₀₂ │ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃                    │ B₁₀ B₂₁ᵛ │ B₁₀ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃
    b = 3:  B₂₁ F₀₂ │ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃ ⟨B₄₃ F₂₄ F₁₄ F₀₄⟩  │ B₁₀ B₂₁ᵛ │ B₁₀ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃ ⟨B₄₃ F₂₄ F₁₄ F₀₄⟩

One block, inserted twice — once per term. Confirms the induction shape recorded
above from the raw trace, now against the emitted Lean.

**The generator** is `scripts/gen-hecke-corner-column.py`, alongside the existing
`gen-gluing-lean.py`. It derives words, stages, rules and contexts from the
confluence engine's trace, so nothing is transcribed. Two things it needed that
the engine does not give:

* The engine's driver `clean`s zero coefficients, so the final stage — where the
  two words become equal and cancel — is simply absent from its output. The
  generator carries the two-term pair itself. Every rule reachable in this regime
  is monic with exactly two words, so a step is just "replace the redex word by
  the rule's other word"; the generator asserts that rather than assuming it.
* Because rule names embed the run's bottom index, a rule at the general depth
  and a rule at a fixed depth print alike. The generator distinguishes them
  structurally (bottom `= a`, or not) and picks the Bokut–Shiao form over the
  Yang–Baxter one where both share a leading monomial — the `−1` leading
  coefficient that cost a full debugging cycle in §4ab.

**Validation.** Re-deriving §4ad from the generator reproduces all seventeen
words and all fifteen rules and slot assignments exactly, against the table
worked out by hand. That is what licenses trusting it at `b = 3`.

**`rfl` after `rw`, made deterministic.** `rw` closes a goal by `rfl` only at
*reducible* transparency, so whether a trailing `rfl` is needed depends on
whether the rewritten side lands in the same cons/association shape as the
statement. It does when the statement keeps the `… ++ E ++ [x]` shape (the
general-bottom rules' `lm`), and does not when the statement is a flat literal
list (the fixed-depth rules, and the `descWord` splits). Writing `<;> rfl`
everywhere builds fine but draws a linter warning either way — "would suffice"
or "does nothing" — which is exactly the oracle needed to pin the rule down. The
committed output has neither.

**Correction.** §4aa's prose said "nine steps take the second term … six take the
first", contradicting its own "8 and 7" two paragraphs later; §4ad repeated the
wrong figures. The split is 8 and 7 — `V0 ⋯ V8` and `U0 ⋯ U7`, meeting at
`V8 = U7`. Both fixed. At `b = 3` it is 12 and 11.

## §4af — the corner is a loop, and its body is proved

Writing columns out one at a time does not scale: column `b` is `b² + 3b + 5`
steps, so each needs a longer script than the last. It does not have to. Setting
§4ad against §4ae shows the chain is **a loop over a single index**, and the body
of that loop is now proved: `CornerBlock.blockStep`, sorry-free, standard axioms.

**The invariant.** With `D = descWord i j₁` the long run and `j₂` the short one,
both terms march down through

    V:  R ++ D ++ descWord k j₂           →  (R ++ [σ_{k−1}]) ++ D ++ descWord (k−1) j₂
    U:  Q ++ D ++ descWord k j₂ ++ [σᵢ]   →  (Q ++ [σ_{k−1}]) ++ D ++ descWord (k−1) j₂ ++ [σᵢ]

as `k` runs from `i` down past `j₂`. Each pass is two moves: a Bokut–Shiao step
at top `k` — available because the `σ_k` ending `descWord k j₁` inside `D` is
immediately followed by the `σ_k` heading `descWord k j₂`, which is exactly where
the two runs meet and exactly what makes the redex — and a leftward transport of
the newly exposed `σ_{k−1}` across the part of `D` above `k`. So the block is one
`monicStep` plus one `farComm_transport_left` (§4v), its side condition from
`descWord_index_ge`. It built first try.

`Y`, the part of `D` above `k`, enters abstractly rather than as
`descWord i (k+1)`. That costs nothing and avoids naming `k + 1`, which matters:
the first pass has `k = i` and no such index need exist. `blockStep_top` is that
pass, and doubles as a witness that the hypotheses are satisfiable — worth having
for a statement with this many parameters, since a wrong index relation would
leave it true and unusable.

**Validated before writing.** `computations/hecke_corner_block_blueprint.py`
builds the block-decomposed chain from the invariant and checks every consecutive
pair really is one rule applied in one context: 48 cases, `b = 2 … 7`,
`a = b+1 … b+4`, no illegal step, endpoints meeting, lengths exactly
`b² + 3b + 5`. Predicted per side and confirmed:

    V = 2 + (b+1) + b(b+1)/2      U = b + b(b+1)/2 + 2

**A distinction that had to be got right.** At `a = b + 1` the engine does *not*
follow these blocks for `b ≥ 5`: the Bokut–Shiao step of pass `d` exposes a redex
that deg-lex prefers over finishing pass `d`'s transport, so the engine
interleaves. That is not a counterexample — a `SingleStepReduction` may rewrite
any redex, not only the largest — and the checker confirms the block chain is
legal there too. Checking the blueprint against *the engine's ordering* would
have reported a failure that was not one; checking it against *legality* is the
right test and is what the committed script does.

**Left to do for the whole `a > b` regime:** assemble the passes. The loop runs
`k` from `i` down past `j₂`, so it is an induction on `k.val − j₂.val` in the
style of `descWord_split_aux` (§4w). What needs care is the collision hypotheses:
each pass needs the bystander term to miss every word the pass passes through,
and the assembled statement has to carry that through the induction rather than
re-proving it per pass.

**Also:** a Lean identifier may not contain `′` (U+2032, PRIME) — only ASCII `'`.
The parse error lands on the *use* site, not the binder. Third member of this
family after `₊` and the `rw`-transparency trap.

## §4af cont. — the loop is proved (single term), and what blocks the two-term case

`CornerBlock.loop` and `CornerBlock.loopFromTop`, sorry-free, standard axioms.
`blockStep` iterated: `k` walks down one index per pass and what the passes leave
behind is the descending run `descWord kd ed` accumulated in front. The induction
is on passes remaining and carries `Y` — the part of the long run above `k` — as
a parameter rather than as `descWord i (k+1)`, so each pass hands the next
`Y ++ [σ_k]` and no index above `k` is ever named. `loopFromTop` enters at
`k = i` with `Y = []`, and doubles as a satisfiability witness.

This is the whole combinatorial content of the `a > b` corner. What remains is
bookkeeping about which words the bystanding term must avoid, not rewriting.

**A boundary case the design surfaced.** The last pass has `k = j₂`, where
`descWord_cons`'s hypothesis `j₂ ≤ k − 1` is false — but the identity still holds,
because the tail `descWord (j₂−1) j₂` is empty rather than a shorter run. Hence
two new lemmas: `descWord_of_lt` (a run from below its own floor is empty; the
module had no emptiness lemma at all) and `descWord_cons_le`, which needs the
floor only at or below `i`. `blockStep`'s short-run hypothesis is weakened to
`j₂ ≤ k` to match.

**The real obstruction to the two-term version, stated precisely.**
`farComm_transport_left`'s collision hypothesis quantifies over all splits
`u ++ v = w`, and the two extreme splits are the transport's *start* and its
*end*. So it demands the bystander differ from the transport's endpoint. In the
actual chain the bystander during the `V` loop **is** the final word `W`, and the
last pass's transport ends exactly at `W` — so that hypothesis is false there and
the lemma cannot be applied to the last pass as it stands.

That is not a flaw in the chain: `monicStep` only ever needs the *source* word to
be distinct, which is why §4ad and §4ae go through writing their transports out
as individual steps. Two ways forward, and the choice is the next decision:

* a variant of `farComm_transport_left` whose collision hypothesis covers only
  the sources — the existing proof already uses only those (the `nil` case
  discards the hypothesis outright), so this should be a weakening of the
  statement rather than new work; or
* peel the last pass off the loop and do its transport by hand.

The first is better if the weakened lemma really does fall out of the existing
proof, since §4t–§4v's other transport lemmas likely carry the same needlessly
strong hypothesis.

Also worth noting for the length bound: every rule in this regime preserves word
length — Bokut–Shiao maps `|descWord k j₁| + 1` letters to `2 + |descWord kd j₁|`,
which is the same — so length can never be used to separate the bystander from a
chain word. Distinctness has to come from a letter position, as it did in §4ad.

## §4af cont. — the two-term loop, and the transport hypothesis that blocked it

`CornerBlock.loopTwo` and `loopTwoFromTop`: the corner loop with the
S-polynomial's other term riding along. Sorry-free, standard axioms, full library
builds. The obstruction recorded last time is cleared.

**The weakening, and why it was available.** `farComm_transport_left`'s collision
hypothesis quantifies over all splits `u ++ v = w`, and the split `u = []` names
the transport's *final* word — which is exactly the bystander in the corner
chain, so the hypothesis is false where it is needed. Reading the proof: `hcol`
is applied only with a cons-headed first argument (`⟨yi⟩ :: u`, and `[⟨yi⟩]`),
and the `nil` case discards it outright. So `u ≠ []` suffices. Split into
`farComm_transport_left_sources` (the real proof, weak hypothesis) and
`farComm_transport_left` (a two-line corollary with the old statement), so §4v's
callers are untouched. `blockStep` now asks only for the weak form, and
`blockStep_top` consequently loses a hypothesis: with `Y` empty there is no split
with `u ≠ []` at all, so its collision obligation is vacuous.

**Two facts make the bystander uniform.**

* **It does not move.** At pass `k` it is `A ++ descWord kd ed ++ ⋯`; after the
  pass `A` has grown by `σ_kd` and the run shortened to `descWord kdd ed`, and
  `A ++ [σ_kd] ++ descWord kdd ed` is again `A ++ descWord kd ed`. Literally the
  same word at every pass, so the induction carries it unchanged.
* **Every word a pass rewrites begins, after `A`, with `σ_i`** — the pass's own
  source is `A ++ (descWord i j₁ ++ ⋯)`, and each word the transport visits is
  `A ++ (u ++ ⋯)` with `u` a *non-empty* prefix of the run above `k`, whose head
  is the run's head. The bystander begins with `σ_kd`, and `kd < i`. One letter
  separates it from everything in sight.

Hence `pass_hne` and `pass_hcol`, discharging both obligations of every pass from
data the loop already carries; the second needs only `hY`, since every letter
above `k` is more than one above `σ_kd` and so is not `σ_kd`. Both built first
try, as did `loopTwo` and its entry point. Helper `append_cons_ne`: two words
with a common prefix differ as soon as the next letter does.

Worth noting the earlier observation about lengths was the right warning and the
wrong tool — every rule here preserves length, so length is useless, but a single
*position* does the job, and it is the same position at every pass.

**What is left for the whole `a > b` regime.** The loop is the quadratic part and
it is done. Remaining is a fixed, small amount of work independent of `a` and `b`:
the two setup steps that take the first term to the loop's entry shape, the two
closing steps on the second term (a `B₁₀` and the fixed-depth Bokut–Shiao), and
the assembly against `oc.spoly`. Roughly the shape of §4ad's ends with its middle
excised.

## §4ag — the corner's four end steps, and the second loop variant

All four steps that bracket the loop are proved, sorry-free, standard axioms,
full library builds. Each built first try.

**A second loop variant was needed.** `loopTwo` hardcodes the bystander to be the
loop's own endpoint, which is right for the first term — it is heading for the
word the second term ends at. But while the *second* term runs its loop, the
parked word is the *first* term, `V2`, which is not the loop's endpoint. Hence
`loopTwoGen`, taking an arbitrary parked word `P` with the single hypothesis
`∀ z, P ≠ A ++ z`. That discharges every obligation of every pass at once,
because the accumulator only ever grows on the right of `A`, so every word any
pass rewrites has that form — and it is preserved by the induction, since
`(A ++ [σ_kd]) ++ z = A ++ ([σ_kd] ++ z)`. In the corner it holds because the two
terms start with different letters.

Note the two variants take the parked term in opposite list positions —
`loopTwo` second, `loopTwoGen` first — because that is the order the phases put
them in, and `MultiStepReduction.trans` needs the intermediate to match
syntactically rather than up to `CoeffEq`.

**The four steps**, in the order the chain takes them:

* `s1` Bokut–Shiao at top `i−1`, general bottom, inside `σᵢ · − · descWord i j₂`
* `s2` `σᵢσᵢ₋₂ → σᵢ₋₂σᵢ`, putting the first term into the loop's entry shape
* `s3` Bokut–Shiao at top `i`, at the tail
* `s4` the fixed-depth Bokut–Shiao at `(i−2, i−1, j₂−1)`, at the head

`s3` and `s4` need `descWord ed j₂ = []` — the run below `j₂` is empty — which is
`descWord_of_lt`, added for the loop's boundary case last time and reused here.
Every distinctness is again a first letter: `U0_ne_cons` (`σᵢ₋₁` against `σᵢ`)
for the setup pair, `V2_ne_cons` (`σᵢ₋₂` against `σᵢ₋₁`) for the closing pair.

None of the four rules needed a custom `hrel`/`hlm`: at general depth the words
are already `descWord`-shaped, so `fun v => rfl` and `bokutShiaoRelation_lm`
serve directly. That is the payoff for §4ad and §4ae having been written with the
abstract tail in one slot.

**What remains** is wiring only: `MultiStepReduction.trans` over
`s1, s2, loopTwoGen, s3, s4, loopTwo`, plus the `OverlapComposition` and its
`spoly` identity. The S-polynomial is already known to be `V0 − U0`:
`rule₁ = bokutShiaoRelation i₁ i j₁`, `rule₂ = bokutShiaoRelation i₁ i j₂`,
`left = descWord i j₁`, `overlap = [σᵢ]`, `right = descWord i₁ j₂ ++ [σᵢ]`, and
the two leading words cancel because `descWord i j₂ = σᵢ :: descWord i₁ j₂`.

## §4ag — the `a > b` regime is closed, at every pair of depths

`CornerGeneral.resolves`: the Bokut–Shiao rule at bottom `j₁` composed with the
one at bottom `j₂` reduces to zero whenever `j₁ < j₂ ≤ i − 2`. No bound on either
depth. Sorry-free, standard axioms, full library builds. Checked non-vacuous by
instantiating at rank 5, `a = 3`, `b = 2` — §4aa's case, now an instance.

**What the assembly amounted to.** Six pieces, in the order the engine takes them:

    s1 → s2 → loopTwoGen (second term's loop) → s3 → s4 → loopTwoFromTop (first term's)

and the two terms coincide. The chain length — `b² + 3b + 5`, quadratic in the
depths — is carried entirely by the two loop invocations; everything else is four
fixed steps. Wiring it was mechanical because the word definitions had been
chosen to match the loop lemmas' shapes syntactically, which matters:
`MultiStepReduction.trans` needs the intermediate to match on the nose, not up to
`CoeffEq`. Had `V2`, `U0`, `U1`, `W` been written in any other associativity the
chain would have needed bridging lemmas at every seam.

The composition is `rule₁ = bokutShiaoRelation i₁ i j₁`,
`rule₂ = bokutShiaoRelation i₁ i j₂`, `left = descWord i j₁`, `overlap = [σᵢ]`,
`right = descWord i₁ j₂ ++ [σᵢ]`; the two leading words cancel because the short
run splits as `descWord i j₂ = σᵢ :: descWord i₁ j₂`, which *is* the overlap.

**Scope, precisely.** This subsumes §4aa (`(3,2)`), §4ad (`b = 2`, all `a`) and
§4ae (`b = 3`, all `a`) — all of them `a > b`. It does **not** subsume §4z
`(2,2)`, §4ab `(2,3)` or §4ac `(3,3)`: those are `a ≤ b`, the other regime, where
the quadratic rule appears twice and the length is `2ab − a² + 5a + 1`. Those
three remain fixed-depth cases.

## Where the arc stands now

**Done.** All 92 overlap and 22 inclusion compositions at `n = 4`, sorry-free.
Every family general in `n`. The corner's **`a > b` regime general in both
depths**. Confluence verified computationally to `n = 12`.

**Open, in order of size.**

1. **The corner's `a ≤ b` regime**, general in both depths. Structurally harder
   than the one just closed: the quadratic rule appears twice, so the chain is
   not all-monic and `monicStep` does not reach every step; and the length
   `2ab − a² + 5a + 1` depends on *both* depths, so a single loop over one index
   will not do. Whether it factors as two nested loops is not yet known — that is
   the first thing to measure, the way §4af's blueprint was measured before any
   Lean was written.
2. **The shape enumeration for general `n`** — §4k computes `overlapTriples` by
   `decide` at `n = 4`; a general theorem needs it characterised abstractly.

## The `a ≤ b` regime, measured — and it is not one loop

Same order of work as §4af's blueprint: measure before writing Lean. New artifact
`computations/hecke_corner_le_regime.py` and its witness.

**The split.**

    prefix(a)     a² + a + 5 steps, depending on `a` alone, containing both
                  applications of the quadratic rule
    block(a,b)    ab − a² + 2a − 3 far-commutations, and nothing else
    two steps
    block(a,b)    the very same sequence again

    a² + a + 5 + 2[ab − a² + 2a − 3] + 2  =  2ab − a² + 5a + 1   ✓

exactly the fitted length. Checked at every `(a, b)` for `a = 2 … 5`,
`b = a … a+4`: twenty cases, no failure. Both blocks are far-commutations only,
they are identical sequences, the two middle steps are not far-commutations, and
no quadratic step occurs anywhere after the prefix.

**A wrong fit, caught.** My first reading of the chains gave `prefix = 6a − 1`
and `block = a(b−1) − a(a−1)/2`. Those fit `a = 2` and `a = 3` — and fail from
`a = 4` on, where the prefix is 25 and not 23. Both are quadratic in `a`, not
linear. This is why the script checks the *split* at each pair rather than
inferring it from the length: the length formula was right all along and would
have hidden the error indefinitely.

**Why this regime is harder than the one just closed.** The block is a **nested
double loop**, not a single one: `a` levels, level `p` a run of far-commutations
`F_{p,q}` with `q` ascending to `b`, of lengths `2, 3, 4, …` capped at `b−a+2`.

    a=3 b=5:  F24 F25 | F13 F14 F15 | F02 F03 F04 F05
    a=4 b=6:  F35 F36 | F24 F25 F26 | F13 F14 F15 F16 | F03 F04 F05 F06
    a=5 b=7:  F46 F47 | F35 F36 F37 | F24 F25 F26 F27 | F14 F15 F16 F17 | F04 F05 F06 F07

That is the structural reason the length depends on both depths rather than one,
and it is what `a > b` did not have. Two further differences: the prefix is
itself `a`-dependent and quadratic, and it contains the quadratic rule twice —
so `monicStep`, which carried every step of the other regime, does not reach it.

**What this suggests for the Lean.** The two blocks are the same sequence, so one
lemma serves both, and being pure far-commutations they should be a nested
application of `farComm_transport_left_sources` — an outer induction over levels
with an inner transport per level, rather than §4af's single loop. The prefix
looks like the genuinely new work: quadratic-rule steps at general depth, which
nothing in the development currently handles in a depth-general way. Measuring
*its* internal structure is the next step, and it should be done before any Lean,
on the evidence of the fit that just failed.

### The prefix, measured — and the regime is far less alien than it looked

Measured to `a = 7`, and the previous turn's assessment ("the prefix is the
genuinely new work; nothing handles it depth-generally") was too pessimistic.

**The prefix splits as `A · B₁₀ · C · D`** with

    A = (a² − 3a + 10)/2      C = a(a+1)/2      D = 2a − 1

and it is **self-similar with the whole chain**: `C = A[2:] ++ small(a)` and
`D = [B₁₀, B₂₁] ++ small(a)`, where `small(a)` is a far-commutation block of
length `2a − 3`. That is the same `block · two steps · block` shape the top level
has, one scale down. Both identities hold for every `a` from 3 to 7; at `a = 2`
the rule in `D`'s second slot is named `Y₂₁` rather than `B₂₁⟨2⟩` because at that
depth the Bokut–Shiao word degenerates to the braid word — the §4aa
coincidence again, not a structural exception, and the check accepts either.

**`A` is the loop I already have.** Writing it out at `a = 6`:

    B₂₁ F₀₂ │ B₃₂ F₁₃ F₀₃ │ B₄₃ F₂₄ F₁₄ F₀₄ │ B₅₄ │ Y₆₅ Q₆

after an initial `B₂₁ F₀₂`. Each group is exactly a pass of §4af's loop: a
Bokut–Shiao step at top `d`, then `d` far-commutations carrying the exposed
letter left. So `blockStep` and the loop lemmas apply here too, at `d = 1 … a−3`.

**What is actually new is two steps.** The chain uses the quadratic rule exactly
twice — end of `A`, end of `C`'s non-block part — and each time it is preceded by
a Yang–Baxter step, as `Y_{a,a−1} Q_a`. Everything else in the whole chain is a
loop pass or a far-commutation. So the new Lean content for this regime is:

1. the `Y_{a,a−1} Q_a` pair at general depth — the only place `monicStep` cannot
   reach, since the quadratic rule has three words;
2. the far-commutation blocks, `small(a)` and `block(a,b)`, as nested transports
   over `farComm_transport_left_sources`.

Both are bounded pieces of work, and (1) is two steps rather than a family. The
`a ≤ b` regime is not a second development; it is the one already built plus a
quadratic-rule pair and a second layer of transport.

The witness now asserts the prefix split, both self-similarity identities, and
that the quadratic rule is used exactly twice, at every `(a, b)` tested.

### The two quadratic steps, opened up — and `quadStep`

Last turn located the two quadratic steps and read off that everything else in
the `a ≤ b` chain is a loop pass or a far-commutation. This turn measures the
steps themselves and supplies the Lean lemma they need.

**Measured** (`computations/hecke_quad_pair_shape.py`, 36 occurrences over
`a = 2 … 7`, `b ∈ {a, a+1, a+3}`, none failing). Both occurrences apply the
**same** rule, `heckeRelation j₁`, after the **same** step,
`yangBaxterRelation j₁ (j₁+1)`; they differ only in their contexts:

    occurrence 1:  L              ++ [σ_{j₁}, σ_{j₁}] ++ descWord (j₁−1) j₂ ++ [σ_i]
    occurrence 2:  [σ_{i−2}] ++ L ++ [σ_{j₁}, σ_{j₁}] ++ descWord (j₁−1) j₂

    L = descWord (i−1) (j₁+2) ++ descWord i (j₁+3)
          ++ [σ_{j₁+1}, σ_{j₁+2}, σ_{j₁}, σ_{j₁+1}]

uniformly in `a`, `a = 2` included — both `descWord`s are empty there. Unlike
the prefix split, this family has no degenerate case, so no `Y`-vs-`B`
alternative is needed in the check.

A first guess at these contexts, written before the probe ran, was wrong at
**all 36** occurrences. The formulas are measured then asserted, not derived,
and the witness caveat says so — the same status as the split formulas, and the
same reason the check is per `(a, b)`.

**`quadStep`** (§4ah, `HeckeCompletion.lean`). `monicStep` asks for a monic
*two-word* rule, so a step is a substitution: one term in, one out. The
quadratic rule has *three* words, so `(a σ_z² b, c)` becomes the **pair**
`(a σ_z b, h·c)` and `(a b, c)`. `quadStep` is `monicStep`'s statement with that
output and the same proof shape — `ofTerms_coeff_mid` for the coefficient, then
`split_ifs <;> ring`. Built first try.

The contexts being *parameters* is what makes one lemma cover both occurrences:
the assembly supplies the one-letter difference and the step lemma never sees
it. It also subsumes the five hand-written quadratic steps of §4y, which exist
only because this lemma was missing.

Sorry-free, standard axioms (`propext, Classical.choice, Quot.sound` — same as
`monicStep`), `lean`-direct exit 0 on the full file with no warnings, and
checked non-vacuous by instantiating at rank 4 with a non-empty context at each
end and a bystander term.

**Scope.** This does **not** close the `a ≤ b` regime. It supplies the one
piece nothing in the development could reach. The Yang–Baxter half of each pair
is monic two-word, so `monicStep` already covers it — meaning item (1) of last
turn's list is now done at the step level.

**Next**, in order: the far-commutation blocks — `small(a)` in the prefix and
`block(a,b)` twice at top level — as nested transports over
`farComm_transport_left_sources`, an outer induction over levels with an inner
transport per level; then the assembly, which is the same `MultiStepReduction.trans`
wiring the `a > b` regime needed, over a longer list.

**Process note.** This arc's 29 commits had **no PR** — the branch
`claude/auq3-quad-left-family` was never opened for review, against the
ALWAYS-PR rule. (Recorded here first as "79 commits", which was wrong: that
came from `git rev-list origin/main..` in a **shallow** clone, where the
merge-base is unresolvable and the count is meaningless. Recomputed after
deepening: 29 arc commits, 36 with this session's, matching GitHub's count.
Worth remembering — a shallow clone silently returns plausible garbage from
any range query, and the first symptom here was a `git diff main...branch`
that failed outright with "no merge base".) Continued on `claude/prefix-self-similarity-fo9avn`, which
carries those commits plus this turn's, and opened
[#5247](https://github.com/litlfred/qou/pull/5247) over the whole arc. The
sibling branch is untouched.

### The far-commutation blocks — two corrections, and the transport lemma

`computations/hecke_block_transport_shape.py` + witness. The earlier conjecture
that the blocks are "a nested application of `farComm_transport_left_sources`"
is wrong twice over, and both corrections make the remaining work smaller.

**Correction 1 — the direction.** Within a level the *high* letter is fixed and
passes successively lower ones, so the shape is
`a ++ (x :: (w ++ b)) → a ++ (w ++ (x :: b))` — `farComm_transport_right`
(§4y), **not** `farComm_transport_left` (§4v). The two are mirrors and not
interchangeable.

Checked positionally rather than by restating rule names: a transport of one
letter across `k` others is `k` steps whose rewrite position advances by exactly
one, with the high letter at that position throughout, every letter passed at
least two below it, and the net effect the source → target shape. All four hold
for all **275** runs, over the whole chain rather than only the blocks.

**Correction 2 — the nesting.** "Nested double loop" describes the rule list
accurately but overstates the Lean. Over all 20 pairs `a = 2 … 6`,
`b = a … a+3`:

    b > a:  a levels;   level k passes min(b−a−1+k, b−a+2) letters
    b = a:  a−1 levels; level k passes min(k, 2)

so the number of **short** levels is fixed at two (one on the diagonal), and
every remaining level transports one letter past the *same* run
`descWord (j₁+1) j₂`. That is a fixed prologue plus a **uniform single-index
loop** — the shape §4af's loop already has — not a nested loop with a growing
inner run.

**`farComm_transport_right_sources`** (§4y). The blocks need the rightward
transport with the relaxed collision hypothesis, for the reason §4v needed it on
the left: the corner chain's bystanding term *is* the transport's final word, so
the unrestricted hypothesis is false exactly where the transport is wanted.

The end that relaxes is **not** the mirror image of the left one. On the left
the final word is the split `u = []`; on the right it is `v = []`, because the
moving letter starts at the left of `w` and finishes at its right, so the two
ends swap with the direction of travel. Mirroring `u ≠ []` verbatim would have
relaxed the *source* split and left the real obstruction in place.
`farComm_transport_right` is now a two-line corollary, so §4y's callers are
untouched. Sorry-free, standard axioms, `lean`-direct exit 0, no warnings, and
checked **strictly stronger** — an instance whose bystander is the transport's
final word, where `_sources` applies and `farComm_transport_right` provably
cannot.

**A probe bug worth remembering.** Runs must be grouped by *same-term
continuation*, not by high letter alone: an element becomes multi-term the
moment the quadratic rule fires, so adjacent chain steps can rewrite different
terms. Grouping without that test welded two unrelated `F(0,2)` steps — on words
of length 6 and 5 — into one bogus run and reported it as a structural failure.

**Still open, and now the whole of what remains.** The outer induction over the
levels, and then the assembly. The per-level lemma exists
(`farComm_transport_right_sources`), the level structure is measured, and the
quadratic steps are covered by `quadStep` — so the assembly is
`MultiStepReduction.trans` over: prefix loop passes, the two `Y·Q` pairs, the
two blocks, and the closing steps, with the `OverlapComposition` and its `spoly`
identity at the end. Same wiring the `a > b` regime needed, over a longer list.
No new *kind* of object is known to be missing; that claim is only as good as
the measurements above, which cover `a ≤ 7` and a sample of `b`.

### Landed — PR #5247 merged 2026-08-19

Rebase-merged, so the arc's commits sit on `main` individually (`895f5e07`
… `114abbb1`). Verified on `main` after the merge: `quadStep` and
`farComm_transport_right_sources` both present in `HeckeCompletion.lean`, and
both probes with their witnesses present under `computations/`.

The bean stays **in-progress**: the merge landed the *infrastructure* for the
`a ≤ b` regime, not the regime. `hecke_is_gs_basis` is untouched by this arc so
far.

**The next tranche, in order.**

1. **The outer induction over the block's levels.** Everything it needs exists:
   the per-level lemma is `farComm_transport_right_sources`, and the level
   structure is measured — `b > a` gives `a` levels with lengths
   `min(b−a−1+k, b−a+2)`, `b = a` gives `a−1` levels with `min(k, 2)`. Because
   the number of *short* levels is fixed (two, or one on the diagonal), this
   should be a fixed prologue plus a uniform single-index loop, i.e. the same
   kind of object as §4af's loop rather than a new one.
2. **The assembly.** `MultiStepReduction.trans` over: prefix loop passes, the
   two `Y·Q` pairs, the two blocks, the closing steps, then the
   `OverlapComposition` and its `spoly` identity. Same wiring the `a > b`
   regime needed, over a longer list.

**Two cautions for whoever picks this up.**

- The measurements behind (1) cover `a ≤ 7` and a *sample* of `b`. "No new kind
  of object is missing" is an inference from that sample, not a theorem — this
  arc has already had three structural guesses fail (the linear prefix fit, the
  quadratic-step contexts, the transport direction).
- Verify with `lean`-direct, never `lake build`, on a tree restored from
  `lake-cache/qou-<toolchain-slug>`: that branch carries Mathlib but **no UGB
  oleans**, so build the cone Elem → Basic → CompositionLemma → NormalForms →
  AlgOps → HeckeGS first (~30 s), then `HeckeCompletion` (~2 min).

### The block's uniform loop — `blockTransportRight` (§4ai)

Half of next-tranche item 1. Measured the per-level `(A, X, W, B)` decomposition
across the block, and the level-to-level transition is:

    B_{k−1} = [σ just moved] ++ B_k        (the moved letter joins B)
    W_{k−1} = one letter longer, until the cap; then fixed
    A_{k−1} = A_k shortened correspondingly

So in the **capped** region — every level after the fixed two (one on the
diagonal) — the run `W` is constant and each level peels one letter off the
right end of the remaining block and carries it across. That is exactly "carry a
whole word `X` rightwards past a whole word `W`", with no reference to the block
at all, which is what `blockTransportRight` states.

**Peeling direction is forced.** `X` must be peeled from the **right**: its last
letter sits against `W`, transports across, and joins `B`. From the left there
is no single transport to apply — the head of `X` is separated from `W` by the
rest of `X`. Hence `List.reverseRecOn` rather than ordinary list induction.

**Parked-term hypothesis.** Enumerating this induction's intermediates would
mean splitting `X` *and* `W` simultaneously, which is unusable. But every word
any step rewrites is `A ++ z`, so `loopTwoGen`'s single hypothesis — no parked
term begins with `A` — discharges every collision obligation at once. Same
device, same reason.

Built first try. Sorry-free, standard axioms, `lean`-direct exit 0 on the full
file with no warnings, and checked non-vacuous by carrying a two-letter block
past a two-letter run (four far-commutations) with a bystander that does not
begin with the context.

**Remaining, narrowed.** (a) The fixed prologue — two short levels off the
diagonal, one on it — as individual `farComm_transport_right_sources`
applications with explicit contexts, in the style of the `a > b` regime's
`s1`–`s4`. (b) The assembly. Note (a) is a *fixed* amount of work independent of
`a` and `b`, which is the whole point of the level-structure measurement.

### The block is CLOSED — `blockPass` (§4aj)

Next-tranche item 1 is done, and it went further than the plan: rather than
write the two short levels as named lemmas alongside `blockTransportRight`, the
whole block composes into one lemma.

**Blueprint, measured over 102 levels** (`a = 2 … 7`, `b = a … a+3`), uniform on
and off the diagonal — the diagonal differs only in *which* levels exist, not in
their shapes. Level with high letter `σ_h`:

    W = descWord (min(h−2, j₁+1)) j₂        the run it passes
    B = descWord (h−1) (j₁+1) ++ [σ_i]      what sits to its right

**So the block is three steps**, and the two short levels need **no new lemma** —
they are `farComm_transport_right_sources` applications, with the blueprint
supplying their arguments:

    h = j₁+1   transport across descWord (j₁−1) j₂
    h = j₁+2   transport across descWord j₁ j₂
    h ≥ j₁+3   one blockTransportRight, X = descWord i (j₁+3)

**The composition is forced by the left contexts.** With `A` the block
transport's context, the earlier steps must run at
`A₂ = A ++ descWord i (j₁+3) ++ [σ_{j₁+1}]` and `A₁ = A₂ ++ [σ_{j₁+2}, σ_{j₁}]`.
Then each step's target is the next one's source *on the nose*, because
`descWord j₁ j₂` and `descWord (j₁+1) j₂` peel exactly the letters those
contexts carry. Two `descWord_cons` peelings plus
`descWord (j₁+2) (j₁+1) = [σ_{j₁+2}, σ_{j₁+1}]` are the entire gluing — no
bridging lemmas, which is the payoff for the word definitions having been
chosen to match syntactically.

**One hypothesis dropped.** I first stated `blockPass` with `j₁+3 ≤ i`; the
linter flagged it unused and it genuinely is — if the bound fails,
`descWord i (j₁+3)` is empty and the middle step is vacuous, which is exactly
the degenerate short-block case. The lemma is more general without it.

Sorry-free, standard axioms, `lean`-direct exit 0 on the full file with zero
warnings. Checked non-vacuous by instantiating at a **real** block — the
`a = 4, b = 6` corner (rank 13, `i = 11`, `j₁ = 7`, `j₂ = 5`) — with a bystander
that does not begin with the context, so every index hypothesis is satisfied at
once rather than merely individually satisfiable.

**What is left is now only the assembly.** Every *kind* of step in the `a ≤ b`
chain now has its lemma: loop passes (§4af), the quadratic pairs (`quadStep` +
`monicStep` for the Yang–Baxter half), and the blocks (`blockPass`). Remaining is
`MultiStepReduction.trans` over the whole list plus the `OverlapComposition` and
its `spoly` identity — the same wiring the `a > b` regime needed, over a longer
list. Caveat unchanged: the blueprint is measured over `a ≤ 7` and a sample of
`b`, not proved, and this arc has had structural guesses fail before.

### The assembly is not only wiring — the chain cancels, twice

Started the assembly and found the arc's own description of it incomplete.
"`MultiStepReduction.trans` over a longer list" assumes a fixed-shape term list.
It is not fixed-shape.

**Measured** (`computations/hecke_chain_cancellation.py`, all 20 pairs
`a = 2 … 6`, `b = a … a+3`): the two quadratic steps each add a term, so the
element peaks at **four**; then **two** later steps remove two at once. No
rewrite can do that — a far-commutation takes one term to one term — so each is
a pair reconverging on a single word with opposite coefficients and
annihilating. At `a = 4, b = 6`, step 24 rewrites `h · (σ_i σ_{i−4} ⋯)` into
precisely the word already carried by `−h`, and both vanish.

**The second event is the FINAL step.** So the chain does not terminate by some
separate mechanism: reaching zero *is* a cancellation. The lemma is therefore
needed twice, and the second use is what will deliver "reduces to zero".

My first predicate asserted *one* cancellation and failed all 20 cases. Counting
the final collapse is the whole correction — the failure was mine, not the
chain's.

**`ofTerms_cancel_pair`** (§4ak) is the bridge. `MultiStepReduction` is stated
through `CoeffEq`, so the cancellation is **sound** with no help at all (§6
already carries the congruences); what was missing is the **shape** bridge,
without which every lemma downstream of a cancellation would have to be stated
against a list whose first two entries are dead weight.

Sorry-free, standard axioms, `lean`-direct exit 0 on the full file, zero
warnings, non-vacuous at the configuration the chain actually produces. One
note for whoever edits it: the `unnecessarySeqFocus` linter suggestion inside it
is **wrong** — `(simp only …; ring)` fails with "no goals to be solved" because
`simp only` already closes several `split_ifs` branches, and taking the
suggestion silently introduced `sorryAx` until `#print axioms` caught it. The
option is disabled for that declaration with the reason in a comment.

**Where the assembly stands.** The term-count profile is now known end to end:

    2 terms → (quad) 3 → (quad) 4 → (cancel) 2 → both blocks at 2 → (cancel) 0

so the multi-term phase is confined to the prefix, and **both blocks run on a
two-term element**, which `blockPass` already handles via its `L₁`/`L₂`
parameters. What remains is the prefix's own step-by-step composition — the
`a²+a+5` steps up to the first cancellation — and then the closing
`OverlapComposition` + `spoly` identity. Unchanged caveat: all of this is
measured over `a ≤ 7` and a sample of `b`, not proved.

### Two scope defects in the merged `blockPass` — found, fixed

Started the prefix, asked whether `small(a)` could reuse `blockPass`, and the
answer exposed two things wrong with what #5354 merged.

**1. The diagonal was excluded.** `blockPass` carried `hj₂ : j₂ ≤ j₁ − 1`, and
`b = a` gives `j₂ = j₁`, so it could not be instantiated on the diagonal *at
all*. But `a ≤ b` includes `b = a`, and the diagonal block is real — `a−1`
levels rather than `a`, starting one level higher, which is why it doesn't fit:
the first level is simply absent there. **So #5354's claim that the block is
"closed at general depth" was too strong** — it was closed for `b > a`.

**2. The trailing word was hardcoded.** Source and target both ended `++ [σ_i]`.
Right for the top-level block; wrong for `small(a)`, where what sits to the
right is `descWord j₁ j₂`.

**How the check nearly went wrong.** `small(a)` has the *same*
`(high, length)` level profile as a diagonal block — measured, identical at
every `a` from 3 to 6. That agreement is real and it is **not sufficient**: the
`W` words match exactly and the `B` words do not. Had I stopped at the profile I
would have asserted reuse that does not hold.

**The unified blueprint**, over 102 top-level levels and 56 `small(a)` levels:

    W = descWord (min(h−2, j₁+1)) j_eff        B = descWord (h−1) (j₁+1) ++ T

    top-level:  j_eff = j₂,  T = [σ_i]
    small(a):   j_eff = j₁,  T = descWord j₁ j₂

**The fix** handles both defects at once: `blockPassFromTwo` covers the second
level upward, asks only `j₂ ≤ j₁`, and takes `T` as a parameter — so it covers
the diagonal *and* `small(a)`. `blockPass` is now one leading transport plus it.
Freeing `T` is what turns the prefix's `block · two steps · block`
self-similarity into literal lemma reuse rather than an observation about
shapes.

Both sorry-free, standard axioms, `lean`-direct exit 0 on the full file, zero
warnings.

**Running count of structural descriptions in this arc that failed under
measurement: five.** The linear prefix fit; the quadratic-step contexts; the
transport direction; "the assembly is wiring"; and now "the block is closed at
general depth". Every one was caught by measuring rather than by reasoning from
the previous description. That is the working method for the rest of this arc,
not a run of bad luck.

### The prefix, read by term lineage — and it needs no new lemma kinds

`computations/hecke_prefix_phases.py` + witness. The prefix's step list resists
reading because the element is multi-term there and the engine interleaves the
terms by deg-lex, so consecutive chain steps often belong to *different* terms.
Tagging each step by term lineage makes it simple.

**Exactly two lineages act, running the same script, offset.** Measured over
`a = 3 … 6`, `b ∈ {a, a+1, a+2}` — 12 cases, none failing:

    A = [B₂₁, F₀₂, B₁₀] ++ (B minus its trailing [B₁₀⟨b⟩, B₂₁])
    B = for d = 1 … a−3:  one Bokut–Shiao step, then d far-commutations
        then one bare Bokut–Shiao step
        then Y_{j₁,j₁+1} Q_{j₁}, adjacent

`B`'s script is §4af's loop followed by the quadratic pair.

**The lengths corrected my own first phrasing.** "A is the head prepended to
B's script" is what the picture suggests, and it is wrong: `|A| = |B| + 1`, not
`|B| + 3`, because `B` ends with two steps `A` has no counterpart for. The check
now pins that exactly rather than comparing a common prefix — the weaker form
would have passed while leaving `B`'s last two steps unexamined.

**Consequence — the prefix introduces no new *kind* of step:**

    loop passes      §4af (loopTwo / loopTwoGen / blockStep)
    B and Y steps    monicStep          (§4x)
    Q steps          quadStep           (§4ah)
    small(a)         blockPassFromTwo   (§4aj — reachable only because T was freed)
    the cancellation ofTerms_cancel_pair (§4ak)

**That is an inventory result, not a schedule**, and the witness says so. The
pieces still have to compose on the nose across an interleaving of two
lineages. Given the arc's record — five structural descriptions falsified by
measurement, one of them about this same assembly — the composition should be
attempted and allowed to fail loudly, not assumed from the inventory.

**Remaining:** the prefix composition itself, then the `OverlapComposition` and
its `spoly` identity.

### `quadPair` (§4al) — the pair, and why it is a pair

The prefix uses the quadratic rule exactly twice, each time right after a
Yang–Baxter. One lemma covers both occurrences (they differ only in `L` and
`R`), but the mechanism is the part worth recording:

    L ++ [σ_{j₁+1}, σ_{j₁}, σ_{j₁+1}] ++ (σ_{j₁} :: R)
      Y →   L ++ [σ_{j₁}, σ_{j₁+1}] ++ [σ_{j₁}, σ_{j₁}] ++ R
      Q →   (L ++ [σ_{j₁}, σ_{j₁+1}, σ_{j₁}] ++ R,  c·h)
            (L ++ [σ_{j₁}, σ_{j₁+1}] ++ R,          c)

The Yang–Baxter step ends by emitting a `σ_{j₁}`; `R` already **begins** with
one. They land adjacent, and that adjacency *is* the quadratic redex — neither
step creates it alone. The original handoff was right to name the pair rather
than the quadratic step on its own.

**The Yang–Baxter step does not go through `yangBaxterRelation`.** That rule
carries `−1` at its own leading word, so it is not monic and `monicStep` cannot
take it. The route is `bokutShiaoRelation j₁ (j₁+1) j₁` — the same relation at
`j = i−1` (§4j), monic, leading word the right way round. `braid_hrel` /
`braid_hlm` are exactly that repackaging and already existed; finding them was
the whole difficulty.

Sorry-free, standard axioms, `lean`-direct exit 0, zero warnings, non-vacuous at
a **real** occurrence — the first quadratic pair of the `a = 4, b = 6` corner
(rank 13, `i = 11`, `j₁ = 7`) with the measured contexts.

**Inventory status.** Every piece of the prefix now has a lemma *by name*:

    loop passes      §4af (loopTwo / loopTwoGen / blockStep)
    B steps          monicStep           (§4x)
    the Y·Q pairs    quadPair            (§4al)
    small(a)         blockPassFromTwo    (§4aj)
    the cancellation ofTerms_cancel_pair (§4ak)

**Remaining: the composition itself**, then the `OverlapComposition` + `spoly`
identity. That is now the only unattempted piece of the `a ≤ b` regime — and it
is the one the arc has been wrong about before, so it should be attempted and
allowed to fail rather than scheduled from the inventory.

### First test of the inventory — `blockPass` does fit the chain

The prefix-phases result was an *inventory* ("every kind of step has a lemma"),
explicitly not a schedule. `computations/hecke_tail_assembly_fit.py` is the
first direct test of it.

It takes `blockPass`'s **actual Lean statement** — source and target, written in
the same `descWord` formulas the lemma uses — and asks whether they reproduce
the chain's measured block transition. `A` and `T` are **solved for** by
searching splits, and both source and target must come out right under the
**same** `(A, T)`. A lemma matching its source under one context and its target
under another would not compose; that is the failure this is built to catch.

**All 8 off-diagonal cases fit**, with clean contexts:

    A = descWord (i−1) (j₁+2)      [rel 1 … a−2]
    T = [σ_i]                      [rel 0]

`T` is exactly the tail `blockPass` originally hardcoded — a small vindication
of the earlier generalisation: freeing `T` did not disturb the top-level use, it
only added `small(a)`.

**What a pass means:** `blockPass` is *applicable* at the transition the engine
actually performs, with the contexts it actually has. That is genuinely more
than the inventory claimed.

**What it does not mean:** that the tail assembles. The `hpark` collision
hypotheses are properties of the *other* term and are untested here, and the
Lean chain may order its steps differently from the engine. Off-diagonal only —
`blockPass` does not cover `b = a`, so the diagonal needs its own fit check,
not yet written.

**Tail shape, measured** (`a = 4, b = 6`), for whoever assembles it:

    T_pre  −1·(1,2,0,1,3,2,4,3,5,6,0)   +1·(2,1,2,0,1,3,2,4,3,5,6)
    T_b1   −1·(1,2,3,4,5,6,0,1,2,3,0)   +1·(…unchanged…)     ← blockPass on term 1
    T_mid  +1·(2,1,2,0,1,3,2,4,3,5,6)   −1·(2,1,2,3,4,5,6,0,1,2,3)
    T_end  0 terms                       ← blockPass on term 2, then the pair cancels

So the tail is four applications: `blockPass`, two `monicStep`s, `blockPass`,
then `ofTerms_cancel_pair`. The second block drives term 2 onto term 1's word
with the opposite coefficient, and that is the final annihilation.

---

## The `a ≤ b` tail composes (2026-08-21, PR #5435, §4am)

The inventory's untested hypothesis, tested — and the answer changed the fix.

**`hpark` fails, and it is the engine's fault.** `blockPass` asks that no other
term be an extension of the block's left context. That is a property of the
*other* term, so no fit of a transition can see it — but the tail runs the block
twice, once per surviving term, so each application has the other as bystander.
Measured (`hecke_tail_collision_check.py`, 8/8 off-diagonal): `hpark` **holds at
block 1 and fails at block 2**, because block 2's *last step emits the
bystander* — that emission is the cancellation ending the chain. The bystander
is never a word either block *rewrites*.

**The reflex fix was wrong.** Since `SingleStepReduction` reads the redex
coefficient off the **source** side, a collision on a word only ever *produced*
costs nothing, so the apparent fix was to propagate down the source-only
relaxation `farComm_transport_right_sources` already carries. That is three
lemmas restated, plus an argument that a block's destination differs from each
of its own intermediate sources.

**None of it was needed — the schedule was.** The two blocks act on *different
terms*, so their steps commute and `MultiStepReduction` fixes no order beyond
each redex being present. Deg-lex runs block 1 first; that is the engine's
accident. Run block 2 first and its bystander is term 1 *pre*-block, which does
not extend `σ_{i−2} :: A`; by the time term 1 moves, term 2 begins `σ_{i−2}` and
does not extend `A`. `hecke_tail_reorder_check.py`: both `hpark`s hold, every
source unique, chain still reaches zero, 8/8.

**`tailChain` (§4am), sorry-free.** `blockPass` on term 2 → `blockPass` on
term 1 → two `bsStep`s. Ends at a pair differing only in sign — the `a > b`
regime's own ending (`chain` → `T6` → `T6_isZero`), so **`ofTerms_cancel_pair`
is not what finishes the tail** after all; it stays the right tool for the
*mid-prefix* cancellation, where the chain continues. The two terms meet by two
instances of `descWord_split`.

Also landed: `bsStep` (Bokut–Shiao at general depth in `monicStep`'s shape),
`bsWord₂_ne_bsWord₁`, `heckeGen_ne_of_val_ne`, and
`tailChain_indices_nonvacuous` (a = 4, b = 6 at n = 13 satisfies every index
hypothesis).

**Two corrections to my own work this tranche.** (1) The first collision check
reported the bystander was *not* the block's final word — a harder problem. That
was my bug: the chain ends at zero, so reading the post-block term set finds
nothing and the test went vacuous; asking the last step what it *emits* is the
fix. (2) I began re-deriving `descWord_split`, which the file already had; my
grep for it had been truncated by `head -40`, and the compiler caught it.

**Still open.** The **prefix** (`a² + a + 5` steps) is not assembled — only its
inventory is known, and this tranche is precisely a case of the inventory being
insufficient. Then the `OverlapComposition` + `spoly` identity joining the two.
The diagonal `b = a` runs `blockPassFromTwo` and is covered by *neither* the
collision nor the reorder measurement.

### Two follow-ons, same tranche

**The mid-prefix cancellation is forced — for a different reason than I gave.**
`hecke_prefix_schedule_check.py` simulates the chain in the **list** model Lean
actually uses (`ofTerms L`, every lemma reading its redex off
`L₁ ++ (W, c) :: L₂`, so `W` must occur exactly once) rather than the engine's
cleaned word→coefficient map. The two agree until the cancellation: the engine
drops the reconverged pair, the list keeps both entries. Measured:

- `dup_sources = 0` — no step ever rewrites a duplicated word, so the dead pair
  is inert **as a source** and could be carried on that count alone;
- **4** entries at `T_pre` against the **2** `tailChain` is stated on;
- **one** dead word extends a live term's block context — which is exactly what
  `hpark` forbids.

So `ofTerms_cancel_pair` is forced, and `hecke_chain_cancellation.py` gave the
wrong reason (a word being reduced twice; it never is) and the wrong count
(twice; it is once, the second cancellation being the sign-pair ending).
Consequence: **`tailChain` reaches the prefix's output only if the cancellation
is discharged before it.** Nothing new is needed — `Basic.lean` §6 already has
`SingleStepReduction.of_coeffEq_left` and `MultiStepReduction.congr_source`,
whose disjunctive conclusion `reducesToZero_congr` shows how to absorb.

**The diagonal.** `hecke_tail_diagonal_check.py` runs the fit, the collision and
the reorder at `a = b = 3..6` against `blockPassFromTwo`'s actual source and
target: fits both terms under a common `(A, T)`; `hpark` fails at the second
block under the engine's order and holds under the reordered one; reaches zero.
4/4. The two Bokut–Shiao steps and the endpoint are the **same** as the
off-diagonal's — measured. `tailChainFromTwo` (sorry-free) is that argument, and
its `j₂ ≤ j₁` covers the diagonal. Neither tail statement subsumes the other:
the hypotheses nest, the sources do not.

**Next.** The prefix assembly itself (`a² + a + 5` steps, two lineages, the
loop, the quadratic pair, `small(a)`), then `OverlapComposition` + `spoly`
joining it to the tail. The prefix's own per-step hypotheses have **not** been
swept — the clash above is measured only against the block contexts `tailChain`
would use.

### The prefix will be harder than the tail — measured, before writing its Lean

Every context hypothesis in the tail was discharged by **one letter**: no other
term shared the source's first letter, so "no other term extends this context"
followed from `List.cons.inj` whatever context the lemma picked. Free, and
lemma-independent. `hecke_prefix_head_separation.py` asks whether the prefix
affords the same, over `a = 3..5`, `b ∈ {a, a+1, a+2}`:

- **`4(a−1)` of the prefix's `a²+a+5` steps are NOT head-separated** — 8 of 17,
  12 of 25, 16 of 35. Roughly half.
- The shared prefix runs as deep as **`2a+1`**.
- Only **B** and **F** steps clash; the **Y** and **Q** steps of the quadratic
  pair never do.
- All three counts are **independent of `b`** — the clash structure is a
  function of the depth alone; the block length does not enter it.

**And scheduling does not repair it.** That is what repaired the tail, so it was
the first thing to try. Both lineage-grouped orders are legal and reach the same
endpoint; lineage-0-first clashes exactly as often as the engine's order, and
lineage-1-first is strictly worse (12/18/25 vs 8/12/16). **Scope (a)** — those
two groupings, alone, do not help; the space of legal orders is far larger than
three and nothing here excludes a better one.

**Refined — head separation was a proxy, and it overstated the difficulty.** The
real condition is closed-form. A left context `A` is necessarily a *prefix* of
the source (every lemma reads its source as `A ++ redex ++ tail`), so `hpark`
holds exactly when `lcp(source, r) < |A|` for every other term `r`; and `|A|`
reaches at most the redex offset. So a working context **exists iff
`redex_offset > max lcp`**. Against that:

- `2(a−2)` of the head-clashing steps are **rescued** — their redex sits past
  the shared prefix;
- the **hard core is `2a`** steps (6, 8, 10 at a = 3, 4, 5) where no choice of
  left context works;
- and the clashes are a **contiguous suffix** beginning at step `a²−3a+9`.

So the prefix splits cleanly: an **opening phase** of `a²−3a+9` steps that are
entirely head-separated and need no collision reasoning at all, then a
**closing phase** of `4(a−1)` where the lineages have converged enough to share
prefixes. That seam is the natural place to cut the assembly, and the opening
phase is the obvious next Lean target. All of it independent of `b`.

`context_fits` is optimistic — it asks whether a context exists at the *full*
redex offset, and a lemma may force a shorter `A` (`blockPass`'s stops where the
block begins). The `2a` figure is the robust one. The necessary condition is
separately clean (`dup_sources = 0` chain-wide).

### §4af's loop fits the opening phase (a ≥ 4)

The phase seam makes the opening phase the cheapest remaining Lean target — if
the lemma covering it fits. `hecke_prefix_loop_fit.py` does for `loopTwoGen`
what `hecke_tail_assembly_fit` did for `blockPass`: actual Lean source and
target, `A`/`S` solved by searching splits, `k`/`e` searched over the whole
range, every side condition enforced (`kd+1=k`, `ed+1=e`, `j₁≤ed`, `j₂≤e`,
`k≥e`, the `hD` decomposition of `descWord i j₁`, `hY` on the resulting `Y`),
and the predicted target required to occur in the chain.

**At `a ≥ 4`, both lineages fit** — B from its starting word, A from its word
after its own three-step head `[B21, F02, B10]`.

**`a = 3` has no loop pass at all** — its group structure is `[0]`, one bare
Bokut–Shiao step, zero far-commutations. `loopTwoGen` has nothing to fit there;
that opening phase needs its own treatment. My first version of the probe
counted this as a failure, and also tested starting words only, which made
lineage A miss by construction. Both were probe defects, not corpus facts.

A fit is applicability, not assembly: `loopTwoGen` carries a bystander `P` with
the same `∀ z, P ≠ A ++ z` shape as `hpark`, and fit and collision are separate
questions — the distinction the tail turned on.

**State of the `a ≤ b` regime**

| piece | status |
|---|---|
| tail, off-diagonal | `tailChain` — sorry-free |
| tail, diagonal | `tailChainFromTwo` — sorry-free |
| opening phase, `a ≥ 4` | lemma fits (measured); **not assembled** |
| opening phase, `a = 3` | no loop; needs its own treatment |
| closing phase (`4(a−1)` steps, hard core `2a`) | **open** — no schedule helps |
| mid-prefix cancellation | forced; `Basic.lean` §6 has the bridge |
| `OverlapComposition` + `spoly` | ~~open~~ **already in the corpus** — see below |

### Correction: the overlap and s-polynomial were never open

This arc carried "`OverlapComposition` + `spoly`" on its open list. Wrong, and
it is the failure the corpus-grep rule exists to catch. Neither
`CornerGeneral.oc` nor `oc_spoly_coeff` relates `j₁` to `j₂` — both ask only
`j₁ ≤ i₁` and `j₂ ≤ i₁`. So the overlap is constructible and its S-polynomial is
identified as `T0` for `j₂ ≤ j₁`, **diagonal included**.

Verified rather than read off the signature: instantiated `oc_spoly_coeff` at
`j₂ ≤ j₁` and at `j₂ = j₁`, `lean`-direct exit 0 on both. Separately measured
against the engine — the `a ≤ b` start element is exactly
`ofTerms [(V0, 1), (U0, −1)] = T0` at (a,b) = (3,4), (4,6) and the diagonal
(5,5).

**So the only regime-specific piece is the reduction chain from `T0` to zero.**
Recorded in `oc_spoly_coeff`'s docstring, where the next reader will be
standing.


### §4an — the opening was mostly already proved

Two `CornerGeneral` results carry the `a ≤ b` regime unchanged, both established
by **instantiation**, not by reading a signature:

- `oc` / `oc_spoly_coeff` never relate `j₁` to `j₂` → same `T0`, diagonal
  included.
- **`s1` and `s2` too.** They ask only `i₁+1 = i`, `i₂+1 = i₁`, `j₁ ≤ i₂`; Lean's
  unused-variable linter reports **`j₂` unused** when they are instantiated,
  which is the sharpest possible statement of it. They carry the chain to
  `ofTerms [(V2, 1), (U0, −1)]` — exactly where the engine's replay lands after
  two steps.

So the regime-specific part starts *later* than this arc assumed. `s3`/`s4` are
where it begins: they need `hed : ed+1 = j₂` with `j₁ ≤ ed`, i.e. `j₁ < j₂`, and
cannot be instantiated at `j₂ ≤ j₁` at all.

New namespace **`CornerLe`** with **`uHead`** (sorry-free): the *second* term's
head — the same two-rule motif as `s1`/`s2` (Bokut–Shiao then far-commutation)
displaced one letter right, because `U0` carries a leading `σᵢ₋₁` that `V0` does
not. The Bokut–Shiao redex straddles the two descending runs. Both collision
hypotheses fall to one letter: the bystander `V2` opens `σᵢ₋₂`, every word here
opens `σᵢ₋₁`.

**Revised state of the `a ≤ b` regime**

| piece | status |
|---|---|
| overlap + S-polynomial | already in the corpus, both depths |
| chain steps 1–2 (on `V0`) | `s1`/`s2` — already proved, `j₂`-independent |
| chain steps 3–4 (on `U0`) | `CornerLe.uHead` — sorry-free |
| tail, off-diagonal / diagonal | `tailChain` / `tailChainFromTwo` — sorry-free |
| middle of the opening phase, `a ≥ 4` | `loopTwoGen` fits (measured); not assembled |
| opening phase, `a = 3` | no loop; own treatment |
| closing phase — `4(a−1)` steps, hard core `2a` | needs the source-only relaxation; **not** an obstruction |
| mid-prefix cancellation | forced; `Basic.lean` §6 has the bridge |

### Correction: the `2a` hard core is a lemma-shape problem

I called it "the single genuine obstruction in this regime". That over-claims.

`hpark` is **sufficient, not necessary**. What a step actually needs is
`monicStep`'s `hne` — the *source* word absent from the rest of the list, so its
coefficient reads off `L₁ ++ (W, c) :: L₂`. A bundled lemma needs that at each of
its own intermediate sources, which is exactly the relaxation
`farComm_transport_right_sources` already carries one level down (it excludes
only the split naming the transport's final word).

**Measured: every source in the chain is unique, the `2a` hard-core steps
included** (9/9 per case, plus the chain-wide `dup_sources = 0`). So the precise
per-step condition holds everywhere, and the `2a` figure measures that
`blockTransportRight` / `blockPassFromTwo` / `blockPass` / `loopTwoGen` do not
propagate the relaxation — a known fix, not a wall.

**The symmetry worth keeping.** For the **tail**, scheduling made the relaxation
unnecessary, and I recorded that ("none of it was needed"). For the **closing
phase**, scheduling does not help — both lineage groupings measured no better or
worse — and the relaxation is the route. Same two options at each phase; the
answer differs.

So nothing in this regime is currently known to be blocked. What remains is
work: propagate the source-only hypothesis into the four bundled lemmas, then
assemble.

**First of the four is done (§4ai).** `blockTransportRightSources` narrows the
hypothesis to the family the transport actually rewrites —
`A ++ P ++ u ++ (x :: (v ++ (S ++ B)))` for `P ++ (x :: S) = X`, `u ++ v = W`,
`v ≠ []` — one per letter of `X` and per interior split of `W`. The recursion
threads it through: when `X` loses its last letter to `B`, a split of `X'`
becomes a split of `X` with `S` extended by that letter. `blockTransportRight`
keeps its exact signature and is now the one-line corollary, so `blockPass`,
`blockPassFromTwo` and both tail chains are untouched (`#print axioms` on all
six: no `sorryAx`). Proved first attempt — the claim that this was "a known fix"
is now tested rather than asserted.

Remaining to relax: `blockPassFromTwo`, `blockPass`, `loopTwoGen`.

---

## PR #5435 merged (`f2875e72`); relaxations complete on #5454

**All four bundled lemmas now have source-only forms**, each keeping its
original as a one-line corollary so no caller changed:

| lemma | § | note |
|---|---|---|
| `farComm_transport_right_sources` | 4ah | already existed — the template |
| `blockTransportRightSources` | 4ai | landed in #5435 |
| `blockPassFromTwoSources` | 4aj | two families, one per transport |
| `blockPassSources` | 4aj | three — those two plus the leading transport |
| `loopTwoGenSources` | 4af | two families **per level** |

`blockStep` needed nothing: its `hne` already names the redex and its `hcol`
already carries `u ≠ []`. The over-approximation lived entirely in
`loopTwoGen`.

**Why `loopTwoGen` went through unchanged despite being the one with real
induction structure.** Its accumulator only ever grows on the *right* of `A`, so
quantifying over that growth `D` makes the hypothesis closed under the recursion
for free — descending a level replaces `D` by `σ_kd :: D`, and the level's own
obligations are the `D = []` instances. No new argument was needed.

**One error, compiler-caught:** I first wrote the block transport's hypothesis
with `W` and `X` swapped, as though the run passed were `descWord i jppp` and
the block carried `descWord jp j₂`. It is the other way round, and the
conclusion `A ++ (X ++ (W ++ B)) → A ++ (W ++ (X ++ B))` says so. I had read the
call site rather than the conclusion.

**Next:** the opening-phase assembly (`a ≥ 4`, `loopTwoGen` measured to fit both
lineages), then `a = 3` (no loop pass — needs its own treatment), then the
closing phase, which now has every lemma it needs.

### Opening-phase coverage, measured (#5454)

`uHead` turned out to be **`loopTwoGen` at m = 0** — I hand-proved a lemma the
file had. Same reuse failure as `descWord_split`, but with a difference worth
keeping: there the *name* collided and the compiler stopped me; here nothing
collided, so nothing would have. It surfaced only because `uHead`'s target
looked like a `loopTwoGen` endpoint while setting up the opening phase.

**The consequence is the useful part.** If one level is `loopTwoGen` at m = 0,
the whole U-side loop is `loopTwoGen` at general **m = a − 4** — a single
application, not a chain. That also *explains* two earlier findings instead of
restating them: `a = 3` would need m = −1 (hence no loop pass), and `a = 4` is
m = 0 (hence `uHead`).

`hecke_opening_coverage.py`, 6/6 at a = 4..6:

| | a=4 | a=5 | a=6 |
|---|---|---|---|
| opening phase | 13 | 19 | 27 |
| `s1`/`s2` → V2 | 2 | 2 | 2 |
| `loopTwoGen` (k = i₁, e = jppp) | 2 | 5 | 9 |
| U-side steps after the loop | **3** | **3** | **3** |
| covered | 4 | 7 | 11 |
| left (the V-side loop) | 9 | 12 | 16 |

Those 3 trailing U-side steps are a bare Bokut–Shiao plus the Y-then-Q pair
that §4al's `quadPair` already covers — so the U side needs **one** named step
beyond loop + quadPair, not a family.

**Probe bug, recorded because it recurred:** the first version looked for the
loop's endpoint at the *end* of the contiguous U run, which continues past the
loop into those 3 steps. False negative in all six cases. Same wrong-index
shape as the tail's collision check — twice now.

**Next:** the V-side loop (9/12/16 steps), then the closing phase.

### Opening phase fully specified (#5454)

**All five stretches have named lemmas; none is new.**

| stretch | lemma | note |
|---|---|---|
| V0 → V2 | `s1`, `s2` | already proved, `j₂`-independent |
| U loop | `CornerLe.uLoop` | `loopTwoGen`, `A = [σ_{i−1}]`, `k = i₁`, `S = [σᵢ]`, **m = a−4** |
| U trio | `bsStep` + `quadPair` | `BS(jp, jpp, j₁)`, then `Y(j₁, jp)`, then `Q(j₁)` |
| V loop | `loopTwoGen` | `A = [σ_{i−2}]`, **k = i**, `S = []`, **m = a−3** |
| V trio | same as U trio | identified by rule, uniform in a and b |

`uLoop` landed; `uHead` is its `m = 0` case; the dead `U0₁` is gone.

**Scheduling constraint (new).** `loopTwoGen` is stated for a **two-term**
element; `quadPair` takes general `L₁`/`L₂` and tolerates any number. Under the
engine's order the U trio — whose quadratic step **splits U in two** — runs
*before* the V loop, so the V loop would face three terms and `loopTwoGen`
could not be applied at all. Measured: U splits at step 6/9/13, V loop completes
at 9/15/23. **Both loops must precede both trios**, which is legal because steps
on different terms commute.

That is the **third** time in this arc the engine's schedule proved an accident
rather than a constraint: the tail's two blocks, the closing phase (where
reordering did *not* help), and now the opening phase. Worth treating the
schedule as a free parameter by default and asking what the lemmas need.

**Two hypothesis lessons.** `uLoop` first asked `j₂ ≤ j₁` — the regime's fact —
when `loopTwoGen` needs only `j₂ ≤ jppp`; the strong form made `uHead`
un-instantiable. And the earlier fit search's two-letter V context was a
*different parse* of the same word, not the natural one (`A = [σ_{i−2}]`,
`k = i`).

**Next:** compose the five stretches into one `openingPhase` lemma under the
loops-first schedule. Then `a = 3` (no loop) and the closing phase.

### Opening phase CLOSED — `T0 →* TOpen`, sorry-free (#5454)

`CornerLe.openingPhase` proves the whole `a²−3a+9` opening for `a ≥ 4`, from
the S-polynomial to a four-term element. Five stretches, four lemma calls:

    s1, s2  →  uLoop  →  vLoop  →  trio (U)  →  trio (V)

Three things had to be built; all three turned out smaller than expected.

**1. `loopListSources` — the loop against an arbitrary term list.** `loopTwo`
and its descendants fixed `blockStep`'s list to `[(P, c')]` and `[]`, parking
the bystander in the FIRST slot. `blockStep` had taken general `L₁`/`L₂` all
along, so the restriction was in the *statement*, never in the mathematics.

It bites because `ofTerms` is a **representation, not a normal form** — the
same element with its terms in the other order is a different *value*. `uLoop`
runs `loopTwoGen` (parked first) and ends at `[(V2L, 1), (U0L, −1)]`; the V loop
has V active and U parked, so its source must list V first. Those two do not
compose syntactically.

I first tried a `CoeffEq` congruence (`MultiStepReduction.congr_target` beside
the existing `congr_source`). **Wrong tool, reverted.** `congr_source` returns a
*disjunction* because `refl` is a syntactic constructor and an empty chain
leaves only the source available; discharging the degenerate branch needs a
refutation of `CoeffEq` between the two words the loop exists to separate.
`loopTwoGenRightSources` — the same induction against the other slot — is both
smaller and exact.

**2. `vLoop`.** `V2` is already the loop's entry shape on the nose, so this is
`loopTwoGenRight` at `A = [σᵢ₋₂]`, `k = i`, `S = []`, `m = i − jppp` — one more
than `uLoop`'s. Measured: U and V take `2/5/9` and `3/6/10` steps at
`a = 4/5/6`, i.e. `V = U + 1`, 6/6. It went through first try.

**3. `trio` — ONE lemma, both lineages.** The six steps after `TL` are
`B(jp,jpp,j₁)`, `Y(j₁,jp)`, `Q(j₁)` twice, and the two occurrences differ only
in `A` and a trailing `T`:

| | `A` | `T` |
|---|---|---|
| U | `[σᵢ₋₁] ++ descWord i₂ jpp ++ descWord i jppp` | `[σᵢ]` |
| V | `[σᵢ₋₂] ++ descWord i₁ jpp ++ descWord i jppp` | `[]` |

`hj₂ : j₂ ≤ j₁` **is the regime** (`b ≥ a`) and is what makes `descWord jp j₂`
open `σ_jp, σ_j₁` — so `trio` does not instantiate in the `a > b` corner at all.
The diagonal `b = a` is included (`descWord jm j₂` empty).

#### What the new probe measured — `hecke_opening_trio_shape.py`, 7/7, 6/6

`hecke_opening_coverage.py` replays under deg-lex; `openingPhase` uses the other
(legal) order, so the continuation could not be read off that trace.

* **`TL` is reached exactly** — the element after the forced loops-first
  schedule is precisely `{V2L, U0L}`. Confirms no logic, but checks the Lean's
  *words* against the engine's, which sorry-freeness does not.
* **Term count `2,2,3,3,3,4`.** The QUADRATIC step splits, at the END of each
  trio. So the first trio runs at two terms and the second at three — both fine
  (`bsStep` and `quadPair` take general lists), and it confirms from the other
  side why the loops must come first: they are the only two-term-only lemmas.
* **Exactly 6 steps left after `TL`**, in all six cases. `opening = 2L + 9`.
* **After the trios: far-commutations** (`F(jpp,j₁)`, `F(jppp,jp)`) at four
  terms. That is where the next tranche starts.

#### Four errors this tranche, all mine, all the same two shapes

*A check that finds nothing reads as a measurement* (now **three** instances):

1. `importlib.util.spec_from_file_location` returns a **fresh** module, so
   loading the engine a second time left the probe reading an untuned (empty)
   rule table. No redex was ever found; every stretch measured 0 steps and the
   run reported `0/6` rather than erroring.
2. Then the *same bug* in my ad-hoc inspection script, one level up — the probe
   module loads its own copy of the sibling, so `cov.retune` there tuned a third
   instance. It made `TL` look unreachable when the probe had just proved it was.

*A structural claim not measured is usually wrong* (**two** more):

3. I derived the trio's words for the **V** lineage and tested them against the
   **first** trio, which is the **U** side's — deg-lex reaches `U0L` before
   `V2L`. Six clean `False`s rather than a near miss is what made it findable.
   `U_trio_runs_first` is now its own assertion.
4. `openingLoops`' docstring gave `L = jpp − j₁`. That is `2` for every `a` and
   agrees with the measured `2, 5, 9` only at `a = 4`. Right figure
   `L = (a²−3a)/2`; it is the loop's *level* `m = a−4` that is linear in `a`,
   not its step count. Corrected in place.

Plus three Lean metavariable failures with one cause worth naming: a bare
`have` has no expected type, so an implicit the hypotheses do not *determine*
stays open and the `by omega` beside it is asked to prove something about a
metavariable. Every index is now pinned by name at those call sites.

**Next:** the region after `TOpen` — far-commutations at four terms — then
`a = 3` (no loop pass: `m` would be −1) and the closing phase.

### Closing phase measured — and the `2a` core is NOT a wall (#5454)

`hecke_closing_from_topen.py`, 8/8 assertions, 6/6 cases. Measured from
`TOpen`, which is where the next lemma has to start.

**`TOpen` is exact** — the four-word element the Lean names, checked against
the engine word by word, not just by term count.

**One shape, uniform in `a` and `b`:**

    F-run (2a−3)  →  B(i₁,i,j₁)  →  B(i₂,i₁,j₁)  →  the SAME F-run  →  cancel

Machine-checked, not eyeballed: exactly two adjacent B steps, the two F-runs
literally equal, each `2a−3` long. The F-run is `F(i_{a−2}, j₁)` then
`F(x, jp), F(x, j₁)` for `x = i_{a−3} … i₁, i` — a far-commutation transport,
which §4u/§4v already carry in source-only form.

Term count 4 throughout, dropping to 2 on the last step: one cancellation,
`ofTerms_cancel_pair`. `2(2a−3) + 2 = 4(a−1)`, and **opening + closing = the
prefix exactly**, 6/6.

**The `2a` hard core: confirmed, and defused.** `hpark` — "no other term
extends this step's left context" — fails on exactly `2a` closing steps
(8/10/12 at `a = 4/5/6`), reproducing `hecke_prefix_head_separation.py`'s count
at the very steps it applies to. **It is not an obstruction.** Every lemma the
closing phase needs (`farComm_transport_*_sources`, `bsStep` via `monicStep`)
already takes the source-only hypothesis. That is what this arc's four
relaxations were for, and this is the measurement that says they suffice.

#### The fifth vacuous check

The source-uniqueness test in the first version was a **tautology**: the engine
keys the element by word, so no word can appear twice, and `not any(u == w for
u in gg if u is not w)` cannot be false. I wrote "dict keys are unique by
construction" in the comment beside it and did not draw the conclusion.

`monicStep`'s `hne` **cannot be measured in this model at all**. Its Lean-side
content is that the assembled LIST repeats no word — a property of the
assembly, under the prover's control, which `hecke_prefix_schedule_check.py`
measures directly (`dup_sources = 0`).

Also: the cancellation detector compared the term count against
`before + |image|`, but a far-commutation is a two-word rule and a quadratic a
three-word one, so the expected count differs per rule. It fired on step 1 of
every case and reported a 1-step closing phase.

**Pattern to watch, now with five instances:** a test whose subject is
determined by the *data structure* rather than by the mathematics. Ask what
would have to be true for the check to FAIL before trusting a pass.

**Next:** the closing phase in Lean — F-run transport, two `bsStep`s, the
F-run again, `ofTerms_cancel_pair`. Then `a = 3`.

#### The F-run sequences into three lemma calls, not `2a−3` steps

Traced at `a = 6` and checked across all six cases. The engine interleaves two
letters, but they can be sequenced, and the net effect is small:

    trioLeft ++ [σ_jp, σ_jpp, σ_j₁, σ_jp, σ_j₁] ++ T
      →  [σ_x] ++ descWord y jpp ++ [σ_jp, σ_j₁] ++ descWord i jppp
                                 ++ [σ_jpp, σ_jp, σ_j₁] ++ T

Step 0 is the bare far-commutation `F(jpp, j₁)`, which makes `σ_jp σ_j₁`
**adjacent**. The remaining `2(a−2)` steps then migrate that pair left through
`descWord i jppp`, one letter at a time, alternating. Since they are on one
term, the order is free, so:

* `σ_jp` transports fully left — every letter of `descWord i jppp` is
  `≥ jppp = jp + 2`, so all far-commute;
* then `σ_j₁` transports fully left — every letter is `≥ jppp = j₁ + 3`.

That is **one `monicStep` plus two `farComm_transport_left_sources`**, whose
hypothesis is source-only — which is exactly why the `2a` `hpark` failures do
not matter here.

For the U lineage the target has the closed form
`descWord i₁ j₁ ++ descWord i j₁ ++ T`; for V it does **not**, because V's left
context is `[σ_{i₂}] ++ descWord i₁ jpp`, which jumps from `i₂` to `i₁` and is
not a descending run. Do not state the lemma in the closed form — state it in
the `[σ_x] ++ descWord y jpp ++ …` form both lineages share.

**Measurement note.** Two wrong guesses on the way, both caught the same way.
First `T = [σᵢ]`, which is only right on the diagonal (`descWord jm j₂` is empty
there); off-diagonal it must be `descWord jm j₂ ++ [σᵢ]`, and the three
diagonal cases passing while the three off-diagonal ones failed is what named
it. Then I expected all four terms to have moved after `2a−3` steps — only
**one** has: the engine transports a single lineage word per F-run, which is
what the `F-run, B, B, F-run` shape says and I had not carried over.

**Next in Lean:** `fRun` (one `monicStep` + two transports), then the two
`bsStep`s, then `fRun` again, then `ofTerms_cancel_pair`. Then `a = 3`.

### `fRun` landed; the closing phase's remaining contexts measured

`CornerLe.fRun` is in (`bb64de7aaa`), sorry-free: `2a−3` engine steps as one
`monicStep` plus two `farComm_transport_left_sources`. Its hypotheses are in the
**source-only** form deliberately — see below.

**Why the `A`-prefix hypothesis is unavailable, confirmed at `TOpen`.**
`quadPair` splits a word into two differing only in an interior `σ_j₁`, so the
two terms of one lineage share their entire left context. Measured directly:
`U1` extends `Uh`'s `A`. That is the `2a` hard core, and it is why `fRun` takes
`monicStep`'s `hne` plus the two transports' split-indexed conditions rather
than "no other term extends `A`". This is the payoff of the four `_sources`
relaxations built earlier in this arc.

**The closing phase's full schedule** (traced at `a = 6`, `b = 7`; identical
shape on the diagonal):

| steps | what | on |
|---|---|---|
| `0 … 2a−4` | `fRun` | T0 |
| `2a−3` | `bsStep (i' := i₁) (i := i) (j := j₂)`, `a = descWord i₁ j₁`, `b = []` | T0 |
| `2a−2` | `bsStep (i' := i₂) (i := i₁) (j := j₁)`, `a = []`, `b = σ_i :: descWord i₁ j₂` | T0 |
| `2a−1 … 4a−5` | `fRun` again | T1 |
| `4a−5` | …its **last step cancels** against T0's word | — |

Contexts read off the trace, not derived. Note the index asymmetry, which is
invisible on the diagonal and is exactly the kind of thing this arc keeps
punishing: the **first** B step is at `j₂`, the **second** at `j₁`. On `b = a`
they coincide; at `b = a+1` the first redex is `bsWord₁ i j₂`, because
`descWord i j₁ ++ descWord jm j₂ = descWord i j₂`.

**Two of the four terms never move.** Only T0 and T1 are touched; the other two
are bystanders for the whole phase. That is what makes the source-only
hypotheses dischargeable — the bystanders are fixed words, so each obligation is
a word-inequality rather than a prefix claim.

**Inventory, not schedule.** Every piece the closing phase needs now exists:
`fRun`, `bsStep`, `fRun`, `ofTerms_cancel_pair`. **No new lemma *kind* is
missing** — but `hecke_prefix_phases.py` records five structural descriptions in
this arc that failed under measurement, including one about this very assembly,
so treat that as an inventory result. The pieces still have to compose on the
nose, and the cancellation has to land on the word `ofTerms_cancel_pair` expects.

**Next:** assemble the closing phase (`fRun`, two `bsStep`s, `fRun`,
`ofTerms_cancel_pair`) into `closingPhase`, then chain with `openingPhase` for
the whole prefix. Then `a = 3`.

### Every closing-phase piece now exists; the assembly's hard part is cheap

Landed this tranche, all sorry-free, `#print axioms` clean:

| lemma | what |
|---|---|
| `CornerLe.fRun` | the `2a−3`-step F-run as one `monicStep` + two `farComm_transport_left_sources` |
| `CornerLe.closingBs` | the two B steps — first at `j₂`, second at `j₁` |
| `ofTerms_cancel_split` | cancellation with terms in between; `ofTerms_cancel_pair` is its `M = []` case |

**The cancellation is not adjacent, and that is forced.** `trio` emits its
h-weighted word immediately before its plain one, in place, so `TOpen` reads
`[(Vh, h), (V1, 1), (Uh, −h), (U1, −1)]` and the two terms that reconverge are
the two h-weighted ones — with `(V1, 1)` between them. `ofTerms` is a
representation, not a normal form, so reordering the list is not available
either. Hence `ofTerms_cancel_split`. Cancelling the two h-terms leaves
`[(V1, 1), (U1, −1)]`, which is the measured 4 → 2 drop.

**The closing phase's endpoint is `closingBs`'s target, exactly.** Traced: T0's
`fRun` + `closingBs` lands on `bsWord₂ i₂ i₁ j₁ ++ (σ_i :: descWord i₁ j₂)`, and
T1's `fRun` lands on the *same word* — its target
`[σ_{i₂}] ++ descWord i₁ j₁ ++ descWord i j₂` is that word letter for letter.
So the cancellation needs no bridging lemma beyond the split one.

#### The source-only hypotheses discharge on two cheap facts

This was the part I expected to be hard, since one bystander shares the moving
term's entire left context (that *is* the `2a` core). Measured across all six
cases, **zero unresolved**:

* **two bystanders by first letter** — the V words open `σ_{i₂}`, the moving U
  word opens `σ_{i₁}`;
* **one bystander by length** — the other U term shares the prefix but is one
  letter shorter.

And the load-bearing detail: **every intermediate word of an F-run has the same
length** (measured as a singleton set in all six cases), because both the swap
and the two transports are length-preserving. So "length ≠ |U1|" is a *single*
fact that discharges every split at once, rather than a per-split argument. In
Lean that is `congrArg List.length` on the word equation, then
`simp [List.length_append]` and `omega`.

**Next:** assemble `closingPhase : TOpen →* [(V1, 1), (U1, −1)]` from the four
pieces, then chain with `openingPhase` for the whole prefix. Then `a = 3`.

### CORRECTION — "the assembly's hard part is cheap" was measured on ONE run

The previous entry reported **zero unresolved bystanders across all six cases**
and concluded the discharge is "head letter × 2, length × 1". That measurement
covered **F-run 1 only**. Completing it to F-run 2 gives `(1, 1, 1)` — one
bystander separated by head, one by length, and **one unresolved** in every
case.

**The unresolved one is `W*` itself** — the word F-run 2 is heading for, i.e.
the word the cancellation happens on. It shares the mover's head *and* its
length, because the transports are length-preserving and `W*` is where they
land.

**It is not an obstruction, and the file already anticipated it.**
`farComm_transport_left_sources` carries `u ≠ []` precisely to exclude the
transport's final word, and its docstring says so in as many words: *"In the
corner chain of §4af the bystanding term IS the final word, so the unrestricted
hypothesis is false exactly where the transport is needed."* Measured
`inSources = False`: `W*` is never the source of any step in the run, so neither
`hcol₁` nor `hcol₂` constrains it.

**What does remain is one interior-letter argument.** `fRun`'s `hne` — the
swap's `monicStep` obligation — compares the bystanders against the run's
*source*, and there `W*` is not excluded by anything. The two words share the
prefix `σ_{i₂} :: σ_{i₁} :: descWord i₂ jpp`; after it the mover continues
`descWord i jppp` (head `σ_i`) and `W*` continues `descWord jp j₁` (head
`σ_jp`), because `descWord i₂ j₁ = descWord i₂ jpp ++ descWord jp j₁`. So the
discriminator is `σ_jp ≠ σ_i`, after one peel. Measured uniform: the first
differing index is exactly `|A_V|` in all six cases.

**Corrected summary of the discharge:** head letter, or length, or — for `W*`
against the swap's source alone — one `descWord_split` peel then a head
comparison. Still bounded; not the two-fact story the previous entry told.

Sixth instance of the arc's recurring shape, in its subtlest form yet: not a
check that *could not* fail, but a check run over a **proper subset** of its
subject and reported as if complete. The tell was there — I wrote "F-run 1" in
the probe and then generalised in the prose.

### DEFECT in `closingU` as committed (4ac0cb67b6) — true, but not instantiable

`closingU` takes one packaged collision hypothesis:

    hV : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∃ t, r = σ_{i₂} :: t

and its commit message claims the length argument "lands at the caller". **That
is wrong.** At the intended call site the U run acts on `TOpen`'s *third* entry,
so `L₁ = [(Vh, h), (V1, 1)]` and `L₂ = [(U1, −1)]` — and `U1` is
`trioLeft i i₁ i₂ …`, which opens **`σ_{i₁}`**, not `σ_{i₂}`. `hV` is therefore
**false at the call site**, and `closingU` cannot be applied there at all.

The lemma is *true* — everything it proves, it proves — and `lean`-direct exit 0
plus a clean `#print axioms` say nothing about whether its hypothesis is
reachable. That is the whole point: **sorry-freeness does not check
instantiability.** This is the §3b-cond non-degeneracy concern in a different
costume, and the same failure the `uLoop`/`uHead` episode produced earlier in
this arc (a hypothesis made too strong, so the intended instance did not fit) —
second time this session.

**What it should be.** The five obligations split three ways, per the measured
discrimination:

* `Vh`, `V1` — open `σ_{i₂}`; one `List.cons.inj`.
* `U1` — opens `σ_{i₁}`, same lineage, split off by `quadPair`; separated by
  **length**. It differs from the run's words only in carrying
  `descWord jm j₂ ++ [σᵢ]` where they carry `σ_j₁ :: (descWord jm j₂ ++ [σᵢ])`.
* (V run only) `WStar` — same head *and* length; excluded from the transports by
  `u ≠ []`, and separated from the swap's source by one `descWord_split` peel.

So `closingU` should take the five hypotheses **raw**, in the shape `fRun` and
`closingBs` state them, and let `closingPhase` discharge each against the three
concrete bystanders with whichever of the three arguments applies. That matches
the file's `_sources` idiom and is the only form that instantiates.

A useful fact for that rewrite, worth recording: **every word in the entire
closing run has the same length.** Far-commutation is a two-word rule swapping
adjacent letters; Bokut–Shiao takes `descWord i j ++ [σᵢ]` to
`σ_{i−1} :: σᵢ :: descWord (i−1) j`, and `|descWord i j| = |descWord (i−1) j| + 1`,
so both are length-preserving. No length *formula* is needed anywhere — the same
`descWord`s appear on both sides and `omega` closes with their lengths opaque.

**Next:** restate `closingU` with raw hypotheses, then `closingV`, then
`closingPhase`. Then `a = 3`.

### THE WHOLE `a ≤ b` PREFIX IS PROVED — `prefixChain`, sorry-free

`CornerLe.prefixChain : T0 →* TCancel` covers all `a² + a + 5` steps of the
corner's `a ≤ b` prefix, from the S-polynomial to the first cancellation.
`a ≥ 4`, diagonal `b = a` included.

    openingPhase   a² − 3a + 9   s1, s2, uLoop, vLoop, trio, trio
    closingPhase   4(a − 1)      fRun, closingBs, fRun
                   -----------
                   a² + a + 5

Both counts close against the prefix length exactly, 6/6 at `a = 4,5,6`,
`b ∈ {a, a+1}`.

`TCancel_coeffEq` is the cancellation: the two `WStar` entries carry `h` and
`−h` and drop out, leaving `[(V1, 1), (U1, −1)]` — the measured 4 → 2 drop.

**All four final declarations went through first try.** That is not luck and is
worth recording as method: every endpoint had already been *forced* to match, by
the two bridge lemmas (`trio_out_eq_fRun_source`, `fRun_target_eq`) and by
stating each half against the same four-term list. `closingV_at_TOpen`'s source
IS `closingU_at_TOpen`'s target, syntactically — so `closingPhase` is one
`.trans` and `prefixChain` is another. The cost was paid earlier, in the six
iterations `closingV_at_TOpen` took.

#### What this arc actually cost, and where

Ten errors, all mine, in two shapes that recurred until they were named:

*A check that cannot fail, or covers less than it reports* — six instances,
ending with the bystander sweep run over one of two F-runs and written up as
complete. The tell each time: the probe's own variable names said what the prose
did not.

*A structural claim not measured is usually wrong* — four instances, including
`L = jpp − j₁` (right only at `a = 4`), a diagonal-only `T`, and testing
V-lineage words against the U trio.

Plus two of one Lean-specific trap: a **hypothesis made too strong for its
intended instance**. `uLoop`'s `j₂ ≤ j₁` broke `uHead`; `closingU`'s packaged
`hV` was outright unsatisfiable at its call site. The second is the important
one — **`lean`-direct exit 0 and a clean `#print axioms` say nothing about
whether a hypothesis is reachable.** The discipline that fixed it, and that
every later lemma used: *state the lemma and instantiate it at the real call
site in the same commit.*

**Remaining:** `a = 3` — loop parameter `m = −1`, no loop pass, the opening
phase's shape does not arise. Its own treatment, sharing nothing with the
general assembly. Stated in `prefixChain`'s docstring rather than left implicit.

### The small-`a` framing was wrong — `a = 3` is the same construction

Measured before touching Lean, and it revises what three probes have been
saying in their caveats.

**`a ∈ {1,2,3}` are all valid corners.** `oc` requires only `j₁ ≤ i₁`, i.e.
`a ≥ 1`. All of `a = 1,2,3` (at `b ∈ {a, a+1, a+2}`) reach **zero**. The caveat
*"a = 2 is excluded throughout this arc"*, carried verbatim in
`hecke_opening_coverage.py`, `hecke_opening_trio_shape.py` and
`hecke_closing_from_topen.py`, **records no reason** — and `a = 2` is a
perfectly good resolvable corner. Treat that caveat as unexplained, not as a
justification.

**`a = 3` fits the SAME phase decomposition**, 3/3:

| stretch | steps at `a = 3` |
|---|---|
| `s1`, `s2` | 2 |
| U loop | **0** |
| V loop | **1** |
| two trios | 6 |
| | `= 9 = a²−3a+9` |

plus `4(a−1) = 8` closing, total **17**, matching the measured first
cancellation at index 16. The U loop is 0 because at `a = 3`, `jpp = i₁`, so
`descWord i₂ jpp` is empty and **`U0L` and `U0` are the same word** — the loop
is the identity, not absent.

So `a = 3` is **not** a different construction needing its own treatment. It is
this one with `uLoop` replaced by `refl`. What blocked it was two hypotheses.

**One of them was never needed.** `vLoop` carried `htop : jppp ≤ i₁`, copied
from `uLoop`. `uLoop` genuinely needs it (its loop parameter is `m = i₁ − jppp`);
`vLoop`'s is `m = i − jppp`, so it only ever needed `jppp ≤ i`. Weakened:
`vLoop` compiled unchanged, and the only breakage was `openingLoops` passing its
own `htop`, now discharged by `omega`. **At `a = 3`, `jppp = i`** — so the
weakened form is satisfiable at exactly the case the arc called out of scope.

Third instance of the too-strong-hypothesis trap, and the first with a
consequence rather than a cosmetic one. The pattern across all three: a
hypothesis copied from a sibling lemma whose *parameter* differs.

**`a = 1` and `a = 2` are genuinely different.** `a² + a + 5` holds at `a = 2`
and `a = 3` but **not** at `a = 1` (measured 6 steps to first cancellation, not
7). Their rule sequences differ visibly from `a ≥ 3` — `a = 1` opens with two
quadratic steps, `a = 2` with `Y, F, Y, Q`. Separate cases; measure each before
assuming anything.

**Next:** `openingPhase₃` — the same five stretches with `refl` for the U loop —
then `prefixChain₃`. Then measure `a = 1` and `a = 2` properly.

### `a = 3` PROVED — `prefixChain₃`. And what `a = 1`, `a = 2` actually need

`prefixChain₃ : T0 →* TCancel`, all 17 steps, same `TCancel` and same five
stretches. **So the `a ≤ b` prefix is proved for `a ≥ 3`, diagonal included:**

    prefixChain    a ≥ 4
    prefixChain₃   a = 3

What unblocked it was one hypothesis that was never a bound. `fRun_target_eq`
asked `hy : jpp ≤ y`, used *only* to prove
`descWord y j₁ = descWord y jpp ++ [σ_jp, σ_j₁]`. `fRun_target_eq_of_left` takes
that identity as a **hypothesis**; `fRun_target_eq` is its `descWord_split`
supplier and keeps its signature. At `a = 3` the U lineage has `y = i₂` and
`jpp = i₁ > i₂`, so `descWord_split` does not apply — and the identity is still
true, because `descWord i₂ jpp` is empty and `jp = i₂`. **A different proof, not
a weaker bound, is exactly when a side condition should become a hypothesis.**
Fifth use of the `_sources` idiom here.

Two further splits were genuinely over-strong and are now routed through
`descWord i₁ j₁` instead of `descWord i₂ j₁` (`WStar_split`, `closingU.hAsplit`):
`[σᵢ₋₁] ++ descWord i₂ jpp` **is** `descWord i₁ jpp`, so the `i₂` bound was never
load-bearing. The whole closing chain now asks `jpp ≤ i₁` (true at `a = 3` with
equality) rather than `jppp ≤ i₁` (false there).

#### `a = 1` and `a = 2`, measured

| | `s1`,`s2` reach `V2`? | `U0L` reached? | `V2L` reached? |
|---|---|---|---|
| `a = 1` | **no** | no | no |
| `a = 2` | **yes** (2 steps) | **no** | yes, in **0** steps |

* **`a = 2` is PARTIALLY the same.** `s1` and `s2` do apply — the engine names
  the first step `Y(j₁,jp)` (Yang–Baxter) rather than a Bokut–Shiao step, but at
  `a = 2` we have `j₁ = i₂`, and `bokutShiaoRelation i₂ i₁ i₂` **is** the braid
  relation (§4j). `s1`'s hypothesis `j₁ ≤ i₂` holds with equality. The V loop is
  trivial: at `a = 2`, `jpp = i`, so `descWord i₁ jpp` is empty and
  **`V2L = V2`**.
  What fails is the **U** side: `U0L ≠ U0` there (they differ by one letter —
  `descWord i j₂` against `descWord i₁ j₂`), and the chain never produces `U0L`.
  So `U0L` is simply the wrong U-side target at `a = 2`; the U lineage goes
  somewhere else and needs its endpoint measured.
* **`a = 1` differs from step one** — `s1`,`s2` do not reach `V2` at all. It also
  does not satisfy `a² + a + 5` (measured 6 steps to first cancellation, not 7).
  Its own construction.

**The `a = 2` exclusion still has no recorded reason**, and this measurement
weakens the case for one: two of the five stretches transfer unchanged. Do not
carry that caveat forward as if it were justified.

**Next:** measure the U-side endpoint at `a = 2` (the only stretch that does not
transfer), then `a = 1` from scratch.

### `a = 2`'s U side is a different SCRIPT, not a different target word

Last entry guessed the `a = 2` case "may close with one new target word rather
than a new construction". **Measured, and that is wrong.**

Tracing the U lineage in isolation at `a = 2`, `b ∈ {2,3,4}`:

    a=2 b=2:  Y(j₁,jp)  Q(j₁)  F(i,j₁)  Y(jp,i)  Y(j₁,jp)
    a=2 b=3:  Y(j₁,jp)  Q(j₁)  F  F  F  Y(jp,i)  B(j₁,jp,j₂)
    a=2 b=4:  Y(j₁,jp)  Q(j₁)  F  F  F  F  F  Y(jp,i)  B(j₁,jp,j₂)

That is not `loop, trio`. The U side **opens with `quadPair`** — `Y(j₁,jp)` then
`Q(j₁)` — where the `a ≥ 3` construction opens with a loop and reaches
`quadPair` only inside the trio. Then a far-commutation transport of growing
length, then a Yang–Baxter and a Bokut–Shiao step.

Its endpoint is `bsWord₂ i₂ i₁ j₂ ++ [σᵢ, σᵢ₋₁]` (rel `[2,1] ++ descWord i₂ j₂
++ [0,1]`, uniform in `b`) — **not** `WStar`, which at `a = 2` would be
`bsWord₂ i₂ i₁ j₁ ++ (σᵢ :: descWord i₁ j₂)`, one letter longer. So neither the
target nor the route transfers.

**Revised scope for `a = 2`:** two of five stretches transfer unchanged (`s1`,
`s2`; and the V loop is trivial since `V2L = V2`). The U side and both trios do
not. It is a smaller job than `a = 1` but it is a construction, not a
substitution.

Why the U side differs is visible in the indices: at `a = 2`, `descWord i j₁` is
only three letters (`j₁ = i₂`), so `U0` carries a braid redex `[σ_jp, σ_j₁,
σ_jp]` from the start — the quadratic pair is *already present* rather than
being produced by a loop pass. The `a ≥ 3` construction spends its loop building
exactly that.

**Standing correction to three probes:** the caveat *"a = 2 is excluded
throughout this arc"* still records no reason, and now has a measured one — the
U-side script differs. Whoever next edits those probes should replace the bare
caveat with this.

---

## RETRACTION + `a = 2` PROVED (2026-08-23)

**The section immediately above is wrong and is retracted.** It reports the
`a = 2` U lineage's endpoint as `bsWord₂ i₂ i₁ j₂ ++ [σᵢ, σᵢ₋₁]`, concludes
that "neither the target nor the route transfers", and revises the scope to
"a construction, not a substitution". All three are wrong about the **prefix**.

The error: `hecke_small_a_decomposition.py` ran the U lineage to its **normal
form**. The prefix ends at the **first cancellation**, which is far earlier —
and the branch that measurement followed is *never touched* before the prefix
ends. It just sits there as a bystander, which is why the prefix's step count
is independent of `b` while that branch's length is not.

Re-measured to the first cancellation (9/9 assertions, 8 cases):

| | `a = 1` | `a = 2` | `a ≥ 3` |
|---|---|---|---|
| prefix steps | 6 | **11** | `a²+a+5` |
| matches `a²+a+5` | ✗ (7) | ✓ | ✓ |
| opening / closing | — | 7 / 4 ✓ | `a²−3a+9` / `4(a−1)` |
| cancellation word | `bsWord₂ i₁ i j₂` | **`WStar`** ✓ | `WStar` |
| source-only at every step | ✓ | ✓ | ✓ |

So `a = 2` obeys **every** general formula and lands on the **same word**. It is
a substitution after all, in three of five stretches.

`CornerLe.prefixChain₂` proves it — lean-direct exit 0, 0 sorries, `#print
axioms` clean on all six new declarations. What actually degenerates, all from
`j₁ = i₂` forcing `jp = i₁`, `jpp = i`:

* **U loop absent** (not the identity): `descWord i j₁` is three letters, so
  `U0` already carries `quadPair`'s redex and needs neither the loop nor the
  trio's `bsStep`. `uQuad₂` is `trio` minus its first step. At `a = 3` the loop
  is *present and is the identity* — the two small cases degenerate in
  **opposite** directions.
* **V loop trivial** (`descWord i₁ jpp` empty, `V2L = V2`).
* **both F-runs one step** (`descWord i jppp` empty) — hence `fRun_gen`, which
  takes the run as a parameter and the close-up as a hypothesis, leaving `fRun`
  as its `descWord_split` supplier so the `a ≥ 3` chain is untouched.

The V trio, `closingBs`, and the cancellation transfer unchanged. `closingBs`
transfers because its `hj₁ : j₁ ≤ i₂` holds with **equality** here.

**Why the trace's step 9 reads `Y` and not `B`.** Measured, not assumed: at
`j = i′` the Bokut–Shiao rule and Yang–Baxter share a leading word on 8/8 pairs
at `n = 9` and have the same relation on 0/8 — they differ by a **sign**, `Y`
carrying `−1` at its own leading word. The engine names whichever its rule
table reaches first; the Lean takes the monic Bokut–Shiao form, for the reason
§4al already gives for `quadPair`.

**Standing caveat, now discharged for `a = 2`.** The three sibling probes'
bare "a = 2 is excluded throughout this arc" is replaced with the measured
reason. All four Hecke GS probes now declare `q0Anchor: "independent"` with a
reason (verified: the whole import cone reads no q₀; the engine's only symbol
is a formal `sp.Symbol("h")`). Audit: `Q0_INDEPENDENT` 35 → 39,
`Q0_ANCHOR_MISSING` 1924 → 1922.

### Method note — the fourth instance in this arc

This is the **fourth** structural claim in this arc to reach a durable artifact
having been measured against the wrong question (after: V-lineage words tested
against the U trio; `L = jpp − j₁`; `T` hardcoded to `[σᵢ]`). The pattern is
not "insufficient measurement" — each had a measurement — it is a measurement
answering a *neighbouring* question. The probe now states its question in its
own docstring: **run to the first cancellation, not to a normal form.**

### `a = 1` — measured, open

6 steps, not 7. Schedule `QQYQBQ` for `b ≥ 2`, `QQYYQQ` on the diagonal
`b = 1`. Cancellation word `bsWord₂ i₁ i j₂` = `σᵢ₋₁ :: σᵢ :: descWord i₁ j₂`,
uniform in `b`. Nothing transfers: at `a = 1`, `j₁ = i₁`, so **both** `V0` and
`U0` carry a bare quadratic redex `σᵢ₋₁σᵢ₋₁` from the start and the chain opens
with two `Q` steps, one per term. Not yet proved.

### `a = 1` PROVED — the `a ≤ b` regime is complete (2026-08-23)

`prefixChain₁`: six steps, `T0` to the first cancellation. Unlike `a = 2`,
`a = 1` shares **neither** the count formula (6, not 7) **nor** the target
(`bsWord₂ i₁ i j₂`, not `WStar`) — the "measured, open" entry above is now
closed, and its measurement stands.

| | steps | target |
|---|---|---|
| `prefixChain`  | `a ≥ 4` | `a²+a+5` | `WStar` |
| `prefixChain₃` | `a = 3` | 17 | `WStar` |
| `prefixChain₂` | `a = 2` | 11 | `WStar` |
| `prefixChain₁` | `a = 1` | 6 | `bsWord₂ i₁ i j₂` |

`oc` requires only `j₁ ≤ i₁`, i.e. `a ≥ 1`, so **no uncovered corner is left in
this regime.** All four are lean-direct exit 0, 0 sorries, and `#print axioms`
clean.

Two things worth keeping from the `a = 1` proof:

* **Every word is written over `D = descWord i₂ j₂`,** which is *empty* on the
  diagonal `b = 1`. That is what makes the bystander arguments uniform in `b`:
  the words have lengths `|D|+2 … |D|+5`, and at the three places where two
  collide they differ in their first letter.
* **The chain's order is deliberately not deg-lex's, and that is load-bearing.**
  Deg-lex interleaves the lineages and at `b = 1` takes a U step before the V
  one; under that order the U word after its `bsStep` and the V word after its
  braid are both `|D|+4` long *and* agree in their first three letters, so
  separating them would need a case split on whether `D` is empty. Running the U
  lineage to its end first means the V words are only ever compared against
  words of a different length. `MultiStepReduction` fixes no order beyond each
  step's redex being present — deg-lex picks one, the Lean is not obliged to.

### The `a > b` corner — measured, and it is EASIER (2026-08-23)

I had written *"the `a > b` corner is a new construction, not an extension"*
into this PR's body and a scheduled follow-up note, inferred from `trio`'s
`hj₂ : j₂ ≤ j₁` not instantiating there. Sound inference, wrong emphasis, and
**unmeasured**. Measured (15 cases, `a ∈ 2..6`, `b ∈ 1..a−1`, 8/8 assertions,
[`hecke_agtb_corner_shape.py`](../computations/hecke_agtb_corner_shape.py)):

| | `a ≤ b` | `a > b` |
|---|---|---|
| S-polynomial | partial cancellation, 2 terms survive | **reduces to ZERO**, 15/15 |
| max terms | 4 | **2** |
| quadratic steps | 2 (one per trio) | **0**, 15/15 |
| step count | `a² + a + 5` | `b² + 3b + 5` — **no `a` dependence at all** |
| first cancellation | mid-chain | **is the end of the chain**, 15/15 |

`Q` is the only rule that splits one term into two, so with zero `Q`s the whole
4-term apparatus this arc built — `quadPair`, `trio`, `TOpen`,
`ofTerms_cancel_split` — is **unnecessary** in `a > b`. It is a 2-term
convergence over `monicStep` / `bsStep` / `farComm_transport_left_sources`
ending at the zero element. So: *"new construction"* was right about the route
and **wrong about the effort** — `a > b` is the easier half, and the hard half
is the one already done.

It also understates how related they are. Same two-run target shape, **bottoms
swapped**:

```
a ≤ b :  WStar = bsWord₂ i₂ i₁ j₁       ++ descWord i j₂
a > b :          bsWord₂ i₂ i₁ (j₂ − 1) ++ descWord i j₁
```

and both counts quadratic in `min(a,b)`: `m² + m + 5` for `m = a ≤ b`,
`m² + 3m + 5` for `m = b < a`. They differ by `2m`, so they do **not** meet on
the diagonal — the diagonal belongs to `a ≤ b`.

**Sixth instance of the arc's recurring error, caught by the probe rather than
shipped.** I first wrote the middle run as `descWord i₂ j₁`. That is right
exactly when `b = a−1` or `b = 1` — which is every case a quick eyeball lands
on. Extending the sweep to `a = 6` broke it and the assertion fired. The
formula is asserted in the probe rather than stated in prose *because* of this.

## The `a > b` corner (2026-08-23, PR #5539, §4ao)

Measured first, then proved. The shape, from `hecke_agtb_corner_shape.py` and
`hecke_agtb_lineage_schedule.py`:

- the S-polynomial **reduces completely to zero** — no residue, where `a ≤ b`
  ends its prefix at a *partial* cancellation with two survivors;
- the element **never exceeds two terms**, because the chain uses **no
  quadratic step**. `quadStep` is the only rule that splits a term, so
  `quadPair`, `trio`, `TOpen` and `ofTerms_cancel_split` — the whole four-term
  apparatus the other corner needed — are unnecessary here;
- step count `b² + 3b + 5`, with **no `a`-dependence**;
- meeting word `bsWord₂ i₂ i₁ (j₂ − 1) ++ descWord i j₁`.

**This retracts an unmeasured claim of mine.** I had written that `a > b` was
"a new construction, not an extension", inferred from `trio`'s `hj₂ : j₂ ≤ j₁`
not instantiating. The inference is sound; the conclusion about *effort* was
wrong. `a > b` is the easier half, and the hard half was already done.

### Both lineages are BLOCKS

Each lineage is a sequence of blocks: one Bokut–Shiao step, then a run of
far-commutations. **69/77 of those runs move a single letter past
contiguously-descending obstacles**, so the whole run is one
`farComm_transport_left_sources` call and a block costs **two lemma
applications** however long its run — `b² + 3b + 5` steps but `O(b)` lemma
calls. `gtBlock` packages exactly that pair.

Per lineage: `b` blocks with an F-run, and on the second lineage **two**
trailing B-only steps. (I first wrote `b + 1` blocks in a check-in note; that
was the index *range* end read back as a count, corrected in the probe.)

The first lineage's opening is **`b`-independent** — `vOpen`, five steps with
an arbitrary trailing context `S` carried inert, where `b = 1` is `S = []`.
The second lineage's opening is **not**, which the probe measures rather than
assumes.

### Proved

| | |
|---|---|
| `sPolyChain_gt₁` | `b = 1`, 9 steps → `(W, 1), (W, −1)` |
| `sPoly_zero_gt₁` | → 0 |
| `sPolyChain_gt₂` | `b = 2`, 15 steps → `(W, 1), (W, −1)` |
| `sPoly_zero_gt₂` | → 0 |

`b = 2` is `vOpen` at `S = [σᵢ₋₂]` — its first call with a **non-empty**
trailing context, which is what the parameter was stated for — then one
`gtBlock`; and on the second lineage two `gtBlock`s at runs of one and two
letters, then two bare `bsStep`s. Same two lemmas throughout; only the
arguments change. Both new lemmas are now instantiated at a second real call
site, per the rule that a lemma is not established until its hypotheses are
shown reachable.

All sorry-free; `#print axioms` on each: `propext`, `Classical.choice`,
`Quot.sound`.

### `a = b + 1` is not an exception for the Lean

The probe records the eight `a = b + 1` cases as exceptions because deg-lex
interleaves the last block's two moved letters differently there.
`MultiStepReduction` does not require deg-lex order — only that each step is
applicable — so `sPolyChain_gt₂`'s hypothesis is `j₁ ≤ i₃`, i.e. `a ≥ 3`
**with equality allowed**, and it covers `a = 3` as well. The exception is in
the engine's schedule, not in the mathematics.

### CLOSED — `gtRun`, and the chain at every `b`

The induction landed the same session. `sPolyChain_gt` proves the corner for
every `b ≥ 2`; with `sPolyChain_gt₁` that is the **whole `a > b` half**, and
both resolve to zero.

| | |
|---|---|
| `gtRun` | the induction — `gtBlock` iterated over a run of any length |
| `sPolyChain_gt` | `b ≥ 2`, any `a > b` → `(W, 1), (W, −1)` |
| `sPoly_zero_gt` | → 0 |

The whole chain is **four lemma applications regardless of `b`** — `vOpen` +
`gtRun` on the first lineage, `gtRun` + two `bsStep`s on the second — where the
step count is `b² + 3b + 5`. That is the measured block decomposition turned
into Lean.

Two design points, both bought by proving `b = 1` and `b = 2` concretely first:

- **`z` and `j₂'` are parameters with `+1 =` hypotheses, not constructed.**
  That is the file's idiom (`descWord_cons_le` takes its `i'` the same way).
  The one place a `Fin n` predecessor must be *built* is the recursive call's
  `z − 1`.
- **The split `w ++ descWord y j₁ = descWord i j₁` is a hypothesis, not a
  computation.** Stating `w` as `descWord i (y+1)` instead would have forced a
  `Fin n` **successor** at every level; carrying the split forces none. This
  was the obstacle identified below, and carrying the split is what dissolved
  it.

`b = 1` is not covered by the general theorem and cannot be: there the first
lineage's run `descWord i₂ j₂` is **empty** (`j₂ = i₁ > i₂`), so `vOpen`
already lands on the meeting word and `gtRun`, whose run has `k + 1 ≥ 1`
letters, has nothing to do.

### How the induction was found

The block, in `descWord`-relative form, is the induction step:

```
A ++ (descWord i j₁ ++ (σ_y :: T))   →*   (A ++ [σ_{y−1}]) ++ (descWord i j₁ ++ T)
```

— each block pulls the leading letter of the trailing run across
`descWord i j₁`, demoting it by one and depositing it on the left. Both
lineages are that same move: the whole trailing descending run slides down by
one and jumps to the left of `descWord i j₁`. Verified against the exact words
at `b = 2` and `b = 3`.

The obstacle looked like `Fin n` predecessor arithmetic — the deposited
letters are `y−1, y−2, …`. It was not: passing the predecessors as parameters
with `+1 =` hypotheses, and carrying the split rather than computing `w`,
removes every construction but one. `b = 2` was proved concretely first,
deliberately, to check that `gtBlock` composes at a longer run before
committing to a design for the induction — and that is what made the right
statement visible.

## The `a ≤ b` prefix and tail are JOINED (2026-08-23, PR #5586, §4ap)

`sPoly_le_resolves` (`a ≥ 4`) and `sPoly_le_resolves₃` (`a = 3`): the `a ≤ b`
S-polynomial reduces to an element that is coefficientwise **zero**, for every
`b ≥ a`, the diagonal included. With `sPoly_gt_resolves` (#5539) that is the
whole Bokut–Shiao corner except `a = 1, 2`.

Every piece was already on `main`. What was missing was the join, and **the join
is not a `trans`**:

```
prefixChain      T0 →* TCancel                 (4 terms, two a cancelling WStar pair)
TCancel_coeffEq  CoeffEq TCancel (2-term pair)
tailChain        2-term pair →* sign-pair
```

The middle arrow is a `CoeffEq`, and `MultiStepReduction` is stated on
**representations** — `ofTerms` is a representation, never a normal form. So
`TCancel` and `tailPair` are the same element and different objects.
`MultiStepReduction.congr_source` is the way through; its conclusion is a
disjunction, forced by `refl` being a syntactic constructor. Both branches give
the same thing, so the join costs only naming them. That `Basic.lean` §6
machinery was written for exactly this and had **no consumer until now**.

**The case split is on the diagonal, not on `a`.** `tailChain` runs off it,
`tailChainFromTwo` on it; their targets are literally the same expression, so
only the sources needed reconciling. At `j₂ = j₁`, `descWord jm j₂` is empty
while `descWord j₁ j₂` is one letter, so `tailChainFromTwo`'s trailing `σ_jp` —
which sits *after* its run where `tailPair`'s sits *before* — lands in the same
place. Off the diagonal the two words genuinely differ. That is the recorded
"neither tail statement subsumes the other", now used rather than noted.

**`a = 3` forced a hypothesis correction.** `tailFromCancel` takes `jpp ≤ i₁`
**directly**, not `htop : jppp ≤ i₁`. At `a = 3`, `jpp = i₁` so `jppp = i₁ + 1`
and `htop` is **false**. Stating the tail on `htop` — which reads naturally,
since it is what `prefixChain` carries — would have made `sPoly_le_resolves₃`
unprovable for precisely the case it exists to cover. Compiler-caught, along
with an invented `hleft` hypothesis that is `closingPhase₃`'s parameter, not
`prefixChain₃`'s.

Also dropped: an `hq : q − q⁻¹ ≠ 0` I had put on `sPoly_le_resolves`. The
cancellation is `h` against `−h` whatever `h` is, so it was never needed —
the unused-variable linter caught it. Same failure mode as `closingU`'s
unsatisfiable packaged hypothesis, one step milder.

### `a = 1` and `a = 2` do NOT transfer — measured, not assumed

Checked concretely rather than left as "unmeasured", since assuming a transfer
is what this arc has repeatedly paid for:

- **`a = 2`.** `TCancel₂_coeffEq` *does* leave a two-term pair, and its **first**
  word is exactly `tailPair`'s: at `a = 2`, `jp = i₁` and `jpp = i`, so
  `trioLeft i i₂ i₁ jpp jppp` collapses to `[σᵢ₋₂]` and the rest lines up. Its
  **second** does not. `tailPair`'s second word carries a leading `σᵢ₋₁` that
  `TCancel₂`'s lacks, because the peel `descWord i₁ jpp = σᵢ₋₁ :: descWord i₂ jpp`
  needs `jpp ≤ i₁` — and at `a = 2`, `jpp = i`. The same bound is `hjppid` in
  both tail statements, so neither applies as stated.
- **`a = 1`.** `TCancel₁_coeffEq` leaves **four** terms, with coefficients
  `h, 1, −h, −1`. It does not reach a two-term pair at all, so there is nothing
  for a tail stated on a pair to consume.

So both small cases need their own tail argument. Neither is a rewrite of this
one, and the obstruction in each is a specific index bound rather than effort.

## The corner meets the criterion (2026-08-24, §4as)

`CornerCriterion.bsbs_overlap_resolves`: every Bokut–Shiao × Bokut–Shiao
overlap at top `i − 1` satisfies the criterion's obligation,
`∃ nf, ReducesToNF … oc.spoly nf ∧ nf.isZero` — for every pair of depths with
`j₁ ≥ 1`.

**Correction to this bean's own open list.** It carried "`OverlapComposition` +
`spoly` joining the two" as remaining work. That was **wrong, and the corpus
already said so**: `CornerGeneral.oc` and `oc_spoly_coeff` have been in the file
throughout, and the latter's docstring records the same correction in as many
words — *"both were in the corpus, generic in both depths, the whole time"*. I
repeated the stale item from this list instead of grepping, which is exactly
what the corpus-grep discipline exists to prevent. The item is struck.

What was genuinely missing was narrower: `CornerGeneral.resolves` existed but
only for `a > b` with `b ≥ 2` (its `hed`/`hj₁`/`hj₂` pin that regime). The five
`sPoly_*_resolves` theorems now cover every regime, so what remained was the
**case analysis** — which theorem applies at which depth, and the `Fin n`
witnesses each needs.

Three pieces do the joining and all three were already present:
`oc_spoly_coeff` (regime-independent — it relates neither depth to the other),
`reducesToZero_congr` (carries the obligation across that `CoeffEq`), and
`isNormalForm_of_isZero`. `resolves_of_T0` packages them; the case split is the
only new content.

| depth | theorem |
|---|---|
| `j₁ < j₂` | `sPoly_gt_resolves` |
| `j₂ ≤ j₁`, `j₁ = i₁` | `sPoly_le_resolves₁` |
| `j₂ ≤ j₁`, `j₁ + 1 = i₁` | `sPoly_le_resolves₂` |
| `j₂ ≤ j₁`, `j₁ + 2 = i₁` | `sPoly_le_resolves₃` |
| `j₂ ≤ j₁`, `j₁ + 3 ≤ i₁` | `sPoly_le_resolves` |

### The gap, stated rather than hidden

`jm` is a **hypothesis**, not a construction, because it is `j₁ − 1` and does
not always exist. The `a ≥ 2` branches need it. So `j₁ = 0` is **not covered**,
and since `j₂ ≤ j₁` forces `j₂ = 0` there, the uncovered set is exactly the
deep diagonal `j₁ = j₂ = 0`.

It is not degenerate and there is no shortcut: `OverlapComposition.spoly_isZero_of_self`
needs `left = []`, and this `oc`'s `left` is `descWord i j₁`, which is non-empty
whenever `j₁ ≤ i₁ < i`. So that case needs a chain of its own, or a
generalisation of one of the `a ≥ 2` tails that does not reference `jm`.

`hq : q − q⁻¹ ≠ 0` is needed only by the `a = 1` branch, where the first term
carries coefficient `h` and a `SingleStepReduction` needs it nonzero to
transport.

### Still open, after this

- the deep diagonal `j₁ = j₂ = 0` above;
- this is **one** composition family. `IsGrobnerShirshovBasis` quantifies over
  *every* `oc` and every `ic` in the system. The other families
  (`ybBs`, `bsYb`, `quadSelf`, the far-commutation pairs) have their own
  `_resolves` lemmas in the file; assembling all of them into the structure
  itself is a separate tranche and is **not** claimed here.

## Rule-level membership inversion (2026-08-24, §4at)

`mem_heckeRewritingSystem_rules` (3 families) and
`mem_heckeCompletedRewritingSystem_rules` (4) invert `r ∈ rules` to the **rule**:
`r = bokutShiaoRelation i' i j`, with that family's side condition.

**Correction to my own measurement, made in this session.** I told the user that
nothing in the corpus inverts membership — that only the constructive `_mem`
direction existed. Wrong. `heckeRewritingSystem_lm_cases` (§4b) and
`heckeCompletedRewritingSystem_lm_cases` (§4i) are both inversions and have been
there throughout; I grepped `mem_rules|rules_mem|classify`, missed, and drew a
conclusion from the miss rather than reading the section headers that say so.

The accurate claim is narrower, and it is the reason this section exists. Both
existing inversions stop at the **leading monomial**. `OverlapComposition.spoly`
is computed from `rule.relation` and `rule.lc`, so lm-level cannot reach it — and
in the completed system the lm does not even determine the rule, because §4j's
`bokutShiao_lm_eq_yangBaxter_lm` puts `bokutShiaoRelation i' i i'` and
`yangBaxterRelation i' i` on one word. The criterion's `overlap_resolves`
quantifies over `oc` with both rules in `rules`, so it is exactly a statement
that needs the rule-level form.

Both `lm_cases` are re-proved through the new lemmas (the completed one: 15 proof
lines → 7) with their statements unchanged, so the lm-level classification is now
a corollary rather than a parallel proof of the same `flatMap`/`filterMap`
destructuring. Every existing consumer — `_lm_ne_nil`, §4e's irreducibility
machinery — is untouched.

### What this does NOT do

It does not discharge `overlap_resolves`. Two pieces still stand between:

1. **The shape bridge.** `bsbs_overlap_resolves` is stated for the *constructed*
   `CornerGeneral.oc i i₁ j₁ j₂ …`; the criterion quantifies over an *arbitrary*
   `oc`. Going from one to the other means recovering `left` / `overlap` /
   `right` from `lm₁_decomp : bsWord₁ i₁ j₁ = left ++ overlap` and
   `lm₂_decomp : bsWord₁ i₂ j₂ = overlap ++ right` — i.e. enumerating which
   splittings of two Bokut–Shiao words are possible. §4k *counts* these (58
   shapes at `n = 4`, 45 with both contexts non-empty) but does not carry them in
   general.
2. **The other fifteen rule-kind pairs**, plus every `ic`. Rule-level inversion
   turns `overlap_resolves` into a 4×4 case split; only the BS×BS cell has its
   corner closed, and only for `j₁ ≥ 1`.

Verified lean-direct: HeckeGS exit 0 (4 s), HeckeCompletion exit 0 (100 s), 0
errors and 0 warnings on both. `#print axioms` on both new declarations, both
re-proved `lm_cases`, `_lm_ne_nil` and `bsbs_overlap_resolves`: propext,
Classical.choice, Quot.sound only. PR #5626.

## The overlap of a proper composition is one letter (2026-08-24, §4au)

**The inventory that reframed the remaining work.** Reading the ~20 composition
namespaces in `HeckeCompletion.lean`, they are indexed by the **shape** of the
composition, not by the kinds of the two rules — and several take a *generic*
rule in one or both slots, so they already cover whole rows and columns of the
rule-kind table:

| namespace | rule₁ | rule₂ | `overlap` | gated on |
|---|---|---|---|---|
| `CyclicQuad` | `r` | `heckeRelation x` | `[σₓ]` | `r.lm = u' ++ [σₓ]` |
| `CyclicQuadLeft` | `heckeRelation x` | `r` | `[σₓ]` | `r.lm = σₓ :: u''` |
| `BraidSelfOverlap` | `r₁` | `r₂` | `[σᵢ]` | both on `wHi i' i` |
| `FarCommCyclic` | `farCommRelation x m` | `r` | `[σ_m]` | `r.lm = σ_m :: u''` |
| `CyclicFarCommLow` | `r` | `farCommRelation i j₀` | `[σᵢ]` | `r.lm = (σᵢ :: D') ++ [σᵢ]` |
| `BokutShiaoBraid` | BS | `r₂` | `[σᵢ]` | `r₂.lm = wHi i' i` |
| `BraidBokutShiao` | `r₁` | BS | `[σᵢ]` | `r₁.lm = wHi i' i` |
| `BokutShiaoFarComm`, `CornerGeneral` + 5 corner namespaces | | | `[σᵢ]` | |

**Every one fixes `overlap` to one letter.** So the gap between this machinery
and the criterion's `∀ oc` is exactly the multi-letter overlaps — a much
narrower thing than "the other fifteen rule-kind pairs", which is how §4at
framed it.

**Measured** ([`hecke_overlap_length_probe.py`](../computations/hecke_overlap_length_probe.py),
PR #5627): at `n = 2 … 8`, **1351** compositions with both contexts non-empty,
overlap-length histogram `len1` only, zero exceptions. The same probe reproduces
§4k's shape counts independently — 16 rules → 13 distinct lms → 58 shapes = 45
proper + 13 degenerate at `n = 4`.

**Proved** (PR #5629): the invariant is that every rule's leading monomial begins
with its largest letter (`lm_head_is_max`, off the *leading-monomial* inversion —
the one §4at said `spoly` cannot use, which is the right tool here because this
claim is about leading monomials). Then `overlap_length_one_of_bs_left`: the
overlap's head is `lm₂`'s head so it dominates the overlap; the overlap is a
suffix of `lm₁` so once longer than one letter its head is strictly inside the
descending run, capped at `i − 1` by `descWord_index_le`; and the trailing `σᵢ`
is in the overlap either way.

### ~~Not proved~~ — closed the same day

The three remaining `rule₁` shapes are now proved too: `overlap_length_one`
covers all four. Quadratic and far-commutation are a pure length bound (lm of
length 2, so one letter of left context leaves exactly one); Yang–Baxter has one
escape — a two-letter overlap `[σᵢ, σⱼ]` — which puts `σⱼ` behind `σᵢ` at the
head of `lm₂`, forbidden by `lm_head_is_max` since `j = i + 1`.

**The Lean is stronger than the probe here.** `overlap_length_one` assumes
`oc.left ≠ []` **alone**; the probe measured only the *proper* compositions,
where the right context is non-empty too. So the theorem also covers
`left ≠ [], right = []`, which the enumeration never looked at.

### The remaining chain to `overlap_resolves`, as it now stands

1. **Rule-level inversion** — done, §4at.
2. **Single-letter overlap** — measured for all four shapes, proved for BS.
3. **The shape bridge** — from an arbitrary `oc` to the constructed
   `CornerGeneral.oc`, i.e. recovering `left`/`right` once `overlap` is known to
   be `[σᵢ]`. Step 2 is what makes this tractable: with a one-letter overlap the
   two `lm_decomp`s determine `left` and `right` outright.
4. **The other cells**, and every `ic`.
5. The deep diagonal `j₁ = j₂ = 0`, still open from §4as.

## The shape bridge (2026-08-24, §4av) — the criterion's own form, reached

`bsbs_resolves_of_oc`: the §4as result for an **arbitrary** `OverlapComposition`
whose two rules are Bokut–Shiao, rather than for the `CornerGeneral.oc` this file
builds. That is `overlap_resolves`'s own shape, for this cell of the table.

Three pieces:

- **`bsbs_oc_eq`** — the bridge. With the overlap known to be one letter (§4au),
  the two `lm_decomp`s determine everything: `lm₁ = descWord i j₁ ++ [σᵢ]` splits
  against `left ++ [x]` with matching tails, so `left = descWord i j₁` and
  `x = σᵢ`; then `lm₂ = [σᵢ] ++ right` against `σᵢ :: (descWord i₁ j₂ ++ [σᵢ])`
  gives `right`. Structure equality follows, the three `Prop` fields being
  proof-irrelevant.
- **`bsbs_top_eq`** — the two rules need **not** be assumed to share a top. The
  overlap is `σᵢ` from `rule₁`'s side and `σ_{i₂}` from `rule₂`'s (a Bokut–Shiao
  word begins with its top), so a one-letter overlap *forces* `i₂ = i`, hence
  `i₂' = i₁`.
- **`bsbs_resolves_of_oc`** — the two together, feeding
  `CornerCriterion.bsbs_overlap_resolves`.

**§4au was the enabling step, not decoration.** Without the single-letter fact
the two decompositions constrain `left`/`right` only up to a splitting, and the
bridge is a case analysis over splittings rather than an equation.

### Scope, unchanged and added

Inherits every §4as limit, `j₁ ≥ 1` included. **Adds one**: `oc.left ≠ []`, which
is what §4au needs and what `overlap_resolves` does *not* require — so the
degenerate `left = []` compositions are still uncovered here. `spoly_isZero_of_self`
handles those only when the two rules coincide.

### Remaining

1. `left = []` for this cell.
2. The other cells of the rule-kind table, and every `InclusionComposition`.
3. The deep diagonal `j₁ = j₂ = 0`, still open from §4as.

## The BS × BS cell, closed (2026-08-24, §4aw)

`bsbs_resolves`: the criterion's obligation for an arbitrary `OverlapComposition`
whose two rules are Bokut–Shiao, with **no hypothesis on either context**. The
`oc.left ≠ []` that §4av had to assume — because §4au does — is gone.

**The degenerate case turned out not to be a reduction argument at all.** With no
left context the first leading monomial *is* the overlap, so the second contains
the first as a prefix: `bsWord₁ i' j₂ = bsWord₁ i j₁ ++ right`. Both words begin
with their top letter, so `i' = i` and `ip = i₁`. The trailing `σᵢ` of the
shorter word then has to land somewhere in the longer one, and it cannot land
inside the descending run (`descWord_index_le` caps every index at `i − 1`), so
it lands at the very end: `right = []` and the two runs coincide.
`descWord_bot_inj` turns that into `j₁ = j₂`, so the two rules are **the same
rule** with both contexts empty — and `spoly_isZero_of_self` had already
discharged that.

Two small helpers, both `Classical.choice`-free: `descWord_bot_mem`
(`⟨j⟩ ∈ descWord i j`) and `descWord_bot_inj` (`descWord i j₁ = descWord i j₂ →
j₁ = j₂`, by `descWord_index_ge` in both directions).

### Where the bean now stands

| step | state |
|---|---|
| rule-level membership inversion | done, §4at |
| single-letter overlap, all four shapes | done, §4au |
| shape bridge, arbitrary `oc` → constructed | done, §4av |
| empty left context | done, §4aw |
| **BS × BS cell of `overlap_resolves`** | **done, modulo `j₁ ≥ 1`** |
| deep diagonal `j₁ = j₂ = 0` **with `i₁ ≥ 1`** | **open** — see §4ax; the gap is narrower than this table first said |
| the other rule-kind pairs | open |
| every `InclusionComposition` | open |


## The gap, measured rather than assumed (2026-08-24, §4ax)

`jm` was a **parameter** of `bsbs_overlap_resolves`, so passing it was required
even in the branches that never mention it. Reading which branches actually use
it: only `a ≥ 2` under `j₂ ≤ j₁`. The `a = 1` branch and the entire `a > b`
regime do not.

So `jm` is now **derived inside the proof** and the parameter is replaced by

    hcov : 1 ≤ j₁ ∨ 1 ≤ j₂ ∨ i₁ = 0

whose negation is exactly `j₁ = 0 ∧ j₂ = 0 ∧ i₁ ≥ 1`. Each disjunct discharges
the `a ≥ 2` branch: the first directly; the second because `j₂ ≤ j₁` holds
there; the third **vacuously**, since that branch also carries `j₁ + 1 ≤ i₁`.

**The open set is smaller than this bean has been saying.** It is not "all of
`j₁ = 0`", nor even all of `j₁ = j₂ = 0`:

| case | status |
|---|---|
| `j₁ ≥ 1` | covered (as before) |
| `j₁ = 0`, `j₂ ≥ 1` | covered — this is the `a > b` regime, `sPoly_gt_resolves`, which never needed `jm` |
| `j₁ = j₂ = 0`, `i₁ = 0` | covered — `a = 1`, `sPoly_le_resolves₁`, which never needed `jm` |
| **`j₁ = j₂ = 0`, `i₁ ≥ 1`** | **open** |

Two of those three newly-covered rows were reachable by chains already in the
file; only the parameter's position was stopping them. Nothing new was proved
about the reductions here — the correction is to what the hypothesis *claimed*
was open.


## Corpus-grep failure, and what it changes (2026-08-24, §4ay)

**§4m already carried both facts I presented as new questions**, and I did not
cite it. Found only afterwards, while grepping the `_resolves` inventory for the
next tranche.

| §4m has | since when | what today added |
|---|---|---|
| `overlapTriples_four_proper_overlap_length_one` — the single-letter fact, `decide` at `n = 4`, with the reason in prose | before today | §4au proves it for **every `n`** |
| `completedLMSet_four_infix_antichain` + `inclusion_contexts_empty` — **the inclusion half settled at `n = 4`** | before today | nothing |

Two distinct errors, and they are not the same size.

1. **§4au and PR #5627 framed "is any overlap multi-letter?" as an open
   question.** It was decided at `n = 4` and the argument was written out in
   prose three sections up. Generalising a `decide`-at-one-`n` to all `n` is
   real content and stands — but it is a *generalisation*, not an answer to an
   open question, and saying so was the corpus-grep discipline's job.
2. **I listed "every `InclusionComposition`" as fully open** in the §4av and
   §4aw prose, in three PR bodies, and in this bean's own status table. §4m
   settles the inclusion half at `n = 4` *structurally* —
   `inclusion_contexts_empty` needs no hypothesis about which rules are
   involved. That is an over-claim of openness, the exact class the
   "Before declaring open" checklist exists to prevent.

**One note on §4m's prose, in its favour and against it.** Its stated reason —
"every leading monomial is descending after its first letter" — is a sketch, not
the statement: `σⱼσᵢσⱼ` with `j = i + 1` ascends after its first letter, and
`σᵢσᵢ` is neither strictly low-then-high nor strictly high-then-low, which is
precisely why the quadratic self-pairing is a legal two-letter overlap *shape*
saved only by an empty left context. §4au's `lm_head_is_max` has no such edge
cases. So the two are complementary, and neither supersedes the other.

### The consequence for what to do next

The inclusion half is settled at `n = 4` and **its general-`n` form is the
better target than another overlap cell** — it is half of
`IsGrobnerShirshovBasis`, and `lm_head_is_max` is most of what it needs. Sketch:
a leading monomial's max sits only at position 0 or at the last position, so an
infix `lm₁` of length ≥ 3 starting at `p ≥ 1` would need its two copies of its
own max both strictly inside a strictly-decreasing run. The length-2 shapes are
separated by their consecutive drop (0 for `σᵢσᵢ`, ≥ 2 for far-commutation,
1 elsewhere).

## Half of §4m's antichain, for every n (2026-08-24, §4az)

Acting on §4ay's conclusion that the **inclusion half** is the better target than
another overlap cell — it is half of `IsGrobnerShirshovBasis`, and §4m has it
only at `n = 4` by `decide`.

`lm_split` is the engine: every leading monomial is `h :: (mid ++ [l])`, and all
four families read off through a single `List.append_inj'` — interiors `[]`,
`[σᵢ]`, `[]`, `descWord i' j`. Off it:

- `lm_interior_lt_head` — the interior is **strictly** below the head.
- `lm_last_eq_head_or_far` — the last letter **is** the head, except
  far-commutation, where it drops by ≥ 2 **and the interior is empty**. The
  second conjunct is deliberate: it lets a consumer *discharge* the exception
  rather than reason about it.
- `lm_cons_snoc` — every leading monomial has length ≥ 2.

**`lm_not_proper_suffix`** is what closes: no leading monomial is a proper suffix
of another, for every `n`. Three lemmas in sequence, no case analysis of its own
— `lm₁`'s head lands in `lm₂`'s interior so is strictly below `lm₂`'s head, while
`lm₁`'s last letter *is* `lm₂`'s last letter, which is `lm₂`'s head; and a head
dominates its own word.

### Not done, and why it does not follow

The other direction — proper **prefix**, and the strictly-interior case — needs
two facts about `descWord` the file does not have:

1. **no repeated letter** — separates a Bokut–Shiao word sitting inside another's
   descending run (equal head and last letter would be a repeat);
2. **adjacent letters drop by exactly one** — rules out the far-commutation word
   (drop ≥ 2) sitting in that run.

(1) looks routine: `descWord` is a `filter`/`reverse`/`map` off `List.finRange`,
so `List.nodup_finRange` plus injectivity of `⟨·⟩` should give it. (2) is the
real work; `descWord_split` plus (1) is the likely route, since splitting at a
letter exhibits its successor as the head of the second piece.

**So the antichain is NOT generalised — half of it is.** Do not read §4az as
closing the inclusion half.

## The antichain's second case (2026-08-24, §4ba)

`lm₂ = left ++ lm₁ ++ right` splits three ways:

| case | status |
|---|---|
| `right = []` — proper suffix | §4az `lm_not_proper_suffix` |
| `left = []` — proper prefix | §4ba `lm_not_proper_prefix` |
| both non-empty — strictly interior | **open** |

**The two are not one argument run backwards.** §4az reads `lm₁`'s *head* out of
`lm₂`'s interior; §4ba reads `lm₁`'s *last letter* out of it, and discharges the
far-commutation exception differently — there by its empty interior, here by what
`lm₂`'s interior *begins* with. In both Yang–Baxter and Bokut–Shiao that first
interior letter is exactly one step below the head (`σᵢ` under `σᵢ₊₁`; `σᵢ₋₁`
under `σᵢ`, via `descWord_head`), while far-commutation demands a drop of ≥ 2.

**The third case does not follow from the two.** There is no re-association of
`left ++ lm₁ ++ right` making either apply, because `lm₁ ++ right` is not itself
a leading monomial. It needs the two `descWord` facts §4az names.

### `descWord_nodup` — tested, not landed

§4az predicted it "looks routine". **Checked: it does prove**, in two lines —
`List.Nodup.map` with `⟨·⟩` injective, over
`List.nodup_reverse.mpr ((List.nodup_finRange n).filter _)`. One wrong lemma name
on the first attempt (`List.Pairwise.reverse` flips the relation;
`List.nodup_reverse` is the one that does not).

It is **not** in the file, because nothing there would consume it yet — the
consumer is the strictly-interior case. Recorded here so the next agent does not
re-derive it, and so the prediction is on record as *tested* rather than assumed.

## §4m's antichain, generalised (2026-08-24, §4bb)

`lm_infix_antichain` and `inclusion_contexts_empty_general` — §4m's two
`decide`-at-`n = 4` theorems, now proved for every `n`.

The third case landed with the two tools §4az named:

- **`descWord_nodup`** — the two-line fact §4ba recorded as tested. Now it has
  its consumer.
- **`descWord_adjacent`** — the one that needed work. Route: `descWord_split`
  above the letter exhibits its successor as the head of the second piece
  (`descWord_last`, `descWord_head`), and `nodup_split_unique` — a letter pins
  its own position in a duplicate-free list — matches that against the
  decomposition in hand. It needs the letter not to be the run's bottom, which
  is `descWord_last`'s second use.

`lm_not_proper_interior` then has two outcomes and no arithmetic: three of the
four families repeat their head as their last letter, so inside a
duplicate-free run they would place one letter twice
(`repeat_of_head_eq_last`); far-commutation's two letters are adjacent but drop
by ≥ 2, which `descWord_adjacent` forbids.

### The antichain, complete

| case | closed by |
|---|---|
| `right = []` — proper suffix | §4az |
| `left = []` — proper prefix | §4ba |
| both non-empty — strictly interior | §4bb |

### This is NOT the inclusion half of the criterion

It says every inclusion composition has **empty contexts and a shared leading
monomial**. `inclusion_resolves` additionally needs the classification of *rule
pairs* on a shared leading monomial — either the same rule
(`InclusionComposition.spoly_isZero_of_self`) or §4j's Yang–Baxter/Bokut–Shiao
pair (`DegenerateYbBs`) — **and that those are the only two**.
`mem_heckeCompletedRewritingSystem_rules` (§4at) is the tool; it would be that
lemma's first non-`lm_cases` consumer.

## The inclusion half of the criterion, for every n (2026-08-24, §4bc)

`inclusion_resolves_general` — `IsGrobnerShirshovBasis`'s **`inclusion_resolves`
obligation, discharged for every `n`**, for an arbitrary `InclusionComposition`
whose two rules are in the system.

`shared_lm_classify` is the missing piece §4bb named: two rules sharing a
leading monomial are **the same rule, or §4j's Yang–Baxter / Bokut–Shiao pair,
and nothing else**. Sixteen cases off `mem_heckeCompletedRewritingSystem_rules`
(§4at) — its **first consumer outside `lm_cases`**, and the leading-monomial
inversion could not have served, since the conclusion is about *rules*. Eleven
cases are impossible, most dying on `bsWord₁_length_ge_three` with no
arithmetic; the two live off-diagonal ones force the descending run to a
singleton (`descWord_eq_singleton`), which pins `j = i − 1` — exactly §4j.

**No structure bridge was needed**, unlike the overlap side's §4av.
`InclusionComposition.spoly_isZero_of_scaled` already takes an arbitrary `ic`
and asks only for empty contexts plus a coefficient identity, so the arbitrary
composition is discharged where it stands.

### Where the criterion now stands

| obligation | state |
|---|---|
| `inclusion_resolves` — **every `ic`, every `n`** | **done, §4bc** |
| `overlap_resolves` — BS × BS cell | done modulo the deep diagonal `j₁ = j₂ = 0 ∧ i₁ ≥ 1` (§4aw, §4ax) |
| `overlap_resolves` — the other fifteen rule-kind pairs | open |

Half the criterion is closed. Note the asymmetry in what remains: the overlap
half's generic namespaces (`CyclicQuad`, `BraidSelfOverlap`, `BokutShiaoBraid`,
…) are gated on overlap *shape*, and `overlap_length_one` (§4au) now supplies
that gate — so several of the fifteen may be much cheaper than the BS × BS cell
was.

## One bridge for every family (2026-08-24, §4bd)

**The remaining overlap work is bridges, not chains.** Measured against the
`_resolves` inventory: the reduction chains for the other cells mostly already
exist — `farComm_quad_resolves`, `yangBaxter_quad_resolves`,
`bokutShiao_quad_resolves`, `quad_farComm_resolves`, `quad_yangBaxter_resolves`,
`quad_bokutShiao_resolves`, the four `BraidSelfOverlap` theorems,
`FarCommCyclic.{bokutShiao,yangBaxter}_resolves`,
`CyclicFarCommLow.{bokutShiao,yangBaxter}_resolves`,
`BokutShiaoBraid.{yangBaxter,bokutShiao}_resolves`,
`BraidBokutShiao.{yangBaxter,bokutShiao}_resolves`. Each is stated for a
*constructed* composition; what each lacks is the bridge from an arbitrary one.

**`oc_ext_of_left_ne_nil` supplies every bridge at once**: two overlap
compositions with the same two rules and non-empty left contexts are **equal**.
§4au is what makes it true — with the overlap a single letter `x`,
`lm₁ = left ++ [x]` fixes `left` and `x`, and `lm₂ = [x] ++ right` then fixes
`right`. No hypothesis about which rules, no case analysis. It replaces the
per-family bridge §4av had to write by hand.

`quad_right_resolves` is the first column crossed: the obligation for an
arbitrary composition whose **second** rule is quadratic, whatever the first is.
Four branches, each reading `x` off `lm₁`'s last letter and handing the named
composition to a chain that was already there.

### Correction to §4bc's closing prediction

§4bc guessed the generic-namespace cells "may be considerably cheaper than the
BS × BS cell". Measured: **right, but for the wrong reason.** They are cheaper
because their *chains already exist*, not because their shape gate is easier.
And the saving is bigger than predicted, since the bridge turned out to be one
lemma for all families rather than one per family.

### Remaining overlap cells

`quad_right_resolves` covers four of the sixteen. `CyclicQuadLeft` (quadratic
first) is the mirror and has all three of its chains; the `FarCommCyclic` /
`CyclicFarCommLow` / `BokutShiaoBraid` / `BraidBokutShiao` families cover more.
All still need `oc.left ≠ []`, and the `left = []` degenerates are untouched
outside the BS × BS cell (§4aw).

## The mirror column, and a trap worth recording (2026-08-24, §4be)

`quad_left_resolves` — §4bd's column reflected: an arbitrary composition whose
**first** rule is quadratic. Same shape, `oc_ext_of_left_ne_nil` again.

**One branch is not a mirror image, and I nearly wrote it as one.**
`CyclicQuadLeft.quad_bokutShiao_resolves` covers Bokut–Shiao **at `j = i − 1`
only** — `bsWord₂ i' i j` puts its extra letter on the left, so for `j < i − 1`
the second word is not the shape its chain needs. The rest is `QuadBokutShiao`,
a namespace written for exactly that gap (*"this covers precisely what §4q
leaves open"*). The branch splits on `Nat.eq_or_lt_of_le` and calls a different
chain on each side; the composition is unchanged across the split, only the
reduction differs.

**The general lesson for the remaining columns:** an existing `_resolves` may
cover **less of its cell than its name suggests**, and the boundary lives in the
docstring rather than the statement. §4bd's "the chains already exist" is true
but needs reading per chain, not per name. Only the file's own prose caught this
one.

### Overlap cells crossed so far

| cell | by |
|---|---|
| BS × BS | §4aw (modulo the deep diagonal) |
| ? × quadratic | §4bd `quad_right_resolves` |
| quadratic × ? | §4be `quad_left_resolves` |

All still assume `oc.left ≠ []`.

## CORRECTION: the remaining cells are not all mechanical (2026-08-24, §4bf)

I told the owner, at the end of the §4be turn, that what remains is "mechanical
application of the bridge, at roughly one column per PR". **Measured against the
next cell, that is wrong.**

Applying §4be's own lesson — read what each chain covers, not what it is called —
to Bokut–Shiao against far-commutation turns up **four** namespaces, partitioned
by where the far-commutation bottom `j₀` sits relative to the Bokut–Shiao
bottom `j`:

| `j₀` vs `j` | chain | target |
|---|---|---|
| `j₀ + 1 < j` | `CyclicFarCommLow.bokutShiao_resolves` | `CyclicFarCommLow.oc` |
| `j₀ + 1 = j` | `BokutShiaoFarComm.oc_reduces_to_zero` (§4o) | `BokutShiaoFarComm.oc` |
| `j₀ = j` | `BokutShiaoFarCommSame.oc_reduces_to_zero` | `BokutShiaoFarCommSame.oc` |
| `j < j₀` | `CyclicFarCommInner.oc_reduces_to_zero` | `CyclicFarCommLow.oc` |

The partition is complete (`farCommRelation i j₀` needs `j₀ + 1 < i`; the
Bokut–Shiao side has `j ≤ i − 1`), and the last row shares its *target* with the
first while needing a different chain — `σ_{j₀}` lands **inside** the descending
run rather than below it.

**Three of the four rows would go the §4bd/§4be way. The fourth will not:**
`CyclicFarCommInner.oc_reduces_to_zero` asks for four structural hypotheses
(`hsplit`, `hsplit'`, `hB`, `hfarA`) exhibiting how `descWord i j` breaks at
`σ_{j₀}` — a caller has to *build* those with `descWord_split`, not read them off
a leading monomial.

So: `oc_ext_of_left_ne_nil` still bridges; what it does not do is **choose the
chain**, and choosing it is where the remaining work actually is. §4bf records
the map in the file so the next agent starts from it rather than re-deriving it.

**Estimate to carry forward, stated as an estimate:** the two quadratic columns
were ~1 PR each; this cell looks like more, chiefly for its fourth row. The
braid-word families (`BraidSelfOverlap`, `BokutShiaoBraid`, `BraidBokutShiao`)
have not been read this way yet and may hold similar splits — that is unmeasured.

## The braid-word cell — the clean case, measured as such (2026-08-24, §4bg)

§4bf read the next cell before writing it and found a four-way split. The same
reading applied to the braid-word families finds the **opposite**, and the reason
is in their own docstrings: `wHi i' i` carries **exactly two** rules (§4j), and on
the other side *"`rule₁` cannot double: `j₁ ≤ i − 2` puts its leading monomial
strictly longer than the braid word"*. `BraidSelfOverlap`'s four theorems are not
a sample of a larger family — they are all of it.

- **`lm_eq_wHi_cases`** — a rule of the completed system leading on `wHi i' i`
  **is** `yangBaxterRelation i' i` or `bokutShiaoRelation i' i i'`. Quadratic and
  far-commutation are the wrong length; a Bokut–Shiao word reaches length three
  only when its descending run is a singleton (`descWord_eq_singleton`), forcing
  `j = i − 1`.
- **`braid_self_resolves`** — two applications of that plus one
  `oc_ext_of_left_ne_nil` per branch. The bridge is unusually direct here, since
  `BraidSelfOverlap.oc` takes its two rules as *parameters*, so the rule-equality
  side conditions are the classification's own output.

**A hypothesis dropped, not silenced.** The first draft gave `lm_eq_wHi_cases` an
`hi : i'.val + 1 = i.val`; the linter flagged it unused, and it is — matching a
leading monomial against `[σᵢ, σᵢ', σᵢ]` *forces* `i' + 1 = i` in both surviving
families, so the side condition is an **output**, not an input. Removing it made
the lemma strictly stronger. (The warning appeared only once the code was in the
file, not in the scratchpad — worth knowing: the per-file linter set differs.)

### Cells crossed, all under `oc.left ≠ []`

| cell | section |
|---|---|
| `BS × BS` | §4aw (modulo the deep diagonal) |
| `? × quadratic` | §4bd |
| `quadratic × ?` | §4be |
| braid word × braid word | §4bg |
| `BS × FC` | **mapped only** (§4bf) |

## Bokut–Shiao against the braid word, both ways (2026-08-24, §4bh)

Measured before writing, as §4bf and §4bg were. `BokutShiaoBraid.oc` admits any
`j₁ ≤ i − 1`, but its two chains require `j₁ < i − 1` **strictly**. The excluded
endpoint is **not a gap**: at `j₁ = i − 1` the Bokut–Shiao rule leads on the
braid word itself (`bs_hlm`), so *both* rules do — and that is §4bg. The two
sections compose to cover the cell, with §4bg a **prerequisite** of this one
rather than a parallel result.

Each direction splits on `Nat.eq_or_lt_of_le` at that point, the two branches
going to different sections. `BraidBokutShiao` mirrors it exactly.

This is the shape §4bd predicted for the generic-namespace cells, and it holds —
with the caveat §4be added and §4bf illustrated: **the split point came from
reading the chains' side conditions, not the family's name.**

### Score on the "read before writing" discipline

Three cells read this way so far: `BS × FC` (four-way, §4bf), braid-word (clean,
§4bg), BS-against-braid-word (two-way, §4bh). Two of three had a split the name
did not advertise, and none of the three matched a guess made without reading.
The discipline has paid for itself each time; the `BS × FC` four-way remains the
worst case found.

### Cells crossed, all under `oc.left ≠ []`

| cell | section |
|---|---|
| `BS × BS` | §4aw (modulo the deep diagonal) |
| `? × quadratic` | §4bd |
| `quadratic × ?` | §4be |
| braid word × braid word | §4bg |
| `BS × braid word`, both directions | §4bh |
| `BS × FC` | **mapped only** (§4bf) |

## The four-way cell, crossed (2026-08-24, §4bi)

§4bf mapped `BS × FC` and stopped. §4bi crosses it. **The map held** — four rows
on `j₀` against `j` — and row 4 needed exactly what §4bf said it would.

**One side condition the map missed.** `BokutShiaoFarCommSame.oc_reduces_to_zero`
also wants a `jp` with `j + 1 = jp ≤ i − 1`. It is *vacuous* here (that row has
`j₀ = j`, and `farCommRelation i j` exists only for `j + 1 < i`), but it still
has to be **supplied**. §4bf had read the chains' *docstrings*; reading their
*hypotheses* is a different act, and only the second finds this.

**Row 4 is the one that is not a bridge application**, as predicted.
`CyclicFarCommInner` asks for four structural facts about how `descWord i j`
breaks at `σ_{j₀}`, built rather than read off:

- `descWord_split` cuts the run at `j₀`;
- `descWord_last` peels `σ_{j₀}` off the upper piece to expose `A`;
- **`descWord_nodup` is what makes every letter of `A` strictly above `j₀`** —
  membership alone gives `≥`, and the chain needs `>`.

All three come from §4bb, written for the antichain and reused here unchanged.
That is the second time §4bb's `descWord` infrastructure has paid for itself
outside its original purpose.

### Cells crossed, all under `oc.left ≠ []`

| cell | section |
|---|---|
| `BS × BS` | §4aw (modulo the deep diagonal) |
| `? × quadratic` | §4bd |
| `quadratic × ?` | §4be |
| braid word × braid word | §4bg |
| `BS ×` braid word, both directions | §4bh |
| `BS × FC` | §4bi |

Remaining: `FC × ?` and `YB × ?` combinations not covered above, the standing
`oc.left ≠ []` assumption everywhere, and the deep diagonal
`j₁ = j₂ = 0 ∧ i₁ ≥ 1`.

## The `FC × ?` row — and a gap that was a chain, not a bridge (2026-08-24, §4bj)

Reading `FarCommCyclic`'s **hypotheses** rather than its docstrings (the §4bi
lesson) turned up something the earlier cells did not have: a **missing
instantiation**. The namespace exposes a generic `oc_reduces_to_zero` and two
uses of it — `bokutShiao_resolves`, `yangBaxter_resolves`. There is no third,
and `FC × FC` needs one.

`farComm_farComm_resolves` supplies it, and the fit is exact:
`farCommRelation m d = ofTerms [([σ_m, σ_d], 1), ([σ_d, σ_m], −1)]` **is** the
family's normal form `ofTerms [(σ_m :: u'', c), (q :: t, −c)]` at `u'' = [σ_d]`,
`c = 1`, `q = σ_d`, `t = [σ_m]` — so `hrel` is `fun _ => rfl`, exactly as for
`farComm_quad_resolves`. The two blanket far-commutation conditions follow from
`d < m` and `m + 1 < x` by `omega`.

**This is the first cell whose gap was a chain rather than a bridge**, and the
two are worth separating. `oc_ext_of_left_ne_nil` (§4bd) still did all the
bridging. What a bridge cannot do is notice that a family has an uninstantiated
member — only reading the family against the cells it is supposed to cover does
that.

`farComm_left_resolves` closes the row. Its quadratic branch defers to §4bd's
column rather than repeating it: `quad_right_resolves` already carries its own
bridge, so no second one is built.

### Measured for the next tranche: `YB × FC` splits two ways

`CyclicFarCommLow.yangBaxter_resolves` requires `j₀ + 1 < i'`, **stricter** than
the far-commutation rule's own `j₀ + 1 < i = i' + 1`. The endpoint `j₀ + 1 = i'`
is `YangBaxterFarComm.oc` (§4p). Together they are exactly the rule's condition.
Recorded now so the next pass does not re-derive it.

### Cells crossed, all under `oc.left ≠ []`

| cell | section |
|---|---|
| `BS × BS` | §4aw (modulo the deep diagonal) |
| `? × quadratic` | §4bd |
| `quadratic × ?` | §4be |
| braid word × braid word | §4bg |
| `BS ×` braid word, both directions | §4bh |
| `BS × FC` | §4bi |
| `FC × ?` (whole row) | §4bj |

## §4bk — `YB × FC`, and the `? × FC` row closed (PR pending)

The one cell §4bj measured but did not cross. Because that measurement was
*recorded* rather than left implicit, this pass spent nothing re-deriving it:
the two-way split went straight into the proof.

`yb_farComm_resolves` splits on `j₀ + 1` against `i'`:

- `j₀ + 1 = i'` — §4p's own `YangBaxterFarComm.oc`, discharged by
  `oc_reduces_to_zero`.
- `j₀ + 1 < i'` — `CyclicFarCommLow.oc` at `left = [σ_{i'}]`, discharged by
  `yangBaxter_resolves`.

`Nat.eq_or_lt_of_le` off `j₀ + 1 ≤ i'` is the whole case split, and the two
branches are jointly exhaustive because the far-commutation rule's condition is
`j₀ + 1 < i = i' + 1`, i.e. `j₀ + 1 ≤ i'`. Nothing left over, nothing
overlapping — the fit is exact, not merely adequate.

`farComm_right_resolves` then closes the row by dispatch on `rule₁`'s family:
quadratic → §4be, YB → here, FC → §4bj, BS → §4bi.

**The dispatch has one shape, used four times.** The overlap is a single letter
(§4au), `lm₂ = σᵢσ_{j₀}` starts with it, so the letter *is* `σᵢ`; hence
`lm₁ = left ++ [σᵢ]`. Each branch then reads its family's `lm` and matches the
last letter with `List.append_inj'`. That is why the four branches differ only
in which `lm` lemma they rewrite with — the identification of `i` is uniform.

### What this did NOT do

- Still assumes `oc.left ≠ []`. Every cell §4bd–§4bk does; the nil-left
  compositions are untouched and open.
- Does not close `overlap_resolves`. The `YB × ?` combinations other than
  `YB × FC` are not covered — that row is what remains.
- The deep diagonal `j₁ = j₂ = 0 ∧ i₁ ≥ 1` of `BS × BS` (§4aw) is still the
  only piece needing genuinely new reduction content.

### Cells crossed, all under `oc.left ≠ []`

| cell | section |
|---|---|
| `BS × BS` | §4aw (modulo the deep diagonal) |
| `? × quadratic` | §4bd |
| `quadratic × ?` | §4be |
| braid word × braid word | §4bg |
| `BS ×` braid word, both directions | §4bh |
| `BS × FC` | §4bi |
| `FC × ?` (whole row) | §4bj |
| `YB × FC`, and `? × FC` (whole row) | §4bk |

## §4bl–§4bn — `IsGrobnerShirshovBasis`, modulo one self-overlap (PR pending)

The bean's stated goal, reached with a single explicit hypothesis left standing.

### §4bl — the `oc.left ≠ []` caveat was not a gap

Every cell §4bd–§4bk assumed `oc.left ≠ []`, and I had been recording the
excluded case as open. It is not: it needs **no cell and no reduction**.

`left = []` says `lm₁` *is* the overlap, so `lm₂ = lm₁ ++ right`; §4ba's
`lm_not_proper_prefix` forces `right = []`; the two rules therefore lead on the
same word, which is §4bc's `shared_lm_classify` — same rule, or §4j's YB/BS
pair. Same rule → `spoly_isZero_of_self`. The pair → the two relations sum to
zero coefficient by coefficient (`DegenerateYbBs.relations_add_eq_zero`) against
leading coefficients `−1` and `+1`, so the S-polynomial is **zero**, not merely
reducible to zero.

Strictly more general than §4aw's `bsbs_resolves_of_nil_left`, which proved the
same thing for two Bokut–Shiao rules only. Compiled first try.

### §4bm — the matrix assembles, and two "hypotheses" evaporate

Dispatching on `rule₂` first cuts the work in half: `quad_right_resolves` (§4bd)
and `farComm_right_resolves` (§4bk) already take an arbitrary `rule₁`, so only
the YB and BS columns need a second dispatch. `overlap_letter` is the one shared
step — single-letter overlap (§4au) gives `lm₁ = left ++ [z]` and
`lm₂ = z :: right` at once, and every index identification in both columns is
that argument.

**Two things I had been carrying as open were artefacts of not reading
hypotheses:**

1. **`hq : q − q⁻¹ ≠ 0` is not a hypothesis.** `HeckeParams.h_ne_zero`
   (line 1311, already in the file) proves it from `HeckeParams` alone.
   `bsbs_resolves_of_oc` carries it redundantly. The assembly discharges it.
   I had listed it as a standing condition on the BS×BS cell.
2. **`i₁ = 0` is not a Bokut–Shiao case.** `bsbs_resolves_of_oc` needs `i₂` with
   `i₂ + 1 = i₁`, so it silently requires `i₁ ≥ 1` — and at `i₁ = 0` both `j`s
   are forced to `0 = i₁`, making both leading monomials the braid word. §4bg
   takes it.

### The gap, stated sharply

Forcing `i' = i` off the overlap letter forces `ip = i₁`, so at `j₁ = j₂ = 0`
the two rules are **the same rule**. `hdeep` is therefore not a family: it is the
longest Bokut–Shiao word `σᵢσᵢ₋₁⋯σ₀σᵢ` overlapping **itself** in its shared `σᵢ`,
at `left = descWord i 0`. One composition.

### §4bn — the criterion

`heckeCompleted_isGrobnerShirshovBasis` = §4bc (inclusion half, unconditional,
every `n`) + §4bm (overlap half, modulo `hdeep`). No `sorry`, no axiom; `hdeep`
is an explicit argument.

**Not proved: that `hdeep` holds.** If that self-overlap does not resolve, the
completion is incomplete and needs a further rule. This statement is where that
would surface — it is a reduction of the problem to one composition, not a
closure of it.

## The deep self-overlap RESOLVES — measured, with the target (PR pending)

Before trying to prove `hdeep`, the cheap decisive check (AGENTS.md
formalize-first §caveat: run the probe when it is cheap and decisive).
[`computations/hecke_deep_selfoverlap_probe.py`](../computations/hecke_deep_selfoverlap_probe.py)
reduces both sides of the S-polynomial under the completed system, exact
symbolic in `q`, 1.8 s to `i = 9`.

**It resolves for every `i = 1 … 9`, and the normal form does not depend on rule
order** (checked against the reversed rule list). So the completion is **not**
missing a rule — the outcome that would have mattered most did not happen.

**The target, for `i ≥ 2` — both sides land on the same TWO-term normal form:**

```
bsWord₂(i−1, 0) · descWord(i, 1)  +  (q − q⁻¹) · bsWord₂(i−1, 0) · descWord(i, 0)
```

The second word is the first with a trailing `σ₀`. `i = 1` is degenerate
(`descWord(i−1, …)` collapses; four terms). All three facts are **assertions in
the probe**, not prose — a future edit that breaks them fails.

**Chain size:** `i(i+5)/2` steps on the left, one more on the right, checked for
`i = 2 … 9`. Strategy-dependent — a size estimate for the induction, not a fact
about the algebra. It says the chain grows linearly per level, so the Lean proof
wants a general step lemma, not an enumeration.

Rules were read off the Lean `def`s (`heckeRelation`, `yangBaxterRelation`,
`farCommRelation`, `bokutShiaoRelation`) rather than off prose, including the
Yang–Baxter `lc = −1` sign that makes `wHi → wLo`.

### Not mine, recorded rather than swept

`precision-gates.sh --changed` reported two stale committed audit witnesses
(`q0-anchor-consistency-audit`, `witness-provenance-audit`). The movement is
**main's**, not this branch's: the newly-listed witnesses are
`gz-third-knot-rank-grading` (`749186133b`) and `aomega-m3-adjoint-index-set`
(`683299faf7`). Counts would move `total_scanned` 2731 → 2732, `prov_ok`
2333 → 2335, `Q0_INDEPENDENT` 47 → 48. Tree restored; not swept into a Lean PR.
All blocking precision gates green.

### The shape of the induction, measured (rule census)

Tracing *which* rules fire, not just that the sides converge:

| i ≥ 3 | QUAD | YB | FC | BS |
|---|---|---|---|---|
| A | 1 | 1 | `(i+4)(i−1)/2` | `i` |
| B | 1 | 1 | `(i+4)(i−1)/2 − 1` | `i+2` |

**For `i ≥ 2` exactly ONE quadratic step fires, always on `σ₀`.** That is the
only coefficient-producing rule, and it is why the normal form has two terms:
the split's `1` branch drops two letters and its `Hσ₀` branch drops one, so the
two words differ by a trailing `σ₀`. Everything else is a length-preserving
monomial rewrite.

**Consequence for the Lean proof:** the coefficient bookkeeping is a single
`heckeRelation` split. The rest is pure word combinatorics — which is the
tractable half. `i = 1` is degenerate (three quadratic steps at indices
`[0,1,0]`, hence the `H²` and four terms).

The QUAD count is the **robust** one, and it is now *measured* rather than
argued. I first wrote that it is "pinned by the two-term normal form" — but that
is only an argument, and it has a hole: a second split whose branch died would
produce the same two-term form. So the census now runs under the **reversed rule
order** as well, and gets one quadratic step on `σ₀` both ways.

The YB/FC/BS split is strategy-dependent bookkeeping, like the step count;
asserted so a change in the rule set surfaces, not claimed as algebra. Totals
reconcile: `1 + 1 + (i+4)(i−1)/2 + i = i(i+5)/2` ✓.

### Next tranche: the `hdeep` induction — what the measurements say to build

Not started. Recorded so it is not re-derived.

- **Target** (§4bn docstring + probe): both sides land on
  `bsWord₂(i−1,0)·descWord(i,1) + H·bsWord₂(i−1,0)·descWord(i,0)` for `i ≥ 2`.
- **Coefficient work is one step.** A single `heckeRelation` split on `σ₀`;
  every other rewrite is monomial. So the chain lemmas can be stated on *words*
  and the algebra enters once.
- **Do not look for a shared pre-split word.** Measured: the two sides reach
  the `σ₀σ₀` differently — at `i = 2` A splits in `(0,1,2,0,1,0,0)` and B in
  `(1,2,0,1,0,0,2)`. The convergence is after the split, not before it, so a
  "both reduce to a common word, then split once" plan does not fit.
- **Size:** the chain grows by about `i+2` rewrites per level
  (`FC` by `i+1`, `BS` by `1`), so an enumeration will not scale — the step
  lemma has to be general in `i`.
- **`i = 1` needs its own case** (three splits, `H²`, four terms), as does
  `i = 2` (its YB/FC/BS counts do not follow the `i ≥ 3` pattern).

### The chain's shape — and why the obvious induction does NOT fit (PR pending)

Two findings, one positive and one negative. The negative one is the useful one.

**Positive: the per-step machinery already exists.** `monicStep` (one step by any
monic two-word rule, arbitrary contexts and surrounding terms), `quadStep` (the
split, output one term longer) and `bsStep` (`monicStep` at Bokut–Shiao) are
already in `HeckeCompletion.lean`. Since every non-quadratic rule here is monic
and two-word, each step of the chain is a one-liner. Per-step cost is not the
problem.

**Negative, and measured: `chain(i−1)` is NEVER a prefix of `chain(i)`.** The
shared opening grows — `(i²−5i+12)/2` on side A, `(i−3)(i−2)/2` on side B — but
the differing tail grows too, `5i−6` and `5i−2`, and never vanishes. So the
greedy reduction does **not** satisfy "chain(i) extends chain(i−1)", and an
induction on `i` has to be built on a **hand-designed** chain, not on this one.

Recorded because reading the traces by eye suggests the opposite: the openings
do visibly agree, at length, and I read that as "chain(i−1) is a prefix". It is
not. The assertion is now in the probe so the claim cannot rot.

**A second error the assertions caught.** I fitted the shared-opening formula on
side A and applied it to side B; side B follows triangular numbers instead. One
fit does not cover both sides. Both are now asserted separately.

**Shape of the greedy chain (side A):** a nested cascade —
`BS(-1)@1 FC(0)@0`, then for `k = 0 … i−2` a block `BS(-k)@(2k+1)` followed by
`FC` steps sweeping down, then `YB(-(i-1))@(2i-1)`, the single `QUAD` on `σ₀` at
`2i+1`, and an `FC` tail with every step doubled — one per branch of the split.

**So the next tranche is: design the chain, don't transcribe this one.** The
target normal form and the one-quadratic-step fact still hold and still apply.

**Starting points for the designed chain** (corpus-grepped, not guessed):
`descWord_split` / `descWord_split_aux` (which already inducts *on the gap*,
`HeckeCompletion.lean:3963`), `descWord_snoc`, `descWord_cons`, `descWord_at_pred`.
The cascade sweeps a descending run downward one index at a time, which is the
same motion `descWord_split_aux` already formalises — so the induction variable
is the gap, not `i`.

### Designing the chain: three plans ruled out, two waypoints found (PR pending)

The reframing that made this tractable: the normal form **factors**,

```
NF(i) = bsWord₂(i−1,0) · descWord(i,1) · (1 + H·σ₀)
```

and `1 + Hσ₀` is exactly what `σ₀σ₀` rewrites to. So the whole S-polynomial is
one word with a `σ₀σ₀` on the end, and the single quadratic step is the last one.

**Waypoint 1 — side A.** A reaches `bsWord₂(i−1,0)·descWord(i,1)·σ₀σ₀` by
length-preserving rewrites *alone*, in `(i²+i+4)/2` steps (BFS-minimal), and the
one quadratic step there lands **directly on the normal form**. Side A's whole
reduction is monomial until the very last step.

**Waypoint 2 — side B.** B reaches
`splitWord(i) = (i−1,i, i−2,i−1, …, 0,1, 0,0, i)` in only **i−1** steps — pairs
`(k−1,k)` descending, then `σ₀σ₀`, then `σᵢ` — and does its quadratic work after
the split, `(i²−i+4)/2` steps per branch.

**Ruled out, each measured rather than argued:**

1. **`chain(i)` extends `chain(i−1)`** — no (previous section: the shared opening
   grows but the differing tail never vanishes).
2. **A and B reach a common word and cancel with no split** — no. The two
   length-preserving closures are **disjoint**, checked to `i = 6` with ~200
   words each. So the quadratic step is unavoidable; there is no shortcut in
   which the difference dies before it.
3. **The `i`-case reduces into a context around the `(i−1)`-case** — no. No word
   reachable from `A(i)` contains `A(i−1)` as a factor, and likewise for B.

**Consequence:** the induction is on the **sweep inside one chain** — the gap —
not on `i` relating whole chains. That is the motion `descWord_split_aux`
(line 3963) already formalises, which is why it is the right starting point.

All five facts are assertions in the probe, so none of them can rot.

**Honest status: `hdeep` is NOT proved and is a multi-session formalization.**
The route is now specified rather than searched for: two closed-form waypoints,
`monicStep`/`quadStep`/`bsStep` for the steps, and the gap as the induction
variable. What is left is writing it.

**Side A's minimal path, extracted (BFS shortest, indices relative to `i`):**

```
i=3:  BS(-1)@1 FC(0)@0 BS(0)@1 BS(-1)@3 YB(-2)@5 FC(-1)@4 FC(0)@2 FC(0)@3
i=4:  BS(-1)@1 FC(0)@0 BS(0)@1 BS(-1)@3 FC(0)@2 BS(-2)@5 YB(-3)@7
      FC(-2)@6 FC(-1)@4 FC(-1)@5 FC(0)@3 FC(0)@4
i=5:  BS(-1)@1 FC(0)@0 BS(0)@1 BS(-1)@3 FC(0)@2 BS(-2)@5 FC(-1)@4 FC(0)@3
      BS(-3)@7 YB(-4)@9 FC(-3)@8 FC(-2)@6 FC(-2)@7 FC(-1)@5 FC(-1)@6
      FC(0)@4 FC(0)@5
```

A descent phase — for `k = 1, 2, …` a `BS(-k)@(2k+1)` followed by an `FC` sweep
`FC(-(k-1))@(2k), …, FC(0)@(k+1)` — terminated by `YB(-(i-1))@(2i-1)`, then a
final `FC` sweep. Doubly nested, and each loop is a descending sweep, so both
levels are gap inductions of the `descWord_split_aux` kind.

## §4bo — side B's half of `hdeep`, PROVED in full generality (PR pending)

Not a measurement this time. Lean, general in `i`, sorry-free.

`doubleDesc_sweep`: `descWord m z ++ descWord m z ⟶* pairSweep m z`, by exactly
one Bokut–Shiao step per level. The peel is uniform — the second copy's head
`σ_m` closes the first copy into `bsWord₁ m z`, the rule replaces it by
`bsWord₂ (m−1) m z = σ_{m−1}σ_m ++ descWord (m−1) z`, and what remains is the
same shape one level down. **The bottom needs no step at all**:
`descWord z z ++ descWord z z` *is* `σ_z σ_z`.

`bside_to_splitWord`: the sweep applied in the context `[σ_{i−1}, σ_i] ⋯ [σᵢ]`,
landing B on `pairSweep i 0 ++ [σᵢ]` in `i − 1` steps.

**`pairSweep` is defined by a zip, not a recursion** —
`zip (descWord m z) ((descWord m z).tail ++ [σ_z])` flattened pair-by-pair — so
no arithmetic on `Fin n` appears in the definition and `pairSweep_cons` is a
one-line `descWord_cons` rewrite. That choice is what kept the whole section
short; a recursive definition would have needed `Fin.mk` bounds at every level.

**A correction to the measurement that led here.** The BFS labelled B's last
step `YB`. It is a **Bokut–Shiao** step: at `m = 1` the word `σ₁σ₀σ₁` is
`bsWord₁ 1 0` *and* the braid word `wHi 0 1` — §4j's shared-lm pair — and both
rules send it to `σ₀σ₁σ₀`. So the route is uniform after all, one rule
throughout, which is why the induction is a single peel rather than a peel plus
a special last step.

### What this does NOT do

- **Side A is not this.** Doubly nested — a `BS` per level each followed by an
  `FC` sweep — and `(i²+i+4)/2` steps rather than `i−1`. Still to be written.
- **Both statements are on a ONE-TERM element**, which makes `monicStep`'s side
  condition on the surrounding terms vacuous. The `hdeep` application carries
  the other spoly term alongside; re-establishing that condition against every
  intermediate is work this section does not do.
- **`hdeep` is still open**, and so `heckeCompleted_isGrobnerShirshovBasis` is
  still conditional.

### Measured for the next tranche: B's two branches share one chain shape

After the split, B's `H`-branch and `1`-branch follow the **same shape** of
chain — same families, same positions, same top indices — for `i = 3, 4, 5`
(5, 8, 12 steps each).

**Not "the same chain", and I nearly wrote that.** My label printed only each
rule's *top* index, which hid that the Bokut–Shiao steps differ in their bottom
index `j`: the `H`-branch uses `bsWord₁(3,0)` where the `1`-branch uses
`bsWord₁(3,1)`. That is exactly the extra `σ₀` showing up. So the two branches
are one lemma **parameterised by `j`**, not one lemma applied twice — which is
still a halving of the work, but it is a different statement.

The extra `σ₀` travels: it starts before the final `σᵢ` and ends after it,
commuting past by far-commutation. That is why `NF₂ = NF₁ ++ [σ₀]` while the
branch words differ in the *middle*.

Remaining for `hdeep`, now fully scoped:
1. side A's route to `NF₁·σ₀σ₀` — doubly nested, `(i²+i+4)/2` steps;
2. B's post-split chain, one lemma in `j` — `(i²−i+4)/2` steps;
3. the two-term bookkeeping (`monicStep`'s `hne` against the other spoly term).

## §4bp — side A, swept, and a correction to my own figure (PR pending)

Side A opens with **three fixed steps** onto a doubled descending run, after
which §4bo's sweep applies unchanged:

1. the second copy of the run is preceded by `σ_{i−1}`, so the *first* copy plus
   that letter is `bsWord₁ (i−1) 0` — inner Bokut–Shiao fires;
2. far commutation pulls the freed `σ_{i−2}` to the front;
3. what is left behind it is `descWord i 0 ++ [σᵢ] = bsWord₁ i 0` — outer
   Bokut–Shiao fires, and its `bsWord₂` puts a second `descWord (i−1) 0` against
   the first.

`aside_to_sweptWord`: A reaches `σ_{i−2}σ_{i−1}σᵢ · pairSweep (i−1) 0` in
`3 + (i−1)` steps. Sorry-free, general in `i`, compiled first try.

### Correction: `(i²+i+4)/2` was never side A's cost

I recorded it as "side A's BFS-minimal route" in the previous PR. It is the
distance to **one particular** split word, `bsWord₂(i−1,0)·descWord(i,1)·σ₀σ₀`.
Side A can split much earlier — at the `σ₀σ₀` that `pairSweep` ends with — and
getting there is **linear**. The quadratic figure describes a *choice of split
point*, not the cost of the side.

### And a pattern in the numbers that is not a fact

The residual tails are `i(i−1)/2` per branch on A and `(i²−i+4)/2` per branch on
B — differing by exactly 2 at every `i` tested, which reads like B's branches
reducing onto A's in two steps. **They do not.** Checked to `i = 6`: no B-branch
reaches its A-counterpart at all. The two tails are separate work.

That is the fourth time this session an appealing arithmetic coincidence has
failed a structural test — and the fourth time testing it cost minutes while
assuming it would have cost the tranche.

### Remaining for `hdeep`

1. side A's tail — `i(i−1)/2` per branch;
2. side B's tail — `(i²−i+4)/2` per branch, one lemma in `j`;
3. the two-term bookkeeping (`monicStep`'s `hne` against the other spoly term).

## §4bq — the far-commutation carry, side A's tail inner loop (PR pending)

Side A's tail is **pure far commutation**, and its shape was measured, not
guessed. Grouped by top index the rules are `(2,0)`, `(3,1) (3,0)`,
`(4,2) (4,1) (4,0)`, …, `(i,i−2) … (i,0)` at consecutive positions — `m−1` steps
per `m` from 2 to `i`, i.e. the measured `i(i−1)/2`. Each group is one generator
carried rightward past a descending run.

`gen_past_descWord`: `σ_m · descWord k z ⟶* descWord k z · σ_m` whenever
`k + 1 < m`, one step per letter, induction on the gap. Sorry-free, general.

So the tail's inner loop is done; what remains of it is the outer induction
over `m` from 2 to `i`.

### Two measurements about the tail, both checked properly this time

- **The two branches run the SAME chain**, compared as full rule-and-position
  sequences — not as labels. That distinction matters: labels print only a
  rule's *top* index and have already misled this bean twice (the `YB`-vs-`BS`
  last step in §4bo, and side B's branches, whose Bokut–Shiao steps differ in
  their lower index). Identical at `i = 3, 4, 5, 6`. The branches differ only by
  a trailing `σ₀` that no tail rule touches, so the tail is one lemma with the
  trailing context as a parameter — which `monicStep` already carries as `b`.
- **Side B's tail is not side A's.** `(i²−i+4)/2` vs `i(i−1)/2` — exactly two
  more at every `i`, which reads like B's branches reducing onto A's in two
  steps. They do not: checked to `i = 6`, no B-branch reaches its A-counterpart.

### Remaining for `hdeep`

1. side A's tail — outer induction over `m`, using `gen_past_descWord`;
2. side B's tail — `(i²−i+4)/2` per branch, one lemma in `j`;
3. the two-term bookkeeping (`monicStep`'s `hne` against the other spoly term).

### The carry lemma serves BOTH tails — measured at the rule level

Side B's tail is the **same far-commutation carry sequence** as side A's, at
positions shifted by exactly one, **followed by two Bokut–Shiao steps**. At
`i = 5`:

```
A tail: (2,0)@8 (3,1)@6 (3,0)@7 (4,2)@4 (4,1)@5 (4,0)@6 (5,3)@2 (5,2)@3 (5,1)@4 (5,0)@5
B tail: (2,0)@7 (3,1)@5 (3,0)@6 (4,2)@3 (4,1)@4 (4,0)@5 (5,3)@1 (5,2)@2 (5,1)@3 (5,0)@4
        + bsWord₁(5,j)@5  + bsWord₁(4,0)@0
```

The shift is one because A's swept word carries three leading letters
(`σ_{i−2}σ_{i−1}σᵢ`) and B's carries two (`σ_{i−1}σᵢ`). **That is the whole "+2"**
— B's two extra steps are the two Bokut–Shiao ones, not a different chain.

And the `j` prediction is confirmed: the first of those two BS steps is
`bsWord₁(i,1)` on the `1`-branch and `bsWord₁(i,0)` on the `H`-branch — the only
place the two branches differ. The second BS step is identical in both.

**So `gen_past_descWord` is the shared inner loop of both sides**, which is worth
more than either tail on its own. Remaining: the outer induction over `m`
(shared, modulo the leading context), plus B's two Bokut–Shiao steps with `j` as
a parameter.

This is consistent with the earlier negative — B's branches do *not* reduce onto
A's. Same rule sequence applied to different words is not the same thing as one
word reducing to the other, and both facts hold.

## §4br — the unshuffle, and SIDE A OF `hdeep` COMPLETE (PR pending)

**The unshuffle.** `pairList m z` — the interleaved pairs, i.e. `pairSweep`
without its trailing `σ_zσ_z` — separates into two descending runs:

```
pairList m z  ⟶*  descWord (m−1) z ++ (descWord m z).dropLast
```

one `gen_past_descWord` per level. The IH separates the pairs below; then the
top pair's upper letter `σ_m` is carried across the lower run it now fronts.
Base case `m = z+1`: a single pair is already the target, no step.

Writing the upper run as `(descWord m z).dropLast` is what keeps `z + 1` from
ever having to be named as a `Fin n`. Same trick as `pairSweep`'s zip: **let a
list operation stand in for Fin arithmetic.** Third time it has paid off.

**Side A closes end to end.** §4bp head → unshuffle → one last carry (`σ_i`
leaves the leading block, turning `σ_{i−2}σ_{i−1} ++ descWord (i−2) 0` into
`bsWord₂ (i−2) (i−1) 0` and `σ_i ++ (descWord (i−1) 0).dropLast` into
`(descWord i 0).dropLast`) → **one word ending in `σ₀σ₀`** → the single quadratic
step → `NF + (q−q⁻¹)·(NF·σ₀)`.

That is exactly the two-term normal form the probe measured, and every step
before the last is monomial — exactly as the rule census said. `aside_resolves`
is side A of `hdeep`, in full, general in `i`, sorry-free.

### Two parse traps worth recording

Both cost a compile cycle and neither is about the mathematics:

- **`;` inside `by simpa using e`** ends the *outer* tactic block, so
  `simpa using f (by simp; omega)` does not parse as intended.
- **`[` inside `by simpa using e`** is read as `simpa`'s simp-argument list, so
  a list-literal argument breaks the term.

Both fixed the same way: bind the term with `have` first, then `simpa using` the
name. Worth doing by default in this file, where every step lemma takes list
literals.

### Remaining for `hdeep`

1. side B's tail — the same carry sequence shifted by one, plus two Bokut–Shiao
   steps, the first with `j` as a parameter;
2. the two-term bookkeeping (`monicStep`'s `hne` against the other spoly term),
   which joins the two halves into the S-polynomial statement.

## §4bs — SIDE B COMPLETE. Both halves of `hdeep` land on one element (PR pending)

`bside_to_split` runs §4bo's route to the split word, rewrites it through
`pairSweep_eq` into pairs-plus-`σ₀σ₀`, unshuffles with §4br's
`pairList_unshuffle`, and fires the one quadratic step. **Both sides use the
same unshuffle**; only the context differs — which is what §4bq's measurement
meant by "the same carry sequence shifted by one".

`bside_branch` is the tail, **one lemma parameterised by `j`**: the trailing
`σ_i` closes `descWord i j` into `bsWord₁ i j`; after that fires, the `σ_{i'}`
its `bsWord₂` puts down closes `descWord i' 0` into `bsWord₁ i' 0` for a second.
`j = 0` on the `H`-branch, `j = 1` on the `1`-branch. **Predicted in §4bq from
the measurement, confirmed here in Lean.**

### The two-term bookkeeping, handled by length

After the split `monicStep`'s side condition stops being vacuous. Rather than
compare words, `bside_branch` takes **one** hypothesis — every surrounding term
has a length other than this word's — and discharges both its steps from it,
because Bokut–Shiao is monic and all three words of its chain have the same
length. The two branch words differ in length by exactly one (that same `σ₀`),
so **each is the other's witness**. `descWord_length` makes this arithmetic;
proved on the gap like everything else about `descWord`.

That is the first time the bookkeeping has actually bitten, and length turned
out to be the cheap invariant. Worth reusing for the joining.

### Both targets are the same element

Via `[σ_i] ++ descWord i' 0 = descWord i 0` and
`(descWord i 0).dropLast ++ [σ₀] = descWord i 0`.

### An idea that looked good and is wrong

Before writing the tail I checked whether B could reach A's *pre-split* word,
which would have avoided the bookkeeping entirely. **It cannot**: far
commutation sorts smaller-index-first, so `σ_z σ_i` is already reduced and
`σ_i` cannot move left past the `σ₀σ₀`. I had the rewrite direction backwards.
This is consistent with — and independently confirms — the measured disjointness
of the two monomial closures.

### Remaining for `hdeep`: the joining, and that is all

Run the two chains inside the S-polynomial's two terms, each carrying the other
side's term as context. Both chains exist; both land on the same element; the
coefficients are `+1` and `−1`, so the difference is zero.

### Measured for the joining: length does NOT separate the two sides — the first letter does

Worth knowing before the joining is attempted, because the obvious move fails.

**Length fails.** `A = descWord i 0 ++ bsWord₂ i' i 0` and
`B = bsWord₂ i' i 0 ++ descWord i' 0 ++ [σ_i]` both have length `2i+3`, and both
chains are monic until their quadratic step. So the length invariant that
discharged §4bs's *within-side* bookkeeping cannot separate side A's
intermediates from side B's term.

**The first letter does.** A's word begins `σ_i`; after its second step (far
commutation pulling `σ_{i−2}` out) every later A-intermediate begins `σ_{i−2}`,
because the sweep and the tail all run in a context whose head is that letter.
B's word begins `σ_{i−1}`, and *every* B-intermediate does too — `bside_to_split`
runs its sweep in the context `[σ_{i−1}, σ_i]`, which is never touched. Since
`i`, `i−1`, `i−2` are pairwise distinct, the head letter separates the two sides
throughout.

**Measured, not just reasoned** — I wrote the paragraph above from the chain
structure and then checked it, because reasoning-without-measuring has misfired
four times in this bean. Head letters of *every* monomially-reachable word:

| `i` | A heads | B heads |
|---|---|---|
| 3 | `{1, 3}` | `{2}` |
| 4 | `{2, 4}` | `{3}` |
| 5 | `{3, 5}` | `{4}` |
| 6 | `{4, 6}` | `{5}` |
| 7 | `{5, 7}` | `{6}` |
| 8 | `{6, 8}` | `{7}` |

Exactly `{i−2, i}` against `{i−1}`, disjoint throughout — extended to `i = 8`,
where the closures are 2058 and 2055 words and still wholly disjoint. That is also an
independent confirmation of the measured closure-disjointness, and it is the
invariant the joining should thread — not length.

## §4bt — `CtxAvoids`: the context abstraction the joining needs (PR pending)

The joining needs every chain to run with the *other* side's term sitting
alongside, which means `monicStep`'s side condition stops being vacuous at every
step of every chain. Threading a bespoke condition through ~400 lines would have
been the obvious way and would have been miserable. One definition avoids it:

```lean
def CtxAvoids (L) (a b) : Prop :=
  ∀ w ∈ L.map Prod.fst, ∀ Z, w ≠ a ++ Z ++ b
```

Every intermediate of a chain that rewrites strictly inside `a … b` **has that
shape**, so this single hypothesis discharges all of them. Two lemmas make it
compositional — `.extend` (grow `a` on the right, for a recursive call that
moves letters into the prefix) and `.extendRight` (grow `b` on the left) — and
`.ne` turns it into the `q ≠ W` a step lemma wants, given `W = a ++ Z ++ b`.

`ctxAvoids_nil` says the empty context avoids everything, so **the original
single-term lemmas fall out as one-liners** rather than being duplicated:

```lean
theorem doubleDesc_sweep … := doubleDesc_sweep' … [] [] a b c hc (ctxAvoids_nil a b)
```

Generalised so far, each compiling first try: `gen_past_descWord'`,
`doubleDesc_sweep'`, `pairList_unshuffle'` — the three **recursive** chains,
which were the ones I expected to fight. The `∀ Z` shape is what made them
cheap: a recursive call that moves `[σ_m]` from the middle into the prefix is
`hctx.extend [σ_m]`, one term.

### Why `∀ Z` and not a head-letter invariant

I considered threading "every context word has a different first letter", which
is what the *top-level* discharge will use (§4bs measured it). It is the wrong
shape for the *interior*: each lemma would then have to prove its intermediates'
heads, which is a second invariant to carry. `∀ Z, w ≠ a ++ Z ++ b` needs no
proof obligation inside the chain at all — the shape is structural.

### Remaining

The A-side and B-side assemblies (non-recursive, so the same treatment should be
quicker), then the joining itself: build the canonical composition, compute its
S-polynomial, and run the two chains against each other, discharging `CtxAvoids`
at top level from the head-letter separation.

### §4bu — the A side generalised (PR pending)

`aside_head'`, `aside_to_sweptWord'`, `aside_to_normalWord'`, `aside_resolves'`
— side A now runs inside an arbitrary S-polynomial. The four originals are
corollaries at empty context, so again no duplication.

**The A side needed a different hypothesis shape from the recursive chains, and
`CtxAvoids` supplied it without a new definition.** Its three opening steps sit
in three *different* contexts, so a single `CtxAvoids L a b` does not cover
them. But `CtxAvoids L [σ_x] []` unfolds to *"no surrounding word begins with
`σ_x`"* — a head condition — and every word in the A chain begins with `σ_i` or
`σ_{i−2}`. So two head hypotheses cover the whole side, and `CtxAvoids.narrow`
(`b = []` to any `b`) plus a one-line `hCi'' w hw (…)` re-association discharges
each step.

That is the head-letter invariant §4bs measured, entering exactly where it
belongs — at the *boundary* of a side, not threaded through its interior.

**One trap worth recording:** a step lemma's `hne` is about the word *as the
goal currently has it*, not as the accompanying `e`-equation rewrites it. Stating
it in the rewritten form type-errors; state it on the goal's word and `rw [e]`
inside the proof.

### §4bv — the B side generalised, and the joining's shape settled

`bside_to_splitWord'`, `bside_to_split'`, `bside_branch_core`,
`bside_resolves'` — side B now runs inside an arbitrary S-polynomial too. The
four originals are corollaries at empty context. With §4bu that is **both
sides** generalised; what is left is the joining itself.

#### The collision I expected does not exist

I had assumed the joining would be blocked at its last step: side A and side B
reach the *same two monomials*, so running one chain with the other's normal
form already in the context looked like it would ask a step to fire on a word
that is already present. It does not, for two independent reasons, and I only
found them by reading the definitions rather than reasoning from the shape:

- **`isZero` is coefficient-wise** — `∀ m, f.coeff m = 0`
  ([`Elem.lean:125`](../content/unital-groebner-bases/lean/UGB/GrobnerShirshov/Elem.lean)),
  and `ofTerms` *sums* over the terms carrying a given monomial. Two terms with
  the same word and opposite coefficients are not a problem to be avoided; they
  are exactly the cancellation the S-polynomial needs.
- **`hne` guards the word ENTERING a step, never the one leaving it.**
  `monicStep`'s hypothesis is `∀ q ∈ ctx, q ≠ W` with `hW : W = a ++ L ++ b`,
  and it is used only to prove `coeff (a ++ lm ++ b) = c` — that the step
  subtracts the right amount. The *result* `W'` may coincide with a context
  word freely.

So the joining can run the two chains **sequentially**: A first with B's word
as context, then B with A's normal form as context. The last B step needs its
*penultimate* word absent from the context, and that word is one step short of
A's normal form.

#### Side B needs a head condition and a TAIL condition

Side A took two head conditions (§4bu). Side B takes one head and one tail, and
the tail is not an artefact:

- the sweep and the quadratic step act with `σ_{i−1}σ_i` fixed in front, so
  `CtxAvoids L [σ_{i−1}] []` covers them;
- the **unshuffle** acts at `a = []`. Nothing sits in front of it to separate
  on, so what protects it is the word's right end instead:
  `CtxAvoids L [] [σ₀,σ₀,σ_i]` — no surrounding word ends in `σ₀σ₀σ_i`.

Cheap to discharge at the joining: side A's normal-form terms end in `σ₀` and
`σ₁` respectively, and the pattern ends in `σ_i` with `i ≥ 2`, so a last-letter
comparison settles both.

#### `bside_branch`'s length hypothesis is the wrong discharge at the joining

Within side B every word of the chain has the same length, so one length
condition served both steps — that is what §4bs shipped. It does **not**
separate A from B: A's normal form has *exactly* the lengths B's post-split
words do (`2i+2` and `2i+1`). So `bside_branch_core` now takes its two `≠`s
raw, and the caller assembles them from whatever it has. `bside_resolves'`
needs both shapes at once — head for the ambient terms, length for side B's
*own* other branch, which also begins with `σ_{i−1}` and so is invisible to the
head condition. `bside_branch` survives unchanged as the length instance.

New helpers: `CtxAvoids.ne_descWord` (a word opening with a descending run is
avoided by a context avoiding that run's head letter — the workhorse turning a
head condition into the plain `≠` a step lemma asks for), `bsWord₂_length`,
`mem_ctx_or_eq`.

**Trap, and it bites twice in adjacent lines.** `rw [descWord_length' h]` closes
its goal *by rfl* when the `Fin` literal reduces — so `rw [descWord_length'
honei]; simp` is a "No goals to be solved" error at `⟨1, hnn⟩`, while the
visually identical `rw [descWord_length' hz']; simp` at `⟨0, hn⟩` **needs** the
`simp`, because `i.val - 0 + 1` still has to lose its `- 0`. Same for
`simp only` closing a goal ahead of an `omega` that then has nothing to do.

### §4bw — `hdeep` DISCHARGED; the criterion is unconditional

```
'UGB.GrobnerShirshov.Hecke.heckeCompleted_isGrobnerShirshovBasis'
  depends on axioms: [propext, Classical.choice, Quot.sound]
```

No hypothesis, no `sorry`. The completed Hecke rewriting system is a
Gröbner–Shirshov basis, for every `n` and every `HeckeParams`.

The conditional form survives as `heckeCompleted_isGrobnerShirshovBasis_of_deep`
— everything above §4bw in the file depends only on it, and the two halves are
proved 1400 lines apart.

#### What the joining needed

1. **`selfOverlap_spoly_coeff`** — when both rules of an overlap composition are
   the *same* monic `L − R`, the two `L`-placements are the same word:
   `L ++ right = left ++ overlap ++ right = left ++ L`. They cancel, and the
   S-polynomial is `left · R − R · right`. Stated for any monic two-word rule,
   not just Bokut–Shiao.
2. **`deep_left_right`** — the contexts are forced. `σ_a σ_{a−1} ⋯ σ₀ σ_a` has
   exactly one border once `a ≥ 1`: a border of length `k ≥ 2` would need its
   first letter `σ_a` to equal the suffix's first letter `σ_{k−2}`, which holds
   only at `k = a+2`, the whole word — excluded by `left ≠ []`. So
   `left = descWord a 0` and `right = descWord (a−1) 0 ++ [σ_a]`, and the two
   S-polynomial terms are *exactly* side A's and side B's opening words.
3. **The two chains, sequentially** — A with B's word as its only ambient term,
   then B with A's two normal-form terms as its ambient. Four terms out, equal
   in pairs with opposite signs.

#### The collision I expected does not exist — the correction that unlocked it

I had assumed the joining would deadlock at its last step, because both sides
reach the same two monomials. Reading the definitions rather than reasoning
from the shape:

* **`isZero` is coefficientwise** (`∀ m, f.coeff m = 0`) and `ofTerms` *sums*
  over terms carrying a monomial. Two terms with the same word and opposite
  coefficients are the cancellation the S-polynomial needs, not a problem.
* **A step's side condition constrains the word it CONSUMES, never the word it
  produces.** `monicStep`'s `hne` is used only to prove
  `coeff (a ++ lm ++ b) = c`, i.e. that the step subtracts the right amount.

Both facts were sitting in `Elem.lean` and in `monicStep`'s own proof the whole
time. The design work of §4bt–§4bv — `CtxAvoids`, the head/tail conditions, the
raw side conditions on `bside_branch_core` — was still needed, but for the
*interiors* of the two chains, not for the collision I was bracing against.

#### The context conditions, discharged

| side | condition | discharged by |
|---|---|---|
| A | no ambient word begins `σ_a` | B's word begins `σ_{a−1}` |
| A | no ambient word begins `σ_{a−2}` | same |
| B | no ambient word begins `σ_{a−1}` | A's normal form begins `σ_{a−2}` |
| B | no ambient word ends `σ₀σ₀σ_a` | A's terms end `σ₀` and `σ₁`; `a ≥ 2` |

Each is one letter comparison. `ctxAvoids_head_of_ne` and
`ctxAvoids_tail_of_last_ne` are the two one-line bridges; the second had to be
generalised from "every ambient word ends in the same letter `x`" to "each ends
in *some* letter ≠ `y`", because A's two normal-form terms end in `σ₀` and `σ₁`
respectively.

`deep_selfOverlap_resolves` compiled first try once those were in place.
