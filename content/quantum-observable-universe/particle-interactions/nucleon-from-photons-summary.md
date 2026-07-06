This is the complete derivation chain from photons to atoms, verifying conservation laws at each step.

## Chain

$$
  \underbrace{3(\gamma\gamma)}_{\text{6 photons}}
  \xrightarrow{\text{pair prod.}}
  \underbrace{3(q\bar{q})}_{\text{3 pairs}}
  \xrightarrow{\text{select}}
  \underbrace{(q_1, q_2, q_3)}_{\text{3 quarks}}
  \xrightarrow{\mathcal{B}_3}
  \underbrace{\mathfrak{N}}_{\text{nucleon}}
  \xrightarrow{\oplus}
  \underbrace{\mathcal{A}}_{\text{atom}}
$$

| Step | Input | Output | $B$ | $L$ | $Q$ |
|:---|:---|:---|:---:|:---:|:---:|
| $\gamma\gamma$ collision | 2 photons | $q\bar{q}$ pair | $0$ | $0$ | $0$ |
| Quark selection | 3 pairs | 3 quarks + 3 antiquarks | $\pm 1$ | $0$ | $\pm 1$ |
| $\mathcal{B}_3$ confinement | 3 quarks | nucleon ($\mathfrak{p}$ or $\mathfrak{n}$) | $+1$ | $0$ | $0,+1$ |
| Hopf link $\oplus e^-$ | nucleon + electron | atom | $+1$ | $+1$ | $0$ |

Baryon number ($B$), lepton number ($L$), and electric charge ($Q$) remain conserved at every step. The antiquarks either annihilate back to photons or form an antinucleon.

## Key results

1. **Confinement is derived**: Minimum action selects $\mathcal{B}_3$ among operators matching the physical nucleon net ([confinement selection](#prop:confinement-operator-selection)).
2. **Beta decay channel**: The $e^- < 0$ coefficient in the confined nucleon normal form defines the categorical beta decay channel. This emerges directly from $\mathcal{B}_3$ confinement rather than being imposed.
3. **Confinement universality**: The nucleon normal form depends solely on $q_0$ and quark flavors, independent of photon polarization. The strong force erases electromagnetic initial conditions.
4. **Shell closure**: Hydrogen carries $\sigma_1 < 0$ demand (open shell). ${}^{3}\mathrm{He}$ achieves zero demand (closed shell). ${}^{4}\mathrm{He}$ yields a lower Markov trace, indicating tighter binding (doubly magic).

**Witness**: `confinement-operator-selection.witness.json`, `four-term-photon-to-atoms.witness.json`.
