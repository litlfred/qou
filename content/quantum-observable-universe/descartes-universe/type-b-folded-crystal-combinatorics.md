**Proposition (Type-B folded crystal cancellation, sorry-free).**
*For every partition $\lambda$ realised as a list of cells with
contents $c(r, \mathrm{col}) := \mathrm{col} - r$, the cell-level
content cancellation*

$$
  c(r, \mathrm{col}) + c(\mathrm{col}, r) \;=\; 0
$$

*lifts to the partition-level identity*

$$
  \sum_{x \in \lambda} c(x) \;+\; \sum_{x \in \lambda^T} c(x) \;=\; 0,
$$

*where $\lambda^T$ is the transpose partition (every cell
$(r, \mathrm{col})$ replaced by $(\mathrm{col}, r)$). Self-dual
partitions $\lambda = \lambda^T$ have content sum zero.*

> **Status: theorem (unconditional).** This is the combinatorial
> primitive underlying the Type-B folding shortcut from
> CLAUDE.md §7b: *"Fold the $\mathfrak{sl}_n$ Cartan datum into a
> Type B datum; the resulting Kashiwara graph is a symmetric
> crystal, and its GS normal forms are bar-involution
> ($q \mapsto q^{-1}$) invariant by construction."* The proof is
> direct integer arithmetic and is sorry-free in the Lean file
> [`type-b-folded-crystal-combinatorics.lean`](type-b-folded-crystal-combinatorics.lean).

## Lean structure

| Definition / theorem | Content |
|---|---|
| `Cell` | structure `(row col : ℕ)` |
| `Cell.content` | `(col : ℤ) - (row : ℤ)` |
| `Cell.transpose` | swap `row ↔ col` |
| `Cell.transpose_transpose` | involutive |
| `Cell.content_plus_transpose_content_eq_zero` | summand-by-summand cancellation, by `ring` |
| `PartitionWithCells` | structure `(cells : List Cell)` |
| `PartitionWithCells.content_sum` | `Σ c(x)` over cells |
| `PartitionWithCells.transpose` | map `Cell.transpose` over the list |
| `PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero` | partition-level cancellation, proved by induction + `linarith` |
| `PartitionWithCells.self_transpose_content_sum_zero` | self-dual partitions have content sum zero |

## Application to chirality $\langle c \rangle_\beta$

The chirality first-order coefficient
([`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation))
is the Wedderburn-weighted average

$$
  \langle c \rangle_\beta
  \;=\;
  \frac{\sum_\lambda w_\lambda \chi^\lambda(\beta) c(\lambda)}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Under Type-B folding, the partition-summation $\sum_\lambda$ is
reorganised into pairs $\{\lambda, \lambda^T\}$. By the cancellation
theorem above, $c(\lambda) + c(\lambda^T) = 0$ for every pair.
Therefore $\langle c \rangle_\beta$ reduces to the **imbalance**
between $\chi^\lambda(\beta)$ and $\chi^{\lambda^T}(\beta)$ along
the paired cells:

$$
  \langle c \rangle_\beta
  \;=\;
  \frac{\sum_{\lambda < \lambda^T} w_\lambda c(\lambda)
        \bigl[\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)\bigr]}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

The self-dual partitions ($\lambda = \lambda^T$) contribute zero
to the numerator (by the `self_transpose_content_sum_zero` lemma);
only the genuinely chiral pairs contribute. This is the Type-B
folded crystal computation that
[`prop:crystal-basis-resolves-mass-tower-open-problems`](#prop:crystal-basis-resolves-mass-tower-open-problems)
identifies as the structural reduction of the chirality factor.

## Significance

The proposition closes a small but genuine structural gap: the
"why does Type-B folding help?" claim from CLAUDE.md §7b is now
backed by a sorry-free Lean theorem demonstrating the cell-level
cancellation that drives the folded-crystal symmetry. The full
chirality first-order coefficient computation still requires the
explicit character imbalance $\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)$,
but the partition-content half is now structural infrastructure
rather than an open claim.
