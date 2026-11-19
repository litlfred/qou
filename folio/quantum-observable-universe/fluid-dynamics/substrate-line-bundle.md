Let $(\mathbf{C}, A, \tau)$ define a [QOU](#def:quantum-observable-universe) equipped with [weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$ and [Reeb derivation](#def:categorical-reeb) $\xi$.

**The aether line bundle** is the trivial $\mathbb{G}_m$-torsor

$$
  \mathcal{Q}
  = 
  \mathrm{End}(\mathbf{1}) \otimes_\mathbb{Z} \mathbb{G}_m
   \to 
  \mathrm{Spec}R,
$$

possessing fibre $\mathbb{G}_m(R) = R^\times$ across each $R$-point. An **aether section** defines a global section $q \colon \mathrm{Spec}R \to \mathcal{Q}$, resolving to an element $q \in R^\times$.

Fibring $(\mathbf{C}, A, \tau)$ over a space $M$ (the archimedean realisation) recasts the aether line bundle as $\mathcal{Q}_M = M \times \mathbb{G}_m$. An aether section operates as a strict map $q \colon M \to \mathbb{G}_m(k) = k^\times$.

**The $\mathbb{P}^1$-compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the standard inclusion $k^\times \hookrightarrow k \cup \{\infty\} = \mathbb{P}^1(k)$. The compactified aether bundle evaluates to

$$
  \bar{\mathcal{Q}}_M
  = 
  M \times \mathbb{P}^1
   \to  M.
$$

A given aether section extends uniquely to a $\mathbb{P}^1$-valued section $\bar{q} \colon M \to \mathbb{P}^1$. Three specific sections dominate the physics:

| Section | Value | Differential $d_q$ | Regime |
|---|---|---|---|
| $q = 0$ | $[0] \in \mathbb{P}^1$ | Undefined (strict $q^{-1}$ pole) | Boundary (divergent spatial metric) |
| $q = 1$ | $[1] \in \mathbb{P}^1$ | $d$ (unmodified de Rham) | Classical |
| $q = \infty$ | $[\infty] \in \mathbb{P}^1$ | $\pi_V \circ d$ (purely vertical) | Deep quantum |

**The universal family.**
Operating over $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$, the **universal aether differential** is

$$
  \mathbf{d}
  = 
  q^{-1}d + (1 - q^{-1})\pi_V \circ d
   \in 
  \mathrm{Hom}_{\mathbb{Z}[q,q^{-1}]}\!
  \bigl(\Omega^k(A), \Omega^{k+1}(A)\bigr).
$$

This acts as a strict morphism of $\mathbb{Z}[q, q^{-1}]$-modules. Given a ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ executing $q \mapsto q_0$, the targeted base change $\mathbf{d} \otimes_\iota k$ exactly recovers the differential $d_{q_0}$ spanning the specialisation $q_0$.
