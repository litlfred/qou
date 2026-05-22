**Example.**
Hydrogen $\mathcal{A}(1,0)$ derived from $3 \times \gamma\gamma$
pair production.

## Derivation chain

$$
  3(\gamma\gamma)
  \xrightarrow{\text{pair prod.}}
  (\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3)
  + (\bar{\mathfrak{u}}_1, \bar{\mathfrak{u}}_2, \bar{\mathfrak{d}}_3)
  \xrightarrow{\mathcal{B}_3}
  \xrightarrow{\text{gluon } \sigma_0^2}
  \mathfrak{p}
  \xrightarrow{\sigma_0}
  \mathfrak{p} \oplus T_{2,3}
  = \mathcal{A}(1,0)
$$

**Step 1**: Three 4-term $\gamma\gamma$ collisions produce three
quark--antiquark pairs
([4-term pair nucleon](#prop:four-term-pair-nucleon)).

**Step 2**: Three quarks
$(\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3)$ are confined by
$\mathcal{B}_3$
([confinement selection](#prop:confinement-operator-selection)).

**Step 2b**: The LP-derived gluon ($\sigma_0 \to \sigma_0$, two
crossings) stabilises the confined state
([integer LP gluon](#prop:mass-endomorphism-tower)), yielding
the proton NF with $\mathrm{net}(\mathfrak{p}) \approx +0.986$
($11$ total crossings: $6$ B$_{3}$ + $3$ quarks + $2$ gluon).

**Step 3**: The proton is Hopf-linked to the electron (trefoil
$T_{2,3}$) via the electromagnetic crossing $\sigma_0$:

$$
  \mathcal{A}(1,0)
  =
  \mathrm{NF}(\mathfrak{p} \cdot \sigma_0 \cdot e^-)
$$

## Hydrogen NF

$$
  \mathrm{NF}(\mathcal{A}(1,0))
  =
  +0.090\gamma + 1.018\sigma_0 - 0.024\sigma_1
  + 0.213 L_+ + 0.112 L_- + 0.080 e^-.
$$

| Basis | Coefficient | Role |
|:---:|---:|:---|
| $\gamma$ | $+0.090$ | Vacuum energy (positive — bound state) |
| $\sigma_0$ | $+1.018$ | Dominant: proton--electron crossing |
| $\sigma_1$ | $-0.024$ | Small demand (shell structure) |
| $L_+$ | $+0.213$ | Hopf link content |
| $L_-$ | $+0.112$ | Mirror Hopf |
| $e^-$ | $+0.080$ | Electron content (positive — bound) |

$$
  \mathrm{net}(\mathcal{A}(1,0)) \approx +1.489
$$

**Key observation**: the $e^-$ coefficient flips from
$-0.043$ (proton, unbound) to $+0.080$ (hydrogen atom).
The Hopf linking with the electron satisfies the proton's
trefoil demand. The bound atom has $e^- > 0$ — the beta
decay channel is closed.

The only remaining demand is $\sigma_1 = -0.024$, reflecting
the incomplete $1s^1$ shell (hydrogen has one electron, not the
closed-shell pair of helium).

## Mass budget

| Source | Mechanism | Mass |
|:---|:---|---:|
| $\mathrm{Vol}(\mathcal{B}_3) \approx 7.328$ | Borromean volume | $\approx 938$ MeV |
| $\mathrm{Vol}(T_{2,3}) = 0$ | Trefoil (torus knot) | $0$ |
| Vacuum drag | Electron mass | $0.511$ MeV |
| Skein correction | Crossing asymmetry | $\approx 0.3$ MeV |
| Binding | $-13.6$ eV | negligible |
| **Total** | | **$\approx 938.8$ MeV** |

Consistent with
[hydrogen knot structure](#ex:hydrogen-knot-structure).

**Witness**: `four-term-photon-to-atoms.witness.json`.
