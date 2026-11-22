---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-044-51-the-geometry-of-fhilb2
section_title: "The geometry of FHilb2"
section_number: 5.1
pages: 42-43
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
this section we construct explicitly the functors ι∗and ι∗between the category of sheaves on
FHilb2 and the category of Soergel bimodules SBim2. We have the matrix presentation:
FHilb2 =

X =

x1
0
z
x2

, Y =

0
0
w
0

, [X, Y ] = 0, v =

1
0

cyclic

conjugation by g =

1
0
0
c

Note that in the presentation above, we ﬁxed the vector v (and this ﬁxes the ﬁrst column of the
conjugating matrix) to eliminate some coordinates. Unwinding the above gives us:
(5.1)
FHilb2 = {(x1, x2, z, w), (x1 −x2)w = 0, z, w not both zero}
(x1, x2, z, w) ∼(x1, x2, cz, cw)
= Proj(A)
where x1, x2, z, w have degrees 0, 0, 1, 1 in the graded algebra:
(5.2)
A = C[x1, x2, z, w]
(x1 −x2)w
Recall the complex (2.25):
(5.3)
E1 =

qtO
(0,x1−x2,0)
−−−−−−→qO ⊕tO ⊕O
(x1−x2,0,1)T
−−−−−−−→O

FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOVANOV-ROZANSKY HOMOLOGY
43
on FHilb1(C) × C = C2, from which it is clear the the leftmost map is injective and the
rightmost map is surjective on all ﬁbers. Therefore, we have H0(E1) ∼= E1 and hence:
FHilb2 ∼= FHilbdg
2
Moreover, letting z and w be coordinates on the ﬁrst two summands of the middle space of
(5.3), we observe that H0(E1) = (Oz ⊕Ow)/(x1 −x2)w, which matches the algebra (5.2).
The irreducible components of the ﬂag Hilbert scheme are:
(5.4)
FHilb2 = Z1 ∪Z2
where:
(5.5)
Z1 = {x1̸ = x2} = {b = 0} = C2 with coordinates (x1, x2) = Proj(A/wA)
(5.6)
Z2 = {x1 = x2} = C × P1 with coordinates (x, [z : w]) = Proj(A/(x1 −x2)A)
The intersection of these two irreducible components is:
Z1 ∩Z2 = C × [1 : 0] = C × {I(2)}
while the other torus ﬁxed point I(1,1) satisﬁes:
Z1̸ ∋I(1,1) ∈Z2, I(1,1) = (0, [0 : 1])
•
•
I(2)
I(1,1)
Z1
Z2
FIGURE 8. Flag Hilbert scheme of two points
