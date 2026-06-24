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
