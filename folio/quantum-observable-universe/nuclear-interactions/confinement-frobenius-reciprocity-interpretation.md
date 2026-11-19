## Discussion

This proposition provides the master formula for computing numerical predictions about a confined bound state of $H_n(q)$. It governs binding energies, form factors, axial couplings, and magnetic moments.

**Three distinct ingredients are required.**

1. **The Frobenius Gram inverse $G^{-1}$** (**convention D**: read on the quotient $H_n/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$, where the induced pairing is non-degenerate; on $H_n$ itself $\det G = 0$ exactly, the $(1^3)$ block being the radical)**.** The naïve Markov trace $\mathrm{tr}_M(O \cdot \rho(\beta_T))$ is not the physical expectation value of $O$. The Markov form is non-orthonormal on the NF basis, so dualisation requires the Gram inverse.
2. **The LP-active set $A^*(T)$.** Most of the $d = n!$ NF basis elements have zero shadow price ($y_i^* = 0$). Including them in the dual pairing pollutes the observable with off-shell contributions. Only the active channels carry physical weight.
3. **The shadow prices $u_i^* = y_i^*$.** By LP duality, the shadow price on channel $i$ is the marginal cost of saturating the Frobenius positivity constraint. These prices are exactly the weights that make $\langle O\rangle_T$ coincide with the physical expectation.

## Corollaries

- **Corollary (g_A as an instance).** The axial coupling $g_A = \langle \sigma_A\rangle_{\mathfrak{p}} / \langle \sigma_V\rangle_{\mathfrak{p}}$ of the proton bound state is the ratio of two instances of the master formula at the LP-active set $A^*(\mathcal{B}_3)$.
- **Corollary (raw conjugation traces are zero-information).** The pattern $\mathrm{tr}_M(\beta \cdot X \cdot \beta^{-1})$ is cyclically equal to $\mathrm{tr}_M(X)$ and independent of $\beta$. Evaluating physical expectation values therefore requires replacing the conjugation pattern with the master formula.

## Evaluation Protocol

The rigorous evaluation of the master formula requires:

1. **$G$, $G^{-1}$**: Evaluate the Frobenius Gram matrix and its inverse on the NF basis, restricted to the surviving two-row blocks (**convention D**: $G$ is singular on all of $H_n$, $\det G = 0$, so the inverse exists only on $H_n/\mathrm{rad} \cong \mathrm{TL}_n$).
2. **Active set and shadow prices**: Solve the operator-selection linear program to obtain $A^*$ and $u_i^* = y_i^*$.
3. **Observable coefficients $\langle O, b_j\rangle$**: Compute $\mathrm{tr}_M(O \cdot b_j)$ for each active $j$.
4. **Pair**: Compute $\langle O\rangle_T = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij} \langle O, b_j\rangle$, with the active set $A^*$ inside the non-degenerate quotient (**convention D**).
