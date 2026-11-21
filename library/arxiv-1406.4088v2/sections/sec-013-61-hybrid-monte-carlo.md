---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-013-61-hybrid-monte-carlo
section_title: "Hybrid Monte Carlo"
section_number: 6.1
pages: 28-29
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Hybrid Monte Carlo
We use standard techniques to generate gauge conﬁgurations, including the hybrid Monte-Carlo (HMC) al-
gorithm (46) with even-odd preconditioning (47), multiple time-scale integration aka. “Sexton-Weingarten
scheme” (48), mass preconditioning aka. “Hasenbusch trick” (49), Omelyan integrator (50), Rational Hybrid
Monte Carlo acceleration with multiple pseudofermions (51). Conﬁgurations are separated by ten unit-length
trajectories.
In previous isospin symmetric simulations, the two lightest quarks could be bundled together and a standard
Hybrid Monte Carlo was applicable. Now that all the quarks have different charges and masses, each of them
has to be included with a separate fermion determinant. This causes an extra difﬁculty, because the sign
of detD can become negative for small quark masses when Wilson fermions are used. If this happens, the
common update algorithms break down. However if the spectral gap of the hermitian γ5D operator is large
enough, then the negative sign conﬁgurations play no role in the simulation. This is the case, as one approaches
the continuum or the inﬁnite volume limits (52). In practice, if the lowest eigenvalue of the operator
√
D†D has
a non-vanishing separation from zero, then the number of negative-weight conﬁgurations is exponentially small
in that separation and the standard algorithms can be safely used. If there are no negative sign conﬁgurations,
then the relation
detD = det
√
D†D
holds and the simulation can be straightforwardly done with the RHMC algorithm. The RHMC also needs the
lowest eigenvalue of the
√
D†D operator to be determined, in order to get a suitable rational approximation
for the (inverse) square root function. The small eigenvalues are obtained using the Krylov-Schur algorithm.
Our implementation is based on the program package, which is described in Ref. (53). In order to split the
determinant of the fermion matrix D into an infrared and ultraviolet part, we combine the RHMC algorithm
with the Hasenbusch trick:
detD = det
1
p
1 + ρ2/(D†D)
· det
p
D†D + ρ2,
and integrate the ﬁrst/second determinant on a coarse/ﬁne timescale. A similar combination of the two tech-
niques was already proposed in the staggered fermion formulation (54).
The absence of the negative-weight conﬁgurations and the validity of the absolute-value approximation
can only be justiﬁed a posteriori. This validation is shown in Figure S7. The eigenvalue distributions are
sufﬁciently bounded away from zero, from which we conclude that our simulations are safe from problems
induced by eigenmodes becoming too small or even changing signs during the RHMC integration, for the
parameter values considered in this work. We also monitored the fermion force for dangerous spikes, which
would signal eigenmodes approaching zero and being repelled by a large force. We do not see any such spikes
in the time history even in our potentially most affected ensemble.
We check that the violation of the HMC energy (H) conservation is small and that the condition ⟨exp(−∆H)⟩=
1 is always true within errors.
Another important aspect that requires special attention is autocorrelations of physical observables. Since
we generate a Markov Chain with our HMC simulation algorithm, subsequent measurements are correlated.
The most strongly autocorrelated quantity is typically the topological charge. Its autocorrelation becomes very
large for lattice spacings much smaller than ≈0.05 fm and our choice of boundary conditions. We calculated
the autocorrelation of the topological charge using the openly available package UWerr (55). To deﬁne the
charge the Wilson-ﬂow was used to smoothen the conﬁguration. Even on the potentially most affected ensemble
with smallest lattice spacings the integrated autocorrelation time was about 50 trajectories.
