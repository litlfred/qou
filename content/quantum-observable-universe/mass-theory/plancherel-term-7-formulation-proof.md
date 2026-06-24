Each $\{\lambda : \mathrm{depth}(\lambda) = k\}$ is finite, so each
$\Phi_k$ is a finite $R$-valued sum.  By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the central idempotent $e_\lambda$ has GB-filtration depth
$\mathrm{depth}(\lambda)$, so binning
$\sum_\lambda \tilde w_\lambda \cdot
\log|\int_{A_\lambda} \rho(\beta_\mathcal{K}) \cdot \mathcal{T}|$ by
$\mathrm{depth}(\lambda)$ is the canonical curvature-rank
decomposition of the (logarithmic) Frobenius pairing.  The threshold
$k \geq 4$ is determined by which strata of $Z(H_n(R, q))$ still carry
a distinguished knot ideal — empirically $k_* = 4$.

The total sum is bounded: $\sum_{\lambda \vdash n} \tilde w_\lambda$
is finite for every $n$ and equals $1$ exactly at $q = 1$; at
$q_0 = 1.109978595554181\ldots$ (50 dps) it deviates from $1$ — empirically
$\sum \tilde w_\lambda \approx 1.51$ at $n = 12$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness)
remark on q-deformed alternative). Boundedness of $\Phi_k$ follows
from finiteness of the $\tilde w_\lambda$ together with finiteness
of the per-block log-Frobenius pairings; the absolute-convergence
constant is $\sup_\lambda \tilde w_\lambda \cdot \#\Lambda_k \cdot
\sup_\lambda |\log|\!\int||$, not $1$ as for the classical
Plancherel measure.
$\qquad\blacksquare$
