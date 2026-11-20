---
# qou-fdjp
title: 'MEASURED: the proton re-pin moves binding by 128 ppb; the binding error is 21-226% — R2 cannot be the cause'
status: todo
pr: 8219
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T16:38:29Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## The arithmetic (measured 2026-08-25, PR #5765)

Every binding column in `mass_binding_dashboard.py` scales LINEARLY in
`alpha = E_0 = m_e / (q_0 (q_0 - 1))`. So the pin question reduces to: how much
does `E_0` move between the two pins?

Computed at 50 dps, `m_e = 0.51099895069 MeV`:

| pin | q_0 | E_0 |
|---|---|---|
| proton (`qou_substrate.constants.Q`) | 1.1099785827513808 | **4.185981363 MeV** |
| muon (`q-pinning-50-digit.witness.json`) | 1.10997859555733471989976322048322502665620840878015368660798114614493 | **4.185980828 MeV** |

Relative difference: **127.978 ppb**.

## Consequence

The live binding errors are 21% (2H) to 226% (4He). The pin moves them by
1.28e-7 (0.0000128%). The ratio is

    2.26 / 1.28e-7  ~=  1.8e7

**Seven orders of magnitude.** The proton re-pin (owner ruling R2) therefore
CANNOT be a cause of the mass/binding error, at any isotope, by any amount that
matters. This is not an estimate - `alpha` enters linearly, so the bound is exact.

## What this does and does not settle

- **R2 (proton pin) is ruled out as an error source** for binding. Migrating the
  pin is still correct-by-directive and still matters for ppb-scale observables
  (m_n at +501 ppb, the mu-p tension) - but it is NOT the mass/binding story.
- **R3 (colour weighting) is bounded small too**, from the dashboard's own
  Colour-weighting table: the chirality term is +0.00 to +0.56 MeV against a
  2-20 MeV residual, and `B_sym` vs `B_qCLT_fac` agree to ~1-2%. So it is at most
  a few percent of the gap, and it is ALREADY applied in the live run.
- **R1 (convention C -> D) is the ONLY staleness axis left that could be O(1)**,
  because `z` enters `tr_M` itself and hence the bond values `L_pp/L_pn/L_nn`.
  Its magnitude on this cone is NOT yet measured. That measurement is the
  highest-leverage remaining item on the staleness side.

## Scope (per the AGENTS.md (a)/(b) rule)
This is a scope-(b) STRUCTURAL exclusion for R2, not a scope-(a) negative: the
invariant cited is that `alpha` enters every binding form linearly, so a 128 ppb
shift in `alpha` cannot produce a >1% change in any of them. R3's bound is
scope-(a) (measured on the current forms, not proved).


## Progress Update (PR #8219)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`ThermodynamicTemperatureAndRepinBound.lean`, `SiteVsBondVolumeFactorTwo.lean`, `TwoDimensionalInterfaceCollapseAndOrdering.lean`, `WritheSignOppositionEndpointSplit.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` probe (`computations/probes/kt_repin_octahedron_interface_writhe_probe.py`) and stamped witness (`computations/probes/kt-repin-octahedron-interface-writhe-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8219 (`ready: 0004396c02a14ba756cc43c66855073b0a08f82d`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8219, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
