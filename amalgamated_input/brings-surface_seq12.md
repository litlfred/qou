<!-- FILE_START: cohomological-defect-intro.md -->
Having established the self-dual algebraic substrate, we now ask:
where does matter arise? The Frobenius structure of $A$ is globally
non-degenerate, but it can fail locally. Matter emerges precisely at
the locus of this failure — where a non-degenerate Levi form obstructs
the Frobenius pairing. The unit particle is the fundamental
cohomological defect, a generator of the local cohomology at the
singular point $z = 1$.

The section proceeds from defect to particle.  The Levi-form defect
characterises the local obstruction; the maximal-ideal defect lifts
it to the categorical level via the local cohomology group; the
unit-particle state names the resulting generator; and the
topological-charge quantisation pins it as an integer-valued
invariant of the underlying Legendrian knot.  Together these blocks
make precise the slogan "matter = cohomological defect" and supply
the substrate-level prototype for the heavier particle states
constructed in the sections that follow.
<!-- FILE_END: cohomological-defect-intro.md -->

<!-- FILE_START: levi-form-defect.md -->
Define matter as the failure of the Frobenius structure. At a point
$p$ in the spectral fiber, the Levi form
$\mathcal{L}_p : T_p^{1,0}A \times T_p^{0,1}A \to \mathbb{C}$
measures the non-degeneracy of the contact structure. When
$\mathcal{L}_p \neq 0$, the Frobenius form $\lambda$ cannot extend
smoothly through $p$, creating a topological defect. The set of such
points forms the **matter locus**
$\mathrm{Sing}(\lambda) \subset \mathrm{Spec}(A)$.
<!-- FILE_END: levi-form-defect.md -->

<!-- FILE_START: maximal-ideal-defect.md -->
Define the **maximal ideal** $\mathfrak{m}_1 \subset A$ corresponding to
the coordinate $z = 1$ in the spectral fiber. This is the kernel of
the evaluation homomorphism $\mathrm{ev}_1 : A \to k$,
$f \mapsto f(1)$. The point $z = 1$ is distinguished by the Frobenius
structure: it is the fixed point of the antipode $S$, hence the unique
point where the Hopf and Frobenius structures interact maximally. The
local ring $A_{\mathfrak{m}_1}$ captures the algebraic behavior of
the substrate near this fundamental singularity.
<!-- FILE_END: maximal-ideal-defect.md -->

<!-- FILE_START: local-cohomology-group.md -->
Define the **local cohomology group** $H^1_{\mathfrak{m}_1}(A)$ as the
first right derived functor of the $\mathfrak{m}_1$-torsion functor
$\Gamma_{\mathfrak{m}_1}$:

$$
H^1_{\mathfrak{m}_1}(A) = R^1\Gamma_{\mathfrak{m}_1}(A)
$$

This group measures the algebraic obstruction to extending sections
across the defect at $z = 1$. In the commutative case,
$H^1_{\mathfrak{m}_1}(A) \cong A_{\mathfrak{m}_1}/A$ captures the
"principal parts" supported at the singularity. In our
non-commutative setting, the derived category framework of
\cite{yekutieli2010} provides the correct generalization.
<!-- FILE_END: local-cohomology-group.md -->

<!-- FILE_START: unit-particle-state.md -->
Define the **unit particle state** $\mathrm{Li}_q(z)$ as the fundamental
generator of $H^1_{\mathfrak{m}_1}(A)$. It is the unique (up to
scalar) element satisfying the $q$-differential equation:

$$
d_q \mathrm{Li}_q(z) = \frac{1}{\log_q z} dz
$$

where $d_q$ is the Jackson $q$-derivative and
$\log_q z = \frac{z^{\hbar_q} - 1}{\hbar_q}$ is the $q$-logarithm.
The notation $\mathrm{Li}_q$ reflects that in the classical limit
$q \to 1$, this recovers the classical dilogarithm
$\mathrm{Li}_2(z)$, the fundamental period integral of algebraic
geometry.
<!-- FILE_END: unit-particle-state.md -->

<!-- FILE_START: topological-charge-quantization.md -->
The topological charge of the unit particle is quantized. The
algebraic residue at $z = 1$, computed via the observer trace
$\Phi$, equals unity:

$$
\mathrm{Res}_q(\omega, 1) = \Phi\bigl(\mathrm{Res}_{\xi}(\omega)\bigr) = 1
$$

where $\omega$ is the canonical differential form on $A$ and
$\mathrm{Res}_{\xi}$ denotes the residue along the Reeb flow. This
result is the algebraic counterpart of the Gauss--Bonnet theorem:
the total "curvature" of the defect, as measured by the self-dual
pairing, is an integer. The quantization follows from the
non-degeneracy of the Frobenius pairing and the periodicity of the
Reeb derivation $\xi_q$.
<!-- FILE_END: topological-charge-quantization.md -->

<!-- FILE_START: defect-legendrian-knot.md -->
The unit particle defect is a Legendrian knot restricted to the
$q$-torsion leaf $L_q$ where the horizontal contact form $\varTheta$
vanishes. Precisely, the support of $\mathrm{Li}_q(z)$ in the
contact manifold $(A, \varTheta)$ satisfies:

$$
\varTheta\big|_{\mathrm{supp}(\mathrm{Li}_q)} = 0
$$

The vanishing of $\varTheta$ on the support makes the defect
maximally tangent to the contact distribution --- it is a
Legendrian submanifold. Since
$\dim_{\mathbb{R}} L_q = 3$, Legendrian curves in $L_q$ are knots,
and the unit particle inherits a knot type from its embedding in the
$q$-torsion leaf. The Legendrian condition ensures that the defect
carries no "angular momentum" transverse to the contact planes,
consistent with its interpretation as a fundamental scalar particle.
<!-- FILE_END: defect-legendrian-knot.md -->

