---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-012-51-r-operators-as-the-braid-operator
section_title: "R-Operators as the Braid Operator"
section_number: 5.1
pages: 14-18
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We now give the 3-dimensional picture of the R-operators (2.23), and study the relationship be-
tween the hyperbolic geometry and our invariant. The R-operator consists from four S operators,
and its matrix element ⟨⃗ p| ˇR12, 34 | ⃗p′⟩ is explicitly given by
⟨p1, p2, p3, p4 | ˇR12, 34 | p′
1, p′
2, p′
3, p′
4⟩
=
∫ ∫ ∫ ∫
dx dy dz dw ⟨p3, w | S−1 | x, p2⟩ ⟨y, p′
4 | S | p4, w⟩ ⟨p′
2, z | S−1 | y, p′
3⟩ ⟨x, p1 | S | p′
1, z⟩.
(5.1)
This integration can be performed explicitly as eq. (2.28), but we work with this form to see a
gluing condition clearly. As we regard the S-operators as the oriented (ideal) tetrahedron (Fig. 3),
the ˇR-operator is depicted as the oriented octahedron in Fig. 5 bygluing faces of tetrahedra to each
other. From the symmetry of theR-matrix (2.29b), the operator ˇR−1 is written as the octahedron in
Fig. 6. Assignment of the octahedron to the braiding operato r ﬁrst appeared in Ref. 10, and it was
later used to give the decomposition of the knot complement directly from Kashaev’s invariant [8].
Our result in Fig. 5 is essentially same with one in Ref. 10, an d this agreement suggests that our
knot invariant τ1(K) is indeed deﬁned as a non-compact analogue of Kashaev’s invariant (the col-
ored Jones polynomial at a ﬁxed value), only replacing theﬁnite-dimensional representation of the
quantum dilogarithm function with the inﬁnite-dimensional one. Consequently the decomposition
of the knot complement which will be presented below is same w ith one given in Ref. 8 (see also
Ref. 9).
The braiding property can be seen from the realization of the R-operators as in Figs. 5–6.
When we suppose that the gray bold lines in those ﬁgures denot e the link L and we look down
14
PSfrag replacements
p′
3
p
′
4
p1
p2
p′
1
p′
2
p3
p4
Figure 5: The braid operator ( ˇR-matrix) ⟨⃗ p| ˇR | ⃗p′⟩ is represented by the octahedron.
PSfrag replacements
p4
p3p ′
2
p′
1
p′
3
p′
4
p1
p2
Figure 6: The inverse of the ˇR-matrix, ⟨⃗ p| ˇR−1 | ⃗p′⟩, is represented by the same octahedron with
the ˇR operator, though the content is different.
15
each octahedron from the top, we ﬁnd that the braiding is indeed realized as follows;
⟨⃗ p| ˇR | ⃗p′⟩ =
p1
p2 p3
p4
p′
1
p′
2 p′
3
p′
4
(5.2a)
⟨⃗ p| ˇR−1 | ⃗p′⟩ =
p1
p2 p3
p4
p′
1
p′
2 p′
3
p′
4
(5.2b)
We should stress that every 0-simplex of the octahedron is on the link L, and that the octahedron
is in the complement of the link L.
We shall check the hyperbolicity consistency condition in constructing the R-operator from the
ideal tetrahedra in a case of γ → 0. Substituting the asymptotic form (4.1) into eq. (5.1), we get
⟨⃗ p| ˇR12, 34 | ⃗p′⟩ ∼ δ(p1 − p2 + p3 − p′
1) δ(p′
2 − p′
3 + p′
4 − p4)
×
∫ ∫
dz dw exp 1
2 i γ
(
−Li2(ew−p2) + Li2(ew−p′
4) − Li2(ez−p′
3) + Li2(ez−p1)
+ (−p1 + p′
1) (−w + p2 + z − p1) + (p4 − p′
4) (w − p′
4 − z + p′
3)
)
. (5.3)
Here we have used trivial constraints;
x = −p1 + p′
1, y = p4 − p′
4. (5.4)
Above integral is evaluated by the saddle point, in which we have constraints
1 − ew−p2
1 − ew−p′
4
ep1−p′
1+p4−p′
4 = 1, 1 − ez−p′
3
1 − ez−p1
e−p1+p′
1−p4+p′
4 = 1.
This set of equations solves
ew = 1 − ep1−p′
1+p4−p′
4
e−p′
4 − ep1−p′
1+p4−p′
4−p2
, ez = 1 − ep1−p′
1+p4−p′
4
e−p′
3 − ep1−p′
1+p4−p′
4−p1
, (5.5)
and we easily ﬁnd a constraint,
1 − ew−p2
1 − ew−p′
4
· 1 − ez−p′
3
1 − ez−p1
= 1, (5.6)
16
which coincides with the hyperbolicity condition around vertical axis (crossing point in eq (5.2)).
Due to the symmetry of the R-operator (2.29), we can conclude that for each crossing in a link
L we can attach the oriented octahedron, which has a following projection;
⨂
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63
/d63/d63/d63/d63/d63/d63/d63/d63/d63
/d95/d95/d63/d63/d63/d63/d63/d63/d63/d63/d63
/d63/d63/d63/d63/d63/d63/d63/d63/d63 /d127/d127/d127/d127/d127/d127/d127/d127
/d127/d127/d127/d127/d127/d127
/d63/d63/d127/d127/d127/d127/d127/d127
/d127/d127/d127/d127/d127/d127
/d15/d15/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d111/d111/d95 /d95 /d95 /d95 /d95 /d95/d95 /d95 /d95 /d95 /d95 /d95
/d47/d47/d95 /d95 /d95 /d95 /d95 /d95 /d95 /d95 /d95 /d95 /d95 /d95
/d79/d79/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d127/d127/d127/d127/d127
/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63
/d63/d63/d63/d63/d63
/d63/d63/d63/d63/d63
/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127
/d127/d127/d127/d127/d127
p1
p2 p3
p4
p′
1
p′
2 p′
3
p′
4
⟨p3, w | S−1 | x, p2⟩
⟨p′
2, z | S−1 | y, p′
3⟩
⟨x, p1|S|p′
1, z⟩
⟨y, p′
4 | S | p4, w⟩w
z
x
y
a4
a3
a1
a2
(5.7)
Here x and y are auxiliary momenta given by eq. (5.4), and w and z are ﬁxed by eq. (5.5). We
further have
p3 = −p1 + p2 + p′
1, p ′
2 = p4 + p′
3 − p′
4. (5.8)
and the dihedral angles ai satisfying a1 a2 a3 a4 = 1 are given by
a1 = (1 − ez−p1)−1 = ep1−p′
1+p4−p′
4 − ep1−p′
3
1 − ep1−p′
3
,
a2 = 1 − ez−p′
3 = 1 − ep1−p′
3
1 − e−p1+p′
1−p4+p′
4ep1−p′
3
,
a3 = (1 − ew−p′
4)−1 = 1 − e−p1+p′
1−p4+p′
4ep2−p′
4
1 − ep2−p′
4
,
a4 = 1 − ew−p2 = 1 − ep2−p′
4
ep1−p′
1+p4−p′
4 − ep2−p′
4
.
To close this section, we give an explicit form of an asymptot ic form of the ˇR-operators. As
the integral (2.28) has an asymptotic form,
H(a, b, c, d)
∼ exp 1
2 i γ
(
Li2(ea−b) + Li2(ed−a) − Li2(ec−b) − Li2(ed−c) + c (−a + b − c + d)
)
, (5.9)
17
the ˇR±1 operators in a limit γ → 0 are respectively given by
⟨⃗ p| ˇR12, 34 | ⃗p′⟩ ∼ δ(p1 + p3 − p2 − p′
1) · δ(p′
2 − p′
3 + p′
4 − p4)
× exp 1
2 i γ
(
Li2(ep4−p3) + Li2(ep′
3−p1) − Li2(ep′
4−p2) − Li2(ep′
2−p′
1)
+ (p′
1 − p1) (−p4 + p3 − p′
1 + p′
2)
)
, (5.10a)
⟨⃗ p| ( ˇR12, 34)−1 | ⃗p′⟩ ∼ δ(p′
4 − p2 + p3 − p4) δ(p1 − p′
1 − p′
3 + p′
2)
× exp 1
2 i γ
(
Li2(ep2−p1) + Li2(ep4−p′
2) − Li2(ep3−p′
1) − Li2(ep′
4−p′
3)
+ (p1 − p′
1) (p1 − p2 − p′
3 + p′
4)
)
. (5.10b)
In constructing the knot invariantτ1(K), we need another operator µ (3.5). The matrix element
of the µ-operator can be computed simply, and in the classical limit γ → 0 reduces to
⟨p1, p2 | µ | p′
1, p′
2⟩ ∼ δ(p1 − p′
1) δ(p2 − p′
2) · exp π
γ
(
p1 − p2
)
. (5.11)
Thus the saddle point condition coming from the µ-operator is always 2 π i, and we can ignore a
contribution from the µ-operator to the saddle point condition.
In the rest of this section, we study how to glue these octahed ra in the invariant τ1(K). We
show that for every gluing there exists a correspondence bet ween the saddle point equations and
the hyperbolicity consistency conditions around edge.
