---
# qou-ch8w
title: Μ₀ −9% closure via higher-order NA-Stokes (co)unit expansion (A/B/C/D)
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T17:54:14Z
updated_at: 2026-11-16T19:19:00Z
parent: qou-wp3h
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-19 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: μ₀ −9% closure via higher-order NA-Stokes (co)unit expansion (A/B/C/D)

## Progress Update (2026-11-16 — PR #8164)
- **PR:** [`litlfred/qou#8164`](https://github.com/litlfred/qou/pull/8164) (`47da262e4f487a8f51de58f3577a63d5b17e6d6a`)
- **Resolution:**
  - Formalized the 4th-order NA-Stokes counit expansion `naStokesMuEff` and its bar-even ($\cosh$) / bar-odd ($\sinh$) channel decomposition (`naStokesMuEff_bar_parity_split`) in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanChiPerRep.lean` (`0` `sorry`) and verified at 50+ dps in `computations/probes/na_stokes_bar_parity_local_bond_probe.py` (`na-stokes-bar-parity-local-bond.witness.json`).
  - Status kept at `in-progress` pending PR #8164 merge and owner verification.
