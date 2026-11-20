**Small-$\lambda$ table** (at physical substrate $q_0 \approx 1.11$, symmetric quantum integers, values computed at the corpus anchor $q_0 = 1.1099786\ldots$):

See [Table](#tbl:q-heat-kernel-peter-weyl-table-data).

The content-Casimir sum follows explicitly from partition data. No diagonalisation is required to determine the spectrum.

**Convergence and Mercer.** For $t > 0$, the sum converges absolutely. Every eigenvalue satisfies $\mu_\lambda(q) \ge \sum_{\square} c(\square)(c(\square)+1) \ge 0$ for real $q > 0$, because each cell contributes $[j]_q[j+1]_q$ with $j \ge 0$ and $[m]_q \ge m$ there. That the eigenvalues grow fast enough in $n$ for $e^{-\mu_\lambda(q)\, t}$ to beat the dimension weights is the convergence conjecture `qHeatKernelPeterWeyl`; it is not proved. The dimension weights $d_\lambda(q)$ grow at most polynomially. The sum is Mercer-type, defining a continuous kernel $K_q(t; x, y)$ on $\mathcal{S} \times \mathcal{S}$ for every $t > 0$.

**Relation to the Reeb-invariant $q$-Gaussian.** The trivial partition $\lambda = (1)$ carries $\mu_{(1)}(q) = 0$. Its Peter--Weyl component remains constant in $t$, representing the equilibrium distribution as $t \to \infty$. The partitions $\lambda = (2)$ and $(1,1)$ contribute the leading Reeb-invariant heat flow, recovering the $q$-Gaussian. Higher-order partitions produce Reeb-fibre modulations wholly absent from the base-Gaussian.

**Role in the $q$-heat story.** This constitutes the Fourier-side of the heat flow. Every solution decomposes into exponentially decaying $H_n(q)$-isotypic modes with closed-form decay rates $\mu_\lambda(q)$. The Laplace transform $\mathcal{L}[u](s) = \sum_\lambda d_\lambda(q) (\mu_\lambda(q) + s)^{-1} \pi_\lambda(u_0)$ acts as the resolvent of $\Delta_q$, with simple poles precisely at $s = -\mu_\lambda(q)$. The $q$-dilogarithm generates $\sum_\lambda \log \mu_\lambda(q)$. This serves as the partition function of the Reeb-heat flow.
