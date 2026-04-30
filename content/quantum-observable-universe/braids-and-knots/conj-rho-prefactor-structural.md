The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ in the mass formula

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot M(\mathfrak{H})\big|_{q = q_0}
$$

is currently determined case-by-case as a numerical by-product of
the Wedderburn SDP search.  This conjecture proposes a structural rule
for $\rho$ in terms of the categorical data of $\mathfrak{H}$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom with confinement level
$\ell$, strand count $n_0$, and canonical Hecke element $T_w \in H_{n_0}(q)$.
The SDP multiplicity is:*

$$
  \rho(\mathfrak{H})
  \;=\;
  \dim_q\!\bigl(\lambda^*(T_w)\bigr),
$$

*where $\lambda^*(T_w)$ is the dominant Young diagram in the
Wedderburn decomposition of $T_w$: the partition $\lambda \vdash n_0$
maximizing $|y_\lambda(q_0) \chi_\lambda(T_w)|$.*

*Equivalently, $\rho = \dim_q(\lambda^*) = [\ell(\lambda^*)]_q$ where
$\ell(\lambda^*)$ is the number of cells in the dominant summand.*

## Evidence

| Particle | Dominant $\lambda^*$ | $\dim_q(\lambda^*)$ | Observed $\rho$ |
|----------|---------------------|---------------------|-----------------|
| Proton/neutron ($B_3$) | $(2,1)$ | $[2]_q \approx 2.21$ → rounds to $1$? | $1$ |
| Deuterium ($6_2$, $H_6$) | $(3,2,1)$ | $[5]_q/(...)$ | $1$ |
| Tritium ($8_{11}$, $H_6$) | $(3,3)$ | $[2]_q \approx 2.21$ → $\rho = 2$? | $2$ |
| $^3$He ($L_{6a4}$, $H_6$) | $(3,3)$ | $[2]_q \approx 2.21$ → $\rho = 2$? | $2$ |

The pattern is suggestive but the precise rule needs verification
against the full SDP witness data.

## Proof obligations

1. Show that for proton/neutron the dominant Wedderburn summand is
   $\lambda^* = (2,1)$ (the standard 2-dimensional $H_3(q)$ irrep).
2. Show that the multiplicity formula $\rho = \dim_q(\lambda^*)$ —
   or a slight modification accounting for integer rounding — gives
   the correct value for all atoms in the registry.
3. Provide a categorical interpretation: $\rho$ counts the number of
   orthogonal copies of the dominant irrep that fit inside the
   confinement-SDP solution space.

## Relationship to GAP-A-4

This conjecture directly addresses GAP-A-4 of the
[derivation audit report](#prose:derivation-audit-report).
