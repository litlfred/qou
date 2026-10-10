---
# qou-qmnb
title: 'CANDIDATE ONLY: CuspShapeBarParity bar-odd cycle as the theta_K identification'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:10:14Z
updated_at: 2026-10-04T15:16:51Z
parent: qou-avtq
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

---

# ATTACK VECTORS (2026-08-08)

## Where it sits in the chain

`CuspShapeBarParity` sits at the **substrate/geometry interface** — the same
junction as `qou-8vt2`'s bridge `u`. That is not a coincidence and it is the
reason this candidate is worth testing: it is a proposal for what the bridge IS,
phrased in bar-parity language.

## AV1 — the strongest available check is the DIAGONAL, not the ratio

This bean already records that the obvious cusp-field reading is ratio-shaped and
therefore unfalsifiable (`ratio_attained`). But there is an A_omega-free,
ABSOLUTE constraint available that the bean does not yet use:

    `signflip_forces_diagonal_cross` (FigureEightComplexVolume, proved)
    the measured flip S_muon > 0 > S_proton FORCES u to cross |Re u| = |Im u|.

So any bar-parity identification must put the two anchors on OPPOSITE SIDES of
the diagonal `|Re u| = |Im u|`. That is a yes/no test per candidate, needs no
A_omega, and is not ratio-shaped. Apply it BEFORE computing any magnitude.

## AV2 — the signature match can be made precise or killed

The bean notes `ln^2 q0 - theta^2` "is NOT literally `barEven^2 - barOdd^2`".
Make that concrete: `barEven q^2 - barOdd q^2 = 4` is the boost hyperbola, while
`Im V_41 = kappa(Re^2 u - Im^2 u)` is a harmonic form vanishing on the diagonals.
Both are Minkowski-signature but with DIFFERENT invariant level sets (a hyperbola
at level 4 vs a cone at level 0). Either exhibit the map taking one to the other,
or record that the signature coincidence is generic to any (+,-) form and
therefore evidentially worthless. Both outcomes are useful; the second closes it.

## AV3 — cross-check against qou-8vt2 AV2

If the anchors sit at the complete structure (u = 0), any identification sending
the cusp datum to `u` must explain why `u != 0` at the anchors. A bar-parity
reading that lands on u = 0 is excluded immediately by the measured S != 0.

## GUARD (unchanged)

Any pursuit must yield theta ABSOLUTELY, per knot. A ratio is unfalsifiable and
does not close this bean.
