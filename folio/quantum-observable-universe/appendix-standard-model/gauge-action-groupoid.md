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

The action functional is the datum through which the categorical Lagrangian governs the gauge symmetry: $\mathrm{act}(f)$ records the action cost mandated by [the categorical action](#def:categorical-action) for executing the deformation $f$. Reversibility of gauge transformations is exactly the groupoid axiom; the base ring $R$ stays generic, with the archimedean specialisation $R = \mathbb{R}$ deferred to the observable side of the Archimedean boundary.
