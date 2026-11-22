---
# qou-baov
title: prop:t-beta-markov-frobenius-collapse-general assumes untwisted positivity tau(X*X) >= 0, which fails on H_n for n >= 3
status: completed
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T15:29:12Z
updated_at: 2026-11-22T22:14:59Z
parent: qou-uwyf
---

Found 2026-11-22 while fixing qou-uu6g. The general block's class PSDTrace (t-beta-markov-collapse-general-lift.lean:102) assumes 0 <= tau(x * x) for all x. The sibling block prop:t-beta-markov-frobenius-collapse shows that fails for the Markov trace on H_3: X = s1 s2 - s2 s1 gives tr_M(X*X) = -2(q^4+q^2+1)/(q^2+1)^2 < 0. So the general block's hypothesis has no instance in its stated application (Iwahori-Hecke algebra). The Lean is sorry-free and correct; the defect is that its application section applies it where the hypothesis is false. Fix: restate with the twisted form tau(X * X^dag), as t_beta_collapse now does (QOU.QBeta.MarkovFrobeniusCollapse.t_beta_collapse), or scope the application to the commutative / n <= 2 case. Content change: ask the owner which.


2026-11-22: owner card option 1. Restated with the twisted form in PR #9063 (rebase-merged, 3891adf8e88). lean exit 0. The vacuous library General.lean projection is removed. Note: the block's .md already scoped out the Hecke case before this; the defect the owner ruled on was the untwisted hypothesis.


2026-11-22 (W8 thread, branch claude/hecke-axioms-positivity-2026-11-22): instance supplied. QOU/SchurWeyl/WtraceTwistedPositivity.lean proves 0 ≤ wtrace(X·X†) and wtrace(X†) = wtrace(X) at z_D for q > 1 over any ordered field (positive diagonal form on SYT making Young's seminormal matrices self-adjoint; Ocneanu weights at z_D ≥ 0). t-beta-markov-collapse-general-lift.lean: markovTraceZD, markovTraceZDTwist, instance markovTraceZD_twistedPSD, markov_frobenius_min_norm_zD. TwistedNonDegTrace is false at z_D for n+1 ≥ 3. Open point put to owner: TraceTwist admits the degenerate twist x ↦ τ(x)·1, proposed fix adds dag_mul.
