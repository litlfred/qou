---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-014-52-the-knot-63
section_title: "The knot 63"
section_number: 5.2
pages: 21-22
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
In this section, we give the geometric solution and the ﬂattenings of the triangulation of
the 63 knot to compute its twisted 1-loop invariant, following the notation of Sect. 3.2.
The trace ﬁeld of the 63 knot is the number ﬁeld of type [0, 3] and discriminant −11·312
given by F = Q[ξ] where ξ ≈1.073 −0.558√−1 satisﬁes ξ6 −ξ5 −ξ4 + 2ξ3 −ξ + 1 = 0.
The solution for the complete structure is given exactly
(z1, z2, z3, z4, z5, z6) = (−ξ2 + ξ, −ξ2 + 1, −ξ3 + ξ, −ξ2 + 1, −ξ3 + ξ, −ξ2 + ξ)
(71)
and approximately by
z1 ≈0.23279 + 0.64139 i, z2 ≈0.15884 + 1.20014 i, z3 ≈0.84116 + 1.20014 i,
37
Page 22 of 23
z4 ≈0.15884 + 1.20014 i, z5 ≈0.84116 + 1.20014 i, z6 ≈0.23279 + 0.64139 i.
It is easy to check that (f1, . . . , f6) = (0, 1, 0, 1, 0, 0), (f ′
1, . . . , f ′
6) = (1, 0, 1, 0, 1, 1), and
(f ′′
1 , . . . , f ′′
6 ) = (0, 0, 0, 0, 0, 0) is a combinatorial ﬂattening of T . Equations (44) and (45)
give that
τ CS(T , t) = det

G(t) diag(ζ) + G′(t) diag(ζ ′) + G′′(t) diag(ζ ′′)

ζ ′
1ζ2ζ ′
3ζ4ζ ′
5ζ ′
6
=
det
⎛
⎜⎜⎜⎜⎜⎜⎝
ζ1t
ζ2t2
ζ3t
ζ4
0
ζ6t
ζ ′
1
ζ ′′
2 t + ζ ′
2t2 + ζ ′′
2 t3
0
ζ ′′
4 + ζ ′
4t + ζ ′′
4 t2
0
ζ ′
6t3
ζ ′′
1
ζ ′
2t
ζ ′
3t
0
ζ ′
5
ζ ′′
6 t
ζ ′′
1 t2
0
ζ ′
3t2
ζ ′
4t2
ζ ′
5t3
ζ ′′
6 t3
ζ ′
1t2
0
ζ ′′
3 + ζ3t + ζ ′′
3 t2
0
ζ ′′
5 + ζ5t + ζ ′′
5 t2
ζ ′
6
ζ1t2
ζ2t2
0
ζ4t2
ζ5t2
ζ6t2
⎞
⎟⎟⎟⎟⎟⎟⎠
ζ ′
1ζ2ζ ′
3ζ4ζ ′
5ζ ′
6
Substituting the solution for the complete structure into the above, we obtain
τ CS(T , t) = (t −1)t8
44 −15ξ −15ξ2 + 34ξ3 −19ξ5
+ (t + t−1)(−31 + 7ξ + 7ξ2 −10ξ3 + 3ξ5)
+ (t2 + t−2)(15 −3ξ −3ξ2 + 2ξ3 + ξ5) −5(t3 + t−3) + (t4 + t−4)

≈t4(−1.000 + 6.000t −12.805t2 + 33.472t3 −85.242t4
+ 85.242t5 −33.472t6 + 12.805t7 −6.000t8 + 1.000t9).
up to multiplication by a monomial ±tr for some integer r, hence
τ CS
λ (T ) = ±(4 −7ξ −7ξ2 + 18ξ3 −11ξ5) ≈±15.8506 .
Acknowledgements
The ﬁrst author wishes to thank Nathan Dunﬁeld for enlightening conversations and for sharing his drawing program of
the triangulated cusp of an ideal triangulation. The second author was supported by Basic Science Research Program
through the NRF of Korea funded by the Ministry of Education (2020R1A6A3A03037901).
Funding Information
Open Access funding enabled and organized by Projekt DEAL.
Author details
1International Center for Mathematics, Department of Mathematics, Southern University of Science and Technology,
Shenzhen, China, 2Max Planck Institute for Mathematics, Bonn, Germany.
Received: 22 December 2022 Accepted: 29 July 2023 Published online: 5 September 2023
