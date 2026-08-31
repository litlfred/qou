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
