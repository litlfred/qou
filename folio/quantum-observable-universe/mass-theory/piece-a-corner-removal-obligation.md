*Let $\lambda \vdash n$ and let $(r,s)$ be a removable corner, so
$s = \lambda_r - 1$ and row $r+1$ is strictly shorter than row $r$. Write
$\mathrm{colLen}(j)$ for the number of rows reaching column $j$, and*

$$
  h(i,j) \;=\; (\lambda_i - j) + \bigl(\mathrm{colLen}(j) - i\bigr) - 1 .
$$

*Then the change in the hook-square sum caused by deleting the corner is*

$$
  1
  \;+\; \sum_{j=0}^{s-1}\bigl(2h(r,j) - 1\bigr)
  \;+\; \sum_{i=0}^{r-1}\bigl(2h(i,s) - 1\bigr)
  \;=\;
  (s-r)^2 \;+\; 2n - 1 .
$$

*The three terms on the left are the corner's own hook (which is $1$), the
cells of row $r$ strictly left of the corner, and the cells of column $s$
strictly above it — the only cells whose hook length changes.*
