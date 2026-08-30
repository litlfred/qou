---
# qou-w16s
title: 'GAP: borromean_per_lambda_fr_probe B_tower moved 3.3x on re-run — cause unidentified, witness held back'
status: completed
type: task
priority: normal
created_at: 2026-08-23T19:37:18Z
updated_at: 2026-08-23T19:44:03Z
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


---

## RESOLVED 2026-08-23 — it is the C->D ruling propagating, and the new number is correct

Bisected as planned. Lead (1) confirmed causally and quantitatively; the witness
is now committed.

**Timing.** The probe's committed witness is dated **2026-07-02**. Its input
`computations/y-lambda-at-q0.witness.json` was regenerated to convention D on
**2026-08-10** (`7665e0e4bf` "regen: 54 witnesses to convention D",
`506ac91350` "convention-D cascade"). The probe witness predates the cascade by
five weeks, so its `y_lambda` inputs were still convention C.

**Mechanism, from the y_lambda witness across that commit:**

    n=3, partition (3)       C 0.41539578633  ->  D 0.50540422650   x1.2167
    n=3, partition (2,1)     C 0.28092963398  ->  D 0.24729788675   x0.8803
    n=3, partition (1,1,1)   C 0.02274494571  ->  D 0.0             EXACTLY ZERO

The third row is the tell. Under convention D `y_(1^3) = 0` exactly -- the
two-row forcing, `ell(lambda) <= 2`, the same fact
`markovWeights_eq_jones_of_threeRow_eq_zero` encodes and that the mass chapter's
own decomposition writes into its index set.

The probe computes `contrib = {lam: ys[lam] * chi[lam]}` over a `chi` dict that
includes `(1,1,1)` (line 108-110). Annihilating that block and re-weighting the
surviving two is exactly what moves `B_tower`.

**Verdict: the refreshed value is the CORRECT one.** The committed 0.0487849 was
a convention-C number that the 2026-08-15 ruling excised. The new 0.1621985 is
its convention-D replacement. Citation is the ruling itself, not mpmath -- and
NOT the CODATA correction, which at 1.4 ppb could never produce 3.3x.

**Nothing was wrong with the probe.** This is a stale-input artifact of the
kind the excision exists to clear, and finding it is the excision working: a
convention-C value was still live in a committed witness five weeks after the
cascade that was meant to remove it.

Worth noting for the wider sweep: this witness was NOT in the 58 convention-C
witnesses `qou-z11r` triaged, because it carries no `z` spelling of its own --
it inherits C purely through `y_lambda`. Any C-surface measurement keyed on
source spellings or on `z` values will miss this whole class. That is a
detector-blindness note for `docs/audits/2026-08-15-detector-blindness-taxonomy.md`.
