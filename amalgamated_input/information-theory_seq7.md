<!-- FILE_START: q-heat-kernel-analysis-intro.md -->
The substrate supplies a Jackson derivative $D_q$ and a categorical Fourier transform. We now construct the corresponding heat kernel and read off its spectral decomposition. This section verifies that standard heat-kernel analysis survives the $q$-deformation when $q = q_0$ is non-torsion. It also provides a computational fallback when the Peter--Weyl sum diverges at large rank. 

We proceed in three steps. First, the proposition on the Taylor series of $\exp_q$ realises the abstract grouplike $\exp_q$ as a convergent power series. Second, the $q$-Gaussian proposition verifies that the $q$-Gaussian solves the fundamental $q$-heat equation $\partial_t u = D_q^2 u$. Third, the Peter--Weyl decomposition expands this solution in Hecke--Wedderburn characters. The closing remark supplies a Perron--Frobenius truncation for large-rank evaluation. The subsequent section on Statistical Mechanics uses this $q$-heat kernel as the partition function $Z_q$ to extract quantum temperature, pressure, and volume.
<!-- FILE_END: q-heat-kernel-analysis-intro.md -->

<!-- FILE_START: q-exponential-taylor.md -->
Let $R$ be a commutative ring of characteristic zero (e.g., $\mathbb{Q}, \mathbb{R}, \mathbb{C}$) in which all Jackson factorials $[n]_q! = \prod_{k=1}^{n} \frac{1 - q^k}{1 - q}$ are invertible. Over $R$, the convergent power series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}
$$

