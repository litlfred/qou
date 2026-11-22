**Proof.**
The braiding on $V_1^{\otimes n}$ in $\mathrm{Rep}(\mathrm{SU}_q(2))$ gives $H_n(q)$. For $n = 2$: $2$ irreps. For $n = 3$: $3$ irreps. For $n \geq 4$: the embeddability constraint $(m-1)(s-1) \leq 2g$ with $m \geq 4$, $m < s$, $\gcd(m,s) = 1$ contributes no new torus knots at genus $g \leq 5$ beyond $T_{3,4}$ (which equals $T_{4,3}$). So the relevant Iwahori--Hecke algebra is $H_2(q) \oplus H_3(q)$, with $5$ irreps total.

A torus knot $T_{r,s}$ with $\gcd(r,s) = 1$ has Seifert genus $(r-1)(s-1)/2$, so $T_{2,s}$ has genus $(s-1)/2$ for odd $s$ and $T_{3,s}$ has genus $s-1$ for $s$ prime to $3$. Counting those of genus at most $g$:

| $g$ | from $r = 2$ | from $r = 3$ | $N(g)$ | $\geq 5$? |
|:---:|:---|:---|:---:|:---:|
| $2$ | $T_{2,3}, T_{2,5}$ | --- | $2$ | No |
| $3$ | $+\,T_{2,7}$ | $T_{3,4}$ | $4$ | No |
| $4$ | $+\,T_{2,9}$ | $+\,T_{3,5}$ | $6$ | **Yes** |

Since $N(3) = 4 < 5 \leq 6 = N(4)$ and $N$ is non-decreasing, $g = 4$ is the least genus at which $N(g) \geq 5$. $\square$

**What this proof does not establish.** It does not show that at $g = 4$ the six torus-knot evaluations span the five irreducibles, and no value of $q$ can make that true. A torus knot $T_{r,s}$ is the closure of a braid word on $r$ strands, so a row with $r_i = 2$ is supported in the two $H_2(q)$ columns and a row with $r_i = 3$ in the three $H_3(q)$ columns. The character matrix is therefore block-diagonal, and rank is additive over the blocks. At $g = 4$ the four $r = 2$ rows contribute at most $2$ (there are only two such columns) and the two $r = 3$ rows contribute at most $2$ (there are only two such rows), so

$$
\mathrm{rank}(M) \leq 2 + 2 = 4 < 5
$$

independently of $q$.
