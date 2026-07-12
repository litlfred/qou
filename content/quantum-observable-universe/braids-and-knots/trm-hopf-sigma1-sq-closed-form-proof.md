## Proof

The Hecke quadratic relation $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$
gives $\mathrm{tr}_M(\sigma_1^2) = (q - q^{-1})\,\mathrm{tr}_M(\sigma_1) + \mathrm{tr}_M(1)$.
The Markov axioms ([`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive))
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

Stabilisation ([`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive)
axiom 3 and its $\sigma_n^{-1}$ consequence) scales the trace by
$z$ for an adjoined positive crossing and by
$z_{-} = z - (q - q^{-1})$ for a negative one. Neither case arises
here: $\sigma_1^2$ involves only the first generator, and the Markov
trace is compatible with the tower inclusions
$H_2(q) \subset H_n(q)$, so its trace in $H_n$ for any $n \geq 2$
coincides with the trace in $H_2$ — no stabilisation factor enters
because no new crossing is adjoined. ∎

## Taylor expansion at $q = 1 + \varepsilon$

Substituting $q = 1 + \varepsilon$ and expanding gives a closed
binomial series:

$$
  \mathrm{tr}_M(\sigma_1^2) - 1
  \;=\; \varepsilon \cdot (1 + \varepsilon)^{-1/2}
  \;=\; \sum_{k \geq 0} \binom{-1/2}{k} \varepsilon^{k+1}.
$$

The $\varepsilon^k$ coefficients $\binom{-1/2}{k-1}$ for $k \geq 1$
are:

See [Table 1](#tbl:trm-hopf-sigma1-sq-closed-form-table1-data).

The coefficients are verified numerically via
[`probe_F_n_categorical_derivation.py`](computations/probe_F_n_categorical_derivation.py)
([witness](computations/F-n-categorical-derivation-probe.witness.json),
2/2 assertions pass).
