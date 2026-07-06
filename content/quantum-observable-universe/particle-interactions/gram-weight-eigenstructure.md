The Gram weights $w_k^G$ ([Gram-weighted $Q$-value](#prop:gram-weighted-qvalue)) arise from the eigenstructure of the Gram matrix $G$ on $H_A(q)$. They reflect the decomposition of $H_A(q)$ into irreducible representations.

## Eigendecomposition

The Gram matrix $G$ on the NF subspace of $H_A(q)$ has the eigendecomposition:

$$
  G = \sum_\alpha \lambda_\alpha \, v_\alpha v_\alpha^T
$$

where $\lambda_\alpha$ are the eigenvalues and $v_\alpha$ the orthonormal eigenvectors. Each eigenspace corresponds to a sector of the Wedderburn-Artin decomposition $H_A(R, q) \cong \bigoplus_\lambda M_{d_\lambda}(R)$.

The Gram matrix is not positive definite: it has both positive and negative eigenvalues. For $A = 4$ (${}^4\mathrm{He}$), the signature is $(7{+}, 1{-})$ on the $8$-dimensional NF subspace. For $A = 6$ (${}^6\mathrm{He}$), the signature has hundreds of negative eigenvalues.

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

The positive eigenspaces contribute positively. The negative eigenspaces contribute negatively. The physical Frobenius norm $\lVert \delta_k \rVert_F = \sqrt{|\sum_\alpha \lambda_\alpha c_{k\alpha}^2|}$ is the absolute magnitude.

## Boundary vs interior suppression

For ${}^6\mathrm{He}$ ($N = 4$ neutrons at positions $\{0, 2, 4, 5\}$), the computed Frobenius norms are:

| $k$ | position | $\lVert \delta_k \rVert_F$ | normalised $w_k^G$ |
|:---:|:--------:|:-------------------------:|:------------------:|
| $0$ | $0$ | $0.260$ | $0.304$ |
| $1$ | $2$ | $0.186$ | $0.218$ |
| $2$ | $4$ | $0.231$ | $0.271$ |
| $3$ | $5$ | $0.176$ | $0.206$ |

The boundary neutrons ($k = 0$ at the proton-shell edge, $k = 2$ adjacent to the last proton) have larger Frobenius norms than the interior neutrons ($k = 1, 3$ deep in the neutron shell).

This non-uniformity manifests the adjoint character of the Frobenius algebra. The Gram inner product weights each conversion channel by the geometric distance (in the Frobenius metric) between parent and daughter in $H_A(q)$.

## Connection to the Markov trace decomposition

The Markov trace decomposes over irreps as:

$$
  \mathrm{tr}_M(x)
  = \sum_\lambda \frac{z^A}{s_\lambda(q)} \, \chi_\lambda(x)
$$

where $s_\lambda(q) = \prod_{\square \in \lambda} [h(\square)]_q$ is the Schur element (product of $q$-hook lengths) and $\chi_\lambda$ is the character of irrep $\lambda$ ([RJ inner product](#prop:rj-canonical-inner-product)).

The Gram matrix is the matrix of this bilinear form restricted to the NF basis. Its eigenvalues $\lambda_\alpha$ encode the Schur elements. Small eigenvalues (near zero) correspond to representations with large Schur elements (highly symmetric tableaux). Large eigenvalues correspond to representations with small Schur elements (asymmetric tableaux).

The Gram weight $w_k^G$ measures the change in representation content when neutron $k$ converts. A neutron whose conversion significantly reshuffles the irrep decomposition (boundary neutron, crossing a shell boundary) receives a larger weight than one whose conversion leaves the representation structure intact (interior neutron, staying within a shell).
