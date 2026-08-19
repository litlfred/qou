---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-094-63-computations-in-the-symmetric-product-139
section_title: "Computations in the symmetric product 139"
section_number: 6.3
pages: 147-149
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
In this case the vanishingr6 = r5,1 = 0 can again be checked directly,
using the observation that
pδ6⊕ pδ5,1 = pδ1∗ pδ5 = δW1∗δ−W1
must be supported on the two-dimensional closed subsetW1−W1⊂ X. The
valuesr4,2 = 5 and r3,3 = 51 are less obvious from a geometric point of
view, but notice that they are one less than the generic ranks of the local
systemsV± in chapter 5, in accordance with part (b) of proposition 5.24.
More numerical values for partitions of small degree can be found in
section 6.6 below. After these examples, let us now come to the proof of
the recursion formula in theorem 6.1. Consider the stalk cohomology of the
convolution productδα =δd1∗···∗ δdn. For eachi∈{1,2, . . . ,n} the Specht
moduleσdi is the trivial representation of the symmetric groupSdi, hence it
follows from equation (⋆) above and from the construction of Brill-Noether
sheaves in section 6.1 that
δα =
⨁
β≥α
Kβ α· δβ = pδα⊕cδα
where
pδα =
⨁
β≥α
Kβ α· pδβ and cδα =
⨁
β≥α
Kβ α· cδβ.
The stalk cohomology of a perverse sheaf at a general pointx∈ X(C) is
concentrated in degree−g, so to prove theorem 6.1 we can replace the
generic rank by(−1)g times the Euler characteristic of the generic stalk
cohomology. Thus it will sufﬁce to show that for generalx∈ X(C),
∑
m∈Z
(−1)m+gdimC(H m(δα)x) = ∑
c1,...,cn≥0
c1+···+cn=g
g!
c1!···cn!
n
∏
k=1
(2(g−1−ck)
dk−ck
),
∑
m∈Z
(−1)m+gdimC(H m(cδα)x) = ∑
c1,...,cn≥0
c1+···+cn=g
n
∏
k=1
(2(g−1−ck)
dk−ck
).
The ﬁrst of these equalities will follow from theorem 6.6 below since by
base changeH•(δα)x is equal to the cohomology of the ﬁbreF = f−1α (x)
of the Abel-Jacobi morphismfα :Cd1×···× Cdn→X. The second equality
rests on a computation of Betti polynomials, see corollary 6.8.
6.3. Computations in the symmetric product
In this section we compute some intersection numbers of cycle classes
in the cohomology ring of the symmetric products ofC that will be needed
in the proof of theorem 6.6 below. For d∈ N consider the Abel-Jacobi
morphismhd : Cd→ X = JC as before. We will always work with rational
140 Chapter 6 – The generic rank of Brill-Noether sheaves
cohomology unless otherwise stated, so we putH•(−) =H•(−,Q). Fixing
a pointp∈C(C) we have embeddings{p} ↪→C ↪→C2 ↪→··· ↪→Cd−1 ↪→Cd
given by addition ofp. Via the last embedding, let
x = [Cd−1]∈ H2(Cd)
be the fundamental class ofCd−1. Since the cup product in cohomology
corresponds to the intersection of cycles, we havexa = [Cd−a] in H2a(Cd)
for a = 1, . . . ,d. We also put
θ = h∗
d [Θ]∈ H2(Cd)
where[Θ]∈ H2(X) denotes the class of a theta divisorΘ⊂ X. Since [Θ]
is a principal polarization, the integral cohomologyH1(X,Z)⊂ H1(X,Q)
admits a symplectic basisλ1, . . . ,λ2g, i.e. a basis such that using the cup
product onH•(X) we have
[Θ] =
g
∑
i=1
λi· λg+i .
Note that the construction of Jacobian varieties and the K¨unneth theorem
provide natural isomorphismsH1(X)∼= H1(C)∼= H1(Cd). So in the sequel
we will not distinguish notationally between the classesλ1, . . . ,λ2g∈H1(X)
and their images insideH1(C) or H1(Cd).
For any complex varietyZ we denote by degZ : H2dim(Z)(Z)−→Q
the degree isomorphism given by evaluation on the fundamental homology
class ofZ. For example, the classes
ηi = λi· λg+i for 1 ≤ i≤ g
satisfy degX(η1··· ηg) = degX([Θ]g/g!) = 1 by the Poincar´e formula. In
what follows it will be convenient to use the shorthand notation
ηI = ηi1··· ηic
for subsetsI ={i1, . . . ,ic}⊂{ 1, . . . ,g} of cardinality|I| = c, noting that
the ordering of the factors does not matter forηI since the cup product is
commutative in even degrees.
LEMMA 6.4. Let a,b,c∈ N0 with a+b +c = d, and let η∈ H2c(Cd)
be a monomial in the classesλ1, . . . ,λ2g. Then
degCd
(xa· θb· η) =
{(g−c
b
)·b! if η = ηI for some I,
0 otherwise.
Proof. SinceH1(Cd)∼= H1(X), any monomial inλ1, . . . ,λ2g∈ H1(Cd)
can be written as the pull-backη = h∗
d(µ) of some cohomology classµ
