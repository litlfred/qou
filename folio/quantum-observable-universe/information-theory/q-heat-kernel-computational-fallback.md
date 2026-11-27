At the physical aether value $q_0 \approx 1.11$, exact enumeration of $H_n(q)$ irreducibles $\lambda \vdash n$ becomes infeasible for large $n$. The partition count grows as $p(n) \sim \exp(\pi\sqrt{2n/3})/(4n\sqrt{3})$, hitting $\sim 10^6$ at $n = 50$. Exact character-table computations fail beyond an exactness threshold $k_{\mathrm{exact}} \approx 9$--$15$.

**Fallback via the $q$-heat kernel.** For $k > k_{\mathrm{exact}}$, the Peter--Weyl decomposition supplies a principled approximation:
$$
  \mathrm{tr}\,M_\lambda(W_N) \approx d_\lambda(q_0) \cdot e^{-\mu_\lambda(q_0)  s_* N}.
$$
Here $s_* = \hbar_{q_0} = (q_0 - 1)/q_0 \approx 0.0988$ is the canonical Reeb-time scale, and $\mu_\lambda(q_0)$ is the content-Casimir eigenvalue.

**Equivalence to Perron--Frobenius.** This strictly corresponds to the Perron--Frobenius dominant-eigenvalue approximation:
$$
  \ln\bigl|\mathrm{Tr}\,M_\lambda(\text{step})\bigr| \approx \ln d_q(\lambda) + N(\text{step}) \cdot \ln|\mu_\lambda|.
$$
The dominant $\mu_\lambda$ for the mean inter-nucleon crossing is the $q$-Casimir eigenvalue of the symmetric representation $\lambda = (2)$:
$$
  \mu_{(2)}(q_0) = \hbar_{q_0}^2  [1]_{q_0}[2]_{q_0} \approx 0.021.
$$
The approximation $\ln q_0 \approx 0.104$ agrees with $s_* = \hbar_{q_0} \approx 0.099$ to leading order in $\hbar_q$.

**Gaussian approximation at very large $N$.** At extremely large $N$, a Gaussian profile dominates the Peter--Weyl sum. The Plancherel central-limit theorem for the random walk on Young diagrams yields:
$$
  \mathrm{tr}\,M_\lambda(W_N) \approx d_\lambda(q_0) \cdot G_{q_0}(N, \lambda_{\mathrm{centroid}}).
$$
The kernel $G_q$ is the Reeb-invariant $q$-Gaussian. Because $G_q$ is a classical Gaussian with rescaled variance $\sigma^2 = t/q^2$, it remains well-defined at $q_0 > 1$. The distribution simply narrows by a factor of $0.81$ relative to the classical case. No convergence obstruction manifests.

**Computational protocol.** The numerical workflow proceeds in three stages:

1. **Small $k \le k_{\mathrm{exact}}$:** Enumerate all $\lambda \vdash k$ and compute $\mathrm{tr}\,M_\lambda$ exactly via Hecke character tables.
2. **Moderate $k_{\mathrm{exact}} < k \le k_{\mathrm{PF}}$:** Deploy the Perron--Frobenius shortcut utilizing the content-Casimir formula for $\mu_\lambda$.
3. **Large $k > k_{\mathrm{PF}}$:** Invoke the Plancherel-Gaussian approximation. Sum over dominant partitions inside a variance-$\sigma^2$ neighbourhood of $\lambda_{\mathrm{centroid}}$.

Each stage truncates the Peter--Weyl sum systematically. Stage 2 isolates the dominant exponential mode. Stage 3 isolates the leading Gaussian envelope.

**Relation to previous methods.** The Perron--Frobenius truncation exactly duplicates the stage-2 approximation. The previously discarded Bożejko--Speicher $q$-Gaussian restricted to $|q| \le 1$. The QOU $q$-heat-kernel Gaussian subsumes it, remaining valid at $q_0 > 1$ while reflecting the Peter--Weyl decomposition of the Reeb flow.
