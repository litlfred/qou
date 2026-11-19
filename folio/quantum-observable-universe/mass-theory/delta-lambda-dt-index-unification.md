**Proposition.** *Let $\lambda$ be a partition, written as a weakly decreasing list, with
a-function grade $n(\lambda)$ and Wedderburn dimension $\dim V_\lambda$. Set*

$$
  \Delta_\lambda \;=\; (-1)^{n(\lambda)}\,\dim V_\lambda .
$$

*Then both factors are identified with independently-defined objects:*

1. *(**value**) the DT / 3d-index Euler characteristic on the graded pieces equals
   $\Delta_\lambda$,*

$$
  \sum_{k=0}^{n(\lambda)} (-1)^k \dim \mathrm{gr}_k
  \;=\; (-1)^{n(\lambda)}\,\dim V_\lambda ;
$$

2. *(**chirality**) the a-function parity equals the geometric longest-element sign,*

$$
  (-1)^{n(\lambda)} \;=\; (-1)^{\sum_i \binom{\lambda'_i}{2}} ,
$$

*where $\lambda'$ is the conjugate partition. Both hold for every $n$, with no restriction.*

### Theorem status versus definitional stipulation

Writing $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$ by itself asserts nothing: it names
a product of a sign and a dimension. The content is that **neither factor is free**:

- the magnitude is forced as an **Euler characteristic**, an alternating sum over the graded
  pieces, rather than being posited as the Wedderburn dimension;
- the sign is forced as a **geometric** invariant (the longest-element sign of the associated
  Weyl-group datum) rather than being posited as the jet-order parity.

The bridge between the two readings of the sign is the combinatorial identity
$n(\lambda) = \sum_i \binom{\lambda'_i}{2}$, which is what removes the earlier $n \le 5$
restriction: the chirality leg had been established only for small $n$ until that identity was
proved in general.

### Scope: the value only

This fixes the **per-partition value**. It does **not** determine the extensive many-body binding
**magnitude**, which requires an additional body-order mechanism: no per-block weight converts an intensive quantity into an
extensive one, so the missing contribution is a separate additive extensive term rather than a
different choice of $\Delta_\lambda$. Six closure ansätze have failed on the deuteron for
exactly that reason. Nothing here should be read as narrowing that gap.

### Consumers

The per-isotope binding algorithm consumes $\Delta_\lambda$ through
[`alg:delta-lambda-closure`](#alg:delta-lambda-closure), which computes the value above and
hands it to Step 9b.
