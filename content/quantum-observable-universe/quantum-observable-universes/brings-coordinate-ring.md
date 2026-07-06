Bring's curve $\mathcal{B} \subset \mathbb{P}^4$ is defined as the
complete intersection

$$
\mathcal{B}
=  V\!\bigl(
  \textstyle\sum x_i,
  \textstyle\sum x_i^2,
  \textstyle\sum x_i^3
\bigr)
\subset \mathbb{P}^4,
$$

where $[x_0 : x_1 : x_2 : x_3 : x_4]$ are homogeneous coordinates.
This is a smooth algebraic curve of genus $g = 4$, and it serves as the
spectral coordinate fiber of the algebraic substrate.

The :defterm[non-commutative coordinate ring]{#brings-coordinate-ring} of $\mathcal{B}$ is defined as the
quotient

$$
\mathcal{O}_q(\mathcal{B})
=  \mathcal{O}_q(\mathbb{P}^4) \big/
\bigl(
  \textstyle\sum x_i,
  \textstyle\sum x_i^2,
  \textstyle\sum x_i^3
\bigr),
$$

where $\mathcal{O}_q(\mathbb{P}^4)$ is the quantum polynomial ring with
relations $x_i x_j = q x_j x_i$ for $i < j$.

**Symmetry.** The symmetric group $S_5$ acts on $\mathcal{B}$ by
permutation of the homogeneous coordinates. This action descends to an
$S_5$-action on $\mathcal{O}_q(\mathcal{B})$ by algebra automorphisms,
reflecting the five-fold combinatorial symmetry of the substrate.

**Spectral modes.** By the Riemann--Hurwitz formula, a smooth curve of
genus $g$ has $2g$ independent cycles in its first homology. For
$\mathcal{B}$ with $g = 4$, the $2g = 8$ fundamental modes of the Reeb
spectrum correspond to these $8$ independent cycles, providing the
spectral basis for the derivation $\xi_q$ acting on $A$.
