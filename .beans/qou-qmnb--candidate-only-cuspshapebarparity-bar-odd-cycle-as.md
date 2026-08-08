---
# qou-qmnb
title: 'CANDIDATE ONLY: CuspShapeBarParity bar-odd cycle as the theta_K identification'
status: todo
type: task
priority: normal
created_at: 2026-08-07T17:10:14Z
updated_at: 2026-08-07T17:10:14Z
---

AN UNVERIFIED IDENTIFICATION, flagged as a CANDIDATE in PR #4513 and in the
qou-offl bean. Recorded so it is not mistaken for a finding.

CLAIM UNDER CONSIDERATION: `QOU/Knot/CuspShapeBarParity.lean` identifies the
meridian as the bar-odd (boost) cycle and puts q on the boost hyperbola
`barEven q^2 - barOdd q^2 = 4`. The T4/T5 channel `ln^2 q0 - theta^2` carries
the same Minkowski signature, and the T4 probe's own language is
"boost-dominated (theta < ln q0)" / "spin-dominated (theta > ln q0)". So the
corpus may already contain an IDENTIFICATION of what theta_K is: the bar-odd /
Chern-Simons component against ln q0's bar-even / Vol component.

WHY IT IS ONLY A CANDIDATE: the signature match is suggestive, not established.
`ln^2 q0 - theta^2` is a quadratic form in (ln q0, theta); it is NOT literally
`barEven^2 - barOdd^2`. Nothing derives the identification.

WHY IT IS WORTH CHECKING ANYWAY: if it holds it supplies the "normalization
fixed in advance" that qou-offl was told it needs, which is the route's binding
precondition.

AND THE TRAP, ALREADY MEASURED: the obvious reading is dead on arrival. 4_1
cusp field Q(sqrt-3) -> angle pi/3; Borromean cusp field Q(i) -> angle pi/2;
ratio 3/2. That is a RATIO, and `AfreeThetaConstraint.ratio_attained` PROVES a
ratio-shaped candidate is unfalsifiable — it merely names A = 10.35 (the
rho = 1.5 row of the U2 discriminator table) and cannot be tested. Any pursuit
must yield theta ABSOLUTELY, per knot.
