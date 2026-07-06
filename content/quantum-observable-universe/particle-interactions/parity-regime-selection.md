The **parity of the mass number** $A$ determines which computational regime applies to the Q-value. This emerges not as a fitting parameter, but from the fermionic sign of the spectator factor.

## Statement

**Theorem.**
*For all $q > 1$:*

$$
  \operatorname{sign}(a^Z \cdot b^{N-1}) = (-1)^{A-1}
$$

*The Q-value regimes are:*

1. **Odd $A$** ($A \geq 3$): The factorization $a^Z b^{N-1}(a-b)$ is positive, yielding

   $$
     Q = |S \cdot \Delta| \times m_e
   $$

   *where $S = a^Z b^{N-1}$ and $\Delta = a - b$.*

2. **Even $A$**: The factorization is negative. The [Frobenius positivity filter](#prop:frobenius-positivity-filter) restricts the sum to admissible (non-negative-trace) configurations, yielding

   $$
     Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e
   $$

   *where $\Sigma_{\mathrm{FP}}$ represents the sum over Frobenius-positive configurations and $+1$ introduces the [positron correction](#prop:positron-correction).*

3. **$A = 1$** (neutron decay): There are no spectators. We add the positron correction explicitly:

   $$
     Q = (S\Delta + 1) \times m_e
   $$
