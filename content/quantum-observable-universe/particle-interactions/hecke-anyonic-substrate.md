**Theorem (Iwahori–Hecke substrate is the anyon algebra; structural-existence, Sprint 2 follow-up discharge).**
*Let $K$ be a closed braid representing a QOU particle, and let
$T_w \in H_n(R, q)$ be its [Hecke normal form](#def:hecke-normal-form)
at generic deformation parameter $q$. Then the topological statistics
of $K$ are governed by the braid group $B_n$ acting on $T_w$ through
the surjection $B_n \twoheadrightarrow H_n(R, q)$ given by
$\sigma_i \mapsto T_{s_i}$ modulo the Hecke quadratic relation*

$$
  (T_{s_i} - q)(T_{s_i} + 1) = 0.
$$

*That is, every particle in the QOU substrate is an anyon
\cite{kitaev2006, nayak2008}: the wavefunction picks up a topological
braiding matrix rather than a $\pm 1$ permutation sign when two
particles are exchanged. Bosonic and fermionic statistics are not
fundamental; they are the image of anyonic braiding under the
[observation functor](#def:observation) $\tau$.*

**Algorithmic role.**
*The reduction engine treats every transition as a braid-group element
acted on by $H_n(R, q)$ via $\sigma_i \mapsto T_{s_i}$, with no
$\pm 1$ shortcut available at intermediate steps. At generic $q$ the
braid matrices accumulate genuine topological information; only the
trace under $\tau$ collapses them onto a $\pm 1$ statistic.*

**Conjectural status.**
*The braid–Hecke surjection and the standard Schur–Weyl-style
identification of $H_n(q)$-modules with anyon Hilbert spaces are
classical \cite{kassel1995, kitaev2006, nayak2008}. What remains
conjectural in this manuscript is that the QOU substrate's full
particle spectrum — not only a chosen sector — is realised as
$H_n(R, q)$-modules, equivalently, that no QOU particle escapes the
anyonic substrate prior to observation. The conjecture is closed by
exhibiting either a particle outside the Hecke image, or a proof of
exhaustion via the cyclotomic-KLR equivalence
\cite{khovanovlauda2009}.*
