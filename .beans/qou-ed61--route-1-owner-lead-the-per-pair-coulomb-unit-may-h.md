---
# qou-ed61
title: 'ROUTE 1 (owner lead): the per-pair Coulomb unit may have the S_K FORM, not be a constant. S_K(q0) = A_omega * cuspModulus * (ln^2 q0 - theta_K^2) with A_omega=3 exact/q-independent (Stokes symmetry constant, proved) and cuspModulus=sqrt3/4 proved — the knot-dependence is entirely in theta_K = Im u_K (open G3 datum, bean qou-qnnq). If the mirror-series per-pair unit is S_K-shaped then holding it at the A=3 value is WRONG and the residual drift I measured (r=+0.71 for H_FH_Z) may BE the theta_K(A) profile. Attack: invert the series to extract implied theta_K per mirror pair and check they are real/bounded/monotone — would give the first numerical handle on the open G3 datum. Resolves qou-gcmn'
status: completed
type: task
priority: normal
created_at: 2026-08-01T21:33:59Z
updated_at: 2026-08-01T21:47:38Z
---


---
**Update 2026-08-31 — 🛑 THE PROPOSED ATTACK IS THE CIRCULAR-ANCHOR PATTERN, and
this bean's title over-claims one of its two "proved" constants.**

Owner asked to try this route. Answer came from the corpus-grep checklist, not a
probe. Scope (a); nothing refuted, nothing wired, no compute run.

**1. The inversion is already in the corpus and is why an audit class exists.**
`computations/qbeta/qbeta_t4_stokes3_crux_probe.py` fixes `A_omega = 3` and
defines `theta2 = ln2_q0 - S/(A_omega*kappa)` at each anchor, reporting real
theta as confirmation. `content/pipeline/circular-anchor-audit.ts` was written
BECAUSE of that probe and names it in its history: *"Recovering A from those
theta returns 3 BY CONSTRUCTION; the cited 0.6% two-anchor consistency is
rounding in the 8-digit theta values, not independent agreement."* Detector class
`circ-anchor-inverted-roundtrip`; analysis in
`docs/scope/2026-08-01-t4-anchor-circularity.md`.

The mirror-series version has the same shape: theta_A would be DEFINED by the
residual, so "the residual drift may BE the theta_K(A) profile" holds for ANY
residual. It is the inversion restated, not a finding about theta.

**2. Two of the three proposed checks are vacuous, by sorry-free Lean on main.**
`QOU.QBeta.ThetaRealityBound`, whose own docstring says so:
- REAL: `thetaSq_nonneg_iff` — reality is EXACTLY `A >= S/(kappa*ln^2 q0)`, a
  one-sided lower bound ON A. Binds only where S > 0; where S < 0 it is automatic
  (`thetaSq_pos_of_neg`). So "the theta come out real" is a statement about
  A_omega restated, not a measurement of theta.
- The T4 companion check: `diagonal_crossed` holds for EVERY A > 0 — *"not
  evidence for any particular A"*.
- MONOTONE: `thetaSq_nonneg_mono` already characterises it; an identity, not data.

**3. What survives, and it is blocked on qou-gcmn.** Exactly one non-circular
quantity: the tightest lower bound on A_omega the mirror series supports,
`max_A S_A/(kappa*ln^2 q0)` over pairs with `S_A > 0`. Genuinely falsifiable —
if it exceeded 3, `A_omega = 3` would be refuted by the mirror data. It cannot be
computed today: it needs a per-pair `S_A` across the series, and `qou-gcmn`
(todo) IS the statement that this does not exist ("the per-pair Coulomb unit is
held at its A=3 H_6 value across the whole A=3..41 series … the single biggest
blocker"). Running the inversion on the A=3-held unit reproduces the circularity
rather than escaping it.

**4. CORRECTION to this bean's own title.** It says `A_omega=3` is "(Stokes
symmetry constant, **proved**)". It is **conditional**:
`content/quantum-observable-universe/mass-theory/aomega-fourone-dt-count.md`
opens *"**Theorem (conditional on `conj:stokes-dt-bps-bridge`).**"*, and
`content/bib-qa-verifications.json` records that *"the '5 ∉ {3,4}' exclusion
licensing A_ω = 3 rests on an unsourced step"* and that *"the downstream A_ω = 3
argument should carry that conditionality explicitly"*. This is the
conditional-proved ≠ premise-established failure, sitting in a COMPLETED bean —
the status a later agent is most likely to read as settled. (`cuspModulus = √3/4`
is not disputed here.)

**5. SYMBOL COLLISION.** `A_ω` in `computations/deltalambda/` is
`4√2·e^{−3/8} = 3.888`, a Bridge Stokes datum — NOT the `A_ω = 3` of the qbeta
arc. Two objects, one name, ~0.9 apart. Same class as markovZ/markovZC/markovZc.
Resolve any `A_ω` to its definition before using its value.

**Recommendation (judgement):** leave this bean closed with the correction; treat
`qou-gcmn` as the actual prerequisite — it blocks this and `qou-o6ml` both.
Nothing here refutes the `S_K` FORM; what is refuted is that this inversion is
evidence for it.

Audit: `docs/audits/2026-08-31-ed61-theta-inversion-is-the-circular-anchor-pattern.md`.
