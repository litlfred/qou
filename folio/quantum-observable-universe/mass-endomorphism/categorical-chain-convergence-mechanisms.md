**Categorical-chain convergence: per-knot finite truncation + inter-knot linking-number locality.**

The categorical-derivation precision ladder $\mathfrak{Q}_\beta^{\text{cat}}$ from [$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder) is formally an **infinite product** in the Habiro ring (cyclotomic-Pochhammer completion of $\mathbb{Z}[q]$). For any **single isolated knot**, this product reduces to a **finite truncation** at sub-CODATA precision through two convergence mechanisms.

## Mechanism 1: Per-knot c(K) brane-tower bound

Per `conj:archimedean-remainder-exponential-decay`, the truncation residual at depth $N$ satisfies:

$$
  \lvert R_N \rvert \;\le\; \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2},
$$

where $\hbar_q = (q-1)/q$. At the substrate $q_0 \approx 1.110$, $\hbar_q^2 \approx 9.8 \times 10^{-3}$, meaning each new rung tightens the prediction by approximately $100\times$ (see [Table](#tbl:categorical-chain-convergence-mechanisms-table-data)).

The truncation depth this gives for free-neutron $\beta$-decay is recorded in [this remark](#rem:categorical-chain-convergence-mechanisms-neutron-truncation).

## Mechanism 2: Inter-knot linking-number locality

For the **full base-space sum** over all atomic knots, unlinked knot pairs contribute negligibly. If $K_1, K_2$ have linking number $\mathrm{lk}(K_1, K_2) = 0$, their joint Markov trace factorises:

$$
  \mathrm{tr}_M(K_1 \sqcup K_2) \;=\; \mathrm{tr}_M(K_1) \cdot \mathrm{tr}_M(K_2) \quad (\text{linking-trivial limit}).
$$

Their categorical-chain contributions are additive in $\log \mathfrak{Q}_\beta^{\text{cat}}$:

$$
  \log \mathfrak{Q}_\beta^{\text{cat,full}}(K_1 \sqcup K_2)
   \;=\;
   \log \mathfrak{Q}_\beta^{\text{cat}}(K_1)
   \;+\;
   \log \mathfrak{Q}_\beta^{\text{cat}}(K_2)
   \;+\;
   O(\mathrm{lk}_{12}).
$$

Cross-coupling correction terms vanish at leading order and only enter when $\mathrm{lk}(K_i, K_j) \neq 0$.

## Combined picture

For a dense substrate with numerous atomic-knot configurations, the full prediction factorises:

$$
\boxed{
  \mathfrak{Q}_\beta^{\text{cat,full}}
   \;=\;
   \prod_{\text{linked clusters } C}
     \biggl[\prod_{K \in C} \mathfrak{Q}_\beta^{\text{cat}}(K)\biggr]
   \;\cdot\;
   \prod_{\substack{(K_i, K_j) \\ \mathrm{lk} \neq 0}}
     (\text{cross-coupling factor}_{ij}).
}
$$

The inner product (per linked cluster) is finite via Mechanism 1, while the outer product is finite because most pairs remain unlinked.

## Mechanism in the QOU framework

This constitutes the categorical analog of asymptotic freedom:
- At high substrate density (small $\hbar_q$), the per-knot tower truncates sharply.
- At wide spatial dilution (most $K_i, K_j$ pairs unlinked), the inter-knot coupling vanishes.

Both limits converge a formally-infinite Habiro-ring element to a finite-precision real-valued prediction.

## Pre-archimedean home

In the Habiro ring $\widehat{\mathbb{Z}[q]}_{\text{Hab}}$:
- Each $F_k = 1 + c_k \cdot b^k \cdot \hbar_q^{2k}$ constructs a Pochhammer-graded element at depth $k$.
- The infinite product $\prod_k F_k$ exists formally within the inverse limit $\varprojlim \mathbb{Z}[q]/((q;q)_n)$.
- Per-knot evaluation projects to a Habiro residue at the substrate $q_0$, rendered finite by linking-number locality.
- The archimedean realisation provides the numerical $\mathfrak{Q}_\beta^{\text{cat}}$.
