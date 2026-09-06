---
# qou-742w
title: The M1 leading constants are typed into twelve scripts, not imported
status: todo
type: task
priority: normal
created_at: 2026-09-06T06:28:48Z
updated_at: 2026-09-06T06:29:17Z
---

Found by the `qou-psjm` hand pass over the witness-copy audit. Full taxonomy:
`docs/audits/2026-09-06-witness-copy-hand-pass-taxonomy.md`.

## The defect

Twelve sibling scripts under `computations/deltalambda/wlambda_covariance_epic_M1_*`
each TYPE IN the same three constants, every one annotated "merged #5901":

    M_INF         = mp.mpf('0.300186614161')   # IO leading (CS) margin
    SIG_RATIO_INF = mp.mpf('0.679609581496')   # sigma_D/sigma_A limit
    RHO_INF       = mp.mpf('0.979796195657')   # IO leading rho_P

Twelve digits each, twelve copies, no shared module and no witness load. Re-run
#5901's producer and twelve scripts go stale simultaneously with nothing to
detect it. Highest-value single drain in the 232-finding queue; the fix is one
shared constants module.

The twelve: CA_to_margin_conversion, constant_C_landscape, debye_CA_investigation,
delta_ratio_structure, descent_dpp_variance_rate, finite_n_cs_margin,
ingredient_envelope_convergence, margin_envelope_exponent, margin_leg_decomposition,
naive_budget_closes_probe, pointwise_shortfall_recomputed, sigmaD_leg_rate.

## A second question, NOT for this bean to answer

`margin_leg_decomposition.py:45` annotates RHO_INF as `# = 2 sqrt(6)/5`. Measured
at dps 30:

    literal   0.979796195657
    2*sqrt(6)/5  0.97979589711327123928     rel 3.05e-07

They diverge at the 6th significant digit. Three distinct values near 0.9797 sit
in the corpus (0.9797938112..., 0.979796195657, 0.979798768510...) and NONE is
2*sqrt(6)/5.

Either reading changes what the fix should be:
  - conjectured closed form  -> carry the producer's full precision, not 12 digits
  - actual identity          -> compute 2*mp.sqrt(6)/5 exactly; the literal is lossy

That is the M1 epic's own call, not an infrastructure decision. Whoever owns
#5901 should settle it before the shared module fixes the spelling of a value
whose provenance is unresolved.

## Default if nobody acts

Nothing breaks today. The twelve stay in the witness-copy baseline as class-D
findings and the audit keeps reporting them. The risk is latent and realises only
when the M1 producer is next re-run.
