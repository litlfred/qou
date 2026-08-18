---
# qou-jh26
title: 'Accuracy: map what is actually closeable in mass+binding (Delta_lambda magnitude, c_k under convention D)'
status: todo
type: task
priority: normal
created_at: 2026-08-18T20:59:46Z
updated_at: 2026-08-18T21:06:20Z
---

DELIVERED 2026-08-18. Audit: docs/audits/2026-08-18-mass-binding-accuracy-what-is-closeable.md
Probe: computations/accuracy/l2_scoreable_count_probe.py (assertions pass).

HEADLINE CORRECTION: the L2 count is 1/5 scoreable, not 2/7.
The dashboard excludes m_p as an anchor round-trip ('the framework content
cancels') but SCORES m_e, whose err_ppb is not measured but DEFINED zero --
m_e is the CAL-1 input that fixes the MeV unit. Same argument, stronger case.
Only genuine prediction meeting L2 is m_K/m_pi (the only ratio among the five).

THE Q_BETA CHAIN'S STATED CLOSURE PATH IS REFUTED (this is the main finding).
The 2026-05-30 shared-root audit says: extend the ladder to k>=3 with a
canonical rung-selection rule. Two later results kill that:
  (a) QOU/QBeta/GreedyLadderTermination.lean (sorry-free) proves the producer
      extracts ONE rung by inverting the target and the residual is then
      IDENTICALLY zero -- greedy_later_rungs_vanish: 'c_4 ... c_7 carry no
      information; they are not small, they are 0.' There is nothing at
      k >= 3 to extend to.
  (b) the one extracted rung c_3 = (Q_beta^exp/Q_N2 - 1)/u^3 is extracted FROM
      experimental Q_beta, so using it to predict Q_beta is circular.
  => the 164x is the FLOOR of the ladder's non-circular content, not a
     truncation artifact. m_n and Delta_pn inherit it. Closing the trio needs
     a DIFFERENT derivation of Q_beta, not a deeper c_k.
  Also: exists_rung_hitting_target -- 'the ladder reproduces CODATA' is a
  property of having one free coefficient.

RIBBON AXIOMS DO NOT HELP ACCURACY. The twist reaches the mass chain via a
CORRECTNESS dependency (qDim_conj is an unproved input the Gram-inverse
derivation leans on). Supplying it removes an assumption; it moves no number.
beats_100x_count = 2 before and after.

RANKED CLOSEABLE: (1) the 1/5 recount, blocked by nothing; (2) c_k under
convention D (qou-cds1) -- until then the 164x floor is itself C-conditional;
(3) a non-ladder Q_beta derivation; (4) the Delta_lambda EXTENSIVE term (the
six failures were structural -- they forced an extensive quantity into an
intensive per-block weight; pairwise cap proved); (5) the mu-p residual
(structural, and q_0-derivation is permanently gated).

NOT DONE: no new physics compute; did not re-derive c_k under D; did not
re-verify the Delta_lambda magnitude beyond citing the proved value-lemma.
