---
doc_id: arxiv-nucl-th-0507064v2
doc_title: "The Virial Equation of State of Low-Density Neutron Matter"
section_id: sec-002-iii-results
section_title: "RESULTS"
section_number: III
pages: 2-3
source_pdf: 0507064v2.pdf
source_sha256: dcfad7240ba81bf5
doc_brief: "The Virial Equation of State of Low-Density Neutron Matter — 9 sections: Front matter; VIRIAL EQUATION OF STATE; INTRODUCTION"
---
cause low-momentum interactions oﬀer the possibility of
a perturbative and thus systematic approach to nucle-
onic matter [18]. Moreover, for neutron matter at subnu-
clear densities, the Hartree-Fock results agree with com-
plicated Fermi hyper-netted chain [19, 20] and Brueck-
ner [21, 22] calculations. However, these approaches may
not be reliable for very low densities, where the large
scattering length physics is important. This is especially
problematic for Brueckner calculations, since the hole-
line expansion relies on Pauli blocking eﬀects being dom-
inant, so that all large structures are dissolved in the
medium. Note that the equation of state calculation of
Buchler and Coon [23] is close in strategy to the virial
equation of state, but it takes into account Pauli blocking
on the phase shifts and thus uses a model NN interaction.
There are also a number of Skyrme-type [24, 25, 26] and
relativistic mean-ﬁeld [27, 28, 29] parametrizations of the
nuclear energy functional, which are used to calculate
ground-state energies and densities of intermediate-mass
and heavy nuclei. However, the resulting energy func-
tional for neutron matter is not well constrained from
ﬁts to ﬁnite nuclei.
Finally, there are promising lattice simulations for neu-
tron matter using eﬀective ﬁeld theory, where the cou-
plings are regularized on the same lattice [30]. These
calculations are presently limited to small lattices and
to the lowest-order contact interaction, which is ﬁtted to
reproduce the scattering length. In this paper, we study
how the virial equation of state depends on NN scatter-
ing properties and in particular on the physics beyond
the large scattering length. As a result, we assess how a
low-order truncation in the eﬀective ﬁeld theory impacts
the equation of state of low-density neutron matter. This
provides a valuable check for the lattice results.
The virial equation of state is a general, model-
independent equation of state for a dilute gas, provided
the fugacity z = eµ/T is small. Here µ denotes the chem-
ical potential. An additional assumption is that the sys-
tem is in a gas phase and has undergone no phase transi-
tion with decreasing temperature or increasing density.
Under these conditions, the partition function can be
expanded in powers of the fugacity. The second virial
coeﬃcient b2 describes the z2 term in this expansion
and is directly related to the two-body scattering phase
shifts [31, 32]. Little is known about the third virial
coeﬃcient, which describes the z3 term [33, 34]. We em-
phasize that the virial expansion is not a perturbative
expansion in powers of kFas. A great advantage of the
virial formalism is that it includes both bound states and
scattering resonances on an equal footing. It correctly
predicts that thermodynamic quantities, such as the pres-
sure, are continuous as the interaction is changed to con-
vert a low-energy scattering resonance into a weakly-
bound state. This continuity has been demonstrated ex-
perimentally with cold atoms in the crossover region of
a Feshbach resonance (see e.g., [10]) and was also shown
theoretically by Ho and Mueller using the viral expansion
across as = ±∞ [14].
This paper is organized as follows. We brieﬂy intro-
duce the virial equation of state in Section II. Further
details can be found in [3]. In Section III, we present
results for the second virial coeﬃcient, the pressure, en-
ergy, entropy and the free energy of low-density neutron
matter. We also study the dependence of the virial coeﬃ-
cient on NN scattering properties and show that neutron
matter scales to a very good approximation. Finally, we
conclude in Section IV.
II. VIRIAL EQUATION OF STATE
For the virial equation of state we expand the grand-
canonical partition function or the pressure in a power
series of the fugacity
P = 2T
λ3
(
z + z2bn + z3b(3)
n + O(z4)
)
, (3)
where λ denotes the nucleon thermal wavelength λ =
(2π/mT )1/ 2 and bn, b(3)
n are the second and third virial
coeﬃcients for neutron matter respectively. We will in-
clude b(3)
n only to make an error estimate for our virial
results. The density follows from diﬀerentiating the pres-
sure with respect to the fugacity n = z/T (∂zP )V,T and
is given by
n = 2
λ3
(
z + 2z2bn + 3z3b(3)
n + O(z4)
)
. (4)
Therefore, the fugacity expansion is an expansion in pow-
ers of nλ3, and for ﬁnite temperatures, it is valid to much
higher densities than the kFas expansion. In this work,
we truncate the virial expansion after second order in
the fugacity. This leads to an equation of state that is
thermodynamically consistent.
3
The dependence of the density on z can be inverted.
This gives the virial equation of state directly in terms of
density and temperature P = P
(
z(n, T ), T
)
. In practice,
we directly, without this inversion, generate the equa-
tion of state in tabular form for a range of fugacity val-
ues. This maintains the thermodynamic consistency of
the virial equation of state.
The second virial coeﬃcient is related to the partition
function of the two-particle system ∑
states e−E2/T , where
the sum is over all two-particle states of energy E2. This
sum can be converted to an integral over relative momen-
tum k weighted by the density of states of the interacting
two-particle system. The density of states, and therefore
the second virial coeﬃcient, can then be expressed in
terms of the scattering phase shift δ(k), summed over all
allowed partial waves [31, 32].
For neutron matter, the second virial coeﬃcient bn is
given by
bn(T ) = 1
21/ 2 πT
∫ ∞
0
dE e −E/ 2T δtot(E) − 2−5/ 2 , (5)
where −2−5/ 2 is the free Fermi gas contribution and
δtot(E) is the sum of the isospin-triplet elastic scatter-
ing phase shifts at laboratory energy E. This sum is
over all partial waves with two-particle spin S, angular
momentum L and total angular momentum J allowed by
spin statistics, and includes a degeneracy factor (2 J + 1),
δtot(E) =
∑
S,L,J
(2J + 1) δ 2S+1LJ (E)
= δ1S0 + δ3P0 + 3 δ3P1 + 5 δ3P2 + 5 δ1D2 + . . .
(6)
Note that we have neglected the eﬀects of the mixing
parameters due to the tensor force. We expect that their
contributions to the second virial coeﬃcient describing
spin-averaged observables vanish.
Finally, the entropy S and the energy E are obtained
from the virial equation of state using thermodynam-
ics [14, 32]. The entropy density s = S/V follows from
diﬀerentiating the pressure with respect to the tempera-
ture s = (∂T P )µ . This leads to
s = 5P
2T − n log z + 2T
λ3 z2b′
n , (7)
where b′
n(T ) = dbn(T )/dT denotes the temperature
derivative of the virial coeﬃcient. The energy density
ǫ = E/V can be calculated from the entropy density,
ǫ = T s + nµ − P = 3
