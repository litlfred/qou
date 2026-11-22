---
# qou-5o9n
title: Reidemeister mass-invariance block rests on six axioms
status: completed
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:31Z
updated_at: 2026-11-22T21:31:33Z
parent: qou-uwyf
---

mass-theory/reidemeister-mass-invariance.lean declares axiom bareMass, bareMass_R1_invariant, bareMass_R2_invariant, bindingEnergy, bindingEnergy_R2_invariant, bindingEnergy_R1_changes. The block is a conjecture conditional on conj:borromean-quark; recast the axioms as a content-bearing class (AGENTS §3b-cond) so the dependency is in the type.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22 (branch claude/honest-lean-descent-reidemeister-schurweyl-2026-11-22, commit 3870f504e): six axioms replaced by class ReidemeisterMassInvariance (bareMass bindingEnergy); consistent (mass 0, energy writhe) and refutable (constant energy). New bareMass_eq_of_parity: on the (writhe, crossingNumber) carrier any R-I/R-II invariant depends only on (w+c) mod 2, so the carrier cannot hold a hyperbolic volume. conj:borromean-quark link not encoded (types unrelated). 0 axioms in file.

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.
Done on main: PR #8999 merged 2026-11-22T10:58Z (merge fc2a6fab5). `mass-theory/reidemeister-mass-invariance.lean` has 0 `axiom` declarations; the six are the class `ReidemeisterMassInvariance`, as this bean asked. The link to `conj:borromean-quark` is not encoded (types unrelated), as the previous note says; that is a separate item, not this bean's ask.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE (evidence in the closing note above). Premises checked: the bean and the fixed Lean name no retired object (no σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photon or SM-adopted quark charge). The fix is structural Lean hygiene, so it is independent of the physics rulings.
