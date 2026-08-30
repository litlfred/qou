---
# qou-o6ov
title: 'GAP: Magnus tr(rho_lambda Omega2) decays with b(lambda) -- prove it'
status: todo
type: task
priority: normal
created_at: 2026-08-30T17:41:56Z
updated_at: 2026-08-30T18:02:31Z
---

Open theorem. Measured: |c_lambda|=y_lambda|tr(rho_lambda Omega2_lambda)| concentrates on low b=n-lambda_1 (b=1 reflection rep 86->92% for A=3->4). The naive bound |tr|<=q^L*dim FAILS (Sigma y*dim tail plateaus at 0.5, #6183/#6265) -- concentration is a tr cancellation (tr(Omega2)=0), NOT a weight effect. Route: Kerov-Olshanski shifted-symmetric bounded-degree + traceless cancellation = cluster/cumulant statement (Procacci-Yuhjtman/Rebenko ingested). Proving this upgrades the poly-size row-truncation from heuristic to a rigorous error bound (pins the 60-dps partition count). PRs #6265.

RESEARCH (2026-08-30): Kerov-Olshanski route tested empirically on A=3 (28 partitions dim>1). tr(rho_lambda Omega2)/dim_lambda is NOT a low-degree polynomial in content power-sums p_k=Sum c^k: max rel resid only 0.94->0.29(deg1)->0.20(deg2)->0.08(9 terms), no collapse to machine-zero (a true low-degree content polynomial nails it). So the germ-trace is OUTSIDE the standard polynomial-functions-on-Young-diagrams framework (rho*Omega2 neither central nor group-algebra element) -- naive content-polynomiality proof route REFUTED for this normalization. Steers the proof to the cluster/cumulant route (tr(Omega2)=0 connected-diagram cancellation), not content moments.

REFINEMENT (2026-08-30): the theorem statement 'raw |tr| decays with b' is FALSE as written -- measured |tr(10,2)|=12634 > |tr(11,1)|=12211 at A=4 (bump at b=2). The bump tracks dim (peaks mid-sector). The quantity that DECAYS is |tr|/dim (A=4 2-row: 1110,234,71,28,19,22 by b) or equivalently the y-weighted contribution c_lambda=y_lambda*tr. Also: the 2-row sector gives NO clean closed-form decay law (tr non-monotonic, inter-j ratios drift 0.51-1.03, sign-flip at (5,4)/A=3), so the closed-form-2-row proof route is not clean either. Correct theorem: |tr(rho_lambda Omega2)|/dim_lambda decays with b(lambda). Proof still open (cluster/cumulant route).
