---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-060-102-k-projective-dg-modules
section_title: "K-Projective DG Modules"
section_number: 10.2
pages: 179-181
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
and so we will be brief.
Deﬁnition 10.2.1.A DG moduleP∈C(A, M) is calledK-projective if for every
acyclic DG moduleN∈C(A, M), the DGK-module HomA,M(P,N ) is acyclic.
Deﬁnition 10.2.2.Let M∈C(A, M). A K-projective resolutionof M is a quasi-
isomorphism ρ:P→M in Cstr(A, M), whereP is a K-projective DG module.
Remark 10.1.5 on terminology applies here too.
Proposition 10.2.3. A DG moduleP ∈K(A, M) is K-projective if and only if
HomK(A,M)(P,N ) = 0 for every acyclic DG moduleN∈K(A, M).
The proof is like that of Proposition 10.1.3.
Deﬁnition 10.2.4.Let K be a full subcategory ofK(A, M). The full subcategory
of K on the K-projective DG modules in it is denoted byKprj. In other words,
Kprj = K(A, M)prj∩K.
The warning in Remark 10.1.8 applies here too.
Proposition 10.2.5. If K is a full triangulated subcategory ofK(A, M), then Kprj
is a full triangulated subcategory ofK.
The proof is like that of Proposition 10.1.9.
Example 10.2.6.Let⋆be some boundedness condition (namelyb, + or−). Since
K⋆(A, M) is a full triangulated subcategory ofK(A, M), we see thatK⋆(A, M)prj is
a full triangulated subcategory too.
Deﬁnition 10.2.7.Let K be a full triangulated subcategory ofK(A, M). We say
that K has enough K-projectivesif every DG moduleM∈K admits a K-projective
resolution inside K. I.e. there is a quasi-isomorphismρ:P→M where P∈Kprj.
Lemma 10.2.8.Lets :M→P be a quasi-isomorphism inK(A, M), and assumeP
is K-projective. Thens has a right inverse; namely there is a morphismt :P→M
in K(A, M) such thats◦t = idP. Moreover, this morphismt is unique.
179
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The proof is almost the same as that of Lemma 10.1.12.
Theorem 10.2.9.LetA be a DG ring, letM be an abelian category, and letK be a
full triangulated subcategory ofK(A, M). Write S := K∩S(A, M), and let D := KS
be the localization, with localization functorQ : K→D. Then for everyM∈K and
P∈Kprj the homomorphism
QP,M : HomK(P,M )→HomD(P,M )
is bijective.
The proof is like that of Theorem 10.1.13, only now we use the fact that the
functor Q is a right Ore localization.
The results from here to the end of the subsection are also proved like their
K-injective counterparts in Subsection 10.1.
Corollary 10.2.10. In the situation of Theorem10.2.9, the localization functor
Q : Kprj→D is fully faithful.
Corollary 10.2.11. In the situation of Theorem10.2.9, if K has enough K-pro-
jectives, then the localization functorQ : Kprj→D is an equivalence.
Corollary 10.2.12. Let⋆be any boundedness condition. IfK⋆(A, M) has enough
K-projectives, then the triangulated functor
Q : K⋆(A, M)prj→D⋆(A, M)
is an equivalence.
Corollary 10.2.13. Let K ⊆K′be full triangulated subcategories of K(A, M).
DeﬁneS := K∩S(A, M), S′:= K′∩S(A, M), D := KS and D′:= K′
S′. If K and K′
have enough K-projectives, then the canonical functorD→D′is fully faithful.
Corollary 10.2.14. Let φ: P →Q be a morphism in Cstr(A, M) between K-
projective objects. Thenφis a homotopy equivalence if and only if it is a quasi-
isomorphism.
Theorem 10.2.15.In the situation of Theorem10.2.9, assume thatK has enough
K-projectives. Let E be a triangulated category, and letF : K→E be a triangulated
functor. Then F has a left derived functor(LF,ηL) : D→E. Furthermore, for
every P∈Kprj the morphismηL
P : LF (P )→F (P ) in E is an isomorphism.
Deﬁnition 10.2.16.Let K be a full triangulated subcategory of K(A, M), and
assume K has enough K-projectives. A system of K-projective resolutionsin K is
a pair (P,ρ), whereP : Ob( K)→Ob(Kprj) is a function, andρ={ρM}M∈Ob(K)
is a collection of quasi-isomorphismsρM : P (M)→M in K. Moreover, if M ∈
Ob(Kprj), thenP (M) =M and ρM = idM.
Example 10.2.17. Let A be any DG ring. We will prove later thatK(A) has
enough K-projectives. Therefore, given a triangulated functorF : K(A)→E into
a triangulated category E, the left derived functor (LF,ηL) : D(A)→E exists.
Suppose we choose a system of K-projective resolutions(P,ρ) in K(A). Then we
get a presentation of(LF,ηR) as follows: LF (M) :=F (P (M)) and ηL
M :=F (ρM).
Proposition 10.2.18. In the situation of Theorem10.2.9, suppose K has enough
K-projectives, and let (P,ρ) be a system of K-projective resolutions. Then the
function P extends uniquely to a triangulated functorP : D→Kprj, such that
IdKprj = P◦Q|Kprj, andρ: Q◦P⇒IdD is an isomorphism of triangulated func-
tors.
Corollary 10.2.19 (Functorial K-Projective Resolutions). Let K be a full trian-
gulated subcategory ofK(A, M), and assumeK has enough K-projectives.
180
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) There is a triangulated functorP : K→K and a morphism of triangulated
functors ρ:P⇒IdK, such that for every objectM∈K the objectP (M) is
K-projective, and the morphismρM :P (M)→M is a quasi-isomorphism.
(2) If (P′,ρ′) is another such pair, then there is a unique isomorphism of tri-
angulated functorsζ:P′≃
=⇒P such thatρ′=ρ◦ζ.
