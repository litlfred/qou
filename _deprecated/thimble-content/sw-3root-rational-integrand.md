*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.** *The Schur-Weyl 3-root product `λ_{SW}^{(1)}(z)`
appearing in the categorical action
([def:categorical-action](#def:categorical-action))
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
[`rem:color-tube-cubic`](#rem:color-tube-cubic) at its discriminant.*

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
  \prod_k F_c(z, c_k) \;=\; \mathrm{Res}_c(F, F_c).
$$

*Note on sign convention.* For a monic polynomial of degree $n$ in $c$, the discriminant and the
$c$-derivative resultant differ by the sign $(-1)^{n(n-1)/2}$. With $n = 3$ this sign is
$(-1)^{3} = -1$, so $\mathrm{disc}_c(F) = -\mathrm{Res}_c(F, F_c) = -D(z)$. In particular
$D(0) = +16$ while $\mathrm{disc}_c(F)|_{z=0} = -16$, since the cubic $c^3 + c^2 + c + 1$ has
one real and two purely imaginary roots (negative discriminant). The denominator $D(z)$ defined
in this proposition is therefore the **derivative-resultant** $\mathrm{Res}_c(F, F_c)$, equal to
the negative of the discriminant. Its zeros are still the Picard–Lefschetz critical points
(roots of $\mathrm{disc}_c(F)$ and of $\mathrm{Res}_c(F, F_c)$ agree as sets).

Direct symbolic computation (sympy `resultant`):

$$
  \mathrm{Res}_c(F, F_z) = 64 z^6 + 96 z^5 + 120 z^4 + 160 z^3 + 105 z^2 + 66 z + 39 = P(z)
$$

$$
  \mathrm{Res}_c(F, F_c) = 16 z^6 + 24 z^5 + 35 z^4 + 50 z^3 + 35 z^2 + 24 z + 16 = D(z)
$$

(equivalently $\mathrm{disc}_c(F) = -D(z)$; see the sign-convention note above).

Substituting gives the claimed form $\lambda_{SW}^{(1)}(z) = -P(z)/D(z)$. $\square$

## Numerical sanity

At $z = 0.1$:

| Quantity | Value |
|----------|-------|
| Symbolic $-P(0.1)/D(0.1)$ | $-2.4900888950\ldots$ |
| Production [`sw_3root_product_degree1(0.1)`](../../../computations/picard_lefschetz_thimble.py) | $-2.4900888950\ldots$ |

Match to machine precision.

## Categorical reading

- $D(z) = \mathrm{Res}_c(F, F_c) = -\mathrm{disc}_c(F)$: the zeros of $D$ (equivalently of
  the discriminant) are the **Picard-Lefschetz critical points** where two cubic roots
  collide. These mark the **branch points** of the SW 3-root product as a function of $z$.

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
Polynomial division gives

$$
  -\frac{P(z)}{D(z)} \;=\; -4 \;+\; \frac{20 z^4 + 40 z^3 + 35 z^2 + 30 z + 25}{D(z)},
$$

so $\int_{-a}^{a} (-P/D)\,dz = -8a + R(a)$ where $R(a)$ is a sum of
arctangents over the three irrational $w$-roots of
$\tilde D(w) = 16 w^3 + 24 w^2 - 13 w + 2$ ($w = z + 1/z$ palindromic
substitution). $\tilde D$ has no rational roots (by the
rational-root theorem the candidates are $\pm 2^a / 2^b$ with $a \le 1$,
$b \le 4$; direct evaluation rules them all out — verified in
sympy: `Poly(D̃).is_irreducible = True`), so $\tilde D$ is
irreducible over $\mathbb{Q}$; combined with $\mathrm{disc}(\tilde D)
= -80000 < 0$ this means $\tilde D$ has one real and two complex-
conjugate roots, none in $\mathbb{Q}$. Consequently $D(z)$ does
not split over $\mathbb{Q}$ and the partial-fraction expansion of
$-P/D$ requires extending to a cubic-radical field.

The Wedderburn-decomposition target

$$
  A(a) \;=\; \sum_{\lambda \vdash 3} y_\lambda(q) \cdot g_\lambda(a)
$$

(where $y_\lambda$ are the H_3 Markov weights — natural since the
cubic is 3-strand) reduces to identifying the partition-indexed
pieces $g_\lambda(a)$.

**Scope caveat (CAL-4 caveat).** This proposition computes the **integrand** of
$A(a)$ in exact rational form. It does **not** derive the
**integration limit** $a$ at which $A(a)$ matches CODATA $m_p$. The
integration-limit question is conjectural (see
[`conj:lambda-scale-substrate-form`](#conj:lambda-scale-substrate-form)
and the cheat-sheet Migration Backlog #1) and known to be a CAL-4
anchor in the production chain
([`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md)).
The rational-integrand result here is a **necessary** structural
input for any future substrate derivation of $a$, but not a
**sufficient** one — given the integrand alone, the substrate value
of $a$ remains undetermined.

## Citation

The Vieta-resultant identity is classical (Lang, *Algebra* §IV.8).
The specific cubic $F(z, c)$ here is the QOU color-tube cubic
from [`rem:color-tube-cubic`](#rem:color-tube-cubic).
