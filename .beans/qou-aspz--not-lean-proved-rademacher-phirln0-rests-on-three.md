---
# qou-aspz
title: 'NOT-LEAN-PROVED: Rademacher Phi((RL)^n)=0 rests on three agreeing computations'
status: todo
type: task
priority: normal
created_at: 2026-08-07T17:10:11Z
updated_at: 2026-08-07T17:10:11Z
---

NOT LEAN-PROVED. Established by compute only (PR #4513,
computations/probes/qbeta_rdmr_rademacher_winding_probe.py).

CLAIM: for the canonical 3-braid closures (sigma1 sigma2^-1)^n, whose SL(2,Z)
image is (RL)^n, the Rademacher function vanishes: Phi((RL)^n) = 0.

CURRENT EVIDENCE: three independent numerical/symbolic methods agree —
the Dedekind-sum formula in exact `Fraction` arithmetic, the RL-word count
(Phi = sum a_i - sum b_i), and homogeneity Phi(A^n) = n*Phi(A). This is the
basis of the scope-(a) refutation of the Rademacher route for theta_K.

WHY IT MATTERS: the refutation is durable and load-bearing (qou-rdmr is closed
on it). A Lean proof would make it permanent rather than resting on three
agreeing computations.

WHAT A PROOF NEEDS: the substantive content is the homogeneity / word-count
characterisation of the Rademacher function on hyperbolic conjugacy classes.
A bare `Phi := #R - #L` definition plus "balanced words give 0" would be
DEFINITIONAL and near-vacuous — do NOT ship that and call it a proof; the
vacuity audit would be right to flag it. The real target is the agreement of
the Dedekind-sum formula with the word count.

DIFFICULTY: medium. Dedekind sums exist in Mathlib
(`Mathlib.NumberTheory.DedekindSum`?  verify); the reciprocity law is the
likely lever.
