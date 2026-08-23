---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-012-c-it-will-turn-out-that-the-scheme-representingf
section_title: "It will turn out that the scheme representingF is in factAN"
section_number: C
pages: 22-25
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
C for someN.
Example 3.1.— S = P1 ⊕ P2, with pure modules P1,P 2 of slopes
λ1 <λ 2.
Any element inU has the formu =1+ u1,2 withu1,2 :P2 →P1 aK-linear
map. Furtherv := a−1uΦaΦ−1 satisﬁes v1,2 = u1,2 −a1,2 +Φ(a1,2). Here
Φ(a1,2) denotes the action of Φ on the elementa1,2 of the pure module
B := HomK(P2,P 1)= P ∗
2 ⊗P1. The mapB →F (C) yields an isomorphism
coker(Φ −1,B) →F (C).
For any C-algebra R, one obtains in the same way one isomorphism
coker(Φ −1,R ⊗C B) →F (R). In 2.6, one has deﬁned theC-vector space
Repr(B) ⊂ Bglobal ⊂ B of representatives for coker(Φ−1,B). One intro-
duces the functorFo by Fo(R)= R ⊗C Repr(B). One obtains an isomor-
phism of functorsFo(R) →F (R).
The ﬁnite dimensionalC-vector spaceRepr(B) is seen as complex alge-
– 685 –
Marius van der Put, Marc Reversat
braic variety. Its algebra of regular functionsO(Repr(B)) is the symmetric
algebra ofRepr(B)∗. Then
HomC−algebra(O(Repr(B)),R ) = Hom C−vectorspace(Repr(B)∗,R )= Repr(B)⊗R.
Thus Fo and F are represented byO(Repr(B)). In terms of schemes,F is
represented byRepr(B), seen as aﬃne space overC. We note thatRepr(B)
is in fact the C-vector space Ext1(P2,P 1), where P1,P 2 are seen as left
K[Φ,Φ−1]-modules. The universal family is made explicit in the following
examples.
(1) Pi = Kei for i =1 ,2 and Φe1 = e1, Φe2 = zte2. Then the universal
family isK[x0,...,x t−1]e1 +K[x0,...,x t−1]e2 with Φ given by Φe1 = e1
and Φe2 =zte2 +(x0 +x1z+ ··· +xt−1zt−1)e1.
(2) P1 = Res(Kne1) with Φe1 = z−t/ne1,t , n/greaterorequalslant1, g.c.d.(t,n) = 1 and
P2 =Ke2 with Φe2 =e2. The universal family is:
Kn[x0,...,x t−1]e1 +K[x0,...,x t−1]e2 with Φ given by Φe1 =z−t/ne1 and
Φe2 =e2 +(x0 +x1z1/n + ··· +xt−1z(t−1)/n)e1.
Theorem 3.2.—L etS =P1 ⊕···⊕ Pr be a direct sum of pure modules
with slopesλ1 < ··· <λr. The functorF associated toS is represented by
a free polynomial ring overC in N := ∑
i<j(λj −λi) ·dimK Pi ·dimK Pj
variables. Equivalently, F, seen as a contravariant functor fromC-schemes
to sets, is represented by the aﬃne spaceAN
C.
Proof.— We will use induction with respect tor. The caser = 2 is dealt
with in Example 3.1. Taker = 3. WriteF1,2,3 for the functor associated
to P1 ⊕P2 ⊕P3. Further F1,2, F2,3, F1,3 are the functors associated to
P1 ⊕P2,P 2 ⊕P3,P 1 ⊕P3. There is a morphism of functorsT : F1,2,3 →
F1,2 ×F 2,3. An element ofF1,2,3(R), represented by a ﬁltrationM1 ⊂M2 ⊂
M3, is mapped to the pair of equivalence classes ([M1 ⊂ M2],[M2/M1 ⊂
M3/M1]) inF1,2(R) ×F 2,3(R). Weclaim that F1,2,3 is atrivial torsorover
G := F1,2 ×F2,3 forthealgebraicgroup F1,3.Inotherwords,wewillproduce
an actionm, functorial inR,
m: F1,3(R) ×F 1,2,3(R) →F 1,2,3(R),
suchthatthemap( g,h) ↦→(m(g,h),h)from F1,3(R)×F1,2,3(R)totheﬁbre
product F1,2,3(R) ×G(R) F1,2,3(R) is a bijection. We note that this deﬁnition
becomes the usual one, after introducing the algebraic group (F1,3)G over
G, by the formula (F1,3)G(R)= F1,3(R) ×G (R).
– 686 –
Galois theory ofq-diﬀerence equations
The triviality of the torsor means that there is an isomorphism of func-
tors F1,3 ×(F1,2 ×F 2,3) →F 1,2,3 compatible withT. The last statement
and the caser = 2 imply the theorem for the caser =3 .
We represent, as before, an element ofF1,2,3(R) as an equivalence class
of actionsuΦo nS withu ∈U(R). Let∼ denote the equivalence relation on
U(R), given byu1 ∼u2 if there exists ana ∈U(R) witha−1u1ΦaΦ−1 =u2.
ThenU(R)/ ∼ identiﬁes withF1,2,3(R). LetU ′(R) denote the subgroup of
U(R) consisting of the elementsu such thatu −1i s0o n R ⊗C (P1 ⊕P2)
andR ⊗CP3 is mapped toR ⊗CP1.O nU ′(R) we introduce the equivalence
relation ∼ byu1 ∼u2 is there exists ana ∈U ′(R) witha−1u1ΦaΦ−1 =u2.
NowU ′(R)/ ∼ identiﬁes in an obvious way withF1,3(R).
A small calculation, based on the observation thatU ′(R) lies in the cen-
ter ofU(R), shows that the mapU ′(R) ×U(R) →U(R), given by (u′,u) ↦→
u′u, has the property thatu′
1 ∼u′
2 and u1 ∼u2 imply u′
1u1 ∼u′
2u2.T h u s
there is an induced actionm:(U ′(R)/ ∼) ×(U(R)/ ∼) →(U(R)/ ∼). One
can verify thatm deﬁnes a group action, thatm has the torsor property
over G(R), and that the construction is functorially inR. Finally, we want
toshowthatthetorsoristrivial.Thusweneedtodeﬁneafunctorialisomor-
phism F
1,3(R) ×G (R) →F 1,2,3(R). This is done as follows. One considers
the map
Fo
1,3(R) ×Fo
1,2(R) ×Fo
2,3(R) →F +
1,2,3(R) (see Example 3.1),
given by (u1,3,u 1,2,u 2,3) ↦→


