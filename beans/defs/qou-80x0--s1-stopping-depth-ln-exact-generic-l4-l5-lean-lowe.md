---
# qou-80x0
title: 'S1: stopping depth L(n) — exact generic L(4), L(5); Lean lower bound abstract + model checks'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T15:36:29Z
updated_at: 2026-11-25T16:22:54Z
parent: qou-y2o9
---

2026-11-25: done in PR #9430 (audit §14); see table sent to coordinator.


HANDOVER 2026-11-25 (session_01EucfRopy82qV7K5FpozNB9).
DONE: L(3)=2 proved in the concrete model (PhotonStoppingDepthThree, HeckeH3Model). L(4)=4 exact for all q; L(5)=6 exact at two q (modular rank, photon_stopping_depth_probe.py). Abstract lower bound ceil(N/2) <= L(n) and staircase count sum ceil(r/2) = floor(n^2/4) proved (PhotonStoppingDepth.lean). Content: prop:photon-filtration-depth-bounds, conj:photon-stopping-depth. Merged #9415/#9427/#9430.
NEXT: generic L(5)=6 — rank of F_1^5 vs F_1^6 over Q(q) symbolically (or at enough q to bound the degree of the rank-drop locus), then the leading-term upper-bound argument (audit §12.2) in Lean for general n. Needs a Lean model of H_n(q) for n>=4; none exists (only H_3 in HeckeH3Model).
BLOCKERS: none; compute is modest (n=5 dim 120).
ROUTE: research child; final heads to merge manager session_01EucfRm2khmNLbMgiuTA6UZ.
