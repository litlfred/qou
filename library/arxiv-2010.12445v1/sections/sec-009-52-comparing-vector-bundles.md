---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-009-52-comparing-vector-bundles
section_title: "Comparing vector bundles"
section_number: 5.2
pages: 23-27
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect"
---
the vector bundles on X and on Fib X , C.
Proposition 5.14. Let X and C be as in 5.1. The following conditions are equivalent:
1) (if X is quasi-separated (see [Ton20, Def 1.4] )) the morphism OFibX ,C → P C∗OX is an
isomorphism;
2) the functor Vect(FibX , C) → Vect(X ) is fully faithful;
3) the functor G∗ : C → Vect(FibX , C) is fully faithful.
4) the functor G∗(C) → Vect(X ) is faithful
Proof. 1. ⇐ ⇒ 2. We assume X quasi-compact and quasi-separated. Since Fib X , C is quasi-
compact and quasi-separated by 5.1, the functor PC : X → FibX , C is quasi-compact and quasi-
separated as well, so that pushing forward quasi-coherent s heaves works as expected (see [ Ton20,
Prop 1.15]). In particular PC∗OX is a quasi-coherent sheaf.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 24
For H ∈ QCoh(FibX , C) consider the morphism
δH : Hom(H, OFibX ,C ) → Hom(H|X, OX )
This map can also be obtained applying Hom (H, −) on the map OFibX ,C → P C∗OX :
Hom(H, OFibX ,C ) → Hom(H, PC∗OX ) ≃ Hom(H|X, OX )
In particular Yoneda’s lemma tells us that 1. is equivalent to the fact that δH is an isomorphism
for all H ∈ QCoh(FibX , C). On the other hand, condition 2. is equivalent to the fact that all
mapsδH are isomorphisms for H ∈ Vect(FibX , C). Thus clearly 1. =⇒ 2. . The converse instead
follows from 1.6: QCoh (FibX , C) → LR(Vect(FibX , C),R ) is fully faithful because Fib X , C has the
resolution property by 5.1.
2. =⇒ 3. ⇐ ⇒ 4. It is enough to recall that C
G∗
− →Vect(FibX , C) → Vect(X ) is the inclusion.
4. =⇒ 2. We have to show that the map
Hom(H, H′) → Hom(H|X, H′
|X ′)
is an isomorphism for all H, H′ ∈ Vect(FibX , C). Since G∗(C) generates QCoh (X ) by 5.1 and H
is ﬁnitely presented, there exists an exact sequence
GE ′ → G E → H → 0
for some E, E ′ ∈ C ⊕. As Hom (−, H′) and Hom (−|X, H′
|X ) are both exact on the above sequence,
we can assume H = GE for some E ∈ C ⊕.
Considering a resolution for H′∨, dualizing and using that G∨
E ≃ G E ∨ by 5.5, we also obtain
an exact sequence
0 → H → G E → G E ′
for some E, E ′ ∈ C ⊕. Moreover also this sequence restricts to an exact sequence on X because H′
is locally free: Coker (H → G E ) is locally free. In particular Hom (GE, −) and Hom (E, −|X ) are
exact on the above sequence and therefore we can also assume H′ = GE for some E ∈ C ⊕.
Splitting E and E into direct sums of sheaves in C we are left to prove that
Hom(GE, GE ) → Hom(E, E)
is an isomorphism for E, E ∈ C . By hypothesis this map in injective. On the other hand it is
surjective because C
G∗
− →Vect(FibX , C) → Vect(X ) is the inclusion. □
Conjecture 5.15. Let X and C be as in 5.1. Then the equivalent conditions of Proposition 5.14
holds.
Remark 5.16. Conjecture 5.15 holds in two special cases. The ﬁrst one is when X is quasi-
compact with quasi-aﬃne diagonal and C generates QCoh (X ): by 3.2 the map X → FibX , C
is actually an equivalence. The second is when X is quasi-compact and quasi-separated and
C = {OX }, the simplest category: the Conjecture is veriﬁed thanks to 5.20, that we are going to
prove.
Proposition 5.17. Let X be a quasi-compact ﬁbered category over R and Y a quasi-compact
fpqc stack with quasi-aﬃne diagonal and with the resolution property. Then any map f : X → Y
has a canonical factorization X → FibX , Vect(X ) → Y .
Proof. The canonical extension Fib X , Vect(X ) → Y is the composition of Fib X , Vect(X ) → FibY, Vect(Y),
Γ ↦→Γ ◦f ∗ and the equivalence Y → FibY, Vect(Y) (see 3.2). This can also be described, again
using 3.2, as the map corresponding to the composition
Vect(Y) → Vect(X )
G∗
− →Vect(FibX , Vect(X ))
□
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 25
Conjecture 5.18. Let X be a quasi-compact ﬁbered category over R. The morphism X → FibX , C
is universal among maps from X to quasi-compact fpqc stacks with quasi-aﬃne diagonal and w ith
the resolution property, that is
(5.1) Hom (FibX , Vect(X ), Y) → Hom(X, Y)
is an equivalence for all such stacks Y.
Proposition below shows that Conjecture 5.15 for C = Vect(X ) is equivalent to Conjecture
5.18.
Proposition 5.19. Conjecture 5.18 holds if and only if
Vect(FibX , Vect(X )) → Vect(X )
is faithful. In this case the above map is an equivalence.
Proof. As the composition Vect (X )
G∗
− →Vect(FibX , Vect(X )) → Vect(X ) is the identity, we see
that if Vect (FibX , Vect(X )) → Vect(X ) is fully faithful then it is an equivalence. Moreover by 5.14
faithfulness also implies the fullness. Assume this is true . If we start by a functor Fib X , Vect(X ) →
Y, which is completely determined by the pullback
Vect(Y) → Vect(FibX , Vect(X ))
by 3.2, the new map Fib X , Vect(X ) → Y obtained corresponds to
Vect(Y) → Vect(FibX , Vect(X )) → Vect(X )
G∗
− →Vect(FibX , Vect(X ))
and therefore is canonically isomorphic to the original one .
Conversely assume X → FibX , Vect(X ) is universal. Given h ∈ N we deﬁne Yh as the stack of
vector bundles whose local rank is bounded above by h. In other words
Yh =
h⨆
l=0
B Gll
which is a quasi-compact stack with aﬃne diagonal and the res olution property. Assuming that
(5.1) is an equivalence for all Yh means that
Vect(FibX , Vect(X )) → Vect(X )
induces an equivalence on the corresponding groupoids. We h ave to show that, if E, H ∈
Vect(FibX , Vect(X )) and φ : E → H is a morphism and φ |X = 0 then φ = 0 . Consider the
isomorphism
ψ : ( E ⊕ H ) → (E ⊕ H ), e ⊕h ↦− →e ⊕ (h +φ(e))
By construction ψ |X = id. Thus ψ = id and φ = 0 as required. □
5.3. The case C = {OX }. In this section we consider the simple case C = {OX }. Notice that
Symn OX ≃ OX so the hypothesis of 5.1 are satisﬁed.
Proposition 5.20. Let X be a quasi-compact ﬁbered category over R. Then FibX , {OX } is the
intersection of all quasi-compact open subsets of Spec H0(OX ) containing the image of X →
Spec H0(OX ).
If X is quasi-compact and quasi-separated then Vect(FibX , {OX }) → Vect(X ) is fully faithful,
or, equivalently, OFibX ,{OX } → P {OX }∗OX is an isomorphism. Moreover X → FibX , {OX } is
universal among maps from X to pseudo-aﬃne sheaves.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 26
Proof. We can assume R = H0(OX ). Set C = {OX }. If A is an R-algebra, there is a unique
R-linear and strong monoidal functor Γ A : C → Vect(A), namely Γ A = H0(−) ⊗RA. This means
that Fib X , C is a subfunctor of Spec R. We have that Γ A ∈ FibX , C(A) if and only if, given a test
sequence T∗ for C, Γ A is exact on it. As
Γ A(T∗) = H0(T∗) ⊗RA
we can conclude that Fib X , C is the locus where all complex of free R-modules H 0(T∗) are exact.
By 4.1, this is an intersection of quasi-compact open subsets of Sp ecR containing the image
of X → SpecR. Conversely if X → U ⊆ SpecR and U is a quasi-compact open subset, say
U = SpecR −V (a1,...,a n), then U is the locus where (a1,...,a n) :Rn →R is surjective and,
in particular,
On
X
(a1,...,a n)
− − − − − − → OX → 0
is a test sequence. Therefore Fib X , C ⊆U as required.
Now assume that X (and therefore PC : X → FibX , C) is quasi-compact and quasi-separated.
Set π : X → SpecR. By construction π∗OX = OSpec R. From the Cartesian diagram
X X
FibX , C SpecR
id
PC π
u
the ﬂatness of u and [ Ton20, Prop 1.15] we can conclude that
OFibX ,C ≃u∗OSpec R ≃u∗(π∗OX ) ≃ P C∗OX
By 5.14 this is equivalent to the fully faithfulness of Vect (FibX , C) → Vect(X ).
For the last claim, if X → U is a map to a quasi-aﬃne scheme consider the diagram
X FibX , C V SpecR
U Spec H0(OU )
where the square one is Cartesian. The dashed arrow exists th anks to the description of Fib X , C
as intersection. From the same diagram we can see that Fib X , C → U is uniquely determined.
The general case of a pseudo-aﬃne sheaf follows easily from 4.2. □
Proposition 5.21. Let X be a quasi-compact ﬁbered category. If X → Spec H0(OX ) has open
image then FibX , {OX } coincides with this image. Conversely if FibX , {OX } is an algebraic stack,
X → SpecR is a ﬁnitely presented algebraic stack and H0(OX ) is a Noetherian Jacobson ring
then X → Spec H0(OX ) has open image.
Proof. Set C = {OX }. The ﬁrst claim follows from 5.20, so let us focus on the converse.
We can assume R = H0(OX ). By 2.8 and 5.20, the fact that Fib X , C is algebraic means that
it is quasi-aﬃne. Moreover, since H 0(OFibX ,C ) = R, it follows that V = FibX , C is open inside
SpecR. By Chevalley’s theorem [ Aut19, Tag 054K] the image U of X → SpecR is constructible.
In conclusion, from 5.20, we can conclude that V is the smallest open of Spec R containing U .
Assume by contradiction U ⁄=V . As V −U is constructible, we need to show that a constructible
subset Q of Spec R contains a closed subset. We can easily reduce to the case tha t Q is open.
As R is a Jacobson ring, Q contains a closed point of Spec R as required. □
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 27
Example 5.22. We show an example of an integral scheme X of ﬁnite type over a ﬁeld k such
that
• the stack Fib X, {OX } is not algebraic.
• the mapX → FibX, {OX } is not surjective, which shows that not all ﬁber functors (lo cally)
comes from a section of X.
By 5.21, the idea is to look for an X such that the image of X → Spec H0(OX ) is not open. Let
A =k[x,y,z ] and B =k[x/y,y,z/y ] and notice that
A ⊆B ⊆Ay ⊆Axy =Bx
We deﬁne X as the scheme obtained by gluing Spec Ax and Spec B along Spec Axy. By con-
struction there are maps
SpecA −V (x,y ) = SpecAx ∪ SpecAy →X
f
− →SpecA
As the ﬁrst map is dominant because Spec Ax ⊆ X is open, we obtain that H 0(OX ) = A.
Moreover
f −1(V (x,y )) = Spec(B/ (x,y )) = Spec(k[x/y,z/y ]) → SpecA
is given by A → k[x/y,z/y ], x,y,z → 0. It follows that the image of X → SpecA is Im =
SpecA −V (x,y ) ⊔ {(x,y,z )}.
By 5.21 the stack Fib X, {OX } cannot be algebraic because Im is not open. Moreover we claim
that P = (x,y ) ∈ FibX, {OX } − Im. By 5.20 we have to show that if Im ⊆ U ⊆ SpecA is open
then P ∈U . This is true because otherwise we would have the contradict ion
P ∈ (SpecA −U ) ⊆ SpecA − Im =V (P ) − {(x,y,z )} ⊆ V (P ) = {P }
