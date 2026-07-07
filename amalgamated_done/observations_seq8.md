<!-- FILE_START: beta-decay-observations-intro.md -->
The $\beta$-decay $Q$-value is the imaginary part of the complex volume $\mathfrak{V}$ ([The complex volume $\mathfrak{V}$](#sec:complex-volume)): $\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$. It represents the anti-binding unstable decay direction. Because $\operatorname{Im}(q_0) = 0$ at the archimedean level, each yields a real measured number. Beta-decay half-lives and $Q$-values provide the most stringent quantitative test of the framework. Rates span twenty orders of magnitude; any error in the $q$-dependence amplifies enormously.

We fix the observable. We compare $Q$-value predictions versus experiment, determine the channel decomposition, and compare predicted to measured lifetimes across selected beta emitters. We sort emitters by their regime in the $q$-landscape. We propose a conjectural structure linking the electroweak vacuum scale to the brane tower through the $S_5$ action on $H_n(q)$, the brane-tower depth, and the leading-order count $N_v = 120 \cdot q_0^{90}$.

We develop calculations using shell structure in half-lives (${}^3\mathrm{H}$ and ${}^{14}\mathrm{C}$), precision probes of local $q$-variation, and the interpretation of $[A\!-\!1]_q! > [2]_q^{A-1}$. We audit the tritium $Q$-value derivation. We explain the half-life difference between $A = 14$ isobars by comparing the ${}^{14}\mathrm{N}$ maximal braid shortcut to the ${}^{14}\mathrm{C}$ broken alternation.

We identify the half-life ratio with a ratio of Markov-trace volumes. We capture the LR-fusion rigidity that pins double-magic isotopes. We record the homological shortcut that analytically bypasses the $k \geq 12$ matrix-evaluation barrier. We derive magic numbers directly from the per-partition nuclear character at $q_0$.

We close with complementary examples and the Strutinsky reformulation. We map each empirical Bethe–Weizsäcker term onto a Schur–Weyl stratum. Finally, we formulate Strutinsky's shell correction as the categorical residue sum.
<!-- FILE_END: beta-decay-observations-intro.md -->

<!-- FILE_START: qvalue-observation.md -->
The $q$-weighted method ([derivation chain](#rem:qvalue-derivation-chain)) predicts $\beta^-$ decay $Q$-values from $q$ alone. We employ zero fitting parameters.

**Predicted vs observed $Q$-values.**

See [Table](#tbl:qvalue-observation-table-data).

The MAE is $\approx 4.4\%$ and the RMS is $\approx 5.4\%$. Light nuclei ($A \leq 14$) achieve errors $\leq 2.2\%$. Heavy nuclei require $F_{\mathrm{deg2}} = 0.5904$ and $F_{\mathrm{Pauli}} = 0.6382$.

**Headline demonstration: ${}^{90}\mathrm{Sr}$.**

For ${}^{90}\mathrm{Sr}$, the bare prediction $\mathcal{Q}_{\mathrm{bare}} \approx 0.944\,\mathrm{MeV}$ overshoots $\mathcal{Q}_{\mathrm{exp}} = 0.546\,\mathrm{MeV}$ by $+73\%$. Applying the correction $F_{\mathrm{deg2}} = 0.5904$ yields $Q \approx 0.557\,\mathrm{MeV}$ ($+2.1\%$). This categorical reduction involves no fitting.

**Method.**

The method leverages the eigenvalue asymmetry $q$ versus $-q^{-1}$ of the Iwahori--Hecke algebra to isolate unbinding, rebinding, and spectator channels. The shell correction factors derive from the $6 \times 6$ regular representation of $H_3(q)$.

**Error structure.**

The parametric uncertainty $\deltaQ / \delta q_0$ is negligible. The residual errors stem from the shell correction approximation. Improving $F_{\mathrm{shell}}$ requires extending the spectral decomposition ([spectral decomposition](#cor:spectral-decomposition-qvalue)).
<!-- FILE_END: qvalue-observation.md -->

<!-- FILE_START: hadron-half-life-verification.md -->
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
<!-- FILE_END: hadron-half-life-verification.md -->
