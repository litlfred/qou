The preceding results establish that the Frobenius eigenvalues satisfy
$|\alpha_i| = q^{1/2}$ unconditionally.  The question is:
*why* does the geometry force this? The answer traces back through the
entire chain of categorical machinery to a single geometric constraint.

**Step 1: Global coherence demands vanishing Chern classes.**
The multiplicative integral \cite{yekutieli2015} computes a path-ordered product
of holonomy matrices along the Reeb flow. For this product to be
globally well-defined --- yielding the same answer regardless of how
one triangulates the bounding surface --- the connection on the
adjoint bundle $\mathrm{Ad}(A)$ must be *flat*. This is a standard
consequence of the nonabelian Stokes theorem
([nonabelian Stokes](#rem:yekutieli-stokes)): if the curvature
$F_\nabla$ of the connection were nonzero, different triangulations
of a surface $\Sigma$ bounding the same curve would produce different
path-ordered products, because the surface integral
$\prod^{\to}_\Sigma \exp(F_\nabla)$ would contribute a
triangulation-dependent factor. Consistency therefore requires
$F_\nabla = 0$, which in cohomological terms is the measurability
condition $c_1(\mathrm{Ad}(A)) = 0$, $c_2(\mathrm{Ad}(A)) = 0$.
The first Chern class vanishing ensures path-independence of the
parallel transport; the second ensures the absence of topological
phases around non-contractible cycles.

**Step 2: Flatness forces unitarity.**
A flat connection on a vector bundle over a compact base has holonomy
valued in the structure group of that bundle. The adjoint bundle
$\mathrm{Ad}(A)$ inherits a *Hermitian structure* from the Frobenius
form $\lambda \colon A \to \mathbf{1}$: the pairing
$\langle x, y \rangle = \lambda(\mu(x \otimes S(y)))$ (where $S$ is
the antipode) defines a positive-definite inner product preserved by
the adjoint action. Since the connection is flat and the bundle carries
this Hermitian structure, the holonomy around any closed curve ---
including the prime orbits of the Reeb flow --- must lie in the
*unitary group* $\mathrm{U}(V)$ rather than the full
$\mathrm{GL}(V)$.

On the algebraic-geometric side, this translates directly to the
Castelnuovo--Severi argument
([Hasse--Weil bound](#thm:hasse-weil-bound)): the Frobenius
endomorphism $\varphi$ acts on $H^1(\mathcal{B}, \mathbb{Q}_\ell)$
as a unitary operator with respect to the Weil pairing (which is the
$\ell$-adic avatar of the Frobenius Hermitian structure). The
Castelnuovo--Severi inequality on the self-product
$\mathcal{B} \times \mathcal{B}$ then gives $|\alpha_i|^2 = q$ for
all 8 eigenvalues, i.e. $|\alpha_i| = q^{1/2}$.

**Step 3: Unitarity locks the zeros to the critical line.**
The eigenvalues $\alpha_i$ of the Frobenius endomorphism are the
reciprocal roots of the local zeta function $Z_q(t)$. The condition
$|\alpha_i| = q^{1/2}$ translates, under the standard change of
variable $t = q^{-s}$, to the statement that all zeros of $Z_q(s)$
satisfy $\mathrm{Re}(s) = 1/2$: if $\alpha_i = q^{1/2} e^{i\phi}$
then $q^{-s} = \alpha_i^{-1}$ gives $s = 1/2 - i\phi/\ln q$, which
has real part exactly $1/2$
([spectral half-line](#cor:spectral-half-line)). This is the Riemann
hypothesis for Bring's curve over $\mathbb{F}_q$ --- an
*unconditional theorem*, not a conjecture.

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
construction --- the critical-line property is visibly forced by the
compactness of the gauge group.

**The physical picture.** The non-trivial zeros of the zeta function
are eigenvalues of the Reeb flow, and each eigenvalue corresponds to a
fundamental oscillation mode of the substrate. The unitary constraint
means that no mode grows or decays: the substrate is in a *critical
phase* of exact balance between order and disorder
([unitary stability](#rem:unitary-stability)). If any eigenvalue
drifted off the critical line, the holonomy around the corresponding
prime orbit would cease to be unitary, the Chern classes would become
nonzero, and the multiplicative integral would develop an anomaly --- the
global coherence of the counting mechanism would break down.

In summary: the prime distribution cannot have wild, unconstrained
error terms because *the geometry does not permit it*. The vanishing of
Chern classes $\to$ flatness of the connection $\to$ unitarity of the
holonomy $\to$ confinement of zeros to $\mathrm{Re}(s) = 1/2$. This
chain of implications is the geometric hammer that enforces the quantum
Riemann hypothesis at the $q$-scale. Whether this local rigidity
survives the classical limit $q \to 1$ is precisely the content of the
classical Riemann hypothesis
([Conjecture](#conj:classical-riemann-hypothesis)).
