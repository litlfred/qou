---
# qou-5u0i
title: 'DERIVED, not fitted: the Q_beta truncation rule constant 2.07 is log10(1/u) = 2.0697 (u = 0.008517234550156142). Ladder term at rung k is O(u^k) so log10(1/u) digits per rung. Closes the qou-ai9u target for this rule, CONDITIONAL on c_k = O(1)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T03:27:53Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** log10(1/u) = 2.0697 is correct arithmetic. The rule it "closes" is a property of the C-frame ladder, and its O(1) premise is untested under D. Re-check once a D-frame ladder exists (qou-cds1), or scrap with cds1.

Evidence: Body is empty. Arithmetic checks: log10(1/0.008517234550156142) = 2.06970139. The "closes target" claim is conditional on c_k = O(1). That holds only for the C-frame coefficients; the hybrid z_D extraction gives c_3 ≈ -974 (the sensitivity witness above), and no D ladder exists.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Progress (PR #8448)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/CuspLatticeUncertaintyTruncationDigitSlopeJetHorizonProjectionSubstrateModelScalarTrace.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_4kgh_5u0i_a2d7_aawz_nnyn_probe.witness.json` (`Commit 1` = `03aab630aaf498438c097ced372d1b9624239334`, `HEAD` = `9712a8a7c54237632ba55faa0a1e31fdd3332e05`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8448, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
