---
# qou-dvqx
title: Cite 0401068v1 (1).pdf at prop:phi-q-aj-machinery-identification
status: completed
pr: 8347
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:44Z
updated_at: 2026-11-21T13:32:29Z
parent: qou-ysb7
---

Separate finding surfaced by this read: le2006 already exists in references.ts, proves AJ for all twist knots, and is cited by NO block — while prop:phi-q-aj-machinery-identification carries AJ as an unsourced conditional-class input. The right fix is to cite le2006 there.

**From the source**
- Thm 2.2 and §4 — Setting q = 1 in the summand recurrences and solving f_0 = l, f_1 = f_2 = 1 recovers a polynomial B_{K_p}(l,m) equal to the A-polynomial A_{K_p}(l,m); §4 additionally derives the A-polynomials of 5_2 and 6_1 from explicit colored-Jones recursions.
  Use here: Concrete worked instances of the classical limit of the AJ machinery that prop:phi-q-aj-machinery-identification describes abstractly. Weaker than le2006, so the honest action is to cite le2006 at that block and keep this as the explicit-computation companion.

Source: `library/arxiv-math-0401068v1/0401068v1 (1).pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0401068v1/  ->  [takata2004]
  THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [takata2004] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8347, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

prop:phi-q-aj-machinery-identification now cites takata2004 Thm 2.2 and §4 (5_2, 6_1 recorded as a computer-algebra observation, as the source says). le2006 NOT cited: no library copy, so its hypotheses could not be checked; left for cite-intake.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
