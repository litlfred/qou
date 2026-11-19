Let $K$ be a field of characteristic zero and let

$$
  \tilde f(z) = \sum_{n \geq 0} a_n \, z^{-n-1},
  \qquad a_n \in K,
$$

be a formal power series at $z = \infty$. The **formal Borel
transform** of $\tilde f$ is

$$
  \mathcal{B}\tilde f(\xi) = \sum_{n \geq 0} \frac{a_n}{n!} \, \xi^n .
$$

For $K \subseteq \mathbb{C}$, $\tilde f$ is **Gevrey-1** if
$|a_n| \leq C \, n! \, A^{-n}$ for some $C, A > 0$.

Suppose $\mathcal{B}\tilde f$ continues analytically along the ray
$e^{i\theta} \mathbb{R}_{\geq 0}$ with at most exponential growth. The
**lateral Laplace–Borel sum** of $\tilde f$ in the direction $\theta$
is

$$
  \mathcal{L}^{\theta} \tilde f(z)
  = \int_0^{e^{i\theta} \infty} \mathcal{B}\tilde f(\xi) \,
    e^{-z\xi} \, d\xi .
$$

A direction $\theta$ is a **Stokes ray** if a singularity $\omega$ of
$\mathcal{B}\tilde f$ lies on $e^{i\theta} \mathbb{R}_{> 0}$; then
$\mathcal{L}^{\theta^+}$, $\mathcal{L}^{\theta^-}$ denote the lateral sums
deformed on either side of $\omega$. The **median resummation**
$\mathcal{L}^{\mathrm{med}}$ is the composition of a lateral sum with the
half-power of the Stokes automorphism \cite{ecalle1981}.
