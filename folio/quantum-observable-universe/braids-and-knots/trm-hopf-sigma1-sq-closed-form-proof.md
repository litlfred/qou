The Hecke quadratic relation $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$
gives $\mathrm{tr}_M(\sigma_1^2) = (q - q^{-1})\,\mathrm{tr}_M(\sigma_1) + \mathrm{tr}_M(1)$.
The Markov axioms ([Primitive Markov-trace axioms](#rem:markov-axioms-primitive))
fix $\mathrm{tr}_M(1) = 1$ and
$\mathrm{tr}_M(\sigma_1) = z := q^3/(q^2+1)$, so
$$
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; (q - q^{-1}) \cdot \frac{q^3}{q^2 + 1} + 1.
$$
Simplifying the first term: $q - q^{-1} = (q^2-1)/q$, so
$$
  (q - q^{-1})\,z
  \;=\; \frac{q^2 - 1}{q} \cdot \frac{q^3}{q^2+1}
  \;=\; \frac{q^2(q^2-1)}{q^2+1}
  \;=\; \frac{q^2\,h}{[2]_q},
$$
writing $h = q - q^{-1}$ and $[2]_q = q + q^{-1} = (q^2+1)/q$. Adding $1$ over
the common denominator $q^2+1$ gives
$$
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; \frac{q^2 + 1 + q^4 - q^2}{q^2+1}
  \;=\; \frac{q^4 + 1}{q^2 + 1}
  \;=\; \frac{q\,[2]_{q^2}}{[2]_q},
$$
using $q^4 + 1 = q^2 [2]_{q^2}$ and $q^2 + 1 = q\,[2]_q$. No half-integral
power of $q$ appears; the result is rational in $q$.

Stabilisation ([Primitive Markov-trace axioms](#rem:markov-axioms-primitive)
axiom 3 and its $\sigma_n^{-1}$ consequence) scales the trace by
$z$ for an adjoined positive crossing and by
$z_{-} = z - (q - q^{-1})$ for a negative one. Neither case arises
here: $\sigma_1^2$ involves only the first generator, and the Markov
trace is compatible with the tower inclusions
$H_2(q) \subset H_n(q)$, so its trace in $H_n$ for any $n \geq 2$
coincides with the trace in $H_2$ — no stabilisation factor enters
because no new crossing is adjoined. ∎

## Taylor expansion at $q = 1 + \varepsilon$

Split off the polynomial part by division:

$$
  \mathrm{tr}_M(\sigma_1^2) - 1
  \;=\; \frac{q^4 - q^2}{q^2+1}
  \;=\; q^2 - 2 + \frac{2}{q^2+1}.
$$

Substituting $q = 1 + \varepsilon$, the polynomial part contributes
$\varepsilon^2 + 2\varepsilon - 1$ and the rational part expands about a pair of
conjugate poles at $q = \pm i$, i.e. $\varepsilon = -1 \pm i$:

$$
  \bigl[\varepsilon^k\bigr]\,\frac{2}{q^2+1}
  \;=\; (-1)^k\,2^{(1-k)/2}\,
        \sin\!\Bigl(\tfrac{(k+1)\pi}{4}\Bigr),
        \qquad k \geq 0 .
$$

So the series is a damped oscillation of period $8$ in $k$, with radius of
convergence $\sqrt 2$, rather than a binomial series. Its coefficients:

See [Table 1](#tbl:trm-hopf-sigma1-sq-closed-form-table1-data).
