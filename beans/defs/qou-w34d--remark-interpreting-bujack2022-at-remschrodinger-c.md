---
# qou-w34d
title: Remark interpreting [bujack2022] at rem:schrodinger-color-falsifiability
status: in-progress
pr: 8425
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:06Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-aqfj
---

Withdraw the crossover-bracketing sentence: the β_{Δd=5} vs β_{Δd=10} contrast is not a crossover measurement and the source reports no crossover scale. Record the correction and the resulting fact that the framework's η prediction currently has NO empirical corroboration in this source. Scope-(a): as read, this document supplies no crossover datum — it does not refute η either.

**From the source**
- Table 1, p. 5 — Regression coefficients: β₀=0.161 (t(60)=8.894), β_{Δd=5}=0.048 (t=2.815, P=0.010), β_{Δd=10}=0.119 (t=6.632, P<0.001), β_d̄=−0.005 (t(60)=−5.566, P<0.001); R²=0.556, F(3,60)=25.00.
  Use here: β_d̄ is the ONLY diminishing-returns coefficient; the Δd-level coefficients must be removed from the crossover argument in the falsifiability remark.
- p. 5, interpretation of β_d̄ — The authors interpret the negativity of β_d̄ as WEAKLY supporting nonadditivity, conditional on the L* axis being nearly perceptually uniform — an assumption they say 'may not be appropriate'.
  Use here: Downgrades the block's 'proved' to 'reported evidence for'.

Source: `library/bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co/bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf` (`bujack2022`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8425)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/PadicPolylogSelfReciprocalVortexPotentialRound71.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round71_padic_polylog_self_reciprocal_vortex_potential_probe.py` with 2-commit witness `computations/probes/round71-padic-polylog-self-reciprocal-vortex-potential.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8425 (`ready: e9a0477369d852fec1b713ba0fbbc441b552fa75`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8425, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T13:00:00Z expo-remarks drain (session_01Qmmkt7Gng13BtVDyQLMYQT)

Remark written: commit 4c68aac92 on branch claude/expo-remarks-2026-11-21, draft PR #8832 (issue #8803). Exposition only: no new claim, no new number. Superseded-premise check (owner 2026-11-21 list: L-plus/minus in the photon, virtual photons, pre-Nov-15 gamma-gamma interface letters, T(2,n_s), convention C, single-term trace, trefoil as primary electron, 'c_2=-1 PROVED', chi_(2,1)=2-h^4, fitted alpha/CODATA in proofs, project memory): none found in the edited text. Also checked: no superseded premise in the withdrawn sentence itself. Status kept in-progress until #8832 merges; close as completed then.
