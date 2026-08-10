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

## Outcome for the 9: disclosure, NOT axiom conversion

Recipe 3 ("make it a cited `axiom`") was the intended fix here and it is
**unsound for all nine.** Every one projects off an abstract class whose data
is arbitrary — `RMatrixBraidingContext` (`comp`, `R12`, `R13`, `R23`),
`LevelSufficient P P' q`, `QOneShadowGateClass c2 c3`,
`BarEvenKernel pole c2 c3 magnitude`, `CosimplicialCrossedGroupoid M`. A
global `axiom` over such a context asserts the property for **every**
assignment of that data, and YBE (or a trace equality, or a `q = 1` shadow) is
plainly false for a general one. Converting would have replaced an invisible
but *true* hypothesis with a visible and *false* axiom — the §9
"cited `sorry` on a false statement" defect, in axiom form.

Recipe 3 applies when the content is a genuine external input **about fixed
objects**. It does not apply to a property of arbitrary context data. Where
the class is the honest carrier, the fix is criterion (1): say so.

Applied, `lean`-direct exit 0 on each:

| declaration | fix |
|---|---|
| `braids-and-knots/r-matrix-braiding-structure.lean` ×2 | disclosure added; notes YBE fails for general context data, so no `axiom` |
| `lean/QOU/Braiding/r_matrix_braiding_structure.lean` | same (the library copy) |
| `lean/QOU/BraidKnot/LevelSufficiency.lean` | disclosure; Jones cited for the theory, not for a proof performed here |
| `mass-theory/q-beta-q-eq-one-shadow-gate.lean` | disclosure; "routine restatement" made exact |
| `mass-theory/q-beta-bar-even-kernel-typeclass.lean` | disclosure; "from the bundle" ⇒ *projected from* it |
| `mass-endomorphism/conj-qbeta-c-k-closed-forms.lean` | **different defect** — see below |

**Three were false positives of the disclosure regex**, which is why the
24/28 split above is a measurement and not a census:

- `ccg_cosimplicial_identities` — already discloses, in wording the regex did
  not match ("packages the level-based fragment that is immediately
  discharged from the structure", plus what a full statement would require).
- `ccg_crossed_module_structure` — discloses *and* does not project a
  conclusion: `⟨ccg.crossedMod n⟩` genuinely constructs
  `Nonempty CrossedModule` from a data field.
- `qbeta_c_k_closed_forms_derived` — discloses openness correctly but
  described the wrong mechanism: the docstring said the `sorry` is honest
  "open" and **there is no `sorry`**; the body projects two class fields.
  That is `proof-docstring-sorry-mismatch` (§8), where prose and
  `#print axioms` disagree about whether a proof exists. Docstring corrected
  to describe what the code does; the openness is real and comes from nothing
  inhabiting the class.

So of the 9, six needed the disclosure fix, two were already honest, and one
was a mislabelled instance of a different defect.

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

## Outcome (2026-08-09, owner-authorised)

Steps 3 and 4 were both authorised. Step 2 was already executed — see
§"Outcome for the 9" above: disclosure, **not** axiom conversion.

### Step 4 applied: `isDefProof` narrowed

The branch no longer overrides a `CONCLUSION_FIELD` name-gate match:

```ts
const nameGateMatched = !!field && CONCLUSION_FIELD.test(field);
if ((isDefProof && !nameGateMatched) || pat === "applied-tuple-projection") {
```

Measured before/after on the full corpus (2765 `.lean`):

| | before | after |
|---|---:|---:|
| non-exempt `proof-no-self-assuming-projection` | 56 | **94** |
| exempt | 162 | **124** |

**38 declarations flipped exempt → non-exempt** and are seeded into the review
ledger as `needs-agent`, so `--check-ledger` exits 1 again. That is the gate
working — the same posture as PR #4882 §3, not a regression. Drain tracked in
bean `qou-nbz9`, which carries the full list.

### Step 3 re-measured, then beaned rather than swept

Before writing the disclosure sentences the classification was recomputed, and
**the "19" turned out to be an artifact of scope**. The original measurement
covered only the 52 §3b-exempt declarations. Re-running the same disclosure
test across **all 147** `proof-no-self-assuming-projection` hits (exempt *and*
non-exempt):

| class | count |
|---|---:|
| discloses — premise holds | 22 |
| asserts `**Theorem/Proposition**`, no disclosure | 3 |
| literature-cited, no disclosure | 24 |
| bare, no disclosure | 98 |

**125 of 147 (85%)** carry no disclosure — not 19. The §3b subset discloses at
24/52 ≈ 46% against 22/147 ≈ 15% corpus-wide, which is unsurprising: that
subset was carved out partly *because* it disclosed. Quoting 19 as the size of
the disclosure backlog understates it by roughly 6×.

Tracked as epic `qou-5p7n` with four children, split by class and by current
exempt status, rather than applied as one sweep:

| bean | scope | priority |
|---|---|---|
| `qou-ajfl` | 3 asserting `**Theorem/Proposition**` (all non-exempt) | high |
| `qou-hxzl` | 24 literature-cited (5 non-exempt, 19 exempt) | high |
| `qou-bvo3` | 20 bare + non-exempt — live scanner defects | normal |
| `qou-pqmw` | 78 bare + exempt — tracked, triage pending | low |

`qou-hxzl` carries the standing warning that these must **not** be
bulk-converted to cited `axiom`s, with the unsoundness argument from
§"Outcome for the 9".

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
