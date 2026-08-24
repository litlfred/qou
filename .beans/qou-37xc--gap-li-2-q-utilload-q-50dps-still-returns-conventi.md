---
# qou-37xc
title: 'GAP: _li_2_q_util.load_q_50dps still returns convention-C z — 21 callers, must be atomic'
status: todo
type: task
priority: normal
created_at: 2026-08-24T11:19:46Z
updated_at: 2026-08-24T11:20:25Z
---

The largest remaining convention-C site (`qou-cds1`, PR #5622). **Not attempted
as a drive-by** — sized, then deferred, for the reason below.

## The defect

[`computations/_li_2_q_util.py:312`](../computations/_li_2_q_util.py), inside
`load_q_50dps()`:

    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))       # = sqrt(q)/(q+1) = z_C

It should be `z_D = q**3/(q**2+1)`. One line.

The *anchor* half of this helper was already fixed on 2026-08-22 (default
flipped `None`→muon to `anchor="proton"`, beans `qou-dkm2` / `qou-v90i`), so
this is now a single, unentangled convention defect.

## Blast radius — measured, not estimated

29 files call `load_q_50dps`. Splitting by whether they bind the third return:

| | count | affected? |
|---|--:|---|
| **binds `z`** (as `z`, `ZMARK`, `z_markov`, `z_loaded`, `z_anchor`) | **21** | yes |
| discards it (`_`, `_z`) | 6 | no |
| mentions without unpack-assign | 2 | no |

Of the 21, **19 emit a committed witness**. So the change moves numbers in 19
witnesses. Full list in the PR-side inventory; the ones that matter for
sequencing:

- `probe_9b_perlambda_brane_tower.py` — **blocked** on `qou-5t68` (its upstream
  `borromean-binding-recompute.witness.json` is 17–23 % stale).
- `convergence_safe_vhat_tower.py` — already escalated separately; its `z_bar`
  site needs a bar-symmetry decision (`bar(z_C) = z_C`, `bar(z_D) = q^-4·z_D`).
- `derive_m_p_hecke_full_tower_50dps.py`, `vhat_tower_im_cancellation.py`,
  the three `deltalambda/*` probes — long-running; need the measured-timeout
  treatment, not a 900 s harness default.

## Why it must be ONE commit, not incremental

Converting some callers and not others is precisely the defect this PR exists
to remove. Every straddle found so far was a file computing at `z_C` while the
module it consumed or mirrored was already `z_D`:

    delta_lambda_borromean_ascaling edge-set  vs its own tower        16 %
    borromean_per_lambda_fr_probe::tower()   vs the fn it mirrors     16 %
    substrate/hecke_core_symbolic            vs pyhecke.gram       22.70 %

A shared helper is the worst place to create one, because the disagreement is
then between *callers* and invisible in any single file.

There is a direct precedent for doing it atomically: the anchor default flip
above changed the value for 28 call sites in 26 files in one change, and that
was right — the inventory was the work, the edit was one line.

## What the next agent needs

Not a conversion — a **baseline campaign**. Run all 19 witness-emitting callers
before touching the line, record which complete and which are already stale
(several will be: the deuteron ledger was 50 fields stale, `qou-58sa`), then
flip the line, re-run, and attribute. Budget the long ones explicitly;
`scripts/convention-c-convert-one.sh` takes a 5th `timeout_s` argument and
**aborts rather than diffing against a killed baseline**, which is the guard
that matters here.

Do **not** widen any precision baseline to absorb the movement.
