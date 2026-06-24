By [Wenzl bridge](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q) = s_{\lambda, \check{q}}(Q) / Z_n$ with $Q = q^2$ and
$X = Q^{\check{q}} = q \cdot z / (1 - Q + q \cdot z)$.

Substitute $q = \check{q}^2$ throughout: $Q = \check{q}^4$, $z = \check{q} / (\check{q}^2 + 1)$,
$qz = \check{q}^3 / (\check{q}^2 + 1)$, and

$$
  X(\check{q}) = \frac{\check{q}^3}{1 + \check{q}^2 + \check{q}^3 - \check{q}^4 - \check{q}^6}.
$$

The Schur principal-specialisation factor is

$$
  s_{\lambda, \check{q}}(Q) = Q^{n(\lambda)} \prod_{x \in \lambda}
    \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
$$

The denominator $\prod (1 - Q^{h(x)}) = \prod (1 - \check{q}^{4 h(x)})$
factors over $\mathbb{Z}[\check{q}]$ as

$$
  1 - \check{q}^{4h} \;=\; \prod_{d \mid 4h} \Phi_d(\check{q}).
$$

Hence each $s_{\lambda, \check{q}}(Q)$, before normalisation, has a
denominator that is a product of $\Phi_d(\check{q})$ for $d \mid 4 h(x)$.
The sum $Z_n = \sum_\mu d_\mu s_{\mu, \check{q}}$ has a common denominator
that is the LCM of these — itself a product of $\Phi_d(\check{q})$.

After reducing $y_\lambda = s_\lambda / Z$, the **denominator
$D_n(\check{q})$ is a product of cyclotomic polynomials** by the closure of
cyclotomic factorisations under multiplication and division.

The **numerator** $P_\lambda(\check{q})$ encodes the specific $X$
substitution and the per-partition Schur structure; it is not
cyclotomic in general. Its degree is bounded by $\sum_x 4 h(x)$
(the total hook content). $\square$
