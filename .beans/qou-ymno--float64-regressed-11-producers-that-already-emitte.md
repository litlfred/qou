---
# qou-ymno
title: 'float64 regressed 11: producers that already emitted float64, now emitting more rows'
status: todo
type: task
created_at: 2026-08-24T07:16:57Z
updated_at: 2026-08-24T07:16:57Z
---

From witness_raw_float64_audit after the drain (1e18c44fd) and my two fixes:
regressed 13 -> 11, drained 72 -> 74, dirty 1391 -> 1380.

WHAT THE 11 ARE, AND ARE NOT
  ZERO fields anywhere went from an mpf string to a float64. Checked leaf by
  leaf across all 13 originals. The witnesses GREW (leaves 448->625, 55->100,
  83->213 ...) and the new float fields were ABSENT before -- the producers
  already emitted float64 in those slots and the drain made them emit more
  rows. This is the PR #4677 producer-side backlog, which the audit itself
  names as `drain_owner`, not new damage.

TWO WERE GENUINE AND ARE FIXED
  gg-production-bond-probe    collapse_factor was 0.301 / float64-epsilon
                              -> 904080051203560. Fixed in 681796995.
  per-nucleon-shift-derivation fit_residuals: numpy lstsq returned an EMPTY
                              residuals array until EMPIRICAL_SHIFT grew past
                              two atoms, so the field reported the SHAPE of
                              the input. Ported to mp.qr_solve; the fit turns
                              out to have an exact rational answer (19/20,
                              -219/130, 99/65). Fixed in 43e14ea47.

THE beta-decay-matrix "DOWNGRADES" ARE NOT DOWNGRADES
  17 of the 19 nominal int->float entries are there: crossing_coefficients
  .{pp,nn,mixed}.c: 1 -> 1.0 and .pp.d: 0 -> 0.0. Exactly representable, no
  precision lost. And the SOURCE is byte-identical at the merge-base and now
  (`c_pp, d_pp = 1.0, 0.0`), so the committed witness's ints came from a
  SUPERSEDED source version. The drain made a stale witness agree with source
  that was already float64 -- exactly the drift a drain exists to remove.

  A real fix here is an mpf migration, not a literal edit: this producer does
  `from q_parameter import Q, Q_INV, HA, S_SKEIN` -- the FLOAT64 family. HA is
  float64, so `-HA` and `-0.5*HA` are float64 no matter what the `1.0` says.
  Changing `1.0` to `1` while d stays float64 would be cosmetic. The producer
  also imports mpmath but never calls set_compute_dps(), so a naive migration
  would run it at 15 dps -- WORSE than the float64 it replaces. Whoever takes
  this must add set_compute_dps() and switch to Q_MP in the same change.
