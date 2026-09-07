---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-002-3-extensions-of-gerbes
section_title: "Extensions of Gerbes"
section_number: 3
pages: 11-19
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
---
(†) G is locally nonempty . What this means is that any point x ∈ X has an
open neighborhood U such that Ob G(U ) ⁄= ∅.
(††) G is locally connected. This says that for any i,j ∈ Ob G(U ) and anyx ∈X,
there is an open set V such that x ∈V ⊂U and G(V )(i,j ) ⁄= ∅.
A gerbe G is called trivial if Ob G(X) ⁄= ∅.
Let G be a sheaf of groups on X. By a left G-torsor onX we mean a sheaf of sets
S, with a left G-action, such that S is locally nonempty (i.e. each point x ∈X has
an open neighborhood U such that S(U ) ⁄= ∅), and for any s ∈ S (U ) the morphism
of sheaves of sets G|U → S| U , g ↦→g ·s, is an isomorphism. The torsor S is trivial
if S(X) ⁄= ∅.
Suppose G is a gerbe on X. Given an open set U ⊂X and i ∈ Ob G(U ), there
is a sheaf of groups G(i,i ) on U . If j ∈ Ob G(U ) is some other object, then the
sheaf of sets G(i,j ) is a G(j,j )-G(i,i )-bitorsor. Namely, forgetting the left action
by G(j,j ), the sheaf G(i,j ) is a right G(i,i )-torsor; and vice versa.
We denote by GerbeX the full sub-2-category of PreStGrX gotten by taking
all gerbes, all 1-morphisms between gerbes, and all 2-morph isms between these
1-morphisms.
Here are two prototypical examples of gerbes.
Example 2.3. Let I be the groupoid with one object, say 0, and with I(0, 0) :=
{10}, the trivial group. This groupoid is a terminal object in Cat, since any category
C admits exactly one functor C → I.
Now take a topological spaceX, and deﬁne a prestack I on it by letting I(U ) := I
for any open set U . Then I is a gerbe. The gerbe I is a terminal object in
PreStackX. Indeed, given any prestack G on X there is a unique morphism of
prestacks G → I. We call I the terminal gerbe (because the word “trivial” is
over-used in this area).
Example 2.4. Let G be a sheaf of groups on X. For an open set U let Tors(G|U )
be the set of all left G|U -torsors. This is a groupoid. Given V ⊂U there is a functor
Tors(G|U ) → Tors(G|V ),
namely S ↦→ S|V . Thus we obtain a prestack of groupoids TorsG with
(TorsG)(U ) := Tors(G|U ).
Since torsors are locally trivial it follows that TorsG is a gerbe, called the gerbe of
G-torsors.
Remark 2.5. A prestack of groupoids G is sometimes called a category ﬁbered in
groupoids over OpenX. More precisely, given G, we can construct a category G,
together with a functor Φ : G → OpenX called the ﬁber functor. The set of objects
of G is
Ob G :=
∐
U∈Open X
Ob G(U ).
For objects i ∈ Ob G(U ) and j ∈ Ob G(V ) one deﬁnes
HomG(i,j ) := Hom G(U)(i,j |U )
if U ⊂ V ; and Hom G(i,j ) := ∅ otherwise. The ﬁber functor Φ : G → OpenX is
Φ(i) := U for i ∈ Ob G(U ), and Φ(g) := (U →V ) for g ∈ HomG(i,j ) as above.
Conversely, the prestack G can be recovered from the data Φ : G → OpenX.
12 AMNON YEKUTIELI
For stacks of groupoids arising from moduli problems it is of ten more natural to
use the ﬁbered category approach (cf. [LMB]); but for our app lications in [Ye], the
pseudofunctor approach is more suitable.
3. Extensions of Gerbes
We begin by taking certain basic notions about groups (such a s normal subgroup
and center) and generalizing them to groupoids. As a matter o f convenience we
often refer to a functor F : G → H between groupoids as a morphism. (Indeed this
is a 1-morphism in the 2-category Groupoid of groupoids.)
Deﬁnition 3.1. Let G be a groupoid. A normal subgroupoid of G is a subgroupoid
N satisfying the following three conditions.
(i) Ob N = Ob G.
(ii) For every i,j ∈ Ob G and g ∈ G(i,j ) there is equality
Ad(g)
(
N(i,i )
)
= N(j,j ).
(iii) N is totally disconnected, i.e. N(i,j ) = ∅ for i ⁄=j.
In particular for every i ∈ Ob G the group N(i,i ) is normal subgroup of the
automorphism group G(i,i ).
Note that a normal subgroupoid N is the same as a collection {Ni}i∈Ob G of
subgroups Ni ⊂ G(i,i ), satisfying the obvious variant of condition (ii).
The trivial normal subgroupoid of G is the normal subgroupoid N for which all
the groups N(i,i ) are trivial; namely N(i,i ) = {1i}.
Let F : G → H be a morphism of groupoids. For i ∈ Ob G let
Ker(F )(i,i ) := Ker
(
F : G(i,i ) → H(F (i),F (i))
)
.
This is a normal subgroup of G(i,i ). Moreover, an easy calculation shows that the
collection of subgroups {Ker(F )(i,i )}i∈Ob G is a normal subgroupoid of G, which
we denote by Ker( F ).
Deﬁnition 3.2. Let F : G → H be a morphism of groupoids. We say that F is a
weak epimorphism if it satisﬁes these conditions:
(i) F is essentially surjective objects. Namely for any j ∈ Ob H there exists
some i ∈ Ob G such that H(F (i),j ) ⁄= ∅.
(ii) F is surjective on sets of morphisms. This means that for any i,j ∈ Ob G
the function
F : G(i,j ) → H
(
F (i),F (j)
)
is surjective.
Observe that if F : G → H is a weak epimorphism whose kernel Ker( F ) is the
trivial normal subgroupoid of G, then F is an equivalence.
Deﬁnition 3.3. By an extension of groupoids we mean a diagram of morphisms
of groupoids
N
E
− →G
F
− →H,
such that F is a weak epimorphism, N = Ker(F ), and E : N → G is the inclusion.
CENTRAL EXTENSIONS OF GERBES 13
By analogy with the case of groups we often write
(3.4) 1 → N → G
F
− →H → 1
for an extension of groupoids. But this is only a suggestive n otation – we do not
view the symbols “1” as groupoids. (We could, but then the ﬁrs t 1 has to be
replaced by the trivial normal subgroupoid of G, and the second 1 by the terminal
groupoid of Example 2.3.)
Extensions of groupoids behave very much like extensions of groups. Suppose
G is a groupoid and N ⊂ G is a normal subgroupoid. Then there is an extension
of groupoids (3.4). The groupoid H in this extension is unique up to equivalence.
One could choose H such that the function F : Ob G → Ob H is bijective; and that
would make H unique up to isomorphism.
Next suppose F : G → H, F′ : G′ → H′ and D : G → G′ are morphisms of
groupoids, such that D
(
Ker(F )
)
⊂ Ker(F′). Then there is a morphism of groupoids
E : H → H′, unique up to 2-isomorphism, such that the diagram
G
F /d47/d47
D
/d15/d15
H
E
/d15/d15
G′
F ′
/d47/d47H′
commutes up to 2-isomorphism.
Now consider a groupoid G. For any i ∈ Ob G we have the center Z( G(i,i )) of
the automorphism group G(i,i ). Given any pair of objects i,j ∈ Ob G, and any
isomorphism g ∈ G(i,j ), we have
Ad(g)
(
Z(G(i,i ))
)
= Z(G(j,j )).
Therefore the collection of subgroups {Z(G(i,i ))}i∈Ob G is a normal subgroupoid of
G, which we denote by Z( G), and call the center of G.
Deﬁnition 3.5. (1) Let G be a groupoid. A central subgroupoid of G is any
normal subgroupoid N that is contained in Z( G).
(2) A central extension of groupoids is an extension of groupoids (3.4) such that
N is a central subgroupoid of G.
Suppose G is a nonempty and connected groupoid, and N is a central subgroupoid
of G. Take any i,j ∈ Ob G and g,g ′ ∈ G(i,j ). Then the group isomorphisms
Ad(g), Ad(g′) : N(i,i ) → N(j,j )
are equal. In this way we can canonically identify the abelia n groups N(i,i ), for
i ∈ Ob G, and view them as a single abelian group.
When we are given a central extension of groupoids (3.4) in wh ich G is nonempty
and connected, we can replace the central subgroupoid N by a single abelian group
N as explained above, and the extension becomes
1 →N → G
F
− →H → 1.
So far for the discrete situation; now we geometrize. Let X be a topological space.
Suppose G is a gerbe on X. By a local object i of G we mean an object i ∈ Ob G(U )
for some open set U ⊂ X. If i,j are two local objects, deﬁned on open sets U,V
respectively, then by G(i,j ) we mean the corresponding sheaf of isomorphisms on
U ∩V . By a local isomorphism g :i
≃
− →j we mean an isomorphism g ∈ G(i,j )(W )
14 AMNON YEKUTIELI
for some open set W ⊂U ∩V . Such g gives rise to an isomorphism of sheaves of
groups
Ad(g) : G(i,i )|W
≃
− →G(j,j )|W.
Deﬁnition 3.6. Let G be a gerbe on X. A normal subprestack of groupoids of G
is a subprestack N of G with these two properties:
(i) For every open set U the category N (U ) is a normal subgroupoid of G(U )
(see Deﬁnition 3.1). In particular Ob N (U ) = Ob G(U ), and N (U ) is
totally disconnected.
(ii) For every local object i of N the presheaf N (i,i ) is a sheaf.
Since the full name is too long, we simply call such N a normal subgroupoid of
G.
Here is what the deﬁnition amounts to. For every local object i of G there is a
subsheaf of groups N (i,i ) ⊂ G(i,i ). The condition is that for any local objects i
and j, and any local isomorphism g :i →j, one has
Ad(g)
(
N (i,i )
)
= N (j,j ).
Warning: a normal subgroupoid of a gerbe is usually not a gerb e, nor even a
stack.
Proposition 3.7. Given a morphism of gerbes F : G → H, there is a unique
normal subgroupoid N of G such that
N (U ) = Ker
(
F : G(U ) → H(U )
)
for every open set U .
Proof. The formula deﬁnes a subprestack of groupoids N of G. We know that the
groupoid N (U ) is normal in G(U ). And for any local object i of G we have
N (i,i ) = Ker
(
F : G(i,i ) → H
(
F (i),F (i)
))
as presheaves, so N (i,i ) a sheaf. □
Deﬁnition 3.8. The normal subgroupoid N in the proposition above is called the
kernel of F , and it is denoted by Ker( F )
Deﬁnition 3.9. Let F : G → H be a morphism of gerbes. We say that F is a
weak epimorphism if it satisﬁes these conditions:
(i) F is locally essentially surjective on objects . Recall that this says that for
any open set U ⊂ X, object j ∈ Ob H(U ) and point x ∈ U , there is an
open set V with x ∈V ⊂ U , an object i ∈ Ob G(V ), and an isomorphism
h :F (i)
≃
− →j in H(V ).
(ii) F is surjective on isomorphism sheaves . This says that for any i,j ∈
Ob G(U ) the map of sheaves of sets
F : G(i,j ) → H
(
F (i),F (j)
)
is surjective.
Note that if F : G → H is a weak epimorphism such that Ker( F ) is the triv-
ial normal subgroupoid of G, then F is a weak equivalence, and hence it is an
equivalence.
CENTRAL EXTENSIONS OF GERBES 15
Deﬁnition 3.10. An extension of gerbes is a diagram
N
E
− →G
F
− →H
of morphisms in PreStGrX, such that G and H are gerbes, F is a weak epimor-
phism, N = Ker(F ), and E : N → G is the inclusion.
We often use the notation of “exact sequence”
(3.11) 1 → N → G
F
− →H → 1
for an extension of gerbes.
Deﬁnition 3.12. A morphism of extensions of gerbes is a diagram
N /d47/d47
/d15/d15
G
F /d47/d47
D
/d15/d15
H
E
/d15/d15
N′ /d47/d47G′
F ′
/d47/d47H′
of morphisms in PreStGrX, where the rows are extensions of gerbes, the square
on the right is commutative up to 2-isomorphism, and the squa re on the left is
commutative. We denote this morphism of extensions by ( D,E ).
Theorem 3.13. Let G be a gerbe on X, and let N be a normal subgroupoid of G.
Then there exists a gerbe G/ N , and a morphism of gerbes F : G → G/ N , with the
following properties:
(i) The diagram
1 → N → G
F
− →G/ N → 1
is an extension of gerbes.
(ii) Suppose
1 → N′ → G′ F ′
− →H′ → 1
is an extension of gerbes, and D : G → G′ is a morphism of gerbes, such
that D(N ) ⊂ N′. Then there is a morphism gerbes E : G/ N → H′,
unique up to 2-isomorphism, such that the diagram
1 /d47/d47N /d47/d47
/d15/d15
G
F /d47/d47
D
/d15/d15
G/ N /d47/d47
E
/d15/d15
1
1 /d47/d47N′ /d47/d47G′
F ′
/d47/d47H′ /d47/d471
is a morphism of extensions.
(iii) In the situation of property (ii), assume the morphism D : G → G′ is an
equivalence, and the sheaf homomorphisms
D : N (i,i ) → N′(
F (i),F (i)
)
are isomorphisms for all local objects i of G. Then E is also an equivalence.
Before giving the proof we need some preliminary work. Let U ⊂X be an open
set, and let i,j ∈ Ob G(U ). The sheaf of sets G(i,j ) is a right G(i,i )-torsor on U ,
and hence it has a right action by the sheaf of groups N (i,i ). Let ¯G(i,j ) be the
sheaf of sets on U associated to the presheaf
V ↦→G(V )(i,j )/ N (V )(i,i ).
16 AMNON YEKUTIELI
There is a surjective sheaf morphism G(i,j ) → ¯G(i,j ). If i = j we get a sheaf of
groups ¯G(i,i ).
Lemma 3.14. There is a unique structure of ¯G(j,j )- ¯G(i,i )-bitorsor on ¯G(i,j ),
such that the surjection G(i,j ) → ¯G(i,j ) is G(j,j ) × G(i,i ) -equivariant.
Proof. Uniqueness is clear. For existence, we have to exhibit a suit able action of the
sheaf of groups ¯G(j,j ) × ¯G(i,i ) on the sheaf of sets ¯G(i,j ). Because of uniqueness,
this is a local question.
Choose an open set V ⊂X that trivializes the bitorsor G(i,j ); namely there is
some g ∈ G(i,j )(V ). Then the left action of G(j,j )|V on G(i,j )|V coincides with
the right action of G(i,i )|V , via the isomorphism of sheaves of groups
Ad(g) : G(i,i )|V
≃
− →G(j,j )|V.
Also we have a torsor isomorphism
G(i,i )|V
≃
− →G(i,j )|V, f ↦→g ◦f.
Let ¯g ∈ ¯G(i,j )(V ) be the image of g. We then have an isomorphism of sheaves
of right ¯G(i,i )|V -sets
¯G(i,i )|V
≃
− →¯G(i,j )|V, ¯f ↦→¯g ◦ ¯f.
It follows that ¯G(i,j )|V is a right ¯G(i,i )|V -torsor. On the other hand, the isomor-
phism Ad(g) induces an isomorphism of sheaves of groups
φ : ¯G(i,i )V
≃
− →¯G(j,j )V.
We conclude that ¯G(i,j )|V is a ¯G(j,j )|V - ¯G(i,i )|V -bitorsor. And for this bitorsor
structure, the isomorphism of sheaves of groups is φ = Ad(¯g). An easy calculation
shows that the surjection G(i,j )|V → ¯G(i,j )|V is G(j,j )|V × G(i,i )|V -equivariant.
□
Proof of the theorem. The proof is divided into several steps.
(a) Deﬁne a prestack of groupoids ¯G, and a morphism G → ¯G, as follows. For an
open set U ⊂X the object set is Ob ¯G(U ) := Ob G(U ). For a pair of objects i,j ∈
Ob ¯G(U ) let ¯G(i,j ) be the sheaf of sets from Lemma 3.14, and deﬁne ¯G(U )(i,j ) :=
Γ(U, ¯G(i,j )). Next let G/ N be the stack associated to ¯G. So G/ N is a gerbe, and
there is a weak equivalence of prestacks ¯G → G/ N . It is important to note that
even though G/ N may have more local objects than ¯G, the isomorphism sheaves
(for local objects of ¯G) are unchanged.
(b) The morphism of gerbes F : G → G/ N we get from step (a) is a weak epimor-
phism, and its kernel in N . This proves property (i).
(c) In this step we prove the existence part of property (ii). Let us deﬁne a morphism
of prestacks ¯D : ¯G → H′ as follows. On objects ¯D is just F′ ◦ D. And on
isomorphisms, for local objects i,j of ¯G, we deﬁne
¯D : ¯G(i,j ) → H′(
D(i),D (j)
)
CENTRAL EXTENSIONS OF GERBES 17
to be the unique G(i,i )-equivariant sheaf morphism making the diagram
G(i,j ) /d47/d47
D
/d15/d15
¯G(i,j )
¯D
/d15/d15
G′(
D(i),D (j)
) F ′
/d47/d47H′( ¯D(i), ¯D(j)
)
commute. Due to the universal property of stackiﬁcation, ¯D induces a morphism
of gerbes E : G/ N → H′; and then ( D,E ) is a morphism of extensions.
(d) Now we will prove that the morphism E from step (c) is unique up to 2-
isomorphism. Suppose E′ : G/ N → H′ is some other morphism such that ( D,E ′)
is a morphism of extensions. By composing the canonical morp hism ¯G → G/ N with
E′, we obtain a morphism ¯D′ : ¯G → H′. We are going to construct a 2-isomorphism
¯η : ¯D
≃
=⇒ ¯D′.
For a local object i ∈ Ob G(U ) = Ob ¯G(U ) let j := ¯D(i) ∈ Ob H′(U ) and
j′ := ¯D′(i) ∈ Ob H′(U ). So j = (F′ ◦D)(i) and j′ = (E′ ◦F )(i). Take any 2-
isomorphismη :E′ ◦F
≃
=⇒F′ ◦D. Then η induces a 2-isomorphism ¯η : ¯D
≃
=⇒ ¯D′,
which coincides with η on objects of ¯G, and is the reduction of η modulo N on
isomorphisms in ¯G.
Because G/ N is the stackiﬁcation of ¯G, and E,E ′ are the stackiﬁcations of ¯D, ¯D′
respectively, ¯η induces a 2-isomorphism E
≃
=⇒E′.
(e) Finally we shall prove property (iii). The morphism ¯D : ¯G → H′ is locally
surjective on objects. This is because ¯G and G have the same local objects; G → G′
is locally bijective on objects; and G′ → H′ is locally surjective on objects.
By construction, for any pair of local objects i,j of ¯G we have
¯G(i,j ) = G(i,j )/ N (i,i )
as sheaves of sets. On the other hand
D : N (i,i ) → N′(
D(i),D (i)
)
is an isomorphism of sheaves of groups, and
D : G(i,j ) → G′(
D(i),D (j)
)
is an isomorphism of torsors. Since
H′(
E(i),E (j)
) ∼= G′(
D(i),D (j)
)
/ N′(
D(i),D (i)
)
we see that ¯D : ¯G → H′ is a weak equivalence. Therefore E : G/ N → H′ is an
equivalence. □
Corollary 3.15. Suppose we are given extensions of gerbes
1 → N → G
F
− →H → 1
and
1 → N′ → G′ F ′
− →H′ → 1,
and a morphism of gerbes D : G → G′, such that D(N ) ⊂ N′. Then there is
a morphism of gerbes E : H → H′, unique up to 2-isomorphism, such that the
18 AMNON YEKUTIELI
diagram
1 /d47/d47N /d47/d47
/d15/d15
G
F /d47/d47
D
/d15/d15
H /d47/d47
E
/d15/d15
1
1 /d47/d47N′ /d47/d47G′
F ′
/d47/d47H′ /d47/d471
is a morphism of extensions.
Proof. By the theorem we can replace H with the equivalent gerbe G/ N . Now we
can use property (ii) of the theorem. □
Given a sheaf of groups G on X and an open set U ⊂ X, we write G(U ) :=
Γ(U, G). The center of this group is denoted by Z( G(U )). Since the center is not
functorial, one has to be careful what we mean by the center of the sheaf G. The
correct deﬁnition seems to be as follows.
Deﬁnition 3.16. Let G be a sheaf of groups on X. The center of G is the sheaf of
groups Z( G) whose group of sections on an open set U is
Z(G)(U ) := {g ∈ G (U ) |g|V ∈ Z(G(V )) for any V ⊂U }.
Proposition 3.17. Given a gerbe G, there is a unique normal subgroupoid N of
G such that
N (i,i ) = Z
(
G(i,i )
)
for every local object i of G.
The proof is like that of Proposition 3.7.
Deﬁnition 3.18. Let G be a gerbe.
(1) The normal subgroupoid N in Proposition 3.17 is called the center of G,
and it is denoted by Z( G).
(2) A central subgroupoidof G is a normal subgroupoid N of G that is contained
in Z( G).
Proposition 3.19. Let N be a central subgroupoid of G. Then there is sheaf of
abelian groups N , together with an isomorphism of sheaves of groups
(3.20) χ i : N |U → N (i,i )
for any open set U and object i ∈ Ob G(U ), satisfying this condition:
(♦) Given any i ∈ Ob G(U ), j ∈ Ob G(V ), W ⊂ U ∩V , and g ∈ G(i,j )(W ),
one has
χ j ◦ Ad(g) = χ j
as sheaf homomorphisms N |W → G (j,j )|W .
The sheaf N is unique up to a unique isomorphism.
Conversely, given a sheaf of abelian groups N , together with a collection of in-
jective sheaf homomorphisms
χ i : N |U → Z(G(i,i ))
fori ∈ Ob G(U ), that satisfy condition (♦), there exists a unique central subgroupoid
N of G such that (3.20) are isomorphisms.
Proof. This is due to the local nature of gerbes; cf. part (a) of the pr oof of Theorem
3.13. □
CENTRAL EXTENSIONS OF GERBES 19
The last proposition says that a central subgroupoid N of a gerbe G can be
viewed as a single sheaf of abelian groups.
Finally we can explain the title of the paper.
Deﬁnition 3.21. A central extension of gerbes is an extension of gerbes
1 → N − →G
F
− →H → 1
such that N is a central subgroupoid of G.
Using Proposition 3.19 to replace N with a sheaf of abelian groups N , we can
rewrite this central extension as
(3.22) 1 → N − →G
F
− →H → 1.
Here are a couple of examples of central extensions of gerbes . The ﬁrst is some-
what tautological.
Example 3.23. Suppose N is a central subgroupoid of a gerbe G. Then the
extension of gerbes
1 → N → G
F
− →G/ N → 1
from Theorem 3.13 is central.
The next example was suggested to us by the referee.
Example 3.24. Let
1 → N → G
F
− → H →1
be a central extension of sheaves of groups on X. Given an open set U and a
G|U -torsor S, let us denote by F (S) the induced H|U -torsor. This operation gives
rise to a morphism of gerbes
(3.25) F : TorsG → TorsH
(cf. Example 2.4). Since locally any H-torsor is trivial, it is locally induced from a
G-torsor. This says that (3.25) is locally essentially surje ctive on objects.
Now for any G-torsor S, locally we have a (noncanonical) isomorphism of sheaves
of groups
(TorsG)(S, S) ∼= Gop.
Likewise for H-torsors. This implies that the morphism of gerbes (3.25) is surjective
on isomorphism sheaves, and its kernel is a central subgroup oid of G, isomorphic
to the sheaf N . In this way we get a central extensions of gerbes
(3.26) 1 → N → TorsG
F
− →TorsH → 1.
