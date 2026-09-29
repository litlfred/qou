Let $T_{2,3} \hookrightarrow \Sigma_4$ be the trefoil embedded in Bring's surface, and let $N = N_{T_{2,3}/\Sigma_4}$ be its normal bundle. At shell $n$ (framing twist $k = 2(n-1)$ relative to the Seifert framing), the space of orbital states is:
$$
  \mathcal{O}_n
  = 
  \bigl\{
    \sigma \in \Gamma(N)  : 
    \mathrm{tw}(\sigma) = k, \quad
    \Delta_{T}\sigma = \lambda\sigma, \quad
    \lambda \leq \lambda_{n-1}
  \bigr\}
$$
where $\mathrm{tw}(\sigma)$ is the total twist, $\Delta_T$ is the ambient-induced Laplacian on $T_{2,3}$, and $\lambda_\ell$ is the $\ell$-th eigenvalue. This orbital space has dimension $\dim \mathcal{O}_n = n^2$.

The normal bundle $N$ is a rank-$2$ real vector bundle over $T_{2,3} \cong S^1$. A section $\sigma \in \Gamma(N)$ describes a transverse displacement of the trefoil. The total twist $\mathrm{tw}(\sigma) = k$ measures the self-linking number of the displaced curve relative to the Seifert surface, representing the global R-I count.

The $q$-Laplacian $\Delta_q$ on $T_{2,3} \cong S^1$ has eigenvalues $\lambda_\ell =  [\ell]_q  [\ell + 1]_q$ for $\ell = 0, 1, 2, \ldots$. Each eigenvalue $\lambda_\ell$ for $\ell \geq 1$ has multiplicity $2$.

At each point of the trefoil, the transverse displacement has two independent normal directions in the $3$-dimensional ambient space. A section $\sigma$ with Fourier mode $\ell$ and direction $\hat{n}$ parametrizes the same space as a spherical harmonic $Y_\ell^m$ on the unit sphere surrounding the proton. This identification holds because the trefoil orbits the proton, sweeping out a sphere. The magnetic quantum number $m = -\ell, \ldots, +\ell$ labels the $2\ell + 1$ orientations of the mode relative to the Reeb axis.

At shell $n$, the energy constraint admits modes $\ell = 0, 1, \ldots, n-1$. For each mode $\ell$, the section space transforms as the irreducible $\mathrm{SO}(3)$ representation $V_\ell$ of dimension $2\ell + 1$. The total orbital dimension is:
$$
  \dim \mathcal{O}_n
  = \sum_{\ell=0}^{n-1} \dim V_\ell
  = \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  n^2.
$$
The energy of mode $\ell$ at shell $n$ is $E_\ell = \frac{[\ell]_q  [\ell + 1]_q}{[n]_q^2} \cdot E_{\mathrm{ion}}$. The mode fits within shell $n$ exactly when $\ell \leq n - 1$.
