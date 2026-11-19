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
| Compounds tested (`lp-confinement-nf-forcing`) | {{ qou.computations.onepb-status-dashboard.data.summary.structural_lp_dual.n_compounds_total }} |
| GB NF maximizer in active set | {{ qou.computations.onepb-status-dashboard.data.summary.structural_lp_dual.n_compounds_total }} / {{ qou.computations.onepb-status-dashboard.data.summary.structural_lp_dual.n_compounds_total }} (`confinement_holds = True`) |
| Max LP duality gap | {{ qou.computations.onepb-status-dashboard.assertions.0.computed | precision: 4 }} (strong duality holds, tolerance `{{ qou.computations.onepb-status-dashboard.assertions.0.tolerance }}`) |
| Active set sizes | [2, 2, 2, 4, 4, 4] |

The active-set membership of the GB NF maximizer for every
tested compound braid is the structural QOU prediction: the
LP-dual selected Wedderburn blocks ARE the blocks the bound state
saturates.  No fitting against AME or any other empirical data.

### Layer 2 — Markov-trace consistency (Hoefsmit / chi-cache vs markov_peel)

| Metric | Value |
|---|---|
| Atoms compared | {{ qou.computations.onepb-status-dashboard.data.summary.markov_trace_consistency.atoms_compared }} (proton, neutron, deuteron, tritium, helium-3, helium-4) |
| `any_diverge` | {{ qou.computations.onepb-status-dashboard.data.summary.markov_trace_consistency.any_diverge }} |
| Max relative Δ (`exact_method_rel_delta`) | {{ qou.computations.onepb-status-dashboard.data.summary.markov_trace_consistency.max_rel_delta | precision: 4 }} (1.208 × 10⁻⁴⁹) |
| `all_within_1ppb` / `all_within_1ppQ` | {{ qou.computations.onepb-status-dashboard.data.summary.markov_trace_consistency.all_within_1ppb }} / {{ qou.computations.onepb-status-dashboard.data.summary.markov_trace_consistency.all_within_1ppQ }} |

### Layer 3 — Structural identities

| Metric | Value | Notes |
|---|---|---|
| `structural_max_non_anchor_delta_ppb` (CODATA reconciliation) | {{ qou.computations.onepb-status-dashboard.data.summary.structural_max_non_anchor_delta_ppb | precision: 5 }} ppb (2.7755 × 10⁻⁸ ppb) | Non-anchor structural identity residual (supersedes legacy 92.79 ppb AME2020 publication-rounding floor on `M(¹H)`) |
| Σ d_λ y_λ − 1 (Plancherel, n = 2..6) | ≤ 5.3 × 10⁻⁵¹ | 60-dps output precision via Macdonald telescope |
| α_2 − z² (Markov axiom at H_3) | ≤ 10⁻⁵⁰ | 70-dps compute / 60-dps output mpmath evaluation |
| Brundan–Kleshchev structural battery | {{ qou.computations.onepb-status-dashboard.data.summary.brundan_kleshchev.passed }} / {{ qou.computations.onepb-status-dashboard.data.summary.brundan_kleshchev.total }} | all 4 tests pass for n = 2..6 |

### Layer 4 — Empirical AME data (informational, NOT a QOU prediction)

| Metric | Value | Notes |
|---|---|---|
| Δ_binding average per nucleon | {{ qou.computations.onepb-status-dashboard.data.summary.ame_empirical_data_informational.avg_binding_per_nucleon_MeV | precision: 5 }} MeV/A | exact rational `{{ qou.computations.onepb-status-dashboard.data.summary.ame_empirical_data_informational.avg_binding_per_nucleon_MeV_exact_rational }}` from AME2020 |
| Δ_binding max | {{ qou.computations.onepb-status-dashboard.data.summary.ame_empirical_data_informational.max_delta_binding_MeV }} MeV | tracked in additive-baseline audit |

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
- The `structural_max_non_anchor_delta_ppb` metric is now `{{ qou.computations.onepb-status-dashboard.data.summary.structural_max_non_anchor_delta_ppb | precision: 5 }} ppb` (`2.7755 × 10⁻⁸ ppb`), well below both `1 ppb` and `1 ppQ` (`10⁻⁶ ppb`). (The legacy `92.79 ppb` figure was the AME2020 3-decimal-place publication rounding on `M(¹H)` at `938.783`, which is an empirical table-rounding artifact rather than a structural identity residual.)

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
