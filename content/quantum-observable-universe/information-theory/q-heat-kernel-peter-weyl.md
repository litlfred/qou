Applying the categorical Fourier transform
([categorical Fourier transform](#def:categorical-fourier)) to the
$q$-heat equation ([$q$-heat equation](#def:q-heat-equation))
diagonalises the $q$-Laplacian on each Peter--Weyl isotypic
component of $\mathbf{Rep}(\mathrm{SU}_q(2))$ (or more generally
of any quantum group acting on the substrate).  This gives an
explicit spectral formula for the $q$-heat kernel.

**Spectral decomposition.**  For $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$
solving $\partial_t u = -\Delta_q u$ with initial datum $u_0$:

$$
  u(t, x) \;=\; \sum_{\lambda \in \widehat{H_n(q)}}
    d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t}  \cdot \pi_\lambda(u_0)(x),
$$

where the sum ranges over irreducible Wedderburn blocks of the
Hecke algebra $H_n(q)$ — equivalently partitions $\lambda \vdash n$
of the number of strands $n$ —
$d_\lambda(q)$ is the Steinberg $q$-hook dimension,
$\pi_\lambda$ is the projection onto the $V_\lambda$-isotypic
component, and $\mu_\lambda(q)$ is the $q$-Laplacian eigenvalue.

**Explicit content-Casimir formula.**  For a partition
$\lambda \vdash n$ with cell contents $c(\square) = j - i$, the
**Reeb-spin eigenvalue** of $\Delta_\xi$ on $V_\lambda$ is:

$$
  \boxed{\;
  \mu_\lambda(q)
  \;=\;
  \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q,
  \;}
$$

where $\hbar_q = (q - 1)/q$ is the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)) and
$[k]_q = (1 - q^k)/(1 - q)$ is the Jackson integer.  This is the
eigenvalue of the pure-spin piece $(1 - q^{-1})^2 \Delta_\xi$ from
the three-term expansion
([$q$-Laplacian expansion](#rem:q-laplacian-expansion)).  The
classical-core piece $q^{-2}\Delta$ acts on spatial modes of the
base manifold $M$ and contributes a *separate* eigenvalue
$q^{-2}|\mathbf{k}|^2$ depending on the spatial wavenumber
$\mathbf{k}$, not on the partition $\lambda$.  Coriolis cross-terms
vanish on Hecke-representation spaces by Schur's lemma.

)]_q[c(\square) + 1]_q$ over cells $\square \in \lambda$,
a classical fact due to Jucys--Murphy ($q$-deformed by Ram).
Multiplying by $\hbar_q^2 = (1 - q^{-1})^2$ gives $\mu_\lambda(q)$.
$\qed$

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
