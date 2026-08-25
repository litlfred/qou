The geometric Riemann hypothesis constrains the absolute values of the
Frobenius eigenvalues of Bring's curve; the local $q$-zeta function
packages those eigenvalues as a single generating function.
Define the :defterm[local $q$-zeta function]{#local-q-zeta-function} of Bring's curve $\mathcal{B}$ as
the generating function for point counts over finite extensions:

$$
Z(\mathcal{B}, t) = \exp\!\left(\sum_{n=1}^{\infty} \frac{|\mathcal{B}(\mathbb{F}_{q^n})|}{n} t^n\right) = \frac{P(t)}{(1-t)(1-qt)},
$$

where $P(t) = \prod_{i=1}^{2g}(1 - \alpha_i t)$ is the characteristic polynomial of the Frobenius endomorphism $\mathrm{Fr}_q : H^1(\mathcal{B}) \to H^1(\mathcal{B})$. Because $g = 4$ for Bring's curve, this polynomial has degree $2g = 8$. The roots $\alpha_1, \ldots, \alpha_8$ are the fundamental eigenvalues of the Frobenius action on the first étale cohomology. The denominator factors $(1-t)$ and $(1-qt)$ correspond to $H^0$ and $H^2$ respectively.
