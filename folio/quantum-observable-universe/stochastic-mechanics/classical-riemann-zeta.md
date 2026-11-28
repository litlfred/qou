The **classical Riemann zeta function** $\zeta(s)$ is the Euler product

$$
\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}
         = \sum_{n=1}^{\infty} \frac{1}{n^s},
  \qquad \mathrm{Re}(s) > 1.
$$

It is the zeta function of $\mathrm{Spec}\,\mathbb{Z}$: each local factor $(1 - p^{-s})^{-1}$ is the zeta function of the point $\mathrm{Spec}\,\mathbb{F}_p$, which has no $H^1$ and so no Frobenius eigenvalues. It is not the product of the local zeta functions $Z(\mathcal{B}/\mathbb{F}_p, p^{-s})$ of Bring's curve. That product is $\zeta(s)\,\zeta(s-1)/L(E,s)^4$ up to finitely many Euler factors, where $E$ is the elliptic curve 50a1 ([geometric stability via the Weil bound](#sec:q-gl-weil-bound-stability)); $\zeta(s)$ appears in it only as the $H^0$ factor.
