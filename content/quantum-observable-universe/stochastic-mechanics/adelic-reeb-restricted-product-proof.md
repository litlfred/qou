Both parts are proved formally over the abstract value group
$\Gamma$ in
[`adelic-reeb-restricted-product.lean`](adelic-reeb-restricted-product.lean).
The restricted-product condition is encoded by an explicit finite set $S$ of
*active* places (those with $\ordw_v \neq 0$); off $S$ the local order is the
tame archimedean reference $0$, so the sum is finite and well-defined.
Additivity (`adelic_reeb_order_additive`) is pointwise addition of local orders
summed over $S$ ($\sum_S (a+b) = \sum_S a + \sum_S b$). The squeeze
(`adelic_reeb_squeeze_local_to_global`) is `Finset.sum_lt_sum`: a finite sum of
weak inequalities with one strict term is strict.
$\qquad\blacksquare$
