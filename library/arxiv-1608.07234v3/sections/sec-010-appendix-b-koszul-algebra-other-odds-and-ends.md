---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-010-appendix-b-koszul-algebra-other-odds-and-ends
section_title: "Appendix B.  Koszul algebra; other odds and ends"
section_number: null
pages: 82-85
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS — We describe a graded extension of the usual Hecke algebra: it acts in a graded fashion on the cohomology of an arithmetic group Γ."
---
Let B be a commutative ring with 1. Let
Brrx1, . . . , xrss “ S
ι
ÝÑ R “ Brry1, . . . , yr´δss
where ι sends xi to yi for i ď r ´ δ, and xi to zero for i ą r ´ δ.
Let pS be the kernel of the natural augmentation S Ñ B, and similarly for R. Write tS
for the B-linear dual of for pS{p2
S and similarly for tR. Just as in (88) we have a canonical
identiﬁcation
Ext1
SpB, Bq » tS.
We will prove:
B.1. Lemma. Ext˚
SpB, Bq is a free exterior algebra over its degree 1 component; thus we
have Ext˚
SpB, Bq » ^˚tS as graded B-algebra. Moreover, there is an identiﬁcation of
Ext˚
SpR, Bq with ^˚ptS{tRq in such a way that the natural action of Ext˚
SpB, Bq » ^˚tS
is the natural one obtained from the algebra map ^˚tS Ñ ^˚ptS{tRq.
This will follow from the computations of §B.2 (more precisely, with the precisely
analogous computations wherein one replaces the role of symmetric algebras by power
series algebras).
B.2. Koszul algebra. Let W be a free module of rank e over a base ring B and consider
the ring R “ SymBpWq, i.e. “the ring of functions on W _.” In what follows we will omit
the B subscript on SymB.
We have a resolution
¨ ¨ ¨ Ñ SympWq b ^2W Ñ SympWq b W Ñ SympWq
looooooooooooooooooooooooooooooooooomooooooooooooooooooooooooooooooooooon
K
Ñ B,
where the differential sends
r b w1 ^ ¨ ¨ ¨ ^ wr P SympWq b ^iW ÞÑ
ÿ
i
p´1qi´1rwi b w1 ^ . . . x
wi ^ . . . wr.
There is a corresponding resolution where we replace SympWq by its completion with
respect to the augmentation SympWq Ñ B, i.e. when we replace a symmetric algebra by
a formal power series algebra.
In particular, we get
HomRpK, Bq »
`
^iW
˘_ with zero differentials.
and thus an identiﬁcation of Exti
RpB, Bq with
`
^iW
˘_.
In fact, Ext˚
RpB, Bq is a free exterior algebra, where the algebra structure on the Ext-
groups arising from their identiﬁcation with the cohomology of the differential graded
algebra
HomRpK, Kq.
To see this, one veriﬁes that each element of w P W _, considered as acting on K by
contractions, actually deﬁnes a degree ´1 endomorphism of K; the resulting inclusion
ľ˚pW _q ãÑ HomRpK, Kq
gives a quasi-isomorphism of differential graded algebras.
DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS
83
Suppose now that U is a free submodule of W such that W{U is also free. In this
situation we have a quotient map
R “ SympWq Ñ SympW{Uq :“ ¯R
We have a resolution of R-modules (where the differential is given by the same formula as
before):
¨ ¨ ¨ Ñ SympWq b ^2U Ñ SympWq b U Ñ SympWq
loooooooooooooooooooooooooooooooooomoooooooooooooooooooooooooooooooooon
Q
„
ÝÑ ¯R,
and from this we identify Ext˚
Rp ¯R, Bq with p^˚Uq_.
B.3. Lemma. The action of Ext˚
RpB, Bq » p^˚Wq_ on this is the natural one that arises
from the map W _ Ñ U _.
Proof. It is enough to check this for the action of Ext1
RpB, Bq. We have identiﬁcations:
Ext˚
Rp ¯R, Bq » H˚ pHomRpQ, Bqq “ H˚ pHomRpQ, Kqq .
Explicitly, a class in ωj P p^jUq_ » Extj
Rp ¯R, Bq is represented by a map of complexes
Q Ñ K as follows:
(188)
¨ ¨ ¨
/ R b ^j`1U
/
f

R b ^jU
/
ωjP^jU_

R b ^j´1U
¨ ¨ ¨
/ K1 “ R b W
/ K0 “ R
/ 0.
(since this lifts the map Q Ñ Brjs associated to ωj).
Fix a basis e1, . . . , er for U and extend it to a basis e1, . . . , ee for W. For I Ă t1, . . . , eu
with cardinality r, we deﬁne eI P ^rW thus: write I “ ti1, . . . , iru with i1 ă ¨ ¨ ¨ ă ir
and put eI “ ei1 ^ ei2 ^ ¨ ¨ ¨ ^ eir. We may choose f to be given, explicitly, as
eJ P ^j`1U ÞÑ
ÿ
kPJ
p´1qrks´1ωjpeJ´kq b ek P R b W,
where rks means the position of k in J (i.e. if J is ordered in increasing order, then 1 for
the smallest element, two for the second smallest, etc.)
To compute, now, the action of β P W _ “ Ext1
RpB, Bq on the class ωj, we just regard
β as an R-module map K1 “ R b W Ñ R, and then compose
β ˝ f P HomRp^j`1U b R, Rq “
`
^j`1U
˘_ .
Explicitly,
β ˝ f : eJ ÞÑ
ÿ
kPJ
p´1qrks´1βpekqωjpeJ´kq “ pβ ^ ωj, eJq
i.e. β ^ ωj, where β is the image of β in U _. This concludes the proof.
□
B.4. A result in topology. Suppose that π : X Ñ Y is a covering of pointed Hausdorff
topological spaces, with Galois group ∆. This covering is classiﬁed by a map Y Ñ B∆
from Y to the classifying space of ∆.
There are two natural actions of H˚p∆, Eq (with E a coefﬁcient ring) on H˚pY, Eq:
(a) The ﬁrst arises from pullback of cohomology classes under Y Ñ B∆together
with cup product.
84
AKSHAY VENKATESH
(b) The second arises from the identiﬁcation of the cochain complex of Y , with E
coefﬁcients, with
C˚pY ; Eq » HomE∆pC˚pX, Eq; Eq
where C˚pX; Eq is the cochain complex of X (or e.g. the complex of a ∆-
equivariant cell structure), thought of as a complex of E∆-modules. Then one
composes with self maps of E in the derived category of E∆-modules.
For lack of a reference, we will prove the coincidence of these actions. For this we
will use the following standard Lemma concerning the coincidence of singular and sheaf
cohomology (see [30] for a careful discussion; however this reference does not discuss the
product structures):
B.5. Lemma. For any locally contractible Hausdorff space M, and any E-module A,
let A be the constant sheaf on M with constant value A, considered as an object of the
category of sheaves S of E-modules on M.
Then the complex of local chains U ÞÑ C˚pU, Aq deﬁnes a presheaf on M; let C˚
A be
its sheaﬁﬁcation. Then A Ñ C˚
A is a ﬂasque resolution of A. Moreover, the natural maps
C˚pM, Aq Ñ ΓpM, C˚
Aq “ HomSpA, C˚
Aq
induces, at the level of cohomology, an isomorphism
(189)
H˚pM, Aq » Ext˚
SpA, Aq
which carries the cup product on the left to the Ext-product to the right.
Proof. (that (a) and (b) coincide): Observe, ﬁrst of all, that every E∆-module M gives a
locally constant sheaf M on Y , namely, the one represented by the covering pXˆMq{∆Ñ
Y . The cochains C˚pY, Mq are then given by HomE∆pC˚pX, Eq, Mq.
Fix α∆P Hmp∆, Eq. It gives rise to a homomorphism α : E Ñ Erms in the derived
category of E∆-modules, which can be represented by a diagram E „
Ð P Ñ Erms where
P is a complex of projective E∆-modules. Thus we get a diagram of locally constant
sheaves on Y :
α : E „
Ð P Ñ Erms.
This gives a map in the derived category of sheaves on Y , and thus an element of
Extm
S pE, Eq; this element represents the pullback αY of α∆to Y . or rather its image
under (189).
By the ﬁnal sentence of the Lemma, the cup product with αY is given, at the level of
cohomology, by the Ext-product, which is explicitly the composite:
H˚pY, Eq „
Ð H˚pY, Pq Ñ H˚pY, Ermsq
By the lemma, these groups are naturally identiﬁed with the cohomology of the corre-
sponding cochain groups; so the above composite coincides with
HomE∆pC˚pX, Eq, Eq „
Ð HomE∆pC˚pX, Eq, Pq Ñ HomE∆pC˚pX, Eq, Eq
where the middle term is now the Hom-complex between two complexes.
But this composite is also given by the Ext-product, in the category of E∆-modules,
with the class of α. This concludes the proof of the coincidence of (a) and (b).
□
