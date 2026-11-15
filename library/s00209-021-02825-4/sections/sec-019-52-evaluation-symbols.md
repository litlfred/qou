---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-019-52-evaluation-symbols
section_title: "Evaluation symbols"
section_number: 5.2
pages: 19-20
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
One way to interpret the stability properties of a given polynomial is via the stability-
preservation properties of a particular type of linear operator: the evaluation map. That is,
the map which evaluates a polynomial p(x, y) at (a, b)̸ = (0, 0) preserves strong {(a : b)}-
stability, where {(a : b)} is a subset of CP1 consisting of a single point. Further, given λ ∈Nm
0
and (a, b) = (a1, b1, . . . , am, bm) ∈C2m (with (a j, b j)̸ = 0 for all j), we can deﬁne the
corresponding evaluation map as an element of Hom(V (λ), V (0)) since V (0) ∼= C. This
allows us to obtain symbols for evaluation maps, and these play an important role in our
linear operator characterization.
Deﬁnition 5.9 Fix λ ∈Nm
0 and (a, b) = (a1, b1, . . . , am, bm) ∈C2m such that (a j, b j)̸ =
(0, 0) for all j ∈[m]. Let ev(a,b) : V (λ) →V (0) ∼= C be the evaluation operator which
1378
J. Leake
maps p to p(a, b) = p(a1, b1, . . . , am, bm). We call Symb(ev(a,b)) ∈V (λ) the evaluation
symbol with root (a, b). Further:
Symb(ev(a,b)) =
m

j=1
(b j x j −a j y j)λ j =: (bx −ay)λ
The main signiﬁcance of this notion comes from the following result, which is essentially
just a restatement of the symbol lemma (Lemma 3.7) for evaluation symbols.
Lemma 5.10 (Evaluation Symbol Lemma) Fix λ ∈Nm
0 , p
∈
V (λ), and (a, b) =
(a1, b1, . . . , am, bm) ∈C2m such that (a j, b j)̸ = (0, 0) for all j ∈[m]. Considering
(bx −ay)λ, the evaluation symbol with root (a, b), we have:
Dλ((bx −ay)λ ⊗p) = (λ!)2 p(a, b) ⊗1 = (λ!)2 p(a, b)
In what follows, we will extend Grace’s theorem in a number of ways, mainly relying on
the previous lemma and the symbol lemma itself. As we will see, the representation theoretic
mentality combined with repeated use of the symbol lemma will yield many of the results of
this paper with surprising simplicity.
We now obtain an interesting corollary of Grace’s theorem, making use of the notion of a
disjoint Grace pair. This particular formulation of the theorem will serve as a model for our
linear operator characterization in Sect. 6.2.
Corollary 5.11 Fix λ ∈Nm
0 , q ∈V (λ), and any disjoint Grace pair (C1 × · · · × Cm, B1 ×
· · · × Bm). Then the following are equivalent.
(i) Dλ(p ⊗q)̸ = 0 for all (C1 × · · · × Cm)-stable p ∈V (λ).
(ii) Dλ(p ⊗q)̸ = 0 for all (C1 × · · · × Cm)-stable evaluation symbols p ∈V (λ).
(iii) q is (B1 × · · · × Bm)-stable.
Proof (i) ⇒(ii) Immediate.
(ii) ⇒(iii) Fix any (a, b) = (a1, b1, . . . , am, bm) ∈C2m such that (ak : bk) ∈Bk for all
k ∈[m]. Since Bk and Ck are disjoint, we have that (ak : bk) /∈Ck for all k, and therefore
Symb(ev(a,b)) = (bx −ay)λ is an evaluation symbol which is (C1 × · · · × Cm)-stable. The
evaluation symbol lemma given above then implies:
0̸ = Dλ(Symb(ev(a:b)) ⊗q) = (λ!)2q(a, b) ⊗1 = (λ!)2q(a, b)
That is, q(a, b)̸ = 0 for any (a, b) ∈C2m such that (a : b) ∈B1 ×· · ·× Bm, and this implies
q is (B1 × · · · × Bm)-stable.
(iii) ⇒(i) This follows immediately from the deﬁnition of Grace pair (Deﬁnition 5.2). ⊓⊔
