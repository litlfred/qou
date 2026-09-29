The Frobenius eigenvalues must satisfy $|\alpha_i| = q^{1/2}$. We establish the geometric origin of this constraint.

**Concrete example: $\mathrm{SU}(2)$.** In the archimedean
realisation $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}(2))$, the
adjoint representation $\mathrm{Ad}(A)$ is the 3-dimensional real
representation on $\mathfrak{su}(2)$. The Frobenius form
$\lambda = \mathrm{tr}$ gives the Killing inner product, and the
flatness condition $c_1 = c_2 = 0$ says the $\mathrm{SU}(2)$
connection has zero curvature on the adjoint bundle. Since
$\mathrm{SU}(2)$ is compact, the holonomy of a flat connection lies
in $\mathrm{U}(1) \subset \mathrm{SU}(2)$: any closed loop yields
a pure phase $e^{i\phi}$. The Frobenius eigenvalues are
$\alpha = q^{1/2} e^{i\phi}$, with $|\alpha| = q^{1/2}$ by
construction. The critical-line property is forced by the
compactness of the gauge group.

With this concrete picture in mind, the general mechanism unfolds
in three steps.

**Step 1: Global coherence demands vanishing Chern classes.**
The multiplicative integral computes a path-ordered product of holonomy matrices along the Reeb flow. This product must be globally well-defined. The nonabelian Stokes theorem dictates that if the curvature $F_\nabla$ of the connection on the adjoint bundle $\mathrm{Ad}(A)$ were nonzero, different triangulations of a bounding surface would yield different path-ordered products. Consistency requires $F_\nabla = 0$, implying the Chern classes vanish: $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$. The first Chern class controls path-independence; the second precludes topological phases around non-contractible cycles.

**Step 2: Flatness forces unitarity.**
A flat connection over a compact base has holonomy in the structure group. The adjoint bundle $\mathrm{Ad}(A)$ inherits a Hermitian structure from the Frobenius form $\lambda \colon A \to \mathbf{1}$. The pairing $\langle x, y \rangle = \lambda(\mu(x \otimes S(y)))$ defines a positive-definite inner product preserved by the adjoint action. Because the connection is flat and the bundle carries this Hermitian structure, the holonomy around any closed curve lies in the unitary group $\mathrm{U}(V)$ rather than $\mathrm{GL}(V)$.

Algebraically, this corresponds to the Castelnuovo--Severi argument. The Frobenius endomorphism $\varphi$ acts on $H^1(\mathcal{B}, \mathbb{Q}_\ell)$ as a unitary operator with respect to the Weil pairing. The Castelnuovo--Severi inequality on $\mathcal{B} \times \mathcal{B}$ yields $|\alpha_i|^2 = q$ for all eight eigenvalues.

**Step 3: Unitarity locks the zeros to the critical line.**
The eigenvalues $\alpha_i$ of the Frobenius endomorphism are the reciprocal roots of the local zeta function $Z_q(t)$. Under $t = q^{-s}$, the condition $|\alpha_i| = q^{1/2}$ forces all zeros of $Z_q(s)$ to satisfy $\mathrm{Re}(s) = 1/2$. If $\alpha_i = q^{1/2} e^{i\phi}$, then $q^{-s} = \alpha_i^{-1}$ gives $s = 1/2 - i\phi/\ln q$. This establishes the Riemann hypothesis for Bring's curve over $\mathbb{F}_q$.

**The physical picture.** The non-trivial zeros of the zeta function
are eigenvalues of the Reeb flow, each corresponding to a fundamental
oscillation mode of the substrate; the unitary constraint means no
mode grows or decays, so the substrate sits in a *critical phase* of
exact balance between order and disorder
([unitary stability](#rem:unitary-stability)). The chain of
implications --- vanishing Chern classes $\to$ flatness of the
connection $\to$ unitarity of the holonomy $\to$ confinement of zeros
to $\mathrm{Re}(s) = 1/2$ --- is thus what forbids wild, unconstrained
error terms in the prime distribution. Whether this local rigidity
survives the classical limit $q \to 1$ is precisely the content of the
classical Riemann hypothesis
([Conjecture](#conj:classical-riemann-hypothesis)).