1 u1,2 u1,3
01 u2,3
00 1

 ·Φ. One easly veriﬁes that
the resulting map
Fo
1,3(R) ×Fo
1,2(R) ×Fo
2,3(R) →F 1,2,3(R),
isbijectiveanddependsfunctoriallyon R.Sincethemaps Fo
i,j(R) →Fi,j(R)
areisomorphismsfunctorialin R,wehavefoundatrivializationofthetorsor.
This ends the proof for the caser =3 .
Forr = 4 andS =P1 ⊕···⊕ P4, one deﬁnes in a similar way functors
F1,2,3,4, F2,3,4 etc. With the same methods one proves that the morphism
of functorsF1,2,3,4 →G , whereG := F1,2,3 ×F2,3 F2,3,4, is a trivial torsor for
the algebraic groupF1,4. It is clear how to extend this to anyr> 4. □
Remarks 3.3.— (1) LetS = P1 ⊕···⊕ Pr with corresponding functor
F. The method of the proof of Theorem 3.2 yields maps∏
i<j Fo
i,j(R) →
F+(R), functorial inR. LetFo(R) denote the image of the this map. Then
– 687 –
Marius van der Put, Marc Reversat
Fo is a functor and the obvious morphismFo →F is an isomorphism. In
particular one ﬁnds an isomorphism of functors∏
i<j Fi,j →F which is
obtained by trivializing the sequence of torsors involved inF.
(2) The case of Theorem 3.2 where the slopes are integers is present in
a paper of G. Birkhoﬀ and P.E. Guenther, see [Bir], where they present
normal forms for these equations. This case is also treated in [R-S-Z, Sau2,
Sau3].
(3) Each F
i,j has the natural structure of algebraic group over C and
is in fact equal toExt1(Pi,Pj). However, F has no evident structure of
(unipotent) algebraic group. In contrast with this, the obvious injective
map ∏
i<j Fo
i,j(R) →U(R) has as image asubgroupofU(R).
In proving this, one has to consider indicesa<b<c and one has to
show that the the obvious mapFo
a,b(R) ×Fo
b,c(R)t oR ⊗Hom(Pc,Pa) has
image in Fo
a,c(R). This follows from the statement:Repr(M1) ⊗Repr(M2)
is mapped toRepr(M1 ⊗M2) ⊂M1 ⊗M2, proved in 2.6.
The functorial isomorphism∏
i<j Fo
i,j →F provides the latter with a
structure of unipotent linear algebraic group.
