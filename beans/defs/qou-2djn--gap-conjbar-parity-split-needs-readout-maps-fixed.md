---
# qou-2djn
title: 'GAP: conj:bar-parity-split needs readout maps fixed in advance (identity readouts provably fail)'
status: todo
type: task
created_at: 2026-11-15T09:59:53Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-qs0e
---

With identity readouts, an F with even part tau and odd part Q_beta exists iff tau is bar-even and Q_beta bar-odd (QOU.Mass.BarParitySplitGap.exists_parts_iff). The ruled z_D trace is not bar-odd (ruledTrace_not_bar_odd), so no F in the scalar space works (no_F_with_ruledTrace_odd). The conjecture has content only if an element F and readout maps are specified BEFORE their parts are compared. Choosing F or the readouts because the parts then match is fitting (AGENTS NO FITTING). Natural non-fitted candidate F = Delta in H_3(q) with readout tr_{z_D} reduces to qou-hlx8 route 4 and fails on nuc11_interleaved (context trace g has g_odd = -h[2]_q(q^2+q^-2)/8 != 0). Open: a derivation that names F and the readouts. Audit docs/audits/2026-11-15-bar-parity-split-gap-routes.md. PRs #7857 (demotion) and the gap PR.

## Progress (PR #8443)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityReadoutPartitionWeightBraidedTraceSurfaceGenusPolarizationPair.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_2djn_2joi_4khc_51l1_8ava_probe.witness.json` (`Commit 1` = `76eb5ed3bb589e3c0713062c1916ff3df6e16b60`, `HEAD` = `bd4d50a998e0b0519e966f309ff7ef17c810abac`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8443, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
