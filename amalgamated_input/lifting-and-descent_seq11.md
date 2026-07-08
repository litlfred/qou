<!-- FILE_START: archimedean-lifting-intro.md -->
The preceding sections established lifting, descent, and mass over a generic ring $R$. This section explicitly restricts to $R = \mathbb{R}$. The brane tower geometrically realizes a sequence of smooth jet bundles $J^1 \mathcal{S}_n$, analytically reducing the categorical mass identity to a nonabelian multiplicative integral.

Smooth jet prolongation frames $J^1\mathcal{S}_n$ as the precise geometric carrier of $A_n$. The Yekutieli extension fixes the band $\mathcal{B} = \mathcal{O}_M^{\times}$. The smooth proof of the $\mathrm{QU} \Rightarrow \mathrm{QOU}$ specialisation identically instantiates the main theorem for $\mathrm{SU}_q(2)$ frame bundles. Nonabelian multiplicative integration structurally realizes the categorical mass identity as a physical non-commutativity invariant of the $\mathcal{S}$-vortex.

Two structural lemmas precisely support the mass programme. The smooth Euler characteristic stability rigorously verifies the $\chi(A_n)$ proposition. The defining boundary structure isolates the codimension and chirality data of the brane boundary. The central analytic consequence equates the quantum dilogarithm to the exact torsion volume of the localised Reeb flow.

The remainder establishes the categorical mass conjecture. The conjectural decomposition mathematically splits the mass integrand by descent involution. Subsequent lemmas securely isolate the eigenspaces, the unknot-core holonomy, the transient exceptional-divisor localisations, and their precise quantum dilogarithm evaluation. The mass-decomposition proof aggregates these mechanisms. The $\mathrm{SU}(2)$ example supplies the precise smooth test case guiding all downstream numerical predictions.
<!-- FILE_END: archimedean-lifting-intro.md -->

<!-- FILE_START: jet-prolongation-C.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ define an archimedean quantum observable universe ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) equipped with an instanton connection $A$ on the principal bundle $P$ and a metric $g$ on $\mathcal{S}$. We denote the total space of $\mathcal{S}$ by $\widetilde{M} = \mathcal{S}$. Let $P'$ define the frame bundle and $\mathcal{S}'$ define the bundle of orthonormal frames of the first jet bundle $J^1 \mathcal{S}$. The data $(A, g)$ uniquely determines a connection $A'$ on $P'$ such that $(\mathbf{C}, \tilde\varTheta, G, \mathcal{S}')$ structurally forms an archimedean quantum observable universe.
<!-- FILE_END: jet-prolongation-C.md -->

<!-- FILE_START: yekutieli-archimedean-band.md -->
In the archimedean realisation ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), the banding sheaf rigorously specializes to $\mathcal{B} = \mathcal{O}_M^{\times}$, the sheaf of invertible holomorphic functions on $M$.
<!-- FILE_END: yekutieli-archimedean-band.md -->

<!-- FILE_START: euler-char-stability-C.md -->
In the archimedean realisation, the Leray–Serre spectral sequence independently verifies the stability condition $\chi(A_{n+1}) = \chi(A_n)$.

By the explicit construction of the [recursive brane tower](#def:recursive-brane-tower), $\mathcal{S}_{n+1}$ mathematically acts as the bundle of orthonormal frames of the first jet bundle $J^1 \mathcal{S}_n$ ([jet prolongation](#prop:jet-prolongation)). The Euler characteristic of a fibre bundle $F \hookrightarrow \mathcal{S}_{n+1} \to \mathcal{S}_n$ unconditionally satisfies the multiplicativity formula:
$$
  \chi(\mathcal{S}_{n+1}) = \chi(\mathcal{S}_n) \cdot \chi(F),
$$
provided the fibre $F$ holds the homotopy type of a finite CW-complex and the base acts identically on $H^*(F; \mathbb{Q})$. In the explicit brane tower, the fibre acts as $\mathrm{SU}(2) \cong S^3$, yielding $\chi(S^3) = 0$. However, the relevant structure is not $\mathrm{SU}(2)$ itself but the *projectivised* frame bundle. Its typical fibre is $\mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$, which strictly gives $\chi(S^2) = 2$. Despite this, the Euler characteristic rigidly persists.

The Leray–Serre spectral sequence of $S^2 \hookrightarrow \mathcal{S}_{n+1} \to \mathcal{S}_n$ yields $E_2^{p,q} = H^p(\mathcal{S}_n; H^q(S^2; \mathbb{Z}))$. The quantum characteristic classes $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) represent the exact obstructions to trivial monodromy of the fibre cohomology $H^*(S^2)$. The vanishing condition of the quantum observable universe axioms enforces $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, ensuring the monodromy representation of $\pi_1(\mathcal{S}_n)$ on $H^*(S^2; \mathbb{Z})$ remains strictly trivial; the adjoint bundle possesses no invariant sections to twist the fibre cohomology. Consequently, the spectral sequence cleanly collapses at the $E_2$ page. Because each level of the brane tower alters only the bundle data while preserving the base geometry, the base manifold $M_0$ remains invariant under jet prolongation. Therefore, $\chi(M_0)$ persists unaltered at every level.
<!-- FILE_END: euler-char-stability-C.md -->

