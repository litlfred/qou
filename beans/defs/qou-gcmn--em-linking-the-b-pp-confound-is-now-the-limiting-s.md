---
# qou-gcmn
title: 'EM-linking: the B_pp confound is now the limiting systematic. The per-pair Coulomb unit is held at its A=3 H_6 value across the whole A=3..41 series, so any A-dependence of the underlying strong bond is absorbed into kappa and is indistinguishable from the geometric factor under test. Computing B_pp at higher A (H_2A trace, previously called intractable) or bounding its A-dependence would let the ~4% residual actually discriminate coth-saturation from Vol^{-1/3}. This is the single biggest blocker to closing qou-o6ml'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T21:25:42Z
updated_at: 2026-11-17T07:52:47Z
parent: qou-10v9
---

## Answered in sign and low-A scale (PR #6336) — the bean never recorded it

`computations/probes/bpp_higher_a_sparse_probe.py` (merged 2026-08-31, PR
#6336, *"research(qou-gcmn) ANSWERED: B_pp DECLINES with A"*) and its
follow-on `qou-23dn` establish this confound's **sign** and its **low-A
scale**. This bean stayed `todo` with a title-only body, so a corpus-grep on
it reads as untouched — the path-6 trap that made `qou-0hdx` reopenable on a
stale title. Recording it here.

Measured `B_pp` per bond: **2.128360946 → 1.966342608 → 1.851585614** MeV at
`A = 2, 3, 4`. Committed `kappa_correction`: 1.0823957827 (`A=3`),
1.1494801700 (`A=4`).

## What 2026-09-07 adds: the confound is ~80% of the whole signal

`docs/audits/2026-09-07-em-linking-kernel-and-exponent-are-degenerate.md`
puts the drift in log-slope form. For `kappa = F(alpha)`, `alpha ~ A^p`, and
`B_pp ~ A^(-delta)`, the mirror series measures exactly one scalar:

    s*p + delta  =  -dln(kappa)/dln(A)  =  0.2604989 +/- 0.00722

so the drift is not a scatter nuisance — it is an **additive bias on the one
number the front measures**. From the committed corrections above, the local
drift is

    delta(A=3 -> 4) = 0.20903   =   80.2% of the measured 0.26050.

Consequence, and it is not convenient: `0.26050` is an **upper bound** on
`s*p`. `H_coth`'s single coincidence — `c0 = 0` predicting `p = 0.33007`,
which is `1/3` to 0.34 sigma — holds only at `delta = 0`. At the measured
local drift the same prediction is `p = 0.06522`, **28.19 sigma** from 1/3.

NOT EXTRAPOLATED: #6336 refuses to carry a three-point decline across a
factor of ten in `A`, and that refusal is honoured — `delta(A=3->4)` is used
as a measured local SCALE, never as a value for `delta` over `A = 3..63`.

## Still open (do not close)

`delta` across the full series. #6336's own named next step is `A = 5, 6`.
Per the audit's constructive form — derive any TWO of {s, p, delta} and the
third is predicted — this is the cheapest leg, and now the highest-leverage
one on the whole EM-linking front.


## A = 5 attempt, 2026-09-07: computable at 55 min, but this container cannot reproduce the A = 2 anchor — so no value is usable

Ran `bpp_higher_a_sparse_probe.py 2 3 4 5` (backgrounded, `-u`, teed log).
Two results, one useful and one blocking.

**USEFUL — A = 5 is reachable, and here is its cost.** It completed:

    A    n  cross  parts  maxdim       B_tot MeV       B_pp/bond    secs
    5   15     59      8    2002  0.354993193547  0.0887482983868  3302.4

55 minutes, `n = 15`, max 2-row dim **2002**. The probe previously topped out
at A = 4 (max dim 297). So the route does extend, and the bean's "A = 5, 6 are
the obvious continuation" is right about A = 5. **A = 6 is a different
matter**: `n = 18`, max 2-row dim **13260**, so ≈45× the A = 5 cost again by
the probe's own `O(dim^2 * nnz)` scaling — of order 40 hours. Not attempted,
and not asserted as impossible; just budget for it.

**BLOCKING — the method-validation check FAILED and the numbers are not
usable.** The probe's first check reproduces the committed
`B_pp(A=2) = 2.12836094575708`. This run gives **0.642115075408566**, and the
disagreement is NOT a uniform normalisation:

    A        committed    this run    committed/run
    2          2.12836     0.64212           3.3146
    3          1.96634     0.32584           6.0346
    4          1.85159     0.16853          10.9866

The factor grows by a constant **1.82 per unit A** (6.0346/3.3146 = 1.820,
10.9866/6.0346 = 1.821), so the two disagree in **shape**, not just scale:
committed declines 13.0 % over A = 2 → 4, this run declines 73.8 %. Whatever
this container computed, it is a different quantity, and **every B_pp number
from this run is discarded**.

The witness was **reverted, not committed** — per the standing rule that
leaving a witness honestly stale beats committing one that measures the
harness. This container is missing `scipy` and `clarabel`; the committed
witness's `environment` block is **empty**, so there is nothing to diff
against, which is its own small defect.

**So delta beyond A = 4 is still unmeasured, and the "cheapest leg"
recommendation needs a caveat**: it is cheap in *compute* (55 min for A = 5)
and currently blocked on *environment*. Reproducing the committed A = 2 anchor
is the prerequisite for any further A.

## A defect in the probe itself, found on the way

Its PASS text and verdict are **hardcoded** and disagree with its own computed
table:

- line 225 (check 2 PASS): `"2.128 -> 1.966 -> 1.852 MeV, a {drop4} % drop by
  A=4"` — quotes the COMMITTED values while the table shows 0.642 / 0.326 /
  0.169, and `drop4` printed **86.179 %**, which is the **A = 5** row, not
  A = 4 (A = 4 is 73.754 %). Two errors in one sentence.
- line 285 (verdict): same three committed values, same problem.
- line 206 (check 1 PASS text): *"agrees to <1e-10"* — printed under a check
  that **FAILED**, because the text is a fixed string rather than derived from
  the comparison.

So a reader of the output sees a confident narrative that is not about the run
in front of them. This is the same class AGENTS.md documents for
`qbeta_ck_truncation_order_analysis.py` ("its hardcoded prose disagreed with
its own computed table"). Worth fixing at the producer: derive the quoted
numbers from the computed table, and gate the check-1 text on the check.

## Still open (do not close)

`delta` across the series — unchanged, and now with a named prerequisite.

## Implementation & Witness Progress (PR #8264)
- Branch: `qou-10v9-e58e-gcmn-vbyi-vtlj-xy5f` (`248efc097170676991e07dd557f09bee0827f2bc`), PR: `litlfred/qou#8264`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityIsospinSplitBppConfoundSingletTensorInvarianceDeltaFourValuesAndOrderingDofShift.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/bar_parity_isospin_split_bpp_confound_singlet_tensor_invariance_delta_four_values_and_ordering_dof_shift_probe.py` -> `computations/probes/bar-parity-isospin-split-bpp-confound-singlet-tensor-invariance-delta-four-values-and-ordering-dof-shift.witness.json` (`allPassed: true`, `scriptHash: e7d87b167c3f`, `scriptCommitSha: 7d111fc9111a5ac911879c633afd63652e0f6384`)
