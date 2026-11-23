---
doc_id: arxiv-1203.6041v2
doc_title: "S and D-wave phase shifts in isospin-2 ππ scattering from lattice QCD"
section_id: sec-020-2-induced-representation-method-for-calculating
section_title: "Induced representation method for calculating Clebsch-Gordan coefficients"
section_number: 2
pages: 30-31
source_pdf: 1203.6041v2.pdf
source_sha256: 1113e87534ffd6e0
toc_source: outline
doc_brief: "S and D-wave phase shifts in isospin-2 ππ scattering from lattice QCD — 24 sections: Front matter; S and D-wave phase shifts in isosp; I Introduction"
---
Induced representation method for calculating
Clebsch-Gordan coeﬃcients
We use the projection formula with the induced rep-
resentation [44] to construct the Clebsch-Gordan coeﬃ-
cients for Λ1 ⊗Λ2 →Λ where Λ1, Λ2 and Λ are each
irreps of, respectively, groups G1, G2 and G.
For our
purposes, these groups will be the double cover of the
octahedral group, OD
h , or a little group ⊂OD
h .
A group, G, can be partitioned into cosets by a sub-
group H ⊂G. Two elements x, y ∈G are in the same left
coset17 if and only if y−1x ∈H. One coset, containing
the identity element, will be the subgroup H itself. The
number of cosets n = |G|/|H|. A coset representative is
one element from the coset; ˜R1, ˜R2, . . . , ˜Rn are a set of n
coset representatives, one from each coset (a transversal).
If Λ is a |Λ|-dimensional irrep of H, then Γ = Λ(H) ↑G
is a (n|Λ|)-dimensional unitary representation of G in-
duced from irrep Λ of H. It is deﬁned for R ∈G by
Γ(R)ir,js =

Λ( ˜R−1
i R ˜Rj)rs if ˜R−1
i R ˜Rj ∈H
0
otherwise
(A2)
Here i, j label the coset and r, s the rows and columns of
the irrep Λ.
To make this more concrete, consider the double-cover
octahedral group with parity, G = OD
h (|G| = 96), and
the little group for momentum⃗pref = [0, 0, 1], H = Dic4
(|H| = 16).
There must be 6 left cosets with this lit-
tle group and these correspond to the 6 momenta in
{⃗pref}⋆.
If R1 and R2 are in the same coset, then
R2⃗pref = R1R−1
1 R2⃗pref = R1RH⃗pref where RH ∈H. But
from the deﬁnition of the little group, RH⃗pref =⃗pref,
and therefore R2⃗pref = R1⃗pref.
The converse can also
be shown to be true.
Therefore, each left coset can
be labelled by⃗p ∈{⃗pref}⋆with elements R such that
R⃗pref =⃗p.
Therefore, in Eq. A2, the indices i, j refer to a par-
ticular momentum direction,⃗p ∈{⃗pref}⋆. In eﬀect the
induced representation splits up R into a piece RH in
the little group [giving Λ(RH)] and a piece which rotates
the momentum direction from⃗pref to⃗p.
The freedom
to choose a particular coset representative for each coset
is the same freedom as the choice of lattice rotation R
which rotates⃗pref to⃗p (see Ref. [27]). It is not important
which particular element is chosen as the representative
but this choice should be made consistently; we discuss
our conventions in Section A 3.
Once the induced representations, Γi = Λi(Gi) ↑OD
h
(i = 1, 2), have been constructed, the Clebsch-Gordan
coeﬃcients can be generated using the projection formula
in the same way as Clebsch-Gordan coeﬃcients for OD
h ⊗
OD
h →OD
h . The projection formula gives
h
OΛµ(⃗P)
i†
= |Λ|
|G|
X
R∈G
Λ(R)∗
µµ′
X
j1,µ′
1
j2,µ′
2
Γ1(R)j1µ′
1,i1µ1 Γ2(R)j2µ′
2,i2µ2

OΛ1µ′
1({⃗p1}⋆
j1)
† 
OΛ2µ′
2({⃗p2}⋆
j2)
† ,
(A3)
where⃗P = {⃗p1}⋆
j1 + {⃗p2}⋆
j2 is ﬁxed, µ, µ(′)
1 , µ(′)
2
label ir-
rep rows, and i1, j1 and i2, j2 label the diﬀerent mo-
menta in the sets {⃗p1}⋆and {⃗p2}⋆respectively.
Note
17 note that if H is not a normal subgroup, the left and right cosets
are diﬀerent
that this is written for operators which transform as
ˆRO†
Λµ = P
µ′ Λ(R)µ′µO†
Λµ′.
After forming the appro-
priate linearly independent combinations18, the Clebsch-
18 linear combinations of µ′, µ1, µ2; it is suﬃcient to consider one
particular i1 and i2
Gordan coeﬃcients can be read oﬀup to a phase choice
and normalisation. We choose the phase so that our re-
sulting correlators are real.
When⃗P = {⃗p1}⋆
j1 + {⃗p2}⋆
j2 =⃗0, G = OD
h and the
sum is over all R ∈OD
h . In this case it is suﬃcient to
consider i1 = i2 = 1 to generate all the Clebsch-Gordan
coeﬃcients.
When⃗P = {⃗p1}⋆
j1 + {⃗p2}⋆
j2̸ =⃗0, G is a little group and
the sum over R is restricted to those elements in the little
group. A particular choice of i1 and i2 can be made such
that⃗P = {⃗p1}⋆
i1 + {⃗p2}⋆
i2; because R is in the little group,
the rotations of⃗p1 and⃗p2 will automatically ensure that⃗
P is ﬁxed.
3.
