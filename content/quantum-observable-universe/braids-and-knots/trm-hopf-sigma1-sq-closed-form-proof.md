The Hecke quadratic relation $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$
gives $\mathrm{tr}_M(\sigma_1^2) = (q - q^{-1})\,\mathrm{tr}_M(\sigma_1) + \mathrm{tr}_M(1)$.
The Markov axioms ([`thm:jones-markov-trace`](#thm:jones-markov-trace))
fix $\mathrm{tr}_M(1) = 1$ and
$\mathrm{tr}_M(\sigma_1) = z := 1/(q^{1/2} + q^{-1/2})$, so
$$
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; (q - q^{-1}) \cdot \frac{1}{q^{1/2} + q^{-1/2}} + 1.
$$
Simplifying the first term:
$\frac{q - q^{-1}}{q^{1/2} + q^{-1/2}} = \frac{(q - q^{-1}) \cdot q^{1/2}}{q + 1} = \frac{q^{3/2} - q^{-1/2}}{q + 1}$.
Multiplying numerator and denominator by $q^{1/2}$ and combining
with $+1$ over common denominator $q(q+1) = q^2 + q$ gives
$\frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}$. Algebraically this
equals $1 + (q-1)/q^{1/2}$, as can be verified by clearing
denominators.

Markov invariance under stabilisation ([`thm:jones-markov-trace`](#thm:jones-markov-trace)
property 3): for $\beta \in H_n(q)$,
$\mathrm{tr}_M(\beta \cdot \sigma_n^{\pm 1}) = z^{\pm 1} \mathrm{tr}_M(\beta)$
when the new generator $\sigma_n$ is disjoint from $\beta$. Since
$\sigma_1^2$ involves only the first generator, its trace in $H_n$
for any $n \geq 2$ coincides with the trace in $H_2$: no
stabilisation factor enters because the new strand is unlinked from
the closure of $\sigma_1^2$. ∎
