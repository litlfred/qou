## The three dihedral angles of a shape

An ideal tetrahedron with shape parameter $z$ in the upper half plane has three dihedral angles, one for each pair of opposite edges, given by the arguments of the three edge parameters:

$$
  \theta_1 = \arg z, \qquad
  \theta_2 = \arg\!\left(\frac{1}{1 - z}\right), \qquad
  \theta_3 = \arg\!\left(1 - \frac{1}{z}\right).
$$

They satisfy $\theta_1 + \theta_2 + \theta_3 = \pi$, which is what makes the angles those of a Euclidean triangle — the link of an ideal vertex.

**Theorem.**
*For every $z$ with $\mathrm{Im}\, z > 0$,*

$$
  \lVert z \rVert \;=\; \frac{\sin\theta_2}{\sin\theta_3} .
$$

The name is apt: the modulus of the shape is a ratio of sines of the opposite angles, exactly as a side of a Euclidean triangle is.

## Why this particular lemma is the one worth isolating

Kummer's identity relates the Bloch–Wigner dilogarithm to a sum of Lobachevsky values. Proved on the unit circle $\lVert z \rVert = 1$, extending it to general $z$ appears to need a genuine two-variable argument, matching

$$
  dD \;=\; \log\lVert z\rVert \; d\arg(1 - z) \;-\; \log\lVert 1 - z\rVert\; d\arg z
$$

against $d\Lambda(\theta) = -\log\lvert 2\sin\theta\rvert \; d\theta$ in both variables at once.

It does not. Fix $\arg z$ and vary only the modulus along a ray. Then $\theta_1$ is *constant*, so $\Lambda(\theta_1)$ contributes nothing to the derivative; the angle sum forces $d\theta_3 = -d\theta_2$; and the two sides become

$$
  \frac{d}{dr}\bigl(\Lambda(\theta_2) + \Lambda(\theta_3)\bigr)
    = \log\!\frac{\sin\theta_3}{\sin\theta_2}\cdot\frac{d\theta_2}{dr},
  \qquad
  \frac{d}{dr} D = -\log r \cdot \frac{d\theta_2}{dr}.
$$

These agree precisely when $r = \sin\theta_2 / \sin\theta_3$ — which is the theorem above. So the law of sines is exactly the statement that converts a two-variable problem into a one-variable one, and the basepoint $r = 1$ is supplied by the already-proved unit-circle case. The general identity then follows in the same "same derivative, pin the constant" shape used elsewhere in this arc.

The form the derivative computation actually consumes is the logarithmic one,

$$
  \log(2\sin\theta_3) - \log(2\sin\theta_2) \;=\; -\log\lVert z\rVert ,
$$

which is the theorem after multiplying both sines by $2$ and taking logarithms.

## The proof is elementary

No analysis is involved. The identity $\sin(\arg x) = \mathrm{Im}\, x / \lVert x \rVert$ for $x \neq 0$ applies directly, since $z$ and $1 - z$ are nonzero on the upper half plane. Applying it to the two edge parameters,

$$
  \sin\theta_2 = \frac{\mathrm{Im}\, z}{\lVert 1 - z\rVert},
  \qquad
  \sin\theta_3 = \frac{\mathrm{Im}\, z}{\lVert z\rVert \cdot \lVert 1 - z\rVert},
$$

and the ratio is $\lVert z \rVert$ on the nose. Both sines are positive on the upper half plane, which is what makes the division safe rather than merely formal.

## A numerical illustration, and a normalization that must be stated

For the $5_2$ knot the shape satisfies a cubic, and $\lVert z \rVert = 1.5247025799\ldots$ agrees with $\sin\theta_2/\sin\theta_3$ to full precision.

That number requires care, because "the $5_2$ shape" is ambiguous. Two cubics for $5_2$ appear in this corpus — $x^3 - x^2 + 1$ and the saddle cubic $y^3 - 2y^2 + 3y - 1$ — related by the Landen map. They generate the *same* field, of discriminant $-23$, but they are not the same polynomial and their roots have different moduli: the upper-half-plane root of the first has modulus $\approx 1.1510$, of the second $\approx 1.5247$. The value quoted above is the saddle-cubic root. A modulus is a property of a chosen root, not of the field, so the normalization has to travel with the number.

## Scope

This is one lemma about one ideal tetrahedron. It is not new mathematics: the ideal-tetrahedron angle structure is Thurston's, and the dilogarithm identities are classical, with the shape-field setting due to Neumann and Zagier. What is supplied here is a complete proof and, more usefully, the observation that the general Kummer identity needs only this one-variable reduction rather than a two-variable argument.

As throughout this arc, nothing here establishes that any triangulation is a triangulation *of* a knot complement — that is Thurston hyperbolisation together with Mostow rigidity, which needs a theory of hyperbolic $3$-manifolds not developed here. No volume conjecture is touched.
