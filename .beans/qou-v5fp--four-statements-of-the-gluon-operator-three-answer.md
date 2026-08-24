---
# qou-v5fp
title: Four statements of the gluon operator, three answers - min-cr vs min-|tr_M| disagree
status: todo
type: task
created_at: 2026-08-24T20:59:37Z
updated_at: 2026-08-24T20:59:37Z
---

Found while closing qou-1ngr, 2026-08-24. Separate from qou-jqjx (trace convention); this one is about the objective, not the weights.

The same quantity — which operator step 4 of def:derived-atom selects as the proton's gluon — is stated four times and comes out three ways:

  def:universal-ilp-algorithm, prose instantiation table : sigma_0 sigma_0, 2 crossings
  computations/universal-ilp.witness.json (its OWN witness): sigma_1,        1 crossing
  rem:categorical-proton-properties + the exists/unique proofs: L_- = sigma_1 sigma_0, 2 crossings
  computations/_deprecated/integer-lp-gluon.witness.json    : sigma_0 -> sigma_0, 2 crossings

Two distinct problems underneath.

1. The stated objective is not the objective used. `def:universal-ilp-algorithm` states min cr(K) first, |tr_M(x.K)| as tiebreak WITHIN a crossing shell. The deprecated producer sorts by |tr_M| alone with no crossing preference. They disagree, and the disagreement is exactly on the load-bearing number. Cheapest survivor per crossing shell, retired convention (scratch re-run):

     proton : cr=1 sigma_0 |tr_M|=0.1597 ; cr=2 sigma_0->sigma_0 0.0274 ; cr=3 0.1654 ; cr=4 0.0921
     neutron: cr=2 L_+     |tr_M|=0.3873 ; cr=3 L_+->sigma_1   0.1441 ; cr=4 L_+->L_- 0.1120

   Under min-cr-first the proton takes 1 gluon crossing and the neutron 2 — not 2 and 4. The 2-versus-4 asymmetry, which is what makes the neutron heavier and feeds Q_beta = m_n - m_p - m_e (CAL-2), exists only under pure min-|tr_M|.

2. `computations/universal-ilp.witness.json` is self-certifying. Its assertions compare each computed operator against an `expected` value baked into `universal-ilp.py`, so allPassed=true and status "verified" say nothing about the corpus. It records confinement as sigma_1 at 1 crossing against B_3's 6, and the gluon as sigma_1 at 1 crossing against the blocks' 2 — i.e. the live witness for def:universal-ilp-algorithm does not reproduce a single crossing count the definition's own prose table asserts.

Task: pick one objective, state it once, re-witness the gluon selection against it, and reconcile the four statements. Until then rem:gluon-stabiliser-ledger records the discrepancy in prose rather than resolving it.

Related: qou-jqjx (the trace weight the retired producer used), qou-1ngr (closed - the feasible set itself is fine).
