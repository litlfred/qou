Each factor is non-zero on the domain: $\lvert q^{-k} z\rvert
< q^{-k} \cdot q = q^{\,1-k} \leq 1$ for $k \geq 1$, so
$1 - q^{-k} z \neq 0$
([quantum dilogarithm](#cor\:quantum-dilogarithm)). Writing
$a_k = q^{-k} z$, the geometric series $\sum_{k \geq 1} \lvert a_k\rvert
= \lvert z\rvert \sum_{k\geq 1} q^{-k}$ converges since $q > 1$. On the
domain every denominator obeys the uniform lower bound
$1 - a_k \geq 1 - \lvert z\rvert / q > 0$, so the deviation terms
$g_k = (1 - a_k)^{-1} - 1 = a_k/(1 - a_k)$ satisfy
$\lvert g_k\rvert \leq \lvert a_k\rvert /(1 - \lvert z\rvert/q)$ and are
summable by comparison. Multipliability of $\prod_k (1 + g_k) =
\prod_k (1 - a_k)^{-1}$ then follows from the one-plus-summable
criterion for infinite products.
$\qquad\blacksquare$
