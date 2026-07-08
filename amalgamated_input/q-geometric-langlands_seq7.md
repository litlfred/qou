<!-- FILE_START: weil-bound-intro.md -->
The explicit formula links the distribution of defects to the spectrum of the Reeb flow. This spectrum must be stable. If the Reeb eigenvalues stray from the critical line, the oscillatory terms grow without bound, triggering catastrophic accumulation or rarefaction of defects.

The algebraic geometry of Bring's curve unconditionally constrains the eigenvalues to the critical line $\mathrm{Re}(\rho) = 1/2$. This constitutes the Weil bound applied directly to the spectral geometry of the substrate.
<!-- FILE_END: weil-bound-intro.md -->

<!-- FILE_START: local-q-zeta-function.md -->
We define the :defterm[local $q$-zeta function]{#local-q-zeta-function} of Bring's curve $\mathcal{B}$ as the generating function for point counts over finite extensions:

$$
Z(\mathcal{B}, t) = \exp\!\left(\sum_{n=1}^{\infty} \frac{|\mathcal{B}(\mathbb{F}_{q^n})|}{n} t^n\right) = \frac{P(t)}{(1-t)(1-qt)},
$$

where $P(t) = \prod_{i=1}^{2g}(1 - \alpha_i t)$ is the characteristic polynomial of the Frobenius endomorphism $\mathrm{Fr}_q : H^1(\mathcal{B}) \to H^1(\mathcal{B})$. Because $g = 4$ for Bring's curve, this polynomial has degree $2g = 8$. The roots $\alpha_1, \ldots, \alpha_8$ are the fundamental eigenvalues of the Frobenius action on the first étale cohomology. The denominator factors $(1-t)$ and $(1-qt)$ correspond to $H^0$ and $H^2$ respectively.
<!-- FILE_END: local-q-zeta-function.md -->

<!-- FILE_START: hasse-weil-bound.md -->
The eight fundamental eigenvalues of the Frobenius endomorphism satisfy the Hasse--Weil bound:

$$
|\alpha_i| = q^{1/2} \qquad \text{for all } i = 1, \ldots, 8.
$$
<!-- FILE_END: hasse-weil-bound.md -->

<!-- FILE_START: spectral-half-line.md -->
The spectral coordinate mapping $\alpha_i = q^{\rho_i}$ translates the Hasse--Weil bound into a restriction on the Reeb spectrum. We have $|\alpha_i| = q^{1/2}$ and $|q^{\rho_i}| = q^{\mathrm{Re}(\rho_i)}$. Equating exponents yields:

$$
\mathrm{Re}(\rho_i) = \frac{1}{2} \qquad \text{for all } \rho_i \in \mathrm{Spec}(\xi_q), \quad i = 1, \ldots, 8.
$$

All 8 fundamental modes of the Reeb spectrum lie exactly on the critical line $\mathrm{Re}(\rho) = 1/2$. This formulates the finite-field Riemann hypothesis in the language of the substrate. The spectral oscillations in the explicit formula balance perfectly. Each mode contributes fluctuations of amplitude $|X^{\rho_i}/[\rho_i]_q| = X^{1/2}/|[\rho_i]_q|$, ensuring exact square-root cancellation.
<!-- FILE_END: spectral-half-line.md -->

<!-- FILE_START: unitary-stability.md -->
The confinement of all Reeb eigenvalues to the critical line $\mathrm{Re}(\rho) = 1/2$ implies that the observer drift is unitarily stable. No eigenmode grows or decays exponentially.

The oscillatory terms in the explicit formula satisfy:

$$
\left|\frac{X^{\rho_i}}{[\rho_i]_q}\right| = \frac{X^{1/2}}{|[\rho_i]_q|}
$$

for all $X > 0$. This forces three physical outcomes:

1. **No collapse:** Defects do not cluster, which would require $\mathrm{Re}(\rho) > 1/2$ for some mode.
2. **No rarefaction:** Defects do not disperse, which would require $\mathrm{Re}(\rho) < 1/2$.
3. **Square-root fluctuations:** The deviation from the average defect density is bounded by $O(X^{1/2})$, the minimal fluctuation consistent with the uncertainty principle.

The substrate therefore occupies a critical phase, balanced perfectly between order and disorder. The Reeb flow preserves the $q$-volume form exactly. This provides the algebraic foundation for the stability of the quantum observable universe at the $q$-scale.
<!-- FILE_END: unitary-stability.md -->

<!-- FILE_START: geometric-rh-exposition.md -->
The Frobenius eigenvalues must satisfy $|\alpha_i| = q^{1/2}$. We establish the geometric origin of this constraint.

**Step 1: Global coherence demands vanishing Chern classes.**
The multiplicative integral computes a path-ordered product of holonomy matrices along the Reeb flow. This product must be globally well-defined. The nonabelian Stokes theorem dictates that if the curvature $F_\nabla$ of the connection on the adjoint bundle $\mathrm{Ad}(A)$ were nonzero, different triangulations of a bounding surface would yield different path-ordered products. Consistency requires $F_\nabla = 0$, implying the Chern classes vanish: $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$. The first Chern class controls path-independence; the second precludes topological phases around non-contractible cycles.

**Step 2: Flatness forces unitarity.**
A flat connection over a compact base has holonomy in the structure group. The adjoint bundle $\mathrm{Ad}(A)$ inherits a Hermitian structure from the Frobenius form $\lambda \colon A \to \mathbf{1}$. The pairing $\langle x, y \rangle = \lambda(\mu(x \otimes S(y)))$ defines a positive-definite inner product preserved by the adjoint action. Because the connection is flat and the bundle carries this Hermitian structure, the holonomy around any closed curve lies in the unitary group $\mathrm{U}(V)$ rather than $\mathrm{GL}(V)$.

Algebraically, this corresponds to the Castelnuovo--Severi argument. The Frobenius endomorphism $\varphi$ acts on $H^1(\mathcal{B}, \mathbb{Q}_\ell)$ as a unitary operator with respect to the Weil pairing. The Castelnuovo--Severi inequality on $\mathcal{B} \times \mathcal{B}$ yields $|\alpha_i|^2 = q$ for all eight eigenvalues.

**Step 3: Unitarity locks the zeros to the critical line.**
The eigenvalues $\alpha_i$ of the Frobenius endomorphism are the reciprocal roots of the local zeta function $Z_q(t)$. Under $t = q^{-s}$, the condition $|\alpha_i| = q^{1/2}$ forces all zeros of $Z_q(s)$ to satisfy $\mathrm{Re}(s) = 1/2$. If $\alpha_i = q^{1/2} e^{i\phi}$, then $q^{-s} = \alpha_i^{-1}$ gives $s = 1/2 - i\phi/\ln q$. This establishes the Riemann hypothesis for Bring's curve over $\mathbb{F}_q$.

In the archimedean realisation $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}(2))$, the adjoint representation $\mathrm{Ad}(A)$ is the 3-dimensional real representation on $\mathfrak{su}(2)$. The Frobenius form $\lambda = \mathrm{tr}$ provides the Killing inner product. Flatness requires the $\mathrm{SU}(2)$ connection to have zero curvature. Because $\mathrm{SU}(2)$ is compact, flat holonomy lies in $\mathrm{U}(1) \subset \mathrm{SU}(2)$, yielding a pure phase $e^{i\phi}$. The Frobenius eigenvalues become $\alpha = q^{1/2} e^{i\phi}$, satisfying $|\alpha| = q^{1/2}$. Compactness of the gauge group directly forces the critical-line property.

Non-trivial zeros of the zeta function represent eigenvalues of the Reeb flow. Each eigenvalue defines a fundamental oscillation mode of the substrate. The unitary constraint ensures no mode grows or decays. If an eigenvalue drifted off the critical line, holonomy around the prime orbit would cease to be unitary, the Chern classes would become nonzero, and the multiplicative integral would develop an anomaly. Global coherence would fail.

Prime distribution cannot contain unconstrained error terms because the geometry forbids it. Vanishing Chern classes imply flat connections, flat connections imply unitary holonomy, and unitary holonomy confines zeros to $\mathrm{Re}(s) = 1/2$. This geometric chain enforces the quantum Riemann hypothesis at the $q$-scale. 
<!-- FILE_END: geometric-rh-exposition.md -->

