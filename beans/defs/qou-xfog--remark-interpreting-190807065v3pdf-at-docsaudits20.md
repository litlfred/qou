---
# qou-xfog
title: Remark interpreting 1908.07065v3.pdf at docs/audits/2026-07-12-alien-calculus-review-binding-gevr…
status: in-progress
pr: 8435
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:10Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-vva9
---

Record the technique and, importantly, the reason it does not apply as-is: the corpus's binding period is Gevrey-1/2 with entire level-1 Borel transform and is not q-holonomic, so the exact-WKB/TBA machinery has no established hook. Writing that down prevents a later agent re-proposing the route as though it were available.

**From the source**
- Sect. 3 (Quantum periods from TBA equations) — The resurgent properties of the all-orders WKB periods are encoded in Gaiotto-Moore-Neitzke TBA equations determined by the BPS spectrum, and are solved explicitly in the strong-coupling region.
  Use here: A concrete mechanism for locating Borel singularities of a quantum period from a BPS spectrum, which is exactly the open target the alien-calculus audit names. What would need checking first: whether the corpus's binding period is a period of a quantum curve at all, given the audit's own finding that its level-1 Borel transform is entire.

Source: `library/arxiv-1908.07065v3/1908.07065v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-ghy5): this says 'no references.ts entry yet'.
There is one — the document is registered as **grassi-gu-marino2019qsw**
('Non-perturbative approaches to the quantum Seiberg-Witten curve', Grassi,
Gu, Marino). It was registered under the machine-fallback id
`arxiv-1908.07065v3` with no authors, because JHEP welds the affiliation
letter to each surname ('Alba Grassia, Jie Gu b and Marcos Marinob') and the
parse failed; nothing cited that id while a Lean proof cited
`grassi-gu-marino2019qsw`, which resolved to nothing. Renamed to the key in
use, authors filled from the byline.

Not closing this — it is not mine to close, and the technique note above is
separate from the reference existing.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1908.07065v3/  ->  [grassi-gu-marino2019qsw]
  Non-perturbative approaches to the quantum Seiberg–Witten curve

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [grassi-gu-marino2019qsw] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8435, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md Addendum 6: grassi-gu-marino2019qsw §3 recorded with the reason it has no hook (Gevrey-1/2, entire level-1 Borel, not q-holonomic).

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
