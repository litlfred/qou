---
doc_id: arxiv-0711.4229v2
doc_title: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS"
section_id: sec-004-5-properties-of-dj-and-f
section_title: "Properties of dJ and F'"
section_number: 5
pages: 8-11
source_pdf: 0711.4229v2.pdf
source_sha256: 2e6cc61069016627
toc_source: outline
doc_brief: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS — In this paper we give a re-normalization of the Reshetikhin-Turaev quantum invariants of links, by modiﬁed quantum dimensions."
---
The following lemma shows that the function dJ satisfying the conditions of Theorem 3 is
essentially unique.
Lemma 11. Let J ∈Ob(C) be a simple ambidextrous object such that J ∈A(J). Suppose that
d : A(J) →F is a function such that the construction of Theorem 3 with dJ replaced by d yields
a well deﬁned invariant for all L ∈LA(J). Then d = dJ for an appropriate choice of d0.
Proof. Let L be the Hopf link with components colored V and J, where V is a simple object of
C. By opening one strand of L and then the other, we get
d(V ) S′(J, V ) = d(J) S′(V, J) .
So, d = d−1
0 d(J) dJ.
□
This lemma implies in particular that if J1, J2 are two simple ambidextrous objects such that
A(J1) = A(J2), then dJ1 = dJ2 for any choice of d0 in the deﬁnition of dJ1 and an appropriate
choice of d0 in the deﬁnition of dJ2.
Lemma 12. Let V, W be simple objects in C, then S′(V, W) = S′(V ∗, W ∗).
Proof. We have
S′(V, W) =
* W
V
+
=
* W
V
+
=
*W ∗
V ∗
+
= S′(V ∗, W ∗)
where the ﬁrst and the fourth equalities follow from the deﬁnition of S′, the second from
composing with the morphism (IdV ⊗dV )(bV ⊗IdV ) and the third from the property that
F(↑V ) = F(↓V ∗).
□
Lemma 13. If an object J in C is ambidextrous, then so is J∗.
Proof. We have to prove that trL(f) = trR(f) for any endomorphism f of J∗⊗J∗. First we
deﬁne an endomorphism f ′ of J ⊗J by the following formula:
f ′ = F




❄
❄
❄
❄
f
J
J
J
J



.
As V is ambidextrous we have trL(f ′) = trR(f ′) and thus
F




❄
❄
❄
f
J
J



= F




❄
❄
❄f
J
J




