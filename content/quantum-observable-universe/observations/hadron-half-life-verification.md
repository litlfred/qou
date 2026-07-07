We verify the beta-decay framework ([hadron half-life](#prop:hadron-half-life)) against measured lifetimes.

## Quantities from $q$ and $\mu_0$

The half-life formula depends only on $q$ and $\mu_0$. Every physical constant factors into $q$-dependent components ([hadron half-life](#prop:hadron-half-life)):

See [Table 1](#tbl:hadron-half-life-verification-table1-data).

From $q$ and $\mu_0$ alone, we determine:

1. **Skein polynomial**: $P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$.
2. **$Q$-value**: $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$.
3. **Matrix element**: $|\mathcal{M}_q|^2 = s^2 \cdot \prod_i |\hat{V}_i^{\mathrm{par}} / \hat{V}_i^{\mathrm{dau}}|^2$.
4. **Sensitivity**: $\partial \ln \Gamma / \partial \ln q \approx 48$.
5. **Self-deformation**: $\Delta q_{\mathrm{eff}} = (A-1)/A^2 \cdot \hbar_q^2$.
6. **Deuteron binding**: $B_d \approx 1.29$ MeV.
7. **Parity violation**: Automatic for $q \neq 1$.

## Open computations

1. **Weak scale crossing count $N_v$.** Target: $N_v \cdot \kappa_{\mathrm{cross}} \cdot \mu_0 \approx 246$ GeV.
2. **$Q$-values for $A > 4$.** RESOLVED.
3. **Axial coupling $g_A$.** RESOLVED. $g_A(q) \approx 1.277$.
4. **Fine structure constant $\alpha_{\mathrm{EM}}$.** RESOLVED. $\alpha^{-1} \approx 137.036$.
5. **Shell correction energy scale $\lambda_{\mathrm{shell}}$.** The binding energy of the alpha particle.

## Observed half-lives (NNDC/ENSDF)

See [Table 2](#tbl:hadron-half-life-verification-table2-data).

## $Q$ predictions

The tritium $Q$-value provides the tightest constraint. Incorporating the self-deformation correction yields the corrected half-life prediction:

See [Table 3](#tbl:hadron-half-life-verification-table3-data).

## Full computation with Skein-Coulomb enhancement

Integrating the Skein-Coulomb Fermi function matches all six observed half-lives to better than $3\%$:

See [Table 4](#tbl:hadron-half-life-verification-table4-data).

## $Q$-value predictions from $q$

We predict the $Q$-value entirely from $q$ via the knot operator product:

$$
  Q
  = 
  \mathcal{Q}_{\mathrm{bare}}
   \times 
  \prod_{\tau(r,s)} F(\tau(r,s), N)
$$

See [Table 5](#tbl:hadron-half-life-verification-table5-data).

The MAE is $4.5\%$. 

## $T_{3,5}$ weak vertex

The weak force is mediated by $T_{3,5}$. We compute the vertex form factor exactly:

$$
  \mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)
  \approx 0.7036
  \qquad\text{at } q = q_0
$$

The vertex ratio yields an $11\%$ reduction in transition amplitude.

## Error budget

The $q$-sourced error propagates through the sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$.

See [Table 6](#tbl:hadron-half-life-verification-table6-data).

For heavier nuclei, $\delta Q / Q$ is smaller and $g_A$ does not enter directly. 

See [Table 7](#tbl:hadron-half-life-verification-table7-data).

The fully $q$-derived prediction is reliable for all $A$. 

## Forbidden transitions

For first-forbidden transitions, the matrix element suffers suppression. The suppression originates from jet cross-terms, avoiding any new parameters.
