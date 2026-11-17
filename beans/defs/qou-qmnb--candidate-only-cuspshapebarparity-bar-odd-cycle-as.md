---
# qou-qmnb
title: 'CANDIDATE ONLY: CuspShapeBarParity bar-odd cycle as the theta_K identification'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:10:14Z
updated_at: 2026-11-15T17:33:13Z
parent: qou-avtq
blocked_by:
    - qou-cds1
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


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** AV1 cannot be applied: the measured sign flip it presupposes is unresolved (sign_flip_resolved=False). AV2 (is the (+,−) signature match generic?) needs no data and can still close the candidate.

Evidence: AV1, its only decisive test, uses `signflip_forces_diagonal_cross` (FigureEight:204, sorry-free), whose antecedent (the anchor sign flip) is unresolved per the witness. AV2, whether the signature match is generic, is data-free and undone. CuspShapeBarParity.lean has 0 real sorries.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Progress Update (Round 65 — PR #8267)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8267`](https://github.com/litlfred/qou/pull/8267) (branch `feat/round65-radical-branching-bond-habiro-cusp-43c1`, Commit 1 `20143712c434683951cbe6f568953fd4a98454bc`, Commit 2 / Head `1ee46ede72413597113d706dd733554a25e327d5`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/Knot/CuspShapeBarParity.lean (`cusp_holonomy_hyperbola_and_reconstruct`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/radical_branching_bond_habiro_cusp_probe.py` (`scriptHash: 949a90321cd5`) + `test/results/witnesses/radical-branching-bond-habiro-cusp.witness.json` (`allPassed: true`).
