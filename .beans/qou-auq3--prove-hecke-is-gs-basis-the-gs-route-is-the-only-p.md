---
# qou-auq3
title: Prove hecke_is_gs_basis — the GS route is the only path from n<=4 to general n
status: todo
type: task
created_at: 2026-08-09T16:10:13Z
updated_at: 2026-08-09T16:10:13Z
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

* **The general leading monomial.** `lm (bokutShiaoRelation i' i j) = bsWord₁ i j`.
  The one lemma it needs is **`descWord i j = ⟨i⟩ :: descWord i' j`** (for
  `i' + 1 = i`, `j ≤ i'`) — dropping the top index drops the first letter. With
  it, *no length computation is needed at all*: the two words become
  `⟨i⟩ :: (descWord i' j ++ [⟨i⟩])` and `⟨i'⟩ :: ⟨i⟩ :: descWord i' j`, visibly
  the same length, and the lex comparison is one `List.Lex.rel` on the first
  letters. (An earlier note here said the missing piece was the *length*
  `(descWord i j).length = i − j + 1`; the cons lemma is both easier and
  strictly more useful.) It is a statement about `List.finRange n` being sorted.
  Until it exists there is no `heckeCompletedRewritingSystem_lm_cases`, hence no
  analogue of §4e's irreducibility machinery for the completed system.
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
