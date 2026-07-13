<!-- FILE_START: localized-knot-intro.md -->
The preceding sections established $q$-torsion as a geometric invariant of the brane tower and showed that the descent-eigenspace mass decomposition natively encodes particle identity as a knot type. We now formally position this within the categorical framework. A *particle at a point* structurally acts as a knot localized at a categorical point of the projective line $\mathbb{P}(V)$. A *bundle* (the physical state at the initial moment) algebraically constitutes a finite collection of such localized knots.

This formalizes the operational bundle scenario: an initial state comprises a finite set of pairs $(p_i, K_i)$ where $p_i \in \mathbb{P}(V)$ and $K_i$ is a knot type. The $q$-torsion identically drives the evolution of these positions across $\mathbb{P}(V) \cong \mathbb{CP}^1$, dictating the mechanical trajectories.
<!-- FILE_END: localized-knot-intro.md -->

<!-- FILE_START: localized-knot.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe carrying the projective line object $\mathbb{P}(V) = G/T$ ([Definition](#def:projective-line-object)). A **localized knot** defines a pair:
$$
  (p, K) \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A^{\mathrm{co}T}) \times \mathrm{Knot}
$$
where:
1. $p \colon \mathbf{1} \to A^{\mathrm{co}T}$ is a categorical point of the projective line ([Definition](#def:categorical-point)).
2. $K$ is a knot type—an equivalence class of smooth embeddings $S^1 \hookrightarrow S^3$ under ambient isotopy.

The pair $(p, K)$ formally designates "the knot $K$ localized at the point $p$ on the base manifold $\mathbb{P}(V)$."

Categorically, $(p, K)$ acts as a section of the *knot sheaf* $\mathcal{K} \to \mathbb{P}(V)$. This functor assigns to each open $U \subseteq \mathbb{P}(V)$ the set of knot types embeddable in the fibre $\mathcal{S}_p \cong \mathbb{CP}^1$ over any $p \in U$. The fibre $\mathcal{S}_p = \pi^{-1}(p)$ strictly carries the knot as a vortex line within the chiral sector decomposition $(\mathfrak{r}, \mathfrak{g}, \mathfrak{b})$.

In the archimedean realisation with $G = \mathrm{SU}(2)$ and $T \cong \mathrm{U}(1)$, the projective line is $\mathbb{P}(V) \cong \mathbb{CP}^1 \cong S^2$, making $p$ a literal point on the Riemann sphere. The knot $K$ natively inhabits the fibre $\mathcal{S}_p \cong \mathbb{CP}^1$—a topological $S^3$ neighborhood rigorously resolved by the blowup.
<!-- FILE_END: localized-knot.md -->

