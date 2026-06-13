The mass $\mathfrak{m}(\varrho)$ of a vortex in any quantum observable universe
([mass identity](#def\:mass-identity)) decomposes as a sum of a descended
holonomy contribution and finitely many transient contributions localised
at the exceptional divisors of the brane boundary
([brane boundary](#def\:brane-boundary)):

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert\mathrm{Hol}_{\nabla_A}(\varrho_0;\mathfrak{G})\bigr\rVert
  + 
  \sum_{i=1}^{N}
  \bigl\lVert\Phi_q(z_i)\bigr\rVert,
$$

where $\Phi_q(z_i)$ is the quantum dilogarithm
([quantum dilogarithm](#cor\:quantum-dilogarithm)) evaluated at the
$i$-th blow-up centre $z_i$, and $\varrho_0$ is the unknot core of $\varrho$.

## Relationship to the proved theorem

The analogous decomposition for morphisms supported along the
*recursive brane tower*
([recursive brane tower](#def\:recursive-brane-tower)) has been proved as
[Topological Decomposition of Mass](#thm\:topological-mass). That theorem
uses the :refterm[descent]{#descent} involution $\hat\tau_n$ and Frobenius categorical traces
to split $\mathfrak{m}(\varrho)$ into descended and transient parts.

The present conjecture concerns the *vortex* case: $\varrho$ is a
**closed cycle** whose support does not necessarily factor through
a finite brane-tower extension. The holonomy $\mathrm{Hol}_{\nabla_A}$
along $\varrho_0$ (the flat gauge-field holonomy of the base-level connection)
replaces the :refterm[descent]{#descent}-trace part, while the quantum-dilogarithm sum
captures the transient blow-up contributions at the exceptional divisors of
the brane boundary $\partial A$.

## Proof obligations

1. **Holonomy–trace identification.** Show that
 $\bigl\lVert\mathrm{Hol}_{\nabla_A}(\varrho_0;\mathfrak{G})\bigr\rVert = \bigl\lVert\mathrm{tr}_{\mathrm{desc}}(\varrho_0)\bigr\rVert$
 when $\varrho_0$ is an unknot core. This requires identifying the
 gauge holonomy with the categorical :refterm[descent]{#descent} trace for morphisms in
 the unknot class.

2. **Finite blow-up locus.** Prove that the brane boundary
 $\partial A$ has only finitely many exceptional divisors
 $\{D_i\}_{i=1}^N$ contributing non-by definition to $\mathfrak{m}(\varrho)$.
 (For a vortex, $N$ is determined by the genus of $\varrho$'s brane.)

3. **Quantum-dilogarithm evaluation.** Show that the transient
 contribution at $D_i$ equals $\bigl\lVert\Phi_q(z_i)\bigr\rVert$,
 where $z_i = |\hat{V}_i(q)|$ is the algebraic-volume magnitude of
 the generator at the $i$-th blow-up centre.
