**Conjecture (D6 charge-conjugation closure, conditional on [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube)).**
*Within the QOU framework, charge conjugation $C$ acts as the **flavor swap on color sheets** that exchanges each quark flavor with its antimatter-conjugate:*

$$
  C \;:\;
  \begin{cases}
    u \;\longleftrightarrow\; \bar u, \\
    d \;\longleftrightarrow\; \bar d,
  \end{cases}
$$

*applied independently to each of the three color sheets of every nucleon-coloured braid strand. The proton flavor triple $(u, u, d)$ maps to $(\bar u, \bar u, \bar d)$ (the antiproton); the neutron flavor triple $(u, d, d)$ maps to $(\bar u, \bar d, \bar d)$ (the antineutron). $C$ is an involution ($C^2 = \mathrm{id}$) and commutes with the color-tube weighted averaging of [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube).*

## Disentanglement of D6 from CPT

[`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) formalises the **composite** CPT action. The framework historically collapses C, P, T into the single bar-involution [`def:bar-involution`](#def:bar-involution) on Hecke generators ($q \mapsto q^{-1}$ together with $\sigma_i \mapsto \sigma_i^{-1}$). That conflation suppresses the **distinct categorical sources** of the three discrete symmetries:

| Symmetry | Categorical source | Acts on |
|----------|--------------------|---------|
| **C** (this conjecture) | flavor swap on color sheets | quark-flavor content of nucleon braid strands |
| **P** | mirror reflection of braid diagram | writhe / signed-crossing classification ([`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)) |
| **T** | Markov-trace word reversal | trace-cyclicity dual |

The bar-involution $q \mapsto q^{-1}$, $\sigma_i \mapsto \sigma_i^{-1}$ acts as the **composite CPT** in this categorisation, not as C alone. This conjecture locates the C-component on the color sheets—orthogonal to P (braid-diagram mirror) and T (trace reversal).

## The conjectural content

The proposition relies on the color-sheet flavor structure established in [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube). Specifically:

1. **C is well-defined.** The flavor-content map $(F_1, F_2) \mapsto (\bar F_1, \bar F_2)$ commutes with the color-tube weight tensor $W_{c_1 c_2}(F_1, F_2)$—i.e. $W_{c_1 c_2}(\bar F_1, \bar F_2) = W_{c_1 c_2}(F_1, F_2)$ (the weights are flavor-conjugation invariant).
2. **C is an involution.** Each color sheet flips back to its original flavor under two applications.
3. **C commutes with bar-involution on the algebraic side.** This forces $\mathrm{CP} \cdot \mathrm{T}$ and $\mathrm{C} \cdot \mathrm{PT}$ to reduce to the bar-involution identity classified in [`bar-involution.md`](bar-involution.md) §Bar-symmetric.

When all three hold, $C$ constitutes the well-defined Z/2 categorical symmetry on the color-sheet flavor data. The CPT composite of [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) factors as $\mathrm{CPT} = C \cdot P \cdot T$ in the natural order—three commuting Z/2 actions on the color-tube structure.
