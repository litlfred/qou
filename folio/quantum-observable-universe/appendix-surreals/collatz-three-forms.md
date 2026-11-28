**Status: heuristic.** This remark is a dictionary, not a set of theorems. The contact-boundary criterion it starts from is false as stated ([contact boundary](#conj:collatz-contact-boundary)), and the categorical form below has no precise statement yet. The heuristic it records is the classical one: each tripling followed by at least two halvings on average. Below are its categorical, arithmetic and residue readings.

In the Iwahori--Hecke algebra $H_n(q)$, the Collatz step composes Hecke reduction ($T^2 = (q-q^{-1})T + 1$) and Markov destabilization ($\mathrm{tr}_M(xT_n) = z \cdot \mathrm{tr}_M(x)$). The Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q^{\pm 1}]$ sends braid words to Jones polynomials.

The categorical conjecture asserts that for every $h \in H_n(q)$, the iterated Markov trace converges to the unknot:

$$
\mathrm{tr}_M\bigl(\mathcal{C}_q^k(h)\bigr) \xrightarrow{k \to \infty} 1.
$$

This is a conjecture in words. The map $\mathcal{C}_q$ on $H_n(q)$ has not been defined, so it is not yet a mathematical statement.

The contact boundary translates this into a divisibility condition on the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$. Each odd step produces $[3]_q P + 1$. The Skein divisibility identity $[3]_q = q[2]_q + 1$ guarantees one built-in halving. The net contraction per cycle with $v$ total halvings is $[3]_q / [2]_q^v$. This is contractive if and only if $[2]_q^v > [3]_q$. The integer threshold is exactly $v = 2$. Two halvings per tripling are required.

The $[2]_q$-divisor is $q = -1$. Evaluating the Collatz output at this divisor: since $[3]_q|_{q=-1} = 1$ and $[2]_q|_{q=-1} = 0$, the condition $v_{[2]} \geq 2$ becomes $(q+1)^2$-divisibility of $[3]_q P + 1$ at $q = -1$.

At $q = 1$ (the classical limit), the expected $2$-adic valuation of $3n+1$ for uniformly distributed odd $n$ is:

$$
\mathbb{E}[v_2(3n+1)] = \sum_{k=1}^{\infty} k \cdot 2^{-k} = 2.
$$

The minimum needed is $\log_2 3 \approx 1.585$ halvings per tripling, so the classical average of $2$ already has a margin: the heuristic factor per odd step is $3/4 < 1$. The gap $[2]_q^2 - [3]_q = q$ equals $1$ at $q = 1$, not $0$. So the classical problem is not a degenerate case in which the margin disappears. An earlier version of this remark said it was, and that was wrong. Collatz is hard because the average says nothing about individual orbits. The deformation does not change this, since a domain-stable $q$-orbit has the classical parity sequence of its value at $q = 1$ ([Syracuse lift](#prop:collatz-syracuse-lift)).
