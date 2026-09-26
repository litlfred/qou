---
# qou-yau0
title: 'Residual shape on the normalised bond-counting law: which of symmetry / surface / Coulomb / pairing survives once the writhe artifact is removed'
status: completed
type: task
priority: normal
created_at: 2026-09-04T20:46:50Z
updated_at: 2026-09-05T07:29:46Z
---

Branch claude/normalised-law-residual-shape-2026-09-04. The follow-on qou-hfjc's audit §6 recommended: re-measure #6611's residual shape on the normalised (bond-counting) law, with the un-normalised law as control.

PROBE normalised_law_residual_shape_probe.py (9/9, 50 dps, #6611's AME selection + helpers; control reproduces #6611's −0.804 / −0.178 to 3 dp). Normalised residual r = B_exp/(ε(A−1)): asymmetry corr −0.6965 (was −0.8038), surface −0.2980 (was −0.1781), Coulomb −0.043, pairing +0.096. So ~13 % of the un-normalised symmetry signal was the writhe artifact and the surface signal doubles; #6611's 'wrong by 4×' (asym vs surface) is 2.3× on the artifact-free law. SEMF shape test (least-squares projection, diagnostic only, nothing wired): R² = 0.9616 (control 0.9282), all four corrections SEMF-signed, ratios to volume: surface −0.83 (SEMF −1.13), Coulomb −0.041 (−0.045), asymmetry −1.27 (−1.50), pairing +0.04 (+0.71, mostly missed). κ scan on the normalised law: optimum ≈ −0.2 (p5–p95 1.1656 vs 1.1808 at κ = 0; #6611's ln2-form optimum ≈ −0.15); κ = 0 beats the un-normalised κ_derived = +0.22 (1.2069).

Cross-ref qou-ib3g (#6668): its 'per-nucleon coefficient at N=Z, E_0·0.698581 = 2.92425 MeV' IS ε — un-normalised pp/nn average −ln(zz')/2 = ln[2]_q identically (checked) — so its factor 3.0075 applies to the normalised law unchanged; not re-measured.

VERDICT: the residual has the SEMF shape on the artifact-free law; asymmetry still dominant, surface a live lead again. Recommendation (judgement): update the decision frame's lead ranking to the surviving numbers. Audit docs/audits/2026-09-04-normalised-law-residual-shape.md. Nothing wired.


## 2026-09-05 (qou-kqdn) — follow-on on the re-promoted surface lead: the boundary deficit of a bounded-degree bond count DERIVES the A^{−1/3} shape exactly (Lean, sorry-free), refining bounded_degree_saturates. But its magnitude test is measured GENERIC (67.9 % of the plausible window), so only the shape is a result. docs/audits/2026-09-05-coordination-surface-deficit.md.
