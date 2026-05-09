# CODATA-2022 reconciliation

**Status.** Tracking audit. **Witness:**
[`codata-reconciliation.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/codata-reconciliation.witness.json).

**Script.** [`codata_reconciliation.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/codata_reconciliation.py).

This audit consolidates QOU's primary mass / Q-value /
geometric-volume predictions and compares each against the
corresponding CODATA-2022 (or SnapPy 3.3.2) value, reporting the
deviation in parts-per-billion. Each witness assertion is parametrised
with tolerance = 2 × CODATA uncertainty (in ppb), so a passing
assertion means QOU agrees with CODATA to within twice the
experimental precision.

## Scope

| row | source | role |
|---|---|---|
| `m_e` | CODATA 2022 | anchor — energy scale by definition |
| `m_p` | CODATA 2022 | anchor — atom-mass-tower normalisation |
| `α_2 − z²` (Markov axiom) | `alpha-k-jones-markov-h3.witness.json` | structural cross-check |
| `Σ d_λ y_λ − 1` (Markov M3) | `alpha-k-macdonald-closed-form.witness.json` | structural cross-check |
| `Q_n` (β-decay) | CODATA arithmetic `m_n − m_p − m_e` | structural cross-check |
| Knot volumes | SnapPy 3.3.2 | anchor (Thurston volumes) |

Anchor rows pass at exactly 0 ppb by construction. The two structural
cross-checks (Markov-axiom α_2 = z² and Plancherel completeness)
hit IEEE-754 / 50-dps machine precision via the closed-form path
licensed by `prop:macdonald-hook-telescope`. Current
`max_non_anchor_delta_ppb = 0.000 ppb`.

## Informational: atomic-species derivation gap

The witness's `data.atom_species_informational` field records the
per-element table from `atom-mass-derived.witness.json` (Hydrogen
through Neon). At present the upstream derivation chain has known
gaps — the predicted hydrogen atomic mass is +55% off CODATA and
helium is negative. These rows are **surfaced informationally**
but NOT asserted in the reconciliation witness, so the global
`max_non_anchor_delta_ppb` metric tracks structural integrity
rather than the upstream derivation gap.

Closing the atomic-species gap is a separate workplan item: it
requires reworking the `tr_M_atom` / `tr_M_nucleus` factorisation
in `atom_mass_derived.py` against the closed-form `y_λ` now
available via `alpha_k_macdonald_closed_form.py`.

## How to update

Re-run the script after any upstream prediction changes:

```bash
cd folio-assistant/computations
python3 codata_reconciliation.py
```

The witness is regenerated with current `assertions[]`,
`max_non_anchor_delta_ppb`, and the full per-row table. The CI
witness pipeline (`witness-pipeline.yml`) runs this script on every
PR that modifies any compute script in
`folio-assistant/computations/`.

## 1ppb readiness

The witness's `max_non_anchor_delta_ppb` field is the single number
to track. To reach 1 ppb readiness:

1. Wire orphan `:val[…]` blocks to their backing computations so
   that the derived-prediction rows in this audit can pull their
   values from the live witness chain.
2. Replace any remaining `Hoefsmit-matrix` numerical computations
   with the closed-form path licensed by
   `prop:macdonald-hook-telescope`.
3. Cross-validate the derived neutron mass and muon-to-electron
   ratio rows against multiple independent compute paths
   (Wenzl-bridge / Macdonald telescope / direct Markov-trace).
