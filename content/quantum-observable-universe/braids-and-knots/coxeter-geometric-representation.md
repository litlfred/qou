Let $M$ be a Coxeter matrix over an index set $B$. On the free module
$\bigoplus_{i \in B} \mathbb{R}\,\alpha_i$ equip the pairing with
matrix entries $\langle \alpha_i, \alpha_j \rangle = -\cos(\pi/m_{ij})$
for $i \neq j$ and $\langle \alpha_i, \alpha_i \rangle = 1$, and set

$$
f_i \;=\; \mathrm{id} \;-\; 2\,\langle \alpha_i, \cdot\, \rangle\,
\alpha_i .
$$

Then the $f_i$ satisfy the Coxeter relations of $M$ —
$(f_i f_j)^{m_{ij}} = 1$ for every pair, at every bond order — so they
assemble into the geometric representation of any Coxeter system
$(W, S)$ over $M$. Since $f_i$ and $f_j$ act with opposite signs on
$\alpha_i$ when $i \neq j$, the simple reflections of every Coxeter
system are pairwise distinct: $s_i \neq s_j$ with no hypothesis.

The bond-order relation at $m_{ij} \geq 3$ is a Chebyshev argument.
Writing $g = f_i f_j$ and tracking the scalar pair
$\bigl(\langle \alpha_i, g^k w \rangle, \langle \alpha_j, g^k w
\rangle\bigr)$ of an arbitrary vector $w$, both components satisfy the
second-order recursion

$$
u_{k+2} \;=\; 2\cos\varphi \cdot u_{k+1} \;-\; u_k,
\qquad \varphi = \tfrac{2\pi}{m_{ij}},
$$

whose solutions are trigonometric and hence $m_{ij}$-periodic. The
action of $g^k$ differs from the identity by singles accumulated from
these scalars; periodicity and telescoping force both accumulated sums
to vanish, the coefficient matrix being invertible because
$\cos^2(\pi/m_{ij}) < 1$. Thus $g^{m_{ij}} w = w$. The remaining orders
are elementary: $m_{ij} = 2$ is direct commutation of the two
reflections, and the diagonal is the involution $f_i^2 = 1$.

Combined with the collapsed Tits residue, every hypothesis in the
parabolic-transversal chain is discharged: the braid and
far-commutation relations on the length-rule module hold for every
Coxeter system unconditionally.
