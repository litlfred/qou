The $q$-weighted method ([derivation chain](#rem:qvalue-derivation-chain))
predicts $\beta^-$ decay Q-values from $q$ alone, with zero fitting
parameters and MAE $\approx 4.9\%$ across all six NNDC benchmark
nuclei.

**Predicted vs observed Q-values.**

| Decay | $\mathcal{Q}_{\mathrm{exp}}$ (MeV) | $\mathcal{Q}_q$ (MeV) | $\delta$ | $F_{\mathrm{shell}}$ |
|:---:|:---:|:---:|:---:|:---:|
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ | $0.01861 \pm 0.00001$ | $\approx 0.01849$ | $-0.6\%$ | $1.000$ |
| ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$ | $0.15648 \pm 0.00004$ | $\approx 0.15300$ | $-2.2\%$ | $1.000$ |
| ${}^{60}\mathrm{Co} \to {}^{60}\mathrm{Ni}$ | $0.31817 \pm 0.00013$ | $\approx 0.34116$ | $+7.2\%$ | $0.595$ |
| ${}^{90}\mathrm{Sr} \to {}^{90}\mathrm{Y}$ | $0.54590 \pm 0.00007$ | $\approx 0.56168$ | $+2.9\%$ | $0.595$ |
| ${}^{137}\mathrm{Cs} \to {}^{137}\mathrm{Ba}$ | $0.51400 \pm 0.00021$ | $\approx 0.54163$ | $+5.4\%$ | $0.380$ |
| ${}^{210}\mathrm{Bi} \to {}^{210}\mathrm{Po}$ | $1.16270 \pm 0.00006$ | $\approx 1.29175$ | $+11.1\%$ | $0.595$ |

MAE $\approx 4.9\%$, RMS $\approx 6.0\%$.  Light nuclei ($A \leq 14$)
need no shell corrections and achieve $\leq 2.2\%$.  Heavy nuclei
require $F_{\mathrm{deg2}} = 0.5949$ (degree-2 torus knot suppression
for shells $\geq 5$) and $F_{\mathrm{Pauli}} = 0.6382$ (magic-number
alternating-irrep projection).

**Method distinction.** The $q$-weighted method is *categorically
defined* — it uses the eigenvalue asymmetry $q$ vs $-q^{-1}$ of the
Iwahori--Hecke algebra to separate unbinding, rebinding, and spectator
channels.  The shell correction factors $F_{\mathrm{deg2}}$ and
$F_{\mathrm{Pauli}}$ are derived from the $6 \times 6$ regular
representation of $H_3(q)$, not fitted.  The naive Lagrangian and
Dirac methods (MAE $\approx 45\%$ and $\approx 71\%$ respectively)
lack this channel separation and dilute the signal by summing $A - 1$
generator contributions equally.

**Error structure.** The parametric uncertainty
$\delta\mathcal{Q}_q / \delta q_0 \sim 10^{-9}\;\text{MeV}$ is
negligible (the substrate parameter $q_0$ is known to ten digits from
$m_\mu / m_e$).  The residual errors ($\sim 5$--$11\%$ for heavy
nuclei) are *structural* — they arise from the shell correction
approximation, not from input uncertainty.  Improving $F_{\mathrm{shell}}$
requires extending the spectral decomposition
([spectral decomposition](#cor:spectral-decomposition-qvalue)) beyond
degree-2 torus knots.

See the full benchmark table ([Q-value benchmark](#ex:qvalue-benchmark-table))
for diagnostic channel decomposition and energy-scale calibration details.
