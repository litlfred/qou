# `conditional_on_class` does not mean the block carries a class hypothesis

**Date:** 2026-09-03 · **Bean:** `qou-y3x4` · **Witness:**
[`2026-09-03-conditional-on-class-hypothesis.witness.json`](2026-09-03-conditional-on-class-hypothesis.witness.json) ·
**Script:** [`scripts/conditional-on-class-hypothesis-audit.ts`](../../scripts/conditional-on-class-hypothesis-audit.ts)

## The claim

`conjectural-propagation-audit.ts` reports two buckets, `violators` and
`conditional_on_class`. The second reads as "these blocks satisfy AGENTS.md
§3b-cond", i.e. are rigorous conditional results. **It does not check that,
and cannot** — the split is made on one test only:

```ts
// §3b-cond eligible iff every conjecture in cone is class-axiomatised
const allClassAxiomatised = [...conjAncestors].every((c) => classAxiomatised.has(c));
if (allClassAxiomatised) conditional.push(entry);
else violators.push(entry);
```

Every input to that test comes from the **conjecture carriers**. The
downstream block's own Lean file is never opened. §3b-cond has five
requirements and this is item 1; item 2 —

> **Explicit hypothesis on Lean side.** The downstream block's Lean
> declaration has the class as an explicit `[Instance]` hypothesis.

— is about the downstream block, and is unchecked by anything in the corpus.

## The measurement

Of **139** blocks the propagation audit reports `conditional_on_class`:

| | count |
|---|---|
| binds a class from its **own conjecture cone** | **9** |
| binds some other class/structure carrier | 72 |
| binds **no** carrier at all | **45** |
| `lean.ref` resolves to no declaration (separate defect) | 13 |
| file-level `variable` binds it (undecidable by regex) | 0 |

The 9 are `prop:crystal-r-matrix-sub-lemma`,
`prop:deuteron-binding-dressing-proton-net`,
`prop:operator-valued-combiner-convergence`,
`prop:proton-mass-substrate-identity`,
`prop:reeb-bundle-complement-equals-volume`, `prop:residue-at-root`,
`prop:vol-through-tau`, `thm:aomega-fourone-dt-count`,
`thm:confinement-grading-correspondence-conditional`.

## What the 45 is NOT

**It is a candidate set for hand triage, not a violation count.** A theorem
that is unconditionally true correctly binds nothing, and that is *better*
than a conditional one, not worse. Both blocks hand-checked from the bucket
are of exactly that kind:

- `lem:frobenius-cocasimir-refuted-deuteron` →
  `theorem coCasimir_refuted_deuteron : tol < |coCasimirSum - targetSigned|` —
  a concrete numeric **refutation**. It sits in a conjectural cone because it
  is *about* the ansatz, and needs no hypothesis to be true.
- `prop:alpha-k-derivation-procedure` →
  `theorem alpha_k_derivation_procedure {p} (A : Matrix …) [Invertible A] (b) :
  ∃! y, A *ᵥ y = b` — generic linear algebra, unconditionally true.

The second raises a *different* question worth separating: its Lean proves a
fact independent of the conjecture entirely, which is a
`proof-statement-integrity` concern (does the Lean derive the `.md` claim?)
rather than a §3b-cond one. No regex can settle either.

## Four narrowings, four overstatements — the methodological point

This script's failure count went **96 → 117 → 62 → 49 → 45**. Every
correction was downward, and **not one was caught by the number looking
wrong** — each came from opening a named member of the failure bucket:

1. testing for a bare `[` missed `(sp : ArchimedeanSubstrateField M)`
   (`prop:boltzmann-constant`). An **explicit** binder carries the hypothesis
   identically; the instance bracket is an elaboration convenience, not an
   epistemic difference, and §3b-cond's "[Instance]" wording must not be read
   as excluding it.
2. requiring a **cone** class missed `[ctx : B1Figure8RowContext]`
   (`prop:b1-figure-8-row-theorem`) — a locally-minted context class is a
   different defect (item 5: does it carry genuine sub-hypotheses, or the
   conclusion as a field?), not an unconditional statement.
3. matching `class` alone missed `(S : BodyOrderJetGrading)`
   (`lem:bond-order-eq-jet-degree`) — a `structure` binds identically.
4. matching same-file declarations only missed `(amphi : Amphicheiral …)`
   (`cor:knot-factor-amphicheiral`), whose carrier is declared upstream.

Each narrowing of a name-shaped detector **inflates the count of things it
claims to have found.** This is row 27 of the detector-blindness taxonomy in
kind, and the fourth-generation figure is still only a bound.

## Consequence for the b1 conversion — and why it was NOT done here

All 7 remaining *tractable* violators (the other 17 are permanently blocked by
`conj:magic-numbers-from-q`, which must not be class-axiomatised) share one
blocker: `conj:b1-hyperbolic-rows-theorem`. Its library file states the
conjecture as `axiom b1_holds_at_row` and **derives** the count from it — good
work, and the blast radius of changing it is two files.

Converting that `axiom` to a `class` is independently right: a global `axiom`
pollutes `#print axioms` for every downstream statement unconditionally, while
a class is carried explicitly. **But doing it now would move 7 blocks from
`violators` to `conditional_on_class` without any of the 7 acquiring a class
hypothesis**, because the audit does not check for one. The count would
improve 24 → 17 and nothing about those 7 blocks would have changed.

That is the laundering shape §"Axiomatization is NOT a Proof" warns about, so
the conversion is deliberately **not** in this PR. It should land together
with the seven downstream Lean statements actually taking the hypothesis, or
not at all.

## What would close the gap properly

Fold this check into `conjectural-propagation-audit.ts` so that
`conditional_on_class` requires items 1 **and** 2, and report a third bucket
for blocks that pass item 1 and fail item 2. That is a folio-assistant change
and is not made here.
