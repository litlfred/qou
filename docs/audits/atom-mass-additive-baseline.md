# Additive atomic-mass baseline (informational; replaces a buggy mult chain)

**Status.** Layer-4 informational audit (see
[`onepb-status-dashboard.md`](onepb-status-dashboard.md)).
**Witness:**
[`atom-mass-additive-baseline.witness.json`](https://github.com/litlfred/qou/blob/main/computations/atom-mass-additive-baseline.witness.json).

**Script.** [`atom_mass_additive_baseline.py`](https://github.com/litlfred/qou/blob/main/computations/atom_mass_additive_baseline.py).

## Position in the audit stack

This audit replaces the structurally-wrong multiplicative chain
in `atom_mass_derived.py` with the correct additive constituent
formula.  It is **informational, not a QOU prediction layer** —
QOU's structural predictions live in Layers 1–3 of the
[1ppb dashboard](onepb-status-dashboard.md) (LP dual / GB NF /
Markov-trace consistency / structural identities).  AME atomic
masses are experimental data; they are not a QOU fitting
target.

## Why this exists

The pre-existing `atom_mass_derived.py` uses a *multiplicative*
"$\mathrm{tr}_M(\text{atom NF}) \times E_0$" formula that gives
results structurally far from CODATA — e.g. the predicted
hydrogen atom is +55% high, helium comes out negative — because
atomic mass is *additive* in its constituents, not
multiplicative.

The physical relation is

$$
  M_{\text{atom}}(A, Z)
  \;=\;
  Z \cdot M_p + N \cdot M_n + Z \cdot M_e
    \;-\; E_{\text{binding}}(A, Z),
$$

with $E_{\text{binding}} > 0$ for stable nuclei (~7.5–8 MeV /
nucleon for medium nuclei, peaking near $A \approx 60$). This
script computes the additive constituent baseline and records the
residual

$$
  \Delta_{\text{binding}}(A, Z)
  \;=\;
  \bigl(Z M_p + N M_n + Z M_e\bigr) - M_{\text{AME}}(A, Z),
$$

which **is** the binding energy that the QOU Frobenius-packing
formula
[`rem:frobenius-packing-density`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/particle-interactions/frobenius-packing-density.md)
is expected to reproduce.

## Output

| isotope | constituents (MeV) | AME2020 (MeV) | Δ_binding (MeV) | Δ ppb |
|---------|-------------------:|---------------:|-----------------:|------:|
| ¹H      |   938.783087 |   938.783000 |    +0.000087 |     93 |
| ⁴He     |  3756.697015 |  3728.401000 |   +28.296015 |  7.6e6 |
| ⁷Li     |  6574.610943 |  6535.367000 |   +39.243943 |  6.0e6 |
| ⁹Be     |  8452.959451 |  8394.794000 |   +58.165451 |  6.9e6 |
| ¹¹B     | 10331.307959 | 10255.103000 |   +76.204959 |  7.4e6 |
| ¹²C     | 11270.091046 | 11177.930000 |   +92.161046 |  8.2e6 |
| ¹⁴N     | 13148.439553 | 13043.781000 |  +104.658553 |  8.0e6 |
| ¹⁶O     | 15026.788061 | 14899.169000 |  +127.619061 |  8.6e6 |
| ¹⁹F     | 17844.701989 | 17696.901000 |  +147.800989 |  8.4e6 |
| ²⁰Ne    | 18783.485076 | 18622.835000 |  +160.650076 |  8.6e6 |

Average binding per nucleon (A ≥ 4): **7.224 MeV/A** — this is
within 4% of the empirical SEMF (semi-empirical mass formula)
prediction of ~7.5 MeV/A. The QOU $\rho_F \cdot V_{\text{hyp}}$
law should reproduce this column.

## Status of the QOU side

The Δ_binding column above is empirical AME residual; it is
**not** a QOU prediction target.  QOU's structural prediction is
the LP active set + GB NF data in Layer 1 of the dashboard.

The interpretive question — does the LP-dual shadow-price
machinery `y_λ*` *also* reproduce empirical nuclear binding
through the Frobenius-packing law? — is tracked separately in
[`rho-f-volume-binding-gap.md`](rho-f-volume-binding-gap.md).
That audit is informational, not a 1ppb gate.

Hydrogen passes at <100 ppb (limited by AME2020 publication
rounding to 3 decimal places). The atomic-binding contribution at
$A = 1$ is the 13.6 eV hydrogen ground-state binding,
~10⁻⁵ MeV ≈ 14 ppb — beneath the AME publication floor.

## How to update

```bash
cd computations
python3 atom_mass_additive_baseline.py
```

The witness pipeline runs this script on every PR that modifies
any compute file in `computations/`. The bound
$\sum_A \Delta_{\text{binding}}(A, Z)$ is the single number
to reduce when wiring the QOU binding-energy law into the
reconciliation table.
