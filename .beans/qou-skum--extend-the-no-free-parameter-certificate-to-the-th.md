---
# qou-skum
title: Extend the no-free-parameter certificate to the theta channel
status: todo
type: task
priority: high
created_at: 2026-08-07T15:16:34Z
updated_at: 2026-08-07T15:16:34Z
---

The T5 no-free-parameter certificate (`computations/no_free_parameter_certificate.py`,
bean qou-s16e, epic qou-8lxd) makes "every number is traceable to a calibration,
a derived constant, or combinatorics" MECHANICAL rather than agent-policed. Its
own scope note is explicit: **"Scope of the certificate is the mass path only —
other observables are not yet covered."**

The theta/Q_beta channel is exactly such an uncovered observable, and it is
known to contain a free parameter.

PR #4513 proves in Lean (`QOU/QBeta/AfreeThetaConstraint.lean`, sorry-free) that
the channel `S_K = A_omega * kappa * (ln^2 q0 - theta_K^2)` has two anchor
equations in three unknowns, so `A_omega` is a genuine free parameter — one
degree of freedom that nothing internal pins beyond a one-sided `A >= 2.05`.
`ratio_attained` gives an explicit witness `A = (y*S1 - S2)/(kappa*L*(y-1))`
realising ANY ratio `y > 1`, so the underdetermination is proved, not sampled.

`A_omega = 3` is a hardcoded literal in `qbeta_t4_stokes3_crux_probe.py`,
imported from GGM rather than derived. Every theta value in the corpus is
inverted through it and is therefore A_omega-conditioned.

TASK: extend the certificate's import-closure walk beyond the canonical mass
facade to the theta/Q_beta path, so `A_omega = 3` gets classified. Expected
outcome is `UNTRACEABLE` (a bare literal in arithmetic with no calibration tag,
no witness read, no structural identification) — which is the CORRECT answer,
and would turn the circularity into a standing CI-visible fact rather than a
note someone has to remember.

WHY THIS IS THE HIGHEST-LEVERAGE ITEM ON THE ARC: the arc has produced three
consecutive structural negatives (rdmr refuted; ratio-shaped offl candidates
proved unfalsifiable; A_omega = 3 shown to rest only on the literature value).
None of it is enforceable today. The certificate is the mechanism that makes it
enforceable, and it already exists — it just does not reach this channel.

Caveat to carry: the certificate is a high-recall STATIC detector, not a proof
(its own epistemic-scope section). A clean run is evidence, never a theorem.

Cross-refs: PR #4513; docs/scope/2026-08-01-t4-anchor-circularity.md;
docs/scope/2026-08-01-theta-independent-routes.md; beans qou-qnnq, qou-offl,
qou-i3yg, qou-s16e.
