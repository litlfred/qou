---
# qou-4kgh
title: 'T3a: off-lattice vs on-lattice — why T4-inverted ϑ values are non-integer in cusp lattice units'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-30T16:59:40Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---

The T4 crux probe inverts ϑ(muon) ≈ 0.65 and ϑ(proton) ≈ 2.24 in units of (√3/2)·ln q₀. Neither is an integer. If the mechanism were 'braid closure = integer geodesic (m,ℓ)', these would be integers. Three hypotheses: (1) off-lattice continuous deformation, (2) A_ω varies by winding class, (3) multi-cusp (Borromean) effects. Pursue via Lean formalization of the NZ potential at non-integer slopes + numerical probe scanning the A-polynomial for continuous ϑ solutions.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** "Non-integer ϑ" cannot be posed until ϑ is determined: the inverted values come from convention-C S_leak central values whose uncertainty (±1.262) exceeds the values. Redo only after a D-frame c3 (qou-cds1), or a c3 determination that does not divide by u³.

Evidence: The ϑ values 0.65/2.24 in lattice units come from T4 inversion of the convention-C S_leak central values. Witness: `sign_flip_resolved=False`, `S_uncertainty=1.262`, which gives sigma(ϑ²) ≈ 0.97 against L ≈ 0.011.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Progress (PR #8448)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/CuspLatticeUncertaintyTruncationDigitSlopeJetHorizonProjectionSubstrateModelScalarTrace.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_4kgh_5u0i_a2d7_aawz_nnyn_probe.witness.json` (`Commit 1` = `03aab630aaf498438c097ced372d1b9624239334`, `HEAD` = `9712a8a7c54237632ba55faa0a1e31fdd3332e05`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8448, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
