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
