The baryon period conjecture
([baryon period ratio](#conj:baryon-period-ratio)) integrates the
product $\prod_k dc_k/dz$ over the symmetric interval $[-a,\,a]$
where

$$
a(q) \;=\; \frac{4 - q}{4q + 3}.
$$

This expression defines a Möbius transformation $q \mapsto (-q + 4)/(4q + 3)$
whose algebraic structure we analyze here.

## The Möbius matrix

Every Möbius transformation $f(q) = (aq+b)/(cq+d)$ is represented
by a matrix
$M = \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr)$.
For the integration limit:

$$
M \;=\; \begin{pmatrix} -1 & 4 \\ 4 & 3 \end{pmatrix}.
$$

Its invariants are:

| Invariant | Value | Factorisation |
|-----------|-------|---------------|
| $\det M$ | $(-1)(3) - (4)(4) = -19$ | prime, orientation-reversing |
| $\operatorname{tr} M$ | $-1 + 3 = 2$ | |
| Char.\ poly. | $\lambda^2 - 2\lambda - 19$ | |
| Discriminant | $4 + 76 = 80 = 16 \cdot 5$ | |
| Eigenvalues | $1 \pm 2\sqrt{5}$ | $= 4\varphi - 1$ and $3 - 4\varphi$ |

where $\varphi = (1+\sqrt{5})/2$ is the golden ratio.

## Fixed points

The fixed points of $f$ are $1/\varphi$ and $-\varphi$
([Möbius golden fixed points](#prop:mobius-golden-fixed-points)).
The minimal polynomial $q^2 + q - 1 = 0$ is the characteristic
equation of $1/\varphi$ over $\mathbb{Q}$.

## Origin of the coefficients $\{-1, 4; 4, 3\}$

The matrix entries derive from the color-tube cubic
([color-tube cubic](#rem:color-tube-cubic)):

$$
F(z,c) = c^3 + (4z+1)\,c^2 + (6z^2+3z+1)\,c + (4z^3+3z^2+2z+1).
$$

The leading $z$-coefficients in each degree are $\binom{4}{1} = 4$,
$\binom{4}{2} = 6$, $\binom{4}{3} = 4$ — a binomial row.
The Möbius matrix extracts:

- $4 = \binom{4}{1}$: leading coefficient of the $c^2$ term in $z$,
- $3$: degree of the cubic (number of color sheets),
- $-1$: alternating sign from the numerator $4-q = -(q-4)$,
- $4$: repeated from the binomial coefficient.

The transformation $q \mapsto (4-q)/(4q+3)$ is thus intrinsic to the
binomial structure of the color-tube cubic on Bring's surface.

## Proximity to the golden degeneration threshold

The golden ratio degeneration
([golden ratio degeneration](#rem:golden-ratio-degeneration))
shows that the Descartes elliptic curve $\mathcal{E}_q$ acquires a
node at

$$
q_{\mathrm{gold}} = \frac{1}{\varphi^2} = \frac{3-\sqrt{5}}{2} \approx 0.382.
$$

Evaluating the Möbius limit at the physical substrate parameter gives

$$
a(q_0) = \frac{4 - q_0}{4q_0 + 3} \approx 0.3884.
$$

This value lies close to the golden degeneration point $q_{\mathrm{gold}}
\approx 0.382$, with

$$
a(q_0) - q_{\mathrm{gold}} \approx 0.006.
$$

The baryon period integral thus runs over an interval whose half-width
approximates the distance in parameter space to the elliptic
degeneration.  The $0.0006\%$ proton mass error may encode the
difference between the Möbius approximation (rational in $q$, from
the cubic's binomial coefficients) and the exact degeneration locus
(irrational at $1/\varphi^2$, from the $S_5$ symmetry of Bring's
surface).

## Categorical status

The following ingredients are categorically defined (derived from
$q$ and the Descartes axioms alone, no empirical input):

| Ingredient | Source | Status |
|------------|--------|--------|
| Color-tube cubic $F(z,c)$ | Bring's surface coordinates ($\chi = -6$) | defined |
| Binomial coefficients $\{4,6,4\}$ | $\binom{4}{k}$ from $\dim_{\mathbb{C}} = 4$ | derived |
| Möbius matrix $M$ | $\{-1,4;4,3\}$ from cubic structure | derived |
| Fixed-point equation $q^2+q-1=0$ | From $M$ | derived |
| Golden ratio $\varphi$ | Root of $q^2+q-1$ | derived |
| Degeneration $q_{\mathrm{gold}} = 1/\varphi^2$ | Weierstrass coefficient of $\mathcal{E}_q$ | derived |
| Borromean volume $\mathrm{Vol}(\mathfrak{B}_3)$ | Hyperbolic geometry | derived |

Two points remain open:

- Why the product $\prod_k dc_k/dz$ rather than the sum
  $\sum_k dc_k/dz$ serves as the baryon integrand.  (The product
  gives $0.0006\%$ accuracy; the sum gives a ratio of $\approx 0.99$.)
- Why the Möbius limit $(4-q)/(4q+3)$ rather than the exact
  degeneration locus $1/\varphi^2$ defines the integration domain.
  The Möbius form is rational in $q$ and comes from the cubic's
  coefficients, but a derivation from first principles (a modular
  equation or period relation) is missing.
