**Definition.**
*The **$q$-Pochhammer partial product** at depth $n$ is the finite rational function:*

$$
  \Phi_n(x; q) := \prod_{k=0}^{n-1} \frac{1}{1 - x q^k} = \frac{1}{(x; q)_n}.
$$

*The denominator $(x; q)_n$ carries simple roots at $x = q^{-k}$. This finite product is structurally valid at the $q_0 > 1$ aether. It corresponds exactly to the categorical truncation $\Phi_q^{[\leq n]}$.*

The partial product satisfies the one-step recurrence $\Phi_{n+1} = \Phi_n / (1 - x q^n)$, which mirrors the filtration induction step. The denominator zeros $x = q^{-k}$ define the cuspidal boundary of the JSJ geometry. The algebraic engine uses these zeros as exact initial seeds for the Newton-Raphson solver.
