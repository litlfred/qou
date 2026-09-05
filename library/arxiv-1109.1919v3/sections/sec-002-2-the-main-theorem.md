---
doc_id: arxiv-1109.1919v3
doc_title: "COMBINATORIAL DESCENT DATA FOR GERBES AMNON YEKUTIELI"
section_id: sec-002-2-the-main-theorem
section_title: "The Main Theorem"
section_number: 2
pages: 5-10
source_pdf: 1109.1919v3.pdf
source_sha256: 2b634edddf232047
doc_brief: "COMBINATORIAL DESCENT DATA FOR GERBES AMNON YEKUTIELI — We consider descent data in cosimplicial crossed groupoids."
---
Recall that for a groupoidG, the set of isomorphism classes of objects is denoted
byπ0(G).
Deﬁnition 2.1.Let G = (G1,G 2, AdG1↷G2, D) be a crossed groupoid. We deﬁne
the homotopy set
π0(G) :=π0(G1),
and the homotopy groups
π1(G,x ) := Coker
(
D :G2(x)→G1(x)
)
and
π2(G,x ) := Ker
(
D :G2(x)→G1(x)
)
for x∈Ob(G).
The setπ0(G) and the groupsπi(G,x ) are functorial inG. The groupπ2(G,x )
is central inG2(x), and in particular it is abelian.
Deﬁnition 2.2.A morphism of crossed groupoids Φ : G→H is called a weak
equivalenceif the function
π0(Φ) : π0(G)→π0(H)
is bijective, and the group homomorphisms
πi(Φ,x ) :πi(G,x )→πi(H, Φ(x))
are bijective for allx∈Ob(G) and i∈{1, 2}.
Deﬁnition 2.3.A morphism Φ : G →H of cosimplicial crossed groupoids is
called aweak equivalenceif in every simplicial dimensionp the morphism of crossed
groupoids Φ p :Gp→H p is a weak equivalence.
6 AMNON YEKUTIELI
Theorem 2.4(Equivalence). Let Φ : G→H be a weak equivalence between cosim-
plicial crossed groupoids. Then the function
Desc(Φ) : Desc(G)→Desc(H)
from Deﬁnition1.8 is bijective.
We need a couple of auxiliary results ﬁrst. A partial descent datum inG is a pair
(x,g ) of elementsx∈Ob(G0) and g∈G1
1(x(0),x (1)) (cf. Deﬁnition 1.5). Let(x,g )
and (x′,g′) be partial descent data. A partial gauge transformation(x,g )→(x′,g′)
is a pair (f,c ) of elements as in Deﬁnition 1.6, that satisﬁes condition (i) of that
deﬁnition.
The next lemma is a sort of “Kan condition” satisﬁed byDesc(G).
Lemma 2.5. Let (x,g,a ) be a descent datum in the cosimplicial crossed groupoid
G, let(x′,g′) be a partial descent datum inG, and let(f,c ) be a partial gauge trans-
formation (x,g )→(x′,g′). Then there is a unique elementa′∈G2
2(x′
(0)) such that
the triple (x′,g′,a′) is a descent datum inG, and (f,c ) is a gauge transformation
(x,g,a )→(x′,g′,a′).
Proof. Deﬁne
a′:= Ad(f(0))
(
c−1
(0,2)◦a◦Ad(g−1
(0,1))(c(1,2))◦c(0,1)
)
∈G2
2(x′
(0)).
Then a′satisﬁes condition (ii) of Deﬁnition 1.6, and moreover it is unique.
We have to show that the triple(x′,g′,a′) is a descent datum. Let us check
condition (i) of Deﬁnition 1.5. We have
(g′
(0,2))−1◦g′
(1,2)◦g′
(0,1)
∆
=
(
f(2)◦g(0,2)◦D(c(0,2))◦f−1
(0)
)−1
◦
(
f(2)◦g(1,2)◦D(c(1,2))◦f−1
(1)
)
◦
(
f(1)◦g(0,1)◦D(c(0,1))◦f−1
(0)
)
♦
=f(0)◦D(c(0,2))−1◦g−1
(0,2)◦g(1,2)◦D(c(1,2))◦g(0,1)◦D(c(0,1))◦f−1
(0)
♥
= Ad(f(0))
(
D(c−1
(0,2))◦D(a)◦g−1
(0,1)◦D(c(1,2))◦g(0,1)◦D(c(0,1))
)
⋆
= Ad(f(0))
(
D(c−1
(0,2))◦D(a)◦Ad(g−1
(0,1))(D(c(1,2)))◦D(c(0,1))
)
□
= D
(
Ad(f(0))
(
c−1
(0,2)◦a◦Ad(g−1
(0,1))(c(1,2))◦c(0,1)
))▽
= D(a′).
The equality marked
∆
= is true because of condition (i) of Deﬁnition 1.6, applied
to the elementsg′
(i,j). The equality marked
♦
= is true because of cancellation. The
equality marked
♥
= is because condition (i) of Deﬁnition 1.5 holds for(x,g,a ),
and by the deﬁnition ofAd(f(0)). The equality marked
⋆
= is by the deﬁnition of
Ad(g−1
(0,1)). The equality marked
□
= is becauseD isG2
1-equivariant (this is condition
(i) of Deﬁnition 1.2). And the equality marked
▽
= holds by deﬁnition ofa′.
Finally we have to check that condition (ii) of Deﬁnition 1.5 holds for(x′,g′,a′).
Namely, letting
(2.6) u′:= (a′
(0,1,3))−1◦a′
(0,2,3)◦a′
(0,1,2)◦Ad
(
(g′
(0,1))−1)
(a′
(1,2,3))−1,
we have to show thatu′= 1.
COMBINATORIAL DESCENT DATA 7
From the deﬁnition ofa′we get
(2.7)
Ad
(
(g′
(0,1))−1)
(a′
(1,2,3))
= Ad
(
(g′
(0,1))−1◦f(1)
)(
c−1
(1,3)◦a(1,2,3)◦Ad(g−1
(1,2))(c(2,3))◦c(1,2)
)
♥
= Ad
(
f(0)◦D(c−1
(0,1))◦(g(0,1))−1)
(
c−1
(1,3)◦a(1,2,3)◦Ad(g−1
(1,2))(c(2,3))◦c(1,2)
)
♦
=
(
Ad(f(0))◦Ad(D(c−1
(0,1)))◦Ad(g(0,1))−1)
(
c−1
(1,3)◦a(1,2,3)◦Ad(g−1
(1,2))(c(2,3))◦c(1,2)
)
□
= Ad
(
f(0)
)(
c−1
(0,1)◦Ad
(
g−1
(0,1)
)
(c−1
(1,3))◦Ad
(
g−1
(0,1)
)
(a(1,2,3))
◦Ad
(
g−1
(0,1)◦g−1
(1,2)
)
(c(2,3))◦Ad
(
g−1
(0,1)
)
(c(1,2))◦c(0,1)
)
.
The equality marked
♥
= is true because
(g′
(0,1))−1◦f(1) =f(0)◦D(c−1
(0,1))◦(g(0,1))−1;
this is from condition (i) of Deﬁnition 1.6. The equality marked
♦
= is because Ad
is a group homomorphism. And
□
= is because Ad(D(c−1
(0,1))) = Ad(c−1
(0,1)), which is
an instance of condition (ii) of Deﬁnition 1.2.
A consequence of condition (ii) of Deﬁnition 1.5 and condition (ii) of Deﬁnition
1.2 is that
a−1
(0,1,2)◦c◦a(0,1,2) = Ad(a−1
(0,1,2))(c)
= Ad(D(a−1
(0,1,2)))(c) = Ad(g−1
(0,1)◦g−1
(1,2)◦g(0,2))(c)
for anyc∈G2
2(x(0)). Therefore, takingc := Ad(g−1
(0,2))(c(2,3)), we get
(2.8) Ad(g−1
(0,2))(c(2,3))◦a(0,1,2) =a(0,1,2)◦Ad(g−1
(0,1)◦g−1
(1,2))(c(2,3)).
By the deﬁnition ofa′and by formula (2.7) we have
u′= Ad(f(0))
(
c−1
(0,3)◦a(0,1,3)◦Ad(g−1
(0,1))(c(1,3))◦c(0,1)
)−1
◦Ad(f(0))
(
c−1
(0,3)◦a(0,2,3)◦Ad(g−1
(0,2))(c(2,3))◦c(0,2)
)
◦Ad(f(0))
(
c−1
(0,2)◦a(0,1,2)◦Ad(g−1
(0,1))(c(1,2))◦c(0,1)
)
◦Ad
(
f(0)
)(
c−1
(0,1)◦Ad
(
g−1
(0,1)
)
(c−1
(1,3))◦Ad
(
g−1
(0,1)
)
(a(1,2,3))
◦Ad
(
g−1
(0,1)◦g−1
(1,2)
)
(c(2,3))◦Ad
(
g−1
(0,1)
)
(c(1,2))◦c(0,1)
)−1
.
Canceling adjacent inverse terms we get
u′= Ad(f(0))
(
c−1
(0,1)◦Ad(g−1
(0,1))(c−1
(1,3))◦v′◦Ad
(
g−1
(0,1)
)
(c(1,3))◦c(0,1)
)
,
where
v′:=a−1
(0,1,3)◦a(0,2,3)◦Ad(g−1
(0,1)◦g−1
(1,2))(c(2,3))◦a(0,1,2)
◦Ad
(
g−1
(0,1)◦g−1
(1,2)
)
(c−1
(2,3))◦Ad
(
g−1
(0,1)
)
(a−1
(1,2,3)) .
It suﬃces to prove thatv′= 1. Using formula (2.8) we have
v′=a−1
(0,1,3)◦a(0,2,3)◦a(0,1,2)◦Ad(g−1
(0,1)◦g−1
(1,2))(c(2,3))
◦Ad
(
g−1
(0,1)◦g−1
(1,2)
)
(c−1
(2,3))◦Ad
(
g−1
(0,1)
)
(a−1
(1,2,3)) .
8 AMNON YEKUTIELI
We now cancel two adjacent inverse terms, and use the fact that condition (ii) of
Deﬁnition 1.5 holds for(x,g,a ), to conclude thatv′= 1. □
Suppose G is a crossed groupoid andx,x′∈Ob(G). There is a right action of
the groupG2(x) on the setG1(x,x′), namelyg↦→g◦D(a) for g∈G1(x,x′) and
a∈G2(x). The quotient set is
(2.9) π1(G,x,x′) :=G1(x,x′)/G2(x).
Giveng,g′∈G1(x,x′) let us deﬁne
(2.10) G2(x)(g,g′) :={a∈G2(x)|g′=g◦D(a)}.
Soπ1(G,x,x ) =π1(G,x ) and G2(x)(1x, 1x) =π2(G,x ) in the notation of Deﬁni-
tion 2.1.
Lemma 2.11. Let Φ : G→H be a weak equivalence between crossed groupoids.
Then the induced functions
π1(Φ,x,x′) :π1(G,x,x′)→π1
(
H, Φ(x), Φ(x′)
)
and
Φ : G2(x)(g,g′)→H2
(
Φ(x)
)(
Φ(g), Φ(g′)
)
are bijective for allx,x′∈Ob(G) and f,f′∈G1(x,x′).
Proof. This is the same as the usual proof for2-groupoids (cf. [MS, Lemma 1.1]).
□
Proof of Theorem2.4. The proof is a “nonabelian diagram chasing”, made possible
by Lemma 2.5.
We begin by proving that the functionDesc(Φ) is surjective. Given a descent
datum (y,h,b )∈Desc(H), we have to ﬁnd a descent datum(x,g,a )∈Desc(G),
and a gauge transformation(f,c ) : (y,h,b )→Φ(x,g,a ) in H.
Since the functionπ0(Φ 0) : π0(G0)→π0(H0) is surjective, there is an object
x∈Ob(G0), and a1-morphism f∈H0
1(y,y′), wherey′:= Φ(x)∈Ob(H0). Deﬁne
h′′:=f(1)◦h◦f−1
(0)∈H0
1(y′
(0),y′
(1))
and c′′:= 1 y(0) ∈H1
2(y(0)). Then (y′,h′′) is a partial descent datum inH, and
(f,c′′) : (y,h )→(y′,h′′) is a partial gauge transformation. According to Lemma
2.5 there is a unique elementb′′∈H2
2(y′
(0)) such that(y′,h′′,b′′) is a descent datum
in H, and (f,c′′) : (y,h,b )→(y′,h′′,b′′) is a gauge transformation.
Now by Lemma 2.11 the function
π1(Φ 1,x (0),x (1)) :π1(G1,x (0),x (1))→π1(H1,y′
(0),y′
(1))
is surjective. Hence there are elements g ∈G1
1(x(0),x (1)) and c′∈H1
2(y′
(0))
such that, letting h′:= Φ( g) ∈H1
1(y′
(0),y′
(1)), we have h′′= h′◦D(c′). Con-
sider the partial gauge transformation (1y′,c′) : ( y′,h′′)→(y′,h′). Lemma 2.5
there is a unique element b′∈H2
2(y′
(0)) such that (y′,h′,b′) is a descent da-
tum in H, and (1y′,c′) : (y′,h′′,b′′)→(y′,h′,b′) is a gauge transformation. Let
c := Ad(f−1
(0) )(c′)−1∈H1
2(y(0)). Then
(f,c ) : (y,h,b )→(y′,h′,b′)
is a gauge transformation inH, and (y′,h′) = Φ(x,g ).
By Lemma 2.11 the function
Φ 2 :G2
2(x(0))
(
1x(0),g−1
(0,2)◦g(1,2)◦g(0,1)
)
→H2
2(y′
(0))
(
1y′
(0)
, (h′
(0,2))−1◦h′
(1,2)◦h′
(0,1)
)
COMBINATORIAL DESCENT DATA 9
is bijective. Leta∈G2
2(x(0)) be the unique element such that
D(a) =g−1
(0,2)◦g(1,2)◦g(0,1)
and Φ(a) =b′. Then the triple of elements(x,g,a ) satisﬁes condition (i) of Deﬁni-
tion 1.5, andΦ(x,g,a ) = (y′,h′,b′). Now the element
u :=a−1
(0,1,3)◦a(0,2,3)◦a(0,1,2)◦Ad(g−1
(0,1))(a(1,2,3))−1∈G3
2(x(0))
satisﬁesD(u) = 1, so it belongs to the subgroupπ2(G3,x (0))⊂G3
2(x(0)). Since the
group homomorphism
π2(Φ 3,x (0)) :π2(G3,x (0))→π2(H3,y′
(0))
is injective, and since
π2(Φ 3,x (0))(u) = Φ 3(u) =
(b′
(0,1,3))−1◦b′
(0,2,3)◦b′
(0,1,2)◦Ad(h′
(0,1))−1(b′
(1,2,3))−1 = 1,
we conclude thatu = 1. Thus the triple(x,g,a ) satisﬁes condition (ii) of Deﬁnition
1.5, so it is a descent datum inG.
Now we prove that the functionDesc(Φ) is injective. Given
(x,g,a ), (x′,g′,a′)∈Desc(G),
deﬁne(y,h,b ) := Φ( x,g,a ) and (y′,h′,b′) := Φ( x′,g′,a′). Assume we are given a
gauge transformation
(f,c ) : (y,h,b )→(y′,h′,b′)
in H. We have to produce a gauge transformation
(e,d ) : (x,g,a )→(x′,g′,a′)
in G.
We know that the function
π1(Φ 0,x,x′) :π1(G0,x,x′)→π1
(
H0,y,y ′)
is surjective. Therefore there is a 1-morphism e∈G0
1(x,x′), and a 2-morphism
v∈H0
2(y), such thatΦ(e) =f◦D(v). Let
˜f :=f◦D(v)∈H0
1(y,y′)
and
˜c := Ad(h−1)(v−1
(1))◦c◦v(0)∈H0
2(y(0)).
A simple calculation shows that
( ˜f, ˜c) : (y,h,b )→(y′,h′,b′)
is also a gauge transformation.
Recall that Φ(e) = ˜f, so
Φ(g−1◦e−1
(1)◦g′◦e(0)) =h−1◦˜f−1
(1)◦h′◦˜f(0) = D(˜c).
This is condition (i) of Deﬁnition 1.6 for the gauge transformation( ˜f, ˜c). Because
the group homomorphism
π1(Φ 1,x (0)) :π1(G1,x (0))→π1(H1,y (0))
is injective, it follows that there is an elementd′∈G1
2(x(0)) such that
g−1◦e−1
(1)◦g′◦e(0) = D(d′).
Consider the elementw := ˜c◦Φ(d′)−1 ∈H1
2(y(0)). It satisﬁes D(w) = 1 , so it
belongs to the subgroupπ2(H1,y (0)). But the homomorphism
π2(Φ 1,x (0)) :π2(G1,x (0))→π2(H1,y (0))
10 AMNON YEKUTIELI
is bijective, so there is a unique elementv ∈G1
2(x(0)) satisfying D(v) = 1 and
Φ(v) =w. Letd :=v◦d′∈G1
2(x(0)). Then Φ(d) = ˜c and
D(d) = D(d′) =g−1◦e−1
(1)◦g′◦e(0).
Thus the pair(e,d ) is a partial gauge transformation(x,g )→(x′,g′).
The last thing to check is that condition (ii) of Deﬁnition 1.6 holds for(e,d ).
Let
u := Ad(e−1
(0))(a′)−1◦d−1
(0,2)◦a◦Ad(g−1
(0,1))(d(1,2))◦d(0,1)∈G2
2(x(0)).
A direct calculation shows thatD(u) = 1 x(0)∈G2
1(x(0)), sou∈π2(G2,x (0)). We
know that Φ(u) = 1y(0), and that the homomorphism
π2(Φ 2,x (0)) :π2(G2,x (0))→π2(H2,y (0))
is injective. It follows thatu = 1x(0), which is what we had to check. □
