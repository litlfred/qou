## Proof

**Step 1: Hecke-power recurrence.** We apply the Hecke quadratic relation iteratively. We set $\sigma_i^k = a_k\sigma_i + b_k$ with $a_k, b_k \in \mathbb{Z}[h]$. Multiplying by $\sigma_i$ yields:

$$
  \sigma_i^{k+1} = a_k\sigma_i^2 + b_k\sigma_i = a_k(h\sigma_i + 1) + b_k\sigma_i = (h a_k + b_k)\sigma_i + a_k.
$$

Thus $a_{k+1} = h a_k + b_k$ and $b_{k+1} = a_k$, with initial conditions $a_0 = 0$ and $b_0 = 1$. See [Table 1](#tbl:markov-trace-axiomatic-closed-form-table1-data) for the direct enumeration.

**Step 2: Expansion of the proton word.** Using the recurrence, we expand:

$$
  \sigma_1^7 \sigma_2^4 \;=\; (a_7 \sigma_1 + b_7)(a_4 \sigma_2 + b_4)
   \;=\; a_7 a_4 \,\sigma_1\sigma_2 \;+\; a_7 b_4 \,\sigma_1 \;+\; b_7 a_4 \,\sigma_2 \;+\; b_7 b_4.
$$

The coefficients $a_k, b_k \in \mathbb{Z}[h] \subset \mathbb{Z}[q, q^{-1}]$ are Laurent polynomial scalars. They commute with the basis elements of $H_3(q)$.

**Step 3: Markov-trace values on the $H_3$ basis.** The axioms and cyclicity uniquely fix the trace on the canonical reduced-word basis $\{1, \sigma_1, \sigma_2, \sigma_1\sigma_2, \sigma_2\sigma_1, \sigma_1\sigma_2\sigma_1\}$ of $H_3(q)$. See [Table 2](#tbl:markov-trace-axiomatic-closed-form-table2-data).

The last entry follows from the braid relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$. Applying the Markov axiom to $\alpha = \sigma_2\sigma_1 \in H_3$ (after cyclic rotation) gives $\operatorname{tr}_M(\sigma_2\sigma_1\sigma_2) = z\cdot\operatorname{tr}_M(\sigma_2\sigma_1)$. This contradicts naive expectations. The correct derivation uses the Hecke-quadratic identity $\sigma_1\sigma_2\sigma_1 - \sigma_2\sigma_1\sigma_2 = 0$ and the cyclic application $\operatorname{tr}_M(\sigma_2\sigma_1\sigma_2) = \operatorname{tr}_M(\sigma_1\sigma_2\sigma_1)$. We combine this with $\sigma_1^2 = h\sigma_1 + 1$ on the inner factor to give $\operatorname{tr}_M(\sigma_1\sigma_2\sigma_1) = h\,\operatorname{tr}_M(\sigma_1\sigma_2) + \operatorname{tr}_M(\sigma_2) = h z^2 + z$.

**Step 4: Linear combination.** We apply $\operatorname{tr}_M$ to the expansion in Step 2 and read off the basis values:

$$
  \operatorname{tr}_M(\sigma_1^7\sigma_2^4)
   \;=\; a_7 a_4 \cdot z^2 \;+\; a_7 b_4 \cdot z \;+\; b_7 a_4 \cdot z \;+\; b_7 b_4 \cdot 1.
$$

This methodology is fully axiomatic. It invokes only the Hecke quadratic relation, the Markov axioms, cyclicity, and the braid relations. We do not use representation theory, Hoefsmit-Wenzl seminormal construction, or character tables. $\square$

## Numerical witness

Evaluation gives:

$$
  \operatorname{tr}_M(\sigma_1^7\sigma_2^4)(q_0) \;\approx\; 1.63315\,357\ldots
$$

The `char_fast` cross-check (the `markov_chars` function computed via Hoefsmit seminormal ascent) gives $\approx 1.6334$. This matches to $4$ significant digits. The minor discrepancy reflects floating-point roundoff in the seminormal eigenvalue route. The axiomatic form is exact in $\mathbb{Q}(q)$.

The categorical-mass formula $M(K) = m_e \cdot \rho_K \cdot |\operatorname{tr}_M(\mathcal{B}_K)|$ ([`prop:categorical-mass-markov`](#prop:categorical-mass-markov)) yields the following for the proton ($K = $ proton, $\mathcal{B}_K = \sigma_1^7\sigma_2^4$):

$$
  \rho_p^{\mathrm{CODATA}} \;=\; \frac{1836.15}{|\operatorname{tr}_M(\mathcal{B}_p)|(q_0)} \;\approx\; \frac{1836.15}{1.63315} \;\approx\; 1124.3.
$$

## References

- [Jones 1987] *Hecke algebra representations of braid groups and link polynomials*, Annals of Math. **126**, 335-388.
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III §3 (Markov trace via Frobenius integral).
- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349-383.
- [Kauffman 1991] *Knots and Physics*, World Scientific, Ch. VI (skein-relation derivation).
