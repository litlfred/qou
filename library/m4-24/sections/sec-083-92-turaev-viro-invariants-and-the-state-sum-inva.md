---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-083-92-turaev-viro-invariants-and-the-state-sum-inva
section_title: "Turaev-Viro invariants and the state-sum invariants de-"
section_number: 9.2
pages: 136-139
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
rived from monoidal categories
A state-sum invariant of 3-manifolds is de
ned by using such a set of 6j-symbols
with a monoidal categoryfVigi2I , as follows. Choose a simplicial decomposition
of a closed 3-manifold M , and 
x a total order of its vertices, which induces
30 To be precise, the even part of the subfactor of type D2n is braided, and its S -matrix is
non-degenerate.
31 This is trivially braided.
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 509
subfactor monoidal S-matrixcategory
WZW model subfactors of level k =1; 2; braided non-degenerateSU (N)k, SO(N)k, Sp(N)k,
subfactors of type An (=SU (2)n) braided non-degenerate
index< 4 type D2n braided30 non-degenerate30
type E6;E 8 not braided none
subfactors of (generalized) Haagerup, not braided noneindex> 4: Asaeda-Haagerup,
exotic subfactors, quantum doubles of braided non-degenerate Haagerup subfactor,
subfactors 3-cocycles of 
nite groups not braided none
from | representations of 
nite groups braided31 degenerate
Table 6: Subfactors, their monoidal categories, and S-matrices
orientations of edges. Further, choose an edge coloring , which is a map of
the set of edges to I ,a n dc h o o s eaface coloring’, which is a collection of such
assignments that a basis vector of Hk
i;j is assigned to a triangle
with an edge coloring. To a tetrahedron  with an edge coloring  and a face
coloring ’, we associate the above mentioned 6 j-symbol, which we denote by
W (;;’). Then, a state-sum invariant of M is de
ned by
Z(M)= w−vX

Y
E
(E)
X
’
Y

W (;;’); (48)
where the sums of  and ’run over all edge colorings and all face colorings,
and the products of E and  run over all edges and all tetrahedra of the
simplicial decomposition of M ,a n di is a constant, which corresponds to a
\quantum dimension", and w =P
i2I 2
i ,a n d v is the number of vertices of
the simplicial decomposition. It is known (see [41], [118, Chapter 12]) that the
invariant (48) is a topological invariant of M . The de
nition of the invariant
(48) can naturally be extended to an invariant of 3-manifolds with boundaries,
and a TQFT can be formulated based on it.
In particular, for the set of 6j-symbols arising from representations of the quan-
tum groupUq(Sl2) at a root of unity, the invariant (48) is calledthe Turaev-Viro
invariant [392]. In its de
nition it is not necessary to introduce face colorings
(because Nk
i;j i sa l w a y se q u a lt o0o r1f o ra n yi;j;k in this case) and orienta-
tions of edges (because each representation of Uq(sl2) is self-dual).
Geometry &TopologyMonographs, Volume 4 (2002)
510 T. Ohtsuki (Editor)
The monoidal category of a set of quantum 6 j-symbols is a modular category,
and we can construct the Reshetikhin-Turaev invariant from it (see Section 9.3).
The square of the absolute value of the invariant is equal to the value of the
state-sum invariant derived from these 6j-symbols.
The state-sum invariant derived from the set of 6j-symbols given by a 3-cocycle

 of a 
nite group G is called the Dijkgraaf-Witten invariant [108]. In particu-
lar, when
 = 1, it is equal to the number of conjugacy classes of representations
1(M)!G. It is further equal to the state-sum invariant derived from the set
of 6j-symbols obtained from the representations of the 
nite group G.
When a set of 6 j-symbols arises from a subfactor, the state-sum invariant
derived from these 6 j-symbols is called the Turaev-Viro-Ocneanu invariant.
There are in
nitely many subfactors other than the above cases as shown in
Table 6. The Turaev-Viro-Ocneanu invariants derived from such subfactors
might be new invariants of 3-manifolds.
Problem 9.2 (Y. Kawahigashi) Suppose we have a three-dimensional TQFT.
Can we determine whether it arises from a fusion rule algebra and 6j-symbols?
If yes, can we describe all fusion rule algebras with 6j-symbols producing the
TQFT?
Remark (Y. Kawahigashi) By a result of Ocneanu, we have at most only

nitely many such fusion rule algebras with 6 j-symbols, up to equivalence of
6j-symbols.
Problem 9.3 (Y. Kawahigashi) Suppose we have two fusion rule algebras
with 6j-symbols and that two TQFT’s arising from them are isomorphic. What
relation do we have for the two sets of 6j-symbols?
Remark (Y. Kawahigashi) Are they equivalent in the sense of [362]?
Problem 9.4 (Y. Kawahigashi) Suppose we have a TQFT arising from a
fusion rule algebra with 6j-symbols. Using a fusion rule subalgebra and 6j-
symbols restricted on it, we can construct another TQFT. What relation do we
have for these TQFT’s?
Remark (Y. Kawahigashi) How about the case where the fusion rule subal-
gebra arises from 
-induction? The 
-induction produces a fusion rule algebra
with 6j-symbols from a semisimple ribbon category with 
nitely many isomor-
phism classes of simple objects and a speci
c choice of an object satisfying
certain axioms. See [62], [222] and their references. If the original ribbon cat-
egory is modular, we have some answer in [62], so it is particularly interesting
when the S-matrix is not invertible.
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 511
