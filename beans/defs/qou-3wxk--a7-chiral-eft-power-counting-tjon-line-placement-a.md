---
# qou-3wxk
title: 'A7: chiral-EFT power counting / Tjon-line placement as magnitude diagnostic'
status: todo
pr: 8327
branch: feat/qou-3lsb-3wxk-ebs6-se8k-wdij
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T08:37:53Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Tells us whether r* is 3-body-sized or normalization-sized (mutually diagnostic with A1/qou-78pt). **ROAST:** importing chiral EFT imports a DIFFERENT EFT's hierarchy (Q/Lambda_chi); QOU has its own expansion parameter u = b*hbar_q^2 ~ 0.00852. No reason the two align. Smuggles in exactly the nuclear phenomenology the framework aims to replace. Use only as a placement diagnostic, never as a magnitude input.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`AlphaClusterContactCeilingAndDOFCount.lean`, `ExpansionParameterMismatchAndIMMEIsoscalarBlindness.lean`, `NonMonotoneBorromeanWordAndDisjointBlockEpsilonProduct.lean`) and verified at 50 dps in `computations/probes/alpha_contact_expansion_hierarchy_imme_blindness_nonmonotone_block_probe.py` (`computations/probes/alpha-contact-expansion-hierarchy-imme-blindness-nonmonotone-block-probe.witness.json`, `allPassed = true`). Opened PR #8327 (`ready: 826901651d0315e3267e85bf8f3b7fc2527847c3`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8327, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
