**Proposition.**
*The algebraic quantum volume
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}][z]$
specialises along three routes — only one of which is part of the
QOU-internal derivation; the other two are*
[**post-Archimedean naming**](#rem:kashaev-as-archimedean-realization)
*via the realization functor.*

1. ***$q \to 1$ (classical limit; post-Archimedean naming).** As $q \to 1$,
   $H_A \to 0$, $z \to 1/2$, every crossing matrix degenerates to
   $(c+d)\,I$, and $\mathrm{Vol}_q(\beta) \to 1$.  This is the image
   under the realization functor at $q = 1$, not a QOU-internal
   identity.*

2. ***Roots of unity (post-Archimedean naming via the volume conjecture).**
   At $q = e^{2\pi i/N}$ the colored Jones polynomial grows as
   $\exp(N \cdot \mathrm{Vol}(S^3 \setminus K)/2\pi)$; collectively
   these evaluations encode the hyperbolic volume.  This is the
   Kashaev–Murakami–Murakami theorem, identified with the realization
   functor in
   [Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization);
   it is borrowed naming, not used in any QOU-internal derivation.*

3. ***Substrate evaluation (pre-Archimedean, exact).** At $q = q_0$
   (not a root of unity),
   $\ln\lvert\mathrm{Vol}_{q_0}(\beta)\rvert = \Phi_1(\beta)$
   is a finite element of $\mathbb{Q}(q_0^{1/2})$.  This is the
   $q$-dilogarithm volume that enters the mass formula.*

*The mass formula uses route 3 for the per-atom binding $\Phi_1$
and uses the realized scale $8G = \mathrm{Vol}(\mathcal{B}_3)$ as
its dimensional bridge to laboratory MeV; the appearance of $8G$
is route 2 used only as a name for the realized scale, not as a
derivation step.*

*Proof sketch.*
$\mathrm{Vol}_q(\beta) = \prod \hat{V}_i(q)$ is a finite product in
$\mathbb{Z}[q^{1/2}, q^{-1/2}][z]$; route 1 follows from $H_A(1)=0$,
route 3 is direct evaluation, route 2 is the Kashaev–Murakami–Murakami
theorem applied through the realization functor.  $\square$
