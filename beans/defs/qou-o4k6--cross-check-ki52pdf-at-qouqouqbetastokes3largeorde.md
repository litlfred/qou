---
# qou-o4k6
title: Cross-check ki52.pdf at qou:QOU.QBeta.Stokes3LargeOrderAmplitude
status: completed
pr: 8380
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:36Z
updated_at: 2026-11-21T14:53:46Z
parent: qou-8hur
---

Once registered, the all-orders 5_2 Poincare asymptotics give a parameter-free comparison against the large-order amplitude the corpus extracts from the GGM Stokes constants - a genuine external check rather than an internal consistency test.

**From the source**
- Abstract / main presentation — Presentation of the asymptotic expansion of the Kashaev invariant of the 5_2 knot, with leading term the hyperbolic volume and Chern-Simons invariant, plus a method computing the full Poincare asymptotics to all orders.
  Use here: An independent all-orders 5_2 asymptotic series to cross-check the corpus's 5_2 Stokes/DT-spectrum readings, which currently rest on a single source (garoufalidis-gu-marino2021).

Source: `library/ki52/ki52.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/ki52/  ->  [ohtsuki2016]
  On the asymptotic expansion of the Kashaev invariant of the 5_2 knot

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [ohtsuki2016] as the citation key when you do it.

## Progress (2026-11-18, PR #8380)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`35b03645ad735c533bdb60a9a19a56165e5833fa`, `scriptHash: 197841ead85d03085a06e8bf1a078fa708f1da7e60c96d98a12ad24512b472a1`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8380`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8380, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T14:53:46Z cross-check result

Probe computations/probes/ohtsuki_5_2_asymptotic_crosscheck_probe.py (branch claude/expo-cite-xcheck-wave2-2026-11-21, head 856abed7f07). ALL PASS.
- A 2 pi Re varsigma vs SnapPy Vol(5_2): rel 5.6e-11.
- B 2 pi Im varsigma vs SnapPy CS mod pi^2: 4.1e-10.
- C kappa_1 extrapolated from <5_2>_N (Takata formula, N = 64..120, Neville in 1/N): |diff| 2.4e-6. Takata's value is used directly (no conjugation), so the chiralities agree.
- D Ohtsuki's N = 200 table entry reproduced to 4.5e-7 (limited by his 10-digit varsigma, omega).
Premise finding: the named target QOU.QBeta.Stokes3LargeOrderAmplitude is about 4_1 only and carries no 5_2 object to compare.
