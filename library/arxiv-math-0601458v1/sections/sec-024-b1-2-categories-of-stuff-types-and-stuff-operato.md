---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-024-b1-2-categories-of-stuff-types-and-stuff-operato
section_title: "B.1. 2-Categories of Stuff Types and Stuff Operators"
section_number: null
pages: 62-66
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
notion of 2-categories - is just a preliminary suggestion of a still unfinished subject
of higher-dimensional categories. However, it turns out to be a crucial idea when
we want to describe the connection between stuff types and the quantum harmonic
oscillator. Groupoids and stuff types naturally form a 2-category, and in section 5]
we use the structure of this 2-category to show how the inner product on the space
of categorified states of the oscillator arises naturally.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS
63
Here we want to state and prove the important result that stuﬀtypes and
groupoids both naturally form a 2-category. Structure types F : FinSet0 →Set
formed a functor category whose morphisms were natural transformations. This
was the “coeﬃcient” viewpoint, but for stuﬀtypes we had to take the “bundle”
viewpoint, and deﬁned them as functors F : X →FinSet0, for some groupoid
X. Since a groupoid is already a category, we will see that all such objects can
naturally be formed into something more than a category. In particular, what we
will get is a 2-category:
Deﬁnition 36. A 2-category C consists of the following: a collection of objects,
and for every pair of objects x and y, a category hom(x, y) whose objects are called
morphisms of C and whose morphisms are called 2-morphisms of C.
There
must be functors hom(x, y)× hom(y, z)
mx,y,z
−→hom(x, z) giving composition (f, g) 7→
g ◦f. There are identity morphisms 1x ∈hom(x, x) with unit laws which are
2-isomorphisms λ, ρ from 1y ◦f and f ◦1x to f for f ∈hom(x, y).
There is
an associator, a 2-isomorphism αf,g,h : (h ◦g) ◦f →h ◦(g ◦f). These satisfy
coherence conditions.
We are omitting here any discussion the coherence conditions. Readers wanting
these details can consult [13] for more details.
A terminological note: what we are calling a 2-category some authors, such as [7]
call a bicategory, and what they call a 2-category we would call a strict 2-category,
where the associator and unit laws are identities. We adopt this convention be-
cause the non-strict case seems to be the more generally useful one, and deserves a
nomenclature which generalizes naturally.
Now, we can make the following observation:
Theorem 14. The collection of all categories, Cat, naturally forms a 2-category
whose morphisms are functors between categories, and whose 2-morphisms are nat-
ural transformations between functors. The collection of groupoids, Gpd, is a full
sub-2-category of Cat. In fact, these are strict 2-categories.
This sets up a helpful way of looking at stuﬀtypes: we have described them
as “groupoids over FinSet0” - that is, functors from groupoids X to the groupoid
FinSet0. In particular, since groupoids from a 2-category, of which FinSet0 is
an object, we can describe a 2-category of stuﬀtypes, namely that of groupoids
over FinSet0. This is a 2-categorical version of an “over category”. This sort of
structure is explained in further detail in appendix B.
We have just described stuﬀtypes as functors into FinSet0 in Gpd, so it is
natural to ask whether other functors in Gpd are also of interest as further gener-
alizations of structure types. In section C.1, we brieﬂy describe some work in this
direction.
Deﬁnition 37. The weak 2-category StuﬀTypes has as objects diagrams in Gpd
of the form X
Ψ
→FinSet0 (Denoted (X, Ψ), or just X or Ψ for short whenever the
meaning is clear). Given two objects (X1, Ψ1) and (X1, Ψ1), hom(Ψ1, Ψ2) has as
morphisms functors F : X1 →X2 together with a natural isomorphism α such that
64
JEFFREY MORTON
the diagram
(78)
X1
Ψ1

F
/ X2
Ψ2
zuuuuuuuuu
FinSet0
px
α
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
commutes up to α.
Given a pair F and G of such morphisms between X1 and
X2, the 2-morphisms between them are the natural transformations ν between the
functors F and G for which the resulting diagram commutes.
Theorem 15. The construction given for StuﬀTypes gives a well-deﬁned 2-
category.
Proof. The collections hom(Ψ1, Ψ2) involve functors from X1 to X2 in Gpd. These
are closed under composition. A morphism in StuﬀTypes also includes a natural
transformation α, and these are again closed under composition. If two composable
functors F1 and F2 between groupoids make the triangles over FinSet0 commute
up to natural isomorphisms α1 and α2, then F2 ◦F1 does the same, up to α1 ◦α2.
So in particular, the obvious notion of composition is well deﬁned, and in fact the
hom(Ψ1, Ψ2) are categories.
Identity morphisms are inherited from Gpd, and obviously make the corre-
sponding triangles commute. The unit laws and associator are just these identity
2-morphisms, so we have a strict 2-category.
□
The construction for stuﬀoperators is similar:
Deﬁnition 38. The 2-category StuﬀOps has as objects diagrams in Gpd of the
form FinSet0
p1
←T
p2
→FinSet0) (Denoted (T, p1, p2), or just T , for short). Given
two objects T and T ′, hom(T, T ′) has as morphisms functors F : T →T ′ making
the diagram
(79)
T
p1

p2
&M
M
M
M
M
M
M
M
M
M
M
M
F
/ T ′
p′
1
xqqqqqqqqqqq
p′
2

FinSet0
FinSet0
commute up to two natural isomorphisms. The 2-morphisms are the natural trans-
formations ν between such functors F and G which make the resulting diagram
commute.
Where we have omitted the detailed diagram for the naturality squares. It is
substantially similar to that for stuﬀtypes, in section 4.2.1. We also get a result
similar to that for stuﬀtypes:
Theorem 16. The construction given for StuﬀOps gives a well-deﬁned strict 2-
category.
Proof. The proof that this is a 2-category is similar to that for stuﬀtypes.
□
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS
65
The algebraic structure of StuﬀOps is of interest. It is, in fact, the equivalent
of an algebra - having addition, scalar multiplication (by groupoids) and internal
multiplication in the form of composites. But since groupoids do not have cardanil-
ities in a ﬁeld, we will just point out that if we ignore 2-morphisms, it is a category,
and in fact:
Theorem 17. The category StuﬀOps (disregarding 2-morphisms) is a 2-rig, where
the monoidal operation is composition.
Proof. First, the StuﬀOps is cocomplete because Gpd is, and so any colimit in
Gpd becomes one in StuﬀOps. The monoidal operation given by composition
gets all the required natural isomorphisms from those in the weak pullback.
□
We have only sketched the main ideas of these proofs, of course (in particular,
we have not even stated the necessary coherence conditions, let alone proved they
are satisﬁed). We leave these details for the interested reader. However, this ﬁnally
gives us a clear description of the categoriﬁed version of the algebra of operators
on formal power series.
Analogous results hold for M-stuﬀtypes.
66
JEFFREY MORTON
