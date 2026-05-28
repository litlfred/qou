**Remark (anyon ladder under the observation functor).**
*The three preceding conjectures organise into a single ladder
indexed by the deformation parameter $q$:*

| $q$ regime | Substrate state | Observation image |
|---|---|---|
| Generic $q$ ([anyonic substrate](#conj:hecke-anyonic-substrate)) | Abelian anyons in $H_n(R, q)$ | Topological braiding matrices |
| $q = e^{2\pi i / k}$ ([MTC truncation](#conj:root-of-unity-mtc-truncation)) | Non-abelian anyons in $\mathrm{MTC}_k$ | Finite fusion / $F$- and $R$-matrices |
| $q \to 1$ ([KL classical limit](#conj:kazhdan-lusztig-classical-limit)) | Symmetric-group representations | Pauli ($\pm 1$) statistics |

*Reading the ladder downwards is the
[observation functor](#def:observation) $\tau$ acting on a cooling
substrate: anyonic braiding loses information at each step but never
abandons the categorical algebraic substrate.  The
[Kashiwara crystal traversals](#conj:crystal-graph-realization) used
elsewhere in the chapter to compute pair production and stable
masses are mapping the fusion rules of the appropriate rung — the
generic Hecke fluid for high-energy interactions, $\mathrm{MTC}_k$
for topologically ordered phases, and $\mathbb{Z}[S_n]$ for the
classical-statistics regime accessed by macroscopic detectors.*

**Algorithmic synthesis.**
*The reduction engine selects the rung by the value of $q$ supplied
to the substrate: generic for the open-ended Hecke evaluation, root
of unity for fusion-category enumeration, and $q \to 1$ for the
Pauli/Bose decomposition.  The same canonical-basis machinery
applies at every rung; only the specialisation map changes.*
