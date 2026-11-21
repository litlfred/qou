---
# qou-rx2u
title: 'test_betti_binding.py is dead: it imports information_wenzl_markov_trace, which does not exist anywhere in the repo'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T04:21:52Z
updated_at: 2026-11-21T16:40:00Z
parent: qou-v2om
---

- **Round 87 (`https://github.com/litlfred/qou/pull/8401`, head `e8b8112ae090b9f21e8140c9696e25d7da0297c6`)**: Formalized theorem + 80-dps witness (`status: in-progress`).

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). **Superseded premise found:** the script compares B(D) to the measured 2.224 MeV ('Ratio Betti/Target'), an empirical target inside a 'test', and uses the old canonical deuteron crossings. Still dead on main: line 58 imports `information_wenzl_markov_trace`, which exists nowhere. pytest collects nothing from it (no test_ functions). Recommend: delete the file (owner decision in the drain report).

## 2026-11-21 — owner cleanup (binding-hygiene, session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

**Fixed in PR #8849** (commit `843b1e3be92`): `computations/test_betti_binding.py` deleted on owner approval. It imported a module that exists nowhere and compared to the measured 2.224 MeV. Close this bean when #8849 merges.

## 2026-11-21 — PR #8849 merged (binding-hygiene, session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

**Completed:** the fix landed on main with PR #8849 (merged 2026-11-21).
