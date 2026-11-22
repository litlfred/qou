**Eigenvalue properties:**
- $\lambda_+ \cdot \lambda_- = \det T_{\gamma e} = -1$ (thus $\lambda_- = -1/\lambda_+$)
- $\lambda_+ + \lambda_- = \mathrm{tr} T_{\gamma e} = q - q^{-1}$
- $\lambda_+ > 1 > |\lambda_-|$ for all $q > 1$
- At $q = 1$: $\lambda_+ = 1$, $\lambda_- = -1$ (degenerate)

## Numerical shell energies

| $n$ | $\lambda_+^n$ | $\hat{V}(n)$ | $E_n / E_1$ | Rydberg $1/n^2$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 1.107 | 1.052 | 1.000 | 1.000 |
| 2 | 1.226 | 1.117 | 1.062 | 0.250 |
| 3 | 1.358 | 1.197 | 1.138 | 0.111 |
| 4 | 1.504 | 1.296 | 1.232 | 0.063 |
| 5 | 1.665 | 1.418 | 1.348 | 0.040 |

The binding energy $\mathfrak{E}_{\mathrm{bind}}(n) = E_\infty - E_n \propto 1/\lambda_+^n$ yields the characteristic Rydberg ratios for low $n$.

## Sub-shell structure from multi-electron tensor products

For atoms with $Z$ electrons, the transfer matrix at each electron-nucleus generator is a **tensor product**:

$$
  T_{\mathrm{total}}^{(i)}
  = 
  \bigotimes_{e=1}^{Z} T_{\gamma e}^{(e, i)}
$$

The eigenvalues of the tensor product are **products** of individual eigenvalues: $\lambda_{\pm}^{(1)} \cdot \lambda_{\pm}^{(2)} \cdots$. The degeneracy structure of these products determines the sub-shells:

- **$s$ orbital** ($\ell = 0$): Both electrons occupy the same eigenstate $\lambda_+^n$ (no angular node). Capacity: $2$ (spin up/down).
- **$p$ orbital** ($\ell = 1$): One electron occupies $\lambda_+$, one occupies $\lambda_-$ (one angular node from the alternating eigenvalue). Capacity: $6$ ($m = -1, 0, +1$ times spin).
- **$d$ orbital** ($\ell = 2$): Two alternating eigenvalues (two angular nodes). Capacity: $10$.

The angular momentum quantum number $\ell$ counts how many electrons at shell $n$ occupy the **sub-dominant** eigenvalue $\lambda_-$. The magnetic quantum number $m$ projects the eigenvalue pattern onto the Reeb axis.

The capacity per sub-shell is $2(2\ell + 1)$. The capacity per shell is $\sum_{\ell=0}^{n-1} 2(2\ell+1) = 2n^2$.

## Determining shells from an arbitrary Skein polynomial

Given a Skein polynomial $P(q) = \prod_i \hat{V}_i(q)$ ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)), extract the orbital shell structure via:

1. **Identify the electron-nucleus generators.** These are the generators $\sigma_i$ where electron strands cross nuclear strands.
2. **Extract the transfer matrix** $M_i(q)$ at each such generator from the chain reduction.
3. **Diagonalize** $M_i = S \Lambda S^{-1}$ to find the eigenvalues $\lambda_{\pm}^{(i)}$.
4. **Shell $n$** at generator $i$ is the $n$-th power: $\hat{V}_i(n) = z(S\Lambda^n S^{-1})_{11} + (S\Lambda^n S^{-1})_{21}$.
5. **Sub-shells** emerge from the tensor product eigenvalue degeneracies for multi-electron atoms.
6. **Transition energies** follow from $\hat{V}(n+1) - \hat{V}(n)$ via the Chebyshev recurrence.
