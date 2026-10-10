---
# qou-loq3
title: 'Sorry: markov_identification sorry'
status: completed
type: task
priority: normal
created_at: 2026-08-04T01:49:55Z
updated_at: 2026-09-03T15:07:57Z
---

QOU/FeynmanPathIntegrals/markov_identification.lean: 1 sorry. Needs path-integral / Markov trace identification infrastructure.



## CLOSED 2026-09-03 — duplicate of qou-gzgi, discharged there
The field is derived, not assumed, in QOU/FeynmanPathIntegrals/MarkovIdentificationInstance.lean (MarkovIdentificationContext.ofMarkovTrace): at convention D every Markov trace equals the Ocneanu-weighted seminormal trace (SchurWeyl/MarkovTraceInstance.eq_wtrace_of_markov, general n, sorry-free), which IS tr_M = sum_lam w_lam tr_{S_lam}. The statement in markov_identification.lean was not weakened. Note: the '1 sorry' this bean cites never existed in the body (the docstring claimed one; corrected 2026-09-03 upstream).
