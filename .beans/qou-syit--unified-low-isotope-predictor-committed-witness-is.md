---
# qou-syit
title: 'unified_low_isotope_predictor: committed witness is 24.8x stale AND its refresh is blocked by the raw-float64 ratchet'
status: todo
type: task
priority: normal
created_at: 2026-08-26T16:32:15Z
updated_at: 2026-08-26T16:32:56Z
---

Measured 2026-08-26 while answering "are all witnesses and their dependencies
updated?" on the low-isotope dashboard. Tree was clean before and after; every
re-run below was restored with `git checkout -- computations/`.

## The finding

`computations/unified-low-isotope-predictor.witness.json` is self-stale
(`scriptHash eba70b193ab6 -> a84f7373d484`), computed 2026-07-05, and its
recorded `commitSha 6949424f7a` resolves to nothing — bucket `rewritten` in
`witness_staleness_triage.py`, so "diff the producer first" is unrunnable and a
re-run is the only way to decide it.

Re-ran it. **It moves, hard.** Masked leaf diff (volatile keys removed:
computedAt/timestamp/durationMs/commitSha/scriptHash/environment/...):
**49 of 148 fields moved.**

    .data.isotopes[0].B_pred_MeV   -10570.825368453634 -> -261780.8500515504
    .data.isotopes[0].err_pct      -475285.92          -> -11767825.77
    .data.isotopes[1].B_pred_MeV   -14509.157577614    -> -340647.044194764

That is a **24.8x** move on the headline predicted binding. (Both values are
already nonsense as physics — a binding energy of -10 GeV — so this producer is
exploratory whatever its state; the point is that the committed witness does not
describe the committed producer.)

## Why it cannot simply be refreshed

The re-run emits, on stdout, a live gate warning:

    raw-float64: unified-low-isotope-predictor.witness.json: 70 raw float64
    field(s) would enter the witness -- .parameters.q_0, .parameters.m_e_MeV,
    .parameters.Q_beta_n_MeV, .parameters.E_0_MeV_per_cat,
    .parameters.tr_M_proton_at_q_0, .parameters.tr_M_neutron_at_q_0,
    .data.isotopes[0].T1_descended, .data.isotopes[0].T4_frobenius ...

So refreshing this witness would land **70 raw float64 fields** on `main`, which
the NO-FLOAT64 ratchet forbids and which `scripts/precommit-precision-warn.sh`
would flag on the commit. Note `q_0`, `m_e_MeV` and both `tr_M` values are in
that list: the *inputs* are float64, so per AGENTS.md rule 3 ("a float64 input
poisons the whole result") the payload resolves to ~1e-16 regardless.

**Do not fix this by rebaselining.** The fix is at the producer: carry
`mpmath.mpf` from the source and serialize with `_precision.fmt`. Baselines
drain, never grow.

Sibling beans on the same class (this one is the specific blocked refresh, not a
duplicate of the drain): `qou-5lw7` (1712 payload sites), `qou-xwjs`,
`qou-kn46`, `qou-7q56`, `qou-7kq3`.

## Two neighbours measured in the same pass, recorded so they are not re-measured

- **`low_isotope_mass_table` REFUSES, by design.** Exit 2 after 35.8 s with
  *"Re-run at >= the committed target_dps, or pass
  --allow-precision-downgrade if the downgrade is intended"* (bean `qou-7e1t`).
  Wrote nothing. This is a guard working correctly — a non-zero exit here is not
  a defect, and `--allow-precision-downgrade` would launder a downgrade into a
  refresh. Its witness stays stale until the precision is available.
- **`low_isotopes_binding_sweep` refreshes cleanly and moves a little.** Exit 0,
  35 of 134 masked fields move, at ~1e-8 relative on `Delta_lambda` and
  `B_pred_canonical_MeV` (7th-8th significant figure — small, but real at 60 dps,
  not noise). This one is a safe refresh whenever someone wants it.

## Not in scope of this bean

Whether `B_pred_MeV = -261780 MeV` is meaningful at all. It is not, but that is
the producer's physics, not its precision hygiene.
