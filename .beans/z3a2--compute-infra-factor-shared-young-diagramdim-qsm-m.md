---
# z3a2
title: 'Compute infra: factor shared Young-diagram/dim_q/S(m) machinery into reusable cached module'
status: todo
type: task
priority: normal
created_at: 2026-06-28T06:54:32Z
updated_at: 2026-06-28T23:55:00Z
---


**Progress 2026-06-28:** young_qdim shared module merged (#2952). Migrated 3/7 probes to import from it, verified equivalent (lever1_binding_habiro_qexponential re-run → byte-identical L_m; lever1_qholonomic_kernel_fit + lever1_qholonomic_order3_fit use only q+S, proven-identical via S(3)=(q+1)²/q). Remaining 4 have per-probe quirks (lever1_qinvolution_kernel_test: qint_asym; binding_qaskey_product_probe: qpoch; wlambda_identity_i_structure_probe: classical f_lambda; lever1_lw_depth2: pre-existing) — partial migration (symmetric machinery only), follow-on.



**2026-06-28:** lever1_lw_depth2 migrated (lw via S). 4/7 probes now migrated; remaining 3 (qinvolution qint_asym, qaskey qpoch, wlambda f_lambda) are symmetric-only partials — follow-on.

**2026-06-28 (cont.):** lever1_qinvolution_kernel_test migrated — symmetric machinery (qint/qfact/dim_q/partitions/S) now imported from young_qdim; the probe-specific qint_asym (Gaussian) kept local. Verified: probe re-run → witness BYTE-IDENTICAL (stored values are q0 numeric evals + sp.factor canonical strings, form-independent). Source −35 lines (10 ins / 45 del). **5/7 migrated**; remaining 2 symmetric-only partials: binding_qaskey_product_probe (qpoch), wlambda_identity_i_structure_probe (classical f_lambda).
