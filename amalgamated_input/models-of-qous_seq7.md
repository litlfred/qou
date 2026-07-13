<!-- FILE_START: witt-vector-lifting-intro.md -->
The $\mathbb{Q}_p$ realisation provides a QOU over characteristic $0$. The $\mathbb{F}_p$ realisation provides one over characteristic $p$. The *Witt vector functor* $W$ and the theory of formal groups over $p$-adic rings mediate the passage between them.
<!-- FILE_END: witt-vector-lifting-intro.md -->

<!-- FILE_START: witt-vector-lift.md -->
Let $H$ be a commutative formal group over $\mathbb{F}_p$ equipped with a skewed-Poisson structure $\pi_<$ (a biderivation $\pi_<\colon\mathcal{O}(H)\otimes\mathcal{O}(H)\to\mathcal{O}(H)$ satisfying a graded anti-symmetry and a $p$-truncated Jacobi condition). The *Witt vector lift* is the formal group $\widehat{G}$ over $W(\mathbb{F}_p) \cong \mathbb{Z}_p$ obtained by integrating $\pi_<$ in the sense of Fresse. The distribution algebra $\mathrm{Dist}(\widehat{G})$ is the $p$-adic completion of the universal enveloping algebra $\mathcal{U}(\mathrm{Lie}(H))$ deformed by $\pi_<$.
<!-- FILE_END: witt-vector-lift.md -->

<!-- FILE_START: skew-poisson-integration.md -->
Let $H/\mathbb{F}_p$ be a smooth commutative formal group and $\pi_<$ a skewed-Poisson structure on $H$. There exists a (generally non-commutative) formal group $G/\mathbb{Z}_p$ such that:

1. $G \otimes_{\mathbb{Z}_p} \mathbb{F}_p  \cong  H$ (reduction modulo $p$ recovers $H$).
2. $\mathrm{Dist}(G)$ is a deformation of $\mathrm{Dist}(H)$. The distribution algebra of $G$ deforms that of $H$ and degenerates back to it under reduction modulo $p$. We compute this via a Gröbner–Shirshov basis for the relations of the enveloping algebra.
3. The comultiplication on $\mathrm{Dist}(G)$ satisfies the *strong multiplicativity* condition. The Frobenius relation $(\mathrm{Id}\otimes m)\circ(\Delta\otimes\mathrm{Id}) = \Delta\circ m$ (the comultiplication $\Delta$ intertwines with the multiplication $m$) is preserved under the deformation.
<!-- FILE_END: skew-poisson-integration.md -->

<!-- FILE_START: witt-lift-qou.md -->
Skew-Poisson integration provides the algebraic engine behind jet prolongation when the base field is $\mathbb{Q}_p$ rather than $\mathbb{C}$:

1. The Frobenius–Hopf object $A$ in the $\mathbb{F}_p$ realisation carries a skewed-Poisson structure induced by the $q$-commutator $[\hat{X},\hat{P}]_q = i\hbar_q$.
2. The Witt vector lift $\widehat{G}$ is the non-commutative formal group whose distribution algebra deforms $\mathrm{Dist}(H)$. This is the passage from the $\mathbb{F}_p$ fibre algebra to the $\mathbb{Q}_p$ fibre algebra.
3. Strong multiplicativity is exactly the Frobenius relation used in jet prolongation. This ensures that the comultiplication—hence the gauge connection—is preserved under the lift.
4. The unit-root condition on the $F$-crystal corresponds to the integrability of the skewed-Poisson structure. The biderivation $\pi_<$ integrates if and only if the associated $F$-crystal is unit-root.

Without the formal-groups integration theorem, the $p$-adic lifting mechanism would remain a conjecture. The results of Fresse convert it into a proven categorical lift.
<!-- FILE_END: witt-lift-qou.md -->

