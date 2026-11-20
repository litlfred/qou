---
doc_id: arxiv-1203.6041v2
doc_title: "S and D-wave phase shifts in isospin-2 ππ scattering from lattice QCD"
section_id: sec-002-ii-operator-construction
section_title: "II Operator construction"
section_number: null
pages: 3-4
source_pdf: 1203.6041v2.pdf
source_sha256: 1113e87534ffd6e0
toc_source: outline
doc_brief: "S and D-wave phase shifts in isospin-2 ππ scattering from lattice QCD — 24 sections: Front matter; S and D-wave phase shifts in isosp; I Introduction"
---
In order to calculate scattering amplitudes we must
extract multi-hadron energy levels with high precision
and so need interpolating operators that eﬃciently in-
terpolate these multi-hadron states. To achieve this we
consider operators constructed from the product of two
hadron operators projected onto deﬁnite total momen-
tum,⃗P, and transforming as a deﬁnite irreducible rep-
resentation of the appropriate symmetry group, lattice
irrep3 Λ, with irrep row, µ,
h
OΛµ(⃗P)
i†
=
X
µ1,µ2⃗
k1,⃗k2⃗
k1+⃗k2=⃗P
C(⃗PΛµ;⃗k1Λ1µ1;⃗k2Λ2µ2)
×
h
OΛ1µ1(⃗k1)
i† h
OΛ2µ2(⃗k2)
i†
. (3)
Here OΛ1,µ1(⃗k1) and OΛ2,µ2(⃗k2) are hadron operators (for
example, fermion bilinear operators), each projected onto
deﬁnite momentum, irrep and irrep row. The Clebsch-
Gordan coeﬃcients, C, and the momenta appearing in
the sum over⃗k1 and⃗k2 will be discussed later.
A conventional inﬁnite volume continuum analogue of
this construction (for total momentum zero with⃗p =⃗
k1 = −⃗k2) would be
h
O[S,ℓ]
J,M
i†
∼
X
λ1λ2
Z
dˆp C(JℓSM;⃗p S1λ1; −⃗p S2λ2)
×

OS1λ1(⃗p)
† 
OS2λ2(−⃗p)
† ,
(4)
3 we use ‘lattice irrep’ to refer to the octahedral group irrep for
a particle at rest and the irrep of the appropriate little group,
discussed later, for a particle at non-zero momentum
with
C =

S1λ1; S2 −λ2

Sλ

ℓ0; Sλ

Jλ

D(J)∗
Mλ (ˆp) ,
where D(ˆp) is a Wigner-D matrix and S1,2 and λ1,2 are
respectively the spins and helicities of hadron 1,2. The
spins are coupled to S = S1 ⊗S2, ℓis the partial wave,
J = ℓ⊗S is the total angular momentum and M is
its z component. However, in all but the simplest cases,
multi-hadron operators constructed by subducing Eq. (4)
into irreducible representations of the lattice symmetry
can mix single-hadron operators transforming in diﬀer-
ent lattice irreps.
Therefore, we prefer Eq. (3) where
such mixings do not occur. The single-hadron operators
transforming in deﬁnite lattice irreps can be optimised
variationally, as shown for the pion in Section IV.
Here we concentrate on the operators to be used to
study two-pion states; the generalisation to other multi-
hadron states is given in Appendix A. The ﬂavor struc-
ture of the operators, for example the projection of ππ
onto deﬁnite overall isospin, I, determines which combi-
nations of Wick contractions appear in the calculation of
the correlators (Section III). Because this ﬂavor structure
generally factorises from the spin and spatial structure we
will not discuss it in detail here. However, because we are
considering two identical pions, Bose symmetry requires
the overall wavefunction to be symmetric under the in-
terchange of the two pions. Therefore, in the I = 2 case
we are considering here or I = 0, the symmetric ﬂavor
part requires a symmetric spatial part (even partial waves
with positive parity). In contrast, I = 1 requires an an-
tisymmetric spatial piece (odd partial waves with nega-
tive parity). In addition, these operators have deﬁnite
charge-conjugation parity, C = +1, for neutral combina-
tions, generalising to G-parity for charged combinations;
for brevity, in the following we omit the C-parity labels.
A.
