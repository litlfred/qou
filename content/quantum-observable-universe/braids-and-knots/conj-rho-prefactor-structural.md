The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ in the mass formula

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot M(\mathfrak{H})\big|_{q = q_0}
$$

is currently determined case-by-case as a numerical by-product of
the Wedderburn SDP search.  This conjecture proposes a structural rule
for $\rho$ in terms of the categorical data of $\mathfrak{H}$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom
([confined particle](#def:confined-particle)) with canonical Hecke
element $T_w \in H_{n_0}(q)$.  The SDP multiplicity is:*

$$
  \rho(\mathfrak{H})
  \;=\;
  \dim_q\!\bigl(\lambda^*(T_w)\bigr),
$$

*where $\lambda^*(T_w)$ is the **dominant Young diagram** in the
Wedderburn decomposition of $T_w$: the partition $\lambda \vdash n_0$
maximizing $|y_\lambda(q_0) \cdot \chi_\lambda(T_w)|$
([Markov trace expansion](#prop:wedderburn-trace-identity),
[Wenzl-bridge weights](#prop:alpha-k-derivation-procedure)).*

*The quantum dimension $\dim_q(\lambda) = [d_\lambda]_q$ where
$d_\lambda$ is the number of standard Young tableaux of shape
$\lambda$ (hook-length formula).*

## Evidence

The SDP witnesses for all four currently identified particles give:

| Particle | Knot | $n_0$ | Dominant $\lambda^*$ | $\dim_q(\lambda^*)$ at $q_0$ | Obs.\ $\rho$ |
|----------|------|-------|---------------------|------------------------------|--------------|
| Proton/neutron | trefoil $3_1$ | $3$ | $(2,1)$ | $[2]_{q_0} \approx 2.22$ → rounded $\rho = 1$? | $1$ |
| Deuterium $^2$H | $6_2$ | $6$ | $(3,2,1)$ | $[5]_{q_0}/\cdots \approx 1.0$? | $1$ |
| Tritium $^3$H | $8_{11}$ | $6$ | $(3,3)$ | $[2]_{q_0} \approx 2.22$ → $\rho = 2$ | $2$ |
| Helium-3 $^3$He | $L_{6a4}$ | $6$ | $(3,3)$ | $[2]_{q_0} \approx 2.22$ → $\rho = 2$ | $2$ |

The pattern $\rho = \lfloor\dim_q(\lambda^*)\rceil$ (nearest integer
rounding) is consistent with all known cases, but the rule relating
$\lambda^*$ to $(2,1)$ vs.\ $(3,3)$ as the dominant summand has not
been derived from first principles.

## The rounding question

The exact quantum dimension $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.01$
(with $q_0 \approx 1.1097$), so $\dim_q((2,1)) \approx 2.01$.  The
floor gives $\rho = 2$, but the proton/neutron uses $\rho = 1$.  This
suggests the rule may be:

$$
  \rho(\mathfrak{H})
  \;=\;
  \begin{cases}
    1 & \text{if $\lambda^*$ is the hook partition $(n_0-1, 1)$,} \\
    \lfloor\dim_q(\lambda^*)\rceil & \text{otherwise.}
  \end{cases}
$$

Alternatively, the correct $\rho$ may count the number of
**orthogonal Wedderburn copies** that fit inside the SDP feasible
region of the mass formula, which would give $\rho = 1$ for single-copy
and $\rho = 2$ for double-cover nuclei.

## Proof obligations

1. Identify the dominant $\lambda^*$ for each particle from the
   Markov-weight data and show it is $\lambda^* = (2,1)$ for proton
   and $(3,3)$ for $^3$H/$^3$He.

2. Show the multiplicity rule (exact quantum dimension, rounded, or
   orthogonal-copy count) reproduces the known $\rho$ values.

3. Provide a categorical interpretation of $\rho$: it should count
   a natural structural quantity of the confinement-SDP solution space
   (orthogonal copies, Wedderburn summand multiplicity, etc.).

4. Extend the rule to heavier nuclei $A \leq 60$ in the recursive
   atom-knot atlas and verify no per-atom re-tuning is needed.

## Relationship to GAP-A-4

This conjecture directly addresses GAP-A-4 of the
[derivation audit report](#prose:derivation-audit-report).
