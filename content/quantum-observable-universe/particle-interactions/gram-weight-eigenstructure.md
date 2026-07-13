The Gram weights $w_k^G$ arise from the eigenstructure of the Gram matrix $G$ on $H_A(q)$. They reflect the decomposition of $H_A(q)$ into irreducible representations.

## Eigendecomposition

The Gram matrix $G$ on the NF subspace of $H_A(q)$ has the eigendecomposition:

$$
  G = \sum_\alpha \lambda_\alpha \, v_\alpha v_\alpha^T
$$

The Gram matrix is not positive definite: it has both positive and negative eigenvalues.

## Projection of the conversion difference

The difference element $\delta_k = \mathcal{G}_{\mathrm{par}} - \mathcal{G}_{\mathrm{dau}}^{(k)}$ decomposes as:

$$
  \delta_k = \sum_\alpha c_{k\alpha} \, v_\alpha
$$

Its squared Frobenius norm is:

$$
  \lVert \delta_k \rVert_F^2
  = \delta_k \cdot G \cdot \delta_k
  = \sum_\alpha \lambda_\alpha \, c_{k\alpha}^2.
$$

The physical Frobenius norm $\lVert \delta_k \rVert_F = \sqrt{|\sum_\alpha \lambda_\alpha c_{k\alpha}^2|}$ is the absolute magnitude.

## Boundary vs interior suppression

The boundary neutrons have larger Frobenius norms than the interior neutrons. This non-uniformity manifests the adjoint character of the Frobenius algebra. The Gram inner product weights each conversion channel by the geometric distance between parent and daughter in $H_A(q)$.

## Connection to the Markov trace decomposition

The Markov trace decomposes over irreps as:

$$
  \mathrm{tr}_M(x)
  = \sum_\lambda \frac{z^A}{s_\lambda(q)} \, \chi_\lambda(x)
$$

The Gram matrix is the matrix of this bilinear form restricted to the NF basis. Its eigenvalues $\lambda_\alpha$ encode the Schur elements. Small eigenvalues correspond to representations with large Schur elements. Large eigenvalues correspond to representations with small Schur elements.

The Gram weight $w_k^G$ measures the change in representation content when neutron $k$ converts. A neutron whose conversion significantly reshuffles the irrep decomposition receives a larger weight than one whose conversion leaves the representation structure intact.
