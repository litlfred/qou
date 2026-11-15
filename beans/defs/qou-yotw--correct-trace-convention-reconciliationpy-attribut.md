---
# qou-yotw
title: 'correct trace_convention_reconciliation.py attribution: z_C is not the canonical MASS convention'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T13:28:07Z
updated_at: 2026-11-15T20:20:00Z
parent: qou-cdx1
---

## 2026-11-15 — Convention-D update (`litlfred/qou#7986`)

- Updated `computations/trace_convention_reconciliation.py` and regenerated `computations/trace-convention-reconciliation.witness.json` per owner ruling `Q-CDX1-1 = 1`:
  - Retired the excised `z_C = q/(q^2+q+1)` (`N = 3` SU(3) convention) as the production mass convention.
  - Set `z_D = q^3/(q^2+1)` (`N = 2` SU(2) Temperley-Lieb / Wenzl two-row cap) as the canonical mass/binding convention at the 50-digit proton pin (`0.14704667798040846910949472901991769100370850974176` from `binding-canonical.witness.json`), while preserving `0.5952397103674884` (`hecke_h_n_dp.witness.json`) for historical provenance.
- PR: [`litlfred/qou#7986`](https://github.com/litlfred/qou/pull/7986) (commit `fd12a6522e45d32a4855f0b4dd0db7ac856c2986`, signed `ready:` comment [`#issuecomment-6900782211`](https://github.com/litlfred/qou/pull/7986#issuecomment-6900782211)).

