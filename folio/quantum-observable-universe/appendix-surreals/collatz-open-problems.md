Four problems are open. None of them is claimed.

**1. The conjecture in its sharpest form.** By the [Syracuse lift](#prop:collatz-syracuse-lift) and the [bounded window](#prop:collatz-bounded-window) result, the [$q$-Collatz conjecture](#conj:q-collatz) fails only if a domain-stable Laurent polynomial lifts a divergent Syracuse orbit, and such an orbit has support in no fixed window. Put $t = 1 + q$. A domain-stable element is determined by its parity sequence $(s_k)$. With $i_1 < i_2 < \cdots$ the positions of the odd steps, it is

$$
P = -\sum_{j \geq 1} t^{\,i_j}\, [3]_q^{-j}
$$

in $\mathbb{Z}[[t]]$. Here $[3]_q = 1 - t + t^2$ is a unit. The question is which parity sequences make this series a Laurent polynomial in $q$. It concerns one explicit family of power series, not integer dynamics. We do not know whether it is easier than the classical problem.

**2. Which integers lift.** Characterise the integers $n = P(1)$ that have a domain-stable lift. For those integers, $q$-Collatz gives classical convergence. The set is sparse. An odd step into $[2]_q^{\,k} q^{-1}$, the lift of $2^k$, exists exactly when $[3]_q$ divides $[2]_q^{\,k+1} - q$. Evaluating at a primitive cube root of unity $\omega$, where $1 + \omega$ is a primitive sixth root of unity, shows that this happens exactly when $k \equiv 1 \pmod 6$. So $85 = (2^8 - 1)/3$ lifts, while $5 = (2^4 - 1)/3$ does not, and hence neither does $3$. Constants other than $0$ are not domain-stable.

**3. The mod-$2$ shadow.** Modulo $2$, the map becomes $\bar{\mathcal{C}}(f) = f/(1+q)$ if $f(1) = 0$ and $([3]_q f + 1)/(1+q)$ if $f(1) = 1$, defined on all of $\mathbb{F}_2[q^{\pm 1}]$. The proof of the [bounded window](#prop:collatz-bounded-window) result shows that a domain-stable orbit converges exactly when its shadow is eventually periodic. Unlike the $\mathbb{F}_2[x]$ analogue of $3n+1$ with multiplier $x + 1$, whose orbits all converge \cite{hicksmullenyucaszavislak2008}, this shadow appears to have orbits whose degree grows without bound. That is a computer observation, not a theorem. So the shadow alone will not settle the conjecture. The open question is how the integer lift constrains which shadow orbits occur.

**4. The braid form.** The categorical reading in [three faces](#rem:collatz-three-forms), iterated Markov traces tending to the unknot, needs a definition of $\mathcal{C}_q$ on the Hecke algebra $H_n(q)$ before it is a mathematical statement.
