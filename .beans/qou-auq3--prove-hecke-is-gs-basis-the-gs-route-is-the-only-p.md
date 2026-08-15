---
# qou-auq3
title: Prove hecke_is_gs_basis — the GS route is the only path from n<=4 to general n
status: in-progress
type: task
created_at: 2026-08-09T16:10:13Z
updated_at: 2026-08-15T12:50:00Z
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
