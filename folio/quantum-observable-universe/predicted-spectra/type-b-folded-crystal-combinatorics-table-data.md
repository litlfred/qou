| Datum / identity | Mathematical content |
|---|---|
| Diagram cell | Ordered pair $(r, \mathrm{col}) \in \mathbb{N}^2$ |
| Cell content | $c(r, \mathrm{col}) = \mathrm{col} - r \in \mathbb{Z}$ |
| Cell transpose | $(r, \mathrm{col})^T = (\mathrm{col}, r)$ |
| Transpose involution | $((r, \mathrm{col})^T)^T = (r, \mathrm{col})$ |
| Cell-level cancellation | $c(r, \mathrm{col}) + c(\mathrm{col}, r) = 0$ |
| Partition diagram | Finite cell list representing $\lambda$ |
| Partition content sum | $c(\lambda) = \sum_{x \in \lambda} c(x)$ |
| Conjugate diagram $\lambda^T$ | Elementwise cell transpose across $\lambda$ |
| Partition-level cancellation | $c(\lambda) + c(\lambda^T) = 0$ by induction on cells |
| Self-conjugate vanishing | $\lambda = \lambda^T \implies c(\lambda) = 0$ |
