## Determining shells from an arbitrary Skein polynomial

Given a Skein polynomial $P(q) = \prod_i \hat{V}_i(q)$
([Skein polynomial](#prop:skein-polynomial-transfer-matrix)),
the orbital shell structure is extracted by:

1. **Identify the electron-nucleus generators** — these are
   the generators $\sigma_i$ where electron strands cross
   nuclear strands.

2. **Extract the transfer matrix** $M_i(q)$ at each such
   generator from the chain reduction.

3. **Diagonalize** $M_i = S \Lambda S^{-1}$ to find
   eigenvalues $\lambda_{\pm}^{(i)}$.

4. **Shell $n$** at generator $i$ is the $n$-th power:
   $\hat{V}_i(n) = z(S\Lambda^n S^{-1})_{11} + (S\Lambda^n S^{-1})_{21}$.

5. **Sub-shells** from the tensor product eigenvalue
   degeneracies for multi-electron atoms.

6. **Transition energies** from $\hat{V}(n+1) - \hat{V}(n)$
   via the Chebyshev recurrence.
