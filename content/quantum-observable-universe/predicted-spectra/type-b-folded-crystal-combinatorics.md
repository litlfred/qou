**Proposition (Type-B folded crystal cancellation).**
*For every partition $\lambda$ realized as a list of cells with contents $c(r, \mathrm{col}) := \mathrm{col} - r$, the cell-level content cancellation*

$$
  c(r, \mathrm{col}) + c(\mathrm{col}, r) = 0
$$

*lifts to the partition-level identity*

$$
  \sum_{x \in \lambda} c(x) + \sum_{x \in \lambda^T} c(x) = 0,
$$

*where $\lambda^T$ is the transpose partition. Self-dual partitions $\lambda = \lambda^T$ have content sum zero.*

## Lean structure

See [Table](#tbl:type-b-folded-crystal-combinatorics-table-data).

## Application to chirality $\langle c \rangle_\beta$

The chirality first-order coefficient is the Wedderburn-weighted average:

$$
  \langle c \rangle_\beta = \frac{\sum_\lambda w_\lambda \chi^\lambda(\beta) c(\lambda)}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Under Type-B folding, the partition summation $\sum_\lambda$ reorganizes into pairs $\{\lambda, \lambda^T\}$. By the cancellation theorem, $c(\lambda) + c(\lambda^T) = 0$ for every pair. Therefore, $\langle c \rangle_\beta$ reduces to the imbalance between $\chi^\lambda(\beta)$ and $\chi^{\lambda^T}(\beta)$ along paired cells:

$$
  \langle c \rangle_\beta = \frac{\sum_{\lambda < \lambda^T} w_\lambda c(\lambda)
        \bigl[\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)\bigr]}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Self-dual partitions ($\lambda = \lambda^T$) contribute zero to the numerator; only genuinely chiral pairs contribute. This Type-B folded crystal computation structurally reduces the chirality factor.

## Significance

This proposition closes a structural gap: a sorry-free Lean theorem now demonstrates the cell-level cancellation that drives folded-crystal symmetry. The full chirality computation requires the explicit character imbalance $\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)$, but the partition-content half is established structural infrastructure.
