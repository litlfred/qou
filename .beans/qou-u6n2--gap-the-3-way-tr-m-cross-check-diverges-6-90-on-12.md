---
# qou-u6n2
title: 'GAP: the 3-way tr_M cross-check diverges 6-90% on 12/12 pairs -- likely a CONVENTION mismatch presented as a precision failure'
status: todo
type: task
priority: normal
created_at: 2026-08-24T22:04:11Z
updated_at: 2026-08-24T22:04:50Z
---

## What is established

`cross_check_trM_wenzl_lr_1ppb` compares three independent tr_M compute paths at
substrate q0 against a stated **1 ppb (1e-9)** target. With its loader fixed
(this commit -- see below), all twelve pair-tests diverge:

    pair                        n  diverge  max |delta_rel|
    hoefsmit_vs_markov_peel     5      5         0.5462
    hoefsmit_vs_wenzl_lr        3      3         0.8965
    markov_peel_vs_wenzl_lr     4      4         0.7977

Range 6.5% (proton, hoefsmit vs peel) to 89.7%. Against a 1e-9 target that is
seven to eight ORDERS of magnitude out. The two simplest atoms -- proton and
neutron, hoefsmit vs peel -- are the closest at 6.5-7.0%, which is itself a clue:
whatever differs grows with A.

## The loader bug that hid two thirds of it (FIXED)

`load_peel()` read `doc["results"]`, but `markov-peel-atomic-tr-m.witness.json`
stores its rows under `doc["data"]["results"]` (6 rows; top level has none).
`atomic-tr-m-mpfr-50dps` uses the top level (5 rows), so the same loader shape
worked for one witness and silently returned `[]` for the other.

`.get(key, [])` makes a SCHEMA MISMATCH indistinguishable from a MISSING FILE.
So a THREE-way cross-check ran ONE pair-type and printed the other two as simply
absent -- `markov_peel atoms: []` -- since at least 2026-07-05, the date on the
committed witness. 3 of 3 diverging became 12 of 12.

Fixed with a `_rows_of(doc, key)` helper that tries both locations, plus an
explicit loud line when any path contributes zero atoms, distinguishing "file
missing" from "file present but no rows parsed". Silence is what let this sit.

## The second defect: the failure is invisible downstream

The witness records **`assertions: []` and `allPassed: true`** while 12 of 12
pair-tests diverge. Without `--strict` the producer exits 0. CI is
`workflow_dispatch`-only repo-wide, so `--strict` never runs. Nothing anywhere
reports that a 1-ppb gate is failing by eight orders of magnitude.

## THE LEAD -- convention, not precision

I have NOT established the cause and am not claiming one. The strongest lead is
that these paths use DIFFERENT CONVENTIONS and the script frames a convention
difference as a precision failure:

- The peel witness carries a field literally named **`bridge_is_color_blind`**,
  which says the bridge it compares against does not apply p/n colour weighting.
- AGENTS.md records `bring_color_weighted` as the canonical p/n convention (owner
  ruling 2026-08-15, R3) with **six live non-comparison files still off-canon**
  (bean `qou-cds4`).
- A colour-convention mismatch produces exactly this shape: an O(1) ratio, small
  for p/n (where the p/n distinction is weakest) and growing with A.

Ratios a/b for hoefsmit_vs_wenzl_lr are 5.143 (D), 9.662 (3He), 6.851 (T) -- NOT
a single clean structural factor, and tritium and 3He share n=9 while differing,
so it is not one missing normalisation constant either. Something
composition-dependent.

## What this is NOT

Not the anchor straddle. This producer compares a MUON witness
(`atomic-tr-m-mpfr-50dps`) against two PROTON ones -- a real straddle, and it is
why `reference_anchor_straddle_audit` flagged the file -- but 11.5 ppb cannot
produce 6-90%. The straddle is a separate, smaller defect in the same file.

Also note the audit's producer-side signal is MEANINGLESS here: this script
computes no q0 of its own, it only compares recorded witnesses. A pure comparison
script has no pin. That is a false-positive class in
`reference_anchor_straddle_audit` worth recording (bean `qou-dld9`).

## Next step

Establish whether the three paths agree once put on a common convention before
treating any of this as a compute defect. If they do, the script's framing is
wrong and its 1e-9 tolerance is being applied across a convention boundary; if
they do not, there is a real disagreement between three supposedly independent
routes to the same quantity, which is a much larger finding.
