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

Verified at 50 dps for $n \in \{2, 3, 4, 5\}$, $N \in \{3, 4, 5, 6, 7\}$
(20 combinations), max residual $8.0 \times 10^{-51}$. Witness:
[`jonquiere-cyclotomic-general.witness.json`](https://github.com/litlfred/qou/blob/main/computations/jonquiere-cyclotomic-general.witness.json).

Sample values:

See [Table 1](#tbl:cyclotomic-orbit-sum-all-depths-table1-data).

### Significance

**For $n$ odd**: orbit sum reduces to $\zeta(n)$ — one dim of
genuinely-new content "absorbed" into the classical $\zeta(n)$-line
of $\mathcal{P}_n / \mathcal{P}_{n-1}$ (when $n$ is odd, $\zeta(n)$ is
NOT Tate-rational, conjecturally transcendental over $\mathbb{Q}$).

**For $n$ even**: orbit sum vanishes by definition. The individual
$\mathrm{Cl}_n$ values are bar-anti-symmetric (Glaisher convention),
They pair-cancel. No reduction occurs — all $(N - 1)/2$ distinct
$\mathrm{Cl}_n$ magnitudes are independent (modulo Beilinson).

### Generalises Theorem B

Theorem B ([`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general))
is the $n = 3$ case. This proposition extends the pattern to all $n$
with a single proof.

### Dimension consequences

Combined with
[`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality):

See [Table 2](#tbl:cyclotomic-orbit-sum-all-depths-table2-data).

The depth-3 case (round 3 + round 4 of ) gave $(K - 3)/2$.
The general formula here is parity-dependent: $(K - 3)/2$ for $n$
odd, $(K - 1)/2$ for $n$ even.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- Tate-rationality companion: [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Dimension synthesis: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
