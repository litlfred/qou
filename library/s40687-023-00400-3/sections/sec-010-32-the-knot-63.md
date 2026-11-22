---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-010-32-the-knot-63
section_title: "The knot 63"
section_number: 3.2
pages: 14-16
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
The
default
SnapPy
triangulation
of
the
knot
63
with
isometry
signature
gLLPQccdefffhggaacv_aBBb has six tetrahedra 1, . . . , 6 with the peripheral torus
shown in Fig. 6.
The gluing equations of the six edges are
e1 : z1z2z3z4z6 = 1,
e2 : z′
1z′
2(z′′
2)2z′
4(z′′
4)2z′
6 = 1,
e3 : z′′
1z′
2z′
3z′
5z′′
6 = 1,
e4 : z′′
1z′
3z′
4z′
5z′′
6 = 1,
e5 : z′
1z3(z′′
3)2z5(z′′
5)2z′
6 = 1,
e6 : z1z2z4z5z6 = 1
and the corresponding gluing equation matrices are
G =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
1 1 1 1 0 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 1 0
1 1 0 1 1 1
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
G′ =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0 0 0 0 0 0
1 1 0 1 0 1
0 1 1 0 1 0
0 0 1 1 1 0
1 0 0 0 0 1
0 0 0 0 0 0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
G′′ =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0 0 0 0 0 0
0 2 0 2 0 0
1 0 0 0 0 1
1 0 0 0 0 1
0 0 2 0 2 0
0 0 0 0 0 0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
.
(43)
Fig. 7 The dual 1-skeleton of E2
The NZ matrices are
A =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
1
1
1
1
0
1
−1 −1 0 −1 0 −1
0 −1 −1 0 −1 0
0
0 −1 −1 −1 0
−1 0
1
0
1 −1
1
1
0
1
1
1
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
B =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0
0
0
0
0
0
−1 1
0
1
0 −1
1 −1 −1 0 −1 1
1
0 −1 −1 −1 1
−1 0
2
0
2 −1
0
0
0
0
0
0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
with
ABT =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0 0
0
0
0 0
0 0 −1 −1 2 0
0 −1 3
2 −4 0
0 −1 2
3 −4 0
0 2 −4 −4 6 0
0 0
0
0
0 0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
symmetric. As in Sect. 3.1, we assign an integer to (each oriented edge and) each vertex
of the dual complex according to the abelianization map α : π1(M) ↠Z. See Fig. 7.
Choosing a liftei of ei as in Fig. 7, we have the table
0
1
2
3
e1
z4
z1z3z6
z2
e2
z′
1z′′
4
z′′
2z′
4
z′
2z′′
4
z′′
2z′
6
e3
z′′
1z′
5
z′
2z′
3z′′
6
e4
z′′
1z′
3z′
4
z′
5z′′
6
e5
z′′
3z′′
5z′
6
z3z5
z′
1z′′
3z′′
5
e6
z1z2z4z5z6
37
Page 16 of 23
where the (i, k)-entry is the product of shape parameters contributed from μk ·1, . . . , μk ·
6 toei. Hence, we have
G(t) =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
t t2 t 1 0 t
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 t 0 t 0
t2 t2 0 t2 t2 t2
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
, G′(t) =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0 0 0 0 0 0
1 t2 0 t 0 t3
0 t
t 0 1 0
0 0 t2 t2 t3 0
t2 0 0 0 0 1
0 0 0 0 0 0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
G′′(t) =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0
0
0
0
0
0
0 t + t3
0
1 + t2
0
0
1
0
0
0
0
t
t2
0
0
0
0
t3
0
0
1 + t2
0
1 + t2 0
0
0
0
0
0
0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
(44)
and
A(t) =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
t
t2
t
1
0
t
−1 −t2
0
−t
0
−t3
0
−t
−t
0
−1
0
0
0
−t2 −t2 −t3
0
−t2
0
t
0
t
−1
t2
t2
0
t2
t2
t2
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
B(t) =
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎝
0
0
0
0
0
0
−1 t −t2 + t3
0
1 −t + t2
0
−t3
1
−t
−t
0
−1
t
t2
0
−t2
−t2
−t3
t3
−t2
0
1 + t2
0
1 + t2 −1
0
0
0
0
0
0
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
(45)
giving that
A(t)B(1/t)T =
⎛
⎜⎜⎜⎜⎜⎜⎝
0
0
0
0
0
0
0 −2t + 4 −2t−1
−t2 + t −1
−1 + t−1 −t−2
t3 + t−2
0
0 −1 + t−1 −t−2
3
t−1 + t−3
−t −1 −t−1 −t−2 0
0
−t2 + t −1
t3 + t
3
−t3 −t2 −t−1 −1 0
0
t2 + t−3
−t2 −t1 −1 −t−1 −1 −t−1 −t−2 −t−3
2t + 2 + 2t−1
0
0
0
0
0
0
0
⎞
⎟⎟⎟⎟⎟⎟⎠
which specializes to matrix ABT when t = 1.