represents the abstract grouplike $\exp_q \in G(\mathcal{H}_q)$ ([$q$-exponential](#def:q-exponential)).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, including real-valued physical observables, real-analytic bounds, transcendental constants, and numerical evaluation at the substrate parameter $q_0$. The generic categorical and $q$-deformation identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realisation is specialised here.
<!-- FILE_END: q-exponential-taylor.md -->

<!-- FILE_START: q-gaussian-solves-q-heat.md -->
**Proposition.**
*Over $\mathbb{R}^n$ with the archimedean realisation of the $q$-Laplacian ([three-term expansion](#rem:q-laplacian-expansion)), the Reeb-invariant $q$-Gaussian*

$$
  G_q(t, x) \;=\; \bigl(4\pi q^{-2} t\bigr)^{-n/2}
  \exp\!\left(-\frac{q^2  |x|^2}{4t}\right)
$$

*is a fundamental solution of the $q$-heat equation ([$q$-heat equation](#def:q-heat-equation)):*

$$
  \partial_t G_q \;=\; -\Delta_q G_q,
  \qquad
  \lim_{t \downarrow 0} G_q(t, \cdot) \;=\; \delta_0.
$$
<!-- FILE_END: q-gaussian-solves-q-heat.md -->

<!-- FILE_START: q-gaussian-solves-q-heat-interpretation.md -->
Since $-\Delta_q = q^{-2}\nabla^2$ on Reeb-invariant forms, writing $\tau = q^{-2} t$ yields

$$
  G_q(t, x) \;=\; \bigl(4\pi \tau\bigr)^{-n/2}
  \exp\!\bigl(-|x|^2 / (4 \tau)\bigr).
$$

This is the classical Gaussian heat kernel in rescaled time. Reeb-invariant diffusion on a QOU with substrate parameter $q$ is isomorphic to ordinary diffusion with the clock running at rate $q^{-2}$. 

At the Big Bang ($q \to \infty$), the clock freezes. Heat cannot spread on the base because the Reeb-fibre direction absorbs the entire diffusive budget. At heat death ($q \to 1$), the clock runs at unit rate and $G_q$ recovers the classical Gaussian.
<!-- FILE_END: q-gaussian-solves-q-heat-interpretation.md -->

<!-- FILE_START: q-heat-kernel-peter-weyl.md -->
**Proposition ($q$-heat kernel spectral decomposition).**
*Applying the categorical Fourier transform ([categorical Fourier transform](#def:categorical-fourier)) to the $q$-heat equation ([$q$-heat equation](#def:q-heat-equation)) diagonalises the $q$-Laplacian on each Peter--Weyl isotypic component of $\mathbf{Rep}(\mathrm{SU}_q(2))$. This yields an explicit spectral formula for the $q$-heat kernel.*

**Spectral decomposition.** We consider a solution $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$ to $\partial_t u = -\Delta_q u$ with initial datum $u_0$. The solution decomposes as

$$
  u(t, x) \;=\; \sum_{\lambda \in \widehat{H_n(q)}}
    d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t}  \cdot \pi_\lambda(u_0)(x).
$$

The sum ranges over irreducible Wedderburn blocks of the Hecke algebra $H_n(q)$, equivalent to partitions $\lambda \vdash n$. The dimension $d_\lambda(q)$ is the Steinberg $q$-hook dimension, $\pi_\lambda$ projects onto the $V_\lambda$-isotypic component, and $\mu_\lambda(q)$ is the $q$-Laplacian eigenvalue.

**Explicit content-Casimir formula.** Given a partition $\lambda \vdash n$ with cell contents $c(\square) = j - i$, the Reeb-spin eigenvalue of $\Delta_\xi$ on $V_\lambda$ is

$$
  \boxed{\;
  \mu_\lambda(q)
  \;=\;
  \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q.
  \;}
$$

The factor $\hbar_q = (q - 1)/q$ is the quantum Planck constant ([quantum Planck constant](#def:quantum-planck-constant)) and $[k]_q = (1 - q^k)/(1 - q)$ is the Jackson integer. This formula computes the eigenvalue of the pure-spin piece $(1 - q^{-1})^2 \Delta_\xi$ from the three-term expansion ([$q$-Laplacian expansion](#rem:q-laplacian-expansion)). The classical-core piece $q^{-2}\Delta$ acts on spatial modes of the base manifold $M$ and contributes a separate eigenvalue $q^{-2}|\mathbf{k}|^2$ dependent on the spatial wavenumber $\mathbf{k}$. Coriolis cross-terms vanish on Hecke-representation spaces by Schur's lemma.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, bounds, transcendental constants, or numerical evaluation at $q_0$). Any categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-heat-kernel-peter-weyl.md -->

<!-- FILE_START: q-heat-kernel-peter-weyl-interpretation.md -->
**Small-$\lambda$ table** (at physical substrate $q_0 \approx 1.11$, $\hbar_{q_0}^2 \approx 0.00976$):

See [Table](#tbl:q-heat-kernel-peter-weyl-table-data).

The content-Casimir sum is explicit from partition data. No diagonalisation is required for the spectrum.

**Convergence and Mercer.** For $t > 0$, the sum converges absolutely. The positive eigenvalues $\mu_\lambda(q) > 0$ satisfy $\mu_\lambda(q) \asymp n^2/q^2$ for $\lambda \vdash n$. Thus $e^{-\mu_\lambda(q)\, t} \to 0$ faster than any polynomial in $n$. The dimension weights $d_\lambda(q)$ grow at most polynomially in $n$. The sum is Mercer-type and defines a continuous kernel $K_q(t; x, y)$ on $\mathcal{S} \times \mathcal{S}$ for every $t > 0$.

**Relation to the Reeb-invariant $q$-Gaussian.** The trivial partition $\lambda = (1)$ has $\mu_{(1)}(q) = 0$. Its Peter--Weyl component remains constant in $t$ and represents the equilibrium distribution as $t \to \infty$. The subsequent components $\lambda = (2)$ and $(1,1)$ contribute the leading Reeb-invariant heat flow, recovering the $q$-Gaussian ([Reeb-invariant $q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)). Higher-order partitions produce Reeb-fibre modulations absent from the base-Gaussian.

**Role in the $q$-heat story.** This is the Fourier-side of the heat flow. Every solution decomposes into exponentially decaying $H_n(q)$-isotypic modes with a closed-form rate $\mu_\lambda(q)$. The Laplace transform ([categorical Laplace transform](#def:categorical-laplace)) $\mathcal{L}[u](s) = \sum_\lambda d_\lambda(q) (\mu_\lambda(q) + s)^{-1} \pi_\lambda(u_0)$ is the resolvent of $\Delta_q$, with simple poles at $s = -\mu_\lambda(q)$. The $q$-dilogarithm ([$q$-dilogarithm](#def:q-dilogarithm)) generates $\sum_\lambda \log \mu_\lambda(q)$. This serves as the partition function of the Reeb-heat flow, closing the loop between the categorical and archimedean sides.
<!-- FILE_END: q-heat-kernel-peter-weyl-interpretation.md -->

<!-- FILE_START: q-heat-kernel-computational-fallback.md -->
At the physical substrate value $q_0 \approx 1.11$, exact enumeration of $H_n(q)$ irreducibles $\lambda \vdash n$ for large $n$ is infeasible. The partition count grows as $p(n) \sim \exp(\pi\sqrt{2n/3})/(4n\sqrt{3})$, hitting $\sim 10^6$ at $n = 50$. Exact character-table computations become intractable beyond an exactness threshold $k_{\mathrm{exact}} \approx 9$--$15$.

**Fallback via the $q$-heat kernel.** For $k > k_{\mathrm{exact}}$, the Peter--Weyl decomposition ([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl)) supplies a principled approximation:

$$
  \mathrm{tr}\,M_\lambda(W_N)
  \;\approx\;
  d_\lambda(q_0) \cdot e^{-\mu_\lambda(q_0)  s_* N}.
$$

Here $s_* = \hbar_{q_0} = (q_0 - 1)/q_0 \approx 0.0988$ is the canonical Reeb-time scale ([quantum Planck constant](#def:quantum-planck-constant)), and $\mu_\lambda(q_0)$ is the content-Casimir eigenvalue.

**Equivalence to Perron--Frobenius.** This is the Perron--Frobenius dominant-eigenvalue approximation:

$$
  \ln\bigl|\mathrm{Tr}\,M_\lambda(\text{step})\bigr|
  \;\approx\;
  \ln d_q(\lambda) + N(\text{step}) \cdot \ln|\mu_\lambda|.
$$

The dominant $\mu_\lambda$ for the mean inter-nucleon crossing is the $q$-Casimir eigenvalue of the symmetric representation $\lambda = (2)$:

$$
  \mu_{(2)}(q_0) \;=\; \hbar_{q_0}^2  [1]_{q_0}[2]_{q_0}
  \;\approx\; 0.021.
$$

The approximation $\ln q_0 \approx 0.104$ matches $s_* = \hbar_{q_0} \approx 0.099$ to leading order in $\hbar_q$.

**Gaussian approximation at very large $N$.** For very large $N$, a Gaussian profile dominates the Peter--Weyl sum. Applying the Plancherel central-limit theorem to the random walk on Young diagrams yields:

$$
  \mathrm{tr}\,M_\lambda(W_N)
  \;\approx\;
  d_\lambda(q_0) \cdot G_{q_0}(N, \lambda_{\mathrm{centroid}}).
$$

The kernel $G_q$ is the Reeb-invariant $q$-Gaussian ([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)). Because $G_q$ is a classical Gaussian with rescaled variance $\sigma^2 = t/q^2$, it is well-defined at $q_0 > 1$. The distribution narrows by a factor of $0.81$ relative to the classical case. No convergence obstruction appears.

**Computational protocol.** A complete numerical workflow proceeds in three stages:

1. **Small $k \le k_{\mathrm{exact}}$:** Enumerate all $\lambda \vdash k$ and compute $\mathrm{tr}\,M_\lambda$ exactly via Hecke character tables.
2. **Moderate $k_{\mathrm{exact}} < k \le k_{\mathrm{PF}}$:** Use the Perron--Frobenius shortcut with the content-Casimir formula for $\mu_\lambda$.
3. **Large $k > k_{\mathrm{PF}}$:** Use the Plancherel-Gaussian approximation. Sum over dominant partitions inside a variance-$\sigma^2$ neighbourhood of $\lambda_{\mathrm{centroid}}$.

Each stage truncates the Peter--Weyl sum consistently. Stage 2 retains the dominant exponential mode. Stage 3 retains the leading Gaussian envelope.

**Relation to previous methods.** The Perron--Frobenius truncation exactly mirrors the stage-2 approximation. The previously abandoned Bożejko--Speicher $q$-Gaussian required $|q| \le 1$. The QOU $q$-heat-kernel Gaussian replaces it, remaining valid at $q_0 > 1$ while reflecting the Peter--Weyl decomposition of the Reeb flow.
<!-- FILE_END: q-heat-kernel-computational-fallback.md -->

