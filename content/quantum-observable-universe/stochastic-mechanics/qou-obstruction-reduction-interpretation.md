**Remark (obstruction on $\mathbb{P}^1$).**

The obstruction $\chi(A) \bmod n$ varies over the Kummer tower $\{\mu_n\}_{n \geq 1}$ inside $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$:

$$
\mathrm{obs}(n) :=
\begin{cases}
0 & \text{if } n \mid \chi(A), \\
\chi(A) \bmod n & \text{otherwise.}
\end{cases}
$$

For the Descartes universe with $\chi(A) = -6$:

See [Table 3](#tbl:qou-obstruction-reduction-table3-data).

The obstruction vanishes at finitely many levels (the divisors of $|\chi(A)| = 6$, namely $\{1, 2, 3, 6\}$). It persists at all levels $n$ where $\gcd(n, 6) \neq n$, including all primes $> 3$.

**Physical consequence.** The classical limit $q \to 1$ passes through infinitely many Kummer levels where the obstruction is nonzero. The density of non-vanishing levels in the Kummer tower is:

$$
\delta
=  1 - \frac{|\{n : n \mid 6\}|}{N}
\xrightarrow{N \to \infty} 1.
$$

In the limit, the obstruction is nonzero at a density-$1$ set of levels. The classical limit encounters the obstruction almost everywhere.
