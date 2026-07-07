The class $\mathrm{P}$ consists of computations whose resolution trees exhibit sufficient destructive interference. Cancellation among the $3^c$ Skein histories allows the Markov trace to compress the tree to $O(\mathrm{poly}(c))$ surviving terms. In each Planck step, the $q$-connection $\nabla_q$ processes $n_R(q) = 1/\hbar_q$ iterations. Each iteration generates $\eta_q$ $q$-bits of entropy. After $t$ Planck steps, the total information budget is:
$$
  I(t) = t \mathfrak{B}(q) = t \frac{q\eta_q}{(q-1)^2} \quad q\text{-bits.}
$$

A $\mathrm{P}$-class computation succeeds when $I(\mathrm{poly}(c))$ suffices to determine $P_L(q_0)$. Although the full resolution tree carries $c \log_2 3$ $q$-bits of raw information, destructive interference limits the effective content to $O(\mathrm{poly}(c))$ $q$-bits, fitting within the polynomial budget.

**Three regimes.**

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| Sub-horizon (P) | Effective tree $\leq \mathrm{poly}(c)$ | Interference collapses tree; no computational horizon |
| Critical | Effective tree $= c^{O(\log c)}$ | Quasi-polynomial; horizon marginally transparent |
| Super-horizon (NP-hard) | Effective tree $= 2^{\Omega(c)}$ | Horizon opaque; bandwidth saturated exponentially |

In the sub-horizon regime, the Markov trace funnels the $3^c$ paths through the degree-$0$ bottleneck in polynomial time. The computation avoids any computational horizon; the answer remains accessible from a polynomial-depth subtree.

In the super-horizon regime, the resolution tree retains irreducible exponential weight. The uncancelled paths carry independent information requiring full aggregation. Because the bandwidth $\mathfrak{B}(q)$ per Planck step is finite, this demands exponentially many steps. A computational horizon strictly separates the answer from the observer.
