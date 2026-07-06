Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[weight decomposition](#def:weight-decomposition)
$(\pi_H, \pi_V)$ and
[Reeb derivation](#def:categorical-reeb) $\xi$.

**The substrate line bundle** is the trivial
$\mathbb{G}_m$-torsor

$$
  \mathcal{Q}
  = 
  \mathrm{End}(\mathbf{1}) \otimes_\mathbb{Z} \mathbb{G}_m
   \to 
  \mathrm{Spec}R,
$$

whose fibre at each $R$-point is $\mathbb{G}_m(R) = R^\times$.
A **substrate section** is a global section
$q \colon \mathrm{Spec}R \to \mathcal{Q}$, i.e. an element
$q \in R^\times$.

When $(\mathbf{C}, A, \tau)$ is fibred over a space $M$
(archimedean realisation), the substrate line bundle is
$\mathcal{Q}_M = M \times \mathbb{G}_m$ and a substrate
section is a map $q \colon M \to \mathbb{G}_m(k) = k^\times$.

**The $\mathbb{P}^1$-compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the
standard inclusion
$k^\times \hookrightarrow k \cup \{\infty\} = \mathbb{P}^1(k)$.
The compactified substrate bundle is

$$
  \bar{\mathcal{Q}}_M
  = 
  M \times \mathbb{P}^1
   \to  M.
$$

A substrate section extends to a $\mathbb{P}^1$-valued section
$\bar{q} \colon M \to \mathbb{P}^1$.  The three distinguished
sections are:

| Section | Value | Differential $d_q$ | Regime |
|---|---|---|---|
| $q = 0$ | $[0] \in \mathbb{P}^1$ | Undefined ($q^{-1}$ pole) | Boundary (spatial divergence) |
| $q = 1$ | $[1] \in \mathbb{P}^1$ | $d$ (full de Rham) | Classical |
| $q = \infty$ | $[\infty] \in \mathbb{P}^1$ | $\pi_V \circ d$ (vertical) | Deep quantum |

**The universal family.**
Over $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$,
define the **universal substrate differential**

$$
  \mathbf{d}
  = 
  q^{-1}d + (1 - q^{-1})\pi_V \circ d
   \in 
  \mathrm{Hom}_{\mathbb{Z}[q,q^{-1}]}\!
  \bigl(\Omega^k(A), \Omega^{k+1}(A)\bigr).
$$

This is a morphism of $\mathbb{Z}[q, q^{-1}]$-modules.  For
any ring homomorphism
$\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ sending
$q \mapsto q_0$, the base change
$\mathbf{d} \otimes_\iota k$ recovers the differential
$d_{q_0}$ at the specialisation $q_0$.
