---
# qou-afzu
title: Cite 1511.00400v2.pdf at folio/quantum-observable-universe/lean/QOU/OneLoopEdgeLattice.lean (--…
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:12Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

OneLoopEdgeLattice.lean names the change-of-curve law as one of its validation criteria and carries only a dimofte-garoufalidis2013 -- Ref:; §5.1 here is the source for that law.

Source: `library/arxiv-1511.00400v2/1511.00400v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1511.00400v2/  ->  [porti2015]
  Reidemeister torsion, hyperbolic three-manifolds, and character varieties

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [porti2015] as the citation key when you do it.

## 2026-11-21 — expo-cite-xcheck drain

`Ref: [porti2015] §5.1 prop:change` added to OneLoopEdgeLattice.lean (change-of-curve law checked in the held text). Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.

## 2026-11-21: merged

Completed: PR #8852 merged (merge 4d8767a1c).
