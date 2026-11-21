---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-011-52-comparing-vector-bundles
section_title: "Comparing vector bundles"
section_number: 5.2
pages: 23-25
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
the vector bundles on X and on FibX ,C.
Proposition 5.14. Let X and C be as in 5.1. The following conditions are equivalent:
1) (if X is quasi-separated (see [Ton20, Def 1.4])) the morphism OFibX,C →PC∗OX is an
isomorphism;
2) the functor Vect(FibX ,C) →Vect(X) is fully faithful;
3) the functor G∗: C →Vect(FibX ,C) is fully faithful.
4) the functor G∗(C) →Vect(X) is faithful
Proof. 1.
⇐⇒
2. We assume X quasi-compact and quasi-separated. Since FibX ,C is quasi-
compact and quasi-separated by 5.1, the functor PC : X →FibX ,C is quasi-compact and quasi-
separated as well, so that pushing forward quasi-coherent sheaves works as expected (see [Ton20,
Prop 1.15]). In particular PC∗OX is a quasi-coherent sheaf.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
24
For H ∈QCoh(FibX ,C) consider the morphism
δH : Hom(H, OFibX,C) →Hom(H|X , OX )
This map can also be obtained applying Hom(H, −) on the map OFibX,C →PC∗OX :
Hom(H, OFibX,C) →Hom(H, PC∗OX ) ≃Hom(H|X , OX )
In particular Yoneda’s lemma tells us that 1. is equivalent to the fact that δH is an isomorphism
for all H ∈QCoh(FibX ,C). On the other hand, condition 2. is equivalent to the fact that all
maps δH are isomorphisms for H ∈Vect(FibX ,C). Thus clearly 1. =⇒2.. The converse instead
follows from 1.6: QCoh(FibX ,C) →LR(Vect(FibX ,C), R) is fully faithful because FibX ,C has the
resolution property by 5.1.
2. =⇒3. ⇐⇒4. It is enough to recall that C
G∗
−→Vect(FibX ,C) →Vect(X) is the inclusion.
4. =⇒2. We have to show that the map
Hom(H, H′) →Hom(H|X , H′
|X ′)
is an isomorphism for all H, H′ ∈Vect(FibX ,C). Since G∗(C) generates QCoh(X) by 5.1 and H
is ﬁnitely presented, there exists an exact sequence
GE′ →GE →H →0
for some E, E′ ∈C⊕. As Hom(−, H′) and Hom(−|X , H′
|X ) are both exact on the above sequence,
we can assume H = GE for some E ∈C⊕.
Considering a resolution for H′∨, dualizing and using that G∨
E ≃GE∨by 5.5, we also obtain
an exact sequence
0 →H →GE →GE′
for some E, E′ ∈C⊕. Moreover also this sequence restricts to an exact sequence on X because H′
is locally free: Coker(H →GE) is locally free. In particular Hom(GE, −) and Hom(E, −|X) are
exact on the above sequence and therefore we can also assume H′ = GE for some E ∈C⊕.
Splitting E and E into direct sums of sheaves in C we are left to prove that
Hom(GE, GE) →Hom(E, E)
is an isomorphism for E, E ∈C. By hypothesis this map in injective. On the other hand it is
surjective because C
G∗
−→Vect(FibX ,C) →Vect(X) is the inclusion.
□
Conjecture 5.15. Let X and C be as in 5.1. Then the equivalent conditions of Proposition 5.14
holds.
Remark 5.16. Conjecture 5.15 holds in two special cases. The ﬁrst one is when X is quasi-
compact with quasi-aﬃne diagonal and C generates QCoh(X): by 3.2 the map X →FibX ,C
is actually an equivalence. The second is when X is quasi-compact and quasi-separated and
C = {OX }, the simplest category: the Conjecture is veriﬁed thanks to 5.20, that we are going to
prove.
Proposition 5.17. Let X be a quasi-compact ﬁbered category over R and Y a quasi-compact
fpqc stack with quasi-aﬃne diagonal and with the resolution property. Then any map f : X →Y
has a canonical factorization X →FibX ,Vect(X ) →Y.
Proof. The canonical extension FibX ,Vect(X ) →Y is the composition of FibX ,Vect(X ) →FibY,Vect(Y),
Γ 7→Γ ◦f ∗and the equivalence Y →FibY,Vect(Y) (see 3.2). This can also be described, again
using 3.2, as the map corresponding to the composition
Vect(Y) →Vect(X)
G∗
−→Vect(FibX ,Vect(X ))
□
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
25
Conjecture 5.18. Let X be a quasi-compact ﬁbered category over R. The morphism X →FibX ,C
is universal among maps from X to quasi-compact fpqc stacks with quasi-aﬃne diagonal and with
the resolution property, that is
(5.1)
Hom(FibX ,Vect(X ), Y) →Hom(X, Y)
is an equivalence for all such stacks Y.
Proposition below shows that Conjecture 5.15 for C = Vect(X) is equivalent to Conjecture
5.18.
Proposition 5.19. Conjecture 5.18 holds if and only if
Vect(FibX ,Vect(X )) →Vect(X)
is faithful. In this case the above map is an equivalence.
Proof. As the composition Vect(X)
G∗
−→Vect(FibX ,Vect(X )) →Vect(X) is the identity, we see
that if Vect(FibX ,Vect(X )) →Vect(X) is fully faithful then it is an equivalence. Moreover by 5.14
faithfulness also implies the fullness. Assume this is true. If we start by a functor FibX ,Vect(X ) →
Y, which is completely determined by the pullback
Vect(Y) →Vect(FibX ,Vect(X ))
by 3.2, the new map FibX ,Vect(X ) →Y obtained corresponds to
Vect(Y) →Vect(FibX ,Vect(X )) →Vect(X)
G∗
−→Vect(FibX ,Vect(X ))
and therefore is canonically isomorphic to the original one.
Conversely assume X →FibX ,Vect(X ) is universal. Given h ∈N we deﬁne Yh as the stack of
vector bundles whose local rank is bounded above by h. In other words
Yh =
hG
l=0
B Gll
which is a quasi-compact stack with aﬃne diagonal and the resolution property. Assuming that
(5.1) is an equivalence for all Yh means that
Vect(FibX ,Vect(X )) →Vect(X)
induces an equivalence on the corresponding groupoids.
We have to show that, if E, H ∈
Vect(FibX ,Vect(X )) and φ: E →H is a morphism and φ|X = 0 then φ = 0.
Consider the
isomorphism
ψ: (E ⊕H) →(E ⊕H), e ⊕h 7−→e ⊕(h + φ(e))
By construction ψ|X = id. Thus ψ = id and φ = 0 as required.
□
