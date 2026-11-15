---
# qou-li27
title: Magnus branching-tower step-4 engine (transfer-matrix contraction on mpfr)
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T17:41:57Z
updated_at: 2026-10-04T15:21:22Z
parent: qou-v2om
---

Tower steps 1-3 validated + merged (#6183): branching H_n->H_{n-1} faithful, bond p(3(A-1)) sub-exp, germ/link locality O(1), sigma_g & A_g single-level-local MPOs. Step 4 = the doubled-Bratteli weighted-trace contraction Sigma_lambda y_lambda tr(rho_lambda Omega2_lambda) over the shape-bond, gated vs flat-sparse A=3/A=4. Build on gmpy2.mpfr (#6273, 3.8x) and bake in S_Z x S_N / S3 block symmetries (identical nucleon tensors computed once). This is what reaches A>>4.
