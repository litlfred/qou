## Statement

Let $\beta_{{}^4\mathrm{He}}$ be the canonical atomic braid word for $^4\mathrm{He}$ on $H_{12}(q)$. It has 47 crossings on 12 strands with three operator-valued inter-nucleon interfaces (pp at gen 2, pn at gen 5, nn at gen 8). Define the per-partition contribution:
$$
  c_\lambda(q_0) \;:=\; y_\lambda(q_0) \cdot \chi^\lambda_q\!\bigl(\beta_{{}^4\mathrm{He}}\bigr),
$$
where $y_\lambda$ is the Wenzl weight ([Canonical q-deformed Wedderburn-block weight $\tilde w_\lambda$ and named scalings (BW, LP for all $\lambda$)](#prop:wedderburn-weight-canonical)) and $\chi^\lambda_q$ is the Hoefsmit character. Explicitly:
$$
  \sum_{\lambda \vdash 12} c_\lambda(q_0) \;=\; \mathrm{tr}_M\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)(q_0).
$$

**Proposition (conditional on the recorded canonical ${}^{4}\mathrm{He}$ block fingerprint of $\mathrm{tr}_M$).**
The two-row stratum $\Lambda^2(12)$ ([Two-row Wedderburn stratum $\Lambda^2(n) := \{\lambda \vdash n : \ell(\lambda) \le 2\}$](#def:two-row-stratum)) carries at least $80\,\%$ of the canonical Markov trace at the substrate parameter:
$$
  \frac{\bigl|\sum_{\lambda \in \Lambda^2(12)} c_\lambda(q_0)\bigr|}
       {\bigl|\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0)\bigr|}
  \;\ge\; 0.80.
$$

## Empirical verification

The trace is $\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0) \approx 0.011237417660$. The two-row-stratum ratio is **exactly $1$**: all $70$ partitions of $12$ with more than two rows contribute $0$, so the seven partitions of $\Lambda^2(12)$ carry the entire trace. The bound $\ge 0.80$ asserted above is therefore satisfied, and since the whole trace lies in $\Lambda^2(12)$ so do the top five blocks.

| rank | $\lambda \vdash 12$ | $\dim_\lambda$ | $y_\lambda(q_0)$ | $\chi^\lambda_q(\beta_{{}^4\mathrm{He}})$ | $c_\lambda$ | $\%$ of $\lvert$total$\rvert$ |
|---:|---|---:|---:|---:|---:|---:|
| 1 | $(12)$ | 1 | $+3.9658\,e{-3}$ | $+2.41984$ | $+9.5965\,e{-3}$ | $85.398$ |
| 2 | $(9, 3)$ | 154 | $+1.7441\,e{-3}$ | $+4.14962$ | $+7.2375\,e{-3}$ | $64.406$ |
| 3 | $(11, 1)$ | 11 | $+3.1003\,e{-3}$ | $-1.48208$ | $-4.5950\,e{-3}$ | $-40.890$ |
| 4 | $(8, 4)$ | 275 | $+1.1941\,e{-3}$ | $-2.97948$ | $-3.5577\,e{-3}$ | $-31.659$ |
| 5 | $(10, 2)$ | 54 | $+2.3704\,e{-3}$ | $+0.543341$ | $+1.2880\,e{-3}$ | $11.461$ |
| 6 | $(6, 6)$ | 132 | $+2.2873\,e{-4}$ | $+4.25063$ | $+9.7225\,e{-4}$ | $8.652$ |
| 7 | $(7, 5)$ | 297 | $+6.9619\,e{-4}$ | $+0.424982$ | $+2.9587\,e{-4}$ | $2.633$ |
|   | **all $\Lambda^2(12)$** |     |                |          | $+1.1237\,e{-2}$ | $\mathbf{100.000}$ |

The trivial representation $(12)$ is the single largest block at $85.398\,\%$, and the sign representation $(1^{12})$ vanishes ($0$ at 50 dps). Two blocks enter with the opposite sign — $(11, 1)$ at $-40.890\,\%$ and $(8, 4)$ at $-31.659\,\%$ — so the trace is a partial cancellation *within* the stratum: the positive blocks sum to $172.549\,\%$ of it and the negative to $-72.549\,\%$. The five blocks of largest magnitude sum to $88.715\,\%$.

## Structural interpretation

The two-row stratum carries the SU(2) Schur-Weyl image. Partitions with $\ell(\lambda) > 2$ correspond to higher-rank symmetry components absent from the spin-$\tfrac{1}{2}$ pairing observable. The dominance of $\Lambda^2(12)$ is the algebraic fingerprint of $^4\mathrm{He}$ as a $q$-symmetric spin-pairing bound state. The partial cancellation noted above is *internal* to the stratum and does not weaken that statement: the ratio is exactly $1$ because every $\ell(\lambda) > 2$ block is $0$, not because the two-row blocks happen to add constructively.

The canonical formalism predicts the leading blocks via the $\Delta_\lambda$ empirical-tabulation route, and this proposition derives them independently from the $\Sigma_\lambda y_\lambda \cdot \chi^\lambda_q$ Wedderburn sum. The two routes agree on the leading three, $(12)$, $(9, 3)$, $(11, 1)$, in that order.

The largest single block is now the trivial representation $(12)$, whose character is invariant under any reordering of the braid word and which therefore did not move; it leads because every other block fell past it. That is not a fingerprint of $^4\mathrm{He}$: the trivial representation leads in each of $\mathfrak{p}$, $\mathfrak{n}$, $^2\mathrm{H}$, $^3\mathrm{H}$, $^3\mathrm{He}$ and $^4\mathrm{He}$. The leading **non-trivial** block is $(9, 3)$, in both routes, and it is that block the magic-shell reading refers to.
