# ρ_F · V_hyp binding-energy gap analysis

**Status.** Tracking audit. **Witness:**
[`rho-f-volume-binding-gap.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/rho-f-volume-binding-gap.witness.json).

**Script.** [`rho_f_volume_binding_gap.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/rho_f_volume_binding_gap.py).

## Why this exists

`atom_mass_additive_baseline.py` reports the per-isotope nuclear
binding energy $\Delta_{\text{binding}}(A, Z)$ as the residual
between the additive constituent baseline
$Z M_p + N M_n + Z M_e$ and AME2020.
[`rem:frobenius-packing-density`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/particle-interactions/frobenius-packing-density.md)
predicts this binding to be the product

$$
  E_{\text{binding}}(K) \;=\; \rho_F(K) \cdot V_{\text{hyp}}(K),
$$

with $\rho_F \in \{m_e,\,2 m_e\}$ from Type-B fold-orbit closure
([`prop:cpt-orbit-closure-density`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/particle-interactions/cpt-orbit-closure-density.md))
and $V_{\text{hyp}}$ the Thurston volume of the atomic-link
complement.

This script inverts the law: given empirical $\Delta_{\text{binding}}$
and SnapPy-known $V_{\text{hyp}}$ for the available link primitives
(figure-eight, three-twist, Borromean), it reports the **required
$\rho_F / m_e$** that each candidate would need.

## Findings

| isotope | A | Δ_binding (MeV) | ρ/m_e via 4_1 | ρ/m_e via 5_2 | ρ/m_e via 6³_2 |
|---------|---|-----------------|---------------|----------------|------------------|
| ⁴He     | 4 |  28.296         |   27.28       |   19.58        |    7.56          |
| ⁷Li     | 7 |  39.244         |   37.83       |   27.16        |   10.48          |
| ⁹Be     | 9 |  58.165         |   56.08       |   40.25        |   15.53          |
| ¹²C     |12 |  92.161         |   88.85       |   63.77        |   24.61          |
| ¹⁶O     |16 | 127.619         |  123.03       |   88.31        |   34.08          |
| ²⁰Ne    |20 | 160.650         |  154.88       |  111.16        |   42.90          |

**Match count within ±10% of $\rho_F \in \{m_e, 2 m_e\}$: 0.**

So no single link primitive reproduces $\Delta_{\text{binding}}$
under a clean $\rho_F \in \{m_e, 2 m_e\}$ assumption.  Two
non-mutually-exclusive interpretations:

1. **Atomic links are composites.** The atomic-link
   $K_{(A, Z)}$ is built from many primitive links (e.g. one
   Borromean per nucleon triple).  Required $V_{\text{hyp}}$ would
   then scale roughly with $A$ or $\binom{A}{2}$.

2. **$\rho_F$ takes a different value at the binding scale.** If
   the QOU formula is exact but $\rho_F$ is parametrised by
   per-nucleon character data rather than a strict $\{m_e, 2 m_e\}$
   dichotomy, the bound state's "effective" $\rho_F$ could land
   anywhere in $[m_e,\,160 m_e]$.

## What's needed to close the gap

1. **Atom→atomic-link map.** A canonical assignment $(A, Z)
   \mapsto K_{(A, Z)}$ recording the JSJ-decomposed link complement
   for each isotope.  This is paper-side content not yet wired
   through `frobenius-packing-density.md`.

2. **SnapPy V_hyp for each $K_{(A, Z)}$.** For the simplest cases
   (Hopf link $\to$ deuteron, Borromean $\to$ ³He, …), the values
   are tractable; heavier nuclei need explicit triangulations.

3. **Refined $\rho_F$ formula.** Either confirm
   $\rho_F \in \{m_e, 2 m_e\}$ exactly (then the entire deviation
   sits in V_hyp), or replace by a parametric form — e.g.
   $\rho_F(K) = \kappa_F(K) \cdot m_e$ with $\kappa_F$ derived
   from the Wedderburn-block populated set.

The witness emitted by this script provides the per-isotope,
per-link-primitive table that any of these resolutions can be
checked against.

## How to update

```bash
cd folio-assistant/computations
python3 atom_mass_additive_baseline.py    # refresh Δ_binding column
python3 rho_f_volume_binding_gap.py        # invert ρ_F · V_hyp
```

The output's `matches_within_10pct` field is the bound for which
isotopes are explained by a single link primitive at canonical
$\rho_F$.  When the atom→link map lands and that field becomes
non-empty for the simplest isotopes, the next step is wiring
predictions back into `codata-reconciliation.witness.json` as
non-anchor rows.
