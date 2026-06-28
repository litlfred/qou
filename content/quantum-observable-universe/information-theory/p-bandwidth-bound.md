**Proposition.**
*A decision problem encoded by a link $L = \hat{\beta}$ with
$c = 3N$ crossings is in $\mathrm{P}$ if and only if its Skein
polynomial $P_L(q)$ can be evaluated — degree-$0$ answer extracted — within*

$$
  t(c)  \leq  \mathfrak{B}(q)^{-1} \cdot \mathrm{poly}(c)
$$

*Planck steps, where $\mathfrak{B}(q) = q\eta_q / (q-1)^2$ is
the information bandwidth per Planck time
([information bandwidth](#def:information-speed-of-light)).*

**Three regimes.**

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| Sub-horizon (P) | Effective tree $\leq \mathrm{poly}(c)$ | Interference collapses tree; no computational horizon |
| Critical | Effective tree $= c^{O(\log c)}$ | Quasi-polynomial; horizon marginally transparent |
| Super-horizon (NP-hard) | Effective tree $= 2^{\Omega(c)}$ | Horizon opaque; bandwidth saturated exponentially |

In the sub-horizon regime, the Markov trace acts as an efficient
**information funnel**: it channels the $3^c$ resolution paths
through the degree-$0$ bottleneck in polynomial time.  The
computation never encounters a computational horizon — the
degree-$0$ answer is accessible from a polynomial-depth slice
of the resolution tree.

In the super-horizon regime, the resolution tree has
irreducible exponential weight.  The $3^c$ paths do not
cancel — they carry independent information that must be
aggregated to determine the degree-$0$ observable.  The
bandwidth $\mathfrak{B}(q)$ is finite per Planck step, so
exponentially many steps are required.  A computational
horizon separates the answer from the observer.

**Proof sketch.**
The forward direction is the standard simulation: if a
polynomial-time Turing machine decides the problem, encode it
as a braid with $c = O(\mathrm{poly}(N))$ crossings; the
transfer matrix product
([transfer matrix](#prop:skein-polynomial-transfer-matrix))
computes $P_L(q)$ in $O(c)$ matrix multiplications, each
costing $O(1)$ Planck steps.

For the converse, observe that extracting $P_L(q_0)$ requires
resolving the value of a degree $\leq c^2 - 1$ polynomial at a
specific point.  If the factored form
$P_L(q) = \prod_i \hat{V}_i(q)$ has $O(\mathrm{poly}(c))$
factors, each factor is computed in $O(1)$ steps from the local
transfer matrix, and the total cost is polynomial.  If the
factored form requires $\omega(\mathrm{poly}(c))$ factors, the
Skein polynomial does not compress — the information content
of the computation exceeds the polynomial bandwidth budget.
