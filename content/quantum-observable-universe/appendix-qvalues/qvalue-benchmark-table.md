All predictions use $\approx$ (derived from $q$, zero fitting parameters).
Experimental values from NNDC/ENSDF with stated uncertainties.

| Nucleus | Transition | $\mathcal{Q}_{\mathrm{pred}}$ | $\pm\delta\mathcal{Q}$ | $\mathcal{Q}_{\mathrm{exp}}$ | $\pm\delta\mathcal{Q}_{\mathrm{exp}}$ | Error | $F_{I_{10}}$ | Parity |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ${}^3\mathrm{H}$ | $\to {}^3\mathrm{He}$ | $0.01849$ | $3 \times 10^{-10}$ | $0.01861$ | $10^{-5}$ | $-0.6\%$ | $1.000$ | $oA \to oA$ |
| ${}^{14}\mathrm{C}$ | $\to {}^{14}\mathrm{N}$ | $0.15300$ | $2 \times 10^{-9}$ | $0.15648$ | $4 \times 10^{-5}$ | $-2.2\%$ | $1.000$ | $ee \to oo$ |
| ${}^{60}\mathrm{Co}$ | $\to {}^{60}\mathrm{Ni}$ | $0.33071$ | $5 \times 10^{-9}$ | $0.31817$ | $1.3 \times 10^{-4}$ | $+3.9\%$ | $0.969$ | $oo \to ee$ |
| ${}^{90}\mathrm{Sr}$ | $\to {}^{90}\mathrm{Y}$ | $0.56168$ | $7 \times 10^{-9}$ | $0.54590$ | $7 \times 10^{-5}$ | $+2.9\%$ | $1.000$ | $ee \to oo$ |
| ${}^{137}\mathrm{Cs}$ | $\to {}^{137}\mathrm{Ba}$ | $0.53965$ | $7 \times 10^{-9}$ | $0.51400$ | $2.1 \times 10^{-4}$ | $+5.0\%$ | $0.996$ | $oA \to oA$ |
| ${}^{210}\mathrm{Bi}$ | $\to {}^{210}\mathrm{Po}$ | $1.28016$ | $2 \times 10^{-8}$ | $1.16270$ | $6 \times 10^{-5}$ | $+10.1\%$ | $0.991$ | $oo \to ee$ |

**MAE $\approx 4.1\%$, RMS $\approx 5.1\%$** (with $I_{10}$ pairing correction).

The prediction uncertainty $\delta\mathcal{Q}$ is propagated from
$\delta q \approx 1.4 \times 10^{-9}$ (CODATA 2022 uncertainty on
$m_\mu/m_e$).  It is negligible compared to the systematic error:
the dominant residuals are structural (spectator overcounting for
heavy nuclei), not from $q$ precision.

**Error pattern by parity transition:**

- $ee \to oo$: $-2.2\%$, $+2.9\%$ (small, mixed sign — well-captured)
- $oA \to oA$: $-0.6\%$, $+5.0\%$ (moderate)
- $oo \to ee$: $+3.9\%$, $+10.1\%$ (systematic positive — $I_{10}$
  reduces but does not eliminate the pairing deficit)

The $oo \to ee$ residual correlates with $A$: larger nuclei have
more generators contributing small positive log-ratios that
accumulate.  The $I_{10}$ correction $(1 - \delta_{\mathrm{pp}}/Z)
(1 - \delta_{\mathrm{nn}}/N)$ scales as $1 - O(1/Z)$, which
weakens for large $Z$.  A higher-order correction involving
the converting generator's chain length may resolve this.
