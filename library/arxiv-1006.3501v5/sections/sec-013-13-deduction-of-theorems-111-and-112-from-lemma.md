---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-013-13-deduction-of-theorems-111-and-112-from-lemma
section_title: "Deduction of Theorems 11.1 and 11.2 from Lemma 11.3"
section_number: 13
pages: 55-59
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
13.1. Conventions. In this section, the symbol D2 denotes the unit disk in C with
counterclockwise orientation and S1 =∂D 2 is the unit circle with counterclockwise
orientation. Unless explicitly stated to the contrary, the torus S1×S1 and the solid
tori S1×D2 and D2×S1 are provided with the product orientations.
13.2. A surgery formula. Let Z : Cob 3→ vectk be a 3-dimensional TQFT over
a ﬁeld k. We establish a surgery formula for the values of Z on closed 3-manifolds.
Given a framed oriented link L =∪N
q=1Lq in S3, denote by EL its exterior,
i.e., the complement in S3 of an open regular neighborhood of L. We endow EL
with the orientation induced by the right-handed orientation of S3. There is a
homeomorphismf =fL from the disjoint union N (S1×S1) =∐N
q=1(S1×S1)q ofN
ordered 2-tori to ∂EL carrying theq-th copy of the torus to the boundary of a closed
regular neighborhood of Lq so thatf (S1×pt) is a positively oriented meridian of Lq
andf (pt×S1) is a positively oriented longitude of Lq determined by the framing for
q = 1,...,N . Observe that f is an orientation preserving homeomorphism N (S1×
S1)≃−∂EL. We use f to identify−∂EL andN (S1×S1). Then Z(−∂EL) = A⊗N ,
where A =Z(S1×S1). Consider the homomorphism
Z
(
EL,−∂EL,∅
)
:A⊗N =Z(−∂EL)→Z(∅) = k.
For any y1,...,y N∈A, set
Z(L;y1,...,y N ) = Z
(
EL,−∂EL,∅
)
(y1⊗···⊗ yN )∈ k.
Consider the solid torus V =−(S1×D2) with orientation opposite to the product
orientation. Then ∂V =S1×S1 in the category of oriented manifolds. Let w∈A =
Z(S1×S1) be the image of 1 ∈ k under the homomorphism Z(V,∅,∂V ) : k→A.
We call w the canonical vector associated with Z. Pick an arbitrary basis Y of the
vector space A and expand w =∑
y∈Y wyy where wy∈ k.
Lemma 13.1. Let M be a closed oriented 3-manifold obtained by surgery on S3
along a framed link L =L1∪···∪ LN⊂S3. For any orientation of L,
Z(M ) =
∑
y1,...,yN ∈Y
( N∏
q=1
wyq
)
Z(L;y1,...,y N ).
56 V. TURAEV AND A. VIRELIZIER
Proof. LetVN be a disjoint union of N copies of V . The associated homomorphism
Z(VN,∅,∂V N ) : k→A⊗N carries 1∈ k to
w⊗N =
∑
y1,...,yN ∈Y
( N∏
q=1
wyq
)
y1⊗···⊗ yN.
The 3-cobordism M = ( M,∅,∅) can be obtained by attaching the cobordism
(EL,−∂EL,∅) on top of the cobordism ( VN,∅,∂V N ) along the homeomorphism
f :∂VN =N (S1×S1)→−∂EL speciﬁed above. Therefore
Z(M,∅,∅) = Z(EL,−∂EL,∅)◦Z(VN,∅,∂V N ) : k→ k
and
Z(M ) = Z(M,∅,∅)(1) = Z(EL,−∂EL,∅)(
∑
y1,...,yN ∈Y
( N∏
q=1
wyq
)
y1⊗···⊗ yN )
=
∑
y1,...,yN ∈Y
( N∏
q=1
wyq
)
Z
(
EL,−∂EL,∅
)
(y1⊗···⊗ yN )
=
∑
y1,...,yN ∈Y
( N∏
q=1
wyq
)
Z(L;y1,...,y N ).
□
13.3. Link TQFTs. For any categoryB, we deﬁne a category LB of 3-cobordisms
withB-colored framed oriented links inside. The objects of LB are closed oriented
surfaces. A morphism Σ 0→ Σ 1 inLB is represented by a triple ( M,h,K ), where
M is a compact oriented 3-manifold, h is an orientation-preserving homeomorphism
(−Σ 0)⊔ Σ 1≃∂M , and K is aB-colored framed oriented link in M\∂M . (A link
K isB-colored if every component of K is endowed with an object of B called its
color.) Two such triples ( M,h,K ) and (M ′,h ′,K ′) represent the same morphism if
there is an orientation-preserving homeomorphism F : M→M ′ such that h′ =Fh
andK ′ =F (K) in the class of B-colored framed oriented links. The composition of
morphisms inLB is deﬁned via the gluing of cobordisms and the tensor product in
LB is deﬁned via disjoint union. This turns LB into a symmetric monoidal category.
The links in question may be empty so that the category Cob 3 of Section 9.1 is a
subcategory ofLB.
By a link TQFT we mean a symmetric monoidal functor Z :LB→ vectk. We
establish a version of Lemma 13.1 for such a Z. Consider disjoint framed oriented
linksK andL =∪N
q=1Lq inS3 and assume that K isB-colored. Then K lies in the
exterior EL of L. As in Section 13.2, Z(−∂EL) = A⊗N , where A = Z(S1×S1).
For any y1,...,y N∈A, set
Z(K,L ;y1,...,y N ) = Z
(
(EL,K ),−∂EL,∅
)
(y1⊗···⊗ yN )∈ k,
where the pair ( EL,K ) is viewed as a morphism −∂EL→∅ inLB. Let M be the
closed oriented 3-manifold obtained from S3 by surgery along L. Then K⊂EL⊂
M is aB-colored framed oriented link in M .
Lemma 13.2. Let Y be any basis of A and w =∑
y∈Y wyy∈A be the canonical
vector. Then
Z(M,K ) =
∑
y1,...,yN ∈Y
( N∏
q=1
wyq
)
Z(K,L ;y1,...,y N ).
ForK =∅, we recover Lemma 13.1. The proof of Lemma 13.2 repeats that of
Lemma 13.1 with the obvious changes.
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 57
13.4. The link TQFT |·| C. Fix a spherical fusion category C over an algebraically
closed ﬁeld k such that dimC⁄= 0. The results of Section 12 allow us to extend the
TQFT|·| C : Cob 3→ vectk of Section 9 to a link TQFT LZ(C)→ vectk, whereZ(C)
is the center of C. On surfaces and 3-cobordisms with empty links these TQFTs
are equal. In general, the construction follows the same lines as in Se ctions 9.3
and 9.4 but involves 3-cobordisms with Z(C)-colored framed oriented links inside.
The resulting link TQFT is also denoted |·| C.
Let 0∈D2 be the center of D2. For any j∈ Ob(Z(C)), denote by U j the solid
torus D2×S1 endowed with the j-colored framed oriented knot {0}× S1 whose
orientation is induced by that of S1 and whose framing is constant, i.e., determined
by a non-zero tangent vector of D2 at 0. Clearly, ∂U j =S1×S1 so that the link
TQFT|·| C produces a vector
yj =|U j,∅,∂U j|C∈A =|S1×S1|C.
By M¨ uger’s theorem (Theorem 10.3), the categoryZ(C) is modular and anomaly
free. We ﬁx a (ﬁnite) representative set J of simple objects of Z(C).
Lemma 13.3. The set Y = (yj)j∈J is a basis of the vector space A. The canonical
vectorw∈A expands as w = (dim(C))−1∑
j∈J dim(j)yj .
Proof. Consider the framed oriented Hopf link K∪L ⊂ S3 whose components
K, L have framing 0 and linking number 1. Endow K with a color i∈J . The
deﬁnitions of Section 13.3 applied to the link TQFT |·| C yield a k-linear map
A→ k,y↦→|K,L ;y|C∈ k. We compute the value of this map on yj∈A forj∈J .
Since the gluing of D2×S1 to the exterior EL of L along the homeomorphism
fL : S1×S1→∂EL yields S3, the functoriality of |·| C implies that
|K,L ;yj|C =|((EL,K ),−∂EL,∅)|C(yj) =|S3,H i,j|C,
where Hi,j = K∪L is the framed oriented Hopf link whose components K,L are
colored with i,j respectively. Formula (17) gives then
|K,L ;yj|C = (dim(C))−1FZ(C)(Hi,j) = (dim(C))−1Si,j,
where [Si,j ]i,j∈J is the S-matrix ofZ(C). By the deﬁnition of a modular category,
this matrix is non-degenerate. Hence the vectors ( yj)j are linearly independent. By
Lemma 11.3, dim A = dimτZ(C)(S1×S1). By [Tu], dim τZ(C)(S1×S1) = cardJ .
Therefore dimA = cardJ and the set Y = (yj)j∈J is a basis of A.
Consider theZ(C)-colored framed oriented link H +
i,j =K +∪L+⊂S3 obtained
from Hi,j by adding a positive twist to the framing of each component. Since L+
is an unknot with framing 1, the surgery on S3 along L+ gives S3. The knot K +
gives after this surgery an unknot in S3 with framing 0 and color i. Denote this
unknot by K i
0. By (17),
|S3,K i
0|C = (dim(C))−1FZ(C)(K i
0) = (dim(C))−1 dim(i).
On the other hand, Lemma 13.2 gives
|S3,K i
0|C =
∑
j∈J
wj|K +,L +;yj|C,
where w =∑
j∈J wjyj with wj∈ k for all j. As above,
|K +,L +;yj|C =|S3,H +
i,j|C = (dim(C))−1FZ(C)(H +
i,j ) = (dim(C))−1vivjSi,j,
where vk∈ k is the twist scalar of k∈J . Combining these equalities, we obtain
that for all i∈J ,
dim(i) =
∑
j∈J
wjvivjSi,j.
58 V. TURAEV AND A. VIRELIZIER
Since the S-matrix and the twist scalars are invertible, this system of equation s has
a unique solution. By [Tu], Chapter II, Formula (3.8.d),
dim(i) = (dim(C))−1∑
j∈J
dim(j)vivjSi,j.
Hence wj = (dim(C))−1 dim(j) for all j. □
13.5. Proof of Theorem 11.1. We shall prove that for any Z(C)-colored framed
oriented link K in a closed oriented 3-manifold M ,
(18) |M,K|C =τZ(C)(M,K ).
ForK =∅, this gives Theorem 11.1.
PresentM by surgery on S3 along a framed oriented link L =L1∪···∪ LN⊂S3.
Pushing K in the exterior EL of L in S3, we can assume that K⊂ EL. For any
j1,...,j N∈J , denote by L(j1,...,jN ) the link L whose components L1,...,L N are
colored with j1,...,j N respectively. We shall apply the notation of Section 13.3 to
the link TQFT Z =|·| C. Observe that
|K,L ;yj1,...,y jN|C =|S3,K∪L(j1,...,jN )|C.
This follows from the deﬁnitions, the functoriality of |·| C, and the fact that the
gluing of ∐N
q=1U jq to (EL,K ) along the homeomorphism fL : N (S1×S1)→∂EL
introduced in Section 13.2 yields the pair ( S3,K∪L(j1,...,jN )). By (17),
|S3,K∪L(j1,...,jN )|C = (dim(C))−1FZ(C)(K∪L(j1,...,jN )).
Applying Lemma 13.2 to Z =|·| C and the basis of |S1×S1|C given by Lemma 13.3,
we obtain
|M,K|C =
∑
j1,...,jN ∈J
( N∏
q=1
dim(jq)
dim(C)
)
|K,L ;yj1,...,y jN|C
=
∑
j1,...,jN ∈J
( N∏
q=1
dim(jq)
dim(C)
)
(dim(C))−1FZ(C)(K∪L(j1,...,jN ))
= (dim(C))−N −1 ∑
j1,...,jN ∈J
( N∏
q=1
dim(jq)
)
FZ(C)(K∪L(j1,...,jN ))
=τZ(C)(M,K ),
where the last equality is the deﬁnition of τZ(C)(M,K ) in [Tu].
13.6. Proof of Theorem 11.2. For a category B, we deﬁne a category GB of 3-
cobordisms withB-colored ribbon graphs inside, see [Tu] for a deﬁnition of colored
ribbon graphs. (Here we consider only ribbon graphs disjoint from t he bases of
cobordisms.) The category GB is deﬁned as LB replacing “framed oriented links”
with “ribbon graphs”. The category GB contains Cob 3 as a subcategory and is a
symmetric monoidal category in the obvious way. By a graph TQFT we mean a
symmetric monoidal functor GB→ vectk. In the rest of the argument B =Z(C).
The TQFT τZ(C) : Cob 3→ vectk extends to a graph TQFT GZ(C)→ vectk still
denotedτZ(C), see [Tu], Chapter IV. This TQFT is non-degenerate in the following
sense: the vector space τZ(C)(Σ) associated with any closed oriented surface Σ is
generated by the vectors τZ(C)(M,∅, Σ)(1), where M runs over all compact oriented
3-manifolds withZ(C)-colored ribbon graphs inside and with ∂M = Σ.
The TQFT |·| C : Cob 3→ vectk also can be extended to a graph TQFT. To do
this, one proceeds similarly to Section 12 by representing the ribbon graphs in a
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 59
3-manifold M by diagrams on a s-skeleton P of M . Then one deﬁnes a state sum
on such a diagram d as in Section 12. A typical coupon of d
PSfrag replacements
i
j k
l
m
f
A B C
D E
,
contributes to the state sum the factor
FC


