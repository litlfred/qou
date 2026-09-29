## Flat tetrahedra contribute nothing

An ideal tetrahedron with shape parameter $z$ has volume $D(z)$, the Bloch-Wigner dilogarithm. The tetrahedron is *degenerate*, or **flat**, exactly when $z$ is real: its four ideal vertices $0, 1, \infty, z$ then lie on a common circle on the sphere at infinity, and it collapses.

**Theorem.**
*For every real $x$,*

$$
  D(x) \;=\; 0 .
$$

*No hypothesis on $x$ is required.*

## Why the unrestricted form is the one worth stating

Writing $D$ in the Lobachevsky form $D(z) = \Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3)$, where the $\theta_i$ are the arguments of the three edge parameters, the proof is immediate: the edge parameters of a real shape are themselves real, the argument of a real number is $0$ or $\pi$, and $\Lambda$ vanishes at both.

That argument never uses the size of $x$, and the unrestricted statement matters. A version restricted to $0 < x < 1$ — the range in which all three edge parameters have the most obvious signs — is strictly weaker, and too weak for the application in the next block: the trefoil's shape parameters are $-1$ and $2$, both outside that interval. The vanishing must hold on all of $\mathbb{R}$ or it does not reach the case it is wanted for.

The two degenerate values are covered as well. At $x = 1$ the second edge parameter $1/(1-x)$ is undefined, and at $x = 0$ the third, $1 - 1/x$; under the convention $1/0 = 0$ both evaluate to a real number with argument $0$, so the formula returns $0$ there too.

## Consequence

Volume is additive over an ideal triangulation, so a triangulation whose shape parameters are *all* real has total volume zero. This is the mechanism behind the vanishing of hyperbolic volume for torus knots, and it is used in that form in the block that follows.
