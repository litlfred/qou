For the [substrate line bundle](#def:substrate-line-bundle), fibring $(\mathbf{C}, A, \tau)$ over a space $M$ (the archimedean realisation) recasts the substrate line bundle as $\mathcal{Q}_M = M \times \mathbb{G}_m$. A substrate section operates as a strict map $q \colon M \to \mathbb{G}_m(k) = k^\times$.

**The $\mathbb{P}^1$-compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the standard inclusion $k^\times \hookrightarrow k \cup \{\infty\} = \mathbb{P}^1(k)$. The compactified substrate bundle evaluates to

$$
  \bar{\mathcal{Q}}_M
  = 
  M \times \mathbb{P}^1
   \to  M.
$$

A given substrate section extends uniquely to a $\mathbb{P}^1$-valued section $\bar{q} \colon M \to \mathbb{P}^1$. Three specific sections dominate the physics:

| Section | Value | Differential $d_q$ | Regime |
|---|---|---|---|
| $q = 0$ | $[0] \in \mathbb{P}^1$ | Undefined (strict $q^{-1}$ pole) | Boundary (divergent spatial metric) |
| $q = 1$ | $[1] \in \mathbb{P}^1$ | $d$ (unmodified de Rham) | Classical |
| $q = \infty$ | $[\infty] \in \mathbb{P}^1$ | $\pi_V \circ d$ (purely vertical) | Deep quantum |

**The universal family.** The universal substrate differential $\mathbf{d}$ is a morphism of $\mathbb{Z}[q, q^{-1}]$-modules. Given a ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ executing $q \mapsto q_0$, the targeted base change $\mathbf{d} \otimes_\iota k$ exactly recovers the differential $d_{q_0}$ spanning the specialisation $q_0$.
