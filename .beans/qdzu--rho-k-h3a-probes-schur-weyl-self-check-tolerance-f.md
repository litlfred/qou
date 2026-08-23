---
# qdzu
title: 'rho_k_h3a probes: Schur-Weyl self-check tolerance floor (~1e-8) + crystal WRONG_SIGN'
status: in-progress
type: task
priority: normal
created_at: 2026-07-05T11:51:01Z
updated_at: 2026-08-16T21:25:03Z
---


## Evidence (surfaced by the 5-way witness-drain swarm, PR #3351, 2026-07-05)

Three exploratory Δ_λ probes exit nonzero on an internal self-check but
still rewrite their witnesses:

| producer | symptom |
|---|---|
| `computations/rho_k_h3a_crystal.py` | Schur-Weyl `|residual| = 4.74846e-8 FAIL` vs `1e-40` tol; also `Outcome: WRONG_SIGN (sum/target = -412.723)` |
| `computations/rho_k_h3a_lp_dual.py` | same `~1e-8` Schur-Weyl residual FAIL vs `1e-40` tol |
| `computations/rho_k_h3a_refinement.py` | same `~1e-8` residual FAIL vs `1e-40` tol |

The `~1e-8` residual is consistent across all three → a numeric-engine
precision floor, not a logic bug: the self-check tolerance (`1e-40`) is
set far below the engine's achievable precision (~`1e-8`). Two things to
disentangle:

1. **Tolerance floor** — either the compute should run at higher dps to
   actually reach `1e-40`, or the self-check tol should be relaxed to a
   realistic floor (and the witness `allPassed` reflect it honestly).
2. **crystal `WRONG_SIGN`** — `rho_k_h3a_crystal` reports the sum has the
   wrong sign vs target (`sum/target = -412.723`). Consistent with the
   PROBE-4 KL-positivity prune (crystal/KL route supplies magnitude not
   chirality sign); confirm it's the known prune, not a new regression.

These also emit deprecated `M_P_MEV`/`M_N_MEV`/`M_D_MEV` warnings
(three-calibration discipline) — non-fatal, worth cleaning while here.

**Scope:** exploratory probes, not in the mass-binding dashboard or any
production facade. Low priority. No action taken in #3351 (drain was
provenance-only); their witnesses record the failing state honestly.


---

## CORRECTION (PR #5260, 2026-08-16) — the precision-floor hypothesis is refuted

This bean's stated diagnosis is wrong on both halves. Measured, not argued:

    q_0 pin straddle (proton LHS vs muon witness)   8.33961e-8   97.8%
    witness internal self-inconsistency               1.852e-9    2.2%
    Schur-Weyl identity itself                     3.10271e-49     ~0%

**Not a precision floor.** The compute runs at 50 dps; a genuine engine floor
is ~1e-50, not ~1e-8. Matching the inputs drives the residual to 3.1e-49 — the
actual floor, 42 orders below the reported number. The original reasoning
("consistent across all three -> a floor") was pattern-matching on the number's
consistency, not a measurement of its cause; the consistency has a different
explanation, namely that all three probes share the same two inputs.

**Not a logic bug either.** The identity was proved to hold identically in q at
n=3 and n=6 in PR #5168 / bean qou-hdyp. beta_D on H_6 with 23 crossings is
that proof's n=6 atom.

**Actual cause:** the two sides are evaluated at different q_0 pins. LHS at
`q_parameter.Q_MP` (proton, experimental); RHS read from
`atomic-tr-m-mpfr-50dps.witness.json`, stamped `q0Anchor: "muon"`. Separation
11.5371 ppb = the mu-p substrate tension. Same class as
`mu3_anchor_consistency_probe.py`. There is a second, inner straddle inside
`chi_numeric`: `d_for_ctype`'s default delta is pinned at the numeric
`q_parameter.Q`.

Probe: `computations/deltalambda/rho_k_h3a_residual_decomposition.py`.
The 2% remainder is now bean qou-tzsp.

**Still open on this bean** (unchanged, and NOT addressed by #5260):
  * the `crystal` WRONG_SIGN (sum/target = -412.723) — untouched
  * the deprecated M_P_MEV / M_N_MEV / M_D_MEV warnings — untouched
  * whether the 1e-40 tolerance should be relaxed or the two sibling probes
    (`crystal`, `lp_dual`) re-pointed at a matched pin — the correct fix is the
    latter, but they were not re-run

Separately: the committed `rho-k-h3a-refinement.witness.json` was ALSO carrying
colour-blind chi (ctype "averaged", abs_tr_M 0.388... vs the colour-weighted
0.575172329...) and has been refreshed on that PR.
