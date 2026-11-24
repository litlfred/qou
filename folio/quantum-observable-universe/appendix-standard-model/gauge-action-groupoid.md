Let $R$ be an additive abelian group of action values. A **gauge action groupoid** over $R$ is a groupoid $\mathbf{G}$ — objects the *topological states* (knot and braid configurations), morphisms the *gauge transformations* (reversible deformations, braiding operations, cobordism moves) — equipped with an action functional

$$
  \mathrm{act} \colon \mathrm{Hom}_{\mathbf{G}}(X, Y) \to R
$$

satisfying, for all states $X, Y, Z$ and composable gauge transformations $f \colon X \to Y$ and $g \colon Y \to Z$,

$$
  \mathrm{act}(\mathrm{id}_X) = 0,
  \qquad
  \mathrm{act}(g \circ f) = \mathrm{act}(f) + \mathrm{act}(g).
$$

Two states $X, Y$ are **gauge equivalent** when $\mathrm{Hom}_{\mathbf{G}}(X, Y) \neq \emptyset$.
