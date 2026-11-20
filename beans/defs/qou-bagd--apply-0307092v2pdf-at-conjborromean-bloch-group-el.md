---
# qou-bagd
title: Apply 0307092v2.pdf at conj:borromean-bloch-group-element
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:45Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

Hypotheses checked: the theorem requires a complete, finite-volume hyperbolic 3-manifold; the Borromean rings complement satisfies all three. The existence and regulator clause of the conjecture is therefore a corollary, and the block should be re-scoped so that only the h^4 = -3/4 shadow claim remains conjectural. Scope note: this discharges clause 1 only and asserts nothing about clause 2.

**From the source**
- Sec. 1 (main results) + Sec. 14 — Any complete hyperbolic 3-manifold of finite volume carries a natural fundamental class in H_3(PSL(2,C); Z) determining an element betahat(M) in the extended Bloch group, and R o lambda computes the Cheeger--Chern--Simons class i(vol(M) + i cs(M)).
  Use here: Discharges the existence-and-regulator clause of conj:borromean-bloch-group-element for the Borromean complement, whose hypotheses are met; the residual open content is then only the h^4 = -3/4 shadow claim.

Source: `library/0307092v2/0307092v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/0307092v2/  ->  [neumann2004]
  Extended Bloch group and the Cheeger-Chern-Simons class

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [neumann2004] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8486, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
