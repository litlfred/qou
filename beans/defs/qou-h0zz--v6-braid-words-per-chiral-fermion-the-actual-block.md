---
# qou-h0zz
title: 'V6: braid words per chiral fermion -- the actual blocker for T(t)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T18:34:14Z
updated_at: 2026-10-04T15:25:24Z
parent: qou-8lxd
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


RESULT 2026-08-10 — the braid words are NOT missing; the corpus already fixes them.

chi=-6 constraint: 'T(2,n) with odd n<=7 exhaust the fermion spectrum; electron
T(2,3), neutrino T(2,1)'. And T(2,n) IS the closure of sigma_1^n in B_2. So:
  nu_e = sigma_1^1   (w=+1)      nubar_e = sigma_1^-1 (w=-1)
  e-   = sigma_1^3   (w=+3)      e+      = sigma_1^-3 (w=-3)
  gen2 = T(2,5) = sigma_1^5      gen3 = T(2,7) = sigma_1^7
  baryon B_3 = (sigma_0 sigma_1^-1)^3 (w=0);  gluon unit (w=0)

This RESOLVES the chirality obstruction (LeptonNumberCarrierChirality.lean):
nu and nubar are DIFFERENT BRAID WORDS (w=+1 vs -1) though both close to the
unknot. The mirror acts freely at braid level exactly as predicted.

CANDIDATE FOUND: L(beta) = sign(writhe(beta)), parameter-free, matches 6/6
corpus rows (both leptons, both antileptons, baryon, gluon unit). Consequence:
Y = B - L closes all four LH rows (u,d = 1/3; nu,e = -1).
computations/chiral_fermion_braid_words_probe.py

NOT A CLOSURE -- three caveats:
 1. sign() is a CHOICE of function, not derived from the framework.
 2. The QUARK braid word is still NOT in the corpus; w=0 is ASSUMED (motivated by
    the gluon unit being writhe-balanced). Every quark row rests on it.
 3. Chirality L vs R is still unrepresented -- no distinct word for u_L vs u_R.

KEY CONSEQUENCE for the writhe-independence tension: L = sign(w) is
writhe-DEPENDENT, and that is FINE. Y = B - L still does not factor through w
because B varies at fixed w. So the 'second invariant independent of the writhe'
is B (mu-bar_123), NOT L. The apparent L-needs-framing vs Y-needs-independence
collision dissolves: L needs the BRAID WORD (which carries writhe), not a free
framing datum.
