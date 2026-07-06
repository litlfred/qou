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
