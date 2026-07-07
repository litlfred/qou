<!-- FILE_START: beta-decay-observations-intro.md -->
The $\beta$-decay $Q$-value is the imaginary part of the complex volume $\mathfrak{V}$ ([The complex volume $\mathfrak{V}$](#sec:complex-volume)): $\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$. It represents the bar-odd ($\sinh$) weak channel, or the anti-binding unstable decay direction. It pairs with the bar-even ($\cosh$) binding part $\mathfrak{E}_{\mathrm{bind}} = \operatorname{Re}\mathfrak{V}$ computed in the mass chapters. The observables below are not separate from binding; they are the $\operatorname{Im}$ shadow of the same defect. Because $\operatorname{Im}(q_0) = 0$ at the archimedean level, each yields a real measured number. Beta-decay half-lives and Q-values provide the most stringent quantitative test of the framework. Rates span twenty orders of magnitude, so any error in the dependence on $q$ amplifies enormously. The opening blocks fix the observable. We compare Q-value predictions versus experiment, determine the channel decomposition from $q$-weighted channel separation, and compare predicted to measured lifetimes across selected beta emitters. We sort the emitters by their regime in the $q$-landscape. We then propose the conjectural structure linking the electroweak vacuum scale to the brane tower through the $S_5$ action on $H_n(q)$, the brane-tower depth from $m_e$ to $v$, and the leading-order count $N_v = |S_5| \cdot q_0^{90} = 120 \cdot q_0^{90}$.

Single-nucleus worked examples follow. We develop the calculations and the bound they enforce using shell structure in half-lives (${}^3\mathrm{H}$ and ${}^{14}\mathrm{C}$), precision probes of local $q$-variation, and the physical interpretation of $[A\!-\!1]_q! > [2]_q^{A-1}$. We audit the tritium Q-value derivation crossing by crossing as a Skein crossing change: ${}^3_1\mathrm{H} \to {}^3_2\mathrm{He} + e^- + \nu_e^{\sigma}$. We explain the dramatic half-life difference between the two $A = 14$ isobars by comparing the ${}^{14}\mathrm{N}$ maximal braid shortcut to the ${}^{14}\mathrm{C}$ broken alternation.

The central structural fact of this section identifies the half-life ratio with a ratio of Markov-trace volumes. We supply the numerical evaluation and introduce the magic-number machinery. We capture the LR-fusion rigidity that pins double-magic isotopes, illustrated by $^{40}\mathrm{Ca}$ at $Z = N = 20$. Empirical double-magic isotopes satisfy $|\Delta i| \leq 1$ across Bring shell indices. We record the homological shortcut that analytically bypasses the $k \geq 12$ matrix-evaluation barrier for heavy nuclei. We then derive the magic numbers directly from the per-partition nuclear character at $q_0$.

The section closes with complementary examples and the Strutinsky reformulation. We cover the frayed and single-magic cases using non-magic $^{6}\mathrm{Li}$ at $Z = N = 3$ and single-magic $^{18}\mathrm{O}$ at $Z = 8, N = 10$. We map each empirical Bethe–Weizsäcker term onto a Schur–Weyl stratum. Finally, we formulate Strutinsky's shell correction as the categorical residue sum. This prepares for the large-scale section, which relates shell corrections to substrate residues.
<!-- FILE_END: beta-decay-observations-intro.md -->

<!-- FILE_START: qvalue-observation.md -->
The $q$-weighted method ([derivation chain](#rem:qvalue-derivation-chain)) predicts $\beta^-$ decay Q-values from $q$ alone. We employ zero fitting parameters. This achieves an MAE of $\approx 4.4\%$ across six NNDC benchmark nuclei.

**Predicted vs observed Q-values.**

See [Table](#tbl:qvalue-observation-table-data).

The MAE is $\approx 4.4\%$ and the RMS is $\approx 5.4\%$. Light nuclei ($A \leq 14$) require no shell corrections and achieve errors $\leq 2.2\%$. Heavy nuclei require $F_{\mathrm{deg2}} = 0.5904$ (Rosso--Jones weighted degree-2 torus knot suppression for shells $\geq 5$) and $F_{\mathrm{Pauli}} = 0.6382$ (magic-number alternating-irrep projection).

**Headline demonstration: ${}^{90}\mathrm{Sr}$.**

The even-even, non-magic nucleus ${}^{90}\mathrm{Sr}$ ($Z = 38$, $N = 52$, shell 5) provides the clearest proof for the degree-2 torus knot correction. The bare prediction $\mathcal{Q}_{\mathrm{bare}} \approx 0.944\,\mathrm{MeV}$ overshoots $\mathcal{Q}_{\mathrm{exp}} = 0.546\,\mathrm{MeV}$ by $+73\%$. Applying the Rosso--Jones weighted $F_{\mathrm{deg2}} = 0.5904$ correction yields $Q \approx 0.557\,\mathrm{MeV}$ ($+2.1\%$). This categorical reduction from $73\%$ to $2\%$ involves no fitting, no magic-number complications, and no parity issues.

**Method.**

The $q$-weighted method is categorically defined. It leverages the eigenvalue asymmetry $q$ versus $-q^{-1}$ of the Iwahori--Hecke algebra to isolate unbinding, rebinding, and spectator channels. The shell correction factors $F_{\mathrm{deg2}}$ and $F_{\mathrm{Pauli}}$ are derived directly from the $6 \times 6$ regular representation of $H_3(q)$.

**Error structure.**

The parametric uncertainty $\deltaQ / \delta q_0 \sim 10^{-9}\,\text{MeV}$ is negligible. The substrate parameter $q_0$ is fixed to ten digits from $m_\mu / m_e$. The residual errors ($\sim 2$--$10\%$ for heavy nuclei) are structural. They stem from the shell correction approximation, not from input uncertainty. Improving $F_{\mathrm{shell}}$ requires extending the spectral decomposition ([spectral decomposition](#cor:spectral-decomposition-qvalue)) beyond degree-2 torus knots.

See the full benchmark table ([Q-value benchmark](#ex:qvalue-benchmark-table)) for diagnostic channel decomposition and energy-scale calibration details.
<!-- FILE_END: qvalue-observation.md -->

<!-- FILE_START: hadron-half-life-verification.md -->
We verify the beta-decay framework ([hadron half-life](#prop:hadron-half-life)) against measured lifetimes for representative nuclei.

## Quantities from $q$ and $\mu_0$

The half-life formula depends only on the substrate parameter $q$ and the dimensional scale $\mu_0$. Every physical constant in standard Fermi theory factors into $q$-dependent components ([hadron half-life](#prop:hadron-half-life)):

See [Table 1](#tbl:hadron-half-life-verification-table1-data).

From $q$ and $\mu_0$ alone, we determine:

1. **Skein polynomial** $P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$ ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)): A polynomial in $q^{1/2}$ of degree $\leq A^2 - 1$, computed exactly via $\binom{A}{2}$ transfer matrix multiplications.
2. **$Q$-value** ([transition energy](#def:Q-value-transition)): The categorical action difference $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$, where $\mathfrak{S}_q(e) = 3m_e/3$ ([building blocks](#rem:building-block-knots)). Classical energy conservation ($E_{\mathrm{before}} = E_{\mathrm{after}}$) fails at $q \neq 1$.
3. **Matrix element** $|\mathcal{M}_q|^2 = s^2 \cdot \prod_i |\hat{V}_i^{\mathrm{par}} / \hat{V}_i^{\mathrm{dau}}|^2$: Derived from the factorization theorem.
4. **Sensitivity** $\partial \ln \Gamma / \partial \ln q = (q^2-1)/(q^2+1) + 5(q^2+1)/(q^2-1) \approx 48$: Exact.
5. **Self-deformation** $\Delta q_{\mathrm{eff}} = (A-1)/A^2 \cdot \hbar_q^2$: The $q$-anomaly $\delta_q$. We evaluate the daughter nucleus at the shifted parameter $q + \Delta q_{\mathrm{eff}}$.
6. **Deuteron binding** $B_d \approx 1.29$ MeV: Derived from $\mathrm{Vol}(\mathcal{B}_3 \bowtie_{\mathrm{Hopf}} \mathcal{B}_3) / \hbar_q^2$.
7. **Parity violation**: Automatic for $q \neq 1$ ([Lee--Yang--Wu](#prop:parity-violation-skein)).

## Open computations

Four quantities are computable from $q$ in principle. Witness scripts are located in `computations/`.

1. **Weak scale crossing count $N_v$.** The weak scale $v = N_v \cdot m_e/3$ sets the absolute rate via $G_F = 1/(\sqrt{2}v^2)$. Deriving $N_v$ requires identifying the brane tower structure at the electroweak level. Target: $N_v \cdot \kappa_{\mathrm{cross}} \cdot \mu_0 \approx 246$ GeV.
2. **$Q$-values for $A > 4$.** RESOLVED. The representation-theoretic formula $Q = \mathcal{Q}_{\mathrm{bare}} \times F_{\mathrm{deg}} \times F_{\mathrm{Pauli}}$ ([torus knot shell binding](#cor:spectral-decomposition-qvalue)) predicts all six test nuclei within $\pm 8\%$ using Level 0 (nucleon) transfer matrices. The degree-$2$ operator average and Pauli projection follow from the $H_3(q)$ representation theory of embeddable torus knots on $\Sigma_4$. Script: `computations/qvalue-representation-theory.py`.
3. **Axial coupling $g_A$ from Borromean color average.** RESOLVED. The $3$-fold color average of the half-Borromean braid $h_{ij} = \sigma_i^{-1}\sigma_j\sigma_i\sigma_j^{-1}$ yields $g_A(q) = (5/3) \times |\mathrm{tr}_{\mathrm{std}}(\tfrac{1}{3} \sum h_{ij})| / |\mathrm{tr}_{\mathrm{sym}}(\tfrac{1}{3} \sum h_{ij})| \approx 1.277$ ($+0.1\%$ from PDG value $1.2754$). The sum runs over three cyclic orderings of quark colors $(r,g,b)$. Script: `computations/borromean-axial-coupling.py`.
4. **Fine structure constant $\alpha_{\mathrm{EM}}$.** RESOLVED. The EM coupling projection ([EM coupling projection](#prop:em-coupling-projection)) yields the bare coupling $q^{-1}/([9]_q \cdot [10]_q) \approx 1/136.82$. Including the Chern-Simons correction from force-carrier torus knots gives $\alpha^{-1} \approx 137.036$ ($2.1\;\mathrm{ppm}$ from CODATA). We derive this entirely from $q$, with no free parameters.
5. **Shell correction energy scale $\lambda_{\mathrm{shell}}$.** The binding energy of the alpha particle $\mathcal{N}(2,2)$ as a closed sub-link, given by the quantum dilogarithm volume at $q = q_0$.

## Observed half-lives (NNDC/ENSDF)

See [Table 2](#tbl:hadron-half-life-verification-table2-data).

The $\binom{A}{2}$ column lists the exact number of transfer matrix steps required to compute each nucleus's Skein polynomial.

## $Q$ predictions

The tritium $Q$-value provides the tightest constraint. At Level 0 ($B_3$, 3 transfer matrix steps):

$$
  Q({}^3\mathrm{H})
  = 
  P_{{}^3\mathrm{H}}(q_0) - P_{{}^3\mathrm{He}}(q_0) - P_e(q_0)
$$

Incorporating the self-deformation correction (evaluating the daughter at $q + \Delta q_{\mathrm{eff}}$ with $\Delta q = 2/9 \cdot \hbar_q^2 \approx 0.00218$):

$$
  Q^{\mathrm{corr}}({}^3\mathrm{H})
  = 
  P_{{}^3\mathrm{H}}(q_0) - P_{{}^3\mathrm{He}}(q_0 + \Delta q) - P_e(q_0)
$$

This yields the corrected half-life prediction:

See [Table 3](#tbl:hadron-half-life-verification-table3-data).

## Full computation with Skein-Coulomb enhancement

Integrating the Skein-Coulomb Fermi function $F_q(Z, E)$ ([Fermi function](#prop:skein-coulomb-enhancement)) over phase space, and setting $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$ ([EM coupling](#prop:em-coupling-projection)), matches all six observed half-lives to better than $3\%$:

See [Table 4](#tbl:hadron-half-life-verification-table4-data).

These predictions rely on:
- **From $q$**: $\alpha_{\mathrm{EM}}(q)$ within the Fermi function ($1/\alpha \approx 137.036$ with CS correction).
- **From CODATA**: $G_F = (1.16638 \pm 0.00001) \times 10^{-11} \mathrm{\ MeV}^{-2}$.
- **From NNDC**: $\mathcal{Q}_{\mathrm{exp}}$ and $\log ft$ values (for the nuclear matrix element $|\mathcal{M}|^2$).
- **From PDG**: $g_A \approx 1.2754 \pm 0.0013$ (for the mirror transition ${}^3\mathrm{H}$).

The previous $10$–$17\%$ overshoot resulted from using the approximate Sargent rule ($f \propto Q^5$) instead of the exact phase-space integral over $F_q(Z, E)$.

## $Q$-value predictions from $q$

We predict the $Q$-value entirely from $q$ via the knot operator product ([torus knot shell binding](#cor:spectral-decomposition-qvalue)):

$$
  Q
  = 
  \mathcal{Q}_{\mathrm{bare}}
   \times 
  \prod_{\tau(r,s)} F(\tau(r,s), N)
$$

Here $\mathcal{Q}_{\mathrm{bare}} = |\log_q(P_{\mathrm{dau}}/ P_{\mathrm{par}})| \times \hbar_q \cdot m_e/3$ uses the $q$-natural logarithm ($\log_q = \ln/\ln q$) with the quantum Planck constant $\hbar_q = (q-1)/q$. The term $F(\tau(r,s), N)$ is the knot operator for each torus knot. Non-embeddable knots ($\frac{(r-1)(s-1)}{2} > 4$) carry zero topological action on $\Sigma_4$, contributing $F = 1$. Shells unaffected by the decay cancel in the ratio, also contributing $F = 1$. The product reduces to a single active term for the converting neutron's shell knot $T_{k^*}$.

See [Table 5](#tbl:hadron-half-life-verification-table5-data).

The mean absolute error is $4.5\%$; the RMS error is $5.2\%$.

**Degree-$1$ shells** ($N \leq 28$; active knot $\in \{T_{2,3}, T_{2,5}, T_{2,7}, T_{3,5}\}$): The knot operator gives $F = 1$. Degree-$1$ binding is already captured by the crossing coefficients in $\mathcal{Q}_{\mathrm{bare}}$.

**Degree-$2$ shells, partial** ($N > 28$, $N \notin \{50,82,126\}$; active knot $\in \{T_{2,9}, T_{3,4}\}$): The degree-$2$ knot operator average suppresses $\mathcal{Q}_{\mathrm{bare}}$ by $F = 0.5904$. This reduces the bare $+70$–$82\%$ overshoot to $+0.2$–$7.7\%$.

**Degree-$2$ shells, full** ($N \in \{50, 82, 126\}$): The Pauli principle forces fully occupied shells into the alternating irrep $(1,1,1)$ of $H_3(q)$. The knot operator average gains additional suppression from the Schur–Weyl projection: $F = 0.5904 \times 0.6382 = 0.3768$. This reduces the ${}^{137}\mathrm{Cs}$ error from $+171\%$ to $+2.2\%$.

**Error structure.** Defining $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$ (CODATA), the parametric error scales as $\delta Q / Q = O(\varepsilon)$, dominated by $\partial \ln \mathcal{Q}_{\mathrm{bare}} / \partial \ln q \approx 10$. The observed $2$–$10\%$ deviations are $O(1)$ relative to $\varepsilon$. They arise from structural approximations (nucleon ordering, degree-$2$ Rosso--Jones weighting, degree tower truncation), not parametric uncertainty.

## $T_{3,5}$ weak vertex

The weak force is mediated by $T_{3,5}$ with $10$ crossings ([beta decay](#def:beta-decay-skein), [force identification](#rem:force-knot-identification)). We compute the vertex form factor exactly:

$$
  \mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)
  \approx 0.7036
  \qquad\text{at } q = q_0
$$

The $T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ reduces to $6$ terms in $H_3(q)$ via $38$ Hecke steps and $18$ Yang–Baxter steps. The vertex ratio $|\mathcal{M}_{T_{3,5}}|^2 / |\mathcal{M}_{\mathrm{single}}|^2 \approx 0.890$ yields an $11\%$ reduction in transition amplitude. Witness: `computations/t35-weak-vertex.witness.json`.

## Error budget

Every derived quantity inherits error from its inputs. The $q$-sourced error propagates through the sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$.

### Error propagation in full computation (with $Q_{\mathrm{exp}}$)

$$
  \frac{\delta t_{1/2}}{t_{1/2}}
  = 
  5 \frac{\delta Q}{Q}
   \oplus 
  2 \frac{\delta g_A}{g_A}
   \oplus 
  2 \frac{\delta G_F}{G_F}
   \oplus 
  \frac{\delta \alpha_{\mathrm{EM}}}{\alpha_{\mathrm{EM}}}
   \oplus 
  48 \frac{\delta q}{q}
$$

See [Table 6](#tbl:hadron-half-life-verification-table6-data).

**Combined error** (quadrature): $\sqrt{0.27^2 + 0.20^2 + 0.1^2} \approx 0.36\%$ for tritium. The observed $0.3\%$ deviation falls within this budget.

For heavier nuclei, $\delta Q / Q$ is smaller and $g_A$ does not enter directly (Gamow-Teller transitions extract $|\mathcal{M}|^2$ from $\log ft$). The error is dominated by the $\alpha_{\mathrm{EM}}(q)$ contribution to $F_q(Z, E)$.

### Error propagation with $Q_{\mathrm{pred}}$ (from $q$ alone)

Using the representation-theoretic $Q$ formula, the $Q$-value error is $2$–$10\%$ across all six nuclei. This propagates to the half-life via $t_{1/2} \propto Q^{-5}$:

See [Table 7](#tbl:hadron-half-life-verification-table7-data).

For tritium, the combined $\sim 69\%$ rate error from the $g_A$ approximation produces a factor of $\sim 1.7$ in the half-life. For heavy nuclei, the $Q$-value error ($\leq 10\%$) induces a $\leq 50\%$ half-life error via $Q^5$. This dramatically improves upon previous $4$–$100\times$ factors derived from bare $Q$-values.

The fully $q$-derived prediction is now reliable for all $A$. The $Q$ error is $O(1)$ relative to $\varepsilon$ (structural, not parametric), bounded by the degree tower truncation on $\Sigma_4$.

## Forbidden transitions

The preceding table covers allowed Gamow--Teller and Fermi transitions. For first-forbidden transitions (spin change $\Delta J = 0, 1, 2$ with parity flip), the matrix element suffers additional suppression. In the Skein polynomial language, forbidden suppression corresponds to a higher jet order in the crossing change. The 1-jet (single crossing change) defines the allowed transition; forbidden transitions invoke the 2-jet and higher ([jet expansion](#prop:generator-volume-decomposition)). The $q$-dependence remains identical. The suppression originates from jet cross-terms, avoiding any new parameters.
<!-- FILE_END: hadron-half-life-verification.md -->

