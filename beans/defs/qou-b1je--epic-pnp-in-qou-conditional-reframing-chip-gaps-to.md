---
# qou-b1je
title: 'EPIC: P≠NP-in-QOU — conditional reframing + chip gaps to paper standard'
status: in-progress
type: epic
priority: normal
created_at: 2026-07-24T16:00:13Z
updated_at: 2026-07-24T16:00:43Z
---

P≠NP-in-QOU program. Owner directive: state everything CONDITIONAL on the QOU
("Given a QOU, then P≠NP-in-QOU"), never bare P≠NP; chip gaps to paper standard;
slowly, honestly.

DONE (verified sorry-free via lean-direct, restored oleans):
- qou-9yv4: WenzlSchurElement capstone — substrate_avoids_tl_locus /
  substrate_not_tl_degenerate: TL walls X=Q^{-N}>0 disjoint from substrate X≤0.
- qou-ytmz: CONDITIONAL reframing of the carrier. New opaque PNeqNPInQOU:Prop
  (QOU-scoped, NOT general P/NP). chiResidual=-6 + chiResidual_ne_zero (derived
  non-vanishing, sorry-free). class QouPNeqNp(residual):Prop now carries the
  FAITHFULNESS implication (was degenerate — only "∃ nonzero real"). Theorem
  qou_implies_p_neq_np [QouPNeqNp r] (hr:r≠0) : PNeqNPInQOU = "given a QOU, P≠NP
  in that QOU". Sole sorry confined to instance's `faithful`. .md headline
  reframed. (PR #4141.)

REMAINING = two NAMED external gaps, both honest WALLS (scope-(a): "blocked on
X", not "impossible"). Not quick sorry-free chips; do NOT fabricate to close:
- qou-aja6 (faithfulness leg, res≠0⇒P≠NP-in-QOU): needs a counting→decision
  transfer no known result supplies (#P-hardness of one invariant ⇏ P≠NP). This
  IS the conjecture. Wall = complexity theory (no P/NP in Mathlib).
- qou-5hul (Wenzl stage 2): genericity⇒semisimple = Hecke radical / Schur-element
  theory absent from Mathlib. Wall = Mathlib gap (keystone epic 08a2 territory).
- qou-qua1 (unify WenzlCriterion vs SchurElementCriterion): the bridge between
  the two cited forms IS the Geck-Pfeiffer/Wenzl semisimplicity equivalence —
  same Mathlib gap as 5hul. Chippable only after 5hul infra lands.
Chippable kernel is now exhausted; further progress needs one of the two walls.
