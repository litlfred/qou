---
# qou-ni2p
title: Remark interpreting 1002.0126v1.pdf at content/bib-qa-verifications.json
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:35:15Z
updated_at: 2026-08-21T17:04:59Z
---

Record the mis-join itself: the ledger/indexer attached this file to faddeev_kashaev1994, a key that already has its correct upload at library/arxiv-hep-th-9310070v1/9310070v1.pdf. Two uploads pointing at one key is the signature of exactly this failure mode and is worth a note so the indexer heuristic can be tightened.

Source: `library/arxiv-1002.0126v1/1002.0126v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1002.0126v1/  ->  [murakami-h2010]
  An introduction to the volume conjecture

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [murakami-h2010] as the citation key when you do it.
