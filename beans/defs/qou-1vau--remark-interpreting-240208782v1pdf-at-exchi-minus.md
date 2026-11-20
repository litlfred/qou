---
# qou-1vau
title: Remark interpreting 2402.08782v1.pdf at ex:chi-minus-six-derivation
status: todo
pr: 8449
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:27Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-aqfj
---

The {5,4} map's V - E + F = 30 - 60 + 24 = -6 is an independent arithmetic confirmation of the chi = -6 ledger that the chi-chain derives categorically; worth a remark, and worth stating explicitly that it is a consistency cross-check, not a second derivation of the branch-point count.

**From the source**
- Thm. 3.2 — Bring's surface is the compactification of H / H_4(5) for the Hecke group H_4 = C_2 * C_4 over Z[sqrt 2], of index 120, carrying the regular map of type {5,4} with 30 vertices, 60 edges and 24 faces, together with the 20-sided polygon and its side pairings.
  Use here: Gives def:brings-surface and rem:brings-realisations the hyperbolic/uniformization description they lack, and supplies an independent Euler count 30 - 60 + 24 = -6 for the chi = -6 ledger that ex:chi-minus-six-derivation currently derives only from the Frobenius-Hopf six-branch-point argument.

Source: `library/arxiv-2402.08782v1/2402.08782v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2402.08782v1/  ->  [kattan2024]
  Hecke–Farey coordinates for Bring’s surface

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [kattan2024] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8449, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
