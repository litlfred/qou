## Sub-shell structure from multi-electron tensor products

For atoms with $Z$ electrons, the transfer matrix at each
electron-nucleus generator is a **tensor product**:

$$
  T_{\mathrm{total}}^{(i)}
  = 
  \bigotimes_{e=1}^{Z} T_{\gamma e}^{(e, i)}
$$

The eigenvalues of the tensor product are **products** of
individual eigenvalues: $\lambda_{\pm}^{(1)} \cdot \lambda_{\pm}^{(2)} \cdots$.  The degeneracy structure of
these products determines the sub-shells:

- **$s$ orbital** ($\ell = 0$): both electrons in the same
  eigenstate $\lambda_+^n$ (no angular node).
  Capacity: $2$ (spin up/down).
- **$p$ orbital** ($\ell = 1$): one electron in $\lambda_+$,
  one in $\lambda_-$ (one angular node from the alternating
  eigenvalue).  Capacity: $6$ ($m = -1, 0, +1$ x spin).
- **$d$ orbital** ($\ell = 2$): two alternating eigenvalues
  (two angular nodes).  Capacity: $10$.

The angular momentum quantum number $\ell$ counts how many
electrons at shell $n$ are in the **sub-dominant** eigenvalue
$\lambda_-$.  The magnetic quantum number $m$ is the projection
of the eigenvalue pattern onto the Reeb axis.

The capacity per sub-shell: $2(2\ell + 1)$.  Per shell:
$\sum_{\ell=0}^{n-1} 2(2\ell+1) = 2n^2$.
