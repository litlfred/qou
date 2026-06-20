*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

## Statement

Let $\beta_{{}^4\mathrm{He}}$ denote the canonical
atomic braid word for $^4\mathrm{He}$ on
$H_{12}(q)$ — 47 crossings on 12 strands with three operator-valued
inter-nucleon interfaces (pp at gen 2, pn at gen 5, nn at gen 8), as
emitted by
[`mass_at_3A_proper.atom_braid_word_3A(2, 2)`](computations/mass_at_3A_proper.py).
Define the per-partition contribution
$$
  c_\lambda(q_0) \;:=\; y_\lambda(q_0) \cdot \chi^\lambda_q\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)
$$
with $y_\lambda$ the Wenzl weight
from [`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical)
and $\chi^\lambda_q$ the Hoefsmit per-irrep character. Then
$$
  \sum_{\lambda \vdash 12} c_\lambda(q_0) \;=\; \mathrm{tr}_M\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)(q_0).
$$

**Proposition (conditional on
[`he4-canonical-tr-m-block-fingerprint.witness.json`](computations/he4-canonical-tr-m-block-fingerprint.witness.json)).**
The two-row stratum
$\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}$
of [`def:two-row-stratum`](#def:two-row-stratum) carries at least
$80\,\%$ of the canonical Markov trace at the substrate parameter:
$$
  \frac{\bigl|\sum_{\lambda \in \Lambda^2(12)} c_\lambda(q_0)\bigr|}
       {\bigl|\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0)\bigr|}
  \;\ge\; 0.80.
$$

## Empirical verification

The witness reports $\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0) = 0.05534835$
(dimensionless raw trace). The two-row-stratum ratio is
**$86.6\,\%$**. Top-5 binding-receptive Wedderburn blocks — all in
$\Lambda^2(12)$:

| rank | $\lambda \vdash 12$ | $\dim_\lambda$ | $y_\lambda(q_0)$ | $\chi^\lambda_q(\beta_{{}^4\mathrm{He}})$ | $c_\lambda$ | $\%$ of $\lvert$total$\rvert$ |
|---:|---|---:|---:|---:|---:|---:|
| 1 | $(9, 3)$  | 154 | $+5.87\,e{-4}$ | $+27.33$ | $+1.604\,e{-2}$ | $29.0$ |
| 2 | $(8, 4)$  | 275 | $+4.31\,e{-4}$ | $+30.26$ | $+1.304\,e{-2}$ | $23.6$ |
| 3 | $(10, 2)$ | 54  | $+7.12\,e{-4}$ | $+10.46$ | $+7.45\,e{-3}$  | $13.5$ |
| 4 | $(7, 5)$  | 297 | $+2.62\,e{-4}$ | $+21.77$ | $+5.70\,e{-3}$  | $10.3$ |
| 5 | $(11, 1)$ | 11  | $+7.67\,e{-4}$ | $+7.39$  | $+5.67\,e{-3}$  | $10.2$ |
|   |           |     |                |          | top-5 cum         | $\mathbf{86.5}$ |

The trivial rep $(12)$ contributes only $2.9\,\%$; the sign rep
$(1^{12})$ contributes $4.7 \times 10^{-10}$ (sub-1e-9).

## Structural interpretation

The two-row stratum carries the
SU(2) Schur-Weyl image. Partitions
with $\ell(\lambda) > 2$ correspond to higher-rank symmetry
components absent from the spin-$\tfrac{1}{2}$ pairing observable.
The dominance of $\Lambda^2(12)$ at $86.6\,\%$ is the algebraic
fingerprint of $^4\mathrm{He}$ as a $q$-symmetric spin-pairing
bound state — a substrate-derived characterisation of the
magic-shell coupling.

The top block $\lambda^* = (9, 3)$ matches the prediction from
[`delta_lambda_2row_stratum_analysis.py`](computations/delta_lambda_2row_stratum_analysis.py),
which arrived at the same dominant-partition fingerprint via the
$\Delta_\lambda$ empirical-tabulation route. The two derivations
are independent: $\Delta_\lambda$ from per-partition mass-anchor
residuals, this proposition from the canonical
$\Sigma_\lambda y_\lambda \cdot \chi^\lambda_q$ Wedderburn sum.
