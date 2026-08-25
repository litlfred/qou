## Statement

Let $\beta_{{}^4\mathrm{He}}$ be the canonical atomic braid word for $^4\mathrm{He}$ on $H_{12}(q)$. It has 47 crossings on 12 strands with three operator-valued inter-nucleon interfaces (pp at gen 2, pn at gen 5, nn at gen 8). We define the per-partition contribution:
$$
  c_\lambda(q_0) \;:=\; y_\lambda(q_0) \cdot \chi^\lambda_q\!\bigl(\beta_{{}^4\mathrm{He}}\bigr),
$$
where $y_\lambda$ is the Wenzl weight ([`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical)) and $\chi^\lambda_q$ is the Hoefsmit character. We have:
$$
  \sum_{\lambda \vdash 12} c_\lambda(q_0) \;=\; \mathrm{tr}_M\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)(q_0).
$$

**Proposition (conditional on [`he4-canonical-tr-m-block-fingerprint.witness.json`](computations/he4-canonical-tr-m-block-fingerprint.witness.json)).**
The two-row stratum $\Lambda^2(12)$ ([`def:two-row-stratum`](#def:two-row-stratum)) carries at least $80\,\%$ of the canonical Markov trace at the substrate parameter:
$$
  \frac{\bigl|\sum_{\lambda \in \Lambda^2(12)} c_\lambda(q_0)\bigr|}
       {\bigl|\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0)\bigr|}
  \;\ge\; 0.80.
$$

## Empirical verification

The trace is $\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0) \approx 0.160974145442$. The two-row-stratum ratio is **exactly $1$**: all $70$ partitions of $12$ with more than two rows contribute $0$, so the seven partitions of $\Lambda^2(12)$ carry the entire trace. The bound $\ge 0.80$ asserted above is therefore satisfied, and since the whole trace lies in $\Lambda^2(12)$ so do the top five blocks.

| rank | $\lambda \vdash 12$ | $\dim_\lambda$ | $y_\lambda(q_0)$ | $\chi^\lambda_q(\beta_{{}^4\mathrm{He}})$ | $c_\lambda$ | $\%$ of $\lvert$total$\rvert$ |
|---:|---|---:|---:|---:|---:|---:|
| 1 | $(9, 3)$ | 154 | $+1.7441\,e{-3}$ | $+27.3348$ | $+4.7676\,e{-2}$ | $29.617$ |
| 2 | $(8, 4)$ | 275 | $+1.1941\,e{-3}$ | $+30.2676$ | $+3.6142\,e{-2}$ | $22.452$ |
| 3 | $(10, 2)$ | 54 | $+2.3704\,e{-3}$ | $+10.4630$ | $+2.4802\,e{-2}$ | $15.407$ |
| 4 | $(11, 1)$ | 11 | $+3.1003\,e{-3}$ | $+7.3910$ | $+2.2915\,e{-2}$ | $14.235$ |
| 5 | $(7, 5)$ | 297 | $+6.9619\,e{-4}$ | $+21.7770$ | $+1.5161\,e{-2}$ | $9.418$ |
| 6 | $(12)$ | 1 | $+3.9658\,e{-3}$ | $+2.4198$ | $+9.5965\,e{-3}$ | $5.962$ |
| 7 | $(6, 6)$ | 132 | $+2.2873\,e{-4}$ | $+20.4727$ | $+4.6827\,e{-3}$ | $2.909$ |
|   | **all $\Lambda^2(12)$** |     |                |          | $+1.6097\,e{-1}$ | $\mathbf{100.000}$ |

The trivial representation $(12)$ contributes $5.962\,\%$ and the sign representation $(1^{12})$ vanishes ($0$ at 50 dps). The top five blocks carry $91.130\,\%$ cumulatively.

## Structural interpretation

The two-row stratum carries the SU(2) Schur-Weyl image. Partitions with $\ell(\lambda) > 2$ correspond to higher-rank symmetry components absent from the spin-$\tfrac{1}{2}$ pairing observable. The dominance of $\Lambda^2(12)$ is the algebraic fingerprint of $^4\mathrm{He}$ as a $q$-symmetric spin-pairing bound state.

The canonical formalism predicts the top block $\lambda^* = (9, 3)$ via the $\Delta_\lambda$ empirical-tabulation route. This proposition derives the identical fingerprint from the $\Sigma_\lambda y_\lambda \cdot \chi^\lambda_q$ Wedderburn sum.
