**1. Soft confinement at the substrate parameter.**
The Wedderburn block labels of $H_n(q)$ (partitions $\lambda \vdash n$) are combinatorial and $q$-independent. The measure on this grading (the Plancherel weights $w_\lambda(q) = d_q(\lambda)^2 / [n]_q!$) depends sensitively on $q$.

At roots of unity $q = e^{2 \pi i / \ell}$, quantum dimensions $d_q(\lambda)$ vanish or turn negative. Representations with more than $\ell - 1$ rows become strictly confined (zero-weight). This is the Jones-Wenzl truncation underlying fusion-category constructions: a sharp cutoff at level $\ell$.

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (generic real, not a root of unity), no representation is strictly confined. But Plancherel weights decay rapidly with partition size, producing a soft confinement level:
$$
  \ell_*(q_0)
  \;\sim\;
  \frac{1}{\log q_0}
  \;\approx\;
  \frac{1}{\log 1.10998}
  \;\approx\;
  9.6.
$$
Partitions of depth or width exceeding $\ell_*$ contribute negligibly to the Frobenius packing and can be truncated.

**2. Implication for atomic braids.**
An atomic braid with $A$ nucleons has $3A$ strands and lives in $H_{3A}(q_0)$, whose Wedderburn sum ranges over partitions $\lambda \vdash 3A$. Soft confinement implies:

- **Light atoms** ($A \leq 3$, $3A \leq 9 \lesssim \ell_*$): The full Plancherel sum is active. No truncation occurs.
- **Medium atoms** ($A \sim 4$ to $6$, $3A \sim 12$ to $18$): Partitions with more than $\sim 10$ rows or columns have exponentially small weight and drop out.
- **Heavy atoms** ($A \gtrsim 10$): The sum effectively truncates at shape $\approx \ell_*$, the natural ceiling of the Plancherel-concentrated regime (the Vershik-Kerov limit shape, $\lambda_1 \sim 2\sqrt{n}$).

The transition from $H_3$-per-nucleon to the full $H_{3A}$ sum dictates why [$\alpha$-cluster unfolding](#prop:tower-binding-energy) is numerically necessary beyond $A \sim 4$. The block structure of $H_{3A}$ for larger $A$ exceeds $\ell_*$, and cross-Wedderburn couplings that collapse under truncation must be re-summed via cluster decomposition.

**3. Numerical estimate.**
At $q_0 = 1.109978595554181\ldots$:
See [Table](#tbl:soft-confinement-at-q0-table-data).

The rapid saturation of cumulative weight by the first few partitions quantitatively demonstrates soft confinement. The [cutoff $\ell_*(q_0) \approx 10$](#prop:local-substrate-q) represents the horizon where the substrate's grading effectively terminates.
