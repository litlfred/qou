## Proof

The three claims — exact transfer-matrix reduction, additive energy
decomposition, and the $\binom{A}{2}$ step count — follow from the Hecke
relation and far commutativity.

1. **Exact reduction at each generator.** At $\sigma_i$ the product of
   the $k_i = A - i - 1$ crossing factors $C_{ij}(\sigma_i) = c_j\sigma_i + d_j$
   reduces, via $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, to a single
   linear form $a_i\sigma_i + b_i$, with $(a_i, b_i)$ obeying the stated
   $2\times2$ transfer recurrence from $(a_0, b_0) = (0, 1)$. This is
   exact: the Hecke relation closes the span $\{1, \sigma_i\}$, so no
   higher powers survive (the "$\infty$-jet" equals the $k_i$-jet).

2. **Additivity.** Distant generators commute, so on the
   Gröbner--Shirshov normal form
   ([nuclear reduction](#prop:nuclear-groebner-reduction)) the Markov
   trace factorises across generators, giving
   $\tfrac12\ln(\mathrm{tr}\,\overline{\mathrm{tr}}) =
   \tfrac12\sum_i \ln(\hat V_i \overline{\hat V_i})$ with
   $\hat V_i = z\,a_i + b_i$ — the formalised `energy_additive`.

3. **Step count and $\beta$-decay locality.** The total work is
   $\sum_{i=0}^{A-2} k_i = \sum_{i=0}^{A-2}(A - i - 1) = \binom{A}{2}$,
   and a single type-change at position $p$ alters only generators
   $i \le p$ (the formalised `beta_decay_locality`), the higher
   generators cancelling exactly — the 1-jet variation.

The Lean sibling proves `energy_additive` and
`beta_decay_locality` outright, and states the assembly
`generator_volume_decomposition_prop` as the decomposition identity
itself — the categorically-defined energy
`generator_volume_decomposition` equals the generator-volume sum
$\sum_i V_i$ by construction (proved by `rfl`), with the substantive
transfer-matrix, additivity, and locality content carried by the
sublemmas above. $\square$
