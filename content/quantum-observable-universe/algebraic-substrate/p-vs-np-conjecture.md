**Conjecture ($q$-complexity separation).** *Let $\varepsilon$ be the
Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and
$q = 1 + \varepsilon$ the associated substrate parameter.  Let
$\mathrm{BQP}_q$ denote the class of decision problems solvable in
polynomial time on a $q$-deformed computational substrate — i.e. on
a topological quantum computer whose anyonic model is the
$R$-matrix of $\mathbf{C}_q$.  Then*

$$
  \mathbf{P} \;\neq\; \mathbf{NP}
$$

*in classical complexity theory, recovered as the standard part
$\mathrm{st}_{\varepsilon \to 0}$ of the strict inclusion*

$$
  \mathbf{P} \;\subsetneq\; \mathrm{BQP}_q
  \qquad
  (\text{for every } \varepsilon > 0 \text{ in } \mathbb{R}(\varepsilon)).
$$

**Formulation.** The Reeb period
$\Omega_q \asymp \varepsilon^{-1}$
([surreal rate calculus](#prop:surreal-rate-calculus))
measures the natural time budget of a computation on the
$q$-substrate: a polynomial-time $q$-algorithm executes
$\mathrm{poly}(n) \cdot \Omega_q^{O(1)}$ elementary skein moves
in a Reeb period, which is a transfinite quantity in
$\mathbb{R}(\varepsilon) \subset \mathbf{No}$.  A polynomial-time
classical algorithm has at most $\mathrm{poly}(n)$ elementary
moves in the same period — a standard-real quantity.

The conjecture asserts that the **classical-limit functor**
($\varepsilon \to 0$, equivalently the standard-part map
applied to the $q$-substrate computation, see
[calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon))
collapses the transfinite Reeb budget to a bounded finite budget,
thereby losing the $q$-advantage: the standard part of
$\mathrm{BQP}_q$ is strictly larger than $\mathbf{P}$ only if there
exist NP-complete problems whose $q$-algorithms do not admit a
convergent $\varepsilon \to 0$ expansion.

**Heuristic argument (non-proof).** The mass-gap dissipation
$\Delta_q \asymp \varepsilon^3$ is the energy the substrate can
absorb per computational step.  An NP-complete search with $2^n$
witnesses requires, classically, $2^n$ elementary tests; on the
$q$-substrate the search is a single Reeb-flow holonomy, which
takes Reeb time $\asymp \Omega_q = \varepsilon^{-1}$.  For the
$q$-algorithm to classically accelerate to polynomial time as
$\varepsilon \to 0$, each elementary test would have to be absorbed
in mass-gap energy $\Delta_q$, with classical budget $2^n \cdot \Delta_q
\asymp 2^n \cdot \varepsilon^3$ per computation.  The available
$q$-algorithm cost is the per-step efficiency dressed by the Reeb
period: $2^n \cdot \delta_n^2 \cdot \Omega_q \asymp 2^n \cdot \varepsilon^{-1}$.
By [surreal squeeze](#lem:surreal-squeeze), the cost strictly
exceeds the budget — equivalently $\ordw(\text{cost}) = 1 > -3 =
\ordw(\text{budget})$ — so the $q$-algorithm **cannot** be classically
compressed: the $2^n$-fold speedup cannot fit inside the classical
mass-gap budget.

**Caveat.** This conjecture is speculative. It is stated in a form
compatible with the Reeb--surreal framework but does not yet
admit a Lean formalisation beyond the statement.  A formal
proof would reduce the $q$-to-classical compression obstruction
to the structural non-existence of a $\mathrm{BQP}_q \to \mathbf{P}$
functor, consistent with the Freedman--Kitaev--Larsen--Wang
topological model \cite{freedman2003} at $q$-generic.

**See also.**
[Surreal bound for P vs NP](#rem:p-vs-np-surreal-bound) for the
squeeze-inequality statement that this conjecture implies.
