---
# qdzu
title: 'rho_k_h3a probes: Schur-Weyl self-check tolerance floor (~1e-8) + crystal WRONG_SIGN'
status: todo
type: task
created_at: 2026-07-05T11:51:01Z
updated_at: 2026-07-05T11:51:01Z
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
