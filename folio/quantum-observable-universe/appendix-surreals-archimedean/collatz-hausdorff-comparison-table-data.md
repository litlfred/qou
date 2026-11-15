The table below aligns the Hausdorff recurrence in $q$ with the Collatz-type step dynamics in $\Phi$, comparing the two systems row by row.

| | Hausdorff recurrence | Collatz dynamics |
|---|---|---|
| **Space** | $q \in \mathbb{R}_{>0}$ | $\Phi \in \mathbb{R}_{\geq 0}$ |
| **Map** | $F(q) = (q^2-q+1)/q$ | $\Phi \mapsto \Phi + \log_q([3]/[2]^v)$ |
| **Fixed point** | $q = 1$ | $\Phi = 0$ (i.e., $P = 1$) |
| **Step size** | $\hbar_q = (q-1)/q$ | $|\Delta\Phi| \approx 2.76$ |
| **Contraction ratio** | $F'(q) = 1 - 1/q^2$ | $R(v) = [3]_q / [2]_q^v$ |
| **At fixed point** | $F'(1) = 0$ — **superattracting** | $R(2) \approx 3/4$ — **uniform** |
| **Convergence** | Superlinear ($3$ steps from $q_0$) | Linear ($\Phi_0/2.76$ cycles) |
| **Entropy per step** | $\eta_q / |F'(q)| \to \infty$ at $q = 1$ | $3\eta_q \approx \text{const}$ |
