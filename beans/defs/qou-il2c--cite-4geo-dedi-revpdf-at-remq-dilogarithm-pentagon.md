---
# qou-il2c
title: Cite 4GEO-DEDI-REV.pdf at rem:q-dilogarithm-pentagon-associator
status: in-progress
pr: 8355
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:15Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-ysb7
---

rem:q-dilogarithm-pentagon-associator equates the quantum dilogarithm with the 6j-symbol without a source for that identification.

**From the source**
- Sect. 1 (Introduction, item on elementary intertwiners) — The elementary intertwiners associated to diagonal exchanges between ideal triangulations are identified with the Kashaev 6j-symbols.
  Use here: Sources the parenthetical 'equivalently the 6j-symbol' in rem:q-dilogarithm-pentagon-associator's claim that the quantum dilogarithm is the quantum associator, which is currently asserted with only faddeev_kashaev1994 behind it.

Source: `library/4geo-dedi-rev/4GEO-DEDI-REV.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/4geo-dedi-rev/  ->  [baseilhac-benedetti-fibred]
  On the quantum Teichmüller invariants of fibred cusped 3-manifolds

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [baseilhac-benedetti-fibred] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8355, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:q-dilogarithm-pentagon-associator now cites baseilhac-benedetti-fibred §1 for the intertwiner = Kashaev 6j identification, recorded as attributed by that source to earlier work.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
