---
# qou-qqm4
title: 'DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pairwise chain is nearly additive at that order'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T15:51:43Z
updated_at: 2026-09-03T15:58:05Z
---

Successor to qou-pdg9 (c1 derived, PR #6492). Exact c2 = [eps^1]+[eps^2] of Dtr(1+eps) is in c1-leading-coefficient-derived-probe.witness.json: pp 357/32, pn 403/32, nn 217/16, T 3285/128, 3He 3451/128 (4He pending, order-4 series). Observation from that data: chain/atom at SECOND order is 3348/3285 = 1.019 (T) and 3040/3451 = 0.881 (3He), against 292/163 = 1.79 and 30/17 = 1.76 at first order -- the over-count nearly cancels one order up. qou-zrx2 called the q0 agreement 'higher-order terms partially cancelling'; this quantifies it exactly. Goal: (1) 4He c2 exact; (2) derive c2 by extending the [star] expansion to second order (the Y-terms Tr(Y P Y P') no longer vanish; K'' and the normaliser's second derivative enter); (3) explain the near-additivity structurally or refute it as coincidence at A=4.



2026-09-03: 4He c2 EXACT = 15307/512 (order-4 series, 15 min). Second-order chain/atom ratios: T 3348/3285 = 1.019, 3He 3040/3451 = 0.881, 4He (597/16)/(15307/512) = 19104/15307 = 1.248 -- against 1.79 / 1.76 / 3.43 at first order. So the second-order over-count is much smaller than the first-order one but is NOT uniformly ~1; 'nearly additive' in the title overstates 4He. Tensor-picture engine (tensor_picture_markov_trace_probe.py) reproduces the seminormal Markov trace on the deuteron words to every computed order for BOTH R-matrix h-placements -- both must, by uniqueness of the Markov trace at fixed loop value.
