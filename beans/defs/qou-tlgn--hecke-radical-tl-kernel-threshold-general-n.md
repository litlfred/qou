---
# qou-tlgn
title: 'Open: rad(jimboTrace) = θ(ker π) on H_{n+1} iff [k]_q ≠ 0 for 3 ≤ k ≤ n + 2 (general n)'
status: todo
type: task
priority: low
created_at: 2026-11-27T18:35:00Z
updated_at: 2026-11-27T18:35:00Z
parent: qou-0cyu
---

Open conjecture in this corpus (literature: Jones 1983; Goodman–de la Harpe–Jones; Wenzl 1988). Rule 13a: do not close on partial progress.

**Proved so far:**
- generic q (NotRootOfUnity, CharZero): `TLKernelEquality.mem_tlKernelPulled_iff` (#9488);
- n = 2 exactly: `TLKernelThresholdThree.rad_eq_tlKernel_iff` (#9535), with failures at [3] = 0 and [4] = 0 and the witness [3]·JW₃.

**Needed for general n:** Jones–Wenzl recursion in TL with tr(JW_m) = [m+1]/[2]^m, or the TL Gram determinant for the Markov trace. The n = 2 method (an explicit Gram matrix on the Catalan basis) does not scale by hand.

Carl was offered this on a card (2026-11-27). Recommended: record it, do not pursue now.
