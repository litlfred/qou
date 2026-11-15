---
# qou-fxou
title: 'S3: where does the knot-complement ambient S^3 come from'
status: completed
type: task
priority: high
created_at: 2026-09-04T03:04:50Z
updated_at: 2026-09-04T03:23:16Z
parent: qou-8lxd
---

RESOLVED 2026-09-04, commit 6a1ca05322: verdict (c) -- there are THREE S^3s, not two, and the recorded contradiction is a conflation under one glyph. S^3_AM (bare Alexander-Markov input, NOT SU(2) -> the remark was right), S^3_Reeb (Reeb-bundle total space, IS SU(2) structurally -> the 2026-06-28 audit was right), M_S (the QOU's own contact manifold over Bring's genus-4 surface, provably not S^3). The contact volume form Theta^dTheta IS in the corpus and IS natural (Liouville on T*S), but is PROSE tier only -- zero definition, zero Lean, and no block links it to Lambda^3. CircleBundleBettiObstruction.lean proves scope-(b) that the manifold carrying it is not S^3: chi=-6 forces g=4 forces b_1>=8 for every Euler number. Fourth confirmation of the real-type obstruction on the Im H / sp_1 leg. LIVE CONTRADICTION reported not fixed: ker Theta is rank 4 in two blocks and rank 2 in a third.
