## The summand is not concave; the constrained sum is

An ideal tetrahedron with dihedral angles $\alpha, \beta, \gamma$ satisfying $\alpha + \beta + \gamma = \pi$ has volume

$$
  \Lambda(\alpha) + \Lambda(\beta) + \Lambda(\gamma),
$$

where $\Lambda$ is the Lobachevsky function. Rivin's theorem is that the total volume is *strictly concave* on the space of angle structures.

The obvious route to that conclusion does not exist. Differentiating twice gives

$$
  \Lambda''(\theta) \;=\; -\cot\theta ,
$$

so $\Lambda$ is concave on $(0, \pi/2)$ and **convex** on $(\pi/2, \pi)$. Any argument that proves concavity of the sum by proving it termwise is therefore not merely incomplete but false at the second step, and a tetrahedron with an obtuse dihedral angle is not an edge case — it is generic.

What rescues the statement is the constraint. Concavity holds for the sum *on the simplex* $\alpha + \beta + \gamma = \pi$, and the constraint is doing the work, not decoration.

**Theorem.**
*Let $\alpha, \beta, \gamma > 0$ with $\alpha + \beta + \gamma = \pi$, and let $(u, v, w) \neq 0$ satisfy $u + v + w = 0$. Then $\Lambda(\alpha + tu) + \Lambda(\beta + tv) + \Lambda(\gamma + tw)$ is strictly concave in $t$ on the region where all three angles stay positive.*

Strict concavity on a convex set is exactly strict concavity along every segment, so the line formulation is Rivin's theorem for a single tetrahedron rather than a weakening of it. The tangency condition $u + v + w = 0$ is what keeps the angles summing to $\pi$ along the whole line,

$$
  (\alpha + tu) + (\beta + tv) + (\gamma + tw) \;=\; \pi + t\,(u + v + w) \;=\; \pi ,
$$

so the constraint that makes the result true at the basepoint is available at every point of the line.

## The Hessian, and why no case split is needed

The Hessian of $\Lambda(\alpha) + \Lambda(\beta) + \Lambda(\gamma)$ is $\mathrm{diag}(-\cot\alpha, -\cot\beta, -\cot\gamma)$. Restricted to the tangent space $\{u + v + w = 0\}$, negative definiteness of the Hessian is precisely the positivity of

$$
  Q \;=\; \cot\alpha\;u^2 + \cot\beta\;v^2 + \cot\gamma\;w^2 .
$$

At most one of three angles summing to $\pi$ can exceed $\pi/2$, so at most one of the three cotangents is negative — but which one is not known in advance, and a proof by cases on that would need three branches plus the boundary.

None is required, because $Q$ is a sum of squares after clearing denominators. Writing $a = \cot\alpha$, $b = \cot\beta$ and $w = -(u + v)$,

$$
  (a + b)\,Q \;=\; (a\,u - b\,v)^2 + (u + v)^2 ,
$$

an identity in $\alpha, \beta, u, v$ alone once $\gamma = \pi - \alpha - \beta$ is substituted. The prefactor is positive:

$$
  a + b \;=\; \frac{\cos\alpha\,\sin\beta + \sin\alpha\,\cos\beta}{\sin\alpha\,\sin\beta} \;=\; \frac{\sin\gamma}{\sin\alpha\,\sin\beta} \;>\; 0 ,
$$

since all three angles lie in $(0, \pi)$ and so have positive sines. The right-hand side vanishes only when $a\,u = b\,v$ and $u = -v$ simultaneously, which for positive $a + b$ forces $u = v = 0$. Hence $Q > 0$ for every nonzero tangent vector, with no case analysis on which angle is obtuse: the identity absorbs it.

The formalization states the identity in the equivalent denominator-free form

$$
  Q\,\sin\alpha\,\sin\beta\,\sin\gamma \;=\; (\cos\alpha\,\sin\beta\;u - \sin\alpha\,\cos\beta\;v)^2 + (\sin\alpha\,\sin\beta)^2\,(u + v)^2 ,
$$

which is the previous line multiplied through by $(\sin\alpha\,\sin\beta)^2$. In that form the proof is `field_simp; ring` — no analysis at all.

## What is proved here, and what is not

The analytic input is the second derivative $\Lambda'' = -\cot$, which is what makes $Q$ a statement about the Hessian rather than about a quadratic form merely asserted to be one. Mathlib has neither the Clausen nor the Lobachevsky function, so both come from the corpus.

Three limits are worth stating plainly.

This is **concavity for a single tetrahedron**. Rivin's theorem for a triangulation is the sum over its tetrahedra, on the space of angle structures cut out by the edge conditions; that assembly is not carried out here.

This is **not new mathematics**. The concavity is Rivin's, the volume formula Thurston's and Milnor's. What the corpus adds is a machine-checked proof of the one-tetrahedron case, and the observation — recorded here because it is the trap the formalization was built to avoid — that the termwise route is unavailable.

And as elsewhere in this arc, nothing here establishes that any given triangulation is a triangulation *of* a knot complement. That is Thurston hyperbolisation together with Mostow rigidity, which needs a theory of hyperbolic $3$-manifolds that neither Mathlib nor this corpus has. No volume conjecture is touched.
