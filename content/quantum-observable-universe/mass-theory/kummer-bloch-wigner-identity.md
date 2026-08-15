## Kummer's identity for the Bloch-Wigner dilogarithm

The volume of an ideal tetrahedron admits two expressions: a sum of Lobachevsky values at its three dihedral angles, and a single dilogarithm expression. They agree.

**Theorem.**
*For every $z$ with $\operatorname{Im} z > 0$,*

$$
  D(z)
  \;=\;
  \operatorname{Im}\operatorname{Li}_2(z) \;+\; \log\lVert z\rVert \cdot \arg(1-z) ,
$$

*where $D(z) = \Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3)$ is the Lobachevsky sum over the tetrahedron's dihedral angles.*

## The proof is a rigidity argument, not a computation

The two sides are compared along a ray $r \mapsto rz$. Their difference has vanishing derivative — and the vanishing *is* the law of sines for the ideal tetrahedron, $\lVert z\rVert = \sin\theta_2 / \sin\theta_3$, in disguise. So the difference is constant on the ray. At $r = 1$ the shape lies on the unit circle, where $\log\lVert z\rVert = 0$ and both sides reduce to the Clausen value $\mathrm{Cl}_2$; the constant is therefore zero.

This is why the unit circle carries so much weight in the argument: it is the one place where the identity is visible directly, and the radial derivative transports it everywhere else in the upper half plane.

## What it buys

The identity is the bridge between the *geometric* description of tetrahedral volume — angles, Lobachevsky, additivity over a triangulation — and the *analytic* one, in which volume is an imaginary part of a dilogarithm and the machinery of the five-term identity becomes available. The $5_2$ sum rule lives on the analytic side; the triangulation and gluing equations live on the geometric side; this is the map between them.

**Scope.** The hypothesis $\operatorname{Im} z > 0$ is genuine and not removable: the right-hand side involves $\arg(1-z)$, which jumps across the real axis. On real shapes both sides vanish, but for a different reason — see the flat-tetrahedron statement.
