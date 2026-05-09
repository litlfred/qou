# 1ppb readiness dashboard

**Status.** Tracking audit. **Witness:**
[`onepb-status-dashboard.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/onepb-status-dashboard.witness.json).

**Script.** [`onepb_status_dashboard.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/onepb_status_dashboard.py).

Single source of truth for the "is QOU at 1ppb?" question.
Aggregates the headline metric from each contributing audit and
exposes one number, `max_non_anchor_delta_ppb`, to be tracked by
release gates.

## Current state (post PR #577)

| Metric | Value | Notes |
|---|---|---|
| `max_non_anchor_delta_ppb` (CODATA reconciliation) | **92.79 ppb** | AME2020 publication-rounding floor on `M(¹H)` |
| Σ d_λ y_λ − 1 (Plancherel, n = 2..6) | ≤ 5.3 × 10⁻⁵¹ | machine precision via Macdonald telescope |
| α_2 − z² (Markov axiom at H_3) | ≈ 5.6 × 10⁻¹⁷ | IEEE 754 cumulative |
| Brundan–Kleshchev structural battery | 20 / 20 | all 4 tests pass for n = 2..6 |
| Δ_binding average per nucleon | 7.224 MeV/A | within 4% of empirical SEMF |
| Δ_binding max (²⁰Ne) | 160.65 MeV | tracked in additive-baseline audit |

## Sub-witnesses aggregated

1. [`codata-reconciliation`](codata-reconciliation.md) — primary
   CODATA / SnapPy comparison (anchor + structural + derived rows).
2. [`atom-mass-additive-baseline`](atom-mass-additive-baseline.md)
   — additive constituent baseline + Δ_binding column.
3. [`rho-f-volume-binding-gap`](rho-f-volume-binding-gap.md) —
   ρ_F · V_hyp inversion analysis (no single primitive yet
   matches; atom→link map TODO).
4. [`brundan-kleshchev-audit`](brundan-kleshchev-audit.md) —
   structural-evidence dossier for the BK isomorphism.
5. `alpha-k-macdonald-closed-form.witness.json` — closed-form
   α_k via Macdonald hook telescope.
6. `y-lambda-macdonald-telescope.witness.json` — closed-form
   y_λ at all n via principal-specialisation Frobenius identity.
7. `demazure-markov-trace.witness.json` — Demazure-fiber
   functional T^Dem(λ; w) tabulated for n = 2, 3.

## Open path to 1ppb

The headline 92.79 ppb on `M(¹H)` is the AME2020 publication
rounding (3 decimal places at 938.783); the constituent baseline
itself is 938.78308716 MeV which is exact to ~14 significant
figures. To go below 100 ppb on this row, use a higher-precision
AME2020 tabulation (≥ 6 decimal places).

The non-trivial path is the atomic binding-energy column: every
isotope at $A \geq 4$ has an empirical Δ_binding from the additive
baseline, and the QOU ρ_F · V_hyp law should reproduce it. The
ρ_F · V_hyp gap audit shows no single link primitive matches at
canonical $\rho_F \in \{m_e, 2 m_e\}$, so the immediate next step
is the atom→atomic-link map (paper-side content).

## How to update

```bash
cd folio-assistant/computations
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
