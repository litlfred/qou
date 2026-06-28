The squeeze inequality of [surreal squeeze](#lem:surreal-squeeze) gives a heuristic account of why the classical-limit functor collapses the $q$-advantage.

## Heuristic argument (non-proof)

The mass-gap dissipation
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
