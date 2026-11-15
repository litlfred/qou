---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-008-3-moduli-spaces-for-q-diﬀerence-equations
section_title: "Moduli spaces for q-diﬀerence equations"
section_number: 3
pages: 21-25
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
For a diﬀerence module M over K we consider again the slope ﬁltra-
tion 0 = M0 ⊂M1 ⊂· · · ⊂Mr. One associates to M the graded module
gr(M) := ⊕r
i=1Mi/Mi−1. The aim is to produce a moduli space for the col-
lection of all q-diﬀerence modules over K with a ﬁxed gr(M). This problem
is the theme of [R-S-Z]. As Ch. Zhang has remarked, the problem is already
present in a paper of G. Birkhoﬀand P.E. Guenther, see [Bir]. Here we treat
the general case (i.e., arbitrary, rational slopes).
Fix a split diﬀerence module S = P1 ⊕P2 ⊕· · · ⊕Pr (with r ⩾2)
over K such that each Pi is pure of slope λi and λ1 < λ2 < · · · < λr.
One considers the pairs (M, f) consisting of a diﬀerence module over K
and an isomorphism f : gr(M) →S. Two pairs (M(i), f(i)), i = 1, 2 are
called equivalent if there exists an isomorphism f : M(1) →M(2) such
– 684 –
Galois theory of q-diﬀerence equations
that gr(M(1))
gr(f)
→gr(M(2))
f(2)
→S coincides with f(1). One wants to give
the collection of equivalence classes a structure of algebraic variety over C.
A naive, but useful way is to produce in every equivalence class a unique
representative (M, f). Our aim is to deﬁne a moduli functor F and to ﬁnd
a ﬁne moduli space for F.
It is useful to give another formulation for the pairs (M, f). Let U be
the group of the K-linear maps u : S →S such that u respects the ﬁltration
P1 ⊂P1 ⊕P2 ⊂· · · ⊂S of S and moreover gr(u) = id. Let Φ = ΦS denote
the given action on S. For any u ∈U one deﬁnes the q-diﬀerence module M
by M := S provided with a new Φ-action, namely uΦ. Let F+(C) denote
the set of all actions {uΦ}. Two actions u1Φ and u2Φ are equivalent if
there exists an a ∈U such that u1Φa = au2Φ. Let F(C) denote the set of
equivalence classes. We note that this coincides with the set of equivalence
classes for the pairs {(M, f)}.
For any C-algebra R (i.e., commutative and with a unit element) one de-
ﬁnes U(R) as the set of the R⊗C K-linear maps u from R⊗C S to itself such
u respects the ﬁltration R ⊗C P1 ⊂R ⊗C (P1 ⊕P2) · · · ⊂R ⊗C S and more-
over gr(u) = id. Further F+(R) denotes the set of all actions {uΦ} with
u ∈U(R) on R ⊗C S. As before, two actions u1Φ and u2Φ are equivalent
if there exists an a ∈U(R) such that a−1u1ΦaΦ−1 = u2. The set of equiv-
alence classes is denoted by F(R). Thus we obtain a covariant functor F
deﬁned on the category of the C-algebras. One can view F as a contravariant
functor on aﬃne schemes over C and extend F to a contravariant functor
from C-schemes to the category of sets. Our aim is to show that F is repre-
sentable by a certain C-algebra, or in other terms by an aﬃne scheme over
C. It will turn out that the scheme representing F is in fact AN
C for some N.
Example 3.1. — S = P1 ⊕P2, with pure modules P1, P2 of slopes
λ1 < λ2.
Any element in U has the form u = 1 + u1,2 with u1,2 : P2 →P1 a K-linear
map. Further v := a−1uΦaΦ−1 satisﬁes v1,2 = u1,2 −a1,2 + Φ(a1,2). Here
Φ(a1,2) denotes the action of Φ on the element a1,2 of the pure module
B := HomK(P2, P1) = P ∗
2 ⊗P1. The map B →F(C) yields an isomorphism
coker(Φ −1, B) →F(C).
For any C-algebra R, one obtains in the same way one isomorphism
coker(Φ −1, R ⊗C B) →F(R). In 2.6, one has deﬁned the C-vector space
Repr(B) ⊂Bglobal ⊂B of representatives for coker(Φ −1, B). One intro-
duces the functor Fo by Fo(R) = R ⊗C Repr(B). One obtains an isomor-
phism of functors Fo(R) →F(R).
The ﬁnite dimensional C-vector space Repr(B) is seen as complex alge-
– 685 –
Marius van der Put, Marc Reversat
braic variety. Its algebra of regular functions O(Repr(B)) is the symmetric
algebra of Repr(B)∗. Then
HomC−algebra(O(Repr(B)), R) = HomC−vectorspace(Repr(B)∗, R) = Repr(B)⊗R .
Thus Fo and F are represented by O(Repr(B)). In terms of schemes, F is
represented by Repr(B), seen as aﬃne space over C. We note that Repr(B)
is in fact the C-vector space Ext1(P2, P1), where P1, P2 are seen as left
K[Φ, Φ−1]-modules. The universal family is made explicit in the following
examples.
(1) Pi = Kei for i = 1, 2 and Φe1 = e1, Φe2 = zte2. Then the universal
family is K[x0, . . . , xt−1]e1 + K[x0, . . . , xt−1]e2 with Φ given by Φe1 = e1
and Φe2 = zte2 + (x0 + x1z + · · · + xt−1zt−1)e1.
(2) P1 = Res(Kne1) with Φe1 = z−t/ne1, t, n ⩾1, g.c.d.(t, n) = 1 and
P2 = Ke2 with Φe2 = e2. The universal family is:
Kn[x0, . . . , xt−1]e1 + K[x0, . . . , xt−1]e2 with Φ given by Φe1 = z−t/ne1 and
Φe2 = e2 + (x0 + x1z1/n + · · · + xt−1z(t−1)/n)e1.
Theorem 3.2. — Let S = P1 ⊕· · ·⊕Pr be a direct sum of pure modules
with slopes λ1 < · · · < λr. The functor F associated to S is represented by
a free polynomial ring over C in N := 
i<j(λj −λi) · dimK Pi · dimK Pj
variables. Equivalently, F, seen as a contravariant functor from C-schemes
to sets, is represented by the aﬃne space AN
C .
Proof. — We will use induction with respect to r. The case r = 2 is dealt
with in Example 3.1. Take r = 3. Write F1,2,3 for the functor associated
to P1 ⊕P2 ⊕P3. Further F1,2, F2,3, F1,3 are the functors associated to
P1 ⊕P2, P2 ⊕P3, P1 ⊕P3. There is a morphism of functors T : F1,2,3 →
F1,2 ×F2,3. An element of F1,2,3(R), represented by a ﬁltration M1 ⊂M2 ⊂
M3, is mapped to the pair of equivalence classes ([M1 ⊂M2], [M2/M1 ⊂
M3/M1]) in F1,2(R) × F2,3(R). We claim that F1,2,3 is a trivial torsor over
G := F1,2×F2,3 for the algebraic group F1,3. In other words, we will produce
an action m, functorial in R,
m : F1,3(R) × F1,2,3(R) →F1,2,3(R) ,
such that the map (g, h) →(m(g, h), h) from F1,3(R)×F1,2,3(R) to the ﬁbre
product F1,2,3(R)×G(R) F1,2,3(R) is a bijection. We note that this deﬁnition
becomes the usual one, after introducing the algebraic group (F1,3)G over
G, by the formula (F1,3)G(R) = F1,3(R) × G(R) .
– 686 –
Galois theory of q-diﬀerence equations
The triviality of the torsor means that there is an isomorphism of func-
tors F1,3 × (F1,2 × F2,3) →F1,2,3 compatible with T. The last statement
and the case r = 2 imply the theorem for the case r = 3.
We represent, as before, an element of F1,2,3(R) as an equivalence class
of actions uΦ on S with u ∈U(R). Let ∼denote the equivalence relation on
U(R), given by u1 ∼u2 if there exists an a ∈U(R) with a−1u1ΦaΦ−1 = u2.
Then U(R)/ ∼identiﬁes with F1,2,3(R). Let U ′(R) denote the subgroup of
U(R) consisting of the elements u such that u −1 is 0 on R ⊗C (P1 ⊕P2)
and R⊗C P3 is mapped to R⊗C P1. On U ′(R) we introduce the equivalence
relation ∼by u1 ∼u2 is there exists an a ∈U ′(R) with a−1u1ΦaΦ−1 = u2.
Now U ′(R)/ ∼identiﬁes in an obvious way with F1,3(R).
A small calculation, based on the observation that U ′(R) lies in the cen-
ter of U(R), shows that the map U ′(R)×U(R) →U(R), given by (u′, u) →
u′u, has the property that u′
1 ∼u′
2 and u1 ∼u2 imply u′
1u1 ∼u′
2u2. Thus
there is an induced action m : (U ′(R)/ ∼) × (U(R)/ ∼) →(U(R)/ ∼). One
can verify that m deﬁnes a group action, that m has the torsor property
over G(R), and that the construction is functorially in R. Finally, we want
to show that the torsor is trivial. Thus we need to deﬁne a functorial isomor-
phism F1,3(R) × G(R) →F1,2,3(R). This is done as follows. One considers
the map
Fo
1,3(R) × Fo
1,2(R) × Fo
2,3(R) →F+
1,2,3(R) (see Example 3.1) ,
given by (u1,3, u1,2, u2,3) →


