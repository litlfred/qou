The Wedderburn trace identity records the normalization of the Markov
trace on the Wedderburn blocks of the Hecke algebra $H_n(R, q)$: the
total Markov weight is partitioned among the irreducible
representations with unit sum, providing the combinatorial foundation
for the :refterm[descent]{#descent} decomposition of mass and coupling.

**Consequence for mass.**

In the :refterm[descent]{#descent} decomposition of the mass
endomorphism ([BW as :refterm[descent]{#descent}](#conj:mass-categorical-descent)),
the Markov weight $y_\lambda$ of each partition $\lambda$ fixes that
block's contribution to the total binding energy; the unit-sum
normalization is what makes the descent a genuine *partition* of the
weight. The standard representation $[n{-}1, 1]$ carries the dominant
weight, which is why the volume term (sourced by the standard block)
leads the BW formula.

**Scale versus weight: two distinct $q$-objects.**

Two $q$-quantities enter the BW formula and must not be conflated:

- the **Hecke-level scale** $[n]_q! = [1]_q [2]_q \cdots [n]_q$ (for
  example the Wigner coefficient $\lambda_W = [5]_q!\, m_e$ at Hecke
  level $k = 5$), evaluated directly as the $q$-factorial product;
- the **per-block weight ratio** $w_\lambda(q) = \dim_q(\lambda)^2 / [n]_q!$,
  used in the LP-dual shadow prices, which coincides with the Markov
  weight $y_\lambda$ only on self-conjugate $\lambda$.

Neither is the bare sum $\sum_\lambda \dim_q(\lambda)^2$: that sum is a
separate $q$-polynomial (the global dimension of the block algebra)
and equals $[n]_q!$ only at $q = 1$.

**Classical limit.** At $q = 1$ the block dimensions satisfy the
Wedderburn–Artin count $\sum_\lambda d_\lambda^2 = n! = \dim H_n$ for
$\mathbb{C}[S_n]$. Dividing by $n!$ gives the unit-sum normalization
for the Plancherel weights $d_\lambda/n!$, which are the Markov weights
at $z = 0$ (the regular trace). Under convention D, $q = 1$ gives
$z = 1/2$ and different weights: at $n = 2$, $y_{(2)} = 3/4$ and
$y_{(1,1)} = 1/4$.
