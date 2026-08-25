---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-030-24-the-andre-kahn-quotient-33
section_title: "The Andr´e-Kahn quotient 33"
section_number: 2.4
pages: 41-43
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
For any ideal one has the notion of the corresponding quotient category. By
deﬁnition, the quotient
D = D/ND
has the same objects asD, but the morphisms inD between two objectsK,L
are deﬁned by
HomD(K,L) = HomD(K,L)/ND(K,L).
We have a natural quotient functorq : D−→D that is given by the identity
on objects and by the quotient map on morphisms, and in what follows we
denote byP the essential image ofP under this quotient functor. Recall that
ultimately we want to construct a semisimple abelian category; as a ﬁrst
step towards this goal we have
LEMMA 2.6. The quotient functor q: D−→D preserves direct sums,
and the categoryP is pseudo-abelian in the sense that every idempotent
morphism in it splits as the projection onto a direct summand.
Proof. The functorq preserves direct sums since it isΛ-linear. To see
that idempotents inP split, letP be an object ofP. Since P is an abelian
category and hence in particular pseudo-abelian, it sufﬁces to show that
every idempotent in
EndP(P) = EndP(P)/ND(P,P)
lifts to an idempotent inEndP(P). Since P is semisimple by axiom (D4),
passing to isotypic components we can assumeP = Q⊕r for some simple
objectQ of P andr∈ N. ThenEndP(P) is the ring ofr×r matrices over the
skew ﬁeldEndP(Q). Since matrix rings over skew ﬁelds do not have proper
two-sided ideals, it follows that eitherND(P,P) =0 orND(P,P) =EndP(P),
and in both cases the lifting of idempotents is obvious. □
It turns out that this is already enough to conclude that the quotient
categoryD has the desired properties:
PROPOSITION 2.7. The quotient categoryD is a semisimple abelian
Λ-linear rigid symmetric monoidal category.
Proof. By [1, lemma 7.1.1] the Andr´e-Kahn radicalND is a monoidal
ideal in the sense thatidM∗ND(K,L)⊆ND(M∗K,M∗L) for allK,L,M∈D,
hence by sorite 6.1.4 of loc. cit. the quotientD = D/ND inherits fromD
the structure of aΛ-linear rigid symmetric monoidal category whose unit
element satisﬁesEndD(1) = Λ.
The main part of the proof is to check that the categoryD is semisimple
abelian. For this we ﬁrst claim that
(⋆) HomD(P[m],Q[n]) = 0 for all objects P,Q in P andm⁄= n.
34 Chapter 2 – Proof of the vanishing theorem(s)
Indeed, for m > n we even have HomD(P[m],Q[n]) = 0 since under the
faithful functorrat thisHom-group injects into
HomDbc (X,Λ)(rat(P)[m],rat(Q)[n]) = Extn−m
Perv(X,Λ)(rat(P),rat(Q))
which vanishes form >n (for the above identiﬁcation as anExt-group recall
that Dbc (X,Λ) is the derived category of Perv(X,Λ)). On the other hand, in
the casem < n we haveHomD(Q[n],P[m]) = 0, and then the deﬁnition of
the Andr´e-Kahn radical implies that
HomD(P[m],Q[n]) = ND(P[m],Q[n])
which is mapped to zero under the quotient functorq : D−→D. In both
cases the claim (⋆) follows.
Now by the perverse decomposition axiom (D3) every objectK of D
can be written asK =⨁
n∈ZKn[n] with certainKn in P. For such K the
vanishing in (⋆) implies
(⋆⋆) EndD(K) =
⨁
n∈Z
EndD(Kn[n]) =
⨁
n∈Z
EndP(Kn).
In particular, every idempotent endomorphism ofK in the categoryD is a
direct sum of idempotent endomorphisms of the summandsKn[n], and by
lemma 2.6 it follows thatD is pseudo-abelian. Hence to show thatD is a
semisimple abelian category, it will sufﬁce by [1, A.2.10] to show that it is
a semisimpleΛ-linear category in the sense of section 2.1.1 in loc. cit. For
this we use the following general result [2, th. 1].
Let F be a ﬁeld andA an F-linear rigid symmetric monoidal category
with EndA(1) = F. Suppose there exists anF-linear tensor functor ACU
from A to an abelianF-linear rigid symmetric monoidal categoryV such
that dimΛ(HomV(V1,V2)) < ∞ for allV1,V2∈ V. Then the quotient ofA by
its Andr´e-Kahn radicalNA is a semisimpleF-linear category, andNA is the
unique monoidal ideal ofA with this property.
In our case this applies forF = Λ, A = D and for the functorH•(X,−)
fromD to the abelian categoryV of super vector spaces overΛ. □
COROLLARY 2.8. The functorsP→ P and P ↪→ D are exact functors
between semisimple abelian categories. The image of a simple object P∈ P
inside P is either simple or isomorphic to zero, and ifΛ is algebraically
closed, then the latter case occurs if and only ifχ(P) =0.
Proof. By proposition 2.7,D is a semisimple abelian category, and it
also follows from the proof of the proposition thatP is a semisimple abelian
subcategory ofD. Since the considered functors are additive, they are exact
by semisimplicity. IfP is a simple object ofP, thenEndP(P) is a skew ﬁeld,
