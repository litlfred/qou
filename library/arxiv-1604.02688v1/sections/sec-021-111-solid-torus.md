---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-021-111-solid-torus
section_title: "Solid torus"
section_number: 11.1
pages: 34-35
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
the contribution of S to the 3D-index sum has q1/2-degree d(S) ≥1.
Proof. Since S is irreducible, it contains no tetrahedral solution summand, so S = S∗is
the minimal non-negative coset representative of [S] = S + T. Then S∗contains at most
two quad types in each tetrahedron, so can be replaced by an embedded generalised normal
surface ˜S by Lemma 10.5. Now ˜S is connected since S is irreducible, and d(S) ≥−χ( ˜S) by
Lemma 10.8. Assume ﬁrst that ˜S is not simple, so there are at least two of two diﬀerent
quadrilateral types in some tetrahedron for S∗. But then Lemma 10.8 implies that d(S) ≥2.
On the other hand, if ˜S is simple and M is not a solid torus, then χ( ˜S) < 0 by Theorem
10.16, hence d(S) ≥1. This completes the proof.
□
Remark 10.20. This result fails for 1-eﬃcient triangulations of the solid torus and T 2 × I.
Here every normal class S contributing to the index sum has degree d(S) ≥0, but an almost
normal torus S gives a contribution d(S) = 0. (Compare Example 11.1 below.)
One consequence of Corollary 10.19 and Remark 10.20 is the following basic fact about
the 3D-index.
Corollary 10.21. If T is a 1-eﬃcient ideal triangulation then the 3D-index I0
T(0) is a formal
power series in q1/2, not just a formal Laurent series in q1/2.
In general, we expect that the minimum q1/2-degree dmin of I0
T(kb) grows quadratically as
k →+∞. However this is no longer true if b is the boundary of an embedded spun normal
surface.
Lemma 10.22. Assume T is a 1-eﬃcient triangulation of a 3-manifold other than the solid
torus or T 2×I. Assume that T contains an embedded spun normal surface S with ∂S = b̸ = 0,
and that S is the only irreducible spun normal class in Q(T; Z+) whose boundary is a positive
integer multiple of b. Then the minimum q1/2-degree dmin of I0
T(kb) grows at mostly linearly
as k →+∞. In fact, dminI0
T(kb) ≤−χ(S)k for all even k ≥0.
Proof. For each even k ≥0, kS has ∂(kS) = kb and [kS] = 0 so contributes a term to I0
T(kb)
with d(kS)∗) = d(kS) = −χ(S)k + δ(S)k2 = −χ(S)k. Now, by our assumption, any S′ with
∂S′ = b can be written as S′ = kS+S0 where ∂S0 = 0. Hence d(S′) ≥d(kS)+d(S0) > d(kS)
unless S0 = 0 by Corollary 10.19.
□
Example 10.23. For the ﬁgure eight knot complement, with its canonical triangulation
T given in Example 4.1, there are embedded, essential, spun normal once-punctured Klein
bottles with boundary b = ±4µ ± λ and Euler characteristic χ = −1 giving a term in I0
T(kb)
of degree −χk = k for each k ≥0. Further this is the only irreducible spun normal class with
boundary a positive multiple of b, so by Lemma 10.22 this is the minimum q1/2-degree of
I0
T(kb). (Compare the calculations for I0
T(8µ+2λ) = IT(4µ+λ) and I0
T(4µ+λ) = IT(2µ+ 1
2λ)
given in Example 4.1.)
THE 3D-INDEX AND NORMAL SURFACES
35
For the trefoil knot complement, with its 2 tetrahedra triangulation T given in Example
11.2, we have I0
T((xµ + yλ)) = δ0,x+6y. Here there is an embedded, essential, spun normal
Möbius strip S with boundary b = ±(6µ −λ) giving a contribution to I0
T(kb) of degree
0 = −χ(S)k for all k ∈Z+. Further, this is the only irreducible spun normal class with
boundary a positive multiple of b, so Lemma 10.22 again applies.
