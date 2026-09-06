---
doc_id: arxiv-math-0505170v2
doc_title: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-8
source_pdf: math0505170.pdf
source_sha256: 0846b74f9c7c55cb
doc_brief: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS AMNON YEKUTIELI — W e present an averaging process for sections of a torsor unde r a unipotent group."
---
Let K be a ﬁeld of characteristic 0. For any natural number q let K[t0, . . . , t q]
be the polynomial algebra, and let ∆ q
K be the geometric q-dimensional simplex
∆ q
K := Spec K[t0, . . . , t q]/ (t0 + · · ·+ tq − 1).
Our main result is the following theorem.
Theorem 0.1. Let G be a unipotent algebraic group over K, let X be a K-scheme,
let Z be a G-torsor over X, and let Y be any X-scheme. Suppose f = (f0, . . . , f q)
is a sequence of X-morphisms fi : Y → Z. Then there is an X-morphism
wavG(f ) : ∆ q
K × Y → Z
called the weighted average, such that the operation wavG is symmetric, simplicial,
functorial in the data (G, X, Y, Z ), and is the identity for q = 0.
“Symmetric” means that wav G is equivariant for the action of the permutation
group of {0, . . . , q } on the sequence f and the scheme ∆ q
K. “Simplicial” says that
as q varies
wavG : Hom X (Y, Z )q+1 → HomX (∆ q
K × Y, Z )
is a map of simplicial sets. “Functorial in the data ( G, X, Y, Z )” means that e.g.
given a morphism h : Z → Z′ of G-torsors over X, one has
h ◦ wavG(f ) = wav G(h ◦ f ),
where h ◦ f is the sequence ( h ◦ f0, . . . , h ◦ fq). Theorem 0.1 is repeated, in full
detail, as Theorem 1.11.
Observe that when we restrict the morphism wav G(f ) to each of the vertices
of ∆ q
K we recover the original morphisms f0, . . . , f q. This is due to the simplicial
property of wavG. Thus wav G(f ) interpolates between f0, . . . , f q. This is illustrated
in Figure 1.
Date: 12 January 2006.
Key words and phrases. Unipotent group, torsor, simplicial set.
Mathematics Subject Classiﬁcation 2000. Primary: 14L30; Secondary: 18G30, 20G15.
This work was partially supported by the US - Israel Bination al Science Foundation.
1
2 AMNON YEKUTIELI
Here is a naive corollary of Theorem 0.1, which can further ex plain the result.
Let us write G(K) for the group of K-rational points of G. By a weight sequence in
K we mean a sequence w = (w0, . . . , w q) of elements of K such that ∑ wi = 1.
Corollary 0.2. Let G be a unipotent group over K. Suppose Z is a set with
G(K)-action which is transitive and has trivial stabilizers. Le t z = (z0, . . . , z q) be a
sequence of points in Z and let w be a weight sequence in K. Then there is a point
wavG, w(z) ∈ Z called the weighted average. The operation wavG is symmetric,
functorial, simplicial, and is the identity for q = 0.
The corollary is proved in Section 1. The idea is of course to t ake Y = X :=
Spec K in the theorem, and to note that w is a K-rational point of ∆ q
K.
Another consequence of Theorem 0.1 is a new proof of the fact t hat a unipotent
group in characteristic 0 is special. See Remark 1.12. (This observation is due to
Reichstein.)
Theorem 0.1 was discovered in the course of research on defor mation quantization
in algebraic geometry [Ye], in which we tried to apply ideas o f Kontsevich [Ko] to
the algebraic context. Here is a brief outline. Suppose X is a smooth n-dimensional
K-scheme. The coordinate bundle of X [GK, Ko] is an inﬁnite dimensional bundle
Z → X which parameterizes formal coordinate systems on X. The bundle Z is a
torsor under an aﬃne group scheme GL n, K ⋉ G, where G is pro-unipotent. One
is interested in sections of the quotient bundle ¯Z := Z/ GLn, K. If we are in the
diﬀerentiable setup (i.e. K = R and X is a C∞ manifold) then the ﬁbers of ¯Z are
contractible (since they are isomorphic to G(R)), and therefore global C ∞ sections
exist. However in the setup of algebraic geometry such an arg ument is invalid, and
we were forced to seek an alternative approach.
Our solution was to use simplicial sections of ¯Z (see Section 2, and especially
Corollary 2.7). This approach was inspired by work of Bott [B o] on simplicial
connections (cf. also [HY]).
Acknowledgments. The author thanks David Kazhdan and Zinovy Reichstein
for useful conversations. Also thanks to the referee for rea ding the paper carefully
and suggesting a few improvements.
1. The A veraging Process
Throughout the paper K denotes a ﬁxed base ﬁeld of characteristic 0. All schemes
and all morphisms are over K.
We begin by recalling some standard facts about the combinat orics of simplicial
objects. Let ∆ denote the category with objects the ordered sets [ q] := {0, 1, . . . , q },
q ∈ N. The morphisms [ p] → [q] are the order preserving functions, and we write
∆ q
p := Hom∆ ([p], [q]). The i-th co-face map ∂ i : [p] → [p+1] is the injective function
that does not take the value i; and the i-th co-degeneracy map s i : [ p] → [p − 1]
is the surjective function that takes the value i twice. All morphisms in ∆ are
compositions of various ∂ i and s i.
An element of ∆ q
p may be thought of as a sequence i = ( i0, . . . , i p) of integers
with 0 ≤ i0 ≤ · · · ≤ip ≤ q. Given i ∈ ∆ m
q , j ∈ ∆ p
m and α ∈ ∆ q
p, we sometimes
write α∗(i) := i ◦ α ∈ ∆ m
p and α∗(j) := α ◦ j ∈ ∆ q
m.
Let C be some category. A cosimplicial object in C is a functor C : ∆ → C. We
shall usually refer to the cosimplicial object as C = {Cp}p∈N, and for any α ∈ ∆ q
p
the corresponding morphism in C will be denoted by α∗ : Cp → Cq. A simplicial
AN A VERAGING PROCESS 3
object in C is a functor C : ∆ op → C. The notation for a simplicial object will be
C = {Cp}p∈N and α∗ : Cq → Cp.
An important example is the cosimplicial scheme {∆ p
K}p∈N. The morphisms are
deﬁned as follows. For any p we identify the ordered set [ p] with the set of vertices
of ∆ p
K. Given α ∈ ∆ q
p the morphism α∗ : ∆ p
K → ∆ q
K is then the unique linear
morphism extending α : [p] → [q].
Let G be a unipotent (aﬃne ﬁnite type) algebraic group over K, with (nilpotent)
Lie algebra g. We write d(G) for the minimal number d such that there exists a
chain of closed normal subgroups G = G0 ⊃ G1 · · · ⊃Gd = 1 with Gk/G k+1 abelian
for all k ∈ {0, . . . , d − 1}. The exponential map exp G : g → G is an isomorphism of
schemes, with inverse log G; see [Ho, Theorem VIII.1.1].
Given a K-scheme X there is a Lie algebra g× X (in the category of X-schemes),
and a group-scheme G × X. There is also an induced exponential map
expG×X := exp G ×1X : g × X → G × X.
We will need the following result.
Lemma 1.1. Let G, G′ be two unipotent groups, with Lie algebras g, g′. Let X, X′
be schemes, let X → X′ be a morphism of schemes, and let φ : G × X → G′ × X′
be a morphism of group-schemes over X′. Denote by dφ : g × X → g′ × X′ the
induced Lie algebra morphism (the diﬀerential of φ ). Then the diagram
(1.2)
g × X
expG×X
− − − − − →G × X
dφ
↓ φ
↓
g′ × X′ expG′ ×X′
− − − − − − →G′ × X′
commutes.
Proof. For the case X = X′ = Spec K this is contained in the proof of [Ho, Theorem
VIII.1.2].
In order to handle the general case we ﬁrst recall the Campbel l-Baker-Hausdorﬀ
formula:
expG(γ 1) ·expG(γ 2) = exp G(F (γ 1, γ 2)),
where
F (γ 1, γ 2) = γ 1 + γ 2 + 1
2 [γ 1, γ 2] + · · ·
is a universal power series (see [Ho, Section XVI.2]). Hence if we deﬁne γ 1 ∗ γ 2 :=
F (γ 1, γ 2), then ( g, ∗) becomes an algebraic group (with unit element 0), and exp G :
(g, ∗) → (G, ·) is a group isomorphism. In this way we may eliminate G altogether,
and just look at the scheme g with its two structures: a Lie algebra and a group-
scheme. Note that now g is its own Lie algebra, as can be seen from the 2-nd order
term in the series F (γ 1, γ 2).
Consider a morphism φ : g × X → g′ × X′ of X′-schemes. Then φ is a morphism
of Lie algebras over X′ iﬀ it is a morphism of group-schemes (for the multiplication s
∗). And moreover d φ = φ . Therefore the diagram (1.2) is commutative. □
From now on we shall write exp G instead of exp G×X, for the sake of brevity.
Consider the following setup: X is a K-scheme, and Y, Z are two X-schemes.
Suppose Z is a torsor under the group scheme G × X. We denote the action of G
on Z by ( g, z ) ↦→g ·z.
4 AMNON YEKUTIELI
Let f0, . . . , f q : ∆ q
K × Y → Z be X-morphisms. We are going to deﬁne a new
sequence of X-morphisms f′
0, . . . , f ′
q : ∆ q
K × Y → Z. Because Z is a torsor under
G × X, for any i, j ∈ {0, . . . , q } there exists a unique morphism gi,j : ∆ q
K × Y → G
such that fj(w, y ) = gi,j (w, y ) ·fi(w, y ) for all points w ∈ ∆ q
K and y ∈ Y . Here
w and y are scheme-theoretic points, i.e. w ∈ ∆ q
K(U ) = Hom K(U, ∆ q
K) and y ∈
Y (U ) = Hom K(U, Y ) for some K-scheme U . Deﬁne
(1.3) f′
i (w, y ) := exp G
( q∑
j=0
tj(w) ·logG(gi,j (w, y ))
)
·fi(w, y ).
In this formula we view tj as a morphism tj : ∆ q
K → A1
K, and we use the fact that
g is a vector space (in the category of K-schemes).
For any set S let us write S∆ q
0 for the set of functions ∆ q
0 → S, which is the
same as the set of sequences ( s0, . . . , s q) in S. As usual Hom X (∆ q
K × Y, Z ) is the
set of X-morphisms ∆ q
K × Y → Z. In this notation the sequences ( f0, . . . , f q) and
(f′
0, . . . , f ′
q) are elements of Hom X (∆ q
K × Y, Z )∆ q
0 . We denote by
wsymG : Hom X (∆ q
K × Y, Z )∆ q
0 → HomX (∆ q
K × Y, Z )∆ q
0
the operation ( f0, . . . , f q) ↦→(f′
0, . . . , f ′
q) given by the formula (1.3).
We will also need a similar operation
wG : Hom X (Y, Z )∆ q
0 → HomX (∆ q
K × Y, Z )∆ q
0 ,
deﬁned by
wG(f0, . . . , f q) := ( f′
0, . . . , f ′
q)
with
(1.4) f′
i (w, y ) := exp G
( q∑
j=0
tj(w) ·logG(gi,j (y))
)
·fi(y).
It is clear that for q = 0 both operations w G and wsym G act as the identity,
i.e. w G(f0) = wsym G(f0) = f0 for all f0 ∈ HomX (Y, Z ). Both operations w G and
wsymG are symmetric, namely they are equivariant for the simultan eous action
of the permutation group of {0, . . . , q } on ∆ q
0 and ∆ q
K. Also if f = ( f0, . . . , f q) ∈
HomX (∆ q
K×Y, Z )∆ q
0 is a constant sequence, i.e. f0 = · · ·= fq, then wsym G(f ) = f .
Lemma 1.5. Both operations wG and wsymG are simplicial. Namely, given α ∈
∆ q
p the diagram
HomX (∆ q
K × Y, Z )∆ q
0
wsymG
− − − − − →HomX (∆ q
K × Y, Z )∆ q
0
α ∗
↓ α ∗
↓
HomX (∆ p
K × Y, Z )∆ p
0
wsymG
− − − − − →HomX (∆ p
K × Y, Z )∆ p
0
is commutative, and likewise for wG.
Proof. It suﬃces to consider α = ∂ i or α = s i. Since wsym G is symmetric, we
may assume that α = ∂ q : [ q − 1] → [q] or α = s q : [ q + 1] → [q]. Fix a sequence
f = (f0, . . . , f q) ∈ HomX (∆ q
K × Y, Z )∆ q
0 . Let gi,j ∈ HomK(∆ q
K × Y, G ) be such that
fj = gi,j ·fi, and let f′ = (f′
0, . . . , f ′
q) := wsym G(f ).
First let’s look at the case α = ∂ q. Take w ∈ ∆ q−1
K and y ∈ Y , and let
v := α∗(w) ∈ ∆ q
K. The coordinates of v are tj(v) = tj(w) for j ≤ q − 1, and
AN A VERAGING PROCESS 5
tq(v) = 0. Then for any i the i-th term in the sequence α∗(f′), evaluated at ( w, y ),
equals
(1.6)
f′
i (v, y ) = exp G
( q∑
j=0
tj(v) ·logG(gi,j (v, y ))
)
·fi(v, y )
= exp G
( q−1∑
j=0
tj(w) ·logG(gi,j (v, y ))
)
·fi(v, y ).
On the other hand, the i-th term of the sequence wsym G(α∗(f )) is
expG
( q−1∑
j=0
tj(w) ·logG(α∗(gi,j )(w, y ))
)
·α∗(fi)(w, y )
= exp G
( q−1∑
j=0
tj(w) ·logG(gi,j (v, y ))
)
·fi(v, y ).
So indeed α∗ ◦ wsymG = wsym G ◦ α∗ in this case.
Next consider the case α = s q. Take w ∈ ∆ q+1
K and y ∈ Y , and let v :=
α∗(w) ∈ ∆ q
K. The coordinates of v are tj(v) = tj(w) for j ≤ q − 1, and tq(v) =
tq(w) + tq+1(w). For any i ≤ q the i-th term in the sequence α∗(f ), evaluated at
(w, y ), is f′
i (v, y ), which was calculated in (1.6). The ( q + 1)-st term is also f′
q(v, y ).
On the other hand, for any i ≤ q the i-th term in the sequence wsym G(α∗(f′)),
evaluated at ( w, y ), is
zi := exp G
( q+1∑
j=0
tj(w) ·logG(α∗(gi,j )(w, y ))
)
·α∗(fi)(w, y ).
But tq(w) + tq+1(w) = tq(v), α∗(gi,j )(w, y ) = gi,j (v, y ) for j ≤ q, and
α∗(gi,q +1)(w, y ) = gi,q (v, y ). Therefore
zi = exp G
( q∑
j=0
tj(v) ·logG(gi,j (v, y ))
)
·fi(v, y ).
For i = q + 1 one has zq+1 = zq. We conclude that α∗ ◦ wsymG = wsym G ◦ α∗ in
this case too.
The proof for w G is the same. □
Lemma 1.7. Both operations wG and wsymG are functorial in the data
(G, X, Y, Z ). Namely, given another such quadruple (G′, X′, Y ′, Z′), a morphism
of schemes X → X′, a morphism of schemes e : Y′ → Y over X′, a morphism of
group-schemes φ : G × X → G′ × X′ over X′, and a G × X -equivariant morphism
of schemes f : Z → Z′ over X′, the diagram
HomX (∆ q
K × Y, Z )∆ q
0
wsymG
− − − − − →HomX (∆ q
K × Y, Z )∆ q
0
(e,f )
↓ (e,f )
↓
HomX ′ (∆ q
K × Y′, Z′)∆ q
0
wsymG′
− − − − − →HomX ′(∆ q
K × Y′, Z′)∆ q
0
is commutative, and likewise for wG.
Proof. This is due to the functoriality of the exponential map, see L emma 1.1. □
6 AMNON YEKUTIELI
Lemma 1.8. Assume G is abelian. Then for any (f0, . . . , f q) ∈ HomX (∆ q
K ×
Y, Z )∆ q
0 the sequence wsymG(f0, . . . , f q) is constant.
Proof. In this case exp : g → G is an isomorphism of algebraic groups, where g is
viewed as an additive group. So we may assume that Z is a torsor under g × X.
Let ( f′
0, . . . , f ′
q) := wsym G(f0, . . . , f q), and let γ i,j : ∆ q
K × Y → g be morphisms
such that fj = γ i,j + fi. Take ( w, y ) ∈ ∆ q
K × Y . Then
f′
i(w, y ) =
( q∑
j=0
tj(w) ·γ i,j (w, y )
)
+ fi(w, y )
for any i. Because γ i,j = −γ j,i = γ 0,j − γ 0,i , fi = f0 + γ 0,i and ∑ q
j=0 tj(w) = 1, it
follows that f′
i (w, y ) = f′
0(w, y ). □
Let’s write wsym d
G for the d-th iteration of the operation wsym G.
Lemma 1.9. For any f = ( f0, . . . , f q) ∈ HomX (∆ q
K × Y, Z )∆ q
0 the sequence
wsymd(G)
G (f ) is constant. For any d ≥ d(G) one has wsymd
G(f ) = wsym d(G)
G (f ).
Proof. For any k, the orbit of f0 ∈ HomX (∆ q
K × Y, Z ) under the action of the
group Gk(∆ q
K × Y ) will be denoted by Gk(∆ q
K × Y ) ·f0. Let ( f′
0, . . . , f ′
q) :=
wsymG(f0, . . . , f q). We will prove that if f1, . . . , f q ∈ Gk(∆ q
K × Y ) ·f0 then
f′
1, . . . , f ′
q ∈ Gk+1(∆ q
K × Y ) ·f′
0. The assertions of the lemma will then follow.
Let ˜Y = ˜X := ∆ q
K × Y and ˜Z := ˜X ×X Z. So ˜Z is a torsor under G × ˜X,
and f0 induces a morphism ˜f0 ∈ Hom ˜X ( ˜Y , ˜Z). The morphism τ : G × ˜X → ˜Z,
(g, ˜x) ↦→g ·˜f0(˜x), is an isomorphism of ˜X-schemes. Deﬁne ˜W := τ (Gk × ˜X) ⊂ ˜Z.
Then ˜W is the “geometric orbit” of ˜f0 under Gk × ˜X; and in particular ˜W is a torsor
under Gk × ˜X. By assumption ˜f1, . . . , ˜fq ∈ Hom ˜X ( ˜Y , ˜W ). Deﬁne ( ˜f′
0, . . . , ˜f′
q) :=
wsymGk ( ˜f0, . . . , ˜fq). By Lemma 1.7 it suﬃces to prove that ˜f′
1, . . . , ˜f′
q ∈ Gk+1( ˜Y ) ·
˜f′
0.
Deﬁne ¯W := ˜W /G k+1. This is a torsor under the group scheme ( Gk/G k+1) × ˜X.
Let ¯f0, . . . , ¯fq ∈ Hom ˜X ( ˜Y , ¯W ) be the images of ( ˜f0, . . . , ˜fq). Because the group
Gk/G k+1 is abelian, Lemma 1.8 says that wsym Gk/G k+1( ¯f0, . . . , ¯fq) is a constant
sequence. Again using Lemma 1.7, we see that in fact ˜f′
1, . . . , ˜f′
q ∈ Gk+1( ˜Y )·˜f′
0. □
Given an X-scheme Y the collections
{
HomX (∆ q
K × Y, Z )
}
q∈N and{
HomX (Y, Z )∆ q
0
}
q∈N are simplicial sets. For q = 0 there are equalities
(1.10) Hom X (∆ 0
K × Y, Z ) = Hom X (Y, Z ) = Hom X (Y, Z )∆ 0
0.
Theorem 1.11. Let G be a unipotent algebraic group over K, let X be a K-scheme,
and let Z → X be a G-torsor over X. For any X-scheme Y and natural number q
there is a function
wavG : Hom X (Y, Z )∆ q
0 → HomX (∆ q
K × Y, Z )
called the weighted average. The function wavG enjoys the following properties.
(1) Symmetric: wavG is equivariant for the action of the permutation group of
{0, . . . , q } on ∆ q
0 and on ∆ q
K.
(2) Simplicial: wavG is a map of simplicial sets
{
HomX (Y, Z )∆ q
0
}
q∈N →
{
HomX (∆ q
K × Y, Z )
}
q∈N.
AN A VERAGING PROCESS 7
(3) Functorial: given another such quadruple (G′, X′, Y ′, Z′), a morphism of
schemes X → X′, a morphism of X′-group-schemes G × X → G′ × X′, a
G × X -equivariant morphism of X′-schemes f : Z → Z′ and a morphism
of X′-schemes e : Y′ → Y , the diagram
HomX (Y, Z )∆ q
0
wavG
− − − − →HomX (∆ q
K × Y, Z )
(e,f )
↓ (e,f )
↓
HomX ′ (Y′, Z′)∆ q
0
wsymG′
− − − − − →HomX ′ (∆ q
K × Y′, Z′)
is commutative.
(4) If q = 0 then wavG is the identity map of HomX (Y, Z ).
Proof. Given a sequence f = (f0, . . . , f q) ∈ HomX (Y, Z )∆ q
0 deﬁne wav G(f ) := f′ ∈
HomX (∆ q
K × Y, Z ) to be the morphism such that
(wsymd(G)
G ◦ wG)(f0, . . . , f q) = ( f′, . . . , f ′);
see Lemma 1.9. Properties (1)-(4) follow from the correspon ding properties of w G
and wsym G. □
Proof of Corollary 0.2. Take X = Y := Spec K in Theorem 1.11, and consider the
G-torsor Z := G. Choose any base point z ∈ Z; this deﬁnes an isomorphism of left
G(K)-sets Z(K) ∼= Z. The weight sequence w can be considered as a K-rational
point of ∆ q
K, and we deﬁne
wavG, w(z) := wav G(z)(w) ∈ Z.
If we were to choose another base point z′ ∈ Z this would amount to applying
an automorphism of the torsor Z, namely right multiplication by some element of
G(K). Due to the functoriality of wav G the point wav G, w(z) will be unchanged.
The properties of this set-theoretical averaging process a re now immediate con-
sequences of the corresponding properties of the geometric average. □
Remark 1.12. Z. Reichstein observed that our averaging process provides a new
proof (in characteristic 0) of the fact that a unipotent grou p G is special, namely
any G-torsor Z over K has a K-rational point. Let us explain the idea.
Let z0 ∈ Z be some closed point. Choose a ﬁnite Galois extension L of K
containing the residue ﬁeld k(z0). Let Γ be the Galois group of L over K, which
acts on the set Z(L). Let z0, . . . , z q ∈ Z(L) be the Γ-conjugates of z0. The group
Γ acts on the sequence z := ( z0, . . . , z q) by permutations. Thus the simultaneous
action of Γ on
Z(L)∆ q
0 = Hom Spec K(Spec L, Z )∆ q
0
ﬁxes z.
We know that the operator wav G is symmetric. And functoriality says that
the action of the Galois group on Spec L is also respected. Since z is ﬁxed by
the simultaneous action of Γ, so is wav G(z). Take the uniform weight sequence
w := ( 1
q+1 , . . . , 1
q+1 ) and deﬁne z′ := wav G(z)(w) ∈ Z(L). Because w is ﬁxed by
the permutation group we conclude that z′ is Γ-invariant, and hence z′ ∈ Z(K).
Remark 1.13. Theorem 1.11 has a rather obvious parallel in diﬀerential ge ometry.
Indeed, a simply connected nilpotent Lie group is the same as the group G(R) of
rational points of a unipotent algebraic group G over R.
8 AMNON YEKUTIELI
