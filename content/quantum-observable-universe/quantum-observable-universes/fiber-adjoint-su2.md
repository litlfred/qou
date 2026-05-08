Continuing [projective line on $\mathrm{SU}(2)$](#ex:projective-line-su2), take
$G = \mathrm{SU}(2)$, $T = \mathrm{U}(1)$, and
$V = \mathbb{C}^2$. The projective line object is
$\mathbb{P}(V) = \mathbb{P}^1(\mathbb{C})$, and the adjoint object is
$\mathrm{Ad}(A) \cong \mathfrak{su}(2) \cong \mathbb{R}^3$
(trace-free skew-Hermitian $2 \times 2$ matrices under the Killing
form). The embedding $\sigma$ sends a line
$\ell = \mathrm{span}(v) \subset \mathbb{C}^2$ to the rank-$1$
projector

$$
  \sigma([\ell]) =
  \frac{v v^{\dagger}}{\lVert v \rVert^2}
  - \tfrac{1}{2}\mathrm{id}_V
  \in \mathfrak{su}(2).
$$

This identifies $\mathbb{P}^1(\mathbb{C})$ with the unit $2$-sphere
$S^2 \subset \mathfrak{su}(2)$ (the coadjoint orbit of
$\tfrac{1}{2}\mathrm{diag}(i, -i)$). Observability follows:
a $G$-fixed point in $\mathfrak{su}(2)$ would be a matrix commuting
with all of $\mathrm{SU}(2)$, hence a scalar --- but trace-free matrices
have no non-zero scalars, so
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
