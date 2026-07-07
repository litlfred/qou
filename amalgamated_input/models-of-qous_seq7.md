<!-- FILE_START: witt-vector-lifting-intro.md -->
The $\mathbb{Q}_\pp$ realisation ([$p$-adic realisation](#ex:p-adic-realisation)) provides
a QOU over characteristic $0$, while the $\mathbb{F}_\pp$ realisation
([finite field realisation](#ex:finite-field-realisation)) provides one over
characteristic $\pp$.  The passage between them is mediated by the
*Witt vector functor* $W$ and the theory of formal groups
over $\pp$-adic rings.
<!-- FILE_END: witt-vector-lifting-intro.md -->

<!-- FILE_START: witt-vector-lift.md -->
Let $H$ be a commutative formal group over $\mathbb{F}_\pp$ equipped with a
skewed-Poisson structure $\pi_<$
(a biderivation $\pi_<\colon\mathcal{O}(H)\otimes\mathcal{O}(H)\to\mathcal{O}(H)$
satisfying a graded anti-symmetry and a $\pp$-truncated Jacobi condition).
The *Witt vector lift* is the formal group $\widehat{G}$ over
$W(\mathbb{F}_\pp) \cong \mathbb{Z}_\pp$ obtained by integrating $\pi_<$
in the sense of Fresse: the distribution algebra
$\mathrm{Dist}(\widehat{G})$ is the $\pp$-adic completion of the universal
enveloping algebra $\mathcal{U}(\mathrm{Lie}(H))$ deformed by $\pi_<$.
<!-- FILE_END: witt-vector-lift.md -->

<!-- FILE_START: skew-poisson-integration.md -->
Let $H/\mathbb{F}_\pp$ be a smooth commutative formal group and
$\pi_<$ a skewed-Poisson structure on $H$.  Then there exists a
(generally non-commutative) formal group $G/\mathbb{Z}_\pp$ such that:

1. $G \otimes_{\mathbb{Z}_\pp} \mathbb{F}_\pp  \cong  H$
   (reduction modulo $\pp$ recovers $H$);

2. $\mathrm{Dist}(G)$ is a deformation of
   $\mathrm{Dist}(H)$ (the distribution algebra of $G$ deforms
   that of $H$, degenerating back to it under reduction modulo
   $\pp$), computed via a
   Grobner--Shirshov basis for the relations of the enveloping
   algebra;

3. the comultiplication on $\mathrm{Dist}(G)$ satisfies the
   *strong multiplicativity* condition: the Frobenius relation
   $(\mathrm{Id}\otimes m)\circ(\Delta\otimes\mathrm{Id}) = \Delta\circ m$ (the comultiplication $\Delta$ intertwines
   with the multiplication $m$) is preserved under the deformation.

<!-- FILE_END: skew-poisson-integration.md -->

<!-- FILE_START: witt-lift-qou.md -->
[skew poisson integration](#prop:skew-poisson-integration) provides the algebraic
engine behind the
([jet prolongation](#prop:jet-prolongation)) when the base field is
$\mathbb{Q}_\pp$ rather than $\mathbb{C}$:

1. The Frobenius--Hopf object $A$ in the $\mathbb{F}_\pp$ realisation
   ([finite field realisation](#ex:finite-field-realisation)) carries a
   skewed-Poisson structure induced by the $q$-commutator
   $[\hat{X},\hat{P}]_q = i\hbar_q$
   ([Section](#sec:enveloping-algebras-models)).

2. The Witt vector lift $\widehat{G}$
   ([Witt vector lift](#def:witt-vector-lift)) is the non-commutative
   formal group whose distribution algebra deforms
   $\mathrm{Dist}(H)$; in the QOU language this is the passage from
   the $\mathbb{F}_\pp$ fibre algebra to the $\mathbb{Q}_\pp$ fibre
   algebra.

3. Strong multiplicativity (item (3) of
   [skew poisson integration](#prop:skew-poisson-integration)) is exactly the
   Frobenius relation used in Step 2 of the jet prolongation proof,
   ensuring that the comultiplication---hence the gauge connection---is
   preserved under the lift.

4. The unit-root condition on the $F$-crystal
   ([$p$-adic realisation](#ex:p-adic-realisation)) corresponds to the
   integrability of the skewed-Poisson structure: $\pi_<$ integrates
   if and only if the associated $F$-crystal is unit-root.

Without the formal-groups integration theorem, the $\pp$-adic lifting
mechanism would remain a conjecture; the results
of Fresse convert it into a proven categorical lift.
<!-- FILE_END: witt-lift-qou.md -->

