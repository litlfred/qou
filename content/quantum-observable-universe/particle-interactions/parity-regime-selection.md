The **parity of the mass number** $A$ determines which
computational regime applies to the Q-value.  This is not a
fitting parameter — it follows from the fermionic sign of
the spectator factor.

## Statement

**Theorem.**
*For all $q > 1$:*

$$
  \operatorname{sign}(a^Z \cdot b^{N-1}) = (-1)^{A-1}
$$

*The Q-value regimes are:*

1. **Odd $A$** ($A \geq 3$): the factorization
   $a^Z b^{N-1}(a-b)$ is positive, and

   $$
     Q = |S \cdot \Delta| \times m_e
   $$

   where $S = a^Z b^{N-1}$ and $\Delta = a - b$.

2. **Even $A$**: the factorization is negative.  The
   [Frobenius positivity filter](#prop:frobenius-positivity-filter)
   restricts the sum to physically admissible configurations, and

   $$
     Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e
   $$

   where $\Sigma_{\mathrm{FP}}$ is the sum over
   Frobenius-positive configs and $+1$ is the
   [positron correction](#prop:positron-correction).

3. **$A = 1$** (neutron decay): no spectators.  The positron
   correction is added explicitly:

   $$
     Q = (S\Delta + 1) \times m_e
   $$

## Numerical verification

| Decay | $A$ | Regime | $Q_{\mathrm{calc}}$ (MeV) | $Q_{\mathrm{exp}}$ (MeV) | Error |
|-------|-----|--------|---------------------------|--------------------------|-------|
| $n \to p$ | 1 (odd) | $(S\Delta+1) \times m_e$ | $\approx 0.7816$ | $0.7823$ | $-0.10\%$ |
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ | 3 (odd) | $\|S\Delta\| \times m_e$ | $\approx 0.0179$ | $0.0186$ | $-3.64\%$ |
| ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ | 6 (even) | $(\Sigma_{\mathrm{FP}}+1) \times m_e$ | $\approx 3.637$ | $3.508$ | $+3.68\%$ |
