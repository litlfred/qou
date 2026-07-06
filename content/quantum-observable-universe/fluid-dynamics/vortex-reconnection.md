When two vortex filaments approach, the divisor $\{\psi = 0\}$ undergoes surgery. The quantum pressure $Q_q$ regularises the classical reconnection singularity. Let $D = \sum_i n_i\varrho_i$ be the effective divisor encoding the vortex configuration, where $\varrho_i$ are the filament components and $n_i \in \frac{1}{2}\mathbb{Z}$ are their intensity levels. Reconnection acts as a birational transformation of the divisor:

$$
  D =  \cdots + \varrho_i + \varrho_j + \cdots
  \quad\xrightarrow{\text{surgery}}\quad
  D' =  \cdots + \varrho_i' + \varrho_j' + \cdots,
$$

where $\varrho_i'$ and $\varrho_j'$ are the reconnected filaments. The surgery preserves:

- **Total circulation**: $\Gamma_i^{(q)} + \Gamma_j^{(q)} = \Gamma_{i'}^{(q)} + \Gamma_{j'}^{(q)}$ (conservation of the $\mathrm{SU}_q(2)$ Casimir).
- **Categorical helicity**: $\mathcal{H}_q[D] = \mathcal{H}_q[D']$ ([helicity conservation](#prop:helicity-conservation)), though writhe and twist may redistribute.
- **Total homology class**: $[D] = [D']$ in $H_1(\mathcal{S})$.

**Three types of divisor surgery.**

| Surgery type | Divisor operation | Physical process | Hecke eigenvalue |
|---|---|---|---|
| **Pass-through** | $\varrho_i, \varrho_j \to \varrho_i, \varrho_j$ | Elastic scattering | $q$ (symmetric) |
| **Strand exchange** | $\varrho_i, \varrho_j \to \varrho_i', \varrho_j'$ | Reconnection | $-q^{-1}$ (antisymmetric) |
| **Annihilation** | $\varrho_i, \bar\varrho_i \to E_0$ | Pair annihilation $\to$ exceptional divisor | — |

The first two types correspond to the two eigenvalues of the [Hecke relation](#rem:braid-fluid) $(T - q)(T + q^{-1}) = 0$, confirming the [braid--fluid correspondence](#rem:braid-fluid). The third type (annihilation) occurs when a filament meets its orientation-reversed partner $\bar\varrho_i$. The pair collapses to an exceptional divisor $E_0 \cong \mathbb{CP}^1$. This releases energy $2\mathcal{E}_q[\varrho_i]$ as radiation (Kelvin waves propagating along neighbouring filaments).

**Blowup and pair creation.**
The reverse process — blowup of an exceptional divisor — constitutes pair creation. A sufficiently energetic Kelvin wave on a filament $\varrho_k$ concentrates energy at a point. When the local energy density exceeds $2\mathcal{E}_q[\varrho_{\min}]$ (twice the [geodesic vortex](#rem:geodesic-vortices) energy of the fundamental mode), the exceptional divisor inflates into a filament--anti-filament pair:

$$
  E_0  \to  \varrho_{\mathrm{new}} + \bar\varrho_{\mathrm{new}}.
$$

The new filaments inherit the minimum intensity level $j = \frac{1}{2}$. This provides the fluid-dynamical realisation of pair production: a photon (Kelvin wave) creates an electron--positron pair (vortex--antivortex pair).

**Selection rules.**
Not all reconnections are allowed. The $\mathrm{SU}_q(2)$ representation theory imposes fusion rules on divisor surgery. The reconnection $\varrho_i + \varrho_j \to \varrho_{i'} + \varrho_{j'}$ is permitted only if the Clebsch--Gordan decomposition

$$
  V_{j_i} \otimes V_{j_j}
  = 
  \bigoplus_{J = |j_i - j_j|}^{j_i + j_j} V_J
$$

contains the representation $V_{j_{i'}} \otimes V_{j_{j'}}$ as a summand. This connects vortex reconnection to the Clebsch--Gordan coefficients of the quantum group.

**Connection to chirality.**
The [trefoil chirality flip](#rem:trefoil-vortex-chirality-flip) identified three routes for chirality reversal. In the divisor language:

1. **Passage through exceptional divisor**: the vortex momentarily collapses to $E_0$ and re-inflates with reversed orientation. This represents a pair annihilation followed by pair creation with opposite chirality.
2. **Complex substrate rotation**: the divisor rotates through a homotopically non-trivial path in the complexified state bundle. This requires no surgery, but the ambient space must be complexified.
3. **Reidemeister reconnection**: a sequence of strand exchanges (Reidemeister moves) changes the knot type. This constitutes a shell transition, not a particle-type change.
