---
# qou-vbw1
title: Refresh 7 consumers of the T4 theta values after the q0 unit-conflation fix
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T22:02:31Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
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


---

## 2026-08-07 PARTIAL — my 6 probes refreshed; 4 other-agent files remain

Refreshed and re-verified (all 7 probes exit 0, assertions pass):
  qbeta_rdmr_rademacher_winding_probe.py         theta targets -> corrected
  qbeta_qnnq_afree_theta_constraint_probe.py     two grids collapsed to one
  qbeta_offl_ratio_candidates_unfalsifiable_probe.py   + A-grid fix, see below
  qbeta_sdp_angle_offset_theta_probe.py          q0 read, not typed
  qbeta_braid_nf_sdp_offset_probe.py             q0 read, not typed
  qbeta_lorentzian_gram_offset_probe.py          q0 read + q-scan grid point

All now read `qou_substrate.constants.Q_50_DIGIT_STR` rather than typing a
literal — the "suggested fix shape" from this bean, applied.

**TWO THINGS THE REFRESH SURFACED, both worth more than the refresh:**

1. **A control got 10 orders of magnitude tighter.** The qnnq C0 residual (does
   the T4 pair lie on the A-free curve?) went 1.3e-8 -> **5.9e-18**. The old
   value was the 8-digit rounding of the theta literals; with 17-digit theta at
   the corrected q0 it is machine-exact. Independent confirmation the fix is
   right.

2. **A hidden hardcode-to-a-superseded-grid, caught by the refresh.** The offl
   probe's A-sample grid began "2.0462", "2.05" — tuned just above the OLD
   A_crit = 2.046. The corrected A_crit = 2.054 made both infeasible, so they
   were silently skipped, max rho fell to 8.5, and the exhaustiveness assertion
   failed. The MATHEMATICS was unchanged; only the sampling was stale. Fixed by
   deriving the samples from A_crit, so the probe is now correct under any q0.
   This is exactly the failure mode this bean exists to prevent, and it was in
   my own probe.

STILL OPEN — four files, other agents' work, deliberately untouched:
    computations/qbeta/qbeta_t3_multiknot_binding_probe.py
    computations/probes/qbeta_3bp8_w2_direct_sheet_probe.py
    computations/probes/qbeta_3bp8_annihilator_continuation_probe.py
    computations/probes/qbeta_awpk_perwinding_stokes_41_probe.py


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** Done: all consumers refreshed and the last one verified via qou-p2ka. Hygiene only: the ϑ values themselves remain evidence-unreliable (see qou-4kgh).

Evidence: Commits 23b2a60cfe, 653f8d644e, 0b487dd722, ec09f40013 (last consumer), and 833e328165 (registry reads). All 9 named files now read `Q_50_DIGIT_STR` or `theta_t4()` from `computations/qbeta_t4_anchors.py`, or carry corrected 17-digit values, and the remaining `1.11020` hits are comments only. qou-p2ka (completed) verified the A2 re-run: residual 1.6719e-10 vs 1.6704e-10, verdict unchanged. `theta_t4` reproduces 0.0585920168400597 / 0.203132507018276.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
