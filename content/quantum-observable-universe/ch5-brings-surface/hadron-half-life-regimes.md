The half-life formula
([hadron half-life](#prop:hadron-half-life)) exhibits three
qualitatively distinct regimes as the substrate parameter $q$
varies.

| Regime | $q$ range | $(q - q^{-1})^5$ | $(q + q^{-1})$ | Half-life behaviour |
|--------|-----------|-------------------|----------------|---------------------|
| Classical | $q \to 1$ | $\to 0$ | $\to 2$ | $t_{1/2} \to \infty$: no beta decay |
| Descartes | $q = 1.110$ | $\approx 3.6 \times 10^{-4}$ | $\approx 2.012$ | Observed nuclear lifetimes |
| Deep quantum | $q \to \infty$ | $\to \infty$ | $\to \infty$ | $t_{1/2} \to 0$: instantaneous decay |

**Near-stability expansion.**
For nuclei one unit from the valley ($|\delta p| = 1$), the half-life
at fixed $A$ depends only on $q$ and the mass number:

$$
  t_{1/2}(|\delta p| = 1)
  \;\propto\;
  \frac{A^{5/3}}{(q + q^{-1})(q - q^{-1})^5 \, \lambda_C^5}.
$$

At $q = 1.110$: for light nuclei ($A \sim 20$), this gives
$t_{1/2} \sim 1\text{ s}$ (observed: $^{20}\text{F}$ has
$t_{1/2} = 11\text{ s}$); for heavy nuclei ($A \sim 200$), it gives
$t_{1/2} \sim 10^{8}\text{ s}$ (observed: $^{210}\text{Bi}$ has
$t_{1/2} \approx 4 \times 10^{8}\text{ s}$).

**Drip-line asymptotics.**
At the proton or neutron drip line, $|\delta p| \gg 1$ and the
$Q$-value grows linearly.  The Sargent $Q^5$ scaling then predicts
extremely short half-lives, explaining why drip-line nuclei
($|\delta p| \gtrsim 5$) have $t_{1/2} < 10^{-3}\text{ s}$ and are
produced only in nuclear reactions.

**Sensitivity to $q$.**
The $q$-derivative of the decay rate,

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  \;=\;
  \frac{2q^2}{q^2 - 1}
  \;+\;
  \frac{10 q^2}{q^2 - 1}
  \;-\;
  \frac{10}{q^2 - 1}
  \;=\;
  \frac{12 q^2 - 10}{q^2 - 1},
$$

evaluates to $\approx 49$ at $q = 1.110$, confirming that nuclear
half-lives are exquisitely sensitive to $q$: a $1\%$ shift in $q$
changes decay rates by $\sim 50\%$.  This extreme sensitivity is why
the valley of stability has the narrow, sharply-defined shape observed
in nature.
