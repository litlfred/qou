# CODATA-2022 reconciliation

**Status.** Tracking audit. **Witness:**
[`codata-reconciliation.witness.json`](https://github.com/litlfred/qou/blob/main/computations/codata-reconciliation.witness.json).

**Script.** [`codata_reconciliation.py`](https://github.com/litlfred/qou/blob/main/computations/codata_reconciliation.py).

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
| `M(¹H)` | `atom-mass-additive-baseline.witness.json` | derived — 92.79 ppb (AME publication floor) |
| `α_2 − z²` (Markov axiom) | `alpha-k-jones-markov-h3.witness.json` | structural cross-check |
| `Σ d_λ y_λ − 1` (Markov M3) | `alpha-k-macdonald-closed-form.witness.json` | structural cross-check |
| `Q_n` (β-decay) | CODATA arithmetic `m_n − m_p − m_e` | structural cross-check |
| Knot volumes | SnapPy 3.3.2 | anchor (Thurston volumes) |

Anchor rows pass at exactly 0 ppb by construction. The two
structural cross-checks (Markov-axiom α_2 = z² and Plancherel
completeness) hit IEEE-754 / 50-dps machine precision via the
closed-form path licensed by `prop:macdonald-hook-telescope`.
Current `max_non_anchor_delta_ppb ≈ 92.79 ppb`, driven entirely
by the `M(¹H)` row's AME publication-rounding floor (3 decimal
places at 938.783 MeV); the structural cross-checks themselves
hit ≤ 10⁻¹⁷.

## Atomic-species rows: replaced multiplicative chain (informational)

The pre-existing `atom_mass_derived.py` chain used a
multiplicative
$\mathrm{tr}_M(\text{atom NF}) \times E_0$ formula that is
structurally wrong (gives +55% for hydrogen, negative for
helium) because atomic mass is **additive** in its constituents,
not multiplicative. This PR adds
[`atom_mass_additive_baseline.py`](https://github.com/litlfred/qou/blob/main/computations/atom_mass_additive_baseline.py)
with the correct constituent formula
$Z M_p + N M_n + Z M_e$.  Hydrogen passes at 92.79 ppb (limited
by AME2020's 3-decimal-place publication rounding to 938.783).

**Note:** AME atomic masses are experimental data, not a QOU
prediction target.  QOU's structural prediction lives in the
LP-dual / GB-NF / Markov-trace layers of the
[1ppb dashboard](onepb-status-dashboard.md).  The atomic-mass
row above is included as a sanity-check for the constituent-sum
arithmetic, not as evidence about whether QOU is "right."

The `Δ_binding` column for $A \geq 4$ in
[`atom-mass-additive-baseline.md`](atom-mass-additive-baseline.md)
records empirical nuclear binding — average 7.224 MeV/nucleon,
within 4% of empirical SEMF.  Whether the QOU LP active set +
Frobenius-packing law also reproduces this column is the
**interpretive** question tracked by
[`rho-f-volume-binding-gap.md`](rho-f-volume-binding-gap.md);
it is not a 1ppb gate.

## How to update

Re-run the script after any upstream prediction changes:

```bash
cd computations
python3 codata_reconciliation.py
```

The witness is regenerated with current `assertions[]`,
`max_non_anchor_delta_ppb`, and the full per-row table. The CI
witness pipeline (`witness-pipeline.yml`) runs this script on every
PR that modifies any compute script in
`computations/`.

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
