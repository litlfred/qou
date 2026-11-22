---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-009-31-the-knot-41
section_title: "The knot 41"
section_number: 3.1
pages: 12-14
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
The knot complement M of the knot 41 decomposes into two ideal tetrahedra 1
and 2. Using the default triangulation of SnapPy for 41 with isometry signature
cPcbbbiht_BaCB, the gluing equations are
e1 : z2
1z′
1z2
2z′
2 = 1,
e2 : z′
1(z′′
1)2z′
2(z′′
2)2 = 1 ,
the corresponding gluing equation matrices are
G =

2 2
0 0

,
G′ =

1 1
1 1

,
G′′ =

0 0
2 2

,
and the NZ matrices are
A =

1
1
−1 −1

,
B =

−1 −1
1
1

with
ABT =

−2 2
2 −2

symmetric. We can read the above information by looking at the triangulated cusp shown
in Fig. 3.
To describe the ideal triangulation T of the inﬁnite cyclic cover 
M of M, we consider
the triangulation of the peripheral torus induced from T = {1, 2} (see Fig. 3) together
with its lift to the universal cover, the Euclidean plane E2. Note that each triangle of E2
with corner zj has a label j ∈{1, 2} of the corresponding tetrahedron.
We now describe a second labeling of each triangle of E2 by an integer, obtained by
choosing a cocycle representative of the abelianization map α : π1(M) ↠Z. This con-
struction is standard and is appears in unpublished work of Goerner and also in Zickert
[29, Sec.3.5]. Let G denote the dual dual 1-skeleton of the triangulation of E2 (see Fig. 4).
Each vertex and edge of G correspond to a tetrahedron and face-pairing of T , respectively,
and that the edges of G are oriented from 0 to 1. Since the face-pairings generate the
fundamental group π1(M), one can assign an integer α(pi) to each face-pairing pi cor-
responding to the abelianization map α : π1(M) ↠Z. Since in our case there are two
Fig. 4 Face-pairings
Fig. 5 The dual 1-complex of E2, where the labeling α(v)j of a vertex v indicates that v is labeled by the j-th
tetrahedron
tetrahedra, we have four face-pairings, thus four integers α(p1), . . . , α(p4) that are required
to satisfy
α(p2) −α(p4) = 1
α(p1) −α(p4) = 1,
α(p1) −α(p3) = 1
α(p2) −α(p3) = 1.
(39)
Note that these equations are directly obtained from Fig. 4 with the μ-action described in
Fig. 3.
Since E2 is a contractible space, we can assign an integer α(v) to each vertex v of G
such that α(v2) −α(v1) = α([v1, v2]), where [v1, v2] is an oriented edge of G from v1 to v2.
Explicitly, the general solution of the linear equations (39) is given by
(α(p1), α(p2), α(p3), α(p4)) = (a, a, a −1, a −1)
(a ∈Z).
(40)
It follows from the construction that if a vertex v corresponds to j in T , then it corre-
sponds to μα(v) · j in T . Choosing (α(p1), α(p2), α(p3), α(p4)) = (0, 0, −1, −1) and α(v)
andei as in Fig. 4, we obtain the table
0
1
2
e1
z′
2
z2
1z2
2
z′
1
e2
z′
1(z′′
2)2
(z′′
1)2z′
2
where the (i, k)-entry is the product of shape parameters contributed from μk · 1 and
μk · 2 toei (the empty entries are 1). The gluing equation aroundei is the product of the
entries of the corresponding row in the above table, i.e., the product over the vertices of
polygons around each edgeei in Fig. 4. Hence, we have
G(t) =

2t 2t
0 0

,
G′(t) =

t2 1
t t2

,
G′′(t) =

0
0
2t2 2t

,
(41)
A(t) =

−t2 + 2t 2t −1
−t
−t2

,
B(t) =

−t2
−1
2t2 −t −t2 + 2t

,
(42)
37
Page 14 of 23
Fig. 6 The triangulation of the peripheral torus of 63
giving that
A(t)B(1/t)T =

−2t + 2 −2t−1
t + t−2
t2 + t−1
−2t + 2 −2t−1

,
which specializes to the matrix ABT when t = 1.
