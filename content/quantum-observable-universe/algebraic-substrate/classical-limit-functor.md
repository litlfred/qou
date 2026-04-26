Define the classical limit as a monoidal functor

$$
\mathcal{L} : \mathbf{C}_q \longrightarrow \mathbf{C}_1
$$

from the braided monoidal category $\mathbf{C}_q$ (at deformation
parameter $q$) to the symmetric monoidal category $\mathbf{C}_1$
(at $q = 1$). The functor $\mathcal{L}$ acts on the substrate
algebra by:

1. **Quantum gap collapse**: $\hbar_q = 1 - q^{-1} \to 0$, so that
   the non-commutativity vanishes.
2. **Differential smoothing**: The Jackson $q$-derivative
   $d_q f(z) = \frac{f(qz) - f(z)}{(q-1)z}$ converges to the
   ordinary derivative $\frac{df}{dz}$.
3. **Braiding trivialization**: The braiding
   $\sigma_{X,Y} : X \otimes Y \to Y \otimes X$ specializes to the
   symmetric swap $\tau_{X,Y}$, since $R(q) \to \mathrm{id}$ as
   $q \to 1$.

The functor $\mathcal{L}$ is exact (preserves short exact sequences)
but **not** full: quantum information is lost in the limit.

**Topology-free reformulation (forward reference).** This
definition uses a *topological* $q \to 1$ limit on the parameter
space, which has obstructions
([classical limit obstruction](#def:classical-limit-obstruction))
and breaks for surreal-valued $q$. The appendix replaces it with
a literal evaluation in Conway's surreal field at
$q = 1 + \varepsilon$, then takes standard-part:

- At the **single-functor** level —
  $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$
  ([classical limit as standard-part](#conj:classical-limit-stpart)).
- At the **whole-tuple** level — the entire QOU
  $(\mathbf{C}, \varTheta, G, \mathcal{S})$ is the standard-part of
  an $\varepsilon$-relaxed surreal QOU
  ([archimedean QOU is standard-part of surreal](#conj:archimedean-stpart),
  with [proof strategy](#rem:archimedean-stpart-strategy)).

Both replacements are conjectural; if either holds it removes the
need for any analytic / topological machinery on the parameter
space.
