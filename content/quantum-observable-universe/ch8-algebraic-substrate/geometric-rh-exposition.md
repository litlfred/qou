The preceding results establish that the Frobenius eigenvalues satisfy
$|\alpha_i| = q^{1/2}$ unconditionally, but the reader may wonder:
*why* does the geometry force this? The answer traces back through the
entire chain of categorical machinery to a single geometric constraint.

**Step 1: Global coherence demands vanishing Chern classes.**
For the Yekutieli multiplicative integral to be globally well-defined
--- that is, for the path-ordered product of holonomy matrices to yield
a consistent answer regardless of how one triangulates the bounding
surface --- the connection on $\mathrm{Ad}(A)$ must be *flat*. In
cohomological terms, this is precisely the measurability condition
$c_1(\mathrm{Ad}(A)) = 0$, $c_2(\mathrm{Ad}(A)) = 0$
([nonabelian Stokes](#rem:yekutieli-stokes)). The first Chern class
vanishing ensures path-independence of the parallel transport; the
second ensures the absence of topological phases around
non-contractible cycles.

**Step 2: Flatness forces unitarity.**
A flat connection on a compact space has holonomy valued in a compact
group. Since the adjoint bundle $\mathrm{Ad}(A)$ is self-dual (by the
Frobenius compatibility) and the connection is flat (by the Chern class
vanishing), the holonomy around any closed curve --- including the
prime orbits of the Reeb flow --- must lie in a *unitary* subgroup
of $\mathrm{GL}(V)$. Concretely, the Frobenius endomorphism $\varphi$
acts on the $H^1$ of Bring's curve $\mathcal{B}$ as a unitary
operator with respect to the Weil pairing: the Castelnuovo--Severi
inequality then gives $|\alpha_i|^2 = q$ for all eigenvalues, which is
exactly $|\alpha_i| = q^{1/2}$.

**Step 3: Unitarity locks the zeros to the critical line.**
The eigenvalues $\alpha_i$ of the Frobenius endomorphism are the
reciprocal roots of the local zeta function $Z_q(t)$. The condition
$|\alpha_i| = q^{1/2}$ translates, under the change of variable
$t = q^{-s}$, to the statement that all zeros of $Z_q(s)$ satisfy
$\mathrm{Re}(s) = 1/2$
([spectral half-line](#prop:spectral-half-line)). This is the Riemann
hypothesis for Bring's curve over $\mathbb{F}_q$ --- an
*unconditional theorem*, not a conjecture.

**The physical picture.** The non-trivial zeros of the zeta function
are eigenvalues of the Reeb flow, and each eigenvalue corresponds to a
fundamental oscillation mode of the substrate. The unitary constraint
means that no mode grows or decays: the substrate is in a *critical
phase* of exact balance between order and disorder
([unitary stability](#prop:unitary-stability)). If any eigenvalue
drifted off the critical line, the holonomy around the corresponding
prime orbit would cease to be unitary, the Chern classes would become
nonzero, and the Yekutieli integral would develop an anomaly --- the
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
