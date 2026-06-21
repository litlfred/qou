*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The mechanism is as follows.  The universal $R$-matrix
$\mathcal{R} \in \mathcal{U}_q(\mathfrak{su}(2)) \hat{\otimes} \mathcal{U}_q(\mathfrak{su}(2))$
([Remark](#rem:r-matrix-braiding)) controls the failure of the
cocommutativity square

$$
  \sigma \circ \Delta  \neq  \Delta,
$$

where $\sigma$ is the tensor swap.  At $q = 1$ one has
$\mathcal{R} = 1 \otimes 1$ and the comultiplication is
cocommutative, so strands may pass through each other freely (the
"classical" regime where self-intersection is not penalised by the
energy functional).

For $q \neq 1$, by
([$q$-deformed kernel with hard singularity](#lem:nsi-q-deformed-kernel)),
the classical $1/r^2$ repulsion kernel is replaced by
$[2]_q / (\lvert \varrho(s) - \varrho(t) \rvert^2 - \hbar_q^2)$,
which has a hard singularity at $\lvert \varrho(s) - \varrho(t) \rvert
= \hbar_q$, creating an energy barrier of infinite height at the
quantum scale.

Physically, the $R$-matrix endows the vortex filament $\varrho$ with
a "quantum exclusion zone" of radius $\hbar_q$: the filament cannot
pass through itself because doing so would require infinite
categorical energy.  This is the knot-theoretic analogue of the
Pauli exclusion principle, with the non-cocommutativity of
$\Delta_q$ playing the role of fermionic statistics.  $\square$
