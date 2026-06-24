*
The forward direction is the standard simulation: if a
polynomial-time Turing machine decides the problem, encode it
as a braid with $c = O(\mathrm{poly}(N))$ crossings; the
transfer matrix product
([transfer matrix](#prop:skein-polynomial-transfer-matrix))
computes $P_L(q)$ in $O(c)$ matrix multiplications, each
costing $O(1)$ Planck steps.

For the converse, observe that extracting $P_L(q_0)$ requires
resolving the value of a degree $\leq c^2 - 1$ polynomial at a
specific point.  If the factored form
$P_L(q) = \prod_i \hat{V}_i(q)$ has $O(\mathrm{poly}(c))$
factors, each factor is computed in $O(1)$ steps from the local
transfer matrix, and the total cost is polynomial.  If the
factored form requires $\omega(\mathrm{poly}(c))$ factors, the
Skein polynomial does not compress — the information content
of the computation exceeds the polynomial bandwidth budget.
$\qquad\blacksquare$
