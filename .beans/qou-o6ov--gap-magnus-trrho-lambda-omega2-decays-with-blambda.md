---
# qou-o6ov
title: 'GAP: Magnus tr(rho_lambda Omega2) decays with b(lambda) -- prove it'
status: todo
type: task
priority: normal
created_at: 2026-08-30T17:41:56Z
updated_at: 2026-08-30T17:48:16Z
---

Open theorem. Measured: |c_lambda|=y_lambda|tr(rho_lambda Omega2_lambda)| concentrates on low b=n-lambda_1 (b=1 reflection rep 86->92% for A=3->4). The naive bound |tr|<=q^L*dim FAILS (Sigma y*dim tail plateaus at 0.5, #6183/#6265) -- concentration is a tr cancellation (tr(Omega2)=0), NOT a weight effect. Route: Kerov-Olshanski shifted-symmetric bounded-degree + traceless cancellation = cluster/cumulant statement (Procacci-Yuhjtman/Rebenko ingested). Proving this upgrades the poly-size row-truncation from heuristic to a rigorous error bound (pins the 60-dps partition count). PRs #6265.

RESEARCH (2026-08-30): Kerov-Olshanski route tested empirically on A=3 (28 partitions dim>1). tr(rho_lambda Omega2)/dim_lambda is NOT a low-degree polynomial in content power-sums p_k=Sum c^k: max rel resid only 0.94->0.29(deg1)->0.20(deg2)->0.08(9 terms), no collapse to machine-zero (a true low-degree content polynomial nails it). So the germ-trace is OUTSIDE the standard polynomial-functions-on-Young-diagrams framework (rho*Omega2 neither central nor group-algebra element) -- naive content-polynomiality proof route REFUTED for this normalization. Steers the proof to the cluster/cumulant route (tr(Omega2)=0 connected-diagram cancellation), not content moments.
