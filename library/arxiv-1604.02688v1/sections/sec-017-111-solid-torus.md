---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-017-111-solid-torus
section_title: "Solid torus"
section_number: 11.1
pages: 34-35
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
the contribution ofS to the 3D-index sum hasq1/2-degreed(S)≥ 1.
Proof. Since S is irreducible, it contains no tetrahedral solution summand, soS = S∗ is
the minimal non-negative coset representative of[S] = S + T. Then S∗ contains at most
two quad types in each tetrahedron, so can be replaced by an embedded generalised normal
surface ˜S by Lemma 10.5. Now˜S is connected sinceS is irreducible, andd(S)≥−χ( ˜S) by
Lemma 10.8. Assume ﬁrst that˜S is not simple, so there are at least two of two diﬀerent
quadrilateral types in some tetrahedron forS∗. But then Lemma 10.8 implies thatd(S)≥ 2.
On the other hand, if˜S is simple andM is not a solid torus, thenχ( ˜S) < 0 by Theorem
10.16, henced(S)≥ 1. This completes the proof. □
Remark 10.20. This result fails for 1-eﬃcient triangulations of the solid torus andT 2×I.
Here every normal classS contributing to the index sum has degreed(S)≥ 0, but an almost
normal torusS gives a contributiond(S) = 0. (Compare Example 11.1 below.)
One consequence of Corollary 10.19 and Remark 10.20 is the following basic fact about
the 3D-index.
Corollary 10.21.If T is a 1-eﬃcient ideal triangulation then the 3D-indexI0
T(0) is a formal
power series inq1/2, not just a formal Laurent series inq1/2.
In general, we expect that the minimumq1/2-degreedmin ofI0
T(kb) grows quadratically as
k→ +∞. However this is no longer true ifb is the boundary of an embedded spun normal
surface.
Lemma 10.22.Assume T is a 1-eﬃcient triangulation of a 3-manifold other than the solid
torus orT 2×I. Assume thatT contains an embedded spun normal surfaceS with∂S =b⁄= 0,
and thatS is the only irreducible spun normal class inQ(T; Z+) whose boundary is a positive
integer multiple ofb. Then the minimumq1/2-degreedmin of I0
T(kb) grows at mostly linearly
as k→ +∞. In fact,dminI0
T(kb)≤−χ(S)k for all evenk≥ 0.
Proof. For each evenk≥ 0,kS has∂(kS) =kb and [kS] = 0 so contributes a term toI0
T(kb)
withd(kS)∗) =d(kS) =−χ(S)k +δ(S)k2 =−χ(S)k. Now, by our assumption, anyS′ with
∂S′ =b can be written asS′ =kS +S0 where∂S0 = 0. Henced(S′)≥d(kS)+d(S0)>d (kS)
unless S0 = 0 by Corollary 10.19. □
Example 10.23. For the ﬁgure eight knot complement, with its canonical triangulation
T given in Example 4.1, there are embedded, essential, spun normal once-punctured Klein
bottles with boundaryb =±4µ±λ and Euler characteristicχ =−1 giving a term inI0
T(kb)
of degree−χk =k for eachk≥ 0. Further this is theonly irreducible spun normal class with
boundary a positive multiple ofb, so by Lemma 10.22 this is the minimumq1/2-degree of
I0
T(kb). (Compare the calculations forI0
T(8µ+2λ) =IT(4µ+λ) andI0
T(4µ+λ) =IT(2µ+ 1
2λ)
given in Example 4.1.)
THE 3D-INDEX AND NORMAL SURF ACES 35
For the trefoil knot complement, with its 2 tetrahedra triangulationT given in Example
11.2, we haveI0
T((xµ +yλ)) = δ0,x+6y. Here there is an embedded, essential, spun normal
Möbius strip S with boundary b =±(6µ−λ) giving a contribution toI0
T(kb) of degree
0 = −χ(S)k for all k∈ Z+. Further, this is the only irreducible spun normal class with
boundary a positive multiple ofb, so Lemma 10.22 again applies.
