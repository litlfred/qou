---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI"
section_id: sec-003-rank-three
section_title: "Rank three"
section_number: null
pages: 11-23
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI — We classify connected ´ etale algebras A’s in pre-modular fusion categories B with rank(B) ≤"
---
structure or its fusion ring be multiplicity-free. The result implies all F ib’s are completely
anisotropic, giving another proof of the known fact [15].
2.3 Rank three
A rank three pre-MFC has three simple objects {1, X, Y }. As we reviewed above, with the as-
sumption of pivotal structure, there are ﬁve fusion rings, FR 3, 2
1 , FR3, 0
1 , FR3, 0
2 , FR3, 0
3 , K(1, 0, 2, 0).
The last with multiplicity is known [16] not to admit braiding. Thus, we clas sify connected
´ etale algebras in the ﬁrst four8 pre-MFCs.
2.3.1 B ≃ Vec1
Z/ 3Z
The pre-MFCs B’s have three simple objects {1, XhX , YhY } obeying Z/3Z fusion ring
⊗ 1 X Y
1 1 X Y
X Y 1
Y X
.
Hence, they have
FPdimB(1) = FPdim B(X) = FPdim B(Y ) = 1 ,
and
FPdim(B) = 3 .
8The fourth with fusion ring FR 3, 0
3 does not seem to have a common name. Thus, we call it psu(2)5
borrowing one famous realization.
11
The quantum dimensions dX, dY are solutions of d2
X = dY , d 2
Y = dX, d XdY = 1. The only
solution is
dX = dY = 1.
Thus, the pre-MFCs are unitary. Consequently, the pre-MFCs ha ve a unique categorical
dimension
D2(B) = 3 .
The nontrivial simple objects are dual to each other, X ∗ ∼= Y , and they have the same
conformal dimensions
hX = hY = 0, 1
3 , 2
3 (mod 1) .
This implies the pre-MFCs are always anomaly-free α = 1. (We have already speciﬁed this
fact in the name of this subsubsection.) Therefore, there are
3(conformal dimension hX = hY ) × 2(categorical dimension D(B) = ±
√
3) = 6
pre-MFCs with Z/3Z fusion ring. Among them, those with nontrivial conformal dimension s
are modular. There are four of them, consistent with [9]. We study all six pre-MFCs including
degenerate ones simultaneously.
In order to classify connected ´ etale algebras in our pre-MFCs, we ﬁrst ﬁnd an upper
bound on rank( BA). It is given by
rmax = 3. (2.8)
As we reviewed above, there are eight fusion categories which admit pivotal structures, but
the condition FPdim( BA) ≤ FPdim(B) = 3 narrows down to three with fusion rings
FR1, 0
1 , FR2, 0
1 , FR3, 2
1 .
The rank two fusion ring cannot solve (1.5), and is ruled out. This leav es only two candidates,
FR1, 0
1 , FR3, 2
1 . Let us study the two candidates in detail.
We start from the rank three candidate. It has FPdim( C) = 3, and demands FPdim B(A) =
1. This is nothing but the trivial connected ´ etale algebra A ∼= 1 giving BA ≃ B . Next, we
study the rank one candidate Vect C. It has FPdim = 1, and demands FPdim B(A) = 3. Since
any ´ etale algebras are self-dual [2], we are left with two possibilities, 1 ⊕ 1 ⊕ 1 or 1 ⊕ X ⊕ Y .
Connectedness of algebra rules out the ﬁrst. Thus, the only cand idate is A ∼= 1⊕X ⊕Y . This
is connected and separable, but it fails to be commutative depending on conformal dimen-
sions. Let us ﬁrst show those with nontrivial conformal dimensions are non-commutative.
We check the necessary condition (1.9). The relevant double-braid ings are given by
cX,X · cX,X ∼= e−2πih X idY , c Y,X · cX,Y ∼= e−4πih X id1, c Y,Y · cY,Y ∼= e−2πih Y idX.
(We used hX = hY .) The phases are nontrivial for nontrivial conformal dimensions hX =
hY = 1
3, 2
3 mod 1, and they fail to satisfy the necessary condition. Hence, th ey are non-
commutative. On the other hand, when the conformal dimensions a re trivial hX = hY = 0
12
mod 1, the phases become trivial, and they pass the necessary con dition. We thus need to
compute half-braidings cb,b ′’s. We ﬁnd 9
cX,X ∼= idY , c X,Y ∼= id1, c Y,Y ∼= idX .
Therefore, the candidate A ∼= 1 ⊕ X ⊕ Y is commutative for trivial conformal dimensions.
To summarize, we found
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 3 No
1 ⊕ X ⊕ Y for hX = hY = 0 (mod 1) VectC 1 No
.
T able 6: Connected ´ etale algebra in rank three pre-MFC B ≃ Vec1
Z/ 3Z
In other words, the pre-MFCs Vec 1
Z/ 3Z’s with nontrivial conformal dimensions hX = hY = 1
3, 2
3
mod 1 are completely anisotropic.
2.3.2 B ≃ Ising
The pre-MFCs B’s have three simple objects {1, XhX , YhY } obeying the Ising fusion ring
⊗ 1 X Y
1 1 X Y
X 1 Y
Y 1 ⊕ X
.
Hence, they have
FPdimB(1) = 1 = FPdim B(X), FPdimB(Y ) =
√
2,
and
FPdim(B) = 4 .
It is known [17] that Ising fusion categories admit spherical struct ures and (non-degenerate)
braidings. (We will make the most of the non-degeneracy later.) The quantum dimensions
dX, dY are solutions of d2
X = 1, d XdY = dY , d 2
Y = 1 + dX, and there are two solutions
dX = 1, d Y = ±
√
2.
9Employing the known [9] associators F bi,b j ,b k
bl
= 1, one can easily solve hexagon equations to ﬁnd R-
matrices
RX,X
Y = RX,Y
1 = RY,X
1 = RY,Y
X = +1,
giving the half-braidings.
13
(The sign of dY ﬁxes the spherical structure.) The pre-MFCs with positive dY are unitary.
The pre-MFCs have a unique categorical dimension
D2(B) = 4 .
It is known that conformal dimensions take values
hX = 1
2 , h Y = ± 1
16 , ± 3
16 , ± 5
16 , ± 7
16 (mod 1) .
(The conformal dimension hX = 1
2 implies the rank two braided fusion subcategory generated
by {1, X} is isomorphic to sVec. Hence, an obvious Z/2Z algebra A ∼= 1 ⊕ X fails to be
commutative because cX,X ∼= −id1.) Therefore, there are
2(quantum dimension dY )×8(conformal dimension hY )×2(categorical dimension D(B)) = 32
pre-MFCs. Those with dY = +
√
2 are unitary, and there are 16 of them, consistent with [9].
We search for connected ´ etale algebras in all 32 pre-MFCs simultan eously. Since the method
is the same, we will be brief.
The Frobenius-Perron dimension FPdim( B) = 4 gives an upper bound
rmax = 4. (2.9)
Since there are no complete list of fusion categories up to rank four , here we practically have
to assume fusion rings of BA’s be multiplicity-free. Then, there are seven 10 fusion rings, but
only ﬁve
FR1, 0
1 , FR2, 0
1 , FR3, 0
1 , FR4, 0
1 , FR4, 2
1
satisfy the three conditions. Let us check which of them satisfy ax ioms.
We start from those with FPdim = 4. The relation (1.5) requires FPdim B(A) = 1. For
such an algebra to be connected, the only possibility is the trivial one A ∼= 1 giving BA ≃ B .
(This rules out rank four BA’s.) Next, let us see the rank one scenario. One ﬁnds there is
no one-dimensional NIM-rep, and the fusion ring FR 1, 0
1 is ruled out. Finally, let us study
the last candidate FR 2, 0
1 . The scenario demands FPdim B(A) = 2. For such an algebra to be
connected, the only possibility is A ∼= 1 ⊕ X. Indeed, this is an algebra, 11 however, it fails
to be commutative because X is a fermion cX,X ∼= −id1. Thus, we do not get new connected
´ etale algebra from the rank two scenario.
To summarize, we found
10We could take the rank three fusion ring with multiplicity into account, but it is ruled out because
FPdim > FPdim(B) = 4.
11An easiest way to see this fact is to realize that X generates anomaly-free Z/ 2Z symmetry in physical
systems.
14
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 3 No
T able 7: Connected ´ etale algebra in rank three pre-MFC B ≃ Ising
regardless of quantum dimension dY , conformal dimension hY , or categorical dimension D(B).
The result motivates the
Theorem. All B ≃ Ising’s are completely anisotropic.
Proof. So far, we pretended we do not know B ≃ Ising be modular. However, as we
recalled above, they are known to be modular [17]. Thus, we can emplo y further constraints.
When the ambient category B is modular, it is known [5, 2] that the category of dyslectic
modules B0
A for connected ´ etale algebraA is modular obeying
FPdim(B0
A) = FPdim(B)
(FPdimB(A))2 ,
e2πic (B)/ 8 = e2πic (B0
A)/ 8.
(2.10)
Here, the full subcategory B0
A of BA consists of dyslectic modules ( m, p) ∈ B A such that
p · cA,m · cm,A = p. Since B0
A ⊂ B A, we also have
rank(B0
A) ≤ rank(B) ≤ ⌊FPdim(B)⌋.
In our example, we learn the maximal rank of B0
A is four. Fortunately, MFCs up to rank four
are completely classiﬁed [18, 9]. 12 According to the lists, the only MFCs which can match
the (additive) central charges are Ising MFCs. Since the MFCs hav e FPdim = 4, it demands
B0
A ≃ B A ≃ B , and FPdim B(A) = 1. Therefore, the only connected ´ etale algebra is the trivial
one A ∼= 1, showing B ≃ Ising be completely anisotropic. □
Remark. We have already included the theorem in the Table 7.
Remark. Some Ising MFCs are realized by Wess-Zumino-Witten (WZW) models:
Unitary Ising w/ hY (mod 1) Realization
3/16 ˆsu(2)2
5/16 ˆsp(4)1
7/16 ˆso(7)1
15/16 ( ˆe8)2
.
12See also [19] for classiﬁcation of MFCs at rank ﬁve.
15
Connected ´ etale algebras in MFCs C(g, k) describing ˆgk WZW models are especially called
quantum subgroups [20]. They have been studied extensively, and m any results are known.
Such connected ´ etale algebras were classiﬁed in [5] (for ˆsu(2)k), in [21] (for ˆsu(3)k), in [22]
(for ˆsu(4)k), and many more in [23] (see also [24]). Thus, the classiﬁcation resu lts for some
Ising MFCs are known. Our results are consistent with them. 13 However, we could not
ﬁnd a literature classifying connected ´ etale algebras in the other I sing MFCs (in particular,
non-unitary ones). Our results for those MFCs would be new. This e xample demonstrates
a uniﬁed nature of our method; since what is central in our method is the Frobenius-Perron
dimensions, it allows us to classify connected ´ etale algebras in pre-M FCs (or more generally
BFCs) with the same fusion ring – including degenerate and non-(pse udo-)unitary ones –
simultaneously.
2.3.3 B ≃ Rep(S3)
The pre-MFCs B’s have three simple objects {1, XhX , YhY } obeying the fusion ring
⊗ 1 X Y
1 1 X Y
X 1 Y
Y 1 ⊕ X ⊕ Y
.
Hence, they have
FPdimB(1) = 1 = FPdim B(X), FPdimB(Y ) = 2 ,
and
FPdim(B) = 6 .
The quantum dimensions dX, dY are (nonzero) solutions to d2
X = 1 , d XdY = dY , d 2
Y =
1 + dX + dY , and there are two of them
dX = 1, d Y = −1, 2.
13For ˆsu(2)2, BA corresponds to the A3 Dynkin diagram. Thus, the category BA has three simple objects,
implying A ∼= 1. For ˆsp(4)1 and ˆso(7)1, they do not admit exotic quantum subgroups. That is, all nontrivia l
algebras are their centers Z/ 2Z. However, simple objects generating them are fermions, and the Z/ 2Z algebras
fail to be commutative. Thus, they are also completely anisotropic. For ( ˆe8)2, its only nontrivial algebra is
the Z/ 2Z [23], but it is fermionic and fails to be commutative. Thus, the MFC is also completely anisotropic,
and our results are consistent.
Of course, the critical Ising model is described by an Ising MFC with hY = 1/ 16. The MFC is known (see,
e.g., [25]) to be completely anisotropic, and our results are consisten t. (The MFC has only one nontrivial
connected separable algebra A ∼= 1 ⊕ X, but since X is a fermion cX,X ∼= −id1, it fails to be commutative.)
See also [26] for classiﬁcation of connected ´ etale algebras in minima l models.
16
Accordingly, there are two categorical dimensions
D2(B) = 3 , 6.
As we reviewed in Appendix A, there are two classes of pre-MFCs with fusion ring K(Rep(S3)),
one non-symmetric, and another symmetric. The non-symmetric p re-MFCs have conformal
dimensions
hX = 0, h Y = 1
3 , 2
3 (mod 1)
with dY = 2, and symmetric pre-MFCs have
hX = hY = 0 (mod 1) .
Therefore, there are
2(sign of categorical dimension D(B)) × 2(hY = ±1
3 ) = 4
non-symmetric and
2(sign of categorical dimension D(B)) × 2(dY = −1, 2) = 4
symmetric pre-MFCs, eight in total. Since none of them is modular, th ey should not be
listed in MFCs, consistent with [9]. We classify connected ´ etale algebr as in all eight pre-
MFCs simultaneously.
First, since FPdim( B) = 6, the rank of categories of right A-modules is bounded from
above by
rmax = 6. (2.11)
Fusion categories up to rank six have been classiﬁed in [13, 14] assum ing multiplicity-free
fusion rings. In order to apply our method, for a moment, we assum e BA have multiplicity-free
fusion ring. Later, employing an improved method, we relax the assu mption and complete
the classiﬁcation of connected ´ etale algebras.
According to [12], we ﬁnd seven fusion rings
FR1, 0
1 , FR2, 0
1 , FR3, 2
1 , FR3, 0
2 , FR4, 2
2 , FR6, 2
1 , FR6, 4
1
can describe BA’s. The same analysis was done in [3], and we found only four
FR1, 0
1 , FR2, 0
1 , FR3, 2
1 , FR3, 0
2
can satisfy axioms. They correspond to candidates
A ∼= 1 ⊕ X ⊕ 2Y, 1 ⊕ Y, 1 ⊕ X, 1,
respectively. Which of them are connected ´ etale? The answer dep ends on conformal dimen-
sions, or non/symmetry of our ambient category. We start from t he non-symmetric ones.
17
Non-symmetric Rep (S3). In this case, the simple object Y has nontrivial braiding. The
ﬁrst two candidates fail to satisfy the necessary condition (1.9), 14 and we can safely discard
them. We do know the last two are connected ´ etale algebras.
Symmetric Rep (S3). In this case, the simple object Y also has trivial conformal dimen-
sion, and the candidates containing Y can be commutative. We have to check whether the
ﬁrst two satisfy axioms of commutative algebra. Naively, one has to solve associativity ax-
ioms, however, luckily, we do not need any computation. 15 The second candidate A ∼= 1 ⊕ Y
is known [29] to be connected ´ etale when dY = 2. 16 (They call it condensable or normal.)
Thus, we are left with the ﬁrst candidate A ∼= 1 ⊕ X ⊕ 2Y . Note that we are in a special sit-
uation; our ambient category is symmetric, and if A deﬁnes an algebra, it gives BA ≃ VectC.
Since the condensation gives a tensor functor F : B → B A, our question can be rephrased
as follows. Is a symmetric fusion category B ≃ Rep(S3) Tannakian? (A symmetric fusion
category admitting a braided tensor functor F : B → VectC is called Tannakian. Since our B
is symmetric and the only simple object of Vect C is the unit, a tensor functor is automatically
braided.) Once we have rewritten our problem in this form, we can imme diately answer it;
B ≃ Rep(S3) is Tannakian iﬀ it is positive [30, 1]. Recall a symmetric fusion category B is
called positive if ∀b ∈ B , db ∈ N×. Namely, A ∼= 1 ⊕ X ⊕ 2Y is connected ´ etale17 if dY = 2,
14They have double braidings
cA,A · cA,A ∼= (2 + 4e−4πih Y )ι· id1 · p + (2 + e−4πih Y )ι· idX · p + (8 + 4e−2πih Y )ι· idY · p,
and
cA,A · cA,A ∼= (1 + e−4πih Y )ι· id1 · p + e−4πih Y ι· idX · p + (2 + e−2πih Y )ι· idY · p,
respectively.
15In order to check the associativity axioms directly, one may use the method developed in [27] and
associators spelled out in, say, [28]. We checked the solution in [29] is consistent.
16The condition is needed because if dY = −1, the candidate has
dB(A) = dB(1) + dB(Y ) = 0 ,
a contradiction.
17The half-braidings are given by
cX,X ∼= id1, c X,Y ∼= idY , c Y,Y ∼= id1 + idX + idY .
One of the easiest ways to get these is as follows. First, since we kno w A ∼= 1 ⊕ Y is commutative, we learn
cY,Y ∼= id1 + idX + idY .
Then, one can easily solve hexagon equations to get the results abo ve. From the half-braidings, one immedi-
ately ﬁnds
cA,A ∼= 6
(
ι· id1 · p + ι· idX · p + 2ι· idY · p
)
∼= idA⊗A.
18
but not otherwise. Finally, for A ∼= 1 ⊕ X to be separable, we also need dY = 2. The reason
is as follows. In view of anyon condensation, Y ‘splits’ into two simple objects. Thus, simple
objects of BA are given by
1 ⊕ X, Y, Y.
They have quantum dimensions [5] dBA(c) = dB(c)
dB(A). Since the only rank three fusion category
with Frobenius-Perron dimension three is Vec 1
Z/ 3Z, for A to be separable, the three simple
objects should form Vec 1
Z/ 3Z. As we saw in section 2.3.1, simple objects of the fusion category
have quantum dimensions one. Thus, for A to give a fusion category, the simple objects need
to have quantum dimensions one. This condition is satisﬁed only when dY = 2.
So far, we assumed K(BA) be multiplicity-free. However, employing the improved method
[31], we can relax the assumption.
We work with an ansatz
A ∼= 1 ⊕ nXX ⊕ nY Y
with nj ∈ N. It has
FPdimB(A) = 1 + nX + 2nY .
For this to obey
1 ≤ FPdimB(A) ≤ FPdim(B)
resulting from (1.5), the natural numbers can take only 12 values
(nX , nY ) =(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2),
(3, 0), (2, 1), (1, 2), (4, 0), (3, 1), (5, 0).
The ﬁrst is nothing but the trivial connected ´ etale algebra A ∼= 1 giving B0
A ≃ B A ≃ B .
Among the other 11 candidates, ﬁve are ruled out by studying Frob enius-Perron dimensions.
The two candidates (nX, nY ) = (1 , 1), (3, 0) have FPdimB = 4, and demands FPdim( BA) = 3
2 .
However, there is no such fusion category, and the candidates ar e ruled out. Similarly, three
candidates ( nX, nY ) = (0 , 2), (2, 1), (4, 0) have FPdim B = 5, and demand FPdim( BA) = 6
5 ,
but there is no such fusion category. Thus, the three candidates are also ruled out. We are
left with six nontrivial candidates:
(nX , nY ) = (1 , 0), (0, 1), (2, 0), (1, 2), (3, 1), (5, 0).
Regardless of conformal dimensions, three of them, ( nX , nY ) = (2 , 0), (3, 1), (5, 0) or A ∼=
1 ⊕ 2X, 1 ⊕ 3X ⊕ Y, 1 ⊕ 5X, are ruled out by detailed study.
A ∼= 1 ⊕ 2X. It has FPdim B(A) = 3, and demands FPdim( BA) = 2. With the free module
functor FA := − ⊗ A : B → B A, we ﬁnd candidate simple objects of BA:
1 ⊕ 2X, 2 ⊕ X, 3Y.
They have Frobenius-Perron dimensions 1, 1, 2, respectively. Their contributions to FPdim( BA)
exceed two, and the candidate is ruled out.
19
A ∼= 1 ⊕ 3X ⊕ Y . It has FPdim B(A) = 6, and demands FPdim( BA) = 1. The candidate
simple objects of BA are given by
1 ⊕ 3X ⊕ Y, 3 ⊕ X ⊕ Y, . . . .
There exists additional simple objects, but their presence does no t aﬀect the following dis-
cussion. Their contributions to FPdim( BA) exceed one, and the candidate is ruled out.
A ∼= 1 ⊕ 5X. It has FPdim B(A) = 6, and demands FPdim( BA) = 1. We obtain candidate
simple objects (assuming the smallest Frobenius-Perron dimensions )
1 ⊕ 5X, 5 ⊕ X, 3Y.
They have FPdim BA = 1 , 1, 1, and their contributions to FPdim( BA) exceed one. Thus, the
candidate is also ruled out.
Now, we are only left with three nontrivial candidates
(nX, nY ) = (1 , 0), (0, 1), (1, 2).
We have seen that these give nontrivial connected ´ etale algebras depending on quantum
and conformal dimensions. From this analysis, we succeeded to rela x the assumption of
multiplicity on K(BA).
To summarize, we found
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 3 No
1 ⊕ X Vec1
Z/ 3Z 3 No
T able 8: Connected ´ etale algebra in rank three non-symmetric pre-M FC B ≃ Rep(S3)
for non-symmetric, and
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 3 No
1 ⊕ X for dY = 2 Vec1
Z/ 3Z 3 No
1 ⊕ Y for dY = 2 Vecα
Z/ 2Z 2 No
1 ⊕ X ⊕ 2Y for dY = 2 VectC 1 No
T able 9: Connected ´ etale algebra in rank three symmetric pre-MFC B ≃ Rep(S3)
for symmetric B ≃ Rep(S3). Thus, two symmetric ones with dY = −1 are completely
anisotropic, while the other six B ≃ Rep(S3)’s fail to be completely anisotropic.
20
2.3.4 B ≃ psu(2)5
The pre-MFCs B’s have three simple objects {1, XhX , YhY } obeying the fusion ring FR 3, 0
3
⊗ 1 X Y
1 1 X Y
X 1 ⊕ Y X ⊕ Y
Y 1 ⊕ X ⊕ Y
.
Hence, they have
FPdimB(1) = 1 , FPdimB(X) = sin 2π
7
sin π
7
≈ 1.802, FPdimB(Y ) = sin 3π
7
sin π
7
≈ 2.247,
and
FPdim(B) = 7
4 sin2 π
7
≈ 9.3.
The quantum dimensions dX, dY are solutions of d2
X = 1 + dY , d 2
Y = 1 + dX + dY , d XdY =
dX + dY . There are three solutions
(dX, dY ) = ( sin π
7
cos π
14
, − sin 2π
7
cos π
14
), (− sin 3π
7
cos 3π
14
, sin π
7
cos 3π
14
), ( sin 2π
7
sin π
7
, sin 3π
7
sin π
7
),
and categorical dimensions
D2(B) = 7
4 cos2 π
14
, 7
4 cos2 3π
14
, 7
4 sin2 π
7
,
respectively. The pre-MFCs have conformal dimensions
(hX, hY ) =



