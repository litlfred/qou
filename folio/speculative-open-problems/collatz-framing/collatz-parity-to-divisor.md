Under [the $q$-Collatz map](#conj:q-collatz), divisibility by $[2]_q = q + 1$ in $\mathbb{Z}[q^{\pm 1}]$ is vanishing at the divisor $q = -1$: $P$ is $q$-even when $P(-1) = 0$ and $q$-odd when $P(-1) = -1$.

**Odd-step outputs need not be $q$-even.** Writing $[2]_q R = [3]_q P + 1$ for a $q$-odd element $P$ and differentiating at $q = -1$ gives $R(-1) = 1 + P'(-1)$. In particular, the odd fixed point $P = -q^{-2}$ has $P(-1) = -1$ and $P'(-1) = -2$, so $R(-1) = -1$: an odd step maps $-q^{-2}$ to itself, which is $q$-odd (mirroring the classical Syracuse map, where $(3n + 1)/2$ can be odd, as at $n = -1$). When $R$ is $q$-even on a domain-stable orbit, $v_{[2]}(R)$ counts the consecutive even steps preceding the next odd step ([withdrawn contact criterion](#conj:collatz-contact-boundary)).

| Polynomial identity | Formula | At $q = 1$ |
|---|---|---|
| Quadratic-versus-cubic difference | $[2]_q^2 - [3]_q = q$ | $4 - 3 = 1$ |
| Relative ratio | $q / [3]_q$ | $1/3$ |

Evaluating $|P(q)|$ at a real $q > 0$ is a heuristic picture only: $\log |P|$ is not a Laurent-ring invariant, and by the Syracuse-lift theorem the parity word of any domain-stable orbit is the classical parity word of $P(1)$.
