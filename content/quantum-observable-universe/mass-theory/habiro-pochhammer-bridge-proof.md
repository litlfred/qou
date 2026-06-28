**Proof.** The identity $1 - q^k = 1 - u^{2k} = (1 - u^k)(1 + u^k)$ is
immediate from $q = u^2$. Applying it to each factor of the
Pochhammer product gives

$$
  (q;q)_m = \prod_{k=1}^{m}(1 - q^k)
  = \prod_{k=1}^{m}(1 - u^k)(1 + u^k)
  = (u;u)_m \cdot \prod_{k=1}^{m}(1 + u^k).
$$

Substituting into the numerator:

$$
  \sum_m a_m(u)\,(q;q)_m
  = \sum_m a_m(u)\,(u;u)_m \cdot \prod_{k=1}^{m}(1 + u^k).
$$

Dividing by $\sum_m a_m(u)\,(u;u)_m$ gives the weighted average.
$\square$
