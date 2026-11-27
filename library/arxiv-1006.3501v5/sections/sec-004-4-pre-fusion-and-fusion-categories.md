---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-004-4-pre-fusion-and-fusion-categories
section_title: "Pre-fusion and fusion categories"
section_number: 4
pages: 10-13
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
4.1. Pre-fusion categories. An object X of a monoidal k-categoryC is simple
if End C(X) is a free k-module of rank 1. Equivalently, X is simple if the k-ho-
momorphism k→ EndC(X), k↦→k idX is an isomorphism. By the deﬁnition of a
monoidal k-category, the unit object 1 is simple. In the literature, simple objects
in our sense are often called absolutely simple objects or scalar obje cts.
A pre-fusion category (over k) is a pivotal k-categoryC such that
(a) Any ﬁnite family of objects of C has a direct sum in C;
(b) Each object of C is a ﬁnite direct sum of simple objects;
(c) For any non-isomorphic simple objects i,j ofC, we have Hom C(i,j ) = 0.
Conditions (b) and (c) imply that all the Hom spaces in C are free k-modules of
ﬁnite rank. The multiplicity of a simple object i in any X∈ Ob(C) is the integer
N i
X = rank k HomC(X,i ) = rank k HomC(i,X )≥ 0.
This integer depends only on the isomorphism classes of i and X.
A set I of simple objects of a pre-fusion category C is representative if 1∈I and
every simple object ofC is isomorphic to a unique element of I. Condition (b) above
implies that for such I and any X∈ Ob(C), there is a ﬁnite family of morphisms
(pα :X→iα,q α : iα→X)α∈Λ inC such that
idX =
∑
α∈Λ
qαpα, i α∈I, and pαqβ =δα,β idiα for all α,β∈ Λ,
where δα,β is the Kronecker symbol. Such a family ( pα,q α)α∈Λ is called an I-
partition of X. For i∈I, set Λ i = Λ i
X ={α∈ Λ|iα =i}. Then ( pα : X→i)α∈Λ i
is a basis of Hom C(X,i ) and (qα : i→X)α∈Λ i is a basis of Hom C(i,X ). Therefore
#Λ i =N i
X , #Λ = ∑
i∈IN i
X , and dim(X) =∑
i∈I dim(i)N i
X .
Lemma 4.1. LetC be a pre-fusion category. Then:
(a) C is non-degenerate;
(b) The left and right dimensions of any simple object of C are invertible in k;
(c) C is spherical if and only if diml(i) = dim r(i) for any simple object i ofC.
Proof. Let I be a representative set of simple objects of C. Pick X∈ Ob(C) and
an I-partition (pα : X→iα,q α : iα→X)α∈Λ of X. For any endomorphism f of X
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 11
and α∈ Λ, we have pαfq α =λαidiα for some λα∈ k. Then
trl(f ) = tr l(f
∑
α∈Λ
qαpα) = tr l(
∑
α∈Λ
pαfq α) =
∑
α∈Λ
λα diml(iα)
and similarly tr r(f ) =∑
α∈Λ λα dimr(iα). This implies Claim (c).
The families ( p∗
α : 1∗ = 1→ X ∗)α∈Λ 1 and (qα : 1→ X)α∈Λ 1 are bases of the
modules Hom C(1,X ∗) and Hom C(1,X ), respectively, where Λ 1 ={α∈ Λ|iα = 1}.
The pairing ωX between these modules deﬁned in Section 2.4 is non-degenerate
because ωX (p∗
α⊗qβ) = ev X (p∗
α⊗qβ) = pαqβ = δα,β for all α,β ∈ Λ 1. This
implies (a).
Let i be a simple object of C. Then N 1
i∗⊗i = 1 and so there are morphisms
p : i∗⊗i→ 1 andq : 1→i∗⊗i such that HomC(i∗⊗i, 1) = k·p, HomC(1,i ∗⊗i) = k·q,
and pq = id 1 = 1∈ k. Since i is a simple object, ev i is a basis of Hom C(i∗⊗i, 1)
and ~coevi is a basis of Hom C(1,i ∗⊗i). Therefore ev i =λp and ~coevi =µq for some
invertibleλ,µ∈ k. Hence dim l(i) = ev i~coevi =λµpq =λµ is invertible. Since i∗ is
simple, dim r(i) = dim l(i∗) is invertible. This proves Claim (b). □
For sphericalC, we can consider the invariant FC ofC-colored graphs in S2, see
Section 3.3. The following lemma provides useful local relations for FC.
Lemma 4.2. LetC be a spherical pre-fusion category and let I be a representative
set of simple objects of C.
(a) For any i,j∈I,
FC

PSfrag replacements
i
j
vv′

 =δi,j FC

PSfrag replacements i
jvv′

 .
(b) For any i,j∈I,
FC

PSfrag replacements
i
j
vv′

 =δi,j (dim(i))−1 FC

PSfrag replacementsi
jvv′

⊗ FC

PSfrag replacements i
jvv′

.
(c) FC

PSfrag replacements
iuv

 =
∑
i∈I
dim(i)∗u,v FC

PSfrag replacements i u
v

.
(d) FC


PSfrag replacements
uv

 =∗u,v FC


PSfrag replacements
u
v

