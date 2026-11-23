## Proof

The Hecke quadratic relation $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$
gives $\mathrm{tr}_M(\sigma_1^2) = (q - q^{-1})\,\mathrm{tr}_M(\sigma_1) + \mathrm{tr}_M(1)$.
The Markov axioms ([Primitive Markov-trace axioms](#rem:markov-axioms-primitive))
fix $\mathrm{tr}_M(1) = 1$ and
$\mathrm{tr}_M(\sigma_1) = z := q^3/(q^2+1)$ (**convention D**), so
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

**Contrast with Convention C.** Under the excised convention C ($z = 1/(q^{1/2}+q^{-1/2})$), the product $(q-q^{-1})z$ collapses to $q^{1/2} - q^{-1/2}$ because $q - q^{-1}$ factors as $(q^{1/2}-q^{-1/2})(q^{1/2}+q^{-1/2})$ and C is the reciprocal of the second factor, yielding $1 + (q-1)/q^{1/2}$. Under Convention D ($z_D = q^3/(q^2+1)$), the derivation remains entirely inside the rational function field $\mathbb{Q}(q)$ without adjoining $q^{1/2}$.

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

**Comparison with convention C.** Under convention C the same quantity is
the closed binomial series
$\mathrm{tr}_M(\sigma_1^2) - 1 = \varepsilon\,(1+\varepsilon)^{-1/2}
= \sum_{k \geq 0} \binom{-1/2}{k}\varepsilon^{k+1}$,
with coefficients $1, -\tfrac12, \tfrac38, -\tfrac5{16}, \tfrac{35}{128},
-\tfrac{63}{256}, \tfrac{231}{1024}, \ldots$ and radius of convergence $1$
(branch point at $q = 0$). Neither the binomial form nor those coefficients
holds under convention D; the coefficients above are exact rationals derived
symbolically from the convention-D closed form.
