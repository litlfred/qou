---
# qou-gzgi
title: 'Markov trace branching: close markovTrace_branching field'
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-08-24T06:35:58Z
updated_at: 2026-09-03T15:02:26Z
parent: qou-c8p8
---

MarkovIdentificationContext.markovTrace_branching in markov_identification.lean. May be closable from existing Markov trace infrastructure.



## 2026-09-03 — claimed (branch claude/markov-identification-instance-2026-09-03)
Closable now: MarkovTraceInstance.eq_wtrace_of_markov (every Markov trace at z_D equals the Ocneanu-weighted seminormal trace) + wtrace_apply IS the decomposition tr_M = sum_lam w_lam tr_{S_lam}, general n, sorry-free. Plan: new library file QOU/FeynmanPathIntegrals/MarkovIdentificationInstance.lean with an enumeration of the size-(n+1) diagrams by a natural index (Fintype.equivFin), a constructor MarkovIdentificationContext.ofMarkovTrace T x whose markovTrace_branching field is PROVED from eq_wtrace_of_markov, and the specialised markov_identification. Duplicates to close with it: qou-4pzd, qou-loq3.
