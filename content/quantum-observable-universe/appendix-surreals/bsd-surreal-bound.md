The classical Birch–Swinnerton-Dyer (BSD) conjecture equates the order of vanishing of the $L$-function $L(\mathcal{E}_q, s)$ at $s = 1$ to the Mordell–Weil rank of the elliptic curve $\mathcal{E}_q$ ([$q$-Birch--Swinnerton-Dyer](#conj:q-birch-swinnerton-dyer)). This remark formulates the order-of-vanishing matching as a literal identity of surreal $\omega$-orders. This demonstrates how standard drifts separate spectral zeros from mass-gap fluctuations.

### Setup

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)). Set $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)), and let $\mathcal{E}_q$ be the Descartes elliptic curve attached to the substrate. Let $r = \mathrm{rank}\bigl(\mathcal{E}_q(\mathbb{Q})\bigr)$ denote the Mordell–Weil rank.

### The Surreal Bound

By [surreal rate calculus](#prop:surreal-rate-calculus) and the spectral identification of $L$-values with Reeb-period integrals, the surreal $\omega$-order of $L(\mathcal{E}_q, 1 + \delta)$ for a standard-real drift $\delta$ is:

$$
  \ordw\bigl(L(\mathcal{E}_q, 1 + \delta)\bigr)
   \;=\; r \cdot \ordw(\delta)
  \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Equivalently, near $\delta = 0$:

$$
  L(\mathcal{E}_q, 1 + \delta)
   \;\asymp\; c \cdot \delta^r
  \qquad (\text{standard-real } c \neq 0).
$$

By [surreal squeeze](#lem:surreal-squeeze), every standard-real drift $\delta > 0$ produces a cost $\delta^2 \cdot \varepsilon^{-1}$ that exceeds the mass-gap budget $\varepsilon^3$. Thus, the $L$-function cannot support a hidden zero of order strictly greater than the rank. The surreal-order identity is rigid in $\mathbb{R}(\varepsilon)$.

In $\omega$-adic form ([Big-O via $\ordw$](#rem:conway-normal-form)):

$$
  \ordw\bigl(L(\mathcal{E}_q, 1 + \delta) / \delta^r\bigr) \;=\; 0.
$$

This asserts there is no extra vanishing beyond the rank.

### Conclusion

The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals $r$ as a literal identity of surreal $\omega$-orders. Classical BSD is recovered by applying the standard-part functor ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)). Substituting an infinitesimal drift $\delta = \omega^{-1}$ yields $L \asymp \delta^r = \omega^{-r}$, so $\ordw(L) = -r$. Taking $\mathrm{st}\bigl(-\ordw(L)\bigr) = r$ recovers the classical rank formula.

### Relation to RH

The BSD bound generalizes the Riemann Hypothesis (RH) bound ([RH surreal bound](#rem:rh-surreal-bound)) from the rank-zero case (Dedekind $\zeta$) to higher ranks. RH is the $r = 0$ specialization where no extra vanishing is allowed beyond the pole of $\zeta$. The surreal squeeze enforces the same strict inequality at each rank. Every drift beyond the rank-prescribed vanishing is forbidden by the $\varepsilon^{-1} > \varepsilon^3$ separation of orders.

### Leading-coefficient BSD

The refined BSD statement identifies the leading coefficient $c$ with the product of the Tate–Shafarevich order, the regulator, and periods. In surreal-order terms, this is an exact matching of leading coefficients ($\simeq$), not just $\omega$-orders. Proving this requires integrating the surreal $\ordw$-calculus with the Tate thesis adelic Fourier transform ([adelic--Tate surreal bound](#rem:adelic-tate-squeeze)).
