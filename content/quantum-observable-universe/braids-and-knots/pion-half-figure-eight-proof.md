**Proof.** On $V_{(2,1)}$, both $\mathfrak{M}_+$ and $\sigma_1\sigma_2^{-1}$ have determinant $+1$. This follows because both decompose into an even number of Hecke generators, and each generator has determinant $-1$. Both matrices have real trace on $V_{(2,1)}$:

$$
  \chi^{(2,1)}(\mathfrak{M}_+) = -(h^2 + 1),
  \qquad
  \chi^{(2,1)}(\sigma_1\sigma_2^{-1}) = -(h^2 + 1).
$$

Since both are $2 \times 2$ matrices with $\det = 1$ and identical trace, they share the same characteristic polynomial:

$$
  \lambda^2 + (h^2 + 1)\lambda + 1 = 0.
$$

The eigenvalues are therefore identical:
$\lambda = \tfrac{-(h^2+1) \pm \sqrt{(h^2+1)^2 - 4}}{2}$. These give complex conjugates on the unit circle with phase $\theta = \arccos\bigl(-(h^2+1)/2\bigr)$. $\square$
