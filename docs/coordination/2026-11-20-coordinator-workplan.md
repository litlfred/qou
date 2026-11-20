# Coordinator work plan — 2026-11-20

Session epic bean: `qou-c20n` ("Session: coordinator 2026-11-20 — consolidate stalled work").
Coordinator (this session) is **merge manager**: siblings branch, verify and open PRs; only the
coordinator merges, after `/prepare-merge` and **explicit** owner permission ("merge it").

## Snapshot at start (main `917b69399`)

| surface | count | note |
|---|---|---|
| open PRs | 411 | 219 `feat/*`, 106 `claude/*`, 46 `qou-10v9-*`, 23 `qou-8lxd-*`, 11 `cat/*`, 3 `qou-mub3-*`, 3 `fix/*` |
| machine Lean batches (≈5 beans each) | ≈300 | `feat/round*`, `qou-10v9-*`, `qou-8lxd-*`, `cat/round*`, `claude/round*-devacuify`, `claude/qou-rtxm-*` |
| open issues (non-PR) | 4 | #8524, #8520, #8516, #8501 — all covered by open PRs |
| beans on mount | 5792 | 1812 `in-progress` (most stale), 402 `todo` |

## Workstreams

| id | owner | scope | first targets |
|---|---|---|---|
| W1 | sibling | **Mass formula — proof** (Lean + content, `chap:mass-endomorphism`, epic `qou-d8c7`) | #8523 (port of #7551 core), #8522 (port of #7418), #8365 Bring foundations; stalled M6 convention-D redos `qou-fd2u` `qou-q425` `qou-wlnx` `qou-nxjw`, `qou-j11h`, `qou-jgp2`, `qou-2150`, `qou-o3so`, `qou-1jw9` |
| W2 | sibling | **Mass formula — compute & precision** (producers, pyhecke atom, Q_β ladder, program `qou-10v9`) | #8521 (closes #8520, owner ruling 2026-11-18), #8082, Q_β #8098/#8100/#7610, q_int float64 #7440/#7443, `qou-brng` |
| W3 | sibling | **Photon / QED / γγ** | #8367 (closes #8366, #8524), #8517 (#8516), #8502 (#8501), #8126, #7876, #8064, #8374 |
| W4 | sibling | **Batch-formalization PR triage** (≈300 PRs) | rerunnable triage script + table: MERGE-CANDIDATE / NEEDS-REWORK / CLOSE-SUPERSEDED / CLOSE-VACUOUS |
| W5 | sibling | **Legacy `claude/*` PR triage + ports** (≈70, Aug–Nov) | table + top-5 "port core onto main" PRs; RT audit epic `qou-ncxf` state |
| W6 | sibling | **Review of older non-child conversations/sessions** | outstanding work → workstream queues; SAFE-TO-ARCHIVE list for the owner |
| M | coordinator | **Merge queue** | collect READY-FOR-MERGE evidence from W1–W5, run `/prepare-merge`, ask owner per PR |

## Rules every sibling carries

Shared contract: worktrees off one clone (no parallel clones — the proxy allows 2 concurrent
git ops), REST-only GitHub, no merges, NO FITTING except CAL-1/2/3, ask-owner-before-changing
(precision and corpus-derived exemptions only), NO-FLOAT64 incl. probes, lean-direct + `#print
axioms` evidence, corpus-grep before "open"/"refuted".

## Merge order (provisional, coordinator judgement)

1. Ports that unblock the mass chapter: #8523, #8522.
2. Owner-ruled compute switch: #8521.
3. Precision fixes (exemption 1): #8082, q_int excision if not superseded.
4. Photon Lean (#8517, #8502), then #8367 content.
5. Batch PRs in W4's MERGE-CANDIDATE order, oldest-mergeable first, in groups.

This file is updated as sibling reports arrive.
