---
# qou-r9dv
title: 'DEFECT: tr-m-atom-via-transfer.witness.json is stale -- records passed:true against 0.388357, a value NEITHER live path produces'
status: todo
type: task
priority: normal
created_at: 2026-08-19T20:16:50Z
updated_at: 2026-08-19T20:17:29Z
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
