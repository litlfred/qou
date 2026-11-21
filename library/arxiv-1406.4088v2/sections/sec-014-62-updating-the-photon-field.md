---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-014-62-updating-the-photon-field
section_title: "Updating the photon field"
section_number: 6.2
pages: 29-29
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Updating the photon ﬁeld
The HMC has to generate photon ﬁelds that fulﬁll the zero mode constraint, Eq. (S3). Since the constraint
is linear in the ﬁelds, the implementation of such HMC is straightforward: one has to require that the HMC
momenta also satisfy the same constraint. This has to be enforced by removing the zero-mode part of the usual
HMC force in each microcanonical step.
Due to the vanishing mass of the photon and the correspondingly large correlation lengths a standard HMC
integration of the photon ﬁelds results in large autocorrelation times. Even for a pure photon simulation we
observed that the 1x1 compact plaquette does not thermalize after several thousand trajectories, see Fig. S8. To
eliminate this we use a Fourier accelerated HMC. Let us ﬁrst discuss the case of the pure photon theory. In the
standard HMC we introduce momenta Πµ,k for all Aµ,k’s and add a kinetic term |Πµ,k|2/(2m) to the photon
action, Eq. (S5). The mass parameter is usually chosen as m = 1, but one can also allow it to be k-dependent,
leading to the following ”Hamiltonian”:
H =
1
2TL3
X
µ,k

|ˆk|2|Aµ,k|2 + |Πµ,k|2
mk

.
At the beginning of an HMC trajectory we generate new momenta with a distribution
exp(−|Πµ,k|2/(2mk))
and then integrate the canonical equations obtained from the above Hamiltonian until time t. The Hamiltonian
is just a set of uncoupled harmonic oscillators, therefore after time t the photon ﬁeld will be
Aµ,k(t) = Aµ,k(0) cos(ωkt) + Πµ,k(0)
mkωk
sin(ωkt)
with ωk = |ˆk|/√mk. For any oscillator if we let it evolve for a quarter period (ωkt = π/2) then the ﬁrst term
becomes zero, so the Aµ,k ﬁeld ”forgets” its previous (t = 0) value. Since we have the freedom to choose
the parameters mk arbitrarily, setting mk = 4|ˆk|2/π2 will eliminate the ﬁrst term for all oscillators at t = 1,
therefore producing an exact heatbath step with zero autocorrelation. This is demonstrated in Fig. S8, where
the plaquette has the correct distribution starting with the ﬁrst trajectory. The implementation of this algorithm
requires Fourier transformations of the photon ﬁelds and momenta for every step of the HMC, but this turned
out to be computationally negligible compared to Dirac operator inversions.
After including the coupling to quarks, the autocorrelation does not vanish any more, but since the coupling
is small it is much smaller than with a standard HMC algorithm. In our runs the thermalization of the photon
ﬁeld always occurred after a few trajectories.
