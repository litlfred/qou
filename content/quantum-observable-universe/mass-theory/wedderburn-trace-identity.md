The Wedderburn trace identity relates the $q$-dimensions of
irreducible representations of the Hecke algebra $H_n(R, q)$ to the
$q$-factorial, providing the combinatorial foundation for the
:refterm[descent]{#descent} decomposition of mass and coupling.

**Proposition.**
*For the Hecke algebra $H_n(R, q)$ over $R$
with parameter $q \neq 0, \pm 1$, the sum of squared quantum
dimensions equals the quantum factorial:*

$$
  \sum_{\lambda \vdash n} \dim_q(\lambda)^2 = [n]_q!
$$

*where $\dim_q(\lambda)$ is the $q$-analogue of the dimension of
the irreducible representation indexed by the partition $\lambda$,
and $[n]_q! = [1]_q [2]_q \cdots [n]_q$.*

**Consequence for mass.**

This identity determines the partition of the total Markov weight
among the irreducible representations.  In the :refterm[descent]{#descent} decomposition
of the mass endomorphism
([BW as :refterm[descent]{#descent}](#prop\:mass-categorical-descent)), each partition
$\lambda$ contributes a weight proportional to
$\dim_q(\lambda)^2 / [n]_q!$ to the total binding energy.

For the three extremal partitions of $H_n(R, q)$ (symmetric $[n]$,
standard $[n{-}1, 1]$, alternating $[1^n]$), the identity gives:

$$
  1^2 + (n{-}1)^2 + 1^2 = n^2 - 2n + 3 \leq n!
$$

at $q = 1$ (the classical limit), with equality only at $n = 3$.
For $q = q_0$, the $q$-deformed dimensions redistribute the weight:
the standard representation's contribution $\dim_q([n{-}1,1])^2$
dominates for large $n$, which is why the volume term (sourced by
the standard block) is the leading term in the BW formula.

**Explicit values.**

| $n$ | $[n]_{q_0}!$     | $\sum_\lambda \dim_{q_0}(\lambda)^2$ | Partitions          |
| --- | ---------------- | ------------------------------------ | ------------------- |
| $2$ | $[2]_q = 2.230$  | $1 + 1 = 2.230$                      | $[2], [1^2]$        |
| $3$ | $[3]_q! = 8.376$ | $1 + 4.376 + 1 = 8.376$              | $[3], [2,1], [1^3]$ |
| $4$ | $[4]_q! = 42.31$ | $1 + 13.1 + d_{[2,2]}^2 + 13.1 + 1$  | 5 partitions        |
| $5$ | $[5]_q! = 267.5$ | sum of 7 terms                       | 7 partitions        |

The Wigner coefficient $\lambda_W = [5]_q! \cdot m_e$ in the BW
formula arises from the Frobenius reciprocity of the $[n{-}2, 2]$
and $[n{-}2, 1^2]$ partitions at Hecke level $k = 5$.
