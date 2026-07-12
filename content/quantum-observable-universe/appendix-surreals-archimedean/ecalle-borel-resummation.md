A divergent Gevrey-1 asymptotic series acquires a canonical analytic
meaning through the Borel transform and its Laplace–Borel sums
[@ecalle1981]. This block fixes the transform, the lateral sums, and
the median resummation used throughout the surreal appendices and the
mass chapters; the alien derivative and the bridge equation are
recorded at the end as surrounding vocabulary.

## Definition

Let $K$ be a field of characteristic zero and let

$$
  \tilde f(z) = \sum_{n \geq 0} a_n \, z^{-n-1},
  \qquad a_n \in K,
$$

be a formal power series at $z = \infty$. The **formal Borel
transform** of $\tilde f$ is the formal power series

$$
  \mathcal{B}\tilde f(\xi) = \sum_{n \geq 0} \frac{a_n}{n!} \, \xi^n .
$$

At the coefficient level the transform is the exact division
$a_n \mapsto a_n / n!$ (the convention formalised in the Lean sibling,
`borelCoeff`, over a generic characteristic-zero field). When
$\tilde f$ is **Gevrey-1** — $|a_n| \leq C \, n! \, A^{-n}$ for some
$C, A > 0$ and $K \subseteq \mathbb{C}$ — the transformed coefficients
grow at most geometrically, so $\mathcal{B}\tilde f$ is the germ of a
function analytic on the disc $|\xi| < A$.

## Lateral Laplace–Borel sums and Stokes rays

Suppose $\mathcal{B}\tilde f$ continues analytically to a
neighbourhood of the ray $e^{i\theta} \mathbb{R}_{\geq 0}$ with at
most exponential growth there. The **lateral Laplace–Borel sum** of
$\tilde f$ in the direction $\theta$ is

$$
  \mathcal{L}^{\theta} \tilde f(z)
  = \int_0^{e^{i\theta} \infty} \mathcal{B}\tilde f(\xi) \,
    e^{-z\xi} \, d\xi ,
$$

an analytic function asymptotic to $\tilde f$ (Gevrey-1) on a
half-plane bisected by the conjugate direction. A direction $\theta$
is a **Stokes ray** when a singularity $\omega$ of
$\mathcal{B}\tilde f$ lies on $e^{i\theta} \mathbb{R}_{> 0}$: the
integral through $\omega$ is obstructed, and only the two lateral
sums $\mathcal{L}^{\theta^+}$, $\mathcal{L}^{\theta^-}$ (contours
deformed to pass on either side of the singularities) are defined.
Their difference is exponentially small, of order $e^{-\omega z}$ —
the Stokes phenomenon.

## Median resummation

The **median resummation** $\mathcal{L}^{\mathrm{med}}$ is the
canonical average of the two lateral sums across a Stokes ray — in
the simplest one-singularity case
$\tfrac{1}{2}\bigl(\mathcal{L}^{\theta^+} + \mathcal{L}^{\theta^-}\bigr)$,
and in general the composition of a lateral sum with the half-power
of the Stokes automorphism [@ecalle1981]. For a series with real
coefficients whose Stokes ray is the positive real axis, the median
sum is the unique resummation that is **real and single-valued**,
resolving the lateral ambiguity.

## Context: alien derivatives and the bridge equation

The following operators are not part of the object defined above;
they are its surrounding resurgence vocabulary [@ecalle1981]. For a
singularity location $\omega$ of $\mathcal{B}\tilde f$, Écalle's
**alien derivative** $\Delta_\omega$ is a derivation on resurgent
series measuring the singularity type of $\mathcal{B}\tilde f$ at
$\omega$; it vanishes iff the Borel transform is regular there. The
**bridge equation**

$$
  \Delta_\omega \tilde f = A_\omega \, \frac{\partial \tilde f}{\partial z}
$$

links the alien derivations to the natural derivation, with the
scalar $A_\omega$ the **Stokes constant** at $\omega$; the collection
$\{A_\omega\}$ determines the Stokes automorphism and hence the
lateral–median relations above.

## Disambiguation: three unrelated "Borel"s

The transform defined here is due to Émile Borel and belongs to
resurgence theory. It is distinct from two other "Borel"s in this
paper: the Borel **regulator** (Armand Borel) on $K_3$ appearing in
[Borel partial resolution](#prop:borel-partial-resolution) and
[Borel–Zagier QOU volumes](#conj:borel-zagier-qou-volumes), and the
Lie-theoretic Borel **subalgebras** of the $q$-oper chapter.
Resummation statements bear neither on regulator transcendence nor
on $q$-oper flag data, and the three senses must not be
cross-linked.
