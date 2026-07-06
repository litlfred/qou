The Markov trace is built algebraically as a trace on the Hecke quotient of the braid-group algebra ([Jones--Markov trace](#thm:jones-markov-trace)). Yet the invariant it computes is topological: an invariant of an oriented link embedded in the three-sphere $S^3$. The ambient $S^3$ is never posited as a separate object. It enters precisely through the closure construction via two classical theorems.

**Alexander's theorem** ($1923$). The closure map
$$
  \widehat{\,\cdot\,} \colon \coprod_{n \ge 1} B_n
    \;\longrightarrow\; \{\text{oriented links in } S^3\}/\text{isotopy},
  \qquad \beta \mapsto \widehat{\beta},
$$
is surjective: every oriented link in $S^3$ is the closure of some braid. The disjoint union of braid groups already exhausts the link types of the ambient three-sphere.

**Markov's theorem** ($1936$). Two braids have isotopic closures in $S^3$, $\widehat{\beta} \cong \widehat{\beta'}$, if and only if $\beta$ and $\beta'$ are connected by a finite sequence of Markov moves: conjugation $\beta \mapsto \gamma\beta\gamma^{-1}$ within a fixed $B_n$, and stabilisation $\beta \mapsto \beta\,\sigma_n^{\pm 1}$ across the inclusion $B_n \hookrightarrow B_{n+1}$. These two moves generate exactly the kernel of the closure map.

The Markov trace is invariant under both moves. The cyclic trace property $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ yields conjugation invariance. The Markov property $\mathrm{tr}_M(x\,\sigma_n^{\pm 1}) = z^{\pm 1}\,\mathrm{tr}_M(x)$ provides controlled behaviour under stabilisation (which is absorbed into the standard writhe/index normalisation of $J_K(q)$). Combining these facts:

> Because closure maps onto the links of $S^3$ (Alexander), its fibres form exactly the Markov-move orbits (Markov), and $\mathrm{tr}_M$ is constant on those orbits, the Markov trace descends to a well-defined function on isotopy classes of links in $S^3$. The ambient three-sphere manifests in the categorical data not as an extra datum, but as the target of the Alexander--Markov correspondence. The closure construction $\beta \mapsto \widehat{\beta}$ is the categorical encoding of "the link sits in $S^3$."

This categorically locates the $S^3$ that the archimedean layer relies on to compute a hyperbolic volume for a knot complement $S^3 \setminus K$. That $S^3$ is the Alexander--Markov base manifold, recovered from the substrate-level Markov trace. We assume no geometric realisation upstream of it.

**A distinction to keep.** This ambient $S^3$—the base manifold whose links are the closures and whose complements carry the hyperbolic volumes—is not the group manifold $\mathrm{SU}(2) \cong S^3$ that furnishes the braiding $R$-matrix (nor its $q$-deformation, the quantum three-sphere underlying $\mathrm{SU}_q(2)$). The diffeomorphism $\mathrm{SU}(2) \cong S^3$ is a low-dimensional coincidence. The ambient three-sphere is fixed by the closure construction, not by the gauge group. Conflating the two is a category error. The base manifold and the structure group remain independent. In Chern--Simons theory, the empty-link invariant of $(S^3, \varnothing)$ is the vacuum partition function, and the gauge group enters only through the representation category.
