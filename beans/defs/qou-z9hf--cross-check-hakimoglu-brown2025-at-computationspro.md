---
# qou-z9hf
title: Cross-check [hakimoglu-brown2025] at computations/probes/qbeta_fourone_habiro_tail_action_probe.py
status: completed
pr: 8298
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:26Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

Re-affirm Li_2(phi^{-2}) = pi^2/15 - ln^2 phi and the resulting A_0 = pi^2/5 numerically against the existing witness, so the identity is anchored in-repo independently of which paper is cited for its proof.

Source: `library/arxiv-2506.10206v2/2506.10206v2-analytic-dilogarithm-identities-hakimoglu-brown.pdf` (`hakimoglu-brown2025`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Round 58 Update (PR #8298)
- **Status:** `in-progress` (PR `litlfred/qou#8298`, head `92f8a80b907a40e6db76eb1a8a85f081c5960913`, Commit 1 `df446885b17718b4f18e584a2765ba2e802adb68`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/BraidKnot/N5LevelSixRootThresholdAndThreeLinkTriad.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSaddleHessianAndFourOneStokesCrossCheck.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all 5 static audits).
- **80-dps Probe & Witness:** `computations/probes/round58_n5_level_six_ohtsuki_thimble_fourone_stokes_dilog_probe.py` and `computations/probes/round58-n5-level-six-ohtsuki-thimble-fourone-stokes-dilog.witness.json` (`allPassed: true`, `0` raw `float64`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8298, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `2a5686b5a`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). 60-dps check: both residuals ~1e-61; existing witness asserts A0 = π²/5. Not committed as a probe.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
