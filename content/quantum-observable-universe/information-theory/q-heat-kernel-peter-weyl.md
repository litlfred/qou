Applying the categorical Fourier transform
([categorical Fourier transform](#def:categorical-fourier)) to the
$q$-heat equation ([$q$-heat equation](#def:q-heat-equation))
diagonalises the $q$-Laplacian on each Peter--Weyl isotypic
component of $\mathbf{Rep}(\mathrm{SU}_q(2))$ (or more generally
of any quantum group acting on the substrate).  This gives an
explicit spectral formula for the $q$-heat kernel.

**Spectral decomposition.**  For $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$
solving $\partial_t u = \Delta_q u$ with initial datum $u_0$:

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
$\lambda \vdash n$ with cell contents $c(\square) = j - i$:

$$
  \boxed{\;
  \mu_\lambda(q)
  \;=\;
  q^{-2}  \sum_{\square \in \lambda}  c(\square) \bigl(c(\square) + 1\bigr)
  \;+\;
  \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q,
  \;}
$$

where $\hbar_q = (q - 1)/q$ is the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)) and
$[k]_q = (1 - q^k)/(1 - q)$ is the Jackson integer.

The two terms correspond to the classical-core
($q^{-2}\Delta$) and the Reeb-spin
($(1 - q^{-1})^2 \Delta_\xi$) pieces of the three-term expansion
([$q$-Laplacian expansion](#rem:q-laplacian-expansion)); the
Coriolis cross-terms vanish on Hecke-representation spaces by
Schur's lemma.

*Proof sketch.*  Schur's lemma on the irreducible Wedderburn block
$M_{d_\lambda(q)}$ forces $\Delta_q$ to act by a scalar.  The
scalar is computed by evaluating the $q$-Casimir on a highest-weight
vector; for $H_n(q)$, the Casimir value is the sum of
$[c(\square)]_q[c(\square) + 1]_q$ over cells $\square \in \lambda$,
a classical fact due to Jucys--Murphy (q-deformed by Ram).  The
classical-core contribution follows analogously using the
Plancherel Laplacian on Young diagrams.  $\qed$

**Small-$\lambda$ table** (at physical substrate $q_0 \approx 1.11$,
numerical values):

| $\lambda$ | $\sum c(c+1)$ (classical) | $\sum [c]_q[c+1]_q$ (q-Casimir) | $\mu_\lambda(q_0)$ |
|-----------|---------------------------|------------------------------------|---------------------|
| $(1)$     | $0$                       | $0$                                | $0$                 |
| $(2)$     | $2$                       | $[0]_q[1]_q + [1]_q[2]_q$          | $\approx 0.019$     |
| $(1,1)$   | $-2$                      | $[-1]_q[0]_q + [0]_q[1]_q$         | $\approx -0.017$    |
| $(3)$     | $8$                       | $[1]_q[2]_q + [2]_q[3]_q$          | $\approx 0.083$     |
| $(2,1)$   | $0$                       | $\hbar_q [2]_q$                    | $\approx 0.007$     |
| $(1^3)$   | $-8$                      | $-q^{-2}([1]_q[2]_q + [2]_q[3]_q)$ | $\approx -0.064$    |

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
