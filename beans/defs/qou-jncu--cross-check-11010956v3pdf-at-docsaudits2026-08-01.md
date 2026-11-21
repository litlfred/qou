---
# qou-jncu
title: Cross-check 1101.0956v3.pdf at docs/audits/2026-08-01-em-linking-reads-round1.md
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:03Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-8hur
---

Re-upload request, not a computation: the corpus wants arXiv:0901.1612 (announcement) and arXiv:1207.1793 (Part 2, Euclidean case) for the generalized-Gauss-maps / triple-linking material, per the re-upload list already recorded in the round-1 audit. Flagging it here so the ledger row and the audit's re-upload list stay joined.

Source: `library/arxiv-1101.0956v3/1101.0956v3.pdf` — no `references.ts` entry yet
Relevance: **not-relevant** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1101.0956v3/  ->  [arcus2011]
  Algebraic constructions in the category of vector bundles

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arcus2011] as the citation key when you do it.

## 2026-11-21 — expo-cite-xcheck drain

Re-upload request still open (arXiv:0901.1612, 1207.1793); no computation. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
