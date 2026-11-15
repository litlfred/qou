**Proof.** Coefficient-by-coefficient match in descending order of $X$-power:

| Power of $X$ | Coefficient in $a_8$ | $p(n)$ | $n = 5 - k$ |
|---|---|---|---|
| $X^4$ | $1$ | $p(1) = 1$ (match) | $n = 1$ |
| $X^3$ | $2$ | $p(2) = 2$ (match) | $n = 2$ |
| $X^2$ | $3$ | $p(3) = 3$ (match) | $n = 3$ |
| $X^1$ | $5$ | $p(4) = 5$ (match) | $n = 4$ |
| $X^0$ | $7$ | $p(5) = 7$ (match) | $n = 5$ |

Each coefficient is the exact value of the integer partition
function at the corresponding index. The identity is checked in
$\mathbb{Z}[X]$ by `ring` after expanding
$\sum_{n=1}^{5}$ over $\{1, 2, 3, 4, 5\}$. ∎
