---
# qou-adgd
title: 'GAP: ArchimedeanLimit on [-1,0), x=1 and x>1 (LiTwo is a tsum, so the class needs Re Li2 there)'
status: todo
type: task
created_at: 2026-11-15T18:12:20Z
updated_at: 2026-11-15T18:12:20Z
parent: qou-r9ih
---

Issue #7942, PR #7946. ArchimedeanLimit is proved on (0,1) on main (DilogPartAConvergence.archimedeanLimit_Ioo). PR #7946 proves it FALSE for x < -1 (ArchimedeanLimitDomain.not_archimedeanLimit_of_lt_neg_one), because LiTwo is a tsum and is 0 when |x|>1 (not summable), while the q-product limit is not 0. Open: [-1,0) (the series converges; needs the alternating/Abel exchange), x=1 (zeta(2) boundary), and x>1 (statement must be restated with Re Li2 or an analytic continuation, not the tsum). No alpha_em Lean theorem takes ArchimedeanLimit as a hypothesis; it appears only in docstrings.
