---
# qou-t9r1
title: 'GAP: 8 unannounced convention-C sites left in computations/ (detector-blind spelling)'
status: todo
type: task
priority: normal
created_at: 2026-08-29T08:04:35Z
updated_at: 2026-08-30T02:53:07Z
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

2026-08-29: adjudicated 37 of the 86 value-audit blocking sites as deliberate C-vs-D comparison arms (docstring frames it as convention work AND scope co-binds z_D; each entry quotes the file's own purpose). BLOCKING 86 -> 49, ledger 1 -> 38. Remaining 49 = 42 solo + 7 co-bound-but-unframed; the latter include qbeta_utils.py (cds1-gated ladder) and the fork-pricing probe, which need an eye rather than a keyword match. NOTE for anyone quoting a C-surface figure: the SHAPE audit's ACTIONABLE (8) is ~a tenth of the VALUE audit's surface (87 confirmed); do not report the former as the remaining work.

2026-08-29 (cont): 49 -> 30 blocking. Adjudicated 16 sibling-def comparisons (taxonomy row 18), 1 whose D arm is a closed form in h not a z (row 19), and markov_trace_weights_wenzl's two sites — that one is a STALE CANONICITY CLAIM, not just a C binding: it called z_C 'the canonical Markov trace' post-R1. Relabelled, not migrated; zero importers and only inventory audits read its witness, so migration is cheap but is a separate decision. Ledger 38 -> 57.
