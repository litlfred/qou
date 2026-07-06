The Wedderburn trace identity records the normalization of the Markov
trace on the Wedderburn blocks of the Hecke algebra $H_n(R, q)$: the
total Markov weight is partitioned among the irreducible
representations with unit sum, providing the combinatorial foundation
for the :refterm[descent]{#descent} decomposition of mass and coupling.

**Proposition (Markov-trace normalization).**
*For the Hecke algebra $H_n(R, q)$ over a field $R$ with parameter
$q \neq 0$, the Markov-trace weights $y_\lambda(q)$ and the ordinary
block dimensions $d_\lambda = f^\lambda$ (the number of standard Young
tableaux of shape $\lambda$) satisfy*

$$
  \sum_{\lambda \vdash n} d_\lambda\, y_\lambda(q) = 1 .
$$

*Equivalently $\operatorname{tr}_M(\mathbf{1}) = \sum_\lambda y_\lambda\,\chi^\lambda(\mathbf{1}) = \sum_\lambda y_\lambda d_\lambda = 1$: the Markov trace of the identity is unit, so the weights $y_\lambda$ partition the total Markov weight among the irreducibles.*

**Consequence for mass.**

In the :refterm[descent]{#descent} decomposition of the mass
endomorphism ([BW as :refterm[descent]{#descent}](#prop:mass-categorical-descent)),
the Markov weight $y_\lambda$ of each partition $\lambda$ fixes that
block's contribution to the total binding energy; the unit-sum
normalization is what makes the descent a genuine *partition* of the
weight. The standard representation $[n{-}1, 1]$ carries the dominant
weight, which is why the volume term (sourced by the standard block)
leads the BW formula.

**Scale versus weight — two distinct $q$-objects.**

Two $q$-quantities enter the BW formula and must not be conflated:

- the **Hecke-level scale** $[n]_q! = [1]_q [2]_q \cdots [n]_q$ — for
  example the Wigner coefficient $\lambda_W = [5]_q!\, m_e$ at Hecke
  level $k = 5$ — evaluated directly as the $q$-factorial product;
- the **per-block weight ratio** $\tilde w_\lambda = \dim_q(\lambda)^2 / [n]_q!$,
  used in the LP-dual shadow prices, which coincides with the Markov
  weight $y_\lambda$ only on self-conjugate $\lambda$.

Neither is the bare sum $\sum_\lambda \dim_q(\lambda)^2$: that sum is a
separate $q$-polynomial — the global dimension of the block algebra —
and equals $[n]_q!$ only at $q = 1$.

**Classical limit.** At $q = 1$ the block dimensions satisfy the
Wedderburn–Artin count $\sum_\lambda d_\lambda^2 = n! = \dim H_n$ for
$\mathbb{C}[S_n]$, and dividing by $n!$ recovers the unit-sum
normalization above.
