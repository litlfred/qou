For the deuteron representative $\beta_{\mathrm{D}} = \sigma_0 \in B_2$:
$L = 1$, $\|\rho\|_{\mathrm{op}} = |q^{1/2}| \approx 1.0536$ at $q_0 \approx 1.1100$, and $\mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}) \approx 0.61269$ (the level-0 Markov trace of the Hopf link, convention D). Substituting,

$$
  \Delta_{\max}(\mathrm{D})
  \;\leq\;
  2 \cdot 1 \cdot (1.0536)^{2} \cdot 0.61269
  \;\approx\; 1.360.
$$

The $\hbar_q^{2(N+1)}/(1 - \hbar_q^{2})$ tail factor at $N = 2$ gives $\approx 0.00982^{3}/(1 - 0.00982) \approx 9.6 \times 10^{-7}$.
Multiplying, the level-$\ge 3$ truncation error on the deuteron is bounded by $\approx 1.31 \times 10^{-6}$ in categorical units, i.e. **order-ppm binding precision** ($\approx 1.3$ ppm).

## Corollary for the binding energy

Combining with the jet-tower tail bound, the $N$-term truncation error for any vortex is

$$
  |E_\mathrm{bind} - E_\mathrm{bind}^{(N)}|
  \;\leq\;
  E_0 \cdot 2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}})
  \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

For light atoms ($A \le 16$) at $q_0$, numerical evaluation shows $N = 3$ is sufficient for order-ppm precision on binding energies; the bound is saturated within a factor of 2 on the deuteron, tritium, and ${}^3\mathrm{He}$ (cf. `computations/unified_lift.py` with `JET_TARGET_PPM`).
