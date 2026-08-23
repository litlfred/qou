---
# qou-r9dv
title: 'DEFECT: tr-m-atom-via-transfer.witness.json is stale -- records passed:true against 0.388357, a value NEITHER live path produces'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T20:16:50Z
updated_at: 2026-08-23T17:38:23Z
---

Found while verifying qou-j320 (the two edits are NOT the cause -- reproduced identically on a stashed clean tree).

computations/tr-m-atom-via-transfer.witness.json, as committed on main, carries TWO wrong assertion states:

  assertion[0] trM_atom_deuteron_matches_canonical_branching
      computed 0.3883571225623529, expected 0.388357, tolerance 1e-5, PASSED:TRUE
  assertion[1] free_chi_matches_parabolic_lr_50dps
      computed 69.10941725305995, expected 0.0, tolerance 1e-40, PASSED:FALSE

Re-running the producer today gives the OPPOSITE on both:
  assertion[0] computed 0.5751722439177719  -> FAILS
  assertion[1] computed 2.654803731240376e-46 -> PASSES

The 0.388357 is a STALE HARDCODED EXPECTATION. Neither live path produces it:
  tr_m_atom_via_transfer.tr_m_atom_zn(1,1)          = 0.57517224391777187083
  canonical_tr_m_via_branching(1,1)                 = 0.57509087229027536125
  committed witness / hardcoded expected            = 0.3883571225623529   <-- neither

So the witness records passed:true against a number no current code produces, AND records a live failure that current code passes. It has not been regenerated since the underlying value changed, and its expectation drifted with it.

SECOND, SMALLER FINDING worth its own look: the two LIVE paths agree only to 1.4e-4 relative (0.5750909 vs 0.5751722). Both are described as lossless 50-dps computations of the same object; they should agree to the 50-dps floor, not the 4th digit. Which is canonical is not decided here.

NOT FIXED HERE, deliberately: regenerating would commit a visibly-failing assertion, and deciding the right expected value means deciding which path is canonical -- a different domain from the bar-involution work. Reported rather than papered over.

IMPACT ON qou-e58e / qou-kgsx: NONE for the conclusions. Both live paths agree at ~0.5751 to 1.4e-4, and the delta derivation is a symbolic identity of the transfer path, cross-checked against five independent numeric evaluations of that same path. But every result in docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md is ON the transfer path, and that caveat is now stated there.

MUCH BIGGER THAN A STALE WITNESS -- IT IS A LIVE FAILING TEST ON MAIN, and it is NOT from my branch (verified on a clean worktree of origin/main: identical value).

ESTABLISHED:
 1. tr_M^atom(D) on origin/main = 0.5751722439177719. The corpus canonically expects 0.388357 -- a 48% change.
 2. computations/test_tr_m_atom_q_param.py:33 FAILS on clean origin/main:
      AssertionError: D tr_M_atom(q0) drifted: 0.5751722439177719
    A committed, failing test.
 3. tr-m-atom-via-transfer.witness.json records passed:true against 0.388357, which NO live path produces.
 4. At least four other sites hardcode ~0.3884:
      gap_a3_overshoot_robustness_check.py:37   TRM = {"D": 0.38835725751524, ...}
      deltalambda/ka_additive_cluster_derivation_probe.py:90  TR_D_CACHED = 0.38835720735922143663...
      gap_a3_deuteron_A_D_overshoot.py:30       TRM_BETA_D = 0.38835725751524
      canonical_tr_m_via_branching.py:393       comment asserting the match
 5. THREE INDEPENDENT METHODS agreed on 0.3884 as recently as 2026-06-30: the 2026-06-23 audit table (Hoefsmit atomic_tr_m_mpfr + markov_peel = 0.38835726) and the 2026-06-30 audit (muon q0 0.38835718872378100727 vs markov-peel 0.38835718872378100730, agreeing to 9.1e-20).
 6. Both LIVE paths now give ~0.575 and agree with each other to 1.4e-4: transfer 0.5751722439, branching 0.5750908723.

MOST PROBABLE CAUSE, not yet proved: the 2026-08-09 convention C->D switch in y_lambda_at. tr_M = SUM y_lambda chi^lambda, and the switch changed y_lambda(3,q0) from C (0.4153958, 0.2809296, 0.0227449) to D (0.5054042, 0.2472979, 0) -- verified live: y_lambda_at returns exactly the D triple. THE SWITCH DOCSTRING VERIFIES ONLY THE MASS CHANNEL ("The mass channel is unaffected... Verified: m_p unchanged") while noting the function has ~155 CONSUMERS. The atom/binding channel appears never to have been checked.

CAUTION -- MY OWN EARLIER TEST WAS VACUOUS: _y_lambda_at_convention_C_HISTORICAL returns the SAME D values as the live function, so "C and D agree" proved nothing. That function is dead exactly as its docstring says.

NOT YET DECIDED, and I will not decide it without the arbiter: whether 0.575 is correct-and-the-constants-are-stale, or the transfer regressed. Both live paths being D-frame does not settle it, because a common upstream (y_lambda_at) feeds both. The independent arbiter is the Hoefsmit path computations/atomic_tr_m_mpfr_50dps.py (>30 min); it must be run as
    QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor proton
because the stem is bound to ideal_muon in q0_anchor_manifest.json at import, before argparse -- the script refuses otherwise, correctly.

DO NOT refresh the four hardcoded constants until the arbiter returns. Refreshing them to 0.575 on the strength of two paths sharing an upstream would be exactly the kind of consensus-by-common-cause the corpus warns about.
