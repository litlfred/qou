**Proof.**
The Borromean braid has $6$ crossings with quaternion images
$[i, -j, i, -j, i, -j]$ and signs $[+1, -1, +1, -1, +1, -1]$.
The $\binom{6}{2} = 15$ pairwise products $s_k s_l \, c_k c_l$
are $2 \times 2$ quaternion matrices.  Their sum has trace:

$$
  \mathrm{tr}\!\bigl(\textstyle\sum_{k < l}
  s_k s_l \, c_k c_l\bigr)
  = \mathrm{tr}\!\begin{pmatrix}
    -6 & 3i \\ 3i & -6
  \end{pmatrix}
  = -12.
$$

Since $\dim(V) = 2$ and $\chi(\Sigma_4) = 2 - 2 \cdot 4 = -6$,
the identity $-12 = 2 \cdot (-6)$ holds. $\square$

The complete non-abelian Stokes chain connecting the three layers:

| Layer | Value | Source |
|-------|------:|--------|
| **Algebraic** ($Q_{8}$ crossed module) | $-12$ | $\dim(V) \cdot \chi(\Sigma_4)$ |
| **Geometric** (hyperbolic volume) | $-8G$ | $-12 \times \tfrac{2G}{3}$ (Bring bridge) |
| **Boundary** (Markov trace $\kappa$) | $\tfrac{3}{16}$ | $-12 \div (-64)$ via $\Phi_0$ |

The *Bring bridge factor* $\tfrac{2G}{3} = \tfrac{4}{3}\,\Lambda(\pi/4)$
converts the algebraic per-cell curvature $-\tfrac{3}{2}$ to the
geometric per-cell volume $-G$ (Catalan constant), where $\Lambda$
is the Lobachevsky function and $G = \mathrm{Vol}(\mathcal{B}_3)/8$.
