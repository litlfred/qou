*Let $R$ be a commutative ring and $q \in R^\times$ a unit. Every pre-Archimedean aether identity—the Hecke quadratic*

$$
  \sigma_i^2 = (q - q^{-1})\sigma_i + 1,
$$

*the bar involution $q \leftrightarrow q^{-1}$, $\sigma_i \leftrightarrow \sigma_i^{-1}$, the Frobenius pairing $\langle\cdot,\cdot\rangle_F$, and the Markov trace $\mathrm{tr}_M$—is stated polymorphically in $R$. The specialization $R = \mathbb{C}$ with $q_0 \in \mathbb{C}$ and $\lvert q_0 \rvert > 1$ is admissible. The aether identities transfer verbatim, with $\lvert q \rvert > 1$ replacing the archimedean ordering $q > 1$ as the aether-level non-degeneracy condition.*

## Significance

The proposition makes explicit that the framework's pre-Archimedean content is independent of the choice of $\mathrm{Im}(q)$. The current convention $q_0 \in \mathbb{R}$, $q_0 > 1$ is one valid specialization.

**CAL-4 caveat:** A complex $q_0$ with $\lvert q_0 \rvert > 1$ would require either a function expressing $\mathrm{Im}(q_0)$ in terms of the three existing calibrations, or a structural constraint fixing $\mathrm{Im}(q_0)$ from aether data. Neither is currently supplied. The proposition provides infrastructure for the categorical lift without claiming the physical reality of $\mathrm{Im}(q_0)$.

The codebase evaluates one complex-$q$ regime: the unit circle $q = e^{i\Theta}$. Here the bar involution coincides with complex conjugation, and the pair $(\Phi_q, \mathrm{Li}_2^q)$ becomes a Hermitian-conjugate pair. This proposition extends the admissible regime to $\lvert q \rvert > 1$, where Lusztig bar and Hermitian $\ast$ split. The unit-circle case forms the boundary, the real-axis case forms the $\mathrm{Im}(q) = 0$ specialization, and the general complex case sits between them.
