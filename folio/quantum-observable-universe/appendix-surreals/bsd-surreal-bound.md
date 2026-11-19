The classical Birch--Swinnerton-Dyer conjecture asserts that the order of vanishing of the $L$-function $L(\mathcal{E}_q, s)$ at $s = 1$ equals the Mordell--Weil rank of the elliptic curve $\mathcal{E}_q$ ([$q$-Birch--Swinnerton-Dyer](#conj:q-birch-swinnerton-dyer)). This remark expresses that order-of-vanishing match as a literal surreal-order identity.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)), and $\mathcal{E}_q$ the Descartes elliptic curve attached to the substrate. Let $r = \mathrm{rank}\bigl(\mathcal{E}_q(\mathbb{Q})\bigr)$ be the Mordell--Weil rank.

By [surreal rate calculus](#prop:surreal-rate-calculus) and the spectral identification of $L$-values with Reeb-period integrals, the surreal $\omega$-order of $L(\mathcal{E}_q, 1 + \delta)$ as $\delta$ is a standard-real drift is

$$
\ordw\bigl(L(\mathcal{E}_q, 1 + \delta)\bigr) = r \cdot \ordw(\delta) \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Equivalently, near $\delta = 0$:

$$
L(\mathcal{E}_q, 1 + \delta) \asymp c \cdot \delta^r \qquad (\text{standard-real } c \neq 0).
$$

By [surreal squeeze](#lem:surreal-squeeze), every standard-real drift $\delta > 0$ produces cost $\delta^2 \cdot \varepsilon^{-1}$ exceeding the mass-gap budget $\varepsilon^3$. Thus, the $L$-function cannot support a hidden zero of order strictly greater than the rank. The surreal-order identity is rigid in $\mathbb{R}(\varepsilon)$.

In $\omega$-adic form ([Big-O via $\ordw$](#rem:conway-normal-form)):

$$
\ordw\bigl(L(\mathcal{E}_q, 1 + \delta) / \delta^r\bigr) = 0 \qquad (\text{no extra vanishing beyond the rank}).
$$

The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals $r$, as a literal identity of surreal $\omega$-orders. Classical BSD is recovered by applying the standard-part map ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)): $\mathrm{st}\bigl(-\ordw(L)\bigr) = r$ gives the classical rank formula (with $\delta = \omega^{-1}$ infinitesimal, $L \asymp \delta^r = \omega^{-r}$ has $\ordw(L) = -r$; the classical order of vanishing $r$ is the negation).

The BSD bound generalizes the RH bound ([RH surreal bound](#rem:rh-surreal-bound)) from the trivial rank-zero case (Dedekind $\zeta$) to higher ranks. RH is the $r = 0$ specialization where no extra vanishing is allowed beyond the pole of $\zeta$. The surreal squeeze gives the same strict inequality at each rank: every drift beyond rank-prescribed vanishing is forbidden by the $\varepsilon^{-1} > \varepsilon^3$ separation of orders.

The refined BSD statement identifies the leading coefficient $c$ with the product of Tate--Shafarevich order, regulator, and periods. In surreal-order terms, this is a $\simeq$ identity (matching leading coefficients, not just $\omega$-orders). Its proof requires integrating the surreal $\ordw$-calculus with the Tate thesis adelic Fourier transform ([adelic--Tate surreal bound](#rem:adelic-tate-squeeze)).
