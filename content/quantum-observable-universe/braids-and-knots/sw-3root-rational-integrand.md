**Proposition.** *The Schur-Weyl 3-root product `λ_{SW}^{(1)}(z)`
appearing in the categorical action integral
([conj:flavor-dressed-mass-from-substrate-split](#conj:flavor-dressed-mass-from-substrate-split))
is an EXACT rational function of z with polynomial numerator and
denominator of degree 6:*

$$
  \lambda_{SW}^{(1)}(z)
  \;=\; \prod_{k=1}^{3} \frac{dc_k}{dz}
  \;=\;
  -\frac{P(z)}{D(z)}
$$

*where*

$$
  P(z) = 64 z^6 + 96 z^5 + 120 z^4 + 160 z^3 + 105 z^2 + 66 z + 39
$$

*and*

$$
  D(z) = 16 z^6 + 24 z^5 + 35 z^4 + 50 z^3 + 35 z^2 + 24 z + 16
$$

*The denominator $D(z)$ has* **palindromic coefficients**
*(16, 24, 35, 50, 35, 24, 16), reflecting the $z \leftrightarrow 1/z$
symmetry of the underlying color-tube cubic
[`conj:flavor-dressed-mass-from-substrate-split`](#conj:flavor-dressed-mass-from-substrate-split) at its discriminant.*

*The roots $\{c_k(z)\}_{k=1,2,3}$ are the three color-channel
prolongations of the cubic*

$$
  F(z, c) \;=\; c^3 + (4z + 1) c^2 + (6 z^2 + 3 z + 1) c + (4 z^3 + 3 z^2 + 2 z + 1).
$$

## Proof

By the implicit function theorem applied to $F(z, c_k(z)) = 0$:

$$
  \frac{d c_k}{dz} \;=\; -\frac{F_z(z, c_k)}{F_c(z, c_k)}
$$

where $F_z = \partial F / \partial z$ and $F_c = \partial F / \partial c$.

Taking the product over the three roots:

$$
  \prod_{k=1}^{3} \frac{d c_k}{dz}
  \;=\; (-1)^3 \frac{\prod_k F_z(z, c_k)}{\prod_k F_c(z, c_k)}
  \;=\; -\frac{\prod_k F_z(z, c_k)}{\prod_k F_c(z, c_k)}.
$$

By the **resultant-product identity**, for a monic polynomial
$F$ of degree $n$ with roots $\{c_k\}$ and any polynomial $G$:

$$
  \prod_{k=1}^{n} G(c_k) \;=\; \mathrm{Res}_c(F, G).
$$

Since the color-tube cubic is monic in $c$:

$$
  \prod_k F_z(z, c_k) \;=\; \mathrm{Res}_c(F, F_z)
  \quad\text{and}\quad
  \prod_k F_c(z, c_k) \;=\; \mathrm{Res}_c(F, F_c) \;=\; \mathrm{disc}_c(F)
$$

where the last equality (with sign correction (-1)^{n(n-1)/2} for monic F of degree n=3) relates the c-derivative resultant to the discriminant.

Direct symbolic computation (sympy `resultant`):

$$
  \mathrm{Res}_c(F, F_z) = 64 z^6 + 96 z^5 + 120 z^4 + 160 z^3 + 105 z^2 + 66 z + 39 = P(z)
$$

$$
  \mathrm{Res}_c(F, F_c) = 16 z^6 + 24 z^5 + 35 z^4 + 50 z^3 + 35 z^2 + 24 z + 16 = D(z)
$$

Substituting gives the claimed form $\lambda_{SW}^{(1)}(z) = -P(z)/D(z)$. $\square$

## Numerical sanity

At $z = 0.1$:

| Quantity | Value |
|----------|-------|
| Symbolic $-P(0.1)/D(0.1)$ | $-2.4900888950\ldots$ |
| Production [`sw_3root_product_degree1(0.1)`](../../folio-assistant/computations/picard_lefschetz_thimble.py) | $-2.4900888950\ldots$ |

Match to machine precision.

## Categorical reading

- $D(z) = \mathrm{Res}_c(F, F_c) = -\mathrm{disc}_c(F)$: the zeros of the discriminant are
  the **Picard-Lefschetz critical points** where two cubic roots
  collide. These mark the **branch points** of the SW 3-root
  product as a function of $z$.

- $P(z) = \mathrm{Res}_c(F, F_z)$: encodes the derivative information
  of all three roots; vanishes at critical points where
  $\partial F / \partial z = 0$ for some root.

- The ratio $-P/D$ has poles only at $D(z) = 0$ (PL critical
  points). On the real axis between these poles, $\lambda_{SW}^{(1)}$
  is a real-valued rational function.

This is the **algebraic foundation** for the categorical action
$A(a) = \big| \int_{-a}^{a} \lambda_{SW}^{(1)}(z)\,dz \big| / |\cdots|$
used in
[`prop:flavor-dressed-mass-from-substrate-split`](#prop:flavor-dressed-mass-from-substrate-split).

## Consequences

Because $\lambda_{SW}^{(1)}$ is rational, the integral
$\int_{-a}^{a} \lambda_{SW}^{(1)}(z)\,dz$ is computable in closed
form via partial fractions (logs + arctans of polynomial roots).

The Wedderburn-decomposition target

$$
  A(a) \;=\; \sum_{\lambda \vdash 3} y_\lambda(q) \cdot g_\lambda(a)
$$

(where $y_\lambda$ are the H_3 Markov weights — natural since the
cubic is 3-strand) reduces to identifying the partition-indexed
pieces $g_\lambda(a)$. This is the structural path forward for
deriving the substrate $m_p$ anchor categorically.

## Citation

The Vieta-resultant identity is classical (Lang, *Algebra* §IV.8).
The specific cubic $F(z, c)$ here is the QOU color-tube cubic
from [`conj:flavor-dressed-mass-from-substrate-split`](#prop:color-tube-cubic).
