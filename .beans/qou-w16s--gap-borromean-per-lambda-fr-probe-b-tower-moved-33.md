---
# qou-w16s
title: 'GAP: borromean_per_lambda_fr_probe B_tower moved 3.3x on re-run — cause unidentified, witness held back'
status: todo
type: task
priority: normal
created_at: 2026-08-23T19:37:18Z
updated_at: 2026-08-23T19:38:11Z
---

Found refreshing witnesses for the C->D excision (`qou-cds1`, PR #5565).

## The measurement

`computations/probes/borromean_per_lambda_fr_probe.py` re-run on current main,
SOURCE UNMODIFIED. Against its committed witness, **174 numeric mathematical
fields move** (ephemeral/provenance excluded), the largest by a factor of 3.3:

    data/results/w_chi_over_d::both/rows/3H/B_tower
        0.048784915468845884  ->  0.16219848276665358      rel 2.325
    data/results/w_chi_over_d::both/rows/3H/net_over_target
        0.005751703020948672  ->  0.019123073072003473     rel 2.325
    data/results/w_chi_over_d::both/rows/3He/net_over_target
        0.005546793980182176  ->  0.018432687238325276     rel 2.323

This is NOT a version artifact. For comparison, the other three producers in the
same batch moved by 1.8e-11, 0 and 0 mathematical fields respectively. A 3.3x
move in a binding tower is a result change.

## Why the witness was HELD BACK, not committed

The rest of the batch is committed with its ledger; this one is restored to the
committed value. Committing a 3.3x change whose cause I cannot name would put an
unexplained number into the corpus under a commit message about mpmath — exactly
the mislabelling this branch has been correcting.

## Leads, none verified

The probe imports `q_parameter.Q_MP` and `codata_constants.M_E_MEV` directly,
so it is proton-pinned and reads CODATA. Candidate causes, in rough order of
prior:

1. **The convention C->D switch in the binding channel.** `w_chi_over_d` weights
   by chi over dimension; `wedderburn_jones_markov.y_lambda_at` and
   `closed_form_tau_M.markov_z` both moved to D on 2026-08-09, and main landed
   further habiro convention-D regenerations TODAY (`cde2fbcd89`,
   `4a217671fc`). If so this is the owner's own ruling propagating, and the new
   number is the correct one — but that has to be shown, not assumed.
2. The CODATA literal correction (`98acdf5024`) — but that is a 1.4 ppb input
   change and cannot produce 3.3x.
3. A genuine defect introduced upstream.

(2) is almost certainly too small; (1) and (3) both need checking.

## Next step

Bisect the probe's inputs across the window between the committed witness's
`computedAt` and now: recompute `B_tower` for 3H with the OLD y_lambda/markov_z
and with the new, and see whether the 3.3x is fully accounted for. If it is,
commit the refreshed witness citing the D ruling. If it is not, the residual is
a defect and this bean becomes its tracker.

Do NOT commit the refreshed witness before that is resolved.
