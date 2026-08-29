---
# qou-1bgk
title: 'Stale-on-main witnesses found while replanting: two that do not reproduce from their own producer'
status: todo
type: task
created_at: 2026-08-29T20:03:46Z
updated_at: 2026-08-29T20:03:46Z
---

Both found by A/B — reverting my change entirely and re-running MAIN's own
code in this container. Neither is caused by anything on this branch.

1. binding-per-block-magnitude-a3.witness.json
   err_perblock moves ~32% on a plain re-run:
       d     0.03575207656005921  ->  0.04725387641600928
       t    -0.6165350072062381   -> -0.5614851013102126
       3he  -0.5508488187149049   -> -0.5157166810413218
   AME_MeV is unchanged (2.2245662, 8.4818, 7.718), so this is a PREDICTION
   moving while its comparison target holds. The committed witness does not
   reproduce from its own producer.

2. bar-pairing-binding-observable-extension.witness.json
   Committed 2026-07-18 with `engine: rust+mpmath` and
   B_arch_MeV = 2.3043266203187662. This container takes the python path and
   gives 2.330026199174927 — a 1.1% difference. Recorded as an OBSERVATION,
   not a claim: it may be a rust-vs-python implementation discrepancy or
   simply six weeks of code drift, and separating those needs a machine with
   the rust extension. Worth separating, because a 1.1% split between two
   implementations of the same quantity would matter a lot more than a stale
   witness does.

SEPARATELY, the qou-mass vendor mirror is drifted on main independent of any
of this: `sync-qou-mass-vendor.py --apply` regenerates _li_2_q_util.py,
experimental_constants.py and m-p-borromean-verification-50dps.witness.json.
Not folded into the replant branch because none of it is mine, but it is a
red staleness gate that a one-line command clears.
