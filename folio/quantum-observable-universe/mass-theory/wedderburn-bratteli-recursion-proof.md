## Proof

Write $t = [2]_q = q + q^{-1}$ and $d = a - b + 1$. The balanced $q$-integers satisfy

$$
  [d+1]_q + [d-1]_q \;=\; t\,[d]_q,
$$

since $(q^{d+1} - q^{-d-1}) + (q^{d-1} - q^{1-d}) = (q + q^{-1})(q^d - q^{-d})$.

*Restriction.* $y_{(a+1,b)} + y_{(a,b+1)} = \bigl([d+1]_q + [d-1]_q\bigr)/t^{a+b+1} = t\,[d]_q / t^{a+b+1} = y_{(a,b)}$.

*Single edge.* Adding a cell to the first row raises $a - b$ by one and the total by one, so $t\,[d]_q\, y_{(a+1,b)} = [d+1]_q\,[d]_q / t^{a+b} = [d+1]_q\, y_{(a,b)}$. The second row is the same with $[d-1]_q$.

Three-row shapes carry weight $0$ at $z = q^3/(q^2+1)$, so the recursion on two-row shapes is the whole recursion. The divisions are by $[2]_q$ and $[d]_q$, non-zero at generic $q$. At $n = 3$ the weights are $([4]_q/[2]_q^3,\; 1/[2]_q^2,\; 0)$. $\square$

The normalisation $\sum_{\lambda \vdash n} f^\lambda y_\lambda = 1$ follows by induction on $n$ from the restriction identity together with the Young branching rule $f^\lambda = \sum_{\mu \nearrow \lambda} f^\mu$.

