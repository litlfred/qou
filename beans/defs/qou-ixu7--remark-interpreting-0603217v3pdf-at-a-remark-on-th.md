---
# qou-ixu7
title: Remark interpreting 0603217v3.pdf at a remark on the polarization convention attached to conj:bin…
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:51Z
updated_at: 2026-11-24T13:03:54Z
parent: qou-aqfj
---

The Gukov-vs-Murakami polarization difference at Re(u) != 0 is a real risk to the sign-flip conclusion and is not recorded anywhere in the corpus. Proposing new-remark rather than aid-proof: I have not checked which polarization the corpus's V_41 series actually realises, so this flags a check, it does not close one.

Source: `library/arxiv-math-0603217v3/0603217v3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0603217v3/  ->  [murakami2006]
  A version of the volume conjecture

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [murakami2006] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8508, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-22 — remark drafted, PR #9127

Remark block written on branch claude/library-remarks-2026-11-22, draft PR https://github.com/litlfred/qou/pull/9127 (issue #9121). Locators read from the held PDF. Stays open until the PR merges.

Session: https://claude.ai/code/session_01Qmmkt5c8TSSh1GGk4PoPDu



## 2026-11-24 — Tranche 3 origin/main reconciliation

Verified on origin/main (acb646cc6fe): volume-function-polarization-scope.{md,ts} (Murakami 2006 polarization convention scope) landed in mass-endomorphism in merged PR #9184 (7f6bc521263 / dc8919ec7a3).
