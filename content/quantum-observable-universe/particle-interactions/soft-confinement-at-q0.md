The Wedderburn block labels of $H_n(q)$ — partitions $\lambda \vdash n$ —
are combinatorial and $q$-independent.  What **is** $q$-dependent is
the **measure** on this grading: the Plancherel weights
$w_\lambda(q) = d_q(\lambda)^2 / [n]_q!$ depend sensitively on $q$.

At **roots of unity** $q = e^{2 \pi i / \ell}$ the quantum dimensions
$d_q(\lambda)$ can vanish or turn negative, and representations with
more than $\ell - 1$ rows become **confined** (zero-weight).  This is
the Jones-Wenzl truncation underlying fusion-category / TQFT
constructions: a sharp cutoff at level $\ell$.

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps) (generic real, **not**
a root of unity), no representation is strictly confined.  But the
Plancherel weights **decay rapidly** with partition size, producing a
**soft confinement level**

$$
  \ell_*(q_0)
  \;\sim\;
  \frac{1}{\log q_0}
  \;\approx\;
  \frac{1}{\log 1.10998}
  \;\approx\;
  9.6.
$$

Partitions of depth or width exceeding $\ell_*$ contribute negligibly
to the Frobenius packing and can be truncated in practice.

## Consequences of the soft cutoff

### Implication for atomic braids

An atomic braid with $A$ nucleons has $3A$ strands and lives in
$H_{3A}(q_0)$, whose Wedderburn sum ranges over partitions
$\lambda \vdash 3A$.  Soft confinement means:

- For **light atoms** ($A \leq 3$, so $3A \leq 9 \lesssim \ell_*$),
  the full Plancherel sum is active; no truncation.
- For **medium atoms** ($A \sim 4$ to $6$, $3A \sim 12$ to $18$),
  partitions with more than $\sim 10$ rows or columns have
  exponentially small weight and can be dropped.
- For **heavy atoms** ($A \gtrsim 10$), the sum effectively truncates
  at shape $\approx \ell_*$ — the natural ceiling of the
  Plancherel-concentrated regime (Vershik-Kerov / Logan-Shepp limit
  shape, $\lambda_1 \sim 2\sqrt{n}$).

The transition from $H_3$-per-nucleon to full $H_{3A}$ sum is what
makes the [$\alpha$-cluster unfolding](#prop:tower-binding-energy)
numerically necessary beyond $A \sim 4$: the block structure of
$H_{3A}$ for larger $A$ starts to exceed $\ell_*$, and cross-Wedderburn
couplings — which collapse under truncation — must be re-summed
via cluster decomposition.

### Numerical estimate

At $q_0 = 1.109978595554181\ldots$ (50 dps):

See [Table](#tbl:soft-confinement-at-q0-table-data).

The rapid saturation of cumulative weight by the first few partitions
is the quantitative form of soft confinement.  The
[soft-confinement cutoff $\ell_*(q_0) \approx 10$](#prop:local-substrate-q)
is the horizon at which the substrate's grading effectively
terminates.
