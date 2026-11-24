Let $(\mathbf{C}, A, \tau)$ be a [QOU](#def:quantum-observable-universe) equipped with [weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$ and [Reeb derivation](#def:categorical-reeb) $\xi$.

The **substrate line bundle** is the trivial $\mathbb{G}_m$-torsor

$$
  \mathcal{Q}
  = 
  \mathrm{End}(\mathbf{1}) \otimes_\mathbb{Z} \mathbb{G}_m
   \to 
  \mathrm{Spec}R,
$$

with fibre $\mathbb{G}_m(R) = R^\times$ over each $R$-point. A **substrate section** is a global section $q \colon \mathrm{Spec}R \to \mathcal{Q}$, that is, an element $q \in R^\times$.

Over $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$, the **universal substrate differential** is

$$
  \mathbf{d}
  = 
  q^{-1}d + (1 - q^{-1})\pi_V \circ d
   \in 
  \mathrm{Hom}_{\mathbb{Z}[q,q^{-1}]}\!
  \bigl(\Omega^k(A), \Omega^{k+1}(A)\bigr).
$$
