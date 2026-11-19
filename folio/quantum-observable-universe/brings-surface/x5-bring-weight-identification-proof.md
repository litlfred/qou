*Proof.*
Eigenvalue on $\mathcal{X}_5$: the automorphism $\phi_5(x, y) = (\zeta_5 x, y)$
pulls back the coordinate function $x$ to
$(\phi_5^{-1})^{*}(x) = \zeta_5^{-1} x$ under the left-action convention
$\sigma \cdot f = f \circ \sigma^{-1}$, so $x$ is an eigenvector with
eigenvalue $\zeta_5^{-1}$.

Eigenvalue on Bring: the cyclic permutation $\sigma(x_j) = x_{j+1}$
diagonalises on the Lagrange resolvents as $\sigma(w_k) = \zeta_5^{-k} w_k$
([discrete Fourier transform diagonalises $C_5$ on the Bring's surface](#prop:lagrange-resolvent-transform));
specialising to $k = 1$ gives $\sigma(w_1) = \zeta_5^{-1} w_1$.

Both $x$ and $w_1$ span their respective weight-$(-1)$ eigenspaces
(one-dimensional in each coordinate ring).  The linear map
$x \mapsto w_1$ is therefore a canonical $\mathbb{Z}_5$-equivariant
isomorphism of weight-$(-1)$ subspaces, and the extension to powers
$x^{k} \mapsto w_1^{\,k}$ carries weight $\zeta_5^{-k}$ on both sides,
hence is $\mathbb{Z}_5$-equivariant on the five-term cyclic isotypical
decomposition.  $\square$
