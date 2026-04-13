The character sum over all $4^A$ channel configurations
admits an **exact closed-form factorization** in terms of
the spectator normalization and the channel-sum difference.

## Statement

**Proposition.**
*For $\beta^-$ decay of a nucleus $(Z, N)$ with $A = Z + N$:*

$$
  \sum_{\text{all } 4^A \text{ configs}}
  \Delta m_e
  = a^Z \cdot b^{N-1} \cdot (a - b)
$$

*where $a = \sum_c G_P(c)$ and $b = \sum_c G_N(c)$ are the
per-nucleon channel sums
([spectator normalization](#def:spectator-normalization)).*

## Proof

The full character sum distributes over the product structure
of the
[per-nucleon decomposition](#def:per-nucleon-channel-decomposition):

$$
  \sum_{c_1, \ldots, c_A}
  \Bigl(\prod_{m=1}^{A} G_{n'_m}(c_m)
        - \prod_{m=1}^{A} G_{n_m}(c_m)\Bigr)
$$

where $n'_m$ is the daughter nucleon type (the changed nucleon
switches $N \to P$; all others unchanged).  Since the sum over
$c_m$ factors independently for each nucleon:

$$
  = \Bigl(\prod_{\text{spectator } P} a\Bigr)
    \cdot \Bigl(\prod_{\text{spectator } N} b\Bigr)
    \cdot (a - b)
  = a^Z \cdot b^{N-1} \cdot (a - b)
$$

The factorization is **exact** — no approximation is involved.
The only inputs are the eight per-nucleon channel values
$G_P(c)$ and $G_N(c)$, which are rational functions of $q$.
