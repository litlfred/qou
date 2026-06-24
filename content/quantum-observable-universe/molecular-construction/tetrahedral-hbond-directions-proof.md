Realise the four hydrogen-bond directions as the vertex vectors of a regular tetrahedron inscribed in the cube,
$$ u_1 = (1,1,1),\quad u_2 = (1,-1,-1),\quad u_3 = (-1,1,-1),\quad u_4 = (-1,-1,1), $$
the four sign patterns of $(\pm1,\pm1,\pm1)$ with an even number of minus signs. With the Euclidean dot product on $\mathbb{R}^3$, the claim reduces to four explicit computations, each verified exactly in the Lean sibling.

**Balanced coordination.** Summing coordinate-wise, the $+1$ and $-1$ entries cancel in every slot, $u_1 + u_2 + u_3 + u_4 = (0,0,0)$ (Lean `tetra_sum_zero`): the two donor and two acceptor bonds exert no net directional bias.

**Common length.** Each $u_i$ is a $\pm1$ vector in three coordinates, so $u_i \cdot u_i = 3$, $|u_i| = \sqrt 3$ (Lean `tetra_normSq`; the four are sign/permutation images of one another).

**Pairwise dot product.** For distinct vertices exactly two of the three coordinate products are $-1$ and one is $+1$, e.g. $u_1 \cdot u_2 = 1 - 1 - 1 = -1$ (Lean `tetra_dot12`); equivalently $u_i \cdot u_j = 4\,\delta_{ij} - 1$.

**Bond-angle cosine.** Combining the last two,
$$ \cos\theta_0 = \frac{u_i \cdot u_j}{|u_i|\,|u_j|} = \frac{-1}{\sqrt3 \cdot \sqrt3} = -\tfrac13 $$
(Lean `tetrahedral_cos`), so $\theta_0 = \arccos(-\tfrac13) \approx 109.47^\circ$. Equal cosine across all pairs, equal length, and zero sum make the four directions the vertices of a regular tetrahedron. This $\theta_0$ is the unperturbed reference from which the lone-pair shift displaces the H–O–H angle to $\approx 104.5^\circ$. $\qquad\blacksquare$
