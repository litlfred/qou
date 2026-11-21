**Conjecture (charge conjugation as the color-sheet flavor swap; conditional on [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube)).**
*Within the QOU framework, charge conjugation $C$ acts as the **flavor swap on color sheets** that exchanges each quark flavor with its antimatter-conjugate:*

$$
  C \;:\;
  \begin{cases}
    u \;\longleftrightarrow\; \bar u, \\
    d \;\longleftrightarrow\; \bar d,
  \end{cases}
$$

*applied independently to each of the three color sheets of every nucleon-coloured braid strand. The proton flavor triple $(u, u, d)$ maps to $(\bar u, \bar u, \bar d)$ (the antiproton); the neutron flavor triple $(u, d, d)$ maps to $(\bar u, \bar d, \bar d)$ (the antineutron). $C$ is an involution ($C^2 = \mathrm{id}$) and commutes with the color-tube weighted averaging of [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube).*

## Separating $C$ from the CPT composite

The framework historically collapses C, P, T into the single bar-involution [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections](#def:bar-involution) on Hecke generators ($q \mapsto q^{-1}$ together with $\sigma_i \mapsto \sigma_i^{-1}$). That conflation suppresses the **distinct categorical sources** of the three discrete symmetries:

| Symmetry | Categorical source | Acts on |
|----------|--------------------|---------|
| **C** (this conjecture) | flavor swap on color sheets | quark-flavor content of nucleon braid strands |
| **P** | mirror reflection of braid diagram | writhe / signed-crossing classification ([`bar-involution-table3-data`](../stochastic-mechanics/bar-involution-table3-data.md)) |
| **T** | Markov-trace word reversal | trace-cyclicity dual |

The bar-involution $q \mapsto q^{-1}$, $\sigma_i \mapsto \sigma_i^{-1}$ acts as the **composite CPT** in this categorisation, not as C alone. This conjecture locates the C-component on the color sheets, orthogonal to P (braid-diagram mirror) and T (trace reversal).

## The conjectural content

The proposition relies on the color-sheet flavor structure established in [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube). Specifically:

1. **C is well-defined.** The flavor-content map $(F_1, F_2) \mapsto (\bar F_1, \bar F_2)$ commutes with the color-tube weight tensor $W_{c_1 c_2}(F_1, F_2)$—i.e. $W_{c_1 c_2}(\bar F_1, \bar F_2) = W_{c_1 c_2}(F_1, F_2)$ (the weights are flavor-conjugation invariant).
2. **C is an involution.** Each color sheet flips back to its original flavor under two applications.
3. **C commutes with bar-involution on the algebraic side.** This forces $\mathrm{CP} \cdot \mathrm{T}$ and $\mathrm{C} \cdot \mathrm{PT}$ to reduce to the bar-involution identity classified in [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections](../braids-and-knots/bar-involution.md) §Bar-symmetric.

When all three hold, $C$ constitutes the well-defined Z/2 categorical symmetry on the color-sheet flavor data. The CPT composite factors as $\mathrm{CPT} = C \cdot P \cdot T$ in the natural order, as three commuting Z/2 actions on the color-tube structure.

## Structural position

- **GB filtration level.** None: the claim addresses a Z/2 categorical symmetry on color-sheet metadata, not Hecke elements at a particular Coxeter length.
- **Jet order.** $h^0$: the $C$-action is independent of $q$, and the flavor-conjugation map forms a structural Z/2 lifting through the color-tube tensor.
- **Bar-symmetry.** $C$ is bar-symmetric. It preserves $q$ and commutes with $\sigma_i \leftrightarrow \sigma_i^{-1}$, since it acts on color-sheet labels and not on Hecke generators. It is $C$ composed with $PT$ that yields the bar-involution; $C$ itself is bar-trivial in [`bar-involution-table4-data`](../stochastic-mechanics/bar-involution-table4-data.md).

## The hypothesis in summary

The conjecture asserts a map $C$ on color-sheet flavors with $C^2 = \mathrm{id}$, with $W_{c_1 c_2}(C F_1, C F_2) = W_{c_1 c_2}(F_1, F_2)$ for all nucleon flavor contents $F_1, F_2$ and color sheets $c_1, c_2$, and with the bar-involution factoring as $C \circ P \circ T$, where $P$ is the braid-diagram mirror and $T$ is the Markov-trace word reversal. These data are supplied by the color-tube weighting once [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube) is established.

## Consumers / downstream

- The matter/antimatter sheet structure on Bring's quintic surface ([Color tube fibers](color-tube-fibers.md)) acquires a natural C-action that descends to the SO(3) fiber.

## Numerical cross-check and open content

At the 50-digit substrate $q_0$, the flavor-conjugation involution leaves the color-tube weighted inter-nucleon Hecke generator invariant for all sixteen nucleon pairs drawn from $\{p, n, \bar p, \bar n\}$, in two two-dimensional Hecke representations (the diagonal eigenvalue model and a non-diagonal conjugate of it), with the $\epsilon$ and $W$ tables invariant cell by cell. The check runs the uniform projection $W = 1/9$—the only realisation of $W$ available while its closed form remains open—so it corroborates the derivation rather than testing the conjectural Bring-derived $W$. No parameter is fitted.

The statement is conjectural only for as long as [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube) and the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber-action conjecture remain open; establishing both makes it unconditional.

## Cross-references

- Upstream class: [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube)
- [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections](../braids-and-knots/bar-involution.md)—the bar-involution = CPT composite identification at the algebraic level
