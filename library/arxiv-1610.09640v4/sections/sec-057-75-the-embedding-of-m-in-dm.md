---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-057-75-the-embedding-of-m-in-dm
section_title: "The Embedding of M in D(M)"
section_number: 7.5
pages: 139-140
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
category M.
For M, N ∈M there is no diﬀerence between the K-modules HomM(M, N),
HomC(M)(M, N) and HomK(M)(M, N).
Thus the canonical functors M →C(M)
and M →K(M) are fully faithful. The same is true for D(M), but this requires a
proof.
Let D(M)0 be the full subcategory of D(M) consisting of complexes whose coho-
mology is concentrated in degree 0. This is an additive subcategory of D(M).
Proposition 7.5.1. The canonical functor M →D(M)0 is an equivalence.
Proof. Let’s denote the canonical functor M →D(M)0 by F.
Under the fully
faithful embedding M ⊆Cstr(M), F is just the restriction of the functor ˜Q from
Deﬁnition 7.2.8.
The functor H0 : D(M) →M satisﬁes H0 ◦F = IdM. This implies that F is
faithful.
Next we prove that F is full. Take any objects M, N ∈M and a morphism
q : M →N in D(M). By Proposition 7.2.10 we know that q = ˜Q(a) ◦˜Q(s)−1 for
some morphisms a : L →N and s : L →M in Cstr(M), with s a quasi-isomorphism.
Let L′ := smt≤0(L), the smart truncation of L. Since L ∈D(M)0, the inclusion
u : L′ →L is a quasi-isomorphism in Cstr(M). Writing a′ := a ◦u and s′ := s ◦u,
we see that s′ is a quasi-isomorphism, and q = ˜Q(a′) ◦˜Q(s′)−1.
Next let L′′ := smt≥0(L′), the other smart truncation. The projection v : L′ →
L′′ is a surjective quasi-isomorphism in Cstr(M). Because L′′ is a complex concen-
trated in degree 0, we can view it as an object of M. The morphisms a′ and s′
139
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
factor as a′ = a′′ ◦v and s′ = s′′ ◦v, where a′′ : L′′ →N and s′′ : L′′ →M are
morphisms in M. But s′′ is a quasi-isomorphism in Cstr(M), and so it is actually an
isomorphism in M. Therefore we have a morphism a′′ ◦(s′′)−1 : M →N in M, and
˜Q(a′′ ◦(s′′)−1) = ˜Q(a′′) ◦˜Q(s′′)−1 = ˜Q(a′) ◦˜Q(s′)−1 = q.
Finally we have to prove that every L ∈D(M)0 is isomorphic, in D(M), to
a complex L′′ that’s concentrated in degree 0. But we already showed it in the
previous paragraphs.
□
Proposition 7.5.2. Let M be an abelian category and let 0 →L
φ−→M
ψ−→N →0
be a diagram in M. The following conditions are equivalent:
(i) The diagram is an exact sequence.
(ii) There is a distinguished triangle L
˜Q(φ)
−−−→M
˜Q(ψ)
−−−−→N
θ−→T(L) in D(M).
Exercise 7.5.3. Prove Proposition 7.5.2.
The last two propositions say that the abelian category M, with its kernels and
cokernels, can be recovered from the triangulated category D(M).
Remark 7.5.4. Assume that the diagram in Proposition 7.5.2 is an exact se-
quence. By Proposition 5.3.10, this sequence is split if and only if the morphism
θ is zero. Furthermore, if M has enough injectives, then there is a canonical bijec-
tion between the set of isomorphism classes of extensions of N by L, and the set
HomD(M)(N, T(L)). See [62, Section I.6], or use Exercise 12.2.7, which says that
HomD(M)(N, T(L)) ∼= Ext1
M(N, L).
