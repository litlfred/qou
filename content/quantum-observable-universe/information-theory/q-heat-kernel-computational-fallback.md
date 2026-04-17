At the physical substrate value $q_0 \approx 1.11$, exact enumeration
of $H_n(q)$ irreducibles $\lambda \vdash n$ for large $n$ is
infeasible: the partition count grows as $p(n) \sim \exp(\pi\sqrt{2n/3})/(4n\sqrt{3})$,
hitting $\sim 10^6$ at $n = 50$ and $\sim 10^{12}$ at $n = 100$.
Exact character-table computations (e.g.\ for nuclear binding energies,
cf.\ the `nf-transition-projection` branch) become intractable beyond
some *exactness threshold* $k_{\mathrm{exact}}$ — typically
$k_{\mathrm{exact}} \approx 9$--$15$ depending on machine and
representation.

**Fallback via the $q$-heat kernel.**  For $k > k_{\mathrm{exact}}$,
the Peter--Weyl decomposition
([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl))
gives a principled *approximation* that avoids enumerating all
partitions:

$$
  \mathrm{tr}\,M_\lambda(W_N)
  \;\approx\;
  d_\lambda(q_0) \cdot e^{-\mu_\lambda(q_0)  s_* N},
$$

where $s_* = \hbar_{q_0} = (q_0 - 1)/q_0 \approx 0.0988$ is the
canonical Reeb-time scale
([quantum Planck constant](#def:quantum-planck-constant)) and
$\mu_\lambda(q_0)$ is the content-Casimir eigenvalue (explicit from
partition data, cf.\ the content-Casimir formula).

**Equivalence to Perron--Frobenius.**  This is exactly the
Perron--Frobenius dominant-eigenvalue approximation used in the
`nf-transition` branch (commit `9c1e73c`):

$$
  \ln\bigl|\mathrm{Tr}\,M_\lambda(\text{step})\bigr|
  \;\approx\;
  \ln d_q(\lambda) + N(\text{step}) \cdot \ln|\mu_\lambda|,
$$

with the dominant $\mu_\lambda$ for the mean inter-nucleon crossing
being the $q$-Casimir eigenvalue of the symmetric rep $\lambda = (2)$:

$$
  \mu_{(2)}(q_0) \;=\; \hbar_{q_0}^2  [1]_{q_0}[2]_{q_0}
  \;\approx\; 0.021.
$$

More generally $\ln q_0 \approx 0.104$ used in the branch matches
$s_* = \hbar_{q_0} \approx 0.099$ to leading order in
$\hbar_q$ (Taylor: $\ln q = \hbar_q + \hbar_q^2/2 + O(\hbar_q^3)$).

**Gaussian approximation at very large $N$.**  For very large $N$,
the Peter--Weyl sum is dominated by a Gaussian profile in $\lambda$:
the Plancherel central-limit theorem applied to the random walk on
Young diagrams under the $q$-heat flow gives

$$
  \mathrm{tr}\,M_\lambda(W_N)
  \;\approx\;
  d_\lambda(q_0) \cdot G_{q_0}(N, \lambda_{\mathrm{centroid}}),
$$

where $G_q$ is the Reeb-invariant $q$-Gaussian
([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)).
Because $G_q$ is a *classical* Gaussian with rescaled variance
$\sigma^2 = t/q^2$ — not the Bożejko--Speicher distribution — it is
well-defined at $q_0 > 1$: one has $\sigma^2 \approx 0.81\,t$, a
slightly narrower than classical distribution.  No convergence
obstruction appears.

**Computational protocol.**  For a numerical workflow:

1. **Small $k$** ($k \le k_{\mathrm{exact}}$): enumerate all
   $\lambda \vdash k$ and compute
   $\mathrm{tr}\,M_\lambda$ exactly via Hecke character tables.
2. **Moderate $k$** ($k_{\mathrm{exact}} < k \le k_{\mathrm{PF}}$):
   use the Perron--Frobenius shortcut
   $\mathrm{tr}\,M_\lambda(W_N) \approx d_\lambda(q_0) e^{-\mu_\lambda(q_0) s_* N}$
   with the content-Casimir formula for $\mu_\lambda$.
3. **Large $k$** ($k > k_{\mathrm{PF}}$): use the Plancherel-Gaussian
   approximation with the Reeb-invariant $q$-Gaussian kernel, summing
   over dominant partitions inside a variance-$\sigma^2$ neighbourhood
   of $\lambda_{\mathrm{centroid}}$.

Each stage is a *consistent truncation* of the full Peter--Weyl sum:
stage 2 keeps only the dominant exponential mode, and stage 3 keeps
the leading Gaussian envelope.

**Cross-reference to the `nf-transition-projection` branch.**  The
branch's PF replacement ([commit `9c1e73c`](
https://github.com/litlfred/qou/commit/9c1e73c7413cb3303b9a64658d9a983bbe8d0d2a))
is *exactly* the stage-2 approximation above, instantiated for the
nuclear-binding computation with $q_0 \approx 1.11$.  The abandoned
Bożejko--Speicher q-Gaussian was a *different* object (noncommutative
moment distribution, requires $|q| \le 1$); the QOU $q$-heat-kernel
Gaussian is its replacement, valid at $q_0 > 1$ and categorically
grounded in the Peter--Weyl decomposition of the Reeb flow.
