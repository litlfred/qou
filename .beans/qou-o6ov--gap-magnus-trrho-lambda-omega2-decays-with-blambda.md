---
# qou-o6ov
title: 'GAP: Magnus tr(rho_lambda Omega2) decays with b(lambda) -- prove it'
status: todo
type: task
created_at: 2026-08-30T17:41:56Z
updated_at: 2026-08-30T17:41:56Z
---

Open theorem. Measured: |c_lambda|=y_lambda|tr(rho_lambda Omega2_lambda)| concentrates on low b=n-lambda_1 (b=1 reflection rep 86->92% for A=3->4). The naive bound |tr|<=q^L*dim FAILS (Sigma y*dim tail plateaus at 0.5, #6183/#6265) -- concentration is a tr cancellation (tr(Omega2)=0), NOT a weight effect. Route: Kerov-Olshanski shifted-symmetric bounded-degree + traceless cancellation = cluster/cumulant statement (Procacci-Yuhjtman/Rebenko ingested). Proving this upgrades the poly-size row-truncation from heuristic to a rigorous error bound (pins the 60-dps partition count). PRs #6265.
