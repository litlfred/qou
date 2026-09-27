Let $M_0$ be a compact Riemann surface of genus $g$ and $V \to M_0$ a holomorphic vector bundle of rank $r$ and degree $d = \deg \det V$. Its **Chern character** is the cohomology class

$$
  \operatorname{ch}(V) \;=\; r + c_1(V) \;\in\; H^0(M_0; \mathbb{Q}) \oplus H^2(M_0; \mathbb{Q}),
$$

with no higher terms because $M_0$ has real dimension two; integrating the degree-two part over $M_0$ gives $d$. The **Todd class** of the curve is $\operatorname{td}(M_0) = 1 + \tfrac{1}{2} c_1(TM_0)$, and $\int_{M_0} c_1(TM_0) = 2 - 2g$ is the Euler characteristic of the surface (Poincaré–Hopf). The Hirzebruch–Riemann–Roch theorem \cite{hartshorne-1977} computes the sheaf Euler characteristic of $V$ from these two classes:

$$
  \chi(M_0, V) \;=\; h^0(M_0, V) - h^1(M_0, V) \;=\; \int_{M_0} \operatorname{ch}(V) \operatorname{td}(M_0) \;=\; d + r\,(1 - g).
$$

Three instances are used in this chapter.

1. *The trivial bundle*: $\chi(M_0, \mathcal{O}) = 1 - g$, which is $-3$ for $g = 4$; here $h^0 = 1$ and $h^1 = g$.
2. *The tangent bundle*: $d = 2 - 2g$ and $r = 1$, so $\chi(M_0, TM_0) = 3 - 3g = -9$ for $g = 4$. Since a curve of genus at least two has no holomorphic vector fields, $h^0(TM_0) = 0$ and therefore $h^1(M_0, TM_0) = 3g - 3 = 9$. This is the dimension of the space of first-order deformations of the curve; for Bring's surface it decomposes under $S_5$ as the four-dimensional standard representation plus the five-dimensional representation $[3,2]$, with no invariant vector, which is why Bring's surface admits no deformation preserving its symmetry.
3. *A rank-two bundle of degree zero*: $\chi(M_0, V) = 2(1 - g) = 2 - 2g$, the one case in which the sheaf Euler characteristic of a bundle agrees with the topological Euler characteristic of the surface. This is the coincidence that once let a single symbol $\chi$ stand for both.

The Chern character is additive on short exact sequences and multiplicative on tensor products, so it descends to a ring homomorphism from the Grothendieck group $K^0(M_0)$ of vector bundles to $H^{\mathrm{even}}(M_0; \mathbb{Q})$. On a curve that homomorphism records only rank and degree, which is why every Euler characteristic in this chapter is a linear function of those two integers.
