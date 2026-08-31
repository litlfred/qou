---
# qou-wsfl
title: 'NO-FLOAT64 excision: 290 live q_parameter float imports across 269 files'
status: todo
type: task
created_at: 2026-08-31T03:47:45Z
updated_at: 2026-08-31T03:47:45Z
---


Owner ruling 2026-08-31: **no float64 — excise.** Measured surface, so the
campaign is enumerable rather than a gesture.

## The surface

`q_parameter` exports both a FLOAT and an MP form of every substrate constant.
Importing the float form is the contamination:

    Q      (float)  2.725e-17 relative vs the 50-dps closed form
    Q_MP   (mpf)    2.015e-50
    Q_INV_MP                  1.96e-50
    HA_MP                     1.914e-49

Live float-form import sites (comments excluded, `_deprecated/` excluded):

    290  import sites
    269  files

    285  Q            59  HA           48  Q_INV
      9  HBAR_Q        6  E_CROSS       4  LN_Q
      3  HBAR_Q_SQ     2  S_SKEIN

(A further 286 sites are under `_deprecated/` and can be ignored.)

## Done: `hecke_core_legacy` (commit `b3d300d04`)

One file, but the hard one, and it maps the shape of the rest.

- imports → `Q_MP` / `Q_INV_MP` / `HA_MP` / `E_CROSS_MP`
- YSN matrices, `_identity`, `_matmul_dim` accumulator, and the object identity
  all seeded with mpf rather than `0.0` / `1.0` / `np.eye`
- **scipy.sparse had to be dropped**: it refuses dtype object outright, so once
  `q0`/`qi` became mpf the YSN generators could not live in a `csr_matrix`.
  Replaced with `_CooMPF`. Storing them as float64 instead would have put the
  float back exactly where the excision removed it.

Verified: `partition_character_sigma1((3,1))` agrees with the exact 50-dps
reference to **4.73e-50**, against ~2.7e-17 before. 145 tests pass.

## ⚠️ What this campaign will keep running into

1. **scipy/numpy boundaries.** `scipy.sparse` cannot hold mpf at all, and
   `np.eye`/`np.zeros` default to float64. Any file using them for q₀-derived
   data needs a container change, not an import change.
2. **Downcasts at result boundaries.** Swapping the import is not sufficient if
   the file then throws the precision away. `hecke_core_legacy` still does:
       `_trace_dim`          → `float(np.trace(M))`
       `atom_character_raw`  → `float(chi), float(log_norm)`
       three sites           → `hbar_like = float(h)`
   These are consumer-facing signature changes — a caller expecting a float
   gets an mpf — so they need their consumers checked, not just an edit.
3. **Cost.** mpf operands keep matrix work in per-element Python arithmetic
   instead of BLAS. That is the accepted price under the directive, but it
   makes some producers slower and a few (see `qou-c7g8`) infeasible.
4. **Every regenerated witness will move**, from ~17 good digits to ~50. That is
   the correction landing, not drift — but a sweep will look alarming.

## Suggested order

Producers whose witnesses are already q₀-anchored and cheap to regenerate
first; the numpy/scipy-heavy ones last, since they need container work. Do NOT
sweep all 269 in one change: the value movement is real and needs to land in
reviewable batches.

## 2026-08-31 — file 1 of 269 COMPLETE: `hecke_core_legacy.py`

Audited float64-free, comments stripped: **0 `math.*` calls, 0 `float()` casts,
0 `dtype=float`, 0 live `scipy.sparse` references.**

Worth reading before starting file 2 — an import swap was about 10% of the work.
What the other 90% was:

1. **scipy.sparse had to be replaced, not adapted.** It refuses dtype object
   outright, so mpf cannot live in a `csr_matrix` at any price. Replaced with
   `_CooMPF`. Anything storing q₀-derived data in a scipy matrix needs the same.
2. **`math` is float64-only.** 17 call sites, including `math.log(q0)` taking an
   mpf argument directly. The module now imports `math` nowhere, so it cannot
   creep back — worth copying that discipline.
3. **Seeds and accumulators.** `0.0` / `1.0` / `np.eye` are exactly
   representable, so they cost no precision — but they make arrays MIXED, which
   forced mpmath to convert an operand on nearly every multiplication (measured
   6,186,121 `from_float` calls before the excision).
4. **Rescaling exponents are the sneaky ones.** `log_norm` was seeded `0.0` and
   downcast on return. It reconstructs `chi * exp(log_norm)`, so a 1e-17
   relative error in a log_norm of order 100 lands as ~1e-15 in the result —
   *worse* than float64. Look for any log/scale bookkeeping.
5. **Downcasts at the exits.** `_trace_dim` → `float(np.trace(M))`,
   `atom_character_raw` → `float(chi), float(log_norm)`. The whole expensive mpf
   pipeline was discarded at the last step. These are consumer-facing type
   changes: check the callers, don't just edit.
6. **Partial excision BREAKS things.** Two self-inflicted breakages here: making
   the diagonals mpf while `math.sqrt` still produced float64 off-diagonals left
   the matrices mixed and less precise than before; and swapping in `_CooMPF`
   broke `_crossing_in_partition`, which called `.toarray()`. Finish a file or
   revert it — do not leave one half-done.

Result: `partition_character_sigma1((3,1))` matches the exact 50-dps reference
to **4.73e-50**, against ~2.7e-17 before — 33 orders recovered.

Remaining: 289 sites / 268 files.
