*Under convention D ($z = q^3/(q^2+1)$) the Jones–Markov weight of every shape with three or more rows is $0$, and on the two-row shape $(a, b)$, $a \geq b$, it is*

$$
  y_{(a,b)}
  \;=\;
  \frac{[a - b + 1]_q}{[2]_q^{\,a+b}},
$$

*with $[k]_q$ the balanced $q$-integer. These weights satisfy a Bratteli recursion in two equivalent forms.*

*Restriction (sum over the Bratteli edges out of $(a, b)$):*

$$
  y_{(a,b)}
  \;=\;
  y_{(a+1,\,b)} \;+\; y_{(a,\,b+1)}.
$$

*When $a = b$ the second shape is not a partition, and the formula assigns it weight $[0]_q = 0$.*

*Single edge. With $d = a - b + 1$, adding a cell to the first or second row gives*

$$
  y_{(a+1,\,b)}
  \;=\;
  \frac{[d+1]_q}{[2]_q\,[d]_q}\; y_{(a,b)},
  \qquad
  y_{(a,\,b+1)}
  \;=\;
  \frac{[d-1]_q}{[2]_q\,[d]_q}\; y_{(a,b)}.
$$

*So the per-edge factor is $F_q = [d \pm 1]_q / ([2]_q [d]_q)$, depending on which row receives the cell. Each single edge determines $y_\lambda^{(n+1)}$ from one parent; summing these factors over all parents of $\lambda$ would double-count.*

This recursion confirms that $\alpha_k(H_n)$ at a fixed $k$ involves only finitely many strata. The tower of Jones-Markov weights propagates without requiring expensive $p(n) \times p(n)$ linear-system solves.
