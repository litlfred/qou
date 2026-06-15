# `_deprecated/yekutieli-purged/`

Scripts that depended on the Yekutieli per-cell curvature extension
(`λ_Y = λ_A − G·h²`), which was **PURGED from production** on
2026-05-24 (commit [`71d674da1`](https://github.com/litlfred/qou/commit/71d674da1)).

## Why moved here

Per PR [#985](https://github.com/litlfred/qou/pull/985), the
S₄↓S₃ half-symmetric projection bijection gave **κ = +0.5** rather
than the expected `−G`, falsifying the structural claim that
"the per-cell Yekutieli curvature accounts for the canonical
linking-weight correction". The Yekutieli `−G·h²` form is therefore
a substrate-q₀ numerical coincidence, not a categorical theorem.

Subsequently PR [#1080](https://github.com/litlfred/qou/pull/1080)
absorbed the proved Family A linking weight into the per-knot
`Geom_full(K)` evaluation, and PR [#1089](https://github.com/litlfred/qou/pull/1089)
removed the `lambda_scale_family_a` back-compat alias from
`_li_2_q_util.py` (owner directive 2026-05-24: "no lambda-scale
ANYWHERE in production").

Scripts in this directory:

- `lambda_yekutieli_extended_borromean.py` — imports the no-longer-
  exported `lambda_scale_yekutieli_extended` and `lambda_scale_family_a`
  symbols; the entire premise (`λ_Yekutieli = λ_A − G·h²` as a
  production refinement) is invalidated by the bijection falsification.
  Kept for historical reference; do not import.

## Reanimation policy

These scripts should remain deprecated unless a Lean-proved categorical
derivation of the Yekutieli per-cell correction lands (with a positive
bijection result, not `κ = +0.5`). Any reanimation must coordinate
with the canonical-watcher and pass through the 13-driver Rule 14
escalation (see [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../../../../docs/audits/2026-05-23-lambda-scale-canonical-unification.md)).
