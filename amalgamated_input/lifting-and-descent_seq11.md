<!-- FILE_START: archimedean-lifting-intro.md -->
The preceding sections developed lifting, descent, and mass over a generic ring $R$. This section restricts to $R = \mathbb{R}$. The brane tower becomes a sequence of smooth jet bundles $J^1 \mathcal{S}_n$, reducing the categorical mass identity to a multiplicative integral.

The jet machinery descends first. Smooth jet prolongation frames $J^1\mathcal{S}_n$ as the geometric carrier of $A_n$. The Yekutieli extension fixes the band $\mathcal{B} = \mathcal{O}_M^{\times}$, and the smooth proof of the $\mathrm{QU} \Rightarrow \mathrm{QOU}$ specialisation instantiates the main theorem for $\mathrm{SU}_q(2)$ frame bundles. Nonabelian multiplicative integration realizes the categorical mass identity as a physical non-commutativity invariant of the vortex on $\mathcal{S}$.

Two structural lemmas support the mass programme. The smooth Euler characteristic stability verifies the $\chi(A_n)$ proposition, while the defining boundary structure isolates the codimension and chirality data of the brane boundary. The central analytic consequence is the Quantum Dilogarithm as Localized Torsion Volume, equating the quantum dilogarithm to the torsion volume of the localised Reeb flow.

The remainder establishes the categorical mass conjecture. The conjectural decomposition splits the mass integrand by descent involution; subsequent lemmas isolate the eigenspaces, the unknot-core holonomy, the transient exceptional-divisor localisations, and their quantum dilogarithm evaluation. The Mass-decomposition proof aggregates these steps, while the $\mathrm{SU}(2)$ example supplies the smooth test case guiding downstream numerical predictions.
<!-- FILE_END: archimedean-lifting-intro.md -->

<!-- FILE_START: jet-prolongation-C.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum observable universe ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) with instanton connection $A$ on the principal bundle $P$ and metric $g$ on $\mathcal{S}$. Write $\widetilde{M} = \mathcal{S}$ for the total space of $\mathcal{S}$. Define $P'$ as the frame bundle and $\mathcal{S}'$ as the bundle of orthonormal frames of the first jet bundle $J^1 \mathcal{S}$. Then $A$ and $g$ uniquely determine a connection $A'$ on $P'$ such that $(\mathbf{C}, \tilde\varTheta, G, \mathcal{S}')$ is an archimedean quantum observable universe.
<!-- FILE_END: jet-prolongation-C.md -->

<!-- FILE_START: yekutieli-archimedean-band.md -->
In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), the banding sheaf is
$\mathcal{B} = \mathcal{O}_M^{\times}$ (the sheaf of invertible
holomorphic functions on $M$).
<!-- FILE_END: yekutieli-archimedean-band.md -->

<!-- FILE_START: euler-char-stability-C.md -->

In the archimedean realisation, the stability $\chi(A_{n+1}) = \chi(A_n)$ can also be verified via the Leray–Serre spectral sequence.

By the construction of the [recursive brane tower](#def:recursive-brane-tower), $\mathcal{S}_{n+1}$ is the bundle of orthonormal frames of the first jet bundle $J^1 \mathcal{S}_n$ ([jet prolongation](#prop:jet-prolongation)). The Euler characteristic of a fibre bundle $F \hookrightarrow \mathcal{S}_{n+1} \to \mathcal{S}_n$ satisfies the multiplicativity formula:

$$
  \chi(\mathcal{S}_{n+1}) =  \chi(\mathcal{S}_n) \cdot \chi(F),
$$

provided the fibre $F$ has the homotopy type of a finite CW-complex and the base acts as the identity on $H^*(F; \mathbb{Q})$. In the brane tower, the fibre is $\mathrm{SU}(2) \cong S^3$, which has $\chi(S^3) = 0$. However, the relevant bundle is not $\mathrm{SU}(2)$ itself but the *projectivised* frame bundle, whose typical fibre is $\mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ with $\chi(S^2) = 2$. Nonetheless, the Euler characteristic is preserved for the following reason.

The Leray–Serre spectral sequence of $S^2 \hookrightarrow \mathcal{S}_{n+1} \to \mathcal{S}_n$ has $E_2^{p,q} = H^p(\mathcal{S}_n; H^q(S^2; \mathbb{Z}))$. The quantum characteristic classes $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) are precisely the obstructions to trivial monodromy of the fibre cohomology $H^*(S^2)$. By the vanishing condition of the quantum observable universe axioms—which forces $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$—the monodromy representation of $\pi_1(\mathcal{S}_n)$ on $H^*(S^2; \mathbb{Z})$ is trivial (the adjoint bundle has no invariant sections to twist the fibre cohomology). Consequently, the spectral sequence collapses at the $E_2$ page. The preservation of the Euler characteristic follows because the base manifold $M_0$ is invariant under jet prolongation: each level of the brane tower alters the bundle data but not the base geometry. Hence $\chi(M_0)$ is preserved at every level.
<!-- FILE_END: euler-char-stability-C.md -->

