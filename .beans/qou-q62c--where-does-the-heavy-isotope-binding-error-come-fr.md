---
# qou-q62c
title: Where does the heavy-isotope binding error come from? Errors peak at 6Li/7Li (+30-36%) and FALL to +5% at 12C — non-monotonic, so not a simple A-scaling defect
status: completed
type: task
priority: normal
created_at: 2026-08-30T16:49:18Z
updated_at: 2026-08-30T16:57:27Z
---

ANSWERED. Probe computations/probes/heavy_isotope_binding_error_anatomy.py (4 checks, all pass).
TWO INDEPENDENT COMPONENTS, not one defect.

The error is NON-MONOTONIC in A, which is the clue:
  A     4     6     7     9    10    11    12    14    16    20    24    40
  err +5.9 +36.5 +30.8 +15.7 +16.7 +10.1  +5.4  +5.1  +5.3  +8.3  +9.0 +19.5 %

COMPONENT 1 (A=5..11) — the model has NO p-shell dip. Experiment falls 1.742
MeV/A from 4He (7.074) to 6Li (5.332): the alpha peak, then the loosely-bound
p-shell. The model falls 0.213. Over A=4..16 experimental B/A has 5.92x the
VARIANCE of the model's. The model saturates at B/A ~ 7.3 immediately at A=4 and
carries no shell or cluster structure, so it treats 6Li as nearly as tightly
bound per nucleon as 4He when experimentally it is 25% less. The +36% spike is
the ABSENCE of the experimental dip, not an error in A-dependence. A model with
B/A held at a pure constant 7.679 reproduces the error curve to sd 5.05 points
over that range.

COMPONENT 2 (A>=12) — a complete-graph term the corpus has REFUTED. Experiment
saturates near 8.5 MeV/A; the model does not, reaching 10.22 at 40Ca, ABOVE the
experimental maximum for any nucleus (~8.79 at 62Ni). Least-squares fit over
A=4..40 in mpmath:

    B/A = 7.0862 + 0.0781674 * A      max |residual| 0.33 MeV/A
                                      (0.006 at 40Ca; the 0.33 outlier is 14N)

B/A LINEAR in A means B QUADRATIC in A, and a quadratic binding term is C(A,2)
complete-graph pair counting: epsilon = 2b = 0.156335 MeV per pair-bond, on top
of a bounded-degree constant 7.0862 MeV/A.

That is exactly the z = A-1 law QOU.Mass.CoordinationSaturation refutes
STRUCTURALLY (sorry-free): complete graph gives unbounded B/A with no plateau,
bounded degree gives a constant, and observed saturation FORCES bounded degree.
The Lean proves what the model must satisfy and the live compute does not
satisfy it. The term is invisible at low A (0.31 MeV/A at 4He) and is the whole
story by 40Ca (3.13 of a 1.67 MeV/A over-prediction).

NOT ESTABLISHED: which source line introduces the A^2 (measures output form
only; deliberately not guessed) — that is the obvious next step. Nor that fixing
2 fixes 1: they are independent, and removing the A^2 would INCREASE the 6Li
error, since it adds only ~0.47 MeV/A there against a 1.94 shortfall. Nothing
about A>40; 28Si and 32S raise 'no framework B prediction' (coverage gap).
