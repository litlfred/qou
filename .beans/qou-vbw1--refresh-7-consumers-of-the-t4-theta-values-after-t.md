---
# qou-vbw1
title: Refresh 7 consumers of the T4 theta values after the q0 unit-conflation fix
status: todo
type: task
priority: high
created_at: 2026-08-07T22:02:31Z
updated_at: 2026-08-07T22:02:31Z
---

The T4 crux probe's q0 was fixed (PR #4513) from the hardcoded 1.11020 to the
canonical proton-pinned constant 1.1099785827513808, read from
`qou_substrate.constants.Q` rather than typed.

ROOT CAUSE, for the record: not a typo but a UNIT CONFLATION. The substrate
quantity 0.20906 is `h = q0 - 1/q0`, not `2*ln q0`. Solving `2*ln q = 0.209060`
gives q = 1.1101889, matching the old literal to 1.0e-5 relative — while
canonical differs from it by 2.0e-4, twenty times larger. Since
h = 2*sinh(ln q0) = 2*ln q0 + (ln q0)^3/3 + ..., the two agree to second order
and split at third, which is exactly the observed gap.

CONSEQUENCE: the derived theta values moved.

    theta_mu   0.05894648  ->  0.05859202     (-0.60%)
    theta_p    0.20323503  ->  0.20313251     (-0.05%)

SEVEN FILES hardcode the OLD values and are now stale:

    computations/qbeta/qbeta_t3_multiknot_binding_probe.py
    computations/probes/qbeta_3bp8_w2_direct_sheet_probe.py
    computations/probes/qbeta_3bp8_annihilator_continuation_probe.py
    computations/probes/qbeta_awpk_perwinding_stokes_41_probe.py
    computations/probes/qbeta_rdmr_rademacher_winding_probe.py          (mine)
    computations/probes/qbeta_qnnq_afree_theta_constraint_probe.py      (mine)
    computations/probes/qbeta_lorentzian_gram_offset_probe.py           (mine)

Plus `qbeta_braid_nf_sdp_offset_probe.py` and
`qbeta_sdp_angle_offset_theta_probe.py` (mine), which hardcode
`Q0_T4 = 1.11020` with the comment "the grid the T4 inversion used" — a label
that is now inaccurate.

WHY NOT DONE IN THE SAME PR: four of the files are other agents' work, and a
cascade edit across seven probes late in a long session is exactly how a
plausible-looking regression gets introduced. The source is fixed and the delta
is documented; the refresh should be its own reviewable change.

WHAT SURVIVES THE CHANGE UNCHANGED, so the refresh is low-risk:
  - the A-free invariant r = S_mu/S_p = -0.2453912076 is q0-FREE by construction
    (AfreeThetaConstraint.afree_invariant), so the central result of #4513 is
    untouched;
  - every scope-(a) refutation in #4513 turned on straddling/order-of-magnitude,
    and a 0.6% shift moves none of them.
What DOES move: L = ln^2 q0, A_crit (2.046 -> 2.054), and the numeric theta
targets quoted in comparison tables.

SUGGESTED FIX SHAPE: have consumers import the theta values (or recompute them
from the canonical q0) rather than typing them, so the next q0 change does not
require a seven-file sweep.
