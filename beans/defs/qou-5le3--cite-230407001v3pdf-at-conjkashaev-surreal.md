---
# qou-5le3
title: Cite 2304.07001v3.pdf at conj:kashaev-surreal
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:24Z
updated_at: 2026-11-21T13:32:29Z
pr: 8315
parent: qou-ysb7
---

conj:kashaev-surreal can name Cor 1.5 (T(2,2u+1), T(3,2k)) as the proved cases of the resummation half of its statement.

**From the source**
- Cor 1.5 (p. 6), via Thm 1.4 (eq. 1.22) — The Costin-Garoufalidis Conjecture 1.1 holds for the torus-knot families T(2,2u+1) and T(3,2k); specialising u = 1 or k = 1 recovers the trefoil.
  Use here: conj:kashaev-surreal asserts that st applied to the Kashaev transseries is its median resummation, i.e. the asymptotic content of the volume conjecture in resummation form. Cor 1.5 gives the first proved knot families in which the resummation half of that statement holds, so the conjecture can name its verified cases rather than standing entirely unanchored.

Source: `library/arxiv-2304.07001v3/2304.07001v3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2304.07001v3/  ->  [crew2023]
  RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [crew2023] as the citation key when you do it.

### Progress (Round 60)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8315 (`bfd875bed8570b98aa208b007cb51288416e1d03`). Status kept `in-progress` pending PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8315, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

conj:kashaev-surreal now cites crew2023 Conj. 1.1, Cor. 1.5. Correction: the source's second family is T(3,2^k) (exponent; see its eq. (3.19)), not T(3,2k) as this bean says.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
