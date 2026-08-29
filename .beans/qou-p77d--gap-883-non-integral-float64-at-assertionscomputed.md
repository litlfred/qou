---
# qou-p77d
title: 'GAP: 883 non-integral float64 at .assertions[].computed/.expected across 300 witnesses — the class #5910 deferred'
status: todo
type: task
priority: normal
created_at: 2026-08-29T02:28:37Z
updated_at: 2026-08-29T06:33:26Z
---

## 2 of the 883 are already drained (PR #5952, bean `qou-t39x`) — 2026-08-29

Recorded so the tranche does not re-open them, and because the instance
reproduces this bean own reasoning from the opposite direction.

`computations/probes/qbeta_exponentiated_per_block_probe.py` had
`computed = float(results["proton"]["c"][2])` and `expected = -1.0` in its
`scale_fix_c2_minus1_solvable_and_exact` assertion. Both sat in the
INTEGRAL-EXCUSED majority — the value is exactly -1.0 — and both are now
`mp.nstr(..., 40)` and the string "-1", fixed at the producer and re-run, which
is the route this bean prescribes for a `computed` field.

It is a live instance of the "integral is safe by ACCIDENT OF CURRENT VALUE"
warning, and a sharp one: the cast was discarding a 35-DIGIT agreement (the
assertion tests |c+1| < 1e-35 at 60 dps) in order to report -1.0. Nothing was
excused about it except the current value.

Worth carrying into the sweep design: it surfaced from the OTHER end. The
raw-float64 ratchet went red on the same assertion tolerance, a bare 1e-35
literal — the #5910 declared-threshold class, repairable textually. Fixing that
put me inside the function, where the `computed` cast was visible three lines
up. The two classes co-occur in the same assertion dict, so a producer opened
for a #5910-style tolerance fix should have its `computed`/`expected` checked in
the same pass rather than left for a second visit.

After: raw-float64 ratchet NEW dirty 0, REGRESSED 0; integral-float population
down by exactly the 2 fields.
