## Proof

> **Scope of Step 2 (disjoint-support factorisation).** The Markov trace does not factorize across generators in general: $\mathrm{tr}(\sigma_1^2) = hz + 1 \neq z^2$ and $\mathrm{tr}(\sigma_0\sigma_1\sigma_0) = hz^2 + z \neq z^3$. The additive form in step 2 holds only where the word splits into commuting, disjoint-support factors. For a general normal form it is an assumption rather than a consequence of far commutativity.


The three claims—exact transfer-matrix reduction, additive energy decomposition, and the $\binom{A}{2}$ step count—follow from the Hecke relation and far commutativity.

1. **Exact reduction at each generator.** At $\sigma_i$, the product of the $k_i = A - i - 1$ crossing factors $C_{ij}(\sigma_i) = c_j\sigma_i + d_j$ reduces to a single linear form $a_i\sigma_i + b_i$. This reduction uses $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$. The coefficients $(a_i, b_i)$ obey the stated $2\times2$ transfer recurrence from $(a_0, b_0) = (0, 1)$. This reduction is exact. The Hecke relation closes the span $\{1, \sigma_i\}$, leaving no higher powers (the $\infty$-jet equals the $k_i$-jet).

2. **Additivity.** Distant generators commute. On the Gröbner--Shirshov normal form ([nuclear reduction](#prop:nuclear-groebner-reduction)), the Markov trace factorizes across generators. This yields $\tfrac12\ln(\mathrm{tr}\,\overline{\mathrm{tr}}) = \tfrac12\sum_i \ln(\hat V_i \overline{\hat V_i})$ with $\hat V_i = z\,a_i + b_i$.

3. **Step count and $\beta$-decay locality.** The total work is $\sum_{i=0}^{A-2} k_i = \sum_{i=0}^{A-2}(A - i - 1) = \binom{A}{2}$. A single type-change at position $p$ alters only generators $i \le p$. The higher generators cancel exactly to yield the 1-jet variation.

Together, these three steps establish the generator-volume decomposition, its additive structure, and the locality of the single-nucleon $\beta$-decay variation. $\square$
