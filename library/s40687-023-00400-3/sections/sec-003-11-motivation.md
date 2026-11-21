---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-003-11-motivation
section_title: "Motivation"
section_number: 1.1
pages: 1-3
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Torsion and its twisted version . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.3
Neumann–Zagier matrices and their twisted version . . . . . . . . . . . . . . . .
4
1.4
The 1-loop invariant and its twisted version . . . . . . . . . . . . . . . . . . . . .
7
2
Proofs: twisted NZ matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3
Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.1
The knot 41 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.2
The knot 63 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4
Proofs: twisted 1-loop invariant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
5
Examples, continued . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
5.1
The knot 41 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
5.2
The knot 63 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
References
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
1 Introduction
1.1 Motivation
Ideal triangulations of 3-manifolds with torus boundary components were introduced
by Thurston [26] as a convenient way to describe and eﬀectively compute [2] complete
123
© The Author(s) 2023. This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other
third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view
a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
0123456789().,–: volV
37
Page 2 of 23
hyperbolic structures on 3-manifolds. To do so, one assigns a complex number diﬀerent
from 0 or 1 to each tetrahedron and a polynomial equation around each edge of the
triangulation. These so-called gluing equations have special shape that can be described
by two matrices A and B (with rows and columns indexed by the edges and by the
tetrahedra, respectively) whose entries describe the number of times (but not the order by
which) tetrahedra wind around an edge. One of the main discoveries of Neumann–Zagier
is that the matrix (A|B) becomes, after some minor modiﬁcations, the upper part of a
symplectic matrix with integer entries [22]. The symplectic property of the NZ matrices
and of the corresponding gluing equations deﬁne a linear symplectic structure on a vector
space whose quantization leads to a plethora of quantum invariants that include the
loop invariants of Dimofte and the ﬁrst author [6,8], the 3D-index in both the original
formulation of Dimofte-Gaiotto-Gukov [9,10] as well as the state-integral formulation of
Kashaev and the ﬁrst author [13] and Kashaev–Luo–Vartanov state-integral [1,20]. All of
those invariants are deﬁned using the NZ matrices of a suitable ideal triangulation, and
their topological invariance follows by proving that they are unchanged under Pachner
2–3 moves.
Our original motivation was to study the behavior of the loop invariants of [6] under
cyclic covers. Since the latter are deﬁned in terms of NZ data of an ideal triangulation,
we were led to study the behavior of the NZ matrices under cyclic covers. By elementary
topology, each tetrahedron of an ideal triangulation lifts to n tetrahedra in the n-fold
cyclic cover, and lifting all the way to the inﬁnite cyclic cover leads to the notion of
NZ matrices which we can call equivariant or twisted (as is common in algebraic and
geometric topology) or t-deformed (as is common in physics). We will use the term
“twisted”, and keep in mind that the variable t below encodes topological information of
cyclic covers.
Said diﬀerently, as the triangulation of the cyclic cover unfolds, so do its edges and the
tetrahedra that wind around them. This is the content of the twisted NZ matrices. How
can this elementary idea be non-trivial or interesting?
It turns out that the twisted NZ matrices have twisted symplectic properties which come
from topology and using them one can give twisted versions of the above mentioned
invariants, i.e., of the loop invariants [6,8], the 3D-index in [9,10] and [13] and KLV
state-integral [1,20]. A key property of such a twisted invariant is that it determines the
corresponding (untwisted) invariant of all cyclic covers. For example, the twisted 1-loop
invariant of a knot complement deﬁned below satisﬁes this property.
Our goal is to deﬁne the twisted NZ matrices, describe their properties and show how
to compute them in terms of the methods developed by SnapPy [2]. Having done so, we
can use the twisted NZ matrices to deﬁne a twisted version of the 1-loop invariant, prove
its topological invariance and conjecture that it equals to the adjoint twisted Alexander
polynomial. It is interesting to note that the twisted 1-loop invariant depends only on
the combinatorics of the NZ matrices of the inﬁnite cyclic cover (which is abelian infor-
mation), whereas the adjoint twisted Alexander polynomial depends on the complete
hyperbolic structure given as a representation of the fundamental group.
The twisted NZ matrices introduced in this paper have further applications aside from
the topological 1-loop polynomial invariants studied in the present paper. In the sequel
paper [16], we use the twisted NZ matrices to study the behavior of the higher-loop
invariants of [6] under cyclic coverings. The latter were recently shown to be topological
invariants of cusped hyperbolic 3-manifolds [14]. A further application of twisted NZ
matrices was given in our joint work [17] where we introduced a super-version of them
to deﬁne 1-loop torsion polynomials for all representations of sl2(C) that we conjectured
to be equal to their corresponding twisted Alexander polynomials. This conjecture was
recently proven for all ﬁbered 3-manifolds [15].
