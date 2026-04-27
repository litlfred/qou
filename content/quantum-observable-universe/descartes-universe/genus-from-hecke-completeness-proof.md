**Proof.**
The braiding on $V_1^{\otimes n}$ in $\mathrm{Rep}(\mathrm{SU}_q(2))$
gives $H_n(q)$.  For $n = 2$: $2$ irreps.  For $n = 3$: $3$ irreps.
For $n \geq 4$: the embeddability constraint $(m-1)(s-1) \leq 2g$
with $m \geq 4$, $m < s$, $\gcd(m,s) = 1$ contributes no new
torus knots at genus $g \leq 5$ beyond $T_{3,4}$ (which equals
$T_{4,3}$).  So the relevant Iwahori--Hecke algebra is
$H_2(q) \oplus H_3(q)$, with $5$ irreps total.

At genus $g$, the number of embeddable torus knots with
$r \in \{2, 3\}$ is:

| $g$ | From $r = 2$ | From $r = 3$ | Total | $\geq 5$? |
|:---:|:---:|:---:|:---:|:---:|
| $2$ | $T_{2,3}, T_{2,5}$ | --- | $2$ | No |
| $3$ | $+ T_{2,7}$ | $T_{3,4}$ | $4$ | No |
| $4$ | $+ T_{2,9}$ | $+ T_{3,5}$ | $6$ | **Yes** |

At $g = 3$: $4$ evaluations cannot span a $5$-dimensional
space (rank $\leq 4$).  At $g = 4$: $6$ evaluations span
$5$ irreps (verified numerically: the $6 \times 5$ matrix
has rank $5$ for all $q > 1$, $q \neq$ root of unity).
Therefore $g_{\min} = 4$.  $\square$
