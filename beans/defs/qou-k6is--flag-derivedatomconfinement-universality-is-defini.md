---
# qou-k6is
title: 'FLAG: DerivedAtom.confinement_universality is definitional (polarization argument discarded)'
status: todo
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:17:22Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u, PR #7825. QOU/Interactions/DerivedAtom.lean:126-158 defines crossingCoeffsWithPol ct _ := crossingCoeffs ct and then proves independence of the polarization by simp. It is true by definition and says nothing about the gamma-gamma chain. Not edited (owner ask rule). Options: scope it as a definitional remark, or route it through the flavour-extraction map once that exists.

## Progress (PR #8452)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PolarizationArgumentDiscardDecayWindowFractionSurprisalVolumeTermStepUnitDomainWallDilution.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_k6is_kh7e_lsvj_mumr_qjh8_probe.witness.json` (`Commit 1` = `ffa2d78ef5414a49bba12e0efccca6fbb72626d5`, `HEAD` = `078aa49b3db67c82ebbd4ebd6bd00b088ab2f9d9`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8452, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
