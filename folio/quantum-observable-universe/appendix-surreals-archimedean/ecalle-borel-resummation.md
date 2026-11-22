A divergent Gevrey-1 asymptotic series acquires a canonical analytic
meaning through the Borel transform and its Laplace–Borel sums
\cite{ecalle1981}.

## Definition

Let $K$ be a field of characteristic zero and let

$$
  \tilde f(z) = \sum_{n \geq 0} a_n \, z^{-n-1},
  \qquad a_n \in K,
$$

be a formal power series at $z = \infty$. The **formal Borel
transform** of $\tilde f$ is

$$
  \mathcal{B}\tilde f(\xi) = \sum_{n \geq 0} \frac{a_n}{n!} \, \xi^n ,
$$

the coefficient-wise division $a_n \mapsto a_n / n!$. When $\tilde f$ is **Gevrey-1** —
$|a_n| \leq C \, n! \, A^{-n}$ for some $C, A > 0$ and
$K \subseteq \mathbb{C}$ — its coefficients grow at most
geometrically, so $\mathcal{B}\tilde f$ is a germ analytic on the
disc $|\xi| < A$.

## Lateral Laplace–Borel sums and Stokes rays

Suppose $\mathcal{B}\tilde f$ continues analytically along the ray
$e^{i\theta} \mathbb{R}_{\geq 0}$ with at most exponential growth. The
**lateral Laplace–Borel sum** of $\tilde f$ in the direction $\theta$
is

$$
  \mathcal{L}^{\theta} \tilde f(z)
  = \int_0^{e^{i\theta} \infty} \mathcal{B}\tilde f(\xi) \,
    e^{-z\xi} \, d\xi ,
$$

analytic and asymptotic to $\tilde f$ (Gevrey-1) on a half-plane
bisected by the conjugate direction. A direction $\theta$ is a
**Stokes ray** when a singularity $\omega$ of $\mathcal{B}\tilde f$
lies on $e^{i\theta} \mathbb{R}_{> 0}$: the integral through $\omega$
is obstructed, and only the two lateral sums
$\mathcal{L}^{\theta^+}$, $\mathcal{L}^{\theta^-}$ (deformed on either
side of $\omega$) are defined. Their difference is exponentially
small, of order $e^{-\omega z}$ — the Stokes phenomenon.

## Median resummation

The **median resummation** $\mathcal{L}^{\mathrm{med}}$ is the
canonical average of the two lateral sums across a Stokes ray — in
the simplest one-singularity case
$\tfrac{1}{2}\bigl(\mathcal{L}^{\theta^+} + \mathcal{L}^{\theta^-}\bigr)$,
and in general the composition of a lateral sum with the half-power
of the Stokes automorphism \cite{ecalle1981}. For a series with real
coefficients whose Stokes ray is the positive real axis, the median
sum is the unique **real and single-valued** resummation.

## Beyond a single series: trans-series

The definition above resums one Gevrey-1 series. A trans-series
$\Phi = \sum_{\ell \ge 0} y^{\ell} \varphi_\ell(g)$ adds a second layer.
Its lateral resummation $s_\pm(\Phi) = \sum_{\ell} y^\ell s_\pm(\varphi_\ell)(g)$
is itself an infinite sum over the non-perturbative sectors, and that sum
is a potential new source of divergence even when every lateral sum
$s_\pm(\varphi_\ell)$ exists \cite[\S2, eq.~(2.5)]{arxiv-2302.08363v2}.
Reorganising by a fixed power $g^n$ gives the partial series
$G_n(y) = \sum_\ell a_{n,\ell}\, y^\ell$ with $\Phi = \sum_n g^n G_n(y)$
\cite[eqs.~(2.6)--(2.7)]{arxiv-2302.08363v2}; the convergence property
the source studies is that the $G_n$ converge with a common radius $R$,
with $a_{n,\ell} \sim \ell^{-b_n} R^{-\ell}$ expected generically
\cite[eq.~(2.8)]{arxiv-2302.08363v2}. That property is proved for
nonlinear ODEs in the work the source cites, and the source examines
QFT examples in which it holds; it is not implied by the single-series construction of
this definition.
