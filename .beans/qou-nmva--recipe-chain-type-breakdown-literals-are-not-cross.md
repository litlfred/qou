---
# qou-nmva
title: Recipe-chain type_breakdown literals are not cross-checked against atom_canonical_crossings
status: todo
type: task
priority: normal
created_at: 2026-08-14T20:04:06Z
updated_at: 2026-08-14T20:07:07Z
parent: qou-1295
---

From the qou-uzk0 sweep. build_atomic_braid_recipe_{p,d,n}_chain.py record type_breakdown as hand-written literals with trust_basis=DERIVED and operation strings claiming they match atom_canonical_crossings(Z, N, include_inter=True). Nothing checks that claim. The d-chain's literal said {sigma: 11, sigma_inv: 7, averaged: 5}; truth is averaged 4 + averaged_weighted 1 -- wrong from the moment the classifier learned the distinction, and it stayed wrong under a DERIVED label. p and n are correct today ONLY because a single nucleon has no p-n bond; they are equally unverified. Fix: a Part-A2-style check comparing each chain's recorded breakdown against a live Counter(atom_canonical_crossings(Z, N)).
