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

## Progress: 13 -> 10, and the highest-leverage remaining cause is identified

488910f6b  qbeta-silver-ratio-pell-lucas-ck  8 -> 0 raw float64. The
           assertions passed `float(Fraction)` on exact rationals whose
           denominators are all powers of two, so nothing was lost -- rule
           compliance, not a numerical repair. All five computed values
           numerically identical, all still pass.

Classified the remaining 10 by field rather than opening each blind:

  AME table (5 files)      B_AME_MeV / AME_MeV / M_AME_MeV -- 54 fields
                           across binding-single-pipeline (16),
                           catalan-binding (18), log-ratio-prototype (7),
                           atom-vhyp-closure (6), bar-pairing-extension (4),
                           path-b-habiro (3). ONE ROOT CAUSE -> bean qou-ex8k.
  float64 by construction  beta-decay-matrix (transfer matrices from
                           q_parameter's f64 family; see this bean above)
  gram matrices            borromean-axial-coupling -- gram_matrix (36) and
                           gram_inverse (36) come from the pyhecke-native
                           Rust extension, which returns float64. Likely
                           carve-out territory alongside the LP/SDP duals,
                           but that is a decision, not a sweep.
  metadata, not physics    gb-filtration-jet-order-reader -- all 11 are
                           `speedup_estimate` (1.0, 1.2, 4.8, 120.0 ...),
                           heuristic optimisation estimates. Making these
                           mpf would be silly; they want a carve-out or an
                           exemption, and that is also a decision.
  series values            path-b-habiro-mass-probe (a_m_at_u0, u_u_m,
                           contribution x32 each), he4-channel-split
                           (fraction_total x37)

So "10 remaining" is not 10 jobs: it is one root cause worth ~54 fields
(qou-ex8k), two that likely want carve-outs rather than fixes, and a
genuine per-producer tail.
