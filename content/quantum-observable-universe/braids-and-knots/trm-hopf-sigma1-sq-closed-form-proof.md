## Proof

The Hecke quadratic relation $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$ gives
$$
  \mathrm{tr}_M(\sigma_1^2) = (q - q^{-1})\,\mathrm{tr}_M(\sigma_1) + \mathrm{tr}_M(1).
$$
The Markov axioms ([`thm:jones-markov-trace`](#thm:jones-markov-trace)) fix $\mathrm{tr}_M(1) = 1$ and $\mathrm{tr}_M(\sigma_1) = z := 1/(q^{1/2} + q^{-1/2})$, so
$$
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; (q - q^{-1}) \cdot \frac{1}{q^{1/2} + q^{-1/2}} + 1.
$$
Simplifying the first term gives $\frac{q - q^{-1}}{q^{1/2} + q^{-1/2}} = \frac{q^{3/2} - q^{-1/2}}{q + 1}$. Multiplying numerator and denominator by $q^{1/2}$ and combining with $1$ over the common denominator $q^2 + q$ yields $\frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}$. This algebraically equals $1 + (q-1)/q^{1/2}$.

Markov invariance under stabilisation ([`thm:jones-markov-trace`](#thm:jones-markov-trace)) dictates that $\mathrm{tr}_M(\beta \cdot \sigma_n^{\pm 1}) = z^{\pm 1} \mathrm{tr}_M(\beta)$ when $\sigma_n$ is disjoint from $\beta \in H_n(q)$. Since $\sigma_1^2$ involves only the first generator, its trace in $H_n$ for any $n \geq 2$ coincides with the trace in $H_2$. No stabilisation factor enters because the new strand is unlinked from the closure of $\sigma_1^2$. ∎

## Taylor expansion at $q = 1 + \varepsilon$

Substituting $q = 1 + \varepsilon$ and expanding gives a closed binomial series:

$$
  \mathrm{tr}_M(\sigma_1^2) - 1
  \;=\; \varepsilon \cdot (1 + \varepsilon)^{-1/2}
  \;=\; \sum_{k \geq 0} \binom{-1/2}{k} \varepsilon^{k+1}.
$$

The $\varepsilon^k$ coefficients $\binom{-1/2}{k-1}$ for $k \geq 1$ are recorded in [Table 1](#tbl:trm-hopf-sigma1-sq-closed-form-table1-data). This is verified numerically via [`probe_F_n_categorical_derivation.py`](computations/probe_F_n_categorical_derivation.py) ([witness](computations/F-n-categorical-derivation-probe.witness.json)).
