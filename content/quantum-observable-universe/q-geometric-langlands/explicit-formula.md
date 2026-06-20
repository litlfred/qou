*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The Tannaka--Krein self-duality manifests as a discrete Fourier transform
over the spectral-geometric space. The explicit formula equates the
geometric sum (over defects) to the spectral trace (over Reeb eigenvalues):

$$
\psi_q(X) = X - \sum_{\rho \in \mathrm{Spec}(\xi_q)} \frac{X^\rho}{[\rho]_q} - \ln_q(2\pi\Omega_q) - \frac{1}{2}\ln_q(1 - X^{-2})
$$

where $[\rho]_q = \frac{q^\rho - q^{-\rho}}{q - q^{-1}}$ is the
$q$-integer, $\Omega_q$ is the Reeb period, and $\ln_q$ is the
$q$-logarithm.

The leading term $X$ represents the smooth background growth of defect
density. The oscillatory sum over $\mathrm{Spec}(\xi_q)$ encodes the
fluctuations due to the Reeb eigenvalues — each eigenvalue $\rho$
contributes a wave of amplitude $X^\rho / [\rho]_q$. The constant and tail
terms arise from the trivial eigenvalues and the symmetry of the functional
equation. This formula is the non-commutative analog of the classical
explicit formula of prime number theory \cite{reshetikhin1991}.
