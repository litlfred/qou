When two vortex filaments approach, the divisor $\{\psi = 0\}$ undergoes surgery. In smooth inviscid (Euler) flow, vortex lines are transported by the flow and their link type is fixed, so a change of topology is incompatible with smoothness there. Viscous reconnection carries no such obstruction: there exist smooth solutions of the three-dimensional Navier--Stokes equations in which vortex lines and vortex tubes of arbitrary knot and link type are created and destroyed in arbitrarily short time \cite{enciso2017}. Reconnection by itself is therefore compatible with smooth classical viscous flow, and the role assigned here to the quantum pressure $Q_q$ is to organise the surgery. Let $D = \sum_i n_i\varrho_i$ denote the effective divisor framing the vortex configuration, where $\varrho_i$ represent the filament components and $n_i \in \frac{1}{2}\mathbb{Z}$ identify their intensity levels. Reconnection constitutes a **birational transformation** on the divisor:

$$
  D =  \cdots + \varrho_i + \varrho_j + \cdots
  \quad\xrightarrow{\text{surgery}}\quad
  D' =  \cdots + \varrho_i' + \varrho_j' + \cdots,
$$

where $\varrho_i'$ and $\varrho_j'$ designate the reconnected filaments. The surgery preserves three quantities:

- **Total circulation**: $\Gamma_i^{(q)} + \Gamma_j^{(q)} = \Gamma_{i'}^{(q)} + \Gamma_{j'}^{(q)}$ (enforcing conservation of the $\mathrm{SU}_q(2)$ Casimir).
- **Categorical helicity**: $\mathcal{H}_q[D] = \mathcal{H}_q[D']$ ([helicity conservation](#prop:helicity-conservation)), although writhe and twist are free to redistribute. The redistribution is forced whenever the exchange acts as a crossing change between distinct filaments $a \neq b$ of a pure braid. A crossing change of sign $\epsilon = \pm 1$ moves $\mathrm{lk}(\varrho_a, \varrho_b)$ by exactly $-\epsilon$ and the mutual helicity $\sum_{a \neq b} \mathrm{lk}\,\Gamma_a\Gamma_b$ by exactly $-2\epsilon\,\Gamma_a\Gamma_b$, while the Reidemeister II and III moves leave both unchanged. Conservation of the total therefore requires an equal and opposite change in the writhe-plus-twist term, which is the transfer from linking to coiling observed in reconnecting vortex links \cite{scheeler2014}.
- **Total homology class**: $[D] = [D']$ evaluated in $H_1(\mathcal{S})$.

**Three types of divisor surgery.**

| Surgery type | Divisor operation | Physical process | Hecke eigenvalue |
|---|---|---|---|
| **Pass-through** | $\varrho_i, \varrho_j \to \varrho_i, \varrho_j$ | Elastic scattering | $q$ (symmetric) |
| **Strand exchange** | $\varrho_i, \varrho_j \to \varrho_i', \varrho_j'$ | Reconnection | $-q^{-1}$ (antisymmetric) |
| **Annihilation** | $\varrho_i, \bar\varrho_i \to E_0$ | Pair annihilation $\to$ exceptional divisor | — |

The first two classes map exactly to the two eigenvalues of the [Hecke relation](#rem:braid-fluid) $(T - q)(T + q^{-1}) = 0$, explicitly verifying the [braid--fluid correspondence](#rem:braid-fluid). The third class, annihilation, triggers when a filament encounters its orientation-reversed partner $\bar\varrho_i$. The pair physically collapses into an exceptional divisor $E_0 \cong \mathbb{CP}^1$, jettisoning energy $2\mathcal{E}_q[\varrho_i]$ as Kelvin-wave radiation along adjacent filaments.

**Blowup and pair creation.**
The inverse mechanism — the **blowup** of an exceptional divisor — constitutes pair creation. When an intense Kelvin wave on a filament $\varrho_k$ concentrates energy locally, and that density breaches $2\mathcal{E}_q[\varrho_{\min}]$ (twice the fundamental [geodesic vortex](#rem:geodesic-vortices) energy), the exceptional divisor forcefully inflates into a filament--anti-filament pair:

$$
  E_0  \to  \varrho_{\mathrm{new}} + \bar\varrho_{\mathrm{new}}.
$$

These newly spawned filaments adopt the absolute minimum intensity level $j = \frac{1}{2}$. This serves as the precise fluid-dynamical mapping of pair production: a photon (the Kelvin wave) generates an electron--positron pair (the vortex--antivortex pair).

**Selection rules.**
Reconnections are strictly filtered. The $\mathrm{SU}_q(2)$ representation theory issues rigid **fusion rules** controlling divisor surgery. The specific reconnection $\varrho_i + \varrho_j \to \varrho_{i'} + \varrho_{j'}$ proceeds if and only if the Clebsch--Gordan decomposition

$$
  V_{j_i} \otimes V_{j_j}
  = 
  \bigoplus_{J = |j_i - j_j|}^{j_i + j_j} V_J
$$

incorporates the target representation $V_{j_{i'}} \otimes V_{j_{j'}}$ as a viable summand. This binds vortex reconnection entirely to the structural Clebsch--Gordan coefficients of the quantum group.

**Connection to chirality.**
The [trefoil chirality flip](#rem:trefoil-vortex-chirality-flip) defines three avenues for chirality reversal. Translated to divisor terms:

1. **Passage through exceptional divisor**: The vortex collapses briefly to $E_0$ and re-inflates bearing reversed orientation. This is effectively pair annihilation paired directly with opposite-chirality pair creation.
2. **Complex aether rotation**: The divisor sweeps through a homotopically non-trivial path mapped inside the complexified state bundle. No surgery occurs, but the ambient manifold must accommodate complexification.
3. **Reidemeister reconnection**: A structural series of strand exchanges (Reidemeister moves) explicitly alters the core knot type. This denotes a shell transition rather than a modification of particle identity.
