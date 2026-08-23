---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-015-6-example-figure-eight-knot
section_title: "Example: Figure-Eight Knot"
section_number: 6
pages: 24-28
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We shall demonstrate how to decompose the knot complement in to tetrahedra in a case of the
ﬁgure-eight knot. The ﬁgure-eight knot is given as σ1 σ −1
2 σ1 σ −1
2 in the braid group, and is de-
picted as Fig. 12. To each crossing in the ﬁgure-eight knot, w e assign the octahedron (Fig. 5 or
eq. (5.7)), and give the numbering to each crossing as in Fig.13. We have also named each surface
as Di. We call the surface inside the octahedron as Sa
i,j ; a surface is in the octahedron of the a-th
crossing, and is a boundary between Di and Dj.
Figure 12: The ﬁgure-eight knot 41.
In a surface D1 there are 3 tetrahedra. These three tetrahedra are glued to e ach other as shown
in Fig. 14. Due to the pentagon relation we obtain 2 adjacent t etrahedra, whose common surface
(gray surface) is named P1.
24
PSfrag replacements
D0
D1
D2 D3
D4
D5
① ②
③
④
Figure 13: We attach octahedra for each crossing of the ﬁgure-eight knot.
PSfrag replacements
S1
1, 2
S1
1,4
S3
1, 3S3
1, 2
S2
1,4
S2
1, 3
① ②
③
⇐ ⇒
PSfrag replacements
S 11, 4
S
2
1, 3
S3
1,2
S 11, 2
S
2
1, 4
S3
1,3
Figure 14: Gluing 3 tetrahedra in surface D1 results in 2 tetrahedra by the 2-3 Pachner move. The
gray surface in the 2 adjacent tetrahedra is called P1.
25
Three tetrahedra in a surface D0 also gives same adjacent tetrahedra with that in Fig. 14. By
the same method of gluing 3 tetrahedra in surfaces D2 and D3, we obtain adjacent tetrahedra as
shown in Fig. 15.
(a)
PSfrag replacements
S 40, 3
S
2
0, 4
S1
0,2
S 40, 2
S
2
0, 3
S1
0,4
(b)
PSfrag replacements
S 31, 2
S
4
2, 5
S1
0,2
S 32, 5
S
4
0, 2
S1
1,2
(c)
PSfrag replacements
S 40, 3
S
3
3, 5
S2
1,3
S 43, 5
S
3
1, 3
S2
0,3
Figure 15: Gluing 3 tetrahedra in surfaces (a) D0, (b) D2, and (c) D3 gives the 2 adjacent tetrahe-
dra. We call each gray surface respectively P0, P2, and P3.
In a surface D4, we have 2 tetrahedra, which are glued to each other and result in a suspension
as shown in Fig. 16. We also get a suspension from a surface D5 as is shown in Fig. 17.
PSfrag replacements
S1
1, 4
S1
0,4
S2
1, 4
S2
0,4
① ②
⇐ ⇒PSfrag replacements
S2
0, 4
S1
1,4
S1
0,4
S2
1, 4
Figure 16: Gluing 2 tetrahedra in a surface D4 gives a suspension.
We next glue these polyhedra, 4 2-adjacent-tetrahedra (Fig. 14 and Fig. 15) and 2 suspensions
(Fig. 16 and Fig. 17). We ﬁrst cut those polyhedra in the plane which was painted gray in ﬁgures,
and separate them into “upper” and “lower” polyhedra (tetrahedra or cones). In this procedure, we
should remember which vertices in the gray faces were glued t o each other. We then glue these
polygons to each other which have same surfaces Sa
i,j , and we ﬁnally obtain 2 tetrahedra (Fig. 18)
which come from upper and lower polyhedra. Faces in these tet rahedra present gray faces in
26
PSfrag replacements S4
2, 5
S3
3,5
S3
2,5
S4
3, 5
Figure 17: Gluing 2 tetrahedra in a surface D5.
Figs. 14–15 which separates upper and lower polyhedra. It is a well known result by Thurston [5]
that the complement of the ﬁgure-eight knot is decomposed in to these 2 tetrahedra. Note that, in
order to have upper and lower polyhedra, we have used the so-c alled 1-4 Pachner move which
shows that neighborhood of vertex inside the tetrahedron co nstitute sphere as was pointed out in
Ref. 8.
PSfrag replacements
P0
P1
P2
P3
P0
P1
P2
P3
Figure 18: Complement of the ﬁgure-eight knot.
The partition function of the complement of the ﬁgure-eight knot is then computed from
Fig. (18) as
τ1(41) =
∫
d⃗ p⟨p1 = 0, p2 | S | p3, p4⟩ ⟨p4, p3 | S−1 | p2, p1 = 0⟩
∼
∫
dp exp 1
2 i γ
(
Li2(e−p) − Li2(ep)
)
. (6.1)
Here we have introduced a restrictionp1 = 0 which comes from a computation of the knot invariant
for a (1, 1)-tangle. The integral in the partition function can be evaluated at the saddle point,
(1 − ep) (1 − e−p) = 1 ,
27
which, with a root of ω2 − ω + 1 = 0 , gives
˜τ1(41) = lim
γ →0
(2 i γ log τ1(41)) = 2 .02988 i. (6.2)
The imaginary part is nothing but the hyperbolic volume of th e complement of the ﬁgure-eight
knot.
