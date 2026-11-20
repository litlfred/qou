---
# qou-07m1
title: Cross-check 2302.08363v2.pdf at computations/probes/fourone_stokes_series_selfcheck.py
status: todo
pr: 8298
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:49Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8hur
---

Extend the existing 4_1 Stokes-series self-check with the independently published eq (4.5) coefficients and record the verified relation M_1 = g_0 * 2G_0 through q^4 (and the absence of a comparable form for M_2). Cross-check only; nothing to wire, and the relation is a consistency test between two sources' notations, not a QOU observable.

**From the source**
- Sec 4, eq (4.5) — M_1(q) = 1 - 8q - 9q^2 + 18q^3 + 46q^4 + O(q^5) and M_2(q) = -9q - 3q^2 + 39q^3 + 69q^4 + O(q^5), the power series in q~ multiplying the two 4_1 instanton towers, stated to be convergent with radius of convergence R = 1 and with exact expressions attributed to its ref [41].
  Use here: Independent published values for the same 4_1 object that computations/probes/fourone_stokes_series_selfcheck.py already self-checks from the `fantini-wheeler2024` eq (74) blocks g_0(q) = 1 - q - 2q^2 - 2q^3 - 2q^4 + ... and 2G_0(q) = 1 - 7q - 14q^2 - 8q^3 - 2q^4 + ... . Verified during this triage by exact rational power-series arithmetic: M_1 = g_0 * 2G_0 exactly through the printed order q^4 (product coefficients 1, -8, -9, 18, 46 reproduce eq (4.5) term by term). M_2 has no comparable factorisation at this order: M_2/g_0 = -9q - 12q^2 + 9q^3 + 36q^4, M_2/(g_0 * 2G_0) = -9q - 75q^2 - 642q^3 - 5580q^4. This turns the existing single-source self-check into a genuine cross-source consistency test between two independent papers' notations for the 4_1 Stokes data. Scope: 4 non-trivial coefficients matched, which is evidence of the identity, not a proof of it.

Source: `library/arxiv-2302.08363v2/2302.08363v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2302.08363v2/  ->  [arxiv-2302.08363v2]
  On the structure of trans-series in quantum field theory

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-2302.08363v2] as the citation key when you do it.


## Round 58 Update (PR #8298)
- **Status:** `in-progress` (PR `litlfred/qou#8298`, head `92f8a80b907a40e6db76eb1a8a85f081c5960913`, Commit 1 `df446885b17718b4f18e584a2765ba2e802adb68`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/BraidKnot/N5LevelSixRootThresholdAndThreeLinkTriad.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSaddleHessianAndFourOneStokesCrossCheck.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all 5 static audits).
- **80-dps Probe & Witness:** `computations/probes/round58_n5_level_six_ohtsuki_thimble_fourone_stokes_dilog_probe.py` and `computations/probes/round58-n5-level-six-ohtsuki-thimble-fourone-stokes-dilog.witness.json` (`allPassed: true`, `0` raw `float64`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8298, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
