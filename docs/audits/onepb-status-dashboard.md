# 1ppb readiness dashboard

**Status.** Tracking audit. **Witness:**
[`onepb-status-dashboard.witness.json`](https://github.com/litlfred/qou/blob/main/computations/onepb-status-dashboard.witness.json).

**Script.** [`onepb_status_dashboard.py`](https://github.com/litlfred/qou/blob/main/computations/onepb_status_dashboard.py).

Single source of truth for the "is QOU at 1ppb?" question.

QOU prediction is **structural**, not fitted against CODATA
atomic-mass tables.  The dashboard reflects four layers, with
the first two carrying the actual prediction:

1. **LP dual / GB NF** — operator-selection LP dual variables
   (`y₀*`, `y_λ*`, active set) and GB NF coincidence with the
   active-set maximizer.  This IS the QOU prediction layer.
2. **Markov-trace consistency** — Hoefsmit-matrix vs `markov_peel`
   recursive-ascent cross-check at 1 ppb relative tolerance.
3. **Structural identities** — Plancherel completeness, BK
   structural battery, Markov axioms, anchor scales.
4. **Empirical AME data (informational)** — atomic masses are
   experimental data, **not** a QOU prediction target.  QOU does
   not curve-fit against atomic-mass tables.

## Current state (post PR #577)

### Layer 1 — LP dual / GB NF (QOU's structural prediction)

| Metric | Value |
|---|---|
| Compounds tested (`lp-confinement-nf-forcing`) | 6 |
| GB NF maximizer in active set | 6 / 6 |
| Max LP duality gap | 0 (strong duality holds) |
| Active set sizes | [2, 2, 2, 4, 4, 4] |

The active-set membership of the GB NF maximizer for every
tested compound braid is the structural QOU prediction: the
LP-dual selected Wedderburn blocks ARE the blocks the bound state
saturates.  No fitting against AME or any other empirical data.

### Layer 2 — Markov-trace consistency (Hoefsmit vs markov_peel)

| Metric | Value |
|---|---|
| Atoms compared | 5 (deuteron, helium-3, neutron, proton, tritium) |
| `any_diverge` | False |
| Max relative Δ | 2.94 × 10⁻¹⁵ |
| `all_within_1ppb` | True |

### Layer 3 — Structural identities

| Metric | Value | Notes |
|---|---|---|
| `max_non_anchor_delta_ppb` (CODATA reconciliation) | 92.79 ppb | AME2020 publication-rounding floor on `M(¹H)` |
| Σ d_λ y_λ − 1 (Plancherel, n = 2..6) | ≤ 5.3 × 10⁻⁵¹ | machine precision via Macdonald telescope |
| α_2 − z² (Markov axiom at H_3) | ≈ 5.6 × 10⁻¹⁷ | IEEE 754 cumulative |
| Brundan–Kleshchev structural battery | 20 / 20 | all 4 tests pass for n = 2..6 |

### Layer 4 — Empirical AME data (informational, NOT a QOU prediction)

| Metric | Value | Notes |
|---|---|---|
| Δ_binding average per nucleon | 7.224 MeV/A | within 4% of empirical SEMF |
| Δ_binding max (²⁰Ne) | 160.65 MeV | tracked in additive-baseline audit |

Atomic masses come from AME2020, not from QOU.  Their inclusion
is sanity-check only.  Closing the gap between QOU's LP dual
shadow prices and the per-isotope AME Δ_binding column would
constitute a separate, much heavier *interpretive* result —
the LP active set + GB NF data is the prediction proper.

## Sub-witnesses aggregated

1. [`codata-reconciliation`](codata-reconciliation.md) — primary
   CODATA / SnapPy comparison (anchor + structural + derived rows).
2. [`atom-mass-additive-baseline`](atom-mass-additive-baseline.md)
   — additive constituent baseline + Δ_binding column.
3. [`rho-f-volume-binding-gap`](rho-f-volume-binding-gap.md) —
   ρ_F · V_hyp inversion analysis (no single primitive matches
   at canonical ρ_F; atom→atomic-link map is open).
4. [`brundan-kleshchev-audit`](brundan-kleshchev-audit.md) —
   structural-evidence dossier for the BK isomorphism.
5. `alpha-k-macdonald-closed-form.witness.json` — closed-form
   α_k via Macdonald hook telescope.
6. `y-lambda-macdonald-telescope.witness.json` — closed-form
   y_λ at all n via principal-specialisation Frobenius identity.
7. `demazure-markov-trace.witness.json` — Demazure-fiber
   functional T^Dem(λ; w) tabulated for n = 2, 3.

## Open paths

**Structural side (Layers 1–2):**
- All currently-tested compounds and atoms pass at machine
  precision / strong duality / ppb. To extend coverage, add more
  compound braids to `lp-confinement-nf-forcing.py`'s test list
  and more atoms to `cross-check-trM-1ppb.py`.

**Identity side (Layer 3):**
- The 92.79 ppb on `M(¹H)` is the AME2020 publication rounding
  (3 decimal places at 938.783); constituent sum is 938.78308716
  to ~14 sig figs. Going below 100 ppb here just requires a
  higher-precision AME2020 tabulation (≥ 6 dp).

**Empirical-data side (Layer 4) — NOT a 1ppb gate:**
- The Δ_binding column is experimental data. The LP dual shadow
  prices `y_λ*` are the QOU prediction for which Wedderburn
  blocks the bound state saturates; the AME Δ_binding is
  whatever quantum chromodynamics + electroweak physics happen
  to put there. The interpretive question of whether the LP
  active set predicts the right Wedderburn blocks for nuclear
  binding lives outside the structural-prediction layer.

## How to update

```bash
cd computations
# Refresh sub-witnesses in dependency order:
python3 atom_mass_additive_baseline.py
python3 rho_f_volume_binding_gap.py
python3 alpha_k_macdonald_closed_form.py
python3 brundan_kleshchev_audit.py
python3 y_lambda_macdonald_telescope.py
python3 demazure_markov_trace.py
python3 codata_reconciliation.py
# Aggregate:
python3 onepb_status_dashboard.py
```

The witness pipeline runs all of these on every PR via the
`witness-pipeline.yml` paths filter.
