The half-life formula ([hadron half-life](#prop:hadron-half-life)) exhibits three qualitatively distinct regimes as the substrate parameter $q$ varies.

| Regime | $q$ range | $(q - q^{-1})^5$ | $(q + q^{-1})$ | Half-life behaviour |
| --- | --- | --- | --- | --- |
| Classical | $q \to 1$ | $\to 0$ | $\to 2$ | $t_{1/2} \to \infty$: no beta decay |
| Descartes | $q = q_0$ | $\approx 3.6 \times 10^{-4}$ | $\approx 2.012$ | Observed nuclear lifetimes |
| Deep quantum | $q \to \infty$ | $\to \infty$ | $\to \infty$ | $t_{1/2} \to 0$: instantaneous decay |

**$q$-dependent scaling.**

The decay rate depends on $q$ through $(q + q^{-1})(q - q^{-1})^5$. This prefactor vanishes as $q \to 1$ (the classical limit: no Coulomb splitting, no beta decay). It diverges as $q \to \infty$ (instantaneous decay).

**Drip-line asymptotics.**

At the proton or neutron drip line, $|\delta p| \gg 1$ and the $Q$-value grows linearly. The Sargent $Q^5$ scaling predicts extremely short half-lives. This explains why drip-line nuclei ($|\delta p| \gtrsim 5$) have $t_{1/2} < 10^{-3}\text{ s}$ and are produced only in nuclear reactions.

**Sensitivity to $q$.**

Because $\Gamma_\beta \propto (q + q^{-1})(q - q^{-1})^5$, the logarithmic derivative with respect to $\ln q$ is:

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  = 
  \frac{q^2 - 1}{q^2 + 1}
  + 
  5\frac{q^2 + 1}{q^2 - 1}.
$$

The first term derives from $\partial_{\ln q}\ln(q + q^{-1})$, the second from $5\partial_{\ln q}\ln(q - q^{-1})$. At $q = q_0$, this derivative evaluates to $\approx 48$. Nuclear half-lives are thus exquisitely sensitive to $q$: a $1\%$ shift in $q$ drives a $\sim 50\%$ shift in decay rates. This extreme sensitivity dictates the narrow, sharply-defined shape of the physical valley of stability.
