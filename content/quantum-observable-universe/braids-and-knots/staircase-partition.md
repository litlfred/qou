**Definition.**
*For each $k \geq 1$, the **staircase partition** of $n_k =
\binom{k+1}{2} = k(k+1)/2$ is*

$$
  \rho_k \;:=\; (k,\, k-1,\, \ldots,\, 2,\, 1)
  \;\vdash\; \tfrac{k(k+1)}{2}.
$$

*Equivalently, $\rho_k$ is the Young diagram whose $r$-th row
($1 \leq r \leq k$) has $k - r + 1$ cells.  The first few are*

$$
  \rho_1 = (1), \quad
  \rho_2 = (2,1), \quad
  \rho_3 = (3,2,1), \quad
  \rho_4 = (4,3,2,1), \quad
  \rho_5 = (5,4,3,2,1).
$$

*The staircase partition is **self-conjugate**: $\rho_k = \rho_k'$
under transposition of rows and columns.*

The staircase shapes index Specht modules
$V_{\rho_k}$ of the Iwahori–Hecke algebra
$H_{n_k}(q)$ that play a distinguished role in the QOU
electroweak sector: the canonical
$\beta_{\mathrm{EW}} \, \bowtie_K^{\mathrm{minimal}}$
braid word acts on $V_{\rho_k}$ with a spectrum encoding the
$q$-deformed Weinberg-angle ratio (see
[`conj:staircase-ew-residual`](#conj:staircase-ew-residual)).

The Lean side is `QOU.Hecke.staircasePartition`, recursively
constructed via `staircaseList` and a dedicated
`staircaseList_sum` lemma that discharges the
`Partition.sum_eq` obligation; the staircase strand-count
$n_k$ is exposed as `QOU.Hecke.staircaseStrands`.