( 3
7, 1
7 ), ( 4
7, 6
7) (1st quantum dimensions) ,
( 2
7, 3
7 ), ( 5
7, 4
7) (2nd quantum dimensions) ,
( 1
7, 5
7 ), ( 6
7, 2
7) (3rd quantum dimensions) ,
(mod 1) (2.12)
respectively. Therefore, there are
3(quantum dimension) ×2(sign of categorical dimension D(B))×2(conformal dimension) = 12
pre-MFCs. (Actually, they are all modular. See the lemma in Appendix B.) Those with the
third quantum dimensions are unitary, and there are four of them, consistent with [9]. We
study connected ´ etale algebras in all 12 MFCs.
21
As the ﬁrst step, we ﬁnd an upper bound
rmax = 9 (2.13)
on rank(BA).18 According to [12], we ﬁnd BA can have only two fusion rings (assuming K(BA)
be multiplicity-free)
FR1, 0
1 , FR3, 0
3 .
The second scenario requires FPdim B(A) = 1. For such a candidate to be connected, the
only candidate is A ∼= 1. This is the trivial connected ´ etale algebra giving BA ≃ B . To check
the ﬁrst candidate with rank one, we search for one-dimensional N IM-reps. One ﬁnds no
solution, ruling out the possibility of rank one BA.
To summarize, we found
Connected ´ etale algebraA BA rank(BA) Lagrangian?
1 B 3 No .
T able 10: Connected ´ etale algebra in rank three pre-MFC B ≃ psu(2)5
The result motivates the
Theorem. All B ≃ psu(2)5’s are completely anisotropic.
Proof. As we recalled above, all pre-MFCs are actually modular. Thus, the a lgebra should
obey (2.10). Since FPdim( B0
A) ≥ 1, we obtain an inequality 19
1 ≤ (FPdimB(A))2 ≤ FPdim(B). (2.14)
18Actually, we can do a little more. We can show a
Lemma. An upper bound on rank (B0
A) is eight. Namely, rank (B0
A) cannot be nine.
Proof. Assume the opposite, and suppose rank( B0
A) = 9. Then, it is either pointed or non-pointed. If it
is pointed, we only have two possibilities, B0
A ≃ Vec1
Z/ 9Z, Vec1
Z/ 3Z×Z/ 3Z. The MFCs with such fusion rings
cannot match the additive central charges. Thus, we are left with non-pointed possibilities. A rank nine
non-pointed fusion category C with FPdim( C) ≤ FPdim(B) = 7
4 sin2 π
7
is strongly constrained. Since it is
non-pointed, there exists a non-invertible object c ∈ C with FPdim C(c) > 1. It enters the Frobenius-Perron
dimension by squared sum, FPdim( C) ≡ ∑ 9
i=1(FPdimC(ci))2 = (FPdim C(c))2 + · · · . Since any object has
FPdimC(ci) ≥ 1, ∑
ci⁄=c(FPdimC(ci))2 ≥ 8, and we must have 1 < FPdimC(c) < 2, or the squared sum
reaches ten. Here, it is known [4] that such Frobenius-Perron dim ension is expressed as FPdim C = 2 cos π
n
for a natural number n larger than three ( n = 3 is ruled out by our assumption FPdim C > 1). Since
the function is monotonically increasing, the smallest Frobenius-Per ron dimension is achieved when n = 4,
or FPdim C =
√
2. The Frobenius-Perron dimensions of such fusion categories exc eed the upper bound
FPdim(B) = 7
4 sin2 π
7
≈ 9. 3, leading to a contradiction. □
19We thank Victor Ostrik for teaching us an upper bound on FPdim B(A) in the related work [3].
22
The most general candidate can be written as
A ∼=
rank(B)⨁
j=1
njbj
with nj ∈ N. In order to get connected algebra, we set nj = 1 for bj ∼= 1 at the outset. The
candidate in our example thus has
FPdimB(A) = 1 + 1
sin π
7
(
nX sin 2π
7 + nY sin 3π
7
)
.
For this to obey (2.14), there are only two possibilities
(nX , nY ) = (0 , 0), (1, 0).
The ﬁrst candidate is nothing but the trivial connected ´ etale algeb ra A ∼= 1 giving B0
A ≃
BA ≃ B . The second candidate means A ∼= 1 ⊕ X. It has double braiding
cA,A · cA,A ∼= (1 + e−4πih X )ι · id1 · p + 2ι · idX · p + e2πi (hY −2hX )ι · idY · p.
Since X has nontrivial conformal dimensions, the candidate fails to satisfy the necessary
condition (1.9), and it is ruled out. □
Remark. We have already included the theorem in the Table 10.
