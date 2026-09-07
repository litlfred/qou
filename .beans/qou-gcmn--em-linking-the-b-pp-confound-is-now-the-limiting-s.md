---
# qou-gcmn
title: 'EM-linking: the B_pp confound is now the limiting systematic. The per-pair Coulomb unit is held at its A=3 H_6 value across the whole A=3..41 series, so any A-dependence of the underlying strong bond is absorbed into kappa and is indistinguishable from the geometric factor under test. Computing B_pp at higher A (H_2A trace, previously called intractable) or bounding its A-dependence would let the ~4% residual actually discriminate coth-saturation from Vol^{-1/3}. This is the single biggest blocker to closing qou-o6ml'
status: todo
type: task
priority: normal
created_at: 2026-08-01T21:25:42Z
updated_at: 2026-09-07T08:19:14Z
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
