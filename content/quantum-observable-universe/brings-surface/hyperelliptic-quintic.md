*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $\mathcal{X}_5$ denote the smooth projective completion of the
affine curve

$$
  \mathcal{X}_5 \colon y^2 =  x^5 - 1
  \qquad
  \text{in } \mathbb{A}^2(\mathbb{C}),
$$

viewed as a double cover of $\mathbb{P}^1$ via the projection
$(x, y) \mapsto x$.  Writing $\zeta_5 =  e^{2\pi i/5}$ for a
primitive fifth root of unity, the ramification locus of this
double cover consists of the six branch points

$$
  \{x_0, x_1, x_2, x_3, x_4, \infty\}  =
   \{1, \zeta_5, \zeta_5^2, \zeta_5^3, \zeta_5^4, \infty\},
$$

five of them distributed symmetrically on the unit circle and the
last at infinity.  By Riemann--Hurwitz the genus of $\mathcal{X}_5$
is

$$
  g(\mathcal{X}_5)  =  \frac{6 - 2}{2}  =  2,
$$

so $\mathcal{X}_5$ is a hyperelliptic Riemann surface of genus $2$
in the Bolza family \cite{bolza1887}.  Its hyperelliptic involution
is $\iota \colon (x, y) \mapsto (x, -y)$.

**Relation to Bring's surface.**  The coordinate $x$ on
$\mathcal{X}_5$ is a $\mathbb{Z}_5$-equivariant observable
identified with the first Lagrange resolvent
$w_1$ of [prop:lagrange-resolvent-transform](#prop:lagrange-resolvent-transform),
restricted to the cyclic subgroup
$\mathbb{Z}_5 \subset S_5$ of [Bring's surface](#def:brings-surface).
Under this identification the five branch points $\zeta_5^k$ are
the five cyclic images of a single $\mathbb{Z}_5$-orbit.
