---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-066-92-turaev-viro-invariants-and-the-state-sum-inva
section_title: "Turaev-Viro invariants and the state-sum invariants derived from monoidal categories"
section_number: 9.2
pages: 136-139
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
toc_source: inferred
---
rived from monoidal categories
A state-sum invariant of 3-manifolds is deﬁned by using such a set of 6j-symbols
with a monoidal category {Vi}i∈I , as follows. Choose a simplicial decomposition
of a closed 3-manifold M , and ﬁx a total order of its vertices, which induces
30 To be precise, the even part of the subfactor of type D2n is braided, and its S-matrix is
non-degenerate.
31 This is trivially braided.
Geometry & Topology Monographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds
509
subfactor
monoidal
S-matrix
category
WZW model subfactors of level k = 1, 2, · · ·
braided
non-degenerate
SU(N)k, SO(N)k, Sp(N)k, · · ·
subfactors of
type An (= SU(2)n)
braided
non-degenerate
index < 4
type D2n
braided30
non-degenerate30
type E6, E8
not braided
none
subfactors of
(generalized) Haagerup,
not braided
none
index > 4:
Asaeda-Haagerup, · · ·
exotic subfactors,
quantum doubles of
braided
non-degenerate
· · ·
Haagerup subfactor, · · ·
subfactors
3-cocycles of ﬁnite groups
not braided
none
from —
representations of ﬁnite groups
braided31
degenerate
Table 6: Subfactors, their monoidal categories, and S-matrices
orientations of edges. Further, choose an edge coloring λ, which is a map of
the set of edges to I , and choose a face coloring ϕ, which is a collection of such
assignments that a basis vector of Hk
i,j is assigned to a triangle
with an edge coloring. To a tetrahedron σ with an edge coloring λ and a face
coloring ϕ, we associate the above mentioned 6j-symbol, which we denote by
W(σ; λ, ϕ). Then, a state-sum invariant of M is deﬁned by
Z(M) = w−v X
λ
 Y
E
µλ(E)
 X
ϕ
Y
σ
W(σ; λ, ϕ),
(48)
where the sums of λ and ϕ run over all edge colorings and all face colorings,
and the products of E and σ run over all edges and all tetrahedra of the
simplicial decomposition of M , and µi is a constant, which corresponds to a
“quantum dimension”, and w = P
i∈I µ2
i , and v is the number of vertices of
the simplicial decomposition. It is known (see [41], [118, Chapter 12]) that the
invariant (48) is a topological invariant of M . The deﬁnition of the invariant
(48) can naturally be extended to an invariant of 3-manifolds with boundaries,
and a TQFT can be formulated based on it.
In particular, for the set of 6j-symbols arising from representations of the quan-
tum group Uq(Sl2) at a root of unity, the invariant (48) is called the Turaev-Viro
invariant [392]. In its deﬁnition it is not necessary to introduce face colorings
(because N k
i,j is always equal to 0 or 1 for any i, j, k in this case) and orienta-
tions of edges (because each representation of Uq(sl2) is self-dual).
Geometry & Topology Monographs, Volume 4 (2002)
510
T. Ohtsuki (Editor)
The monoidal category of a set of quantum 6j-symbols is a modular category,
and we can construct the Reshetikhin-Turaev invariant from it (see Section 9.3).
The square of the absolute value of the invariant is equal to the value of the
state-sum invariant derived from these 6j-symbols.
The state-sum invariant derived from the set of 6j-symbols given by a 3-cocycle
α of a ﬁnite group G is called the Dijkgraaf-Witten invariant [108]. In particu-
lar, when α = 1, it is equal to the number of conjugacy classes of representations
π1(M) →G. It is further equal to the state-sum invariant derived from the set
of 6j-symbols obtained from the representations of the ﬁnite group G.
When a set of 6j-symbols arises from a subfactor, the state-sum invariant
derived from these 6j-symbols is called the Turaev-Viro-Ocneanu invariant.
There are inﬁnitely many subfactors other than the above cases as shown in
Table 6.
The Turaev-Viro-Ocneanu invariants derived from such subfactors
might be new invariants of 3-manifolds.
Problem 9.2 (Y. Kawahigashi) Suppose we have a three-dimensional TQFT.
Can we determine whether it arises from a fusion rule algebra and 6j-symbols?
If yes, can we describe all fusion rule algebras with 6j-symbols producing the
TQFT?
Remark
(Y. Kawahigashi) By a result of Ocneanu, we have at most only
ﬁnitely many such fusion rule algebras with 6j-symbols, up to equivalence of
6j-symbols.
Problem 9.3
(Y. Kawahigashi) Suppose we have two fusion rule algebras
with 6j-symbols and that two TQFT’s arising from them are isomorphic. What
relation do we have for the two sets of 6j-symbols?
Remark (Y. Kawahigashi) Are they equivalent in the sense of [362]?
Problem 9.4
(Y. Kawahigashi) Suppose we have a TQFT arising from a
fusion rule algebra with 6j-symbols. Using a fusion rule subalgebra and 6j-
symbols restricted on it, we can construct another TQFT. What relation do we
have for these TQFT’s?
Remark (Y. Kawahigashi) How about the case where the fusion rule subal-
gebra arises from α-induction? The α-induction produces a fusion rule algebra
with 6j-symbols from a semisimple ribbon category with ﬁnitely many isomor-
phism classes of simple objects and a speciﬁc choice of an object satisfying
certain axioms. See [62], [222] and their references. If the original ribbon cat-
egory is modular, we have some answer in [62], so it is particularly interesting
when the S-matrix is not invertible.
Geometry & Topology Monographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds
511
9.3
