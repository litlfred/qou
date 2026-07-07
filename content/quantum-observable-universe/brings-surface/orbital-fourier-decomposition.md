Let $\varrho: S^1 \hookrightarrow \Sigma_4$ be the trefoil $T_{2,3}$ embedded in Bring's surface, and let $N = N_{\varrho/\Sigma_4}$ be the normal bundle. The four quantum numbers $(n, \ell, m, s)$ arise directly from the Fourier decomposition of sections $\sigma \in \Gamma(N)$.

At each point of the trefoil, $N_p \cong \mathbb{R}^2$. Let $\varTheta \in [0, 2\pi)$ parametrise the trefoil. A section decomposes into orthogonal modes:
$$
  \sigma(\varTheta)
  = \sum_{\ell=0}^{\infty} \bigl(a_\ell \cos(\ell\varTheta) + b_\ell \sin(\ell\varTheta)\bigr) \hat{n}_1(\varTheta)
  + \sum_{\ell=0}^{\infty} \bigl(c_\ell \cos(\ell\varTheta) + d_\ell \sin(\ell\varTheta)\bigr) \hat{n}_2(\varTheta)
$$
where $\hat{n}_1, \hat{n}_2$ form an orthonormal frame for $N$.

**(1) Principal quantum number $n$.**
The total twist $k = 2(n-1)$ constraints the total energy $E_n = -E_{\mathrm{ion}}/n^2$. The twist equates to the $L^2$ norm-squared of $\sigma$. At fixed $k$, only finitely many Fourier modes can be nonzero.

**(2) Angular momentum quantum number $\ell$.**
The $\ell$-th Fourier mode acts as a resonance frequency of the trefoil's transverse vibration, carrying eigenvalue $\lambda_\ell = [\ell]_q [\ell + 1]_q$ under the $q$-Laplacian. The $q$-deformation shifts the eigenvalues by order $\alpha^2$, producing fine-structure splitting between sub-shells at the same $n$.

**(3) Magnetic quantum number $m$.**
The $\mathrm{SO}(3)$ rotation group acts on $\mathbb{R}^3$ and the normal-bundle sections. Mode-$\ell$ sections transform as the irreducible representation $V_\ell$ of $\mathrm{SO}(3)$. The magnetic quantum number $m = -\ell, \ldots, +\ell$ labels the weight spaces relative to the Reeb axis.

**(4) Spin quantum number $s$.**
The fiber adjoint involution acts on the normal bundle by exchanging the two orientations of the Hopf link between electron and proton. This involution $\sigma \mapsto -\sigma$ splits each orbital $(n, \ell, m)$ into two eigenspaces ($s = \pm 1/2$), doubling the orbital count to $2n^2$ states per shell.

| Quantum number | Fourier origin | Representation |
|:-:|---|---|
| $n$ | Total framing twist $k = 2(n-1)$ | Energy shell |
| $\ell$ | Fourier mode on $S^1$ | $\mathrm{SO}(3)$ irreducible $V_\ell$ |
| $m$ | Weight in $V_\ell$ (Reeb projection) | Spherical harmonic $Y_\ell^m$ |
| $s$ | Fiber adjoint involution eigenvalue | Spin $\pm 1/2$ |
