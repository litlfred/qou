---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-012-18-steven-c-pieper-and-r-b-wiringa
section_title: "Steven C. Pieper and R. B. Wiringa"
section_number: 18
pages: 18-19
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
eight operator terms, [1 , σ i · σ j,S ij, L · S] ⊗ [1, τ i · τ j], chosen such that it equals
the CI part of the full interaction in all S- and P-waves and in the deuteron. The
v′
ij is a little more attractive than vij, so a V ′
ijk adjusted so that ⟨H ′⟩ ≈ ⟨H⟩ is also
used. This ensures the GFMC algorithm will not propagate to e xcessively large
densities due to overbinding. Consequently, the upper boun d property applies to
⟨H ′(τ )⟩, and ⟨H −H ′⟩ must be evaluated perturbatively.
Another complication that arises in the GFMC algorithm is th e “fermion sign
problem”. This arises from the stochastic evaluation of the matrix elements in
Eq.(47). The G(Ri, Ri−1) is a local operator and can mix in the boson solution.
This has a (much) lower energy than the fermion solution and t hus is exponentially
ampliﬁed in subsequent propagations. In the ﬁnal integrati on with the antisym-
metric Ψ T , the desired fermionic part is projected out, but in the pres ence of large
statistical errors that grow exponentially with τ . Because the number of pairs that
can be exchanged grows with A, the sign problem also grows exponentially with
increasing A. For A≥8, the errors grow so fast that convergence in τ cannot be
achieved.
For simple scalar wave functions, the fermion sign problem c an be controlled by
not allowing the propagation to move across a node of the wave function. Such
“ﬁxed-node” GFMC provides an approximate solution which is the best possible
variational wave function with the same nodal structure as Ψ T . However, a more
complicated solution is necessary for the spin- and isospin -dependent wave func-
tions of nuclei. In the last few years a suitable “constraine d path” approximation
has been developed and extensively tested, ﬁrst for condens ed matter systems (46)
and more recently for nuclei (19). The basic idea of the const rained-path method
is to discard those conﬁgurations that, in future generatio ns, will contribute only
noise to expectation values. If the exact ground state |Ψ 0⟩ were known, any con-
ﬁguration for which
Ψ( Pn)†Ψ 0(Rn) = 0 , (50)
where a sum over spin-isospin states is implied, could be dis carded. Here Pn
designates the complete path, ( R0,..., Rn) that has led to Rn. The sum of these
discarded conﬁgurations can be written as a state |Ψ d⟩, which obviously has zero
overlap with the ground state. The Ψ d contains only excited states and should
decay away as τ → ∞ , thus discarding it is justiﬁed. Of course the exact Ψ 0 is
not known, and so conﬁgurations are discarded with a probabi lity such that the
average overlap with the trial wave function,
⟨Ψ d|Ψ T ⟩ = 0 . (51)
Many tests of this procedure have been made (19) and it usuall y gives results that
are consistent with unconstrained propagation, within sta tistical errors. However
a few cases in which the constrained propagation converges t o the wrong energy
(either above or below the correct energy) have been found. T herefore a small
number,nu = 10 to 20, unconstrained steps are made before evaluating ex pectation
values. These few unconstrained steps, out of typically 400 total steps, appear to
Exact Calculations of Light Nuclei 19
0 0.05 0.1 0.15 0.2
-50
-40
-30
-20
τ  (MeV-1)
E(τ)  (MeV)
8Be(3+)
8Be(1+)
8Be(4+)
8Be(2+)
8Be(gs)
Figure 3: GFMC E(τ ) using A V18/UIX for various states of 8Be. Averages with
their standard errors are shown by the solid and dashed lines .
be enough to damp out errors introduced by the constraint, bu t do not greatly
increase the statistical error.
Figure 3 shows the progress with increasing τ of typical constrained GFMC
calculations, in this case for various states of 8Be. The values shown at τ = 0
are the VMC values using Ψ T ; VMC values with the best known Ψ V are about
