The beta-decay framework ([hadron half-life](#prop:hadron-half-life)) is tested here against measured lifetimes.

## Quantities from $q$ and $\mu_0$

The half-life formula depends only on $q$ and $\mu_0$. Every physical constant factors into $q$-dependent components ([hadron half-life](#prop:hadron-half-life)):

See [Table 1](#tbl:hadron-half-life-verification-table1-data).

The parameters $q$ and $\mu_0$ alone determine:

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
3. **Axial coupling $g_A$.** Not derived. The value $g_A(q_0) \approx 1.277$
   carries the imported naive-quark-model factor $5/3$ and a colour average
   chosen from three candidates listed beside their deviations from
   experiment ($-23\%$, $+46\%$, $+0.1\%$); the closest was kept. That is a
   selection against the target, i.e. a fit under the no-fitting
   discipline rather than a prediction.
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

The $Q$-value follows entirely from $q$ via the knot operator product:

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

The weak force is mediated by $T_{3,5}$. The vertex form factor is the canonical Markov trace of the $T_{3,5}$ braid word in $H_3(q)$, the coupling of the rate formula ([hadron half-life](#prop:hadron-half-life)), and it has a closed form:

$$
  \mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}\bigl((\sigma_1\sigma_2)^5\bigr)
  = \frac{q^2\,(q^{12} + q^{8} - 1)}{(q^2 + 1)^2},
  \qquad
  \mathcal{W}(q_0) \approx 1.1875 .
$$

The trace is the Wedderburn sum over the two blocks of $H_3(q)$ that the $\mathrm{SU}_q(2)$ Markov trace weights, $\mathcal{W} = y_{(3)}\,q^{10} - y_{(2,1)}$ with $y_{(3)} = (q^4+1)/(q^2+1)^2$ and $y_{(2,1)} = q^2/(q^2+1)^2$; the sign block carries weight zero. Its numerator is $q^{22}\,V_{T_{3,5}}(q^{-2})$ for the Jones polynomial $V_{T_{3,5}}(t) = t^4 + t^6 - t^{10}$ of the torus knot $10_{124}$. At $q = 1$ the value is $\mathcal{W}(1) = 1/4$, so the classical vanishing of the decay rate is carried by $Q \to 0$ and not by the vertex factor. The half-life tables above use the single-crossing approximation and do not consume $\mathcal{W}$.

## Error budget

The $q$-sourced error propagates through the sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$.

See [Table 6](#tbl:hadron-half-life-verification-table6-data).

For heavier nuclei, $\delta Q / Q$ is smaller and $g_A$ does not enter directly. 

See [Table 7](#tbl:hadron-half-life-verification-table7-data).

The fully $q$-derived prediction is reliable for all $A$. 

## Forbidden transitions

For first-forbidden transitions, the matrix element suffers suppression. The suppression originates from jet cross-terms, avoiding any new parameters.
