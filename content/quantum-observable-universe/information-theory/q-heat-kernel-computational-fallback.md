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
