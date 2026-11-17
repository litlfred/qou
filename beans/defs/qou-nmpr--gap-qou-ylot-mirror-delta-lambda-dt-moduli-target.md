---
# qou-nmpr
title: 'GAP (qou-ylot mirror): Delta_lambda DT-moduli — target under-determines it; concentration obstruction open'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:13:18Z
updated_at: 2026-10-04T15:12:42Z
parent: qou-v2om
---

Epic qou-r2nh · mirrors bean qou-ylot (which lives on the PR #4553 branch, not on main).
PR #4559 · branch claude/deltalambda-dt-substrate-derivation-2026-08-01.

## VERDICT (sorry-free, PR #4559)

The Delta_lambda = Behrend-signed DT-count identity (PR #4553) is the right
categorical HOME but is limitatively INSUFFICIENT to force the Springer moduli
B_lambda from the 13 categorical drivers.

Proved (DeltaLambdaDTModuliUnderdetermined.lean, base ring Z):
- IsDTRealization md vc := forall lambda, (-1)^{md} * vc = Delta_lambda.
- canonical_dt_realization: (n(lambda), dim V_lambda) realizes Delta_lambda.
- shifted_dt_realization: (n(lambda)+2, dim V_lambda) ALSO realizes it.
- dt_moduliDim_sign_forced: target pins only the Behrend sign (-1)^{md} = (-1)^{n(lambda)}.
- dt_moduliDim_underdetermined: two DISTINCT moduli dims both realize Delta_lambda.

So matching Delta_lambda constrains the moduli dimension only mod 2 (parity) +
the count dim V_lambda; it never singles out the Springer value n(lambda) =
dim_C B_lambda. The toy moduliDim:=nStat merely READS the answer. The internal
derivation (DeltaLambdaDTRealization) stays OPEN, now sharply bounded. Mirrors
the A_omega=3 "structurally-open" verdict (#4554 / qou-qnnq) from a second
direction.

## NEXT HONEST STEP (the residual obstruction)

The single-degree concentration (top-cohomology selection) is the load-bearing
extra structure: the coinvariant grading spreads V_lambda over the fake-degree
poly f_lambda(q) whose signed value f_lambda(-1) != Delta_lambda (e.g. (2,1):
f(-1)=0 != -2). Encode the n=5 fake-degree polynomials; prove f_lambda(-1) !=
Delta_lambda (concentration is essential); then test whether the confinement SDP
/ canonical T_w forces the top-degree projection. If yes -> derivation closes;
if no -> substrate under-determines the realization and the DT home is an avatar.

Lean: folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTModuliUnderdetermined.lean
Audit: docs/audits/2026-08-01-deltalambda-dt-substrate-derivation.md
Discipline: 0 free params; Delta_lambda/AME/CODATA/q0 never inverted; no instance fabricated.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 66 — PR #8274)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8274`](https://github.com/litlfred/qou/pull/8274) (branch `feat/round66-young-alien-lp-dt-spectral-43c1`, Commit 1 `efa6ab9e44128d259563d9e6208d6ab9d32edd74`, Commit 2 / Head `5423d4a1b0e6c19be96012412c48bd64329fdf2c`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTModuliUnderdetermined.lean (`even_shifted_dt_realization`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/young_kernel_alien_lp_dt_spectral_probe.py` (`scriptHash: 68202cff458f`) + `test/results/witnesses/young-kernel-alien-lp-dt-spectral.witness.json` (`allPassed: true`).