In ribbon categories, modules are canonically isomorphic to their bidual and if T is a colored
ribbon graph, changing both the orientation of an internal edge and its color to its dual does
MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS
9
not aﬀect F(T ). Doing this for the internal edges of the two ribbon graphs above, we deduce
that
*
✻
✻
✻
f
J∗
J
J
+
=
*
❄
✻
✻
f
J∗
J
J
+
Which mean that trR(f) = trL(f).
□
Corollary 14. For any simple ambidextrous object J ∈Ob(C), we have A(J∗) = {V ∗: V ∈
A(J)} and dJ∗(V ∗) = dJ(V ) for all V ∈A(J). If V, V ∗∈A(J) satisfy S′(V, V ∗)̸ = 0, then
dJ(V ∗) = dJ(V ).
Proof. Lemma 12 implies that
A(J∗) = {V ∈Ob(C) : V simple and S′(J∗, V )̸ = 0} = {V ∗: V ∈A(J)}
and for all V ∈A(J),
dJ(V ) = d0
S′(V, J)
S′(J, V ) = d0
S′(V ∗, J∗)
S′(J∗, V ∗) = dJ∗(V ∗) .
Consider the Hopf link H with components labeled by V and V ∗.
Then by deﬁnition,
F ′(H) is equal to both dJ(V )S′(V ∗, V ) and dJ(V ∗)S′(V, V ∗). Now Lemma 12 implies that
S′(V ∗, V ) = S′(V, V ∗)̸ = 0 and therefore dJ(V ∗) = dJ(V ).
□
Let I be the set of isomorphism classes of simple objects of C. We call a subset B of I
complete if S′(U, V )̸ = 0 for all U, V ∈B and S′(U, W) = 0 for all U ∈B, W ∈I −B.
Lemma 15. Let B be a complete subset of the set I, which contains at least one ambidextrous
object. Then
(1) all objects in B are ambidextrous;
(2) for any object J ∈B, we have A(J) = B;
(3) Let F ′
J, F ′
J′ be the invariants derived above from arbitrary pairs (J ∈B, d0) and (J′ ∈
B, d′
0), respectively, where d0, d′
0 ∈F \ {0}. Then
F ′
J = dJ(J′)
d′
0
F ′
J′ .
Proof. The ﬁrst claim follows from the deﬁnition of a complete set and the remark following
Lemma 2. The equality A(J) = B follows from the deﬁnitions.
Lemma 11 implies that dJ′ is proportional to dJ. More precisely, dJ = (d′
0)−1 dJ(J′) dJ′.
Thus,
F ′
J(L) = dJ(V ) < TV >= (d′
0)−1 dJ(J′) dJ′(V ) < TV >= (d′
0)−1 dJ(J′)F ′
J′(L).
□
The completeness condition on B seems to be very strong. However, complete sets naturally
arise in our examples, see Subsections 6.1, 6.2 and 6.3. In such a situation Lemma 15 says that
the ambidextrous object J deﬁnes a “cluster” A(J) of ambidextrous objects with the property
that any element of this cluster leads to an invariant proportional to F ′
J. There are two kinds
of clusters depending on whether or not dimC(J) = 0. The case dimC(J) = 0 is of particular
interest because then F ′ may be non-zero while the usual invariant F restricted to LA is zero,
as will be clear from the next lemma.
From now on and up to the end of this section we ﬁx a simple ambidextrous object J in C.
10
NATHAN GEER, BERTRAND PATUREAU-MIRAND, AND VLADIMIR TURAEV
Lemma 16. For any V ∈A(J),
dimC(V ) = d−1
0
dimC(J) dJ(V ) .
Proof. Consider the Hopf link H with components labeled by J and V ∈A. Now F(H) can be
computed in two ways, namely by cutting the component labeled by J or cutting the component
labeled by V . This gives
F(H) = S′(V, J) dimC(J) = S′(J, V ) dimC(V ) .
Thus, dimC(V ) = d−1
0
dimC(J) dJ(V ).
□
The corollary below follows directly from the previous lemma.
Corollary 17. The following hold,
(1) if dimC(J) = 0 then dimC(V ) = 0 for all V ∈A(J) and F(L) = 0 for all L in LA,
(2) if dimC(J)̸ = 0 then F ′ is proportional to F.
The following two propositions show that F ′ has behavior similar to the functor F.
Proposition 18. Let U, V, W ∈Ob(C) be such that W ∼= U ⊗V . Let L be a C-colored link,
such that a component of L is colored by W. Let L∥be the link obtained from L by replacing
this component of L by two parallel copies colored by U and V . If L∥is an element of LA(J),
then F ′(L) = F ′(L∥).
Proof. Since W ∼= U ⊗V there exist morphisms f : W →U ⊗V and g : U ⊗V →W such
that f ◦g = IdU⊗V and g ◦f = IdW . Use the equality g ◦f = IdW to replace a portion of
the W-colored component of L by two strings labeled by U and V and two coupons labeled
f and g. Then by sliding one of the coupons around the component and using the equality
f ◦g = IdU⊗V one arrives at L∥. Then F ′(L) = F ′(L∥) since F ′ is a well deﬁned C-colored
ribbon graph invariant.
□
Proposition 19. Let L be an element of LA(J) with a circle component colored by W ∈Ob(C).
If W is the only color of L in A(J), then we additionally assume that W ∗∈A(J) and
S′(W, W ∗)̸ = 0.
Let L−be obtained from L by reversing the orientation of the W-colored
component and changing its color to W ∗. Then F ′(L) = F ′(L−).
Proof. We consider two cases: (a) if W is the only color of L in A(J) and (b) otherwise. In
the latter case we have F ′(L) = dJ(V ) ⟨F(TV )⟩where V ∈A(J) is the label of another circle
component (or an edge) of L and TV is obtained from L by cutting this component (edge). But
F(TV ) = F(T ′
V ) where T ′
V is obtained from TV by reversing the orientation of the W-colored
component and changing its color to W ∗. In the former case we have
F ′(L) = dJ(W) ⟨TW ⟩
= dJ(W)

T −
W ∗

= dJ(W ∗) ⟨⊥W ∗⟩
= F ′(L−)
where ⊥W ∗is the ribbon graph T −
W ∗rotated 180◦. (We use here the second claim of Corollary
14).
□
Proposition 20. If L ∈LA(J), L+ ∈LOb(C), then the disjoint union L ⊔L+ belongs to LA(J)
and F ′(L ⊔L+) = F ′(L) F(L+).
Proof. Follows from the deﬁnitions.
□
MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS
11
Remark 21. Both Propositions 18 and 19 can be extended to analogous statements for non-
closed C-colored ribbon graphs. In other words, F ′ behaves under cabling and reversing orienta-
tion in the same way as the standard ribbon functor F.
