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

**Adelic-assembly perspective (preferred reading).** Equivalently,
$\mathcal{L}$ is the **archimedean component** of the realization
tower $\{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}$ of the
[motivic substrate](#def:motivic-substrate). Under this reading,
the substrate $\mathbf{C}_q$ is the universal motive over
$\widehat{\mathcal{M}}$; each finite place $p$ of
$\mathbb{Q}$ ([adelic substrate](#def:adelic-substrate)) carries a
local realization $\rho_p$ landing in $\mathbb{Q}_p$ (cyclotomic /
Kummer-level data, equivalently Habiro-ring evaluations at roots of
unity); the archimedean place $v = \infty$ carries
$\rho_\infty = \mathcal{L}$, landing in $\mathbb{R}$. The
"$q \to 1$" limit and the "$\hbar_q \to 0$" collapse are the
**vanishing of the local Reeb infinitesimal $\varepsilon_\infty$
at the archimedean place** ([adelic Tate squeeze](#rem:adelic-tate-squeeze));
the classical continuum is what remains after that single local
$\varepsilon_v$ is collapsed, while the non-archimedean $\varepsilon_p$'s
are simply discarded.

**Why $\mathcal{L}$ is not full: phase decoherence.** The full
motivic class $[X] \in \widehat{\mathcal{M}}$ carries the relative
$q$-phases between all finite places — the cohomological data that
the cyclotomic-projection tower
$\{\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_N(q)\}_N$ records.
The archimedean projection $\rho_\infty$ collapses across all those
phases, retaining only the standard-part / real-valued shadow.
That is the rigorous mechanism behind "quantum information is lost":
the relative finite-place phases are traced out in the assembly
$\mathcal{L} = \rho_\infty \circ (\text{motivic lift})$, even though
each individual $\rho_v$ is exact. The classical continuum is a
**low-resolution shadow** of the unglued adelic motives, not a
limit of the full structure.

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
