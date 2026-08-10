---
# qou-h0zz
title: 'V6: braid words per chiral fermion -- the actual blocker for T(t)'
status: todo
type: task
priority: normal
created_at: 2026-08-10T18:34:14Z
updated_at: 2026-08-10T18:34:15Z
---

sm-open-problems.md names this itself: hypercharge Y open, 'framework braid words
per chiral fermion STILL MISSING'.

This is the real blocker, upstream of everything else on the T(t) front. Without a
braid word per chiral fermion there is nothing to read t off, so T(t) is a free
label BY CONSTRUCTION -- which is exactly why the published battery returns a
tautology (TwistBatteryVacuity.lean: the battery collapses to sum(t) = 3Q, and
4 = 1x2x2x1 is multiset counting).

WHAT EXISTS: braid words for the HADRON sector --
  gluon unit        sigma_0 sigma_1^-1      (writhe 0)
  Borromean baryon  B_3 = (sigma_0 sigma_1^-1)^3  (writhe 0)
  Hopf link L_H     from the L+/L- terms
  lepton carriers   e- = T(2,3) trefoil, nu = unknot (KNOT types, not braid words)
WHAT IS MISSING: a braid word per CHIRAL fermion (u_L, d_L, e_L, nu_L and the RH
singlets). The lepton rows are given as knot types only, and chirality is not
represented at all.

NOTE the chirality problem is now sharp (LeptonNumberCarrierChirality.lean): the
carrier cannot be an unframed knot type, so 'e- = trefoil' is not enough -- a
braid word (or framed object) is required for the mirror to act freely.
BLOCKED-BY: V5 (which framing) determines what t even means.
