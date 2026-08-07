---
# qou-t0rf
title: 'float64 entry point: whitehead_c_sigma_torsion.py reads shapes via mp.mpc(complex(s)) — capped at ~16 digits despite dps=40'
status: completed
type: task
priority: normal
tags:
    - compute
    - float64
    - precision
created_at: 2026-08-07T18:40:00Z
updated_at: 2026-08-07T21:20:00Z
---

## The defect

`computations/whitehead_c_sigma_torsion.py` line ~80:

    z = [mp.mpc(complex(s)) for s in M.tetrahedra_shapes('rect')]

`complex()` is float64, and `tetrahedra_shapes` is called without
`bits_prec`. So the computation is capped near 16 digits regardless of
`mp.mp.dps = 40`, and its own `4_1` values wobble at digit 16 across runs —
its reported "match ~15 digits" figures are not what they appear to be.

## The fix

    for s in M.tetrahedra_shapes('rect', bits_prec=BITS):
        z.append(mp.mpc(mp.mpf(str(s.real())), mp.mpf(str(s.imag()))))

with `BITS` derived from `mp.mp.dps`, and `set_compute_dps()` called so mpmath
is not left at its default `dps=15`. Both halves are required: reading SnapPy
at 212 bits achieves nothing if mpmath parses the strings back down to a
double. `computations/probes/one_loop_triangulation_invariance_probe.py` does
it correctly and is the worked example.

## Scope

This is an instance of the class PR #4677 tracks; it does NOT cause the
triangulation-dependence in bean `qou-fl4t` (that reproduces at 212 bits).
Fixing it will change the reported digit counts, not the conclusions.

<!-- 2026-08-07T21:05:00Z branch claude/beans-fl4t-t0rf — claimed: high-precision shape read -->

---

## 2026-08-07 — DONE.

`whitehead_c_sigma_torsion.py` now reads shapes at `bits_prec` derived from
`mp.mp.dps`, converting through decimal strings instead of `complex()`.

Effect is larger than expected. The `4_1` calibration went from
`1.73205080756887777` — wobbling at digit 16 across runs — to
`1.732050807568877293527446`, i.e. sqrt(3) exactly at the working precision
(relative difference 0, so the script's digit counter saturates at its 999
sentinel). float64 was the binding limiter on every digit count that file
reported.

Does NOT change any conclusion: the triangulation-dependence in `qou-fl4t`
reproduces at 212 bits and is unrelated.
