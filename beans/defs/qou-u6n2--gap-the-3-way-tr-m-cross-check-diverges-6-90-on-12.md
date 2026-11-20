---
# qou-u6n2
title: 'GAP: the 3-way tr_M cross-check diverges 6-90% on 12/12 pairs -- likely a CONVENTION mismatch presented as a precision failure'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T22:04:11Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
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


## 2026-08-24 RESOLVED for 2 of 3 path-pairs — and my convention hypothesis was WRONG

The lead recorded above ("likely a CONVENTION mismatch") is **refuted**. Two
separate, mundane causes account for everything except the Wenzl-LR leg.

### Cause 1 — the peel witness was STALE (7% .. 55%)

Its own rows carry `bridge_witness_value` and `abs_diff_vs_bridge ~ 1e-8`: it
AGREED with its bridge to eight digits when it ran, on 2026-08-09. The bridge was
then regenerated on 2026-08-22 (`ecd6594d436`, "q0(ibbr): SOLVED — my own
migration commit, found by bisect"), after `5eb5f275d20` on 08-19 found "the muon
tr_M witness held PROTON numbers — collateral of the pin corruption". Every
bridge value moved; the peel witness did not.

Re-ran the producer (161.6s wall, all six atoms). helium-3 now matches its bridge
at **|diff| = 1.4e-50**. `hoefsmit_vs_markov_peel` collapsed from 0.065..0.55 to
6.9e-8 .. 2.5e-7.

### Cause 2 — the residual 1e-7 was the SAME straddle as PR #5723

Those residuals are not merely similar to the `tr_m_q_hecke_seminormal`
straddle values, they are IDENTICAL: 7.84e-8 proton, 1.51e-7 deuteron, 2.52e-7
helium-3. The peel and Wenzl-LR witnesses are PROTON; the base-name Hoefsmit
witness is MUON. Pointed the cross-check at the proton twin:

    hoefsmit_vs_markov_peel : n=5  diverge=0  max |delta_rel| = 4.4e-50

Five of five OK. Second confirmed site of the defect `reference_anchor_straddle_audit`
(#5727) was built to find.

### What the colour evidence actually said

I read `bridge_is_color_blind: True` as support for a convention mismatch. The
producer's own log line reads *"color-weighting Δ (expected; bridge is
color-blind)"* and reports that Δ as **1.4e-50** — i.e. there is NO colour
difference in these values at all. The field names a distinction that does not
move the number. I inferred a cause from a field NAME without checking the
magnitude it was attached to.

### STILL OPEN — and now isolated

The Wenzl-LR path disagrees with BOTH others by 80–92%:

    hoefsmit_vs_wenzl_lr     n=3  diverge=3  max 0.8965
    markov_peel_vs_wenzl_lr  n=4  diverge=4  max 0.9223

Now that the other two agree at 1e-50, this is a clean single-path question
rather than a three-way mess. Note the two agreeing paths bracket it, so the
Wenzl-LR value is the outlier, not the reference. Ratios (5.143 D, 9.662 3He,
6.851 T) are still not one clean factor and T vs 3He differ at equal n=9.

### The second defect stands

The witness STILL records `assertions: []` / `allPassed: true` while 7 of 12
pairs diverge at ~0.9. Unchanged by any of the above.


## 2026-08-24 CLOSED — the Wenzl-LR divergence was documented at the source all along

I recommended the Wenzl-LR path as "the most tractable open question I've
surfaced today". **It is not open.** The answer is in
`rho_k_full_via_wenzl_lr.py`'s own docstring, dated 2026-05-17 and found by THIS
cross-check:

> "the Wenzl LR identity chi^lambda(b1 (x) b2) = Sum c^lam_{mu,nu} chi^mu chi^nu
>  applies to TENSOR-PRODUCT (disjoint) braids only. The canonical atomic braid
>  `atom_canonical_crossings(Z, N)` is NOT a tensor product -- it includes
>  inter-nucleon arc crossings. This script therefore computes
>  |tr_M(b_p (x) b_n (x) ...)|, NOT |tr_M(b_canonical(Z, N))|. The two diverge by
>  ~80% relative on D, T, 3He."

So the cross-check has been applying a 1e-9 tolerance across a **known
inequality of quantities** and reporting the result as a precision failure. The
~0.9 is a SCOPE difference -- the disjoint product omits exactly the
inter-nucleon crossings the canonical braid carries -- and `atomic_mass_via_rho_k`
layer 4 was already disabled because of it.

**One `sed -n '1,55p'` on the producer answered what two rounds of numerology on
the ratios could not.** The corpus-grep checklist exists for this; I ran it on
the cross-check's identifiers and not on the producer that supplies the outlying
leg.

### What changed in the code

Those two pair-types are now reported **SCOPE**, carry
`compares_same_object: false` plus a `scope_note` naming the reason, and are
excluded from `any_diverge`.

### And that unblocked the assertion defect

Wiring assertions was blocked on knowing WHAT to assert. With the Wenzl-LR pairs
identified as a different object the answer is unambiguous: assert the
same-object comparisons, assert nothing about the scope ones. The witness now
carries **5 assertions, all passing**, where it carried `assertions: []` and a
vacuous `allPassed: true` while every pair diverged.

    hoefsmit_vs_markov_peel : n=5  diverge=0  max |delta_rel| = 4.4e-50   ASSERTED
    hoefsmit_vs_wenzl_lr    : n=3                                        SCOPE
    markov_peel_vs_wenzl_lr : n=4                                        SCOPE

My first version asserted `expected="< 1e-9"` -- a STRING, which the builder
coerces numerically, so all five failed on values as small as 2.6e-50. Caught by
reading the output rather than the exit code. Corrected to `expected="0"` with
`tolerance="1e-9"`.

### Net

Every part of the original 12-of-12 finding is now accounted for: a loader bug
(#5729), a stale witness, an anchor straddle (#5732), and a documented
scope difference. Nothing about the tr_M compute was wrong.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8391, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
