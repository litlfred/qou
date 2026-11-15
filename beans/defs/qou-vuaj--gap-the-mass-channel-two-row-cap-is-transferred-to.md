---
# qou-vuaj
title: 'GAP: the mass-channel two-row cap is transferred to the DECAY channel, and its own source forbids that'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T12:16:30Z
updated_at: 2026-11-15T17:33:09Z
parent: qou-wxhi
---

VERIFIED FROM PRIMARY SOURCES 2026-09-04. Surfaced by a sibling audit
(docs/audits/2026-09-04-eigenphase-character-coordinate-and-the-slope-constraint.md,
bean qou-pdix, section 6 item 2), which explicitly did NOT action it. Every claim
below was then re-checked against the files, not taken from that audit.

THE DEFECT. computations/qbeta/qbeta_d_frame_terminus_probe.py:8-14 asserts:

  "The two-row cap is DERIVED, not a ruling: the mass fibre is 2-dimensional
   (lem:feynman-eigenbasis-decomposition carries the row cap l(lambda) <= 2 in
   its index set), and FibreDimensionForcesTL.lean proves fibre q-dimension ->
   Ocneanu parameter -> y_(1^3) = 0, sorry-free. Bean qou-n1dj, resolved
   2026-08-08. So z = z_D is FORCED"

and then uses that to fix g = y_(3)(z_D) = 0.5054042265 in the Q_beta DECAY
decomposition. The probe's headline verdict inherits it.

THREE INDEPENDENT CONTRADICTIONS, each checkable in one command:

1. THE CITED DERIVATION IS MASS-SCOPED BY ITS OWN DOCSTRING. This is the
   sharpest of the three and is stronger than the audit's phrasing.
   QOU/BraidsAndKnots/FibreDimensionForcesTL.lean, section "Where the input
   comes from": "dim_q V = [2]_q is not assumed here for convenience -- it is
   what the MASS CHAPTER already says. THE MASS CHANNEL's Schur-Weyl
   decomposition (lem:feynman-eigenbasis-decomposition) reads ... with the row
   cap l(lambda) <= 2 in the index set ... so y_(1^3) = 0 is forced."
   Its input is the mass chapter. Nothing in it concerns the decay channel. The
   probe's own sentence even says "the MASS fibre is 2-dimensional" and then
   applies the conclusion to decay -- the transfer is visible in the probe text.

2. A SORRY-FREE THEOREM SAYS THE DECAY CHANNEL CANNOT SEE IT.
   QOU/QBeta/DecayFibreBarParity.lean:244 threeRow_undetermined_by_decay
   (g t : R) : exists y3 y21 y111, y3 - y111 = g and y3 + 2*y21 + y111 = 1 and
   y111 = t -- for ANY prescribed t there is a normalised triple with the given
   decay pairing. Companion cap_member_of_family: "the cap is a choice of
   representative, not a consequence." The file's line 238 states the
   determination "must come from another channel, or a structural argument --
   never from Q_beta itself."
   NOTE THE CARE NEEDED HERE: point 2 ALONE does not refute the probe, because
   line 238 concedes a structural argument could do it. It is point 1 that
   closes that door -- the only structural argument on offer is mass-scoped.
   Do not cite point 2 by itself as the refutation; that was the audit's
   phrasing and it under-states what is wrong.

3. THE BEAN THE PROBE CALLS RESOLVED IS OPEN. qou-n1dj status is `todo`, and
   its title is "GAP: does the MASS fibre functor land in Rep(SU_q(2))~TL or
   full H_3(q)? (corpus self-contradiction, D vs C, 197 ppm on m_p)" -- the MASS
   fibre, unresolved. The probe says "Bean qou-n1dj, resolved 2026-08-08".

WHAT THIS DOES AND DOES NOT ESTABLISH. Scope-(a). It shows the probe's warrant
for z = z_D in the decay channel is unsupported: the structural argument it
cites does not reach that channel, the channel's own data provably cannot supply
it, and the bean it cites as resolved is open. It does NOT show z = z_D is wrong
for decay, does NOT derive the correct g, and does NOT adjudicate the convention.
The discrepancy the probe reports may well survive a correct warrant.

WHY IT IS NOT A ONE-LINE FIX, and why this is a bean rather than a PR. The
probe's headline is an ARC TERMINUS for qou-cds1, stated as a negative ("all
three places are measured-negative"). Removing the forcing does not just edit a
docstring -- it reopens whether g has freedom, which changes what the terminus
claims. Deciding that is research, not editing, and it interacts with qou-n1dj's
open question. Whoever takes it should decide the verdict first and edit second.

FIRST STEP FOR WHOEVER TAKES THIS: re-read the probe's three-place decomposition
with y_(1^3) free rather than 0, and determine whether the "measured-negative"
conclusion survives. If it does, the fix is warrant-only (cite nothing for the
cap, state g as a choice) and cheap. If it does not, the terminus is withdrawn
and qou-cds1's arc is not closed.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

The mass-channel two-row cap transferred to the DECAY channel against its own
source. Live, and it is a correctness question about convention D's scope (the
D7 ruling), not about residual C.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.



2026-11-15: moved under epic `qou-wxhi` (c_k ladder under convention D). Previous parent kept in history.
