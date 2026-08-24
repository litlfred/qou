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

## Summary of Changes

regressed 13 -> 1, drained_files 72 -> 88, dirty_witnesses 1391 -> 1371.
Every fix diffed leaf by leaf against HEAD before committing.

  681796995  gg-production-bond            collapse_factor was 0.301/float64-eps
  43e14ea47  per-nucleon-shift             numpy lstsq -> mp.qr_solve; 36 -> 0
  488910f6b  qbeta-silver-ratio            8 -> 0   Fraction downcast in assertions
  76021b01a  atom-vhyp-closure             43 -> 0  tr_M recovered 16 -> 30 digits
  182f28713  log-ratio-prototype           117 -> 0 50-digit strings read as f64
  9a3c2b06c  catalan-binding               47 -> 29 + six wrong AME literals
  46c83a2d2  binding-single-pipeline       430 -> 0 the largest
  9960ed598  bar-pairing                   20 -> 0  raw json.dumps forced the cast
  89f4a0441  he4-channel-split             59 -> 0  casts at the record site only
  1a62622ad  path-b-habiro                 118 -> 0 + AME atomic masses
  d21fa843d  beta-decay-matrix             42 -> 0  f64 family -> _MP family
  11a5c1311  gb-filtration                 11 -> 0  exact integer ratio

## CORRECTIONS to this bean's own classification

I classified the remaining ten from their WITNESS VALUES rather than by
reading the producers, and got three of them wrong:

  beta-decay-matrix   I wrote "float64 by construction ... a real fix here is
      an mpf migration, not a literal edit", and warned a naive attempt would
      run at 15 dps and be worse. In fact q_parameter builds its _MP family
      AFTER raising its own precision to >= 50 dps (q_parameter.py:181), so
      the swap was safe and mechanical. 42 -> 0.

  gb-filtration       I wrote "metadata, not physics -- making these mpf
      would be silly; they want a carve-out". `1.2, 4.8, 120.0` look like
      hand-tuned heuristics from outside. `reduction_factor` is
      total_basis_size / filtered_basis_size -- a ratio of two integers,
      exact. 11 -> 0.

  the AME "root cause"  (recorded in full under qou-ex8k) I predicted
      _ame_table() would fix ~54 fields across 5 of the 10. It fixed none of
      them: those producers do not consume it.

The pattern is consistent -- classifying from the emitted values instead of
the code that emits them.

## What actually remains: ONE, and it IS a decision

borromean-axial-coupling (108 -> 116). Unlike the other two I mislabelled,
this one holds up on reading:
  * `GRAM = np.array(_gram_data["gram_matrix"], dtype=float)` and
    `pairing = float(u_A @ G_inv_A @ obs_A_vec)` -- a genuine numpy
    linear-algebra path, where mpf triggers the object-dtype trap this
    session already proved live in mass_at_3A_proper.
  * the witness carries LP-dual fields (primal_obj, dual_obj, duality_gap)
    and is gated by lp_dual_witness_validator.py -- the family the audit
    ALREADY carves out.
  * LP_DUAL_F64_FIELDS currently covers the LP solution fields only, not
    gram_matrix / gram_inverse / shadow_prices / char_on_basis.
Extending a carve-out is an owner call: the sibling carve-out in that same
file is annotated "qou-7kq3, owner-approved 2026-08-15". See bean qou-brm1.
