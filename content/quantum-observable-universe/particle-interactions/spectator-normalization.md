*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The **spectator normalization** captures the contribution of
unchanged nucleons to the Q-value character sum.  In a beta
decay ${}^A_Z X \to {}^A_{Z+1} Y + e^- + \bar\nu$, only one
neutron converts to a proton; the remaining $Z$ protons and
$N - 1$ neutrons are spectators.

## Definition

The spectator factor is:

$$
  S(Z, N-1) = a^{Z} \cdot b^{N-1}
$$

where $a$ and $b$ are the **channel sums** of the per-nucleon
Garside factors
([per-nucleon decomposition](#def:per-nucleon-channel-decomposition)):

$$
  a = \sum_{c} G_P(c) = -\frac{h}{2},
  \qquad
  b = \sum_{c} G_N(c)
    = -\frac{3(q^2-1)(q^2+1)^2}{4q^3}
$$

with $h = q - q^{-1}$.

## Fermionic character

Both $a < 0$ and $b < 0$ for all $q > 1$.  The negativity
reflects the **fermionic character** of the nucleon: each
spectator contributes a sign flip to the character sum.
The sign of the full spectator product is:

$$
  \operatorname{sign}(a^Z \cdot b^{N-1})
  = (-1)^{Z} \cdot (-1)^{N-1}
  = (-1)^{A-1}
$$

This sign determines the
[parity regime](#thm:parity-regime-selection) for the Q-value.
