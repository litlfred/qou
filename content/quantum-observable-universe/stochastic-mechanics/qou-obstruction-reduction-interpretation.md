**Remark (the obstruction over $\mathbb{P}^1$ and the three millennium problems as specializations).**

**The obstruction as a function on $\mathbb{P}^1$.**

The obstruction $\chi(A) \bmod n$ varies over the Kummer tower
$\{\mu_n\}_{n \geq 1}$ inside $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$:

$$
\mathrm{obs}(n) :=
\begin{cases}
0 & \text{if } n \mid \chi(A), \\
\chi(A) \bmod n & \text{otherwise.}
\end{cases}
$$

For the Descartes universe with $\chi(A) = -6$:

See [Table 3](#tbl:qou-obstruction-reduction-table3-data).

The obstruction **vanishes at only finitely many levels**
(the divisors of $|\chi(A)| = 6$, namely $\{1, 2, 3, 6\}$)
and **persists at all levels $n$ with $\gcd(n, 6) \neq n$** —
in particular at all primes $> 3$.

**Physical consequence:** the classical limit $q \to 1$ must
pass through infinitely many Kummer levels where the
obstruction is nonzero. The density of non-vanishing levels
in the Kummer tower is

$$
\delta
=  1 - \frac{|\{n : n \mid 6\}|}{N}
\xrightarrow{N \to \infty} 1.
$$

In the limit: the obstruction is nonzero at density-$1$ set
of levels. The classical limit cannot avoid the obstruction.

**The three millennium problems as specializations.**
Each millennium problem is a property $\mathcal{P}$ that holds
unconditionally at the $q$-scale, with obstruction class
$[\mathcal{P}] \in \mathrm{Obs}(\mathbf{C}, q \to 1) \cong k$.
In the QOU, the single obstruction scalar controls all three:

See [Table 4](#tbl:qou-obstruction-reduction-table4-data).

All three obstructions are **images of the same class**
$\chi(A) \in HH^2 \cong k$ under different evaluation maps:

- **RH**: evaluate $\chi(A)$ on the spectral localization
 map $HH^2 \to H^2(\mathrm{Spec}(\xi_q))$
- **NS**: evaluate $\chi(A)$ on the collision restriction
 map $HH^2 \to H^2(\Sigma, \mathcal{B}|_\Sigma)$
- **BSD**: evaluate $\chi(A)$ on the elliptic restriction
 map $HH^2 \to H^2(\mathcal{E}_q, \mathcal{B}|_{\mathcal{E}_q})$

The one-dimensionality of $HH^2$ means these three evaluations
are **proportional**: there is a single real number (the Euler
characteristic $\chi(A) = -6$) that controls whether all three
millennium problems persist through the classical limit.

**Corollary.** If any one of the three millennium problems is
resolved (in either direction), the resolution constrains the
other two. Specifically: if the classical limit functor
$\mathcal{L}$ preserves the property $\mathcal{P}$ for one
problem, then the same functor either preserves or violates
$\mathcal{P}$ for the other two — the mechanism is the same,
only the evaluation map differs.
