---
# qou-uu6g
title: 'prop:t-beta-markov-frobenius-collapse: Lean proves X=S -> X*X=S*S, block claims min Frobenius norm over H_n'
status: todo
type: task
tags:
    - lean
    - vacuity
created_at: 2026-11-22T15:20:06Z
updated_at: 2026-11-22T15:20:06Z
parent: qou-uwyf
---

Found by rule 6 (rewrite-by-own-hypotheses) of scripts/lean-self-assuming-audit.py, 2026-11-22.
The block's lean.ref QOU.QBeta.MarkovFrobeniusCollapse.t_beta_collapse is `(h : X = S) : X * X = S * S := by rw [h]`. The .md claims: over H_n(R,q) with the Markov trace and twisted form tr_M(X Y†), the minimum-norm element with tr_M(T)=S is S·1 with norm S², unique up to the radical. Twin: t_beta_markov_min_frobenius_collapse_substrate in markov-trace-frobenius-selection.lean.
Honest fix (corpus-derived, the .md fixes the claim): state it over an abstract R-algebra H (ordered field R) with linear τ, τ(1)=1, τ(X†)=τ(X), positivity τ(Y Y†) ≥ 0; prove τ(X X†) ≥ S² from τ(X)=S by completing the square. Positivity is Wenzl's theorem and is a hypothesis, not the conclusion. Or demote.
