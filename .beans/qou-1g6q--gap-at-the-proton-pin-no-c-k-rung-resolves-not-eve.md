---
# qou-1g6q
title: 'GAP: at the proton pin NO c_k rung resolves, not even c_2/c_3'
status: todo
type: task
created_at: 2026-08-23T22:22:29Z
updated_at: 2026-08-23T22:22:29Z
---

6d261854d4 (2026-08-23, regenerate the q-pin consumers) re-ran qbeta_decay_sdp_extended_ck and produced last_resolved_rung: null, n_unresolved: 9 -- every c_k null. The residual floor moved from 7.4e-5 (recorded in e5885ebc0f's instrumentation) to 6.0e-4, an order of magnitude worse, so even c_2 and c_3 no longer clear the 10x resolution bar. qou-frch reported c_2 = -1 and c_3 = -2 as testing and passing convincingly against R(q0) at the prior state. Two readings, not settled: (a) genuine anchor effect -- the proton pin really does leave the model's accuracy an order worse, in which case the c_2/c_3 support in qou-frch was pin-specific and needs restating; or (b) a regeneration defect in the q-pin sweep. This matters because c_2 = -1 is quoted in AGENTS.md as structural (no fit, no CODATA, no q0) and c_3 = -2 = J_Hopf(q=1) is a headline near-match. Neither claim depends on THIS extraction -- both are stated independently -- but this extraction is the corpus's numerical check on them, and it currently checks nothing. Determine which reading holds before anything downstream cites the extraction again.
