The Jones polynomial of the Borromean rings is
\cite{murasugi1996}:

$$
  V(\mathcal{B}_3, t)
  = -t^{-3} + 3t^{-2} - 2t^{-1} + 4 - 2t + 3t^2 - t^3.
$$

Setting $t = q^2$ and introducing $u := q^2 + q^{-2}$, this becomes
a polynomial in $u$:

$$
  V = -u^3 + 3u^2 + u - 2.
$$

For a 3-component link, the Markov trace is $\mathrm{tr}_M =
V / [2]_q^2$ where $[2]_q^2 = (q + q^{-1})^2 = u + 2$. Polynomial
long division yields:

$$
  \frac{V}{u + 2}
  = -u^2 + 5u - 9 + \frac{16}{u + 2}.
$$

Substituting $u = h^2 + 2$ (where $h = q - q^{-1}$, so
$q^2 + q^{-2} = h^2 + 2$):

$$
  \mathrm{tr}_M
  = -(h^2 + 2)^2 + 5(h^2 + 2) - 9 + \frac{16}{h^2 + 4}
  = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}.
$$
$\qquad\blacksquare$