.
In (b) and (d) the empty rectangles stand for pieces of C-colored graphs sitting
inside the rectangles. The same C-colored graphs appear on both sides of the
equalities. The relations (a) and (b) can be applied only when there ar e other
vertices (not shown in the picture) on the single strand on the right -hand side.
For the deﬁnition of ∗u,v in (c), (d), see Section 3.1; here the duality between the
verticesu andv is induced by the symmetry with respect to a horizontal line. Note
that for any choice of colors of the strands on the left-hand side o f (c), the sum on
the right-hand side has only a ﬁnite number of non-zero terms.
Proof. Claims (a) and (b) follow from the equalities Hom C(i,j ) = 0 for i⁄=j and
f = (dim(i))−1 tr(f ) idi for any f ∈ EndC(i). Claim (d) follows from (c) since
HomC(1,i ) = 0 for i⁄= 1. Let us prove (c). Let S = ((X1,ε 1),..., (Xn,ε n)) be the
tuple of signed objects of C determined by the strands on the left-hand side of (c).
12 V. TURAEV AND A. VIRELIZIER
LetX =XS∈ Ob(C) be deﬁned by Formula (5). Let ( pα : X→iα,q α : iα→X)α∈Λ
be an I-partition of X. For i∈I, set Λ i ={α∈ Λ|iα = i} and denote by Si the
(n + 1)-tuple of signed objects ( i,−)S. The families
(eα = (id X ∗⊗pα) ~coevX )α∈Λ i and ( fα = (id i∗⊗qα) ~coevi)α∈Λ i
are bases of the modules Hom C(1,X ∗⊗i) and Hom C(1,i ∗⊗X) = Hom C(1,X Si),
respectively. Recall the isomorphism ψS∗ : XS∗→ X ∗
S = X ∗ deﬁned in the proof
of Lemma 2.3. Then ( e′
α = (ψ−1
S∗⊗ idi)(eα))α∈Λ i is a basis of Hom C(1,X S∗⊗i) =
HomC(1,X S∗
i ). Recall from Section 2.3 the evaluation form
ω =ωSi : Hom C(1,X S∗
i )⊗ HomC(1,X Si)→ k.
A direct computation gives ω(e′
α⊗fβ) = δα,β dim(i) for all α,β ∈ Λ i. The inverse
of ω is the tensor (dim( i))−1∑
α∈Λ ifα⊗e′
α written shortly as Ω i⊗ Ω ′
i. We have
∑
i∈I
dim(i)
PSfrag replacements
i
XS
XS
XS∗
EvS∗
ψ−1
S∗
ψS
Ω ′
i Ω ipα
qα
=
∑
α∈Λ
PSfrag replacements
i
XS XS
XSXS∗
EvS∗
ψ−1
S∗ψS
Ω ′
i
Ω i
pα qα
iα
=
∑
α∈Λ
qαpα = id XS.
This formula and the deﬁnition of the contraction maps imply (c). □
4.2. F usion categories. By a fusion category , we mean a pre-fusion category C
such that the set of isomorphism classes of simple objects of C is ﬁnite. A standard
example of a fusion category is the category of ﬁnite rank represe ntations (over k)
of a ﬁnite group whose order is relatively prime to the characteristic of k. The
category of representations of an involutory ﬁnite dimensional Ho pf algebra over a
ﬁeld of characteristic zero is a fusion category. For more examples , see [ENO].
A representative set I of simple objects of a fusion category C is ﬁnite. The
following sum does not depend on the choice of I and is called the dimension ofC:
dim(C) =
∑
i∈I
diml(i) dimr(i)∈ k.
By [ENO], if k is an algebraically closed ﬁeld of characteristic zero, then dim(C)⁄= 0.
For sphericalC, we have dim(C) =∑
i∈I (dim(i))2.
Lemma 4.3. Let I be a representative set of simple objects of a spherical fusi on
categoryC. Then for all X,Y ∈ Ob(C),
∑
k,l∈I
dim(k) dim(l)N 1
X⊗k⊗Y ⊗l = dim(X) dim(Y ) dim(C)
and ∑
j,k,l∈I
dim(k) dim(l)N 1
j⊗k⊗j∗⊗l = (dim(C))2.
Proof. We have
∑
k,l∈I
dim(k) dim(l)N 1
X⊗k⊗Y ⊗l =
∑
k∈I
dim(k)
∑
l∈I
dim(l∗)N l∗
X⊗k⊗Y
=
∑
k∈I
dim(k)
∑
m∈I
dim(m)N m
X⊗k⊗Y =
∑
k∈I
dim(k) dim(X⊗k⊗Y )
= dim(X) dim(Y )
∑
k∈I
(dim(k))2 = dim(X) dim(Y ) dim(C).
The second formula is a direct consequence of the ﬁrst one. □
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 13
4.3. The opposite category . Each monoidal category C determines the oppo-
site monoidal category Cop by reversing all the arrows (and keeping the tensor
product and the unit object). If C is pivotal with the evaluation/coevaluation
morphisms{evX, coevX,~evX, ~coevX}X∈Ob(C), thenCop is pivotal with the evalua-
tion/coevaluation morphisms
evop
X = ~coevX, coevop
X = ~evX, ~evop
X = coev X, ~coevop
X = ev X,
where X∈ Ob(Cop) = Ob(C). If C is a monoidal k-category (respectively, a spher-
ical k-category, a pre-fusion category, a fusion category), then so isCop.
