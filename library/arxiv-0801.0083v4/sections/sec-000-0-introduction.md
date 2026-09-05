---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-8
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
---
1. Recalling some Facts on 2-Categories 3
2. Prestacks on a Topological Space 8
3. Extensions of Gerbes 12
4. Obstruction Classes 19
5. Suﬃcient Conditions for Existence of Obstruction Classe s 25
6. Pronilpotent Gerbes 29
7. Fake Global Objects of Gerbes 33
References 36
0. Introduction
A gerbe G on a topological space X is the geometric version of a connected
nonempty groupoid. Thus G associates a groupoid G(U ) to any open set U ⊂X,
and to any inclusion V ⊂U of open sets there is a restriction functor G(U ) → G(V ).
These have to satisfy a lot of conditions (for the beneﬁt of th e reader we have
included a review in Section 2). Gerbes arise in various cont exts; but for us the are
mainly important as “bookkeeping devices” for certain geom etric data. At the end
of the introduction we will outline the main application we h ave in mind.
A key question is to determine if a given gerbe G is trivial, namely if Ob G(X) ⁄=
∅. When G is abelian, with band some sheaf N of abelian groups, there is an ob-
struction class in the Čech cohomology group ˇH2(X, N ) that vanishes if and only if
G is trivial. However for a nonabelian gerbe G there is no useful obstruction theory,
since the structure is too complicated. There is Giraud’s no nabelian cohomology
theory [Gi], but that does not provide an eﬀective answer.
Date: 18 February 2010.
Key words and phrases. Gerbes, central extensions, obstruction classes, nonabel ian
cohomology.
Mathematics Subject Classiﬁcation 2000. Primary: 20L05; Secondary: 18G50, 20J06, 18F20.
This research was supported by the US-Israel Binational Sci ence Foundation and the Israel
Science Foundation.
1
2 AMNON YEKUTIELI
We noticed during our work on deformation quantization that the gerbes oc-
curring there are pronilpotent (see explanation below). Such gerbes are composed
of central extensions, and for those extensions we can const ruct useful obstruction
classes.
A central extension of gerbes on X is a diagram
(0.1) 1 → N → G
F
− →H → 1,
in which G and H are gerbes, F : G → H is a weak epimorphism of gerbes,
and N = Ker(F ) is a sheaf of abelian groups in the center of G. This notion
is technically quite complicated (see Deﬁnition 3.21), but in principle it is just a
generalization of the notion of central extension of sheave s of groups
(0.2) 1 → N → G → H → 1.
Consider a central extension of gerbes (0.1). Suppose i,j are two objects of
G(X), and h :F (i) →F (j) is an isomorphism if H(X). Then there is obstruction
class
cl1
F (h) ∈ ˇH1(X, N ).
The ﬁrst main result of the paper, Theorem 4.6, says that cl 1
F (h) vanishes if and
only if h can be lifted to an isomorphism g :i →j in G(X).
Given an object j of H(X), we deﬁne (under some hypothesis) an obstruction
class
cl2
F (j) ∈ ˇH2(X, N ).
The second main result of the paper, Theorem 4.17, says that j lifts to an object
of G(X) if and only if cl 2
F (j) = 1.
There are three typical situations where central extension s of gerbes occur. The
ﬁrst is when we are given a central extension of sheaves of gro ups (0.2). This is
discussed brieﬂy in Example 3.24.
Another situation is when we take any gerbe G, and look at N := Z( G), the
center of G, which is a sheaf of abelian groups. We get a central extensio n
1 → Z(G) → G
F
− →G/ Z(G) → 1.
Global objects of G/ Z(G) are called fake global objects of G. See Section 7.
The third situation, which is the most important for us, is wh en the gerbe G is
pronilpotent, i.e. it is complete with respect to a central ﬁ ltration {N p}p∈N (see
Deﬁnition 6.5). Then for any p there is a central extension of gerbes
1 → N p/ N p+1 → G/ N p+1 → G/ N p → 1.
The obstruction classes can detect whether the groupoid ( G/ N p)(X) is nonempty
or connected for any p; but passing to the limit is more delicate. This is done in
the third main result of the paper, namely Theorem 6.10.
Presumably our results can be extended, with minor changes, to sites other than
a topological space (e.g. the étale site of a scheme). But we d id not explore this
direction.
Here is an outline of the role gerbes have in our paper [Ye]. Su ppose X is a
smooth algebraic variety over a ﬁeld K of characteristic 0. We are interested in
twisted deformations of OX . A twisted (associative or Poisson) deformation A
is a collection of locally deﬁned (associative or Poisson) d eformations Ai of OX ,
together with a collection of locally deﬁned gauge equivale nces Ai
≃
− → Aj between
them. The bookkeeping data of deformations and gauge equiva lences are encoded
CENTRAL EXTENSIONS OF GERBES 3
in the gauge gerbe G of A. Here is just a hint of how this goes – see Remark 7.4 for
a few more details, or the paper [Ye] for the full story. Let U ⊂X be an open set.
Then to any object i in the groupoid G(U ) we attach a deformation Ai of OU ; and
to any morphism g :i →j in G(U ) we attach a gauge equivalence A(g) : Ai
≃
− → Aj.
Thus the groupoid G(X) carries the information of global deformations: objects o f
G(X) correspond to global deformations of OX belonging to A, and isomorphic
objects correspond to gauge equivalent deformations. Sinc e the gauge gerbe G is
pronilpotent, we can often use Theorems 4.6, 4.17 and 6.10 to ﬁgure out how many
connected components the groupoid G(X) has.
Acknowledgments. Work on this paper began together with Fredrick Leitner,
and I wish to thank him for his contributions, without which t he paper could not
have been written. Thanks also to Lawrence Breen for reading an early version
of the paper and oﬀering valuable suggestions. Finally I wis h to thank the referee
for his/her input, and especially for discovering a subtle e rror in one of the main
results, as it was stated in a previous version of the paper.
1. Recalling some F acts on 2-Categories
There are several sources in the literature on 2-categories and prestacks, e.g.
[Be], [Gi], [Ma], [Mo], [Le], [KS] and [Br]. Unfortunately t here is disagreement
on terminology among the sources, and hence we feel it is bett er to start with an
exposition of the conventions we adopted, and a recollectio n some facts.
First we must establish some set-theoretical background, i n order to avoid para-
doxical phenomena. Recall that in set theory all mathematic al objects and opera-
tions are interpreted as sets, with suitable additional pro perties. Following [Ma] we
ﬁx a Grothendieck universe U, which is a set closed under standard set-theoretical
operations, and large enough such that the objects of intere st for us (e.g. the topo-
logical space X in Section 2) are elements of U. We refer to elements of U as small
sets. A category C such that Ob( C) ∈ U, and Hom C(C0,C 1) ∈ U for every pair
C0,C 1 ∈ Ob(C), is called a small category .
By Set we refer the category of small sets; thus in eﬀect Ob( Set) = U. Likewise
Grp, ModA etc. refer to the categories of small groups, small A-modules (over a
small ring A) etc. A category C such that Ob( C) ⊂ U, and Hom C(C0,C 1) ∈ U for
every pair C0,C 1 ∈ Ob(C), is called a U-category. Thus Set is a U-category, but it
is not small.
Next we introduce a bigger universe V, such that U ∈ V. Then Ob( Set),
Ob(Grp),... ∈ V. In order to distinguish between them, we call U the small uni-
verse, and V is the large universe. The set of all U-categories is denoted by Cat.
Note that Cat is a V-category, but (this is the whole point!) it is not a U-category.
By default sets, groups etc. will be assumed to be small; and c ategories will be
assumed to be U-categories.
A 2-category C is a “category enriched in categories” . (Some authors use th e term
“strict 2-category” .) This means the following. There is a s et Ob( C), whose ele-
ments are called objects of C. For any pair of objects C0, C1 ∈ Ob(C) there is a cat-
egory C(C0, C1). The objects of the category C(C0, C1) are called 1 -morphisms, and
the morphisms of C(C0, C1) are called 2 -morphisms. For every triple C0, C1, C2 ∈
Ob(C) there is a bifunctor
C(C0, C1) × C(C1, C2) → C(C0, C2),
4 AMNON YEKUTIELI
called horizontal composition. Horizontal composition has to be associative (as bi-
functor). For any C ∈ Ob(C) there is a distinguished 1-morphism 1C ∈ Ob
(
C(C, C)
)
,
called the identity 1-morphism of C. Horizontal composition with 1C, on either side,
is required to be the identity functor.
Given a 1-morphismF ∈ Ob
(
C(C0, C1)
)
, we writeF : C0 → C1. The notation for
horizontal composition is ◦; so given 1-morphisms F1 : C0 → C1 and F2 : C1 → C2,
their composition is F2 ◦F1 : C0 → C2. We sometimes denote the set Ob
(
C(C0, C1)
)
of 1-morphisms C0 → C1 by Hom C(C0, C1).
LetF,G ∈ Ob
(
C(C0, C1)
)
, and let η ∈ HomC(C0, C1)(F,G ); i.e. η is a 2-morphism.
We write η :F ⇒G. This data is usually depicted as a diagram:
η
/d11/d19
C0
F
/d33/d33
G
/d61/d61C1
The composition rule in the category C(C0, C1) is called vertical composition, and we
denote it by ∗. Thus if H ∈ Ob
(
C(C0, C1)
)
is another 1-morphism, and ζ :G ⇒H
is a 2-morphism, then by vertical composition we get ζ ∗η :F ⇒H.
η /d11/d19C0
F
/d33/d33G /d47/d47
H
/d61/d61ζ /d11/d19
C1 ζ∗η
/d11/d19
C0
F
/d33/d33
H
/d61/d61C1
Let us denote by 1F the identity automorphism of the object F in the category
C(C0, C1). Then 1F ∗η =η =η ∗ 1G.
The pictorial description of horizontal composition is thi s: given a diagram
η 1
/d11/d19
η 2
/d11/d19
C0
F1
/d33/d33
G1
/d61/d61C1
F2
/d33/d33
G2
/d61/d61C1
the horizontal composition of the 2-morphisms η 1 and η 2 is
η 2◦η 1
/d11/d19
C0
F2◦F1
/d33/d33
G2◦G1
/d61/d61C2
The horizontal and vertical compositions are required to sa tisfy the following
condition, called the exchange condition. Suppose we are given a diagram
η 1 /d11/d19 η 2 /d11/d19C0
F1
/d33/d33G1 /d47/d47
H1
/d61/d61ζ 1 /d11/d19
C1
F2
/d34/d34G2 /d47/d47
H2
/d60/d60ζ 2 /d11/d19
C2
CENTRAL EXTENSIONS OF GERBES 5
in C. Then
(ζ 2 ◦ζ 1) ∗ (η 2 ◦η 1) = (ζ 2 ∗η 2) ◦ (ζ 1 ∗η 1)
as 2-morphisms F2 ◦F1 ⇒H2 ◦H1.
Regarding set-theoretical issues, we require that Ob( C) ⊂ V, Ob
(
C(C0, C1)
)
∈ V,
and Hom C(C0, C1)(F,G ) ∈ U. Note that if we forget the 2-morphisms in C, then C
becomes a V-category.
The basic example of a 2-category is this:
Example 1.1. The 2-category of U-categories, denoted by Cat. The set Ob( Cat)
of all U-categories was already mentioned. The 1-morphisms in Cat(C0, C1) are the
functors F : C0 → C1 between these categories. And the 2-morphisms η : F ⇒G
are the natural transformations. The composition rules are the usual ones.
Here is another example, of a diﬀerent ﬂavor.
Example 1.2. Let K be a commutative ring. The category DGMod K of DG
(diﬀerential graded) K-modules can be made into a 2-category, as follows. Given
M,N ∈ Ob(DGMod K), the 1-morphisms F :M →N are the usual morphisms in
DGMod K, i.e. K-linear DG module homomorphisms. Now such a homomorphism
F :M →N can be viewed as a 0-cocycle in the DG module Hom K(M,N ). Given
another such homomorphism G : M → N , the 2-morphisms η : F ⇒ G are by
deﬁnition the 0-coboundaries η ∈ HomK(M,N ) such that G =η +F . Compositions
are obvious.
Suppose F,G ∈ HomC(C0, C1). We say that F and G are 2 -isomorphic if there
is some 2-isomorphism η : F
≃
=⇒G in the category Hom C(C0, C1); we denote this
byF
≃
⇐ ⇒G. A diagram (of 1-morphisms)
C0
D /d47/d47
F /d32/d32/d65/d65/d65/d65/d65/d65/d65 C1
E
/d15/d15
C2
is commutative up to 2-isomorphism if E ◦D
≃
⇐ ⇒F .
There is an intrinsic notion of equivalence in a 2-category C. A 1-morphism
F : C → D is an called an equivalence if there is a 1-morphism G : D → C such that
G ◦F
≃
⇐ ⇒1C and F ◦G
≃
⇐ ⇒1D. This generalizes the usual notion of equivalence
(of categories) in Example 1.1.
Suppose C and D are 2-categories. A 2 -functor F : C → D is a triple F =
(F0,F 1,F 2), consisting of functions of the following kinds. The funct ion F0, called
the 0-component of F , assigns to each object C ∈ Ob C, an object F0(C) ∈ Ob D.
The function F1 assigns to each morphism G : C0 → C1 in C, a 1-morphism
F1(G) : F0(C0) →F0(C1)
in D. And the function F2 assigns to each 2-morphism η : G ⇒ G′ in C, a 2-
morphism
F2(η ) : F1(G) ⇒F1(G′)
in D. The condition is that the functions ( F0,F 1,F 2) preserve compositions and
units. Thus, if we forget 2-morphisms, the pair ( F0,F 1) is a functor
(F0,F 1) : C → D
6 AMNON YEKUTIELI
between these categories. And for every C0, C1 ∈ Ob C, the pair (F1,F 2) is a functor
(F1,F 2) : Hom C(C0, C1) → HomD
(
F0(C0),F 0(C1)
)
.
Let C and D be 2-categories, and let F, G : C → D be 2-functors, with compo-
nents
F = (F0,F 1,F 2), G = (G0,G 1,G 2).
A 1-morphism (sometimes called a 2-natural transformation ) p : F → G is a
function that assigns to each C ∈ Ob C a 1-morphism
pC :F0(C) →G0(C)
in D, such that for every E ∈ HomC(C0, C1) one has
pC1 ◦F1(E) = G1(E) ◦ pC0
in Hom D
(
F0(C0),G 0(C1)
)
. Given another 2-functor H : C → D, and a 1-morphism
q : G → H, the composition q ◦ p : F → H is deﬁned in the obvious way.
Now suppose p, q : F → G are 1-morphisms between 2-functors F, G : C → D
as above. A 2-morphism η : p → q (sometimes called a modiﬁcation) is a function
that assigns to each C ∈ Ob C, a 2-morphism η C : pC ⇒ qC in HomD
(
F0(C),G 0(C)
)
.
The condition is that
η C1 ◦ pC1 ◦ F = η C0 ◦ qC0 ◦ G,
as functions
HomC(C0, C1) → HomD
(
F0(C0),G 0(C1)
)
.
If r : F → G is yet another 1-morphism, and ζ : q → r is a 2-morphism, then
the composition ζ ∗ η : p → r is deﬁned in the obvious way. We say that the
2-morphism η : p → q is a 2-isomorphism if each η C is a 2-isomorphism.
A 2-functor F : C → D is called a 2 -equivalence if there is a 2-functor G : D → C,
and 2-isomorphisms G ◦ F
≃
=⇒ 1C and F ◦ G
≃
=⇒ 1D. If a 2-equivalence C → D
exists, then we say that C and D are 2-equivalent.
One could make the set of all 2-categories, with the operatio ns deﬁned above,
into a 2-category, but that would take us outside of the large universe V. Therefore
we shall be careful to consider only “small collections” of 2 -categories in this paper.
We shall also need to recall what are pseudofunctors (sometimes called nor-
malized pseudofunctors, or morphisms of bicategories) fro m a category N to a 2-
category C. A pseudofunctor F : N → C is a triple F = (F0,F 1,F 2), consisting
of functions of the following kinds. The function F0, called the 0-component of F ,
assigns to each object N ∈ Ob N an object F0(N ) ∈ Ob C. The function F1 assigns
to each morphism f :N0 →N1 in N a 1-morphism
F1(f ) : F0(N0) →F0(N1)
in C. And the function F2 assigns to each composable pair of morphisms
N0
f1
− →N1
f2
− →N2
in N, a 2-isomorphism
F2(f1,f 2) : F1(f2) ◦F1(f1)
≃
=⇒F1(f2 ◦f1)
in C. Here are the conditions. First,
(1.3) F2(f2 ◦f1,f 3) ∗F2(f1,f 2) = F2(f1,f 3 ◦f2) ∗F2(f2,f 3)
CENTRAL EXTENSIONS OF GERBES 7
for any composable triple
N0
f1
− →N1
f2
− →N2
f3
− →N3
of morphisms in N. Next, for any object N ∈ N, with identity morphism 1N , it is
required that F1(1N ) = 1F0(N ), the identity 1-morphism of F0(N ). And lastly, the
2-isomorphisms
F2(1N0,f 1) : F1(f1) ◦ 1F0(N0)
≃
=⇒F1(f1)
and
F2(f1, 1N1) : 1F0(N1) ◦F1(f1)
≃
=⇒F1(f1)
have to be the identity 2-automorphism of the 1-morphism F1(f1).
The ﬁnal abstract 2-categorical fact that we need is that giv en a small category
N and a 2-category C, the set of all pseudofunctors F : N → C is itself a 2-
category. The 1-morphisms are deﬁned as follows. Suppose F, G : N → C are
pseudofunctors, with components F = (F0,F 1,F 2) and G = (G0,G 1,G 2). A 1-
morphism p : F → G is a pair p = (p1,p 2), whose 1-component p1 is a function
assigning to any object N ∈ Ob N a 1-morphism
p1(N ) : F0(N ) →G0(N )
in C; and the 2-component p2 is a function assigning to any morphism f :N0 →N1
in N a 2-isomorphism
p2(f ) : p1(N1) ◦F1(f )
≃
=⇒G1(f ) ◦p1(N0)
in C. These are required to satisfy the condition
(1.4) p2(f2 ∗f1) ∗F2(f1,f 2) = G2(f1,f 2) ∗p2(f1) ∗p2(f2)
in Hom C
(
F0(N0),G 0(N1)
)
, for any composable pair of morphisms N0
f1
− →N1
f2
− →
N2 in N.
Horizontal composition of 1-morphisms is deﬁned as follows . Suppose H : N → C
is another pseudofunctor, and q : G → H is a 1-morphism. Their components are
H = (H0,H 1,H 2) and q = (q1,q 2). Let
r1(N ) : F0(N ) →H0(N )
be the 1-morphism
r1(N ) := q1(N ) ◦p1(N ),
and let
r2(f ) : r1(N1) ◦F1(f ) ⇒H1(f ) ◦r1(N0)
be the 2-morphism
r2(f ) := q2(f ) ∗p2(f ).
Then we deﬁne the 1-morphism
q ◦ p : F → H
to be
q ◦ p := (r1,r 2).
Next consider 1-morphisms p, q : F → G. A 2-morphism η : p ⇒ q has only
a 2-component η 2, which is a function that assigns to each object N ∈ Ob N a
2-morphism
η 2(N ) : p1(N ) ⇒q1(N )
8 AMNON YEKUTIELI
in C. The condition is that
q2(f ) ∗η 2(N0) = η 2(N1) ∗p2(f )
for any f : N0 → N1 in N. Given yet another 1-morphism r : F → G, and a
2-morphism ζ = (ζ 2) : q ⇒ r, the vertical composition θ := ζ ∗ η : p ⇒ r has
2-component
θ 2(N ) := ζ 2(N ) ∗η 2(N ).
