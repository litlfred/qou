---
# qou-tcgv
title: Cite [kirillov1995] at def:quantum-bloch-group
status: todo
pr: 8404
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:54Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1qhv
---

def:quantum-bloch-group displays the Phi_q pentagon identity and its .ts has no cites field whatsoever, while Sec. 2.5 Prop. 2 / Cor. 11 of an already-registered reference is the source for exactly that identity.

**From the source**
- Sec. 2.5, Definition 9, Proposition 2 and Corollary 11 — The quantum dilogarithm Li_2(x;q) = sum x^n/(n(1-q^n)) satisfies functional equations under ab = qba and a five-term relation in the form H(Li_2(a;q), Li_2(b;q)) = H(Li_2(b;q), H(Li_2(-ba;q), Li_2(a;q))).
  Use here: The direct source for the pentagon/five-term identity that def:quantum-bloch-group displays with no citation, and the correct locator for the corpus's q-dilogarithm reference (currently pointed at Sec. 2.1, which is about partitions).

Source: `library/arxiv-hep-th-9408113v2/9408113v2.pdf` (`kirillov1995`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

In-progress in PR #8404 (`feat/qou-t8mi-tcgv-tiwv-u33z-u8cp-round68`, `QOU.QBeta.PoincareFalseThetaDilogPentagonRound68`, 80-dps probe `round68_poincare_false_theta_dilog_pentagon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8404, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
