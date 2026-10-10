---
# qou-8j0d
title: 'A_ω step 1: crack the 4₁ index assembly via DGG appendix B anchors'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-17T22:01:00Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** 4₁ total 3d-index assembled from DGG 1112.5179 eq 4.18, reproducing DGG's printed anchor (4.20) exactly; re-run 2026-10-10 reproduces it. It does not feed A_ω.

Evidence: `computations/probes/qbeta_g3_fourone_index_assembly.py` re-run: exit 0, 0.6 s, "reproduces (4.20) exactly: True". Witness `qbeta-g3-fourone-index-assembly.witness.json` has 5/5 passed (anchor 4.20, symmetries 4.19, engine cross-check, q-A-poly annihilation).

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
