---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-012-appendix-b-slice-categories-and-2-categories
section_title: "Appendix B. Slice Categories and 2-Categories"
section_number: null
pages: 62-66
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
We saw that in the special case where the groupoid Z0 of colourings was a set,
the category of groupoid-coloured sets had objects which were m aps from sets S
intoZ0, and morphisms were commuting diagrams like this:
(76) S
c
/d15/d15
σ /d47/d47S′
c′
/d126/d126/d125/d125/d125/d125/d125/d125/d125/d125
Z0
commutes.
This is an example of an “over category”. These are categories of o bjects “over”
some given object. In general, an over category can be construc ted from any cat-
egoriesC and object c∈C by taking objects to be maps f : a→ c (for a∈C )
and morphisms to be commuting triangles. We will encounter this sort of construc-
tion again when we deﬁne M -sets and M -stuﬀ types for a monoid M . This sort
of construction is often called a “slice category”. We will prefer the slightly more
illustrative terminology “over category”. For more details, see e.g. [13] or [14].
In general, however, groupoid-coloured sets have colours taken from a groupoid,
which is not an object in Set, so we have something somewhat weaker. One way
to say it is that we only have a forgetful functor from Z0-Set to Set whereZ0-sets
are taken to the underlying set, and morphisms are taken to their u nderlying set
bijections. It is worth pointing out the relationship between this and the change of
perspective between our original way of deﬁning structure types as functions from
underlying sets to the “bundle” viewpoint, with structured sets lyin g “over” their
underlying sets.
Another way to say what we have with Z0-Set is that it is a weak over 2-category,
when we think of the sets S andS′ as trivial groupoids, hence σ,c andc′ functors.
These are deﬁned like over categories, but instead of morphisms am ounting to
commuting triangles, morphisms consist of natural isomorphisms α with:
(77) S
c
/d15/d15
σ /d47/d47S′
c′
/d126/d126/d125/d125/d125/d125/d125/d125/d125/d125
Z0
/d114/d122
α /d108/d108/d108/d108/d108/d108/d108
/d108/d108/d108/d108/d108/d108/d108
This is exactly the deﬁnition we gave above, where the morphisms com ing from
α give the labels on the strands of σ.
The formulation of over 2-categories is particularly relevant to stu ﬀ types, as we
shall see. First, however, we need to ﬁll in some more infrastructu re.
B.1. 2-Categories of Stuﬀ Types and Stuﬀ Operators. The second - the
notion of 2-categories - is just a preliminary suggestion of a still unﬁ nished subject
of higher-dimensional categories. However, it turns out to be a cr ucial idea when
we want to describe the connection between stuﬀ types and the qu antum harmonic
oscillator. Groupoids and stuﬀ types naturally form a 2-category, and in section 5,
we use the structure of this 2-category to show how the inner pro duct on the space
of categoriﬁed states of the oscillator arises naturally.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 63
Here we want to state and prove the important result that stuﬀ ty pes and
groupoids both naturally form a 2-category. Structure types F : FinSet0→ Set
formed a functor category whose morphisms were natural trans formations. This
was the “coeﬃcient” viewpoint, but for stuﬀ types we had to take t he “bundle”
viewpoint, and deﬁned them as functors F : X→ FinSet0, for some groupoid
X. Since a groupoid is already a category, we will see that all such obje cts can
naturally be formed into something more than a category. In partic ular, what we
will get is a 2-category:
Deﬁnition 36. A 2-categoryC consists of the following: a collection of objects,
and for every pair of objects x and y, a category hom(x,y ) whose objects are called
morphisms ofC and whose morphisms are called 2-morphisms ofC. There
must be functors hom(x,y )× hom(y,z )
mx,y,z
−→ hom(x,z ) giving composition (f,g )↦→
g◦f . There are identity morphisms 1x∈ hom(x,x ) with unit laws which are
2-isomorphisms λ, ρ from 1y◦f and f◦ 1x to f for f ∈ hom(x,y ). There is
an associator, a 2-isomorphism αf,g,h : (h◦g)◦f→ h◦ (g◦f ). These satisfy
coherence conditions.
We are omitting here any discussion the coherence conditions. Read ers wanting
these details can consult [13] for more details.
A terminological note: what we are calling a 2-category some author s, such as [7]
call a bicategory, and what they call a 2-category we would call a strict 2-category ,
where the associator and unit laws are identities. We adopt this conv ention be-
cause the non-strict case seems to be the more generally useful o ne, and deserves a
nomenclature which generalizes naturally.
Now, we can make the following observation:
Theorem 14. The collection of all categories, Cat, naturally forms a 2-category
whose morphisms are functors between categories, and whose 2-morphisms are nat-
ural transformations between functors. The collection of g roupoids, Gpd, is a full
sub-2-category of Cat. In fact, these are strict 2-categories.
This sets up a helpful way of looking at stuﬀ types: we have describe d them
as “groupoids over FinSet0” - that is, functors from groupoids X to the groupoid
FinSet0. In particular, since groupoids from a 2-category, of which FinSet0 is
an object, we can describe a 2-category of stuﬀ types, namely th at of groupoids
over FinSet0. This is a 2-categorical version of an “over category”. This sort o f
structure is explained in further detail in appendix B.
We have just described stuﬀ types as functors into FinSet0 in Gpd, so it is
natural to ask whether other functors in Gpd are also of interest as further gener-
alizations of structure types. In section C.1, we brieﬂy describe so me work in this
direction.
Deﬁnition 37. The weak 2-category StuﬀTypes has as objects diagrams in Gpd
of the form X
Ψ
→ FinSet0 (Denoted (X, Ψ) , or just X or Ψ for short whenever the
meaning is clear). Given two objects (X1, Ψ 1) and (X1, Ψ 1), hom(Ψ 1, Ψ 2) has as
morphisms functors F : X1→ X2 together with a natural isomorphism α such that
64 JEFFREY MORTON
the diagram
(78) X1
Ψ 1
/d15/d15
F /d47/d47 X2
Ψ 2/d122/d122/d117/d117/d117/d117/d117/d117/d117/d117/d117
FinSet0
/d112/d120
α /d105/d105/d105/d105/d105/d105/d105/d105/d105/d105
/d105/d105/d105/d105/d105/d105/d105/d105/d105/d105
commutes up to α. Given a pair F and G of such morphisms between X1 and
X2, the 2-morphisms between them are the natural transformati ons ν between the
functors F and G for which the resulting diagram commutes.
Theorem 15. The construction given for StuﬀTypes gives a well-deﬁned 2-
category.
Proof. The collections hom(Ψ 1, Ψ 2) involve functors from X1 to X2 in Gpd. These
are closed under composition. A morphism in StuﬀTypes also includes a natural
transformationα, and these are again closed under composition. If two composable
functors F1 and F2 between groupoids make the triangles over FinSet0 commute
up to natural isomorphisms α1 and α2, then F2◦F1 does the same, up to α1◦α2.
So in particular, the obvious notion of composition is well deﬁned, and in fact the
hom(Ψ 1, Ψ 2) are categories.
Identity morphisms are inherited from Gpd, and obviously make the corre-
sponding triangles commute. The unit laws and associator are just t hese identity
2-morphisms, so we have a strict 2-category. □
The construction for stuﬀ operators is similar:
Deﬁnition 38. The 2-category StuﬀOps has as objects diagrams in Gpd of the
form FinSet0
p1
←T
p2
→ FinSet0) (Denoted (T,p 1,p 2), or just T , for short). Given
two objects T and T ′, hom(T,T ′) has as morphisms functors F : T→ T ′ making
the diagram
(79) T
p1
/d15/d15
p2
/d38/d38/d77/d77/d77/d77/d77/d77/d77/d77/d77/d77/d77/d77
F /d47/d47T ′
p′
1/d120/d120/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113/d113
p′
2
/d15/d15
FinSet0 FinSet0
commute up to two natural isomorphisms. The 2-morphisms are the natural trans-
formations ν between such functors F and G which make the resulting diagram
commute.
Where we have omitted the detailed diagram for the naturality squar es. It is
substantially similar to that for stuﬀ types, in section 4.2.1. We also ge t a result
similar to that for stuﬀ types:
Theorem 16. The construction given for StuﬀOps gives a well-deﬁned strict 2-
category.
Proof. The proof that this is a 2-category is similar to that for stuﬀ types. □
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 65
The algebraic structure of StuﬀOps is of interest. It is, in fact, the equivalent
of an algebra - having addition, scalar multiplication (by groupoids) an d internal
multiplication in the form of composites. But since groupoids do not ha ve cardanil-
ities in a ﬁeld, we will just point out that if we ignore 2-morphisms, it is a c ategory,
and in fact:
Theorem 17. The category StuﬀOps (disregarding 2-morphisms) is a 2-rig, where
the monoidal operation is composition.
Proof. First, the StuﬀOps is cocomplete because Gpd is, and so any colimit in
Gpd becomes one in StuﬀOps . The monoidal operation given by composition
gets all the required natural isomorphisms from those in the weak p ullback. □
We have only sketched the main ideas of these proofs, of course (in particular,
we have not even stated the necessary coherence conditions, let alone proved they
are satisﬁed). We leave these details for the interested reader. H owever, this ﬁnally
gives us a clear description of the categoriﬁed version of the algebr a of operators
on formal power series.
Analogous results hold for M -stuﬀ types.
66 JEFFREY MORTON
