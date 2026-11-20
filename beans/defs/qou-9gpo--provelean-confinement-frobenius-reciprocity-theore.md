---
# qou-9gpo
title: 'PROVE(lean): confinement_frobenius_reciprocity — theorem confinement_frobenius_reciprocity [ctx : ConfinementFrobeniusReciprocityContext] : [cited bertsimas1997,manuscript]'
status: todo
type: task
priority: normal
tags:
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-bertsimas1997
    - reorg-2026-10-04
    - lean
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean

### `confinement_frobenius_reciprocity`  —  line 107  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem confinement_frobenius_reciprocity [ctx : ConfinementFrobeniusReciprocityContext] : (∀ O : ctx.Observable, ctx.physExp O = ∑ i ∈ ctx.A_star, ∑ j ∈ ctx.A_star, ctx.u_star i * ctx.Ginv i j * ctx.pairing O j) ∧ (∃ i : Fin ctx.d, ctx.x_star i ≠ 0) ∧ 0 < ctx.y_0_star ∧ ctx.A_star.Nonempty ∧ (∀ i :`
- **Cited:** `[bertsimas1997]`, `[manuscript]`, `[bertsimas1997]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md
- **Tractability:** physExp = Σ shadow-price·Ginv·pairing + nonempty active set; LP duality (active set = positive duals) Mathlib lacks.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.


## RE-TRIAGED 2026-08-31 — NOT INFRA-BLOCKED — the class carries the conclusion

The `Next step` line above ("Infra-blocked: needs Mathlib theory that does not exist. Track
upstream") is one verdict that was stamped on fourteen beans in six seconds, and is wrong here.
Full audit: `docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md`.

`confinement_frobenius_reciprocity`'s proof is
`<ctx.reciprocity, ctx.primal_nontrivial, ctx.y_0_star_pos, ctx.A_star_nonempty, ...>` --
six conjuncts, six class fields, the first of which is literally named `reciprocity`. That is
AGENTS.md section-3b-cond rule 5's conclusion-carrier, not a missing LP-duality library.

Belongs to the qou-z9ws self-assuming drain. Note it is MISSED by
scripts/lean-self-assuming-audit.py: that tool needs the whole proof term to be a single
identifier, so a conjunctive `<...>` of projections never matches.

The original text is kept above, not deleted: the Tractability line is per-item and is accurate;
only the Next-step verdict is being corrected.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8308, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
