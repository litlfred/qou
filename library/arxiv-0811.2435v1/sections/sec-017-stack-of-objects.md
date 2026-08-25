---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-017-stack-of-objects
section_title: "Stack of objects"
section_number: null
pages: 48-53
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
In this section we assume that the ground ﬁeld k is perfect, i.e. the
k is a
Galois ﬁeld over k. Our goal in this section is to explain how to associate with
an ind-constructible A∞-categoryC over k an ordinary k-linearA∞-category
C(k), in such a way that ind-constructible equivalences will in duce the usual
equivalences. For any ﬁeld extension k′⊃ k (e.g. for k′ = k) one can deﬁne
A∞-categoryCnaive(k′) to be the small k′-linear category with the set of
objects given by (Ob(C))(k′) and obvious morphisms and compositions. This
48
is not a satisfactory notion because in the deﬁnition of the e quivalence we
demand only the surjectivity on isomorphism classes of obje cts over k. The
naive categoryCnaive(k) will be a full subcategory of the “correct” category
C(k). One should read carefully brackets, as in our notation
Ob(C(k))⁄= (Ob(C))(k) =: Ob(Cnaive(k)),
contrary to the case of k where we have
Ob(C(k)) = (Ob(C))(k).
We will see also the “set of isomorphism classes of objects” i nC should be
better understood as an ind-constructible stack 11.
Let k′ ⊂ k be a ﬁnite Galois extension of k and consider an element
E′ ∈ (Ob(C))(k′) ⊂ Ob(C(k)) such that σ(E) is isomorphic to E for all
σ∈ Gal(k′/k). We would like to deﬁne the descent data for such E′, which
should be data necessary to deﬁne an object in (not yet deﬁned ) k-linear
categoryC(k) which becomes isomorphic to E′ after the extension of scalars
from k to k′.
First, for a ﬁnite non-empty collection of objects ( Ei)i∈I of any A∞-
categoryC′ linear over a ﬁeld k′ (not necessarily a perfect one) we deﬁne
an identiﬁcation data for objects of this collection to be an A∞-functor Φ
from the A∞-categoryCI,k′ describing I copies of the same object:
Ob(CI) = I, Hom•(i,j ) = Hom 0(i,j )≃ k′
toC′. In plain terms, to give such a functor is to give a closed morp hism
of degree 0 for any pair of objects Ei,Ej (representing the identity id Ei in
H•(C(k)) for i =j), a homotopy for any triple of objects, homotopy between
homotopies for any quadruple of objects, etc. Thus, we in a se nse identify
all the objects of the collection ( Ei)i∈I and hence can treat it is a new object
(canonically isomorphic to all (Ei)i∈I), without choosing any speciﬁc element
i∈I.
Returning to the case of E′∈ (Ob(C))(k′), we deﬁne the descent data as
the identiﬁcation of the collection of objects ( σ(E′))σ∈Gal(k′/k) of the category
Cnaive(k′) equivariant with respect to the action of Gal( k′/k) acting both on
the collection and on the coeﬃcients in the identiﬁcation.
11Even in the case when k = k it is important to keep track on automorphisms groups
of objects (and not only on the set of isomorphism classes), e .g. for the correct deﬁnition
of the motivic Hall algebra in 6.1.
49
We deﬁne the set Ob(C(k)) of objects ofC(k) to be the inductive limit over
ﬁnite Galois extensions k′/k of descent data as above. Also one can deﬁne
morphisms and higher compositions. We leave the following P roposition
without a proof.
Proposition 6 There is a natural structure of a k-linear A∞-category on
C(k) containingCnaive(k) as a full subcategory. Any equivalence Φ : C1→C 2
in ind-constructible sense induces an equivalence C1(k) → C2(k). If C is
triangulated in ind-constructible sense then C(k) is also triangulated.
If E is an object of C(k) then any other object E′ ofC(k) which is iso-
morphic to E after the extension of scalars to C(
k) is in fact isomorphic to
E inC(k) (in other words, there are no non-trivial twisted forms). T he rea-
son is that (as follows directly from deﬁnitions) the set of s uch “ k-forms” of
E is classiﬁed by H 1(Gal(k/k),GE), where GE is a simplicial group associ-
ated with the A∞-algebra End•
C(k)(E,E ). There is a spectral sequence which
converges to this set and has the second term E2 = (Epq
2 ) given by
H 1(Gal(
k/k), (Ext0
C(
k)(E,E ))×) ,
H 2(Gal(k/k), Ext−1
C(k)(E,E )) ,
H 3(Gal(k/k), Ext−2
C(k)(E,E )),... .
We observe that all Galois cohomology groups with coeﬃcient s in Ext<0
C(k)(E,E )
are trivial (since Ext i
C(
k)(E,E ),i < 0 are just sums of copies of the addi-
tive group Ga(k)). Also the set H 1(Gal(k/k), (Ext0
C(
k)(E,E ))×) is the one-
element set, because for any ﬁnite-dimensional algebra A over k we have
H 1(Gal(k/k),A×) = 0 (a version of Hilbert 90 theorem, see also section 2.1
in [35]). One can deduce from the above spectral sequence an i mportant
corollary: the set of isomorphism classes of objects of C(k) is in a natural
bijection with the set of isomorphism classes of the usual de scent data in
category H•(C(k)) endowed with the strict action of Gal( k/k).
Finally, we will explain how to associate an ind-constructi ble stack to an
ind-constructible categoryC over k. First of all, we can always assume that
C satisﬁes the following axiom
A4) There exists a decomposition M =⊔i∈IXi into the countable disjoint
union of constructible sets over k such that any two isomorphic objects of
H•(C(k)) belong to the same part Xi(k) for some i∈I.
50
Indeed, if we choose any decomposition M =⊔i∈IX′
i into disjoint union
of constructible sets over k and identify I with the set of natural number
{1, 2,... }, then we can shrink X′
i(k) to the subset consisting of objects which
are not isomorphic to objects from ∪j<iX′
j(k).
By axioms A3),A4) we may assume that Ob(C)(k) is decomposed into
the union of k-points of schemes ( Si)i∈I (as in Axiom A3)) such that any
isomorphism class ofC(k) belongs only to one of the sets Si(k). Let us call it a
locally regular subdivision of Ob(C). Moreover, we can assume that all Si are
smooth and equidimensional, and such that for any i∈I there exists δ(i)∈
Z/greaterorequalslant0 such that for any E∈Si(k) the subset of objects in Si(k) isomorphic to
to E has dimension δ(i). This can be achieved by subdividing each Si into
smaller pieces, and by removing some unnecessary pieces con sisting of objects
which belong to other pieces. Then taking a generic slice of c odimension
δ(i) (and thus shrinking C to an equivalent subcategory), and taking further
subdivisions, one may assume that we have a locally regular s ubdivision of
Ob(C) such that any isomorphism class of objects in Si(k) is ﬁnite. Moreover,
we may assume that the cardinality ci of all isomorphism classes in Si(k)
depend only on i, and also the dimension di of the algebra Ext 0(E,E ) for
E∈Si(k) also depends only on i.
For any given i ∈ I let us consider the constructible set Zi over k
parametrizing isomorphism classes of objects in Si(k). There is a natural
constructible (over k) bundle of ﬁnite-dimensional unital associative alge-
brasA, with the ﬁber Ax over any full collection x = (E1,...,E ci) (up to
permutation) of diﬀerent isomorphic objects equal to
⊕1≤j1,j2≤ci Ext0(Ej1,Ej2).
The above algebra is Morita equivalent to Ext 0(Ej,Ej) for every j≤ci, and
in fact is isomorphic to the matrix algebra
Ax≃ Mat(ci×ci, Ext0(Ej,Ej)) ∀j≤ci.
Informally speaking, the “stack” of objects from Si is the stack of projective
modules M over algebraAx for some x∈ Zi(k) which are isomorphic after
Morita equivalence to a free module of rank one over Ext 0(Ej,Ej) where Ej
is some representative of the equivalence class x, i.e. M is isomorphic to the
standard module (Ext 0(Ej,Ej))⊕ci over the matrix algebra for every j≤ci.
We see that M has dimension
Ni :=cidi
51
over k. This leads to the following construction. Deﬁne a construc tible set
Yi over k to be the set of pairs ( x,f ) where x∈ Zi(k) is a point and f
is a homomorphism of Ax to the algebra of matrices Mat( Ni×Ni, k) such
that the resulting structure of Ax-module on k
Ni
belongs to the isomorphism
class of projective Ax-modules discussed above. The group GL(Ni, k) acts
naturally on Yi by changing the basis in the standard coordinate space k
Ni
.
The quotient set is naturally identiﬁed with Zi(k), and the stabilizer of every
point is isomorphic to Ext 0(Ej,Ej)× in the above notation.
The essential element of the presented construction is that everything
is equivariant with respect to the action of Gal( k/k). Hence, we come
to the conclusion that one associates (making many choices) with an ind-
constructible categoryC over k a countable collection of varieties ( Yi)i∈I (we
can assume that Yi are not just constructible sets but varieties after mak-
ing further subdivisions) endowed with algebraic actions o f aﬃne algebraic
groupsGL(Ni) such that the groupoid of isomorphism classes of C(k) is nat-
urally equivalent to the groupoid of the disjoint union of se ts Yi(k) endowed
with GL(Ni, k)-actions. If we replace C by an equivalent ind-constructible
category, or make diﬀerent choices in the construction, we o btain an equiv-
alent in an obvious sense “ind-constructible stack”. We wil l discuss ind-
constructible stacks later, in Section 4.2.
Moreover, using the fact that the ﬁrst Galois cohomology wit h coeﬃcients
in GL(Ni) vanish, one can see that the same is true for C(k) (and replace
Yi(k), GL(Ni, k)-actions by Yi(k) and GL(Ni, k)-action∀i∈I). In general,
for any ﬁeld k′, k⊂ k′⊂ k one can deﬁne the descent data for k′ and a
k′-linearA∞-categoryC(k′) (which is triangulated if C is triangulated in the
ind-constructible sense). The groupoid of isomorphism cla sses of objects of
H•(C(k′)) is equivalent to the groupoid of the disjoint union of sets Yi(k′)
endowed withGL(Ni, k′)-actions. More generally, one can deﬁne the category
C(k′) for any ﬁeld extension k′⊃ k, not necessarily an algebraic one. In the
case k′ = k we get a non-fatal crash of notations, because the A∞-category
C(k) in last sense is equivalent to the previously deﬁned C(k).
In what follows, we will assume for convenience that Ob(C) for an ind-
constructible categoryC is described by schemes Yi withGL(Ni)-actions. In
particular, for any extension k′⊃ k we will have a bijection
Iso(C(k′))≃⊔ i∈IYi(k′)/GL(Ni, k′)
between the set of isomorphism classes in C(k′) and the set of orbits.
52
Remark 16 In fact, objects of an A∞-category form not a stack but a higher
stack, i.e. one should speak about isomorphisms between iso morphisms etc.
Passing to the level of ordinary stacks we make a truncation. Presumably,
for a proper treatment of ind-constructible categories and problems like non-
functoriality of cones, one should introduce higher constr uctible stacks. Look-
ing on the guiding example of identiﬁcation data for ﬁnite no n-empty collec-
tions, one can guess an appropriate notion of a higher constr uctible stack.
Namely, it should be a simplicial constructible set X• which satisﬁes a con-
structible version of the Kan property (i.e. there exists a c onstructible lifting
from horns to simplices) and such that
1) for any k /greaterorequalslant2 the constructible map (∂0,...,∂ k) : Xk→ (Xk−1)k+1 is
a constructible vector bundle over its image (i.e. there exi sts a constructible
identiﬁcation of non-empty ﬁbers of this map with vector spa ces).
2)∃k0 such that ∀k /greaterorequalslantk0 the above map is an inclusion.
The reason for the ﬁrst property is that in the case of identiﬁ cation on each
step (except ﬁrst two) we have to solve linear equations. The second property
comes from the property HOMn
|Xi×Xi = 0 for n≪ 0 in our axiomatics of
ind-constructible categories.
