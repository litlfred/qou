---
# qou-nbx7
title: 'resolve the delta split: separate the two roles (mass observable vs crossing tilt); subleading coefficient is 1.3147, not 1'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:45:37Z
updated_at: 2026-10-04T15:24:07Z
parent: qou-wp3h
---


Branch: claude/anchor-followups-2026-08-08. Follows the alignment work in
6a946de0 and docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md,
which established the split is principled (trace path = leading, for provenance;
mass path = subleading, for accuracy) but left it unresolved.

## THE RESOLUTION: the two roles are numerically decoupled, so separate them

delta is consumed in two roles that have been treated as one quantity because
they share a name and a formula:

  (a) MASS path -- delta IS Dm/M_N, the physical n-p mass ratio. It is the whole
      observable, faces a 1000 ppm CODATA regression gate, and CODATA knows it
      to ~0.1 ppm. Accuracy is everything.
  (b) TRACE path -- delta appears ONLY as the tilt in the p-n crossing template
      d = -h*(1/2 - delta/4).

Measured, role (b) has essentially no accuracy requirement:

    d with NO tilt (-h/2)  = -0.1045301493978197
    d with leading tilt    = -0.1044582477697263
    d with subleading tilt = -0.1044581778307480

    the ENTIRE tilt          7.19e-5  = 0.0688 % of d
    leading vs subleading    6.99e-8  = 0.000067 % of d

and downstream:

    B(2H), no tilt      3.89045456581 MeV
    B(2H), leading      3.88969225844 MeV
    B(2H), subleading   3.88969151701 MeV

Removing the tilt ENTIRELY moves B(2H) by 0.0008 MeV (0.02%). The
leading/subleading choice moves it by 7.4e-07 MeV.

**So the trace path cannot break the mass gate and the mass path cannot disturb
the trace.** They can be separated cleanly, and should be:

- [ ] give role (b) its own name and its own derivation. It is currently called
      the "colour-weighted" tilt while being computed from the FLAVOUR split
      Dm/M_N -- a category error that is plausibly WHY no derivation has landed:
      the two roles have been treated as one quantity for naming reasons.
      Role (b) needs to be structurally right, not numerically sharp, so it is
      the tractable half.
- [ ] leave role (a) as the accuracy problem it is, with the gate intact.

## THE OTHER HALF: the subleading coefficient is 1.3147, not 1

`flavor_split_subleading = leading * (1 + hbar_q^3)` posits the coefficient 1.
Back-solving against CODATA (m_n = 939.56542194, m_p = 938.27208943):

    required  k = (delta_CODATA/delta_leading - 1)/hbar_q^3 = 1.31470967527

    k = 0    (leading only)              -1277.19 ppm vs CODATA
    k = 1    (posited, current)           -305.73 ppm     <- clears the 1000 ppm gate
    k = 4/3                                 18.09 ppm     <- 17x better
    k = 1.31470967527 (back-solved)          0

CANDIDATE, EXPLICITLY NOT A FINDING: k = 4/3 is the SU(3) fundamental-
representation Casimir C_F, which is a natural object for a 3-quark nucleon and
would fit the docstring's own pointer ("should be DERIVED from the 3-strand /
3-quark (spectator) categorical structure"). It is 1.42% from k_true, i.e.
18 ppm on delta -- a 17x improvement on the posited k=1 and 55x inside the gate.

But 18 ppm is **180x the CODATA experimental uncertainty** (~0.1 ppm), so 4/3 is
a BETTER FIT, NOT A DERIVATION, and must not be wired on that basis. Recorded so
the coincidence is not re-discovered and mistaken for a result. No other simple
candidate came closer: 5/4 (4.9% off), q0^2 (6.3%), 3/2-hbar (6.6%), 1+h (8.0%),
3/2 (14.1%), q0 (15.6%), 1 (23.9%).

ACCEPTANCE TEST for any derived subleading correction: it must produce
k = 1.31470967527 to within the CODATA uncertainty, i.e. delta within ~0.1 ppm.
Neither k=1 (306 ppm) nor k=4/3 (18 ppm) meets that. The 2026-06-29 Part B
result stands: the geometric closure 1/(1-hbar^3) gives k = 1.00097, no better
than k=1, so the missing physics is not in higher geometric terms.

### Progress Update (2026-11-16, PR #8171)
- Formalized Role (a) (`deltaMassObservable : ℝ → ℝ`) and Role (b) (`pnCrossingTemplateFour : ℝ → ℝ → ℝ`) in `folio/quantum-observable-universe/lean/QOU/AppendixQValues/ProtonBorromeanAssembly.lean`, proving `pnCrossingTemplateFour_diff` and `pnCrossingTemplateFour_subleading_shift` (`0` `sorry`).
- Verified numerically to 80 dps at $q_0$ in `computations/probes/delta_split_mrel_four_phi_resummation_probe.py` (`computations/probes/delta-split-mrel-four-phi-resummation.witness.json`, `scriptCommitSha: 66da8967c7bbb2544d7558251e982ed669439326`).
- Opened PR `litlfred/qou#8171` (`1c72739193707fef67fbebe3aa153f994c73933e`). Keeping status `in-progress` pending owner review.
