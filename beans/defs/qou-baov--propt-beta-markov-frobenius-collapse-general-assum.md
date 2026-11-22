---
# qou-baov
title: prop:t-beta-markov-frobenius-collapse-general assumes untwisted positivity tau(X*X) >= 0, which fails on H_n for n >= 3
status: todo
type: task
tags:
    - lean
created_at: 2026-11-22T15:29:12Z
updated_at: 2026-11-22T15:29:12Z
parent: qou-uwyf
---

Found 2026-11-22 while fixing qou-uu6g. The general block's class PSDTrace (t-beta-markov-collapse-general-lift.lean:102) assumes 0 <= tau(x * x) for all x. The sibling block prop:t-beta-markov-frobenius-collapse shows that fails for the Markov trace on H_3: X = s1 s2 - s2 s1 gives tr_M(X*X) = -2(q^4+q^2+1)/(q^2+1)^2 < 0. So the general block's hypothesis has no instance in its stated application (Iwahori-Hecke algebra). The Lean is sorry-free and correct; the defect is that its application section applies it where the hypothesis is false. Fix: restate with the twisted form tau(X * X^dag), as t_beta_collapse now does (QOU.QBeta.MarkovFrobeniusCollapse.t_beta_collapse), or scope the application to the commutative / n <= 2 case. Content change: ask the owner which.
