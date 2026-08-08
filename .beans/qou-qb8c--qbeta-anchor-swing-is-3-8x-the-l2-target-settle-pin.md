---
# qou-qb8c
title: 'Q_beta anchor swing is 3.8x the L2 target -- settle the pin before any L2 claim'
status: todo
type: task
priority: normal
created_at: 2026-08-08T08:10:00Z
updated_at: 2026-08-08T08:10:00Z
---

Measured this session (mpmath 60 dps, symbolic-exact log-derivative of the
Q_beta base form):

    q rel diff (proton - muon)/muon  =  -11.537 ppb
    dlnQ_beta/dlnq                   =  -2.5968
    => anchor swing on Q_beta        =   29.96 ppb

Two readings, both needed:
- 29.96 ppb is 2.4% of the current 1248 ppb residual => re-pinning is NOT a
  lever that closes L2, and must not be presented as one.
- 29.96 ppb is 3.8x the entire 100x target (7.797 ppb) => even with c_3 fully
  derived, the anchor choice ALONE overshoots L2 by ~4x. Deriving c_3 is
  NECESSARY BUT NOT SUFFICIENT for Q_beta to meet L2.

Live straddle to resolve: qbeta-ck-cache.witness.json is stamped
q0Anchor: "muon", q0Value: 1.10997859555733471989..., while
per_observable_100x_status.py reads q_parameter.Q_50_DIGIT_STR. That is a layer
boundary crossed inside one dashboard row -- the hazard named by the 2026-08-07
owner directive (AGENTS.md §q0-anchor: production compute defaults to the
experimental/proton pin).

Per the directive's migration posture, the ~840 muon witnesses are NOT to be
bulk-regenerated (tracked under bean tnjb). Scope here is narrow:
1. Any future claim that Q_beta meets L2 must state its pin and be internally
   consistent about it.
2. When qbeta_ck_cache.py is next touched, move the WHOLE quantity to proton
   rather than leaving one input on each layer.
3. Record the pin explicitly in the L2 dashboard's Q_beta row source string.

Analysis: docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md §3.
