Causal fermion systems (CFS), developed by Felix Finster, Niky Kamran, and Marco Oppio \cite{finster2021}, Felix Finster, Maximilian Jokel, and Claudio F. Paganini \cite{finster2022}, and Felix Finster, Johannes Kleiner, and Claudio F. Paganini \cite{finster2024}, provide a parallel continuum unification programme in which spacetime points are finite-rank self-adjoint operators $x, y$ on a Hilbert space $\mathcal{H}$. Translating both frameworks into tracial non-commutative probability places their spectral functionals on a common footing.

## Structural agreements

1. **Common tracial comparison carrier.** While CFS acts natively on bounded finite-rank spinor operators in $\mathcal{B}(\mathcal{H})$, restricting to finite-dimensional normalized spectral traces embeds both operator algebras into finite type II$_1$ factors for direct comparison.
2. **Asymptotic free-probability universality class.** Under large-rank Plancherel scaling of Philippe Biane \cite{biane1998}, the tracial moments of both frameworks lie in the free-probability universality class.
3. **Common commutative-shadow data type.** The traceful Plancherel projection maps non-commutative algebraic data to a commutative spectrum measure.

## Structural differences

QOU evaluates the Frobenius Gram pairing $G(x, y) := \mathrm{tr}_M(x \cdot y)$, whereas the CFS causal action principle \cite{finster2021, finster2022, finster2024} evaluates symmetric functions of the absolute-value differences $|\lambda_i^{xy}| - |\lambda_j^{xy}|$ of the $2n$ non-trivial eigenvalues of the operator product $x y$.

This yields three functional mismatches:
- **Pointwise mismatch.** $G(1, 1) = 1$, whereas identical eigenvalue magnitudes give $\mathcal{L}_{\mathrm{CFS}}(1, 1) = 0$.
- **Integral mismatch.** $G$ is odd under $x \mapsto -x$, whereas $\mathcal{L}_{\mathrm{CFS}}$ depends on $|\lambda_i^{xy}|$ and is even.
- **Spectral-variance decomposition.** Expanding the normalized pairwise squared difference $\mathcal{L}_{\mathrm{CFS}}^{(\mathrm{norm})}(x, y) := \frac{1}{4n^2}\sum_{i,j=1}^{2n}\bigl(|\lambda_i^{xy}| - |\lambda_j^{xy}|\bigr)^2 = \frac{1}{2n}\sum_{i=1}^{2n}|\lambda_i^{xy}|^2 - \bigl(\frac{1}{2n}\sum_{i=1}^{2n}|\lambda_i^{xy}|\bigr)^2$ rewrites the CFS dispersion directly as $G_2(x, y) - \lVert x \cdot y\rVert_1^{\,2}$ in normalized Schatten moments.

## Unresolved numerical question

Whether the higher-moment spectral variance vanishes or crosses at $q_0 \approx 1.1100$ has not been established.

## Corollary for QOU

The QOU phenomena (knot topology, braid statistics) are pre-projection algebra data. They lie outside any commutative-shadow framework.
