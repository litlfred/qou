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
updated_at: 2026-08-09T17:00:00Z
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

---

## 2026-08-08 — the ratchet backlog is drained; gate exits 0.

Branch `claude/drain-float64-ratchet`, PR #4729. Scope grew from this bean's
single entry point to every witness the raw-float64 audit flagged as NEW or
REGRESSED: 15 NEW (573 fields) + 1 REGRESSED (43) → **0 and 0**.

`witness_raw_float64_audit.py --strict` now exits 0.

Three categories, and they wanted different fixes:

1. **Encoding, not measurement** (6 probes, 45 fields). Every value was
   `1.0 if <predicate> else 0.0` against `tolerance=0.5` — a bit written as a
   float. Strings, no numerics involved.
2. **Coerced at the sink** (4 em-linking producers, 171 fields). mpmath end to
   end, `float()`-ed only on the way out. `mp.nstr(x, 8)` at each sink, mpf kept
   alive wherever a value is also compared or ordered. 8 digits because `kappa`
   enters as an 8-digit string — the old 17-digit output was fake precision.
3. **float64 genuinely upstream** (5 producers). Real ports: an mpmath adaptive
   quadrature for the Borromean ACN; `gram_matrix_mp`/`tr_m_mp`/`hm_mp` +
   clarabel-MPFR for the three pyhecke probes; `Q_MP`/`HA_MP` for
   inverse-markov.

**Four wrong numbers fell out of category 3, none of them serialization:**

* `ACN(Borromean pair)` was `1.6426377156933236`, published to 17 digits and
  correct to ~6. The integrand carries `|det|` and the determinant has the
  closed form `a*b*(b cos t − a sin s)`, so there is a KINK cutting the domain
  and the midpoint rule converges algebraically, not spectrally. Split at the
  kink: `1.642637681773124472637643`. Off by 3.4e-8.
* The Brunnian linking control would have gone vacuous under the symmetry fold
  I used for speed — the signed integrand is odd under `(s,t) → (−s, π−t)`,
  which preserves the quarter domain. Caught because it returned exactly `0.0`.
  Control stays on the full domain.
* `qbeta-lorentzian-gram-offset`'s "signature transition at q_c ≈ 1.03, a
  genuine q threshold below the substrate point" **does not exist**. The old
  control moved `h` to the new q but left the Markov weight `z` at q₀ — the
  Gram of no q at all. Consistently, λ_min stays below −0.7 on [1, 2.5] and
  reaches exactly −3/4 at q = 1; what vanishes at q = 1 is a POSITIVE
  eigenvalue λ₂ ≈ h/2, the classical degeneracy. Structural claim strengthened.
* `qbeta-confinement-sdp-offset-homogeneity` established homogeneity by
  measuring `x*(n) = (n/n₀)x*(n₀)` to 1e-9. That was scipy/HiGHS crossing over
  to a VERTEX — any vertex-returning solver reproduces it regardless of the
  program. Chasing the flip under clarabel found something better: `min t·x = 0`
  and `y0* = 0` at every n, so the objective is DEGENERATE and the LP never
  determined `x*` at all. Conclusion unchanged, now resting on the cone-slice
  identity checked at 50 dps with no solver.

Also found: `em-linking-residual-structure` was **stale against its own input**
— computed 21:29:48 from a mirror series regenerated at 21:51:01 the same day
and never re-run. Its prose quoted the stale figures back at itself; the
`reading` text now interpolates from live values. Conclusion strengthens on the
extended ladder (discriminating gap 0.38 → 0.75).

Library changes, all additive, `G`/`G_INV`/`TR_M` verified byte-identical by
hash so none of the ~76 pyhecke importers moves:
`gram.hm_mp` / `gram.h_mp` (the mp side had no general `(c·σ + d·I)`, so a
braid word with an inverse had no expression), `gram_matrix_mp(q=...)`
(replaces a control that assigned to the module global `_gram.h`), and
`lp_dual_solver` accepting strings IN as well as out (the MPFR solver already
returned decimal strings; `_lp_result_from_dict` `float()`-ed them and threw
~35 digits away at the last step).

Guard default off → **warn**. Not `raise`: ~1580 baseline witnesses still carry
pre-ratchet float64 and raising would break their producers for debt they are
not adding to. The audit gate ENFORCES; the guard LOCATES, printing exact JSON
paths at the producer. `=1` still raises, and every drain here ran under it.

Two things this did NOT touch, both known and neither blocking the gate:
the ~1580 baseline witnesses (540k fields), and the fact that the guard sits at
`WitnessBuilder.save()` — a producer writing its own `json.dump` bypasses it,
which is exactly how `inverse-markov-qvalues` regressed unnoticed.

---

## Merged 2026-08-09 — PR #4729, `25387e2a4`

Shipped with the guard at `WitnessBuilder.save` (default `warn`) and 15 drains.
The follow-on debt main accrued in the meantime is `qou-mnrd`, not this bean.
