---
# qou-y3x4
title: '§3b-cond rule 2 is unchecked: conditional_on_class opens no downstream Lean'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T21:13:23Z
updated_at: 2026-10-04T15:14:29Z
parent: qou-5p7n
---

## What is unchecked

`conjectural-propagation-audit.ts` splits provable blocks into `violators` and
`conditional_on_class` on ONE test — is every conjecture in the block's cone
carried by a Lean `class` (§3b-cond item 1). Every input comes from the
CONJECTURE carriers; the downstream block's own Lean file is never opened.
So item 2 — "the downstream block's Lean declaration has the class as an
explicit [Instance] hypothesis" — is unchecked by anything in the corpus.

Sibling defect, different rule: `cnd4` covers item 4 (`uses[]` declaring the
dependency). This is item 2 (the Lean-side hypothesis). Do not merge them.

## Measured 2026-09-03 (139 conditional_on_class blocks)

    binds a class from its OWN conjecture cone       9
    binds some other class/structure carrier        72
    binds NO carrier at all                         45
    lean.ref resolves to no declaration             13   (separate defect)
    file-level `variable` binds it (undecidable)     0

Script `scripts/conditional-on-class-hypothesis-audit.ts`, witness
`docs/audits/2026-09-03-conditional-on-class-hypothesis.witness.json`, writeup
`docs/audits/2026-09-03-conditional-on-class-item2-unchecked.md`.

Sanity check that passes: `thm:aomega-fourone-dt-count`, whose authorNote
claims §3b-cond compliance, is among the 9.

## The 45 is a CANDIDATE SET, not a violation count

An unconditionally true theorem correctly binds nothing, and that is better
than a conditional one. Both hand-checked members are exactly that:
`coCasimir_refuted_deuteron : tol < |coCasimirSum - targetSigned|` (a numeric
refutation) and `alpha_k_derivation_procedure` (`∃! y, A *ᵥ y = b` for
invertible A — generic linear algebra). The second is a
proof-statement-integrity question instead: its Lean proves a fact
independent of the conjecture.

## The methodological finding, worth more than the number

Failure count went 96 -> 117 -> 62 -> 49 -> 45. Every correction downward,
and NOT ONE caught by the number looking wrong — each came from opening a
named member of the bucket:

  1. bare `[` missed `(sp : ArchimedeanSubstrateField M)` (boltzmann-constant)
  2. requiring a CONE class missed `[ctx : B1Figure8RowContext]` (b1-figure-8)
  3. `class` alone missed `(S : BodyOrderJetGrading)` (bond-order-eq-jet-degree)
  4. same-file only missed `(amphi : Amphicheiral ...)` (knot-factor-amphicheiral)

Every narrowing of a name-shaped detector inflates the count it claims to have
found. Treat 45 as a bound.

## Next, and the trap in it

All 7 remaining TRACTABLE violators share one blocker,
`conj:b1-hyperbolic-rows-theorem` (the other 17 are permanently blocked by
`conj:magic-numbers-from-q`, which must NOT be class-axiomatised — its own
scope refutes its former title). Its library file states the conjecture as
`axiom b1_holds_at_row`; converting that to a class is independently right and
the blast radius is 2 files.

DO NOT do it alone. It would move 7 blocks to conditional_on_class without any
of them acquiring a hypothesis, because the audit does not look — 24 -> 17
with nothing about those blocks changed. Land it together with the 7
downstream statements taking the hypothesis, or not at all.

Proper fix: fold this check into `conjectural-propagation-audit.ts` so that
`conditional_on_class` requires items 1 AND 2, with a third bucket for
item-1-pass / item-2-fail. That is a folio-assistant change.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 89 Formalization (`litlfred/qou#8474`)
- Formalized in `QOU.Foundations.AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild` (`folio/quantum-observable-universe/lean/QOU/Foundations/AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`849ef0b15f72606c848eb897a5fda003d289f504` -> `2fff5cb2db76633d952c403baec2a6519c2cf61d`, `scriptHash = scriptSha256 = 2a824ebc8929957fb1b4acfb6fc295d57631c4e806a1217ab45cd79c79b1902b`).
- PR: https://github.com/litlfred/qou/pull/8474
