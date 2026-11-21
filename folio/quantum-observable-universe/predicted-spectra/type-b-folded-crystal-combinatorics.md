*For every partition $\lambda$ realized as a list of cells with contents $c(r, \mathrm{col}) := \mathrm{col} - r$, the cell-level content cancellation*

$$
  c(r, \mathrm{col}) + c(\mathrm{col}, r) = 0
$$

*lifts to the partition-level identity*

$$
  \sum_{x \in \lambda} c(x) + \sum_{x \in \lambda^T} c(x) = 0,
$$

*where $\lambda^T$ is the transpose partition. Self-dual partitions $\lambda = \lambda^T$ have content sum zero.*

## Application to chirality $\langle c \rangle_\beta$

The chirality first-order coefficient is the Wedderburn-weighted average:

$$
  \langle c \rangle_\beta = \frac{\sum_\lambda w_\lambda \chi^\lambda(\beta) c(\lambda)}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Under Type-B folding, the partition summation $\sum_\lambda$ reorganizes into pairs $\{\lambda, \lambda^T\}$. The cancellation theorem forces $c(\lambda) + c(\lambda^T) = 0$ for every pair. The coefficient $\langle c \rangle_\beta$ isolates the character imbalance $\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)$ between paired cells:

$$
  \langle c \rangle_\beta = \frac{\sum_{\lambda < \lambda^T} w_\lambda c(\lambda)
        \bigl[\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)\bigr]}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Self-dual partitions satisfy $\lambda = \lambda^T$ and contribute zero to the numerator. Only chiral pairs contribute. Type-B folded crystals structurally reduce the chirality factor.

## Significance

This proposition closes a structural gap. The cell-level cancellation driving folded-crystal symmetry is proved. The full chirality computation requires the character imbalance $\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)$. The partition-content cancellation provides the necessary structural infrastructure.
