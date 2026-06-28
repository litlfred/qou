**Small-$\lambda$ table** (at physical substrate $q_0 \approx 1.11$,
$\hbar_{q_0}^2 \approx 0.00976$):

See [Table](#tbl:q-heat-kernel-peter-weyl-table-data).

The content-Casimir sum is *explicit from partition data* — no
diagonalisation is required for the spectrum.

**Convergence and Mercer.**  For $t > 0$ the sum converges
absolutely: the positive eigenvalues $\mu_\lambda(q) > 0$
(which dominate the sum) satisfy
$\mu_\lambda(q) \asymp n^2/q^2$ for $\lambda \vdash n$ (plus
$\hbar_q^2 \cdot$ spin contribution), so
$e^{-\mu_\lambda(q)\, t} \to 0$ faster than any polynomial in $n$.
The dimension weights $d_\lambda(q)$ grow at most polynomially in
$n$, so the sum is Mercer-type and defines a continuous kernel
$K_q(t; x, y)$ on $\mathcal{S} \times \mathcal{S}$ for every $t > 0$.

**Relation to the Reeb-invariant $q$-Gaussian.**  The trivial
partition $\lambda = (1)$ has $\mu_{(1)}(q) = 0$, so its
Peter--Weyl component is *constant* in $t$: it is the asymptotic
$t \to \infty$ limit, the equilibrium distribution.  The next
components ($\lambda = (2)$ and $(1,1)$) contribute the leading
Reeb-invariant heat-flow, recovering the $q$-Gaussian
([Reeb-invariant $q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)).
Higher-order $\lambda$ produce Reeb-fibre modulations absent from
the base-Gaussian.

**Role in the $q$-heat story.**  This is the *Fourier-side* of the
heat flow: every solution decomposes into exponentially decaying
$H_n(q)$-isotypic modes, each with a closed-form rate
$\mu_\lambda(q)$.  The Laplace transform
([categorical Laplace transform](#def:categorical-laplace))
$\mathcal{L}[u](s) = \sum_\lambda d_\lambda(q) (\mu_\lambda(q) + s)^{-1} \pi_\lambda(u_0)$
is the resolvent of $\Delta_q$, with simple poles at
$s = -\mu_\lambda(q)$.  The $q$-dilogarithm
([$q$-dilogarithm](#def:q-dilogarithm)) is the generating function
for $\sum_\lambda \log \mu_\lambda(q)$ — the partition function of
the Reeb-heat flow — closing the loop between the categorical and
archimedean sides.
