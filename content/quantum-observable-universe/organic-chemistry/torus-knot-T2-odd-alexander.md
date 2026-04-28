**Definition.**
For each odd integer $N = 2m + 1 \ge 3$, the **symmetric Alexander
polynomial** of the torus knot $T(2, 2m+1)$ is the symmetric Laurent
polynomial

$$
  \Delta_{T(2,\,2m+1)}(q)
   = 
  \frac{q^{2m+1} + q^{-(2m+1)}}{q + q^{-1}}.
$$

By induction on $m$ this is also the geometric series

$$
  \Delta_{T(2,\,2m+1)}(q)
   = 
  \sum_{k=0}^{2m}\,(-1)^{k}\,q^{2m - 2k}
   = 
  q^{2m} - q^{2m-2} + q^{2m-4} - \cdots + q^{-(2m-2)} + q^{-2m}.
$$

**Examples.**
- $T(2,3)$ (trefoil): $\Delta(q) = q^{2} - 1 + q^{-2}$.
- $T(2,5)$ (cinquefoil / Solomon's seal):
  $\Delta(q) = q^{4} - q^{2} + 1 - q^{-2} + q^{-4}$.
- $T(2,7)$:
  $\Delta(q) = q^{6} - q^{4} + q^{2} - 1 + q^{-2} - q^{-4} + q^{-6}$.

**Specialisation at $q = 1$.**
For all odd $N$,
$\Delta_{T(2, 2m+1)}(1) = 1$
(the alternating signs collapse the $2m+1$ unit terms to a single
$1$ — a single component, in contrast to even $N = 2m$ where the
sum is $m \ge 1$).
