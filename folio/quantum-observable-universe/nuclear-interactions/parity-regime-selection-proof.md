## Proof

> **Explicit regime inequality.** The comparison between $a$ and $b$ that selects the regime follows from $a - b = (q^2-1)\bigl(3(q^2+1)^2 - 2q^2\bigr)/(4q^3) > 0$ for $q > 1$, so $|b| > |a|$. The regime formulas themselves are stated, not derived. The table of $Q_{\mathrm{calc}}$ against $Q_{\mathrm{exp}}$ is an empirical comparison and is not part of the proof.


Since $a < 0$ and $b < 0$ for all $q > 1$ ([spectator normalization](#def:spectator-normalization)), the product $a^Z \cdot b^{N-1}$ carries the sign $(-1)^Z \cdot (-1)^{N-1} = (-1)^{A-1}$.

- **Odd $A$**: $(-1)^{A-1} = +1$. The factorization is positive.
- **Even $A$**: $(-1)^{A-1} = -1$. The factorization is negative, so the raw character sum fails to yield $Q > 0$ directly.

The even-$A$ case requires restricting to Frobenius-positive configurations ([confinement LP](#prop:confinement-lp)). This constraint ensures that both parent and daughter exhibit non-negative Markov traces.

## Numerical verification

| Decay | $A$ | Regime | $Q_{\mathrm{calc}}$ (MeV) | $Q_{\mathrm{exp}}$ (MeV) | Error |
|-------|-----|--------|---------------------------|--------------------------|-------|
| $n \to p$ | 1 (odd) | $(S\Delta+1) \times m_e$ | $\approx 0.7816$ | $0.7823$ | $-0.10\%$ |
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ | 3 (odd) | $\|S\Delta\| \times m_e$ | $\approx 0.0179$ | $0.0186$ | $-3.64\%$ |
| ${}^6\mathrm{He} \to {}^6\mathrm{Li}$ | 6 (even) | $(\Sigma_{\mathrm{FP}}+1) \times m_e$ | $\approx 3.637$ | $3.508$ | $+3.68\%$ |
