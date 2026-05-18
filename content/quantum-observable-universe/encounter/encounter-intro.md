[Chapter 12](#chap:particle-interactions) presented confinement as
an algebraic selection principle: the Gröbner--Shirshov reduction
produces a unique normal form, and the linear program
[(operator-selection LP)](#prop:operator-selection-lp) — together
with its semidefinite refinement
[(confinement SDP)](#prop:confinement-sdp) — picks the active
Wedderburn channels by minimising the categorical action.  What
that chapter does **not** answer is *how two particles come to
interact in the first place*.  Two vortices roaming the brane do
not encounter each other by appointment.  Yet the moment their
cores cross some scale, the SDP runs and a knot operator is
selected.  What scale, and what mechanism?

This short chapter answers the question.  The encounter is
**geometric**, not metric: two particles "find" each other when
their cores enter a region where the smooth base manifold $M$ is
no longer well-defined and the internal fibre
$\mathcal{S}_p \subset \mathcal{S}$
([state bundle fibre](#def:exceptional-divisor)) takes over as
the operative geometry.  Inside that region the merged knot
complement admits a complete, finite-volume hyperbolic
structure, and the SDP solver of
[Chapter 12](#chap:particle-interactions) is the algebraic shadow
of a **Picard--Lefschetz steepest-descent flow** on the
$q$-Pochhammer potential
([algebraic--geometric dilogarithm equivalence](#conj:algebraic-geometric-dilog-equivalence),
[GB--PL thimble bijection](#conj:gb-reduction-pl-thimble-bijection)).
Mostow rigidity then locks the resulting topology to a unique
hyperbolic volume, which the
[Archimedean realization functor](#def:archimedean-realization-functor)
converts into the discrete mass eigenvalue measured in the lab.

The chapter is exposition, not new theory.  Its purpose is to
name and sequence pieces that already live elsewhere in the
manuscript ---
[Picard--Lefschetz thimbles](#def:picard-lefschetz-thimble),
[$\Phi_q$-piece](#def:phi-q-piece) cusp data, the
[shadow-price reading of the LP dual](#prop:mass-coefficient-shadow-price)
--- so that the reader has a single geometric story binding the
algebraic SDP to the observed mass spectrum.
