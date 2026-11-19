## Thurston volume additivity

Every hyperbolic knot complement admits an ideal triangulation by tetrahedra with vertices on the sphere at infinity. A single complex shape parameter $z_i$ determines each tetrahedron up to isometry.

**Proposition.**
*The hyperbolic volume of the knot complement $S^3 \setminus \mathcal{K}$ is the sum of its tetrahedral volumes:*

$$
  V(\mathcal{K})
  \;=\;
  \sum_{i = 1}^N D(z_i),
$$

*where $D(z_i)$ is the Bloch-Wigner dilogarithm evaluated at the shape parameter. Flat tetrahedra ($z_i \in \mathbb{R}$) contribute zero volume.*

The sum does not depend on the ideal triangulation chosen. More generally, for any representation $\rho\colon \pi_1(M) \to \mathrm{Isom}^+(\mathbb{H}^3)$ of a cusped orientable 3-manifold $M$, the volume of $\rho$ is well defined and equals the volume obtained by straightening any ideal triangulation of $M$ \cite[\S2]{francaviglia2003}.

## Braid-theoretic consequence

A knot diagram induces an ideal triangulation containing one tetrahedron per crossing. Consequently, the volume sums additively over crossings:

$$
  V(\mathcal{K}) \;=\; \sum_{\text{crossings } c} D(z_c).
$$

Torus knots project entirely onto a surface, forcing every $z_c$ to be real. Their hyperbolic volume vanishes identically.

## Extremality

The Bloch-Wigner function reaches its maximum at the regular shape $z = e^{i\pi/3}$, yielding the Lobachevsky constant $v_3 \approx 1.01494$. The figure-eight knot $4_1$ comprises exactly two such tetrahedra, producing the minimum hyperbolic volume $V(4_1) = 2 v_3 \approx 2.02988$. This extremality pins the aether parameter $q_0$ by calibrating the quantum of action $\hbar_q^2$.
