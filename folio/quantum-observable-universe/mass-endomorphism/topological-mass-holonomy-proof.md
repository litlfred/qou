**Proof.**
The projection $\hat{\tau}_n(\alpha)$ lies in
$\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\hat{\tau}_n$, which is
isomorphic to the level-$n$ section algebra via the ascent embedding
$\ell_n$ ([:refterm[descent]{#descent} involution](#def:descent-involution)).  The surface
$\Sigma$ with $\partial\Sigma = \varrho$ decomposes under the topological
blow-up as $\Sigma = \Sigma_0 \cup \bigcup_{i=1}^N D_i$, where
$\Sigma_0$ is a disc spanning the unknot core $\varrho_0$ and each
$D_i$ is the disc (exceptional divisor) inserted at the $i$-th blow-up.
On $\Sigma_0$ the transient component vanishes
($\alpha - \hat{\tau}_n(\alpha) = 0$ on the unknot complement, since $\varrho_0$
has trivial topology and all sections there factor through level $n$).
Hence:

$$
  \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha)
  = 
  \mathrm{MI}\!\!\int_{\Sigma_0} \alpha
  = 
  \mathrm{Hol}_{\nabla_A}\!\bigl(\varrho_0; \mathfrak{G}\bigr),
$$

where the second equality is the nonabelian Stokes
theorem \cite{yekutieli2015} applied to the disc $\Sigma_0$.  $\square$