PSfrag replacements
i
j k
l
m
f
A B C
D E


,
where the invariant FC ofC-colored knotted graphs in S2 is extended straightfor-
wardly (by the Penrose calculus) to C-colored ribbon graphs in S2. (In this example
of a coupon, A,B,C,D,E ∈ Ob(Z(C)), f∈ HomZ(C)(A⊗B⊗C∗,D ∗⊗E), and
i,j,k,l,m ∈I are the colors of the regions of d in P adjacent to the coupon.) The
resulting state sum is invariant under the moves Ω 1− Ω 8 (away from the coupons)
and under the moves pushing a coupon over or under a strand or ac ross an edge
ofP . Therefore the state sum in question yields an isotopy invariant of Z(C)-colored
ribbon graphs in M . The extension of |·| C toGZ(C) proceeds as in Sections 9.3, 9.4,
and 13.4 replacing “framed oriented links” with “ribbon graphs”. The resulting
graph TQFTGZ(C)→ vectk is still denoted |·| C.
We claim that there is a natural monoidal isomorphism of the functor sτZ(C) and
|·| C fromGZ(C) to vectk. Restricting both functors to Cob 3, we obtain the theorem.
Our claim follows from a general criterion establishing isomorphism of t wo TQFTs,
cf. [Tu], Chapter III, Section 3. Namely, if at least one of the TQFTs is non-
degenerate, the values of these TQFTs on cobordisms with empty b ases are equal,
and the vector spaces associated by these TQFTs with any closed o riented surface
have equal dimensions, then these TQFTs are isomorphic. Here by a TQFT we
mean a generalized TQFT incorporating graph TQFTs. The ﬁrst cond ition holds
because the graph TQFT τZ(C) is non-degenerate. That |M,K|C = τZ(C)(M,K )
for anyZ(C)-colored ribbon graph K in a closed oriented 3-manifold M is proven
along the same lines as Formula (18). The equality of dimensions is prov ided by
Lemma 11.3. This completes the proof of our claim and of the theorem .
