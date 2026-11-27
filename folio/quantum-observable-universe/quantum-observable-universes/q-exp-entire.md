Fix the aether regime $q > 1$ and write $[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ for the balanced $q$-integer, with $[n]_q! = \prod_{k=1}^{n} [k]_q$. The $q$-exponential series

$$
  \exp_q(x) = \sum_{n \ge 0} \frac{x^n}{[n]_q!}
$$

converges for every $x \in \mathbb{C}$; equivalently $\exp_q$ is entire.

The proof is a ratio test. Dropping the positive tail of the balanced expansion gives $[n+1]_q \ge q^{n}$, so $[n]_q! > 0$ and the ratio of consecutive terms is $\|x\| / [n+1]_q \le \|x\|\, q^{-n} \to 0$; since $q^n \to \infty$ the ratio is eventually below $\tfrac12$, so the series is summable.
