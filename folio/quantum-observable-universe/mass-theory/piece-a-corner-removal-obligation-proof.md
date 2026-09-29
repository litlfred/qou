**Proof.** Write $R = \sum_{i<r} \lambda_i$ for the cells in the rows strictly
above the corner and $C = \sum_{j<s} \mathrm{colLen}(j)$ for the cells in the
columns strictly left of it. The argument runs through five steps.

**(L1) The corner's column has height $r+1$.**
$\mathrm{colLen}(s) = \#\{i : \lambda_i > s\} = \#\{i : \lambda_i \geq
\lambda_r\}$. Row $r$ reaches column $s$ and row $r+1$ is strictly shorter, so
by weak decrease the rows meeting that condition are exactly $0, \ldots, r$:

$$
  \mathrm{colLen}(s) \;=\; r + 1 .
$$

**(L2) Hooks along the corner row.** For $j < s$, substituting
$\lambda_r - 1 = s$ into the definition,

$$
  h(r,j) \;=\; (s - j) + \bigl(\mathrm{colLen}(j) - r\bigr).
$$

**(L3) Hooks along the corner column.** For $i < r$, substituting
$\mathrm{colLen}(s) = r+1$ from (L1),

$$
  h(i,s) \;=\; (\lambda_i - s) + (r - i).
$$

**(L4) The row sum.** By (L2), $2h(r,j) - 1 = 2(s-j) + 2\,\mathrm{colLen}(j)
- 2r - 1$. Summing over $j = 0, \ldots, s-1$ and using
$\sum_{j<s}(s-j) = \tfrac{1}{2}s(s+1)$,

$$
  \sum_{j=0}^{s-1}\bigl(2h(r,j) - 1\bigr)
  \;=\; 2C + s^2 - 2rs .
$$

**(L5) The column sum.** By (L3), $2h(i,s) - 1 = 2\lambda_i - 2s + 2r - 2i - 1$.
Summing over $i = 0, \ldots, r-1$ and using
$\sum_{i<r} i = \tfrac{1}{2}r(r-1)$,

$$
  \sum_{i=0}^{r-1}\bigl(2h(i,s) - 1\bigr)
  \;=\; 2R + r^2 - 2sr .
$$

**(L6) Size decomposition.** Split $\lambda$ against the corner by
inclusion–exclusion. The rows above the corner contribute $R$; the columns
left of it contribute $C$; their overlap is the full $r \times s$ rectangle,
because every row $i \leq r$ has $\lambda_i \geq s+1$ and so contains every
column $j < s$. No cell lies in neither region except the corner itself: rows
below $r$ are strictly shorter than $s+1$, and row $r$ has only $j = s$ left.
Hence

$$
  n \;=\; R + C - rs + 1,
  \qquad\text{so}\qquad
  2(R + C) \;=\; 2n + 2rs - 2 .
$$

**Assembly.** Adding the corner's own contribution $1$ to (L4) and (L5),

$$
  1 + \bigl(2C + s^2 - 2rs\bigr) + \bigl(2R + r^2 - 2sr\bigr)
  \;=\; 1 + 2(R+C) + r^2 + s^2 - 4rs .
$$

Substituting (L6) for $2(R+C)$,

$$
  1 + \bigl(2n + 2rs - 2\bigr) + r^2 + s^2 - 4rs
  \;=\; 2n - 1 + r^2 - 2rs + s^2
  \;=\; (s-r)^2 + 2n - 1 . \qquad \blacksquare
$$
