---
# qou-gcmn
title: 'EM-linking: the B_pp confound is now the limiting systematic. The per-pair Coulomb unit is held at its A=3 H_6 value across the whole A=3..41 series, so any A-dependence of the underlying strong bond is absorbed into kappa and is indistinguishable from the geometric factor under test. Computing B_pp at higher A (H_2A trace, previously called intractable) or bounding its A-dependence would let the ~4% residual actually discriminate coth-saturation from Vol^{-1/3}. This is the single biggest blocker to closing qou-o6ml'
status: todo
type: task
priority: normal
created_at: 2026-08-01T21:25:42Z
updated_at: 2026-08-31T06:53:20Z
---

## A=5 LANDED 2026-08-31 — the fourth point, and it says SATURATION

`computations/probes/bpp_higher_a_resumable_driver.py`, ~49 min, exit 0.

    A  bonds        B_tot MeV        avg/bond        marginal   marg ratio
    2      1    2.128360946     2.128360946     2.128360946          --
    3      2    3.932685215     1.966342608     1.804324269    0.847753
    4      3    5.554756841     1.851585614     1.622071626    0.898991
    5      4    7.100698353     1.775174588     1.545941512    0.953066

**The ratio of successive MARGINAL bonds rises monotonically toward 1** —
0.848, 0.899, 0.953 — which is the signature of a marginal bond converging to a
NONZERO limit. Saturation, not collapse.

NO asymptote is extrapolated. Four points fix the DIRECTION of the ratio
sequence, which is measured; fitting a limit would be a fit, and the mirror
series runs to A=39, eight times beyond the last measured point.

### Against the neutron chain (#6365, A=2,3,4)

nn marginals 2.4356, 0.9412, 0.3457 → ratios 0.3864, 0.3673. That is TWO
ratios, not enough to call the sequence constant rather than slowly declining,
and that distinction is NOT made. What they do show: ~0.37-0.39, with **no sign
of rising toward 1**, unlike pp.

So the defensible claim is the weak one: **the pp ratio sequence rises toward 1
and the nn sequence does not.** Whether nn converges to zero or to a small
nonzero value is UNDETERMINED and needs the A=5 neutron point — the same ~49
min the driver has now made survivable.

### Why it took three attempts

Two runs died silently at 30-40 min. I diagnosed memory; that was WRONG —
measured 0.96 GB against 15.1 GB available. The wall was wall-clock (~49 min
from the 58.5x cost ratio) and the defect was mine: `nohup` from inside a tool
call is not harness-tracked, so nothing owned or restarted them. Fixed by
per-partition checkpointing plus a tracked background run. The A=5 recompute
for the witness took **0.0 s**, entirely served from the checkpoint.
