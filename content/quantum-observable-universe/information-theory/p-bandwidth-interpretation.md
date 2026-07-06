The class $\mathrm{P}$ consists of those computations whose resolution trees admit sufficient destructive interference. There must be enough cancellation among the $3^c$ Skein histories that the Markov trace compresses the tree to $O(\mathrm{poly}(c))$ surviving terms. In each Planck step, the $q$-connection $\nabla_q$ processes $n_R(q) = 1/\hbar_q$ iterations ([Reeb operations](#prop:reeb-operations-per-planck)). Each iteration generates $\eta_q$ $q$-bits of entropy ([operational entropy](#def:operational-entropy)). The total information budget after $t$ Planck steps is:

$$
  I(t) = t \mathfrak{B}(q) = t \frac{q\eta_q}{(q-1)^2} \quad q\text{-bits.}
$$

A $\mathrm{P}$-class computation is one where $I(\mathrm{poly}(c))$ suffices to determine $P_L(q_0)$. The full resolution tree has $3^c$ leaves carrying $c \log_2 3$ $q$-bits of raw information. However, destructive interference reduces the effective information content to $O(\mathrm{poly}(c))$ $q$-bits. This fits within the polynomial bandwidth budget.

**Three regimes.**

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| Sub-horizon (P) | Effective tree $\leq \mathrm{poly}(c)$ | Interference collapses tree; no computational horizon |
| Critical | Effective tree $= c^{O(\log c)}$ | Quasi-polynomial; horizon marginally transparent |
| Super-horizon (NP-hard) | Effective tree $= 2^{\Omega(c)}$ | Horizon opaque; bandwidth saturated exponentially |

In the sub-horizon regime, the Markov trace acts as an efficient information funnel. It channels the $3^c$ resolution paths through the degree-$0$ bottleneck in polynomial time. The computation never encounters a computational horizon: the degree-$0$ answer remains accessible from a polynomial-depth slice of the resolution tree.

In the super-horizon regime, the resolution tree retains irreducible exponential weight. The $3^c$ paths do not cancel. They carry independent information that we must aggregate to determine the degree-$0$ observable. Because the bandwidth $\mathfrak{B}(q)$ is finite per Planck step, the computation requires exponentially many steps. A computational horizon separates the answer from the observer.
