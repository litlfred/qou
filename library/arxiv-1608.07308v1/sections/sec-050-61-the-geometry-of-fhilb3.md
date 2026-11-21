---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-050-61-the-geometry-of-fhilb3
section_title: "The geometry of FHilb3"
section_number: 6.1
pages: 48-49
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
late a precise conjecture about the sheaf ι∗(ﬁgure eight knot). Recall the matrix presentation:
FHilb3 =


X =


x1
0
0
a
x2
0
α1
α2
x3

, Y =


0
0
0
b
0
0
β1
β2
0

, [X, Y ] = 0,
(6.1)
v =


1
0
0

cyclic



.
conjugation by g =


1
0
0
0
c
0
0
t
d


Note that in the presentation above, we ﬁxed the vector v (and this ﬁxes the ﬁrst column of the
conjugating matrix) to eliminate certain coordinates. Note that the map FHilb3 →FHilb2 is
given by only retaining the top 2 × 2 corners of the matrices in question. If one is given the
eigenvalues x1, x2, x3 and the point [a : b] ∈P1, then the datum one needs to construct a point
in FHilb3 is the vector:
(6.2)
(α1, α2, β1, β2) ∈T ∨
2 ⊕T ∨
2
To ensure that the equation [X, Y ] = 0 is satisﬁed, we need to ensure that:
(x1 −x3)β1 = α2b −β2a
and
(x2 −x3)β2 = 0
Moreover, the fact that we quotient out by conjugation matrices implies that we must identify:
(α1, α2, β1, β2) ∼(α1+ta, α2+t(x2−x3), β1+tb, β2)
and
(α1, α2, β1, β2) ∼d(α1, α2, β1, β2)
for t ∈C and d ∈C∗. Unwinding these facts, one sees that the datum (6.2) corresponds
to a vector in H0(E∨
2 ), where E2 is the complex in (2.25) when ∗= C. It is elementary to
prove that E2 and E∨
2 are quasi-isomorphic to their zero-th cohomology, so we conclude that
FHilb3 = FHilbdg
3 . The irreducible components of the ﬂag Hilbert scheme FHilb3 are:
FHilb3(C) = Z1 ∪Z2 ∪Z3 ∪Z4 ∪Z5
where Z1, . . . , Z5 are determined by which eigenvalues x1, x2, x3 are equal to each other:
Z1 = {x1̸ = x2̸ = x3̸ = x2},
Z2 = {x1 = x2 = x3}
Z3 = {x1 = x2̸ = x3}, Z4 = {x3 = x1̸ = x2}, Z5 = {x2 = x3̸ = x1}
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOVANOV-ROZANSKY HOMOLOGY
49
On Z1, because the eigenvalues are generically distinct, the commutation relation [X, Y ] = 0
forces Y = 0. Then the cyclicity of the vector v implies a, α̸ = 0, and so conjugation by g
allows one to set a = α = 1 and e = 0. We conclude that:
(6.3)
Z1 = C3
As for Z2, note that one can always subtract a constant matrix from X without changing any of
the other properties of (6.1). By (2.29), we see that:
(6.4)
Z2 = FHilb2(point) × C = PP1
O(1)
qt
⊕O(−2)

× C
