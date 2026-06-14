**Proposition.**
Let $R$ be the categorical ground ring, $V$ the fundamental object,
and $\mathbb{P}(V)$ the projective line object
([projective line object](#def:projective-line-object)) with two
affine charts $U_0, U_1$ and intersection $U_0 \cap U_1 \cong \mathbb{G}_m$.
Let $\iota \in \mathrm{Aut}_R(U_0 \cap U_1)$ be the chart-swap
involution $z \mapsto z^{-1}$ ($\iota^2 = \mathrm{id}$), and let $T_p$
denote the tangent space at a fixed point $p$ of $\iota$.

The **categorical-coordinate ring** of the chart-transition data of
the deformation family $(\mathbb{P}_q(V))_{q \in R^\times}$ is

$$
  R[i, q^{\pm 1}]
   \;=\;
  R[q, q^{-1}][i] / (i^2 + 1),
$$

characterised by the universal property:
$R[i, q^{\pm 1}]$ is the smallest $R$-algebra extension $S \supseteq R$
such that

1. $q \in S^\times$ (the chart-transition coefficient $z\,w = q^{-1}$
   is a unit in $S$);
2. The tangent representation $\rho_p(\iota) = -1 \in \mathrm{End}_R(T_p)$
   admits a square root in $S$:  there exists $i \in S$ with $i^2 = -1$.

Under this identification, the chart-transition automorphism group
factors as the semidirect product

$$
  \mathrm{Aut}_{R[i, q^{\pm 1}]}(U_0 \cap U_1, \mathbb{P}_q(V))
   \;\cong\;
   \langle q \rangle  \rtimes  \langle \iota \rangle,
$$

with $\mathbb{Z}_2 = \langle \iota \rangle$ acting on the cyclic
subgroup $\langle q \rangle \subset R^\times$ by inversion
$q \mapsto q^{-1}$.

**Mathematical Novelty.** While the construction of $R[q, q^{-1}][i]/(i^2+1)$ is routine commutative algebra, its mathematical novelty here is that this specific elementary ring is proven to universally parameterise the chart-transition data of the quantum projective line. Instead of taking the deformation parameter $q$ and the imaginary unit $i$ as externally posited constants, this algebraic derivation strictly recovers them as the unavoidable geometric consequences of requiring chart-transition invertibility and chart-swap reflection within the non-commutative coordinate algebra.

*Proof.*
Existence: $S = R[q, q^{-1}][i]/(i^2+1)$ visibly satisfies (1) by
construction of the Laurent polynomial ring and (2) via $i = $ image
of the polynomial generator.  The semidirect-product factorisation
follows from $\iota \cdot z \cdot \iota^{-1} = z^{-1}$ on
$\mathbb{G}_m$, which transports through the quantum-plane relation
$y x = q\, x y$ to give $\iota \cdot q \cdot \iota^{-1} = q^{-1}$
on the chart-transition coefficient.

**Why semidirect, not direct.**  Composing the three maps in the
chart-transition group on the affine coordinate $z$:

$$
  z  \;\xrightarrow{\iota^{-1}}\;  z^{-1}
   \;\xrightarrow{q\,\cdot}\;  q z^{-1}
   \;\xrightarrow{\iota}\;  (q z^{-1})^{-1}
   \;=\;  q^{-1} z,
$$

so $\iota \cdot q \cdot \iota^{-1} = q^{-1}$.  The chart-swap inverts
the scaling parameter — a non-trivial $\mathbb{Z}_2$ action on
$\langle q \rangle$ — forcing the *semi*direct (not direct) product.
Equivalent reading: $q$ and $q^{-1}$ are the two eigenvalues of the
braiding ($\lambda_+ = q$, $\lambda_- = -q^{-1}$), and the chart-swap
is exactly the involution exchanging them
([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention)).

The same semidirect persists in the commutative limit: in
$R[i, q^{\pm 1}]$ the chart-swap acts on the $i$-generator by

$$
  \iota \cdot i \cdot \iota^{-1}  \;=\;  -i,
$$

since the Galois action $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$ on
$\pm i$ coincides with the chart-swap $\mathbb{Z}_2$ (one
$\mathbb{Z}_2$, three faces — chart-swap, Galois, braiding orientation
— per [rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).

Universality: any $R$-algebra $S$ satisfying (1) and (2) admits a
unique $R$-algebra homomorphism $R[q, q^{-1}] \to S$ sending the
Laurent generator to the chosen $q \in S^\times$ (universal property
of Laurent polynomials), and a unique extension to
$R[q, q^{-1}][i]/(i^2 + 1) \to S$ sending $i$ to the chosen square
root (universal property of polynomial-ring quotients).

The two structural pieces — invertible scaling generator and
square root of involution-eigenvalue — are exactly the data
recorded by the affine-chart-origin remark
([rem:affine-chart-origin-of-i-and-q](#rem:affine-chart-origin-of-i-and-q)).  $\square$

**Specialisations.**

| Specialisation | Resulting ring | Interpretation |
|----------------|---------------|----------------|
| $q \mapsto 1$, $R = \mathbb{C}$ | $\mathbb{C}$ (as $i \in \mathbb{C}$) | Archimedean commutative limit |
| $q \mapsto 1$, $R = \mathbb{R}$ | $\mathbb{C} = \mathbb{R}[i]$ | Smallest archimedean ring with $i$ |
| $q \mapsto e^{2\pi i/N}$, $R = \mathbb{C}$ | $\mathbb{C}$ | Root-of-unity (anyonic) limit |
| Universal $R = \mathbb{Z}$ | $\mathbb{Z}[i, q, q^{-1}]$ | Lusztig integral form with $i$ |

**Relation to existing structure.**  The proposition is a
*structural* statement: it does not add new categorical content
beyond ([rem:affine-chart-origin-of-i-and-q](#rem:affine-chart-origin-of-i-and-q))
but pins down the universal $R$-algebra extension that makes the
informal categorical-coordinate principle precise.  The convention
$q := \lambda_+$ ([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention))
fixes which Laurent generator is named $q$; the sign of $i$ is
fixed by the braiding orientation
([rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).
