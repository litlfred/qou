The Cardona–Miranda–Peralta-Salas–Presas
\cite{cardonamirandaperaltasalaspresas2021} route from steady
Euler flow to contact-Reeb flow proceeds by a **conformal change
of metric**: a divergence-free, non-vanishing Euler field $X$ on
$(M^3, g)$ becomes, after rescaling $X \mapsto X / |X|_g^2$ and
applying a conformal factor, the Reeb vector field of a contact
form on $(M^3, \tilde g)$. Universality of the dynamics is a
property of the contact structure, not of the original metric.

This is the *exact* operation the QOU performs through its
substrate parameter $q$. The
[$q$-Navier–Stokes equation](#def:q-navier-stokes) replaces the
classical Riemannian inner product on the brane with the
$q$-deformed Frobenius pairing
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate));
this is a one-parameter family of metric changes, smoothly
interpolating between
- the **full Levi-Civita connection** (the "Euler-side" geometry
  in which the substrate looks like a Riemannian fluid), and
- its **Reeb projection** along $\xi_q$ (the "contact-side"
  geometry in which the flow is purely along the Reeb field of
  $\varTheta_q$).

The interpolation parameter is $q$ itself. Two regimes are
useful to keep in mind.

| Parameter limit | Geometric picture | Dynamical content |
|---|---|---|
| $q \to 1^+$ | Full Riemannian metric; contact form $\varTheta_q$ becomes degenerate | Classical Navier–Stokes; Reeb projection collapses |
| $q > 1$ generic | Genuine contact metric on $\mathcal{S}$ | $q$-NS regular ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)); Reeb flow Turing-complete ([rem:reeb-contact-universal-computer](#rem:reeb-contact-universal-computer)) |
| $q \to \infty$ | Pure Reeb (horizontal vanishes) | Hamiltonian first-return on Poincaré section; tape-only dynamics |

**A geometric reading of the $q$-NS obstruction.**
The
[NS obstruction class](#def:ns-obstruction) measures the failure
of the classical $q = 1$ contact form to remain non-degenerate at
a vortex-collision locus. Miranda's metric-change argument
provides the geometric content: increasing $q$ above $1$ rescales
the Riemannian metric so as to push the contact form away from
degeneracy. The
[Levi form condition number](#prop:core-levi-form), which
diagnoses contact degeneracy, is precisely the metric invariant
that the $q$-deformation flattens. Concretely, the
[quantum pressure](#rem:madelung-fluid) term in $q$-NS is the
isotropic "padding" that prevents the Levi eigenvalues from
crossing zero — which is the metric-change face of the
deformation.

**Where this lives in the proof strategy.**
Two consequences for the
[q-NS research programme](#rem:q-ns-research-programme):

1. The well-posedness of $q$-NS for $q > 1$
   ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)) and the
   classical breakdown at $q = 1$ are *not* a quantum
   phenomenon; they are the smooth-vs-degenerate dichotomy in
   contact geometry, viewed through Miranda's lens.

2. The
   [Levi degeneracy conjecture](#conj:levi-degeneracy) becomes
   a question about which limit a particular vortex collision
   takes — the metric-Riemannian (NS regular) limit, in which
   the contact form genuinely degenerates and the flow flattens,
   or the contact (NS blowup) limit, in which the metric change
   leaves the contact structure non-degenerate. The two
   subsequent remarks
   ([Biot–Savart](#rem:townsend-biot-savart-strain) and
   [hyperbolic overlap](#rem:hyperbolic-overlap-saturation))
   examine the two regimes in explicit ODE form.

In the Cardona–Miranda language: the $q$-deformation chooses
*which contact metric* the substrate carries, and the choice
controls whether the Reeb dynamics is regular or runs into a
contact-degenerate singularity.
