---
# qou-6dcc
title: alpha_EM table cells in fine-structure-observation-table1-data have drifted from live values and are internally inconsistent (123.257 vs its own 123.280)
status: completed
type: task
priority: normal
created_at: 2026-08-29T06:26:47Z
updated_at: 2026-08-29T08:28:02Z
---

## RESOLVED 2026-08-29 — refreshed to the proton pin and CODATA 2022

Owner authorised the CODATA-vintage call ("refresh on CODATA 2022 as needed";
"2018 vintage/comparison, 2022 is current"), which was the only thing gating
this.

Every cell recomputed from the canonical `alpha_em_inv_derived` at the proton
pin (the standing default) against CODATA 2022 = 137.035999177(21):

  q^-1                   0.900918284
  [9]_q                  10.3635176
  [10]_q                 11.8942752
  [9]_q [10]_q           123.266530     <- now multiplies out
  bare alpha^-1          136.8232089
  delta_CS               0.00155060213
  CS-corrected alpha^-1  137.035935094
  discrepancy (bare)     -0.15528 %
  discrepancy (corr.)    -468 ppb

The internal inconsistency this bean was opened for is gone: the old table
showed [9][10] = 123.257 against its own product of 123.280. The old
correction row read -2.1 ppm, which is the CS tower resummed with the Gram
factor kappa set to 1 -- no Gram correction at all -- at the MUON pin
(-2.128 ppm).

## Scope: three live sites refreshed, four historical records left alone

The distinction the owner drew is exactly the one applied. 2022 is now the
current value everywhere it is quoted as current; 2018 survives only where it
is the VINTAGE of a superseded figure, inside notes that already say so:

  refreshed   observations/fine-structure-observation-table1-data.md  (this bean)
  refreshed   observations/fine-structure-data.md          (2022 added as current)
  refreshed   observations/substrate-consistency-window-table1-data.md (label)
  refreshed   observations/substrate-consistency-window-table2-data.md (alpha row)

  kept        em-coupling-chern-simons.md x2   "Superseded figures, recorded..."
  kept        em-coupling-projection-table1-data.md  "Superseded values, recorded..."
  kept        alpha-em-derivation-open-problems.md   "Superseded figures, recorded..."

## Measured, so the label change is not mistaken for a number change

The inverted q is vintage-independent. Solving the bare form for each central
value gives 1.11023043771 (2018) and 1.11023043782 (2022) -- a shift of
1.1e-10, six orders of magnitude below the +/-0.00002 quoted in the block. The
substrate-consistency window therefore changed its SOURCE LABEL and nothing
else, and the note in the block says so.

## Epistemic status unchanged

Only the bare row is derived. The Chern-Simons correction stays conjectural
with kappa an unproved Lean `sorry`; exact closure at this pin needs
kappa = 1.9153 against Witten's 1.7216 (11.2%). The refreshed table states
this rather than presenting 137.036 as a result.
