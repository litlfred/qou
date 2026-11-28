Three speculative reformulations—[$q$-Collatz convergence](#conj:q-collatz), [the skein P-versus-NP boundary](#conj:p-vs-np-boundary) ([obstruction form](#conj:qou-p-neq-np)), and $q$-Navier--Stokes vortex complexity—can be phrased as predicates on an abstract length-filtered observation system $(X, T, \ell, \mathrm{obs})$:

| Reformulation | Predicate on the length filtration $\ell$ along $T$-orbits |
| --- | --- |
| [$q$-Collatz](#conj:q-collatz) | Does every domain-stable orbit reach a finite periodic attractor? |
| [P versus NP boundary](#conj:p-vs-np-boundary) | Is $\mathrm{obs}$ computable within a polynomial $\ell$-budget? |
| $q$-Navier--Stokes | Does $\ell$ remain bounded along forward trajectories? |

**What is proved within a single instance versus what is not coupled across problems.** Within *one* dynamical system $(X, T, \ell, \mathrm{obs})$ whose target normal form is periodic (such as the period-$2$ cycle $\{q^{-1}, 1 + q^{-1}\}$ of $\mathcal{C}_q$), any trajectory that reaches the periodic cycle visits only finitely many states thereafter and consequently has bounded $\ell$; conversely, an unbounded trajectory cannot halt on the cycle, and on any forward-invariant halting cone the hitting time $\mu(x) = \min\{k : T^k(x) \in \text{cycle}\}$ is tautologically a strict $\mathbb{N}$-valued descent measure.

Crucially, this implication couples two predicates asked of **the same system instance**. Instantiating $(X, T, \ell, \mathrm{obs})$ once on Laurent polynomials under $\mathcal{C}_q$ and separately on vortex braid words in a fluid model shares a record signature, not a state space or transition map. Neither boundedness of fluid enstrophy nor polynomial-time trace evaluation implies or is implied by $q$-Collatz convergence.
