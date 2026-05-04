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

4. ***$q$-Pochhammer partial-product expansion (pre-Archimedean,
   structural).** Substituting the partial-product factorisation
   $\hat{V}_i(q) = C_i(q) \cdot \Phi_{n_i}(x_i; q)$ from
   [algebraic quantum volume §partial-product expansion](#def:algebraic-quantum-volume)
   into route 3 gives the explicit shared denominator*

   $$
     \mathrm{Vol}_{q_0}(\beta)
     \;=\;
     \frac{\prod_i C_i(q_0)}{\prod_i (x_i; q_0)_{n_i}},
   $$

   *whose denominator $\prod_i (x_i; q_0)_{n_i}$ is the algebraic
   image of the JSJ-piece cusps
   ([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
   This route does not produce a different number from route 3 — it
   is the same evaluation rewritten to expose the pole structure that
   feeds the Picard-Lefschetz / Seiberg-Witten thimble integration
   ([SW-period $\equiv$ thimble integral](#prop:sw-period-thimble-equivalence))
   and the Newton-Raphson seeding rule for the Thurston gluing
   equations.*

*Route 4 is structural rather than numerical: it is a rewriting of
route 3 that names the algebraic denominator. The explicit shared
denominator is the bridge between the algebraic state sum and the
geometric volume; it is the QOU-native form of the Kashaev limit
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence)).*

*Proof sketch.*
$\mathrm{Vol}_q(\beta) = \prod \hat{V}_i(q)$ is a finite product in
$\mathbb{Z}[q^{1/2}, q^{-1/2}][z]$; route 1 follows from $H_A(1)=0$,
route 3 is direct evaluation, route 2 is the Kashaev–Murakami–Murakami
theorem applied through the realization functor.  $\square$
