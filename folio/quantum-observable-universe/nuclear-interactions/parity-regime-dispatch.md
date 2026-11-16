The [sign identity](#thm:parity-regime-selection) is used to select one of three Q-value formulas. The selection is a per-case prescription; none of the three formulas is derived.

1. **Odd $A$** ($A \geq 3$): the factorization $a^Z b^{N-1}(a-b)$ is positive, and the prescription is $Q = |S \cdot \Delta| \times m_e$.
2. **Even $A$**: the factorization is negative. The prescription restricts the sum to Frobenius-positive configurations ([confinement LP](#prop:confinement-lp)) and takes $Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e$.
3. **$A = 1$** (neutron decay): there are no spectators, and the prescription adds the positron correction, $Q = (S\Delta + 1) \times m_e$.

The comparison of $a$ against $b$ is fixed: $a - b = (q^2-1)\bigl(3(q^2+1)^2 - 2q^2\bigr)/(4q^3) > 0$ for $q > 1$, so $|b| > |a|$.

## Empirical comparison

| Decay | $A$ | Regime | $Q_{\mathrm{calc}}$ (MeV) | $Q_{\mathrm{exp}}$ (MeV) | Error |
|-------|-----|--------|---------------------------|--------------------------|-------|
| $n \to p$ | 1 (odd) | $(S\Delta+1) \times m_e$ | $\approx 0.7816$ | $0.7823$ | $-0.10\%$ |
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ | 3 (odd) | $\|S\Delta\| \times m_e$ | $\approx 0.0179$ | $0.0186$ | $-3.64\%$ |
| ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ | 6 (even) | $(\Sigma_{\mathrm{FP}}+1) \times m_e$ | $\approx 3.637$ | $3.508$ | $+3.68\%$ |
