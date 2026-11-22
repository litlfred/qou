---
# qou-zslg
title: 'GAP: no computed proton decay width; tau_p >~ 10^34 yr is the experimental bound restated'
status: todo
type: task
priority: normal
created_at: 2026-11-22T10:47:46Z
updated_at: 2026-11-22T10:47:46Z
parent: qou-wxhi
---

Owner 2026-11-22: "how does the decay width computational prediction compare to experimental for proton?"

FINDING (grep of content/, computations/, docs/audits, beans): the corpus has NO computed proton decay width or lifetime. What exists:
- observations/observables-algebraic-independence.md: "Non-collapse of the brane tower forbids any finite-order categorical channel for proton decay. The predicted proton lifetime satisfies tau_p >~ 10^34 yr." The 10^34 yr is the experimental lower bound restated, not derived from the framework: the derived content is only "no finite-order channel" (qualitatively stable).
- observations/crossing-energy-interpretation.md: proton stability from E_cross(p) < 0 (Hopf stability).
- No witness or producer computes Gamma_p.

CANDIDATE (preregister first): under conj:complex-mass-constituent-functional the width is Im Vol_C = CS. The Borromean rings are amphichiral (also used in issue #9002 to show the closure gives m_p = m_n at every q), and an amphichiral orientation-reversal negates CS, so CS(Borromean) is 0 or 1/2 mod 1. If 0, that reading predicts width 0 for the proton closure, i.e. stable, as a derived (not imported) statement. Compute and check; also state the neutron (its mirror) the same way, since the neutron is not stable, which may falsify the reading.

Related: neutron beta width D_beta is CAL-2 (a calibration, not a prediction). Its proxy Q_beta: dashboard pred 0.325433928735 MeV vs CODATA 0.782333559310 MeV (-58.4 %), conditional on conjectures C1-C3 (per-observable-100x-status.witness.json).
Not started.
