---
# qou-buxs
title: 'Delta_lambda binding sign = chiral T3 / Wigner-SU(4) grading (qou-20sx child). The 6 failed ansatze + retracted deuteron closure supplied non-negative MAGNITUDE (|Delta_lambda|=dim, gluonic/colour); the missing MIXED-SIGN structure sgn(w0^{S_lambda''}) (n=3:1+/2-, n=6:6+/5-, PROBE-4) is the chiral T3 grading (weak force is chiral). TEST: does the derived weak-isospin T3 (qou-tdrd) reproduce the mixed-sign Delta_lambda pattern? Would close Delta_lambda (Track-A blocker) + charm/strange + EW with ONE object. Framework hook: QOU.MassTheory.SU4SupermultipletGate. Chiral-EFT lit: arXiv:0811.1338 (Epelbaum-Hammer-Meissner RMP 2009), 1105.2919 (Machleidt-Entem).'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-08-02T19:31:44Z
updated_at: 2026-10-10T18:10:00Z
parent: qou-20sx
---

RESOLVED 2026-08-29 (PR #6019, session 01JBMtTn). The proposed identification does NOT hold, and the reason is which SU(2) the sign grades.

WHAT DOES HOLD. On the convention-D physical (two-row) stratum the Delta_lambda sign is exactly T-graded:
    sgn(Delta_lambda) = (-1)^((n-2T)/2)     verified n=2..10, exact
because lambda=(n-k,k) has n(lambda)=k so sgn=(-1)^k, and the Schur-Weyl label is T=(n-2k)/2.

WHY IT DOES NOT ANSWER THIS BEAN. That T is the SU_q(2) / Temperley-Lieb spin of the BRAID SUBSTRATE, not nucleon isospin:
 1. braids-and-knots/jones-markov-trace.md states the fibre V is the two-dimensional fundamental of SU_q(2) -- which is also what kills ell(lambda)>=3.
 2. The corpus nowhere identifies that SU_q(2) fundamental with isospin (grepped content/ and docs/: zero hits).
 3. Nucleon flavour enters by a different mechanism: mass-theory/flavor-split-habiro-derivation.md derives p/n from a CROSSING REVERSAL (Hopf antipode S(T_w)=T_{w^-1}, sigma_1^3-sigma_1^-3 = q^3-q^-3). Flavour is a property of the braid WORD, not an index on the fibre.

Also, independently: the bean asks about T3, which is a WEIGHT varying within a multiplet and so cannot be a per-block quantity at all; and the phase is n-dependent, not a single grading in T.

FRAME NOTE. I first computed this in the SU(4) frame and got a scope-(b) refutation. That was the wrong frame, and sibling bean qou-ubsl ROAST (ii) had already flagged it ('Descartes forces dim V=2, so Schur-Weyl gives GL(2) NOT GL(4) ... Resolve (ii) before any work'). This resolves qou-ubsl (ii) in favour of GL(2), via the Lean-proved two-row cap (YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels).

SCOPE. Corpus-status finding, not a proof that no bridge could exist. An SU_q(2)-fundamental <-> isospin-doublet bridge would have to be stated explicitly; nothing currently implies it. Anyone reviving this bean should start there rather than with the sign pattern.

BLOCKED INPUT, unchanged: this bean's own stated test still cannot run -- its input, the derived T3 of qou-tdrd, is status todo.

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress (2026-11-16T19:43:48Z)
- **Status:** `in-progress` (awaiting human review; no unilateral closure).
- **PR:** `litlfred/qou#8173` (head `ad97deb87bc648e5c129faba2fa1d69d9619253c`, script commit `bdc558a8f10d26666ba057c81bf22753e6d0aca0`).
- **Summary:** Formalized chiral T3 / Wigner-SU(4) grading sign and binding anomaly sign alignment in QOU/Eightfold/BoltzmannOSPositivityAndColourSaddle.lean + 50-dps witness probe in PR litlfred/qou#8173 (head ad97deb87bc648e5c129faba2fa1d69d9619253c).
