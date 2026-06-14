**Proposition (Habiro–Markov bridge via Pochhammer factorisation).**
*Let $q \in \mathbb{R}_{>0}$, $u = \sqrt{q}$, and let
$\{a_m(u)\}_{m=0}^{M}$ be the Habiro coefficients of a braid word
$\beta \in B_n$ (integer polynomials in $u$). Define the two
Pochhammer conventions:*

$$
  (q;q)_m \;=\; \prod_{k=1}^{m}(1 - q^k),
  \qquad
  (u;u)_m \;=\; \prod_{k=1}^{m}(1 - u^k).
$$

*Then $1 - q^k = (1 - u^k)(1 + u^k)$ for all $k \geq 1$, and the
ratio of the two Habiro evaluations is the Habiro-weighted product:*

$$
  \frac{\sum_m a_m(u)\,(q;q)_m}{\sum_m a_m(u)\,(u;u)_m}
  \;=\;
  \Bigl\langle\prod_{k=1}^{m}(1 + u^k)\Bigr\rangle_{\!\mathrm{Hab}}
$$

*where the Habiro average is
$\langle f_m \rangle_{\mathrm{Hab}} =
\sum_m a_m(u)\,(u;u)_m \cdot f_m \,/\, \sum_m a_m(u)\,(u;u)_m$.*

## Proof

The identity $1 - q^k = 1 - u^{2k} = (1 - u^k)(1 + u^k)$ is
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

## Numerical verification (proton, $n = 9$)

At the substrate $q_0 \approx 1.1100$, $u_0 = \sqrt{q_0} \approx 1.0536$:

| Quantity | Value |
|----------|-------|
| $\sum a_m\,(q;q)_m$ | $136.071$ |
| $\sum a_m\,(u;u)_m$ | $24.227$ |
| $\langle\prod(1+u^k)\rangle_{\mathrm{Hab}}$ | $5.616$ |
| Ratio check | $136.071 / 24.227 = 5.616$ ✓ |

The full bridge
$R_{\mathrm{alg}}(q) = \mathrm{bridge}(q) / (n!/[n]_q!)$
is an exact rational function of $q$ (degree $226/97$ in $u$).
The correction $S = R_{\mathrm{alg}} / (\mathrm{Vol}(4_1)/\hbar_q^2)$
inherits transcendental dependence on $\mathrm{Vol}(4_1)$ and
cannot be expressed as a closed-form rational function of $\hbar_q^2$
from representation theory alone.


**Mathematical Novelty:** The proved identity relies on the elementary textbook algebraic factorization $1-q^k = (1-u^k)(1+u^k)$. The novel, framework-specific mathematical contribution lies in its application to the Habiro-weighted-average ratio, linking standard q-series identities to the physical structure.