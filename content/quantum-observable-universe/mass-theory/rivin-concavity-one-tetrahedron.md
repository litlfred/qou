## Concavity of the volume functional

Casson and Rivin's approach to hyperbolic structures replaces the search for shape parameters with a *maximisation*: an angle structure assigns three positive dihedral angles summing to $\pi$ to each tetrahedron, subject to the linear condition that angles around each edge sum to $2\pi$; the hyperbolic structure is the critical point of the total volume on that polytope. The argument needs the volume functional to be concave, or the critical point carries no information.

**Theorem.**
*Let $\alpha + \beta + \gamma = \pi$ and let $(u,v,w)$ be a nonzero tangent direction with $u + v + w = 0$. Then*

$$
  t \;\longmapsto\; \Lambda(\alpha + tu) + \Lambda(\beta + tv) + \Lambda(\gamma + tw)
$$

*is strictly concave.*

Strict concavity on a convex set is exactly strict concavity along every segment, so this is Rivin's theorem for a single tetrahedron.

## The Hessian is computed, not assumed

The proof is via the second derivative, and both derivatives of the Lobachevsky function are established rather than quoted:

$$
  \Lambda'(t) \;=\; -\log\lvert 2\sin t\rvert ,
  \qquad
  \Lambda''(t) \;=\; -\cot t .
$$

So along the line the second derivative is $-(u^2\cot\alpha + v^2\cot\beta + w^2\cot\gamma)$, and strict negativity is a statement about that quadratic form. The quadratic form **is** the Hessian, derived, rather than a form asserted to be one. With $\alpha + \beta + \gamma = \pi$ and all three angles in $(0,\pi)$, at most one cotangent is negative, and the constraint $u+v+w=0$ is what forces the combination negative.

## What is not claimed

This is concavity for **one** tetrahedron along **one** line. Rivin's full theorem — that the total volume over an angle-structure polytope has a unique critical point, and that the critical point is the complete hyperbolic structure — additionally needs the polytope itself, a compactness argument, and the identification of the critical point with a geometric structure. None of that is established here, and the angle-structure polytope for $5_2$ is not built.
