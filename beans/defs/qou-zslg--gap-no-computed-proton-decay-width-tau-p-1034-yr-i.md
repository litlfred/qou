---
# qou-zslg
title: 'GAP: no computed proton decay width; tau_p >~ 10^34 yr is the experimental bound restated'
status: todo
type: task
priority: normal
created_at: 2026-11-22T10:47:46Z
updated_at: 2026-11-22T12:08:27Z
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



2026-11-22 RESULT (computations/probes/nucleon_width/, prereg then RESULT.md, PR #8955): CS(L6a4) = -1.5e-65 (SnapPy high precision), so CS = 0 (amphichiral => CS in {0, 1/2}). Proton and neutron closures isometric. Under width = Im Vol_C = CS the closure gives width 0 for BOTH nucleons: derives proton stability but predicts a stable neutron. Scope-(a) negative for the closure-only reading; a width difference must come from braid decorations. Claim 1 not Lean-proved (standard 3-manifold topology + SnapPy isometry). Bean stays open: no derived width for the neutron, no CS-to-width unit map.


2026-11-22 (PR #9013, merged with this tranche): the CS of the hydrogen capture-braid closure was computed for both electron placements, preregistered first. W_L and W_R both close to L12n2208, the Borromean rings plus the braid axis: Vol 12.17929927691584…, CS 0, and W_L ≅ W_R. So the placement is invisible to the closure, a scope-(a) negative. A capture-braid CS cannot supply a p/n or placement-dependent width term. Audit 2026-11-21-qbeta-energy-map-spectator §33.
