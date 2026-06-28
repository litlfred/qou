---
# z3a2
title: 'Compute infra: factor shared Young-diagram/dim_q/S(m) machinery into reusable cached module'
status: todo
type: task
priority: normal
created_at: 2026-06-28T06:54:32Z
updated_at: 2026-06-28T15:06:10Z
---


**Progress 2026-06-28:** young_qdim shared module merged (#2952). Migrated 3/7 probes to import from it, verified equivalent (lever1_binding_habiro_qexponential re-run → byte-identical L_m; lever1_qholonomic_kernel_fit + lever1_qholonomic_order3_fit use only q+S, proven-identical via S(3)=(q+1)²/q). Remaining 4 have per-probe quirks (lever1_qinvolution_kernel_test: qint_asym; binding_qaskey_product_probe: qpoch; wlambda_identity_i_structure_probe: classical f_lambda; lever1_lw_depth2: pre-existing) — partial migration (symmetric machinery only), follow-on.



**2026-06-28:** lever1_lw_depth2 migrated (lw via S). 4/7 probes now migrated; remaining 3 (qinvolution qint_asym, qaskey qpoch, wlambda f_lambda) are symmetric-only partials — follow-on.
