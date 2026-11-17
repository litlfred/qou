---
# qou-se8k
title: 'A5: IMME rank<=2 as a body-order meter (prune before searching)'
status: in-progress
pr: 8327
branch: feat/qou-3lsb-3wxk-ebs6-se8k-wdij
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T08:37:43Z
updated_at: 2026-10-04T15:16:10Z
parent: qou-v2om
---

IMME M(T3)=a+b*T3+c*T3^2 is quadratic because 2-body charge-dependent interactions carry isospin rank<=2; a 3-body force generates rank 3. Measured d/a ~ 1e-7. **ROAST:** IMME constrains the CHARGE-DEPENDENT sector, but the missing extensive term is isoscalar by hypothesis -- so IMME may say nothing about it. Likely re-derives a known negative (option-e already excluded p/n-asymmetry candidates as the magnitude). Downgrade pending that check. Also rank<=2 assumes first-order perturbation theory; isospin mixing generates d too.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`AlphaClusterContactCeilingAndDOFCount.lean`, `ExpansionParameterMismatchAndIMMEIsoscalarBlindness.lean`, `NonMonotoneBorromeanWordAndDisjointBlockEpsilonProduct.lean`) and verified at 50 dps in `computations/probes/alpha_contact_expansion_hierarchy_imme_blindness_nonmonotone_block_probe.py` (`computations/probes/alpha-contact-expansion-hierarchy-imme-blindness-nonmonotone-block-probe.witness.json`, `allPassed = true`). Opened PR #8327 (`ready: 826901651d0315e3267e85bf8f3b7fc2527847c3`).
