Three hard problems reformulated inside a quantum observable universe — the $q$-Collatz halting question, the $P$ versus $NP$ boundary, and $q$-Navier–Stokes regularity — are the **same question asked of one length filtration** on the Skein substrate $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$. Each computation is a braid word $\beta \in H_n(q)$; its observed output is the Markov trace $\mathrm{tr}_M(\beta)$ (the Jones–Skein invariant an observer reads); and its complexity is graded by the crossing-number filtration $\ell$.

Write $\ell$ for that filtration and $\mathrm{obs}$ for the Markov-trace observation. The three problems differ only in what they ask of $\ell$ along an orbit:

| Reformulation | Question on the filtration $\ell$ |
| --- | --- |
| $q$-Collatz | does $\ell$ **descend to the normal form** (the orbit halts)? |
| $P$ versus $NP$ | is the observation reachable within a **polynomial** $\ell$-budget, rather than the naive $3^{c}$ resolution leaves? |
| $q$-Navier–Stokes | does $\ell$ stay **bounded** (no finite-time blow-up of the vortex-knot complexity)? |

The observation is the common, tractable shadow: because the Skein relations cut a single fixed ideal whose quotient is $\mathbb{Z}[q^{\pm 1}]$, the Markov trace is computable, so "the observed output reaches the normal form's value" follows from halting for free. The difficulty is not algebraic — it does not live in an ideal. By the Reeb-flow Turing-completeness of the substrate dynamics, the halting set is undecidable, hence not cut out by any ideal; the content sits entirely in the filtration $\ell$.

For $q$-Navier–Stokes the dictionary is concrete: a vortex tube of the brane fluid is a braid word evolving in time, its closure is a knotted vortex, its conserved helicity is the Markov-trace observation, and its crossing number is $\ell$. A non-increasing filtration — a monotone Lyapunov complexity, the categorical form of bounded enstrophy — rules out blow-up with bound the initial complexity, the abstract shadow of the $q$-Beale–Kato–Majda criterion.

The three legs share the substrate and diverge only in the filtration question; none is settled here. Each remains an open conjecture in its own right: the $q$-Collatz descent measure, the faithfulness leg of the $P$ versus $NP$ boundary, and $q$-Navier–Stokes regularity are the respective open cores. What the shared structure supplies is a common language in which the tractable observation and the hard filtration question are cleanly separated.
