---
# qou-mame
title: 'Close the Lobachevsky-Catalan axiom: lobachevsky(pi/4) = catalan_G/2 via QOU.Knot.clausen_eq_series'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T00:50:24Z
updated_at: 2026-10-04T15:12:09Z
parent: qou-c8p8
---

PROVED 2026-08-26. `lobachevsky_pi_div_four_eq_half_catalan` is now a theorem, sorry-free, [propext, Classical.choice, Quot.sound]. Axiom surface 24 -> 23.

The axiom was recorded External on the strength of its own docstring ("needs Mathlib's full polylogarithm machinery ... none of which is currently upstream"). Both halves were false: Mathlib has `integral_log_sin_zero_pi_div_two` and `Analysis.Complex.AbelLimit`, and this repo already had the whole series-integral bridge in `QOU.Knot.clausen_eq_series` (sorry-free). Proof is 3 steps over those.

Downstream: `WhiteheadVolume.vol_L5a1_eq_eight_lobachevsky` was conditional on the axiom and is now unconditional.

Deleted `LobachevskyClausenGap.lean` (its narrative asserted a gap that does not exist). Guard rc=0 / 40 entries.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
