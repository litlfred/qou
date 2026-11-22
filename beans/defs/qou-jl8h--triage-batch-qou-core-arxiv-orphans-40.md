---
# qou-jl8h
title: 'Triage batch: QOU-core arXiv orphans (~40)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T15:38:27Z
updated_at: 2026-10-04T15:25:10Z
parent: qou-1qhv
---


## 2026-11-22 measurement (session https://claude.ai/code/session_01Qmmkt5c8TSSh1GGk4PoPDu)

Method: every `library/arxiv-*` directory whose arXiv id (old-style ids as `math/NNNNNNN`) appears in no `folio/references/*.json`, excluding `duplicate_of` copies. Result: **194** documents, far above the ~40 in the title.

- **6** are mentioned from `folio/` (all from Lean docstrings) and had no reference entry. Added on branch `claude/library-orphan-refs-batch1-2026-11-22` (issue #9068): brundan2017 (used as a key in 13 OrientedSkein files), tonini2014, tonini2020, chattopadhyay-dutta-mukherjee-neetu2019, dutta-mukherjee-neetu-parihar2021, aishwarya-rotem2023.
- **151** are mentioned only in inventory files (`docs/audits/2026-09-15-library-slug-map.json`, `docs/audits/2026-10-04-workplan-and-migration/*_inventory.tsv`, `docs/coordination/satellite-cabling-source-ledger.md`): bookkeeping, not use.
- **37** are mentioned nowhere outside `library/`.

Still open: a relevance verdict (core / supporting / tangential / not-relevant) for the 188 nothing cites, per `paper-relevance-triage`.
