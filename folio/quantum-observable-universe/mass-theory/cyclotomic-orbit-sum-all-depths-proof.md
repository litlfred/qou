### Proof

**Step 1 (multiplication formula).** The classical $N$-th
roots-of-unity multiplication identity:

$$
  \sum_{k = 1}^{N - 1} \mathrm{Li}_n(\zeta_N^k)
  \;=\;
  \bigl(N^{1 - n} - 1\bigr)\, \zeta(n).
$$

The RHS is real ($\zeta(n) \in \mathbb{R}$).

**Step 2 (extract Re / Im).**

- *$n$ odd:* $\mathrm{Cl}_n = \mathrm{Re}\,\mathrm{Li}_n$. Taking real
 part of both sides:
 $\sum_k \mathrm{Cl}_n(2\pi k/N) = (N^{1 - n} - 1)\, \zeta(n)$.
- *$n$ even:* $\mathrm{Cl}_n = \mathrm{Im}\,\mathrm{Li}_n$. Taking
 imaginary part of both sides:
 $\sum_k \mathrm{Cl}_n(2\pi k/N) = \mathrm{Im}((N^{1 - n} - 1)\,\zeta(n)) = 0$
 (since $\zeta(n) \in \mathbb{R}$). $\square$

### Verifications

Verified at 50 decimal places across all 20 pairs $n \in \{2, 3, 4, 5\}$, $N \in \{3, 4, 5, 6, 7\}$ with maximum residual $8.0 \times 10^{-51}$.

Sample values:

See [Table 1](#tbl:cyclotomic-orbit-sum-all-depths-table1-data).
