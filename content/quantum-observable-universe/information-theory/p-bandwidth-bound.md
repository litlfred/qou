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

**Interpretation.**  The class $\mathrm{P}$ consists of those
computations whose resolution trees admit sufficient destructive
interference — enough cancellation among the $3^c$ Skein
histories — that the Markov trace compresses the tree to
$O(\mathrm{poly}(c))$ surviving terms.  In each Planck step,
the $q$-connection $\nabla_q$ processes $n_R(q) = 1/\hbar_q$
iterations ([Reeb operations](#prop:reeb-operations-per-planck)),
each generating $\eta_q$ $q$-bits of entropy
([operational entropy](#def:operational-entropy)).  The total
information budget after $t$ Planck steps is

$$
  I(t) =  t \cdot \mathfrak{B}(q)
  =  t \cdot \frac{q\eta_q}{(q-1)^2}
  q\text{-bits.}
$$

A P-class computation is one where $I(\mathrm{poly}(c))$
suffices to determine $P_L(q_0)$.  The resolution tree has
$3^c$ leaves carrying $c \cdot \log 3$ $q$-bits of raw information,
but destructive interference reduces the effective information
content to $O(\mathrm{poly}(c) \cdot \log 3)$ $q$-bits — within
the polynomial bandwidth budget.

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

*
