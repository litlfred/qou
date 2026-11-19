*Proof.*
Existence: $S = R[q, q^{-1}][i]/(i^2+1)$ visibly satisfies (1) by
construction of the Laurent polynomial ring and (2) via $i = $ image
of the polynomial generator.  The semidirect-product factorisation
follows from $\iota \cdot z \cdot \iota^{-1} = z^{-1}$ on
$\mathbb{G}_m$, which transports through the quantum-plane relation
$y x = q\, x y$ to give $\iota \cdot q \cdot \iota^{-1} = q^{-1}$
on the chart-transition coefficient.

**Semidirect versus direct structure.**  Composing the three maps in the
chart-transition group on the affine coordinate $z$:

$$
  z  \;\xrightarrow{\iota^{-1}}\;  z^{-1}
   \;\xrightarrow{q\,\cdot}\;  q z^{-1}
   \;\xrightarrow{\iota}\;  (q z^{-1})^{-1}
   \;=\;  q^{-1} z,
$$

so $\iota \cdot q \cdot \iota^{-1} = q^{-1}$.  The chart-swap inverts
the scaling parameter (a non-trivial $\mathbb{Z}_2$ action on
$\langle q \rangle$), forcing the *semi*direct (rather than direct) product.
Equivalent reading: $q$ and $q^{-1}$ are the two eigenvalues of the
braiding ($\lambda_+ = q$, $\lambda_- = -q^{-1}$), and the chart-swap
is the involution exchanging them
([the unit-circle convention for the braiding eigenvalue](#rem:braiding-unit-circle-convention)).

The same semidirect structure persists in the commutative limit: in
$R[i, q^{\pm 1}]$ the chart-swap acts on the $i$-generator by

$$
  \iota \cdot i \cdot \iota^{-1}  \;=\;  -i,
$$

since the Galois action $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$ on
$\pm i$ coincides with the chart-swap $\mathbb{Z}_2$ (one
$\mathbb{Z}_2$ with three faces: chart-swap, Galois, and braiding orientation,
per [the imaginary unit $i$ as braiding-orientation datum](#rem:i-as-braiding-orientation)).

Universality: any $R$-algebra $S$ satisfying (1) and (2) admits a
unique $R$-algebra homomorphism $R[q, q^{-1}] \to S$ sending the
Laurent generator to the chosen $q \in S^\times$ (universal property
of Laurent polynomials), and a unique extension to
$R[q, q^{-1}][i]/(i^2 + 1) \to S$ sending $i$ to the chosen square
root (universal property of polynomial-ring quotients).

The two structural pieces (invertible scaling generator and
square root of involution-eigenvalue) are the data
recorded by the affine-chart-origin remark
([affine-chart origin of the categorical coordinates $i$ and $q$](#rem:affine-chart-origin-of-i-and-q)).  $\square$

**Specialisations.**

| Specialisation | Resulting ring | Interpretation |
|----------------|---------------|----------------|
| $q \mapsto 1$, $R = \mathbb{C}$ | $\mathbb{C}$ (as $i \in \mathbb{C}$) | Archimedean commutative limit |
| $q \mapsto 1$, $R = \mathbb{R}$ | $\mathbb{C} = \mathbb{R}[i]$ | Smallest archimedean ring with $i$ |
| $q \mapsto e^{2\pi i/N}$, $R = \mathbb{C}$ | $\mathbb{C}$ | Root-of-unity (anyonic) limit |
| Universal $R = \mathbb{Z}$ | $\mathbb{Z}[i, q, q^{-1}]$ | Lusztig integral form with $i$ |

**Relation to existing structure.**  The proposition is a
*structural* statement: it does not add new categorical content
beyond ([affine-chart origin of the categorical coordinates $i$ and $q$](#rem:affine-chart-origin-of-i-and-q))
but pins down the universal $R$-algebra extension that makes the
informal categorical-coordinate principle precise.  The convention
$q := \lambda_+$ ([the unit-circle convention for the braiding eigenvalue](#rem:braiding-unit-circle-convention))
fixes which Laurent generator is named $q$; the sign of $i$ is
fixed by the braiding orientation
([the imaginary unit $i$ as braiding-orientation datum](#rem:i-as-braiding-orientation)).
