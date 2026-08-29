---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-027-51-natural-transformations-of--preserving-functo
section_title: "Natural Transformations of ∗-Preserving Functors"
section_number: 5.1
pages: 25-28
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
Proposition 5.1 Let D, K be ∗-categories and F : D → K a ∗-preserving functor. Let NatF be the set of all
natural transformations from F to itself, viz.
NatF = {b = (bX ∈ EndF (X), X ∈ D) | F (s) ◦ bX =bY ◦ F (s) ∀s :X →Y }.
Then with the following pointwise operations NatF is a unital ∗-algebra:
(λb +λ′b′)X = λbX +λ′b′
X,
(bb′)X = bX ◦ b′
X,
(b∗)X = ( bX )∗,
1X = idF (X),
for b,b ′ ∈ NatF, λ,λ′ ∈ C and X ∈ D.
Proof. If s ∈ Mor(X,Y ), then
F (s) ◦ (b∗)X = (bX ◦ F (s∗))∗ = (F (s∗) ◦ bY )∗ = (b∗)Y ◦ F (s),
where we have used F (s∗) = F (s)∗. Thus b∗ ∈ NatF . Similarly, we get bb′, λb +λ′b′ ∈ NatF , so with these
operations Nat F is a ∗-algebra. Obviously 1 is a unit for Nat F . ■
Definition 5.2 LetB be a ∗-algebra and K a ∗-category. Then the category RepKB of ‘representations of B
in K’ has as objects the pairs (X,πX ), where X ∈ Obj K and πX is a non-degenerate ∗-homomorphism of B
into EndX. The morphisms are given by
MorRepKB((X,πX ), (Y,πY )) = {s ∈ MorK(X,Y ) | s ◦ πX (b) = πY (b) ◦ s ∀b ∈B}.
Note that if K = H, the category of ﬁnite dimensional Hilbert spaces, we have End H = B(H). Thus our
deﬁnition reduces to the usual notion of ﬁnite dimensional non-deg enerate ∗-representations of B: Rep HB =
RepfB.
Proposition 5.3 Let C, K be ∗-categories and E : C → K a ∗-preserving functor. Deﬁne a unital ∗-algebra
B = Nat E. There is a ∗-preserving functor F : C → RepKB satisfying K ◦ F = E, where K : Rep KB →
K, (X,πX ) ↦→X is the forgetful functor.
25
Proof. We set F (X) = ( E(X),πX ) for X ∈ Obj C and F (s) = E(s) for the morphisms of C. Here the ∗-
representationπX is deﬁned by
πX : B → EndX, b ↦→bX.
That F really is a functor follows from
F (s) ◦ πX (b) = E(s) ◦ bX =bY ◦ E(s) = πY (b) ◦F (s) ∀s :X →Y ∀b ∈B,
where we used b ∈B = NatE. ■
Proposition 5.4 Let D be a semisimple ∗-category, K a ∗-category and F : D → K a ∗-preserving functor.
Then there is an isomorphism
ψF : Nat F →
∏
i∈ID
EndF (Xi)
of ∗-algebras.
Proof. We deﬁne a map ψF : NatF →∏
i∈ID EndF (Xi) by
ψF (b) =
∏
i∈ID
bXi
for all b ∈ NatF . Clearly ψF is a unital ∗-algebra homomorphism. We ﬁrst show that it is injective. Suppose
ψF (b) = 0, so bXi = 0 for all i ∈ ID. Let X ∈ D . We must show that bX = 0. Recall that, for any
i ∈ID, Mor(Xi,X ) is a Hilbert space with the inner product ( s,t )idXi =t∗s and that every s ∈ Mor(Xi,X ) is
a multiple of an isometry. Let siα ∈ Mor(Xi,X ), i ∈IC, α = 1,... , dim Mor(Xi,X ) be an orthonormal basis
w.r.t. this inner product satisfying ∑
iαsiα ◦ s∗
iα = idX . Hence
bX =bX ◦ F (idX ) =
∑
iα
bX ◦ F (si ◦ s∗
i ) =
∑
iα
F (si) ◦ bXi ◦ F (s∗
i ) = 0,
and injectivity of ψF follows.
Next we prove surjectivity of ψF . Given ( bi ∈ EndF (Xi), i ∈ ID) we need to construct b ∈ NatF such
that ψF (b) = ∏
i∈IDbi. Thus let X ∈ D . As above, pick a basis of isometries siα ∈ Mor(Xi,X ), i ∈ ID, with∑
iαsiα ◦ s∗
iα = idX . Deﬁne bX ∈ EndF (X) by
bX =
∑
iα
F (siα) ◦ bi ◦ F (s∗
iα).
Another choice of orthonormal bases (siα) in Mor(Xi,X ), i∈ID does not aﬀect bX since any two such bases are
related by an orthogonal transformation. It remains to show tha t b ∈ NatF , viz. F (s) ◦ bX =bY ◦ F (s) ∀s :
X →Y . To this purpose consider u ∈ Mor(X,Y ). Pick isometries tjβ ∈ Mor(Yj,Y ), with ∑
jβtjβ ◦ t∗
jβ = idY ,
and deﬁne bY ∈ EndF (Y ) by
bY =
∑
jβ
F (tjβ ) ◦ bj ◦ F (t∗
jβ ).
Then
F (u) ◦ bX =
∑
iα
F (u ◦ siα) ◦ bi ◦ F (s∗
iα) =
∑
iα,jβ
F (tjβ ◦ t∗
jβ ◦ u ◦ siα) ◦ bi ◦ F (s∗
iα).
But t∗
jβ ◦ u ◦ siα ∈ Mor(Xi,Xj) is zero unless i =j and otherwise a scalar multiple of id Xi . Hence
F (u) ◦ bX =
∑
iαβ
F (tiβ ◦ (t∗
iβ ◦ u ◦ siα)) ◦ bi ◦ F (s∗
iα) =
∑
iα,jβ
F (tjβ ) ◦ bj ◦ F (t∗
jβ ◦ u ◦ siα ◦ s∗
iα) = bY ◦ F (u).
26
The last identity in this equation follows by precisely the same sort of a rgument as used before. This proves the
naturality of the family b ∈ NatF . Obviously we have bXi =bi for all i ∈ID. Thus ψF (b) = ∏
i∈IDbi, which
proves surjectivity of ψF . ■
The isomorphism ψF depends on the chosen family Xi,i ∈I of irreducibles in C, but is canonical once the
latter is ﬁxed. Thus there is no risk in suppressing it and writing Nat F =∏
i∈ID EndF (Xi), as will be done in
the sequel.
Example 5.5 The simplest application of this proposition is to the identity D → D , when we get
Nat (Id) ∼
=
∏
i∈ID
C.
Examples of natural transformations of the identity are the ‘twist s’ appearing in the context of braided tensor
categories. ✷
Example 5.6 Suppose D is a tensor ∗-category with tensor product ⊗. A less trivial application of the
proposition is the case of the tensor functor F = ⊗ : D × D → D , where D × D is the product ∗-category. Note
that the isomorphism classes of irreducible objects in D × D are precisely ID ×ID. By semisimplicity of D we
have a ﬁnite decomposition
Xi ⊗Xj ∼
=
⨁
k∈ID
Nk
ijXk,
for any i,j ∈ID and thus End(Xi ⊗Xj) ∼
=⨁
k∈IDMN k
ij
(C). We therefore obtain
Nat ⊗ ∼
=
∏
i,j,k ∈ID
N k
ij⁄=0
MN k
ij
(C).
✷
The following example is a continuation of Example 5.5.
Example 5.7 Suppose C is a semisimple ∗-category. Consider the ∗-algebraA = ⊕i∈IC C. Then Proposition 5.3
provides an equivalence F : C → RepfA of categories such that F (Xi) ∼
=pi for all i ∈IC. Let K : RepfA → H
be the forgetful functor. Then K ◦ F is an embedding functor for C as a ∗-category. By Proposition 5.4 and
Example 5.5 we also conclude that
Nat(K ◦ F ) ∼
= NatId ∼
=
∏
i∈IC
C.
(Here of course, it does not make sense to say that the functors Id andK ◦F are unitarily equivalent.) Suppose
now that C is in addition a tensor category. Then the faithful functor K ◦ F cannot in general be monoidal.
To see this let Xi,Xj withi,j ∈IC. Then K ◦ F (Xi) ∼
=K(pi) ∼
= C, so K ◦ F (Xi) ⊗K ◦ F (Xj) ∼
= C, whereas
K ◦ F (Xi ⊗Xj) ∼
=
⨁
k∈IC
Nk
ij K ◦ F (Xk) ∼
=
⨁
k∈IC
Nk
ij C,
where we used the decomposition Xi ⊗Xj ∼
= ⊕k∈ICNk
ij Xk. ✷
27
Given a ∗-preserving functor E : C → K and writing B = NatE it is natural to ask under which conditions
the functor F : C → RepKB deﬁned in Proposition 5.3 is an equivalence of categories. Instead of pursuing this
line further we restrict ourselves to the case where C is semisimple and K = H. Then End E(X) is a ﬁnite
dimensional matrix algebra for every X ∈ C and Proposition 5.4 shows that Nat E is a direct product of matrix
algebras. The representation theory of such algebras is quite intr icate, cf. [13]. There it is shown, among other
results, that every irreducible representation of B =∏
i∈IB(Hi) is equivalent to a projection pi iﬀ the index
set I has less than measurable cardinality. In practice, this is no serious r estriction but for reasons which will
become clear in the next subsection we prefer to work with direct su ms instead of direct products.
Theorem 5.8 Let C be a semisimple ∗-category and E : C → H a ∗-preserving functor. The ∗-algebra A =
⊕i∈ICB(E(Xi)) embeds canonically into NatE ∼
=∏
i∈ICB(E(Xi)). The functor
F : C → RepfA, F (X) = (E(X),πX ), πX (a) = aX ∀a ∈A, F (s) = E(s)
satisﬁes K ◦ F =E. It gives rise to an equivalence of categories iﬀ E is faithful.
Proof. F as deﬁned above diﬀers from the functor deﬁned in Proposition 5.3 o nly in the restriction of the
representations πX to A ⊂ NatE. Thus it clearly is a ∗-preserving functor. By deﬁnition it is clear that
K ◦ F = E. Since F coincides with E on morphisms, E is faithful if F is an equivalence. Assume now that
E is faithful. Let X ∈ C be irreducible. Then F (X) is a representation πX : a ↦→aX of A on the Hilbert
space E(X). As is clear from the proof of Proposition 5.4, for X = Xi we have πX = pi, which clearly is
irreducible. Since a ∈A is a natural transformation, πX :a ↦→aX is an irreducible ∗-representation whenever
X is irreducible. Consider i ⁄= j,i,j ∈ IC. By Proposition 2.10, the projections pi = F (Xi),pj = F (Xj) are
inequivalent ∗-representations. By semisimplicity of Rep fA this implies that F is full. Since the pi,i ∈ IC
exhaust the equivalence classes of irreducible ∗-representations of A it is clear that F is essentially surjective,
completing the proof. ■
Remark 5.9 The theorem remains true if one replaces A by the direct product algebra Nat E provided one
makes the additional assumption that the set IC of isomorphism classes of C has less than measurable cardinality.
✷
