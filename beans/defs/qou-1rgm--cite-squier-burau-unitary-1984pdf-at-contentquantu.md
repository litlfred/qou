---
# qou-1rgm
title: Cite squier-burau-unitary-1984.pdf at folio/quantum-observable-universe/information-theory/q-ga…
status: todo
pr: 8449
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:20Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

q-game-of-life-proof asserts generator unitarity with respect to the Markov trace form with no citation at all; the invariant-Hermitian-form result is the nearest published statement, and citing it will also force the block to say which form it means.

**From the source**
- Theorem (p. 199) and section 3 — There is a nonsingular matrix J_0 over Z[t,t^{-1}] with beta(w)* J_0 beta(w) = J_0 for all braid words; over Z[s,s^{-1}] (s^2 = t) a change of basis makes it Hermitian, and each generator acts as a unitary reflection.
  Use here: Supplies the standard invariant-form statement for the braid representation the corpus's Burau-at-i computation uses, and a citable anchor for the corpus's otherwise unsourced unitarity assertion.

Source: `library/squier-burau-unitary-1984/squier-burau-unitary-1984.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/squier-burau-unitary-1984/  ->  [squier1984]
  The Burau representation is unitary

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [squier1984] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8449, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

Not cited. Premise stale: q-game-of-life-proof.md now asserts invertibility, not unitarity, and that σ_i is not unitary for any inner product when q≠1 (correct for positive-definite forms at real q). Squier's result is unitarity for a bar-Hermitian indefinite form; citing it needs a new contrast sentence (owner's call). Finding F5. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
