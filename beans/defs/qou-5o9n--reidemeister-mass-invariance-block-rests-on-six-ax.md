---
# qou-5o9n
title: Reidemeister mass-invariance block rests on six axioms
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:31Z
updated_at: 2026-11-22T09:51:31Z
parent: qou-uwyf
---

mass-theory/reidemeister-mass-invariance.lean declares axiom bareMass, bareMass_R1_invariant, bareMass_R2_invariant, bindingEnergy, bindingEnergy_R2_invariant, bindingEnergy_R1_changes. The block is a conjecture conditional on conj:borromean-quark; recast the axioms as a content-bearing class (AGENTS §3b-cond) so the dependency is in the type.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22 (branch claude/honest-lean-descent-reidemeister-schurweyl-2026-11-22, commit 3870f504e): six axioms replaced by class ReidemeisterMassInvariance (bareMass bindingEnergy); consistent (mass 0, energy writhe) and refutable (constant energy). New bareMass_eq_of_parity: on the (writhe, crossingNumber) carrier any R-I/R-II invariant depends only on (w+c) mod 2, so the carrier cannot hold a hyperbolic volume. conj:borromean-quark link not encoded (types unrelated). 0 axioms in file.
