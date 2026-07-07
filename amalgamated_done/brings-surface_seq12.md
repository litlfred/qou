<!-- FILE_START: cohomological-defect-intro.md -->
Where does matter arise? The Frobenius structure of $A$ is globally non-degenerate, but it can fail locally. Matter emerges where a non-degenerate Levi form obstructs the Frobenius pairing. The unit particle is the fundamental cohomological defect, a generator of the local cohomology at the singular point $z = 1$.
<!-- FILE_END: cohomological-defect-intro.md -->

<!-- FILE_START: levi-form-defect.md -->
Matter is defined as the failure of the Frobenius structure. At a point $p$ in the spectral fiber, the Levi form $\mathcal{L}_p : T_p^{1,0}A \times T_p^{0,1}A \to \mathbb{C}$ measures the non-degeneracy of the contact structure. When $\mathcal{L}_p \neq 0$, the Frobenius form $\lambda$ cannot extend smoothly through $p$, creating a topological defect. The set of such points forms the matter locus $\mathrm{Sing}(\lambda) \subset \mathrm{Spec}(A)$.
<!-- FILE_END: levi-form-defect.md -->

<!-- FILE_START: maximal-ideal-defect.md -->
The maximal ideal $\mathfrak{m}_1 \subset A$ corresponds to the coordinate $z = 1$ in the spectral fiber, defined as the kernel of the evaluation homomorphism $\mathrm{ev}_1 : A \to k$. The point $z = 1$ is the fixed point of the antipode $S$, marking the unique location where the Hopf and Frobenius structures interact maximally. The local ring $A_{\mathfrak{m}_1}$ captures the algebraic behavior near this singularity.
<!-- FILE_END: maximal-ideal-defect.md -->

<!-- FILE_START: local-cohomology-group.md -->
The local cohomology group $H^1_{\mathfrak{m}_1}(A) = R^1\Gamma_{\mathfrak{m}_1}(A)$ measures the algebraic obstruction to extending sections across the defect at $z = 1$. In this non-commutative setting, the derived category framework generalizes the commutative concept of principal parts supported at the singularity.
<!-- FILE_END: local-cohomology-group.md -->

<!-- FILE_START: unit-particle-state.md -->
The unit particle state $\mathrm{Li}_q(z)$ is the fundamental generator of $H^1_{\mathfrak{m}_1}(A)$. It uniquely satisfies the $q$-differential equation:
$$
  d_q \mathrm{Li}_q(z) = \frac{1}{\log_q z} dz
$$
where $\log_q z = (z^{\hbar_q} - 1)/\hbar_q$. In the classical limit $q \to 1$, this recovers the classical dilogarithm $\mathrm{Li}_2(z)$.
<!-- FILE_END: unit-particle-state.md -->

<!-- FILE_START: topological-charge-quantization.md -->
The topological charge of the unit particle is quantized. The algebraic residue at $z = 1$, computed via the observer trace $\Phi$, equals unity:
$$
  \mathrm{Res}_q(\omega, 1) = \Phi\bigl(\mathrm{Res}_{\xi}(\omega)\bigr) = 1
$$
This quantization serves as the algebraic counterpart of the Gauss--Bonnet theorem, following from the non-degeneracy of the Frobenius pairing and the periodicity of the Reeb derivation $\xi_q$.
<!-- FILE_END: topological-charge-quantization.md -->

<!-- FILE_START: defect-legendrian-knot.md -->
The unit particle defect is a Legendrian knot restricted to the $q$-torsion leaf $L_q$. Its support in the contact manifold $(A, \varTheta)$ satisfies $\varTheta\big|_{\mathrm{supp}(\mathrm{Li}_q)} = 0$.

Because $\varTheta$ vanishes, the defect is maximally tangent to the contact distribution. Since $\dim_{\mathbb{R}} L_q = 3$, Legendrian curves in $L_q$ are knots. The Legendrian condition ensures the defect carries no angular momentum transverse to the contact planes, consistent with a fundamental scalar particle.
<!-- FILE_END: defect-legendrian-knot.md -->
