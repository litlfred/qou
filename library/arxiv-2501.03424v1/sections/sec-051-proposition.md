---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-051-proposition
section_title: "Proposition"
section_number: null
pages: 22-23
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
Proposition
Let A, B be abelian categories, and let F : A →B, G : B →A be functors. If F is left adjoint to
G and G is exact, then F sends projective objects to projective objects.
Proof:
Recall that an object P in an abelian category is projective if and only if the functor
HomA(P, −) : A →Ab is exact. With the above setup, let P ∈A be a projective object. Then, for
every short exact sequence
0
X′
X
X′′
0
the following sequence is exact:
0
HomA(P, X′)
HomA(P, X)
HomA(P, X′′)
0.
Since F is left adjoint to G, we have the natural isomorphism
HomB(F(A), B) ≃HomA(A, G(B))
for every A ∈A, B ∈B. We want to ﬁnd out whether the functor HomB(F(P), −) : B →Ab is
exact. By adjointness, for every object Y in B, we have the isomorphism
HomB(F(P), Y ) ≃HomA(P, G(Y )).
It follows that HomB(F(P), −) ≃HomA(P, G(−)) as functors B →Ab. Since P is projective,
HomA(P, −) is exact as a functor A →Ab. Moreover, G is exact by assumption. Notice that the
composition of exact functors is exact. Then, if
0
Y ′
Y
Y ′′
0
is a short exact sequence in B, applying G gives us the short exact sequence
0
G(Y ′)
G(Y )
G(Y ′′)
0
in A. Composing with HomA(P, −) gives us the short exact sequence
0
HomA(P, G(Y ′))
HomA(P, G(Y ))
HomA(P, G(Y ′′))
0.
in Ab. By the isomorphism HomB(F(P), −) ≃HomA(P, G(−)), it follows that
0
HomA(F(P), Y ′)
HomA(F(P), Y )
HomA(F(P), Y ′′)
0
is a short exact sequence, and hence F(P) is projective in B.
22
