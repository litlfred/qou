---
# qou-3lsb
title: 'GAP-4: cluster/halo deviations below max-contact (⁶Li α+d, ⁹Be)'
status: todo
pr: 8327
branch: feat/qou-3lsb-3wxk-ebs6-se8k-wdij
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T23:11:26Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---


## Reference

Gap map + anti-fit checkpoint: [`docs/workplans/2026-07-11-mnk-derivation-gaps.md`](../docs/workplans/2026-07-11-mnk-derivation-gaps.md). Parent: `qou-v0yw` (M_n(K) closure, ungated 2026-07-11 via #3607). Coordinate with #3545/#3585/#3588/#3549/#3548 before solo compute.

## Update 2026-07-11 — GAP-4 core is #3551 (anti-duplication); narrowed remainder

Corpus-grep (before writing a GAP-4 probe) found the α-cluster contact structure is ALREADY
computed: `bk_alpha_geometry_selection.py` + #3551 read B(nα)=n_α·B(⁴He)+N_contacts·b_αα with
max-contact SELECTION — the identical GAP-1 principle one scale up (α's; α-α bonds = 3n_α−6).
GAP-2b's constant Li residual is the nucleon-side confirmation of the same fact.

**Resolved-by-#3551.** Narrowed remainder (kept open): (1) the ²⁰Ne one-bond prolate DOF
(α+¹⁶O, below max-contact); (2) `b_αα`≈2.4 MeV is empirical — its substrate derivation is the
α-level analogue of the nucleon `b*` (#3545 Part 12 connected tr_M / Gram norm), same object one
scale up. Bridge: docs/audits/2026-07-11-gap4-alpha-bridge-gap3-frontier.md.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-12 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`AlphaClusterContactCeilingAndDOFCount.lean`, `ExpansionParameterMismatchAndIMMEIsoscalarBlindness.lean`, `NonMonotoneBorromeanWordAndDisjointBlockEpsilonProduct.lean`) and verified at 50 dps in `computations/probes/alpha_contact_expansion_hierarchy_imme_blindness_nonmonotone_block_probe.py` (`computations/probes/alpha-contact-expansion-hierarchy-imme-blindness-nonmonotone-block-probe.witness.json`, `allPassed = true`). Opened PR #8327 (`ready: 826901651d0315e3267e85bf8f3b7fc2527847c3`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8327, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
