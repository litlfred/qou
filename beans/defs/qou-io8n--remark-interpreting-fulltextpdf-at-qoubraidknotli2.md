---
# qou-io8n
title: Remark interpreting fulltext.pdf at QOU.BraidKnot.Li2qUniqueness
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:21Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-aqfj
---

Record that all three kirillov1995 locators (§2.1, Prop 2.1, Prop 2.3) in Li2qUniqueness.lean are currently uncheckable because the file joined to that key is a different work, and that Prop 2.3 in particular is attached to a generic FTC-uniqueness statement that the Lean file proves from Mathlib. Someone with access to the named work should confirm or re-locate all three.

Source: `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/zagier-the-dilogarithm-function/  ->  [zagier-dilogarithm]
  The dilogarithm function

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [zagier-dilogarithm] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8508, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
