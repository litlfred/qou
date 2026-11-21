---
# qou-r6ki
title: Cite 0006156v1.pdf at prop:faddeev-phib-uniqueness
status: in-progress
pr: 8397
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:59Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-ysb7
---

prop:faddeev-phib-uniqueness currently cites only faddeev1995 + faddeev1994 while stating the product formula and the strip-growth hypothesis that this paper's eqs. (21)-(22) give explicitly.

**From the source**
- Sect. 6.2, eq. (21) — e_b(z) equals a ratio of two q-exponentials with q = e^{i pi b^2} and qbar = e^{-i pi b^{-2}}, defining a meromorphic function on all of C with an explicit zero/pole lattice.
  Use here: Primary source for the modular-double product that prop:faddeev-phib-uniqueness writes verbatim as its Phi_b, and for the meromorphy + isolated-zeros facts that block currently establishes by hand.
- Sect. 6.2, eq. (22) — Four-sector asymptotic behaviour of e_b(z) as |z| -> infinity, with Gaussian, theta-function and constant regimes selected by arg(z) relative to arg(b).
  Use here: The sector-wise growth input behind prop:faddeev-phib-uniqueness's 'strip growth' hypothesis; applicable on that block's branch Im b^2 > 0 (arg b = pi/4), so it can replace the block's elementary product-norm bound with a literature statement.

Source: `library/arxiv-hep-th-0006156v1/0006156v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-0006156v1/  ->  [faddeev-kashaev-volkov2000]
  Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [faddeev-kashaev-volkov2000] as the citation key when you do it.

In-progress in PR #8397 (`feat/qou-r6ki-sf0s-spds-ssly-t579-round67`, `QOU.QBeta.ModularDoubleSkeinRibbonRound67`, 80-dps probe `round67_modular_double_skein_ribbon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8397, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

prop:faddeev-phib-uniqueness: section citing faddeev-kashaev-volkov2000 §6.2 eqs. (21)-(22).

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
