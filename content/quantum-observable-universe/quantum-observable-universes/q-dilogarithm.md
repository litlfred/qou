The $q$-shuffle Hopf algebra $\mathcal{H}_q$
([$q$-exponential](#def:q-exponential),
[$q$-logarithm](#def:q-logarithm)) admits a canonical *level-2* element
obtained by iterating its primitive structure once. A
**level-$k$ primitive** of $\mathcal{H}_q$ is an element
$p_k \in \mathcal{H}_q^{\otimes k}$ satisfying the shuffle recursion

$$
  \Delta_q(p_k) \;=\; p_k \otimes 1 + 1 \otimes p_k + \sum_{i=1}^{k-1}
    p_i \otimes p_{k-i},
$$

with $p_0 = 1$ and $p_1 = \log_q$; the solution space at each level is
one-dimensional (up to primitives of lower levels). The
**$q$-dilogarithm** is the unique level-2 primitive

$$
  \mathrm{Li}_2^q \;\in\; \mathcal{H}_q^{\otimes 2}
$$

normalised by the five-term *pentagon* relation

$$
  \mathrm{Li}_2^q(y) + \mathrm{Li}_2^q(x)
  \;=\;
  \mathrm{Li}_2^q(xy) + \mathrm{Li}_2^q\!\left(\frac{x(1-y)}{1-xy}\right)
  + \mathrm{Li}_2^q\!\left(\frac{y(1-x)}{1-xy}\right),
$$

which pins $\mathrm{Li}_2^q$ up to a scalar.
