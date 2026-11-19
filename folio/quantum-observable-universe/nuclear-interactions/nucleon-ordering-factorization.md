The Wedderburn--Artin decomposition of $H_3(q)$, combined with jet-descended confinement, factorizes the nuclear Markov trace. This factorization renders the ground-state ordering search trivial in two of the three channels.

## Statement

**Proposition.**
*The Markov trace decomposes as:*

$$
  \mathrm{tr}_M(\mathcal{N})
  =
  W_{\mathrm{sym}} \cdot S(\pi)
  + W_{\mathrm{std}} \cdot (z \cdot a_\pi + b_\pi)
  + W_{\mathrm{alt}} \cdot A(\pi)
$$

*(i) Ordering independence of scalar channels.*
*The symmetric product $S(\pi)$ and alternating product $A(\pi)$ remain independent of the ordering $\pi$ for a fixed composition.*

*(ii) Standard-channel factorization.*
*The standard-channel state emerges from a $2 \times 2$ matrix product.*

*(iii) Jet-descended nucleon blocks.*
*Intra-nucleon crossings yield fixed $2 \times 2$ transfer matrices $T_\mathfrak{p}^{\mathrm{std}}$ and $T_\mathfrak{n}^{\mathrm{std}}$, precomputed once.*

*(iv) Inter-nucleon crossings (transient).*
*Each inter-nucleon crossing carries a $2 \times 2$ matrix dictated by the pair type.*

## Computational consequence

Factorization reduces the ordering search cost from $\binom{A}{Z} \times O(A^2) \times O(36)$ to $\binom{A}{Z} \times O(A^2) \times O(4)$, providing a $\sim 9 \times$ reduction per ordering.

## Compact nucleon notation

The factorization suggests a natural nucleon-level alphabet. A nucleus is written:

$$
  \mathcal{N}(\pi)
  =
  \mathfrak{t}_1 \cdot \mathfrak{t}_2 \cdots \mathfrak{t}_A
$$

where $\mathfrak{t}_k \in \{\mathfrak{p}, \mathfrak{n}\}$. The six normal-form coefficients per nucleon collapse to a $2 \times 2$ matrix plus two precomputed scalars.
