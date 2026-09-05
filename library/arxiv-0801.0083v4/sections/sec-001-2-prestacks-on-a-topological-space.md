---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-001-2-prestacks-on-a-topological-space
section_title: "Prestacks on a Topological Space"
section_number: 2
pages: 8-11
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
---
Let X be a topological space. We need some notation for open coveri ngs. Let
U ⊂ X be an open set, and let U = {Uk}k∈K be an open covering of U , i.e.
U = ⋃
k∈KUk. Given k0,...,k m ∈K we write
Uk0,...,k m :=Ui0 ∩ · · · ∩Ukm.
Let S be a sheaf of sets on X. For an open set U ⊂ X we denote by S(U ) =
Γ(U, S) the set of sections of S on U .
Recall that a prestack G onX is the geometrization of the notion of category, in
the same way that a presheaf of sets is the geometrization of t he notion of a set.
Formally speaking a prestack G is a pseudofunctor
G = (G0, G1, G2) : ( OpenX)op → Cat,
where OpenX is the small category whose objects are the open sets U ⊂ X, and
the morphisms V → U are the inclusions V ⊂ U . However we shall make things
more explicit here, and introduce some notation, to emphasi ze the geometry.
Thus a prestack G on X has the following structure. For any open set U ⊂ X
there is a category G(U ) := G0(U ). Elements of the set Ob G(U ) shall be denoted
by the letters i,j etc.; this is because we want to view them as indices. We write
(2.1) G(U )(i,j ) := Hom G(U)(i,j ),
the set of morphisms in the category G(U ) from i to j.
There are restriction functors (1-morphisms Cat)
restG
U1/U 0
:= G1(U1 →U0) : G(U0) → G(U1)
for any inclusion U1 ⊂ U0 of open sets. And there are composition isomorphisms
(2-isomorphisms in Cat)
γ G
U2/U 1/U 0
:= G2(U2 →U1 →U0) : rest G
U2/U 1
◦ restG
U1/U 0
≃
=⇒ restG
U2/U 0
for a double inclusion U2 ⊂U1 ⊂U0. Condition (1.3) now becomes
(2.2) γ G
U3/U 2/U 0
∗γ G
U2/U 1/U 0
=γ G
U3/U 1/U 0
∗γ G
U3/U 2/U 1
for a triple inclusion U3 ⊂U2 ⊂U1 ⊂U0. And there are corresponding conditions
for U
=
− →U .
As explained in Section 1, the set of prestacks on X has a structure of 2-category,
which we denote by PreStackX. Again, we want to be more speciﬁc. Suppose G
and H are two prestacks on X. A morphism of prestacks F : G → H is a 1-
morphism between these pseudofunctors. Thus there is a func tor
F (U ) : G(U ) → H(U )
CENTRAL EXTENSIONS OF GERBES 9
for any open set U , together with an isomorphism of functors
ψ F
U1/U 0 :F (U1) ◦ restG
U1/U 0
≃
=⇒ restH
U1/U 0 ◦F (U0)
for any inclusion U1 ⊂U0 of open sets. These isomorphisms are required to satisfy
condition
ψ F
U2/U 0 ∗γ G
U2/U 1/U 0
=γ H
U2/U 1/U 0 ∗ψ F
U2/U 1 ∗ψ F
U1/U 0
for a double inclusion U2 ⊂U1 ⊂U0.
The composition of morphisms of prestacks G
F
− →H
E
− →K is denoted by E ◦F .
Suppose D,E,F : G → H are morphisms between prestacks. We will denote
2-morphisms between E andF byη :E ⇒F . And the (vertical) composition with
a 2-morphism ζ :D ⇒E is denoted by η ∗ζ :D ⇒F .
As in any 2-category, we can say when a morphism of prestacks F : G → H (i.e.
a 1-morphism in PreStackX) is an equivalence. This just means that there is a
morphism of prestacksE : H → G, and 2-isomorphisms E ◦F
≃
=⇒ 1G andF ◦E
≃
=⇒
1H. But here there is also a geometric characterization: F is an equivalence if and
only if for any open set U ⊂X the functor F (U ) : G(U ) → H(U ) is an equivalence.
Let G be a prestack on X. By a subprestack of G we mean a prestack N such that
N (U ) is a subcategory of G(U ) for every open set U , and such that the restriction
functors rest N
−/ − and the composition isomorphisms γ N
−/ −/ − are the same as those
of G.
Suppose G is a prestack on X. Take an open set U ⊂ X and two objects
i,j ∈ Ob G(U ). There is a presheaf of sets G(i,j ) on U , called the presheaf of
morphisms, deﬁned as follows. For an open set V ⊂U we deﬁne the set
G(i,j )(V ) := Hom G(V )
(
restG
V /U (i), restG
V /U (j)
)
.
For an inclusion V1 ⊂V0 ⊂U of open sets, the restriction function
restG(i,j )V1/V 0 : G(i,j )(V0) → G(i,j )(V1)
is the composed function
HomG(V0)
(
restG
V0/U (i), restG
V0/U (j)
)
restG
V1/V 0
− − − − − − →HomG(V0)
(
(restG
V1/V 0
◦ restG
V0/U )(i), (restG
V1/V 0
◦ restG
V0/U )(j)
)
γ G
V1 /V 0/U
− − − − − − →HomG(V1)
(
restG
V1/U (i), restG
V1/U (j)
)
.
Condition (2.2) ensures that
restG(i,j )V2/V 1 ◦ restG(i,j )V1/V 0 = rest G(i,j )V2/V 0
for an inclusion V2 ⊂V1 ⊂V0 ⊂U . Note that the set of sections of this presheaf is
Γ(V, G(i,j )) = G(V )(i,j ).
From now on we shall usually write i|V instead of rest G
V /U (i), for a local object i ∈
Ob G(U ); and g|V1 instead rest G(i,j )V1/V 0 (g), for a local morphism g ∈ G(i,j )(V0).
Furthermore, we usually omit reference to the restriction f unctors rest G
−/ − alto-
gether.
Another convention that we shall adopt from here on is that we denote the
composition in the local categories G(U ) of a prestack G by “◦”, and not by “ ∗” as
we did up to here.
10 AMNON YEKUTIELI
Let F : G → H be a morphism of prestacks. One says that F is a weak equiva-
lence if it satisﬁes these conditions:
(i) F is locally essentially surjective on objects . This mean that for any open
set U ⊂ X, object j ∈ Ob H(U ) and point x ∈ U , there is an open set V
withx ∈V ⊂U , an object i ∈ Ob G(V ), and an isomorphism h :F (i)
≃
− →j
in H(V ).
(ii) For any open set U and i,j ∈ Ob G(U ) the function
F : G(U )(i,j ) → H(U )
(
F (i),F (j)
)
is bijective. In other words, the functor F : G(U ) → H(U ) is fully faithful.
A prestack G is called a stack if it satisﬁes these two conditions:
(a) Descent for morphisms . This means that the presheaves of morphisms
G(i,j ) are all sheaves.
(b) Descent for objects . This means that given an open set U , an open covering
U = ⋃
k∈KUk, objects ik ∈ Ob G(Uk), and isomorphisms
gk0,k 1 ∈ G(Uk0,k 1)(ik0 |Uk0 ,k 1,i k1|Uk0 ,k 1 )
that satisfy
gk1,k 2|Uk0 ,k 1 ,k 2 ◦gk0,k 1 |Uk0 ,k 1 ,k 2 =gk0,k 2|Uk0 ,k 1 ,k 2,
there exists an object i ∈ G(U ), and isomorphisms gk ∈ G(Uk)(i|Uk,i k),
such that
gk0,k 1 ◦gk0|Uk0 ,k 1 =gk1 |Uk0 ,k 1.
Observe that by condition (a), the object i ∈ G(U ) in condition (b) is unique up
to a unique isomorphism. A prestack G satisfying condition (a) is sometimes called
a separated prestack.
We denote by StackX the full sub 2-category of PreStackX gotten by taking
all stacks, all 1-morphisms between them, and all 2-morphis ms between these 1-
morphisms.
It is not hard to see that a morphism of stacks F : G → H is an equivalence if
and only if it is a weak equivalence.
There is a stackiﬁcation operation, which is analogous to sheaﬁﬁcation: to any
prestack G one assigns a stack ˜G, with a morphism of prestacks F : G → ˜G.
These have the following universal property: given any stac k H and morphism
E : G → H, there is a morphism ˜E : ˜G → H, unique up to 2-isomorphism, such
thatE
≃
⇐ ⇒ ˜E ◦F .
Recall that a groupoid is a category G in which all morphisms are isomorphisms.
For an object i the set G(i,i ) is then a group. If the set G(i,j ) ⁄= ∅, then it is a
G(j,j )-G(i,i )-bitorsor. For g ∈ G(i,j ) we denote by Ad( g) the group isomorphism
G(i,i ) → G(j,j ) given by Ad(g)(h) := g ◦h ◦g−1.
By a prestack of groupoids on X we mean a prestack G such that each of the
categories G(U ) is a groupoid. We denote by PreStGrX the full sub 2-category
of PreStackX gotten by taking all prestacks of groupoids, all 1-morphism s be-
tween them, and all 2-morphisms between these 1-morphisms. If G is a prestack of
groupoids, then the associated stack ˜G is a stack of groupoids.
We shall be interested in gerbes. A gerbe is a stack of groupoids G on X that
has these two properties:
