---
# qou-o2n6
title: Is the Door-v residual full (-1)^n alternation? Scope of twoOp_residual_kills_residue against conj:c1-ggm-bar-parity-faces
status: completed
type: task
created_at: 2026-09-03T11:48:16Z
updated_at: 2026-09-04T03:34:18Z
---


RESULT (2026-09-03, PR #6523). Answer: NO. Measured + proved:
- The corpus residual (conj:c1-ggm-bar-parity-faces) is the asymptotic sign
  alternation of the GGM growing solution, module-level. The #6498 hypothesis
  (alternation at EVERY level) is UNSATISFIABLE for the GGM recurrence at any
  q < 2: `ggm_full_alternation_impossible_of_lt_two` (fails at m = 0).
- The block's own reason ("no sign change occurs while 2 - q^{m+1} > 0") is
  FALSE as written: the recurrence is oscillatory there (2-3 sign changes in
  m <= 5 at q0, six initial data). Corrected in place with the sharp statement:
  no two consecutive flips while c > 0 (`ggm_solution_no_double_flip`).
- Exclusivity survives level by level: alternation from n0 kills residues from
  n0+2 on, no seed hypothesis (`twoOp_residual_from_level_kills_residue_beyond`).
  At q0: window m <= 5, persistent alternation from m = 11..14 (initial-data
  dependent). Residue and residual COEXIST at jet levels 2..7 at least.
- Consequence: #6498's 'non-derivative component needed for sums' holds only
  above the window; at low body orders a derivative-only mixed-shift D_q is not
  excluded. Odd shift still required everywhere.
Open: jet level n = GGM index m is the conjecture's identification (not
checked); scalar-sign residual vs eigenfunction hypothesis is a modelling gap.

CLOSED 2026-09-04: merged in #6523 (ed4bf7a4ff). Follow-up: qou-33hb (derivative-only D_q vs the C1 kernel).
