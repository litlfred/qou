The [sign identity](#thm:parity-regime-selection) is used to select one of three Q-value formulas. The selection is a per-case prescription; none of the three formulas is derived.

1. **Odd $A$** ($A \geq 3$): the factorization $a^Z b^{N-1}(a-b)$ is positive, and the prescription is $Q = |S \cdot \Delta| \times m_e$.
2. **Even $A$**: the factorization is negative. The prescription restricts the sum to Frobenius-positive configurations ([confinement LP](#prop:confinement-lp)) and takes $Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e$.
3. **$A = 1$** (neutron decay): there are no spectators, and the prescription adds the positron correction, $Q = (S\Delta + 1) \times m_e$.

The comparison of $a$ against $b$ is fixed: $a - b = (q^2-1)\bigl(3(q^2+1)^2 - 2q^2\bigr)/(4q^3) > 0$ for $q > 1$, so $|b| > |a|$.

## Empirical comparison

The values below are the ones the corpus derives under the current framework (two-term Lagrangian trace, photon $1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}$, electron $\sigma_0\sigma_1\sigma_0$).

| Decay | $A$ | $Q_{\mathrm{calc}}$ (MeV) | $Q_{\mathrm{exp}}$ (MeV) | Error |
|-------|-----|---------------------------|--------------------------|-------|
| $n \to p$ | 1 | $\approx 0.32543$ | $0.78233$ | $-58.40\%$ |
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ | 3 | not derived | $0.0186$ | — |
| ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ | 6 | not derived | $3.508$ | — |

The $n \to p$ value is $|\varepsilon_n - \varepsilon_p| \cdot E_0$ on the $\gamma\gamma$-selected element $V^3$ for both nucleons, with $\varepsilon$ the $z_D$ Markov trace and $E_0$ the tower-summed scale. It holds only if three conjectures hold: the decay functional is the weight-trace difference, both nucleons are $V^3$, and $Q_\beta = |\varepsilon| E_0$. None of the three is proved. No Q-value for ${}^3\mathrm{H}$ or ${}^6\mathrm{He}$ is derived under the current framework, so the three regime prescriptions above are not tested by any current number.
