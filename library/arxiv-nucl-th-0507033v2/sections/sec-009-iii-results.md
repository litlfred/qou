---
doc_id: arxiv-nucl-th-0507033v2
doc_title: "Cluster Formation and The Virial Equation of State of Low-De nsity Nuclear Matter"
section_id: sec-009-iii-results
section_title: "RESULTS"
section_number: III
pages: 4-5
source_pdf: 0507033v2.pdf
source_sha256: 57509b3ce5f9f8cc
doc_brief: "Cluster Formation and The Virial Equation of State of Low-De nsity Nuclear Matter — 19 sections: Front matter; INTRODUCTION; FORMALISM"
---
for spin-zero particles [29] to include spin and isospin.
The virial coeﬃcient is related to the partition function
of the two-particles system ∑
states e−E2/T , where the
sum is over all two-particle states of energy E2. This
sum can be converted to an integral over relative mo-
mentum k weighted by the density of states. The diﬀer-
ence between the density of states of an interacting and a
free two-particle system can be expressed in terms of the
derivative of the two-body phase shift dδ(k)/dk [29, 35].
Finally, if one integrates by parts, the virial coeﬃcients
can be calculated from an integral over the scattering
phase shifts summed over all partial waves with two-body
spin S, isospin T , orbital angular momentum L and total
angular momentum J allowed by spin statistics.
The virial coeﬃcient bn describes the interactions in
pure neutron matter, and we have
bn(T ) = 1
21/ 2 πT
∫ ∞
0
dE e −E/ 2T δtot
n (E) − 2−5/ 2 . (19)
Here, −2−5/ 2 is the free Fermi gas contribution due to the
Pauli principle and δtot
n (E) is the sum of the T = 1 elastic
scattering phase shifts at laboratory energy E. This sum
includes a degeneracy factor (2 J + 1),
δtot
n (E) =
∑
S,L,J
(2J + 1) δ 2S+1LJ (E)
= δ1S0 + δ3P0 + 3 δ3P1 + 5 δ3P2 + 5 δ1D2 + . . .
(20)
Here and in the following we have neglected the eﬀects of
the mixing parameters due to the tensor force. We expect
that their contributions to the second virial coeﬃcients
describing spin-averaged observables vanish.
The pn virial coeﬃcient can be decomposed as
bpn(T ) = bnuc(T ) − bn(T ) , (21)
where bnuc is the second virial coeﬃcient for symmetric
nuclear matter. With bpn and bn one can describe asym-
metric matter with arbitrary proton fraction. For bnuc,
the contributions from the deuteron bound state and the
scattering continuum are given by
bnuc(T ) = 3
21/ 2
(
eEd/T − 1
)
− 2−5/ 2
+ 1
23/ 2 πT
∫ ∞
0
dE e −E/ 2T δtot
nuc(E) , (22)
where the term −1 in the deuteron contribution comes
from the partial integration (the phase shift at zero en-
ergy being π times the number of bound states) and
the factor 3 counts the spin-isospin degeneracy of the
deuteron. The total phase shift δtot
nuc(E) for nuclear mat-
5
ter also receives contributions from T = 0 states,
δtot
nuc(E) =
∑
S,L,J
(2J + 1)(2T + 1) δ 2S+1LJ (E)
= 3 δ1S0 + 3 δ3S1 + 3 δ1P1
+ 3 δ3P0 + 9 δ3P1 + 15 δ3P2 + 15 δ1D2
+ 3 δ3D1 + 5 δ3D2 + 7 δ3D3 + . . . (23)
For spin-zero alpha particles we can directly use the
results of [29, 35], which give for the virial coeﬃcient bα
bα (T ) = 21/ 2
πT
∫ ∞
0
dE e −E/ 2T δtot
α (E) + 2−5/ 2 , (24)
where +2 −5/ 2 describes the contribution for a free Bose
gas and the total phase shift δtot
α (E) for elastic αα scat-
tering is given by
δtot
α (E) =
∑
L
(2L + 1) δL(E)
= δS + 5 δD + 9 δG + 13 δI + . . . (25)
For the αα virial coeﬃcient and for the following N α
virial coeﬃcient, we have not taken into account the ef-
fects of inelasticities. For low temperatures, we expect
their contributions to be small due to the tight binding
of the alpha particle.
Finally, the N α virial coeﬃcient is given by
bαn (T ) =
( 5
4
) 1/ 2 1
πT
∫ ∞
0
dE e −4E/ 5T δtot
αn (E) , (26)
with total phase shift δtot
αn (E) for Nα scattering at nucleon
laboratory energy E,
δtot
αn (E) =
∑
L,J
(2J + 1) δLJ (E)
= 2 δS1/ 2 + 2 δP1/ 2 + 4 δP3/ 2 + 4 δD3/ 2 + 6 δD5/ 2
+ 6 δF5/ 2 + 8 δF7/ 2 + . . . (27)
Once the four virial coeﬃcients bn(T ), bpn(T ), bα (T ) and
bαn (T ) have been calculated, the pressure is determined
from Eq. (11) using fugacities zn and zp that reproduce
the desired baryon density nb and proton fraction Yp us-
ing Eqs. (2,13-17).
D. Entropy and Energy
The entropy S and the energy E can be calculated from
the virial equation of state using thermodynamics [11,
35]. The entropy density s = S/V follows from
s =
( ∂P
∂T
)
µ i
. (28)
Here the temperature derivative is at constant µp and
µn, and thus constant µα due to chemical equilibrium.
This leads to
s = 5P
2T − nn log zn − np log zp − nα log zα
+ 2T
λ3
(
(z2
n + z2
p)b′
n + 2zpznb′
pn
)
+ T
λ3α
(
z2
α b′
α + 2zα (zn + zp)b′
αn
)
, (29)
where b′
i denotes the temperature derivative of the second
virial coeﬃcients b′
i(T ) = dbi(T )/dT . The energy density
ǫ = E/V can be calculated from the entropy density by
ǫ = T s +
∑
i=n,p,α
niµi − P
= 3