1
u1,2
u1,3
0
1
u2,3
0
0
1

· Φ. One easly veriﬁes that
the resulting map
Fo
1,3(R) × Fo
1,2(R) × Fo
2,3(R) →F1,2,3(R),
is bijective and depends functorially on R. Since the maps Fo
i,j(R) →Fi,j(R)
are isomorphisms functorial in R, we have found a trivialization of the torsor.
This ends the proof for the case r = 3.
For r = 4 and S = P1 ⊕· · · ⊕P4, one deﬁnes in a similar way functors
F1,2,3,4, F2,3,4 etc. With the same methods one proves that the morphism
of functors F1,2,3,4 →G, where G := F1,2,3 ×F2,3 F2,3,4, is a trivial torsor for
the algebraic group F1,4. It is clear how to extend this to any r > 4.
□
Remarks 3.3. — (1) Let S = P1 ⊕· · · ⊕Pr with corresponding functor
F. The method of the proof of Theorem 3.2 yields maps 

i<j Fo
i,j(R) →
F+(R), functorial in R. Let Fo(R) denote the image of the this map. Then
– 687 –
Marius van der Put, Marc Reversat
Fo is a functor and the obvious morphism Fo →F is an isomorphism. In
particular one ﬁnds an isomorphism of functors 

i<j Fi,j →F which is
obtained by trivializing the sequence of torsors involved in F.
(2) The case of Theorem 3.2 where the slopes are integers is present in
a paper of G. Birkhoﬀand P.E. Guenther, see [Bir], where they present
normal forms for these equations. This case is also treated in [R-S-Z, Sau2,
Sau3].
(3) Each Fi,j has the natural structure of algebraic group over C and
is in fact equal to Ext1(Pi, Pj). However, F has no evident structure of
(unipotent) algebraic group. In contrast with this, the obvious injective
map 

i<j Fo
i,j(R) →U(R) has as image a subgroup of U(R).
In proving this, one has to consider indices a < b < c and one has to
show that the the obvious map Fo
a,b(R) × Fo
b,c(R) to R ⊗Hom(Pc, Pa) has
image in Fo
a,c(R). This follows from the statement: Repr(M1) ⊗Repr(M2)
is mapped to Repr(M1 ⊗M2) ⊂M1 ⊗M2, proved in 2.6.
The functorial isomorphism 

i<j Fo
i,j →F provides the latter with a
structure of unipotent linear algebraic group.
