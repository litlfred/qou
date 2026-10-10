---
# qou-idwf
title: 'Session: thread1 Wenzl H4 weights + n=4 full Lean identity'
status: completed
type: task
priority: normal
created_at: 2026-08-29T06:16:38Z
updated_at: 2026-08-29T06:41:58Z
---

DONE 2026-08-29: independent general-z H4 weights = Wenzl Schur-principal closed form (markov_weights_symbolic.py machinery, R=qz/(1-q^2+qz)). Verified Wenzl==Molien EXACT as rational functions of (q,z) at n=3 AND n=4 (molien_wenzl_weight_identity_probe.py). Upgraded MolienJonesMarkovN4.lean from structural to FULL identity n4_full_identity (4 ratio identities vs ref (2,2) + normalisation + D-cap), lean-direct EXIT 0 (47s), sorry-free. Ladder linear system is rank-deficient at n>=4 (4 ladder elems, 5 partitions) so the Wenzl route -- not the regular-rep solve -- is the right independent source.
