---
# qou-nmva
title: Recipe-chain type_breakdown literals are not cross-checked against atom_canonical_crossings
status: completed
type: task
priority: normal
created_at: 2026-08-14T20:04:06Z
updated_at: 2026-08-14T20:44:39Z
parent: qou-1295
---

From the qou-uzk0 sweep. build_atomic_braid_recipe_{p,d,n}_chain.py record type_breakdown as hand-written literals with trust_basis=DERIVED and operation strings claiming they match atom_canonical_crossings(Z, N, include_inter=True). Nothing checks that claim. The d-chain's literal said {sigma: 11, sigma_inv: 7, averaged: 5}; truth is averaged 4 + averaged_weighted 1 -- wrong from the moment the classifier learned the distinction, and it stayed wrong under a DERIVED label. p and n are correct today ONLY because a single nucleon has no p-n bond; they are equally unverified. Fix: a Part-A2-style check comparing each chain's recorded breakdown against a live Counter(atom_canonical_crossings(Z, N)).

CLOSED. Part D added to test_ctype_consumer_coverage.py: every recipe-chain breakdown literal is now compared against a live Counter(atom_canonical_crossings(Z, N, include_inter=...)).

Six claim sites checked, all green:
  p_chain:beta_p_canonical      {averaged 2, sigma 6, sigma_inv 3}
  n_chain:beta_n_canonical      {averaged 2, sigma 5, sigma_inv 4}
  d_chain:proton_intra          {averaged 2, sigma 6, sigma_inv 3}
  d_chain:neutron_intra         {averaged 2, sigma 5, sigma_inv 4}
  d_chain:inter_pn              {averaged_weighted 1}       (scope='inter', gens 3k+2)
  d_chain:beta_D_canonical      {averaged 4, averaged_weighted 1, sigma 11, sigma_inv 7}

Handles both recorded shapes (a full type_breakdown map, and the inter_pn step's type+count pair), and checks the total/count field separately since it is a second independently-wrong-able claim.

NEGATIVE CONTROL RUN -- the check was verified to FAIL, not merely to pass. Reverting the d-chain literals to their pre-PR state (type_breakdown averaged: 5, inter_pn type: 'averaged') makes Part D red on exactly the two steps that were wrong, naming the call that refutes them. A guard that has never been seen to fail is the defect this PR is about, so this control is the point of the bean.

Part C's n/p baseline rows re-worded: they were justified as 'correct but unverified'. That is no longer true.
