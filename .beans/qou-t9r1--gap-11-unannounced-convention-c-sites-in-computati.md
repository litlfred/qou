---
# qou-t9r1
title: 'GAP: 8 unannounced convention-C sites left in computations/ (detector-blind spelling)'
status: completed
type: task
priority: normal
created_at: 2026-08-29T08:04:35Z
updated_at: 2026-08-30T07:56:32Z
---

THE FINDING behind PR #5972. `scripts/convention-c-producer-audit.py` reports 9
actionable convention-C sites in computations/ (7 of them registry-blocked on
qou-cds1) plus 61 deliberate. Those numbers are correct FOR WHAT IT CAN SEE, and
it cannot see the sqrt-variable spelling: `z = 1/(sq + 1/sq)` or `u/(u^2+1)`
where the variable is sqrt(q). Both equal sqrt(q)/(q+1) = z_C exactly.

`scripts/convention-c-value-audit.py` (new, this PR) EVALUATES each binding at
two sample points instead of matching its shape, and finds 90 confirmed
convention-C bindings in computations/. Cross-referenced against the shape
audit's own 71 rows, TWENTY-ONE are reported by it NOWHERE -- not actionable,
not deliberate, not at all.

This is the 14th entry for docs/audits/2026-08-15-detector-blindness-taxonomy.md
and it matters more than one more spelling, because the blind spot hides BOTH
buckets at once. A future agent draining the shape audit to zero would declare
the excision complete with these still on C.

DISPOSITION OF THE 21 (verified by reading each site, not by the label):

  ALREADY ANNOUNCED, leave (4) -- deliberate, merely invisible to the audit:
    schur_principal_mpmath.py:123      _wenzl_constants_convention_C_HISTORICAL,
                                       kept ON PURPOSE as the one live C
                                       implementation the D-vs-C comparison in
                                       y_lambda_su_n.main() quotes
    qbeta/qbeta_utils.py:248           inside a `convention == "C"` dispatcher
    probes/casimir_phi_q_markov_probe.py:125   "multiple conventions; tabulate"
    probes/gram_ylambda_sign_check.py:74       "# convention C"

  MIGRATED IN PR #5972 (5, with per-field deltas in the commits):
    prearchimedean_bond_factor.py:68
    deltalambda/deuteron_coupling_s00_probe.py:108
    deltalambda/nuclear_quotient_jones_torus_link_probe.py:56
    probes/b4_antisym_hecke_exchange_derivation.py:68
    probes/pn_pair_two_sector_split.py:81

  BLOCKED, cannot be migrated by substitution -- see bean qou-pmkh (4):
    gram_h3_det_factorization.py:55, gram_h3_symbolic_regression.py:72
    deltalambda/deltalambda_bareven_b4_magnitude_probe.py:131,137
    qbeta/qbeta_c3_barodd_hs_matrix_resolvent_probe.py:86
    qbeta/qbeta_c3_cross_anchor_exactness_probe.py:55

  STILL UNANNOUNCED AND UNMIGRATED -- THIS BEAN (8 sites, 6 files):
    compound_shift_nf.py:256           tr_m_weights_mp, a LIVE PRODUCER emitting
                                       TR_M = [1,z,z,z^2,z^2,z^3]; 3 witnesses
    markov_trace_weights_wenzl.py:254  markov_trace_s, a LIVE PRODUCER; its
                                 :457  docstring STATES z = 1/(q^1/2 + q^-1/2)
                                       as the trace it solves weights for, so
                                       migrating it changes the subject, not
                                       just the number -- check before swapping
    probe_markov_trace_ratio_exact.py:87   markov_z_h(); the claim under test is
                                       a RATIO, which may be z-invariant. Worth
                                       migrating precisely because it is a free
                                       check of that invariance
    probes/markov_stab_trace_axis_probe.py:130  z_markov_sym(); docstring names
                                       the formula but never the convention
    lw2_c2_independent_hopf_test_attempt.py:96  the corpus closed form
                                       tr_M(sigma_1^2) = (q-q^-1)z + 1 is proved
                                       "over Q(q^1/2)" per its own comment --
                                       likely C-premised, verify before swapping
    deltalambda/deltalambda_bareven_b4_magnitude_probe.py:137  z_bar, the partner
                                       of the blocked site above

HOW TO WORK IT. Do not sweep. Per site: baseline the witness FROM GIT (never
from the working tree the run mutates -- AGENTS.md records a contaminated-baseline
measurement that made two of three spot-checked verdicts false), migrate, re-run,
and report which fields moved. A field moving by exactly 0.227044 relative is the
z_D/z_C - 1 crossing signature and confirms a real convention crossing rather
than a re-spelling; anything else needs explaining. Watch for a SECOND spelling
of z in the same file -- prearchimedean_bond_factor.py had one in its assertion
comparand, and migrating only the first sent the assertion 5.55e-17 -> 0.1134.

## RESOLVED 2026-08-30 (PR #6110)

All enumerated sites dispositioned. **The header said 8; the list held 7.**

| site | disposition |
|---|---|
| `compound_shift_nf.py:256` | migrated to D **with** the TR_M[5] fix (qou-ssex) — NOT a clean z-swap: the trace bug was masking the D Gram singularity |
| `markov_trace_weights_wenzl.py:254,:457` | migrated. The premise caution does NOT hold — `a² = z/z₋` is an identity in `z` (`a2_fitted − a2_closed = 0` generically), not a C-specific fact |
| `probe_markov_trace_ratio_exact.py:87` | migrated; 4/4 pass under D, symbolic cancellation still exact in ℚ(q) |
| `probes/markov_stab_trace_axis_probe.py:130` | migrated; its cited authority `hecke_symbolic.py` had **already** moved to D on 2026-08-09 |
| `lw2_c2_independent_hopf_test_attempt.py:96` | **BLOCKED** — C-premised. `(q−1/q)z+1 = 1+(q−1)/√q` holds only at z_C; under z_D the file's own `wenzl_eq_cf` fails by 0.0237 at q₀ |
| `deltalambda_bareven_b4_magnitude_probe.py:137` | **BLOCKED**, registered (qou-pmkh) |

## Two findings beyond the migration

1. **A live layer straddle**, pre-existing, now removed: `markov_stab_trace_axis_probe` hardcoded the frozen MUON literal while reading a PROTON-anchored y-lambda cache, and the two met in one quantity (`y_lam * f_lam`). Same shape as the μ₃ Fréchet incident.
2. **The D radical, independently confirmed**: under D exactly the ℓ(λ) ≥ 3 Wenzl weights vanish, in exact rational arithmetic at every sampled s. Matches qou-fu8c by a completely different route.
