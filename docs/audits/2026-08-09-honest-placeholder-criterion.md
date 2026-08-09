# The honest-placeholder criterion, and the 52 §3b exemptions measured against it

**Date:** 2026-08-09
**Companion to:** [`2026-08-09-self-assuming-projection-reanalysis.md`](2026-08-09-self-assuming-projection-reanalysis.md)
**Subject:** the `canonical §3b placeholder projection (tracked; derivation pending)` exemption in
[`content/pipeline/lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)

## Why this document exists

The scanner exempts a class of self-assuming projections and says so plainly
in its own source, reserving the decision it is deferring:

> Newly-covered patterns … are the acknowledged §3b placeholder-canonical
> projections **whose docstrings honestly state the content is carried by the
> context-class axioms with derivation pending** … Promoting these to a hard
> failure — **once the honest-placeholder vs. dishonest-dodge line is
> codified** — is a deliberate follow-up, not a silent side effect.

That comment states a **premise** ("whose docstrings honestly state…") and
defers a **criterion**. This document supplies the criterion and, more
usefully, measures the premise. It does not change any code.

## The criterion

A §3b placeholder projection — a declaration whose body returns a
context-class field verbatim, with no derivation — is **honest** when all four
hold:

1. **Disclosure.** The docstring states that the substantive content is
   carried by the context-class axiom(s) and that a derivation is pending.
   This is the scanner's own stated premise, and it is the load-bearing one:
   a reader who stops at the docstring must not come away believing a proof
   happened.
2. **No assertion of establishment.** The docstring does not present the
   statement as settled — no bare `**Theorem**` / `**Proposition**` framing
   without the disclosure of (1).
3. **Citations point at the claim's provenance, not at its proof.** A
   literature `-- Ref:` on an *assumed* statement is the most misleading
   configuration available: it makes an axiom read as a result imported from
   a named source. Where the cited theorem really does establish the
   statement, the honest form is not a class field at all — it is an
   `axiom` with that `-- Ref:` (fix recipe 3), which downstream consumers
   *consume* rather than re-assume.
4. **Downstream consumers carry the conditionality** as an explicit
   hypothesis rather than treating the projection as an established lemma.

Failing (1) is a **dishonest dodge**: the exemption's justification is absent,
so the exemption does not apply and the candidate should be triaged like any
other self-assuming projection.

The criterion deliberately says nothing about whether the *mathematics* is
open. An open claim honestly labelled is fine; that is what §3b is for. The
defect is the mismatch between what the prose implies and what the Lean does.

## Measuring the premise: 52 exemptions

| | count |
|---|---:|
| total `canonical §3b placeholder` exemptions | **52** |
| docstring **does** disclose class-carried / derivation pending — premise holds | **24** |
| docstring does **not** disclose it — **premise fails** | **28** |

So the exemption's own stated justification is absent for **54%** of the
declarations it exempts. Breaking down the 28:

| subclass | count | why it matters |
|---|---:|---|
| cites **literature** while assuming the statement | **9** | worst case — criterion (3) |
| asserts `**Theorem/Proposition/Lemma**`, no disclosure | 3 | criterion (2) |
| bare statement, no disclosure, no citation | 16 | criterion (1) |

### The 9 literature-cited-but-assumed

These read as results imported from the literature and are in fact class
axioms. Worked example —
[`r-matrix-braiding-structure.lean:75`](../../content/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.lean):

```lean
/-- **Yang–Baxter equation for the universal `R`-matrix**
    ([`prop:r-matrix-braiding-structure`]).
    `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
-- Ref: [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
def r_matrix_braiding_structure [ctx : RMatrixBraidingContext] :
    ctx.comp (ctx.comp ctx.R12 ctx.R13) ctx.R23
      = ctx.comp (ctx.comp ctx.R23 ctx.R13) ctx.R12 :=
  ctx.claim_yang_baxter
```

Nothing here is false, and YBE for the universal `R`-matrix is of course a
real theorem of Drinfeld's. But the declaration does not prove it, import it,
or say that it assumes it — the citations sit directly above a projection of
`claim_yang_baxter`. Under criterion (3) the honest form is an `axiom` with
these same `-- Ref:`s.

The full list:

| file | decl |
|---|---|
| `braids-and-knots/r-matrix-braiding-structure.lean:75` | `r_matrix_braiding_structure` |
| `braids-and-knots/r-matrix-braiding-structure.lean:90` | `braid_rep_from_R_check` |
| `lean/QOU/BraidKnot/LevelSufficiency.lean:104` | `LevelSufficiency` |
| `lean/QOU/Braiding/r_matrix_braiding_structure.lean:50` | `r_matrix_braiding_structure` |
| `lifting-and-descent/ccg-cosimplicial-identities.lean:43` | `ccg_cosimplicial_identities` |
| `lifting-and-descent/ccg-crossed-module-structure.lean:35` | `ccg_crossed_module_structure` |
| `mass-endomorphism/conj-qbeta-c-k-closed-forms.lean:120` | `qbeta_c_k_closed_forms_derived` |
| `mass-theory/q-beta-bar-even-kernel-typeclass.lean:115` | `bar_even_kernel_implies_q_one_shadow` |
| `mass-theory/q-beta-q-eq-one-shadow-gate.lean:79` | `qbeta_q_eq_one_shadow_anchors` |

## A structural point: the `def` exemption is broader than the name gate

`detectSelfAssuming` tests the `CONCLUSION_FIELD` name gate **before** the
§3b branch, but the §3b branch fires unconditionally on `isDefProof`. So a
Prop-valued `def` whose projected field is named `claim_*` — a field name the
name gate matches, i.e. a case the scanner would otherwise report as a
non-exempt defect — is exempted anyway. Both worked examples above are exactly
this: `ctx.claim_yang_baxter`, `ctx.claim_pslq_independence`.

This is not a regression (before PR #3363 a Prop-valued `def` was not scanned
at all), but it means the §3b exemption currently **swallows the strongest
signal the detector has**. 22 of the 52 are `field-projection`s, and the
`claim_`-named ones among them are in that category.

## Recommendation

Split the exemption rather than promoting or keeping it wholesale:

1. **The 24 that disclose** — keep exempt, tracked. They are doing what §3b is
   for.
2. **The 9 literature-cited** — convert to `axiom` + the existing `-- Ref:`
   (fix recipe 3), or add the disclosure. This is the cheapest real
   improvement in the set: it changes no mathematics and removes the
   "proved-from-Drinfeld" reading.
3. **The 3 + 16 remaining** — add the disclosure sentence, which moves them
   into class 1, or triage them as ordinary self-assuming projections.
4. **Narrow the `isDefProof` branch** so it does not override a
   `CONCLUSION_FIELD` name-gate match. A `def` projecting `claim_*` should be
   reported, not exempted.

Steps 2 and 4 change what the corpus asserts and what CI reports respectively,
so both are owner calls. Step 3 is editorial and could proceed without one.

## Method

Counts are from
[`scripts/lean-self-assuming-typematch-scan.mjs`](../../scripts/lean-self-assuming-typematch-scan.mjs)
and the scanner witness; the disclosure test is a docstring regex over the
block above each flagged declaration (`context-class axiom`, `carried by the
context`, `derivation … pending`, `placeholder`, `§3b`, …), the literature
test counts non-`[manuscript]` `-- Ref:` lines in the same block. Both were
hand-verified on the two worked examples above plus `jp_categorical_jet`
(which discloses correctly, and is counted in the 24). The regex will
misclassify a docstring that discloses in wording it does not match; treat the
24/28 split as a measurement with that caveat, not an exact census.
