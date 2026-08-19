---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-002-12-torsion-and-its-twisted-version
section_title: "Torsion and its twisted version"
section_number: 1.2
pages: 1-3
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
1.3. Neumann–Zagier matrices and their twisted version 3
1.4. The 1-loop invariant and its twisted version 7
2. Proofs: twisted NZ matrices 8
3. Examples 12
3.1. The knot 4 1 12
3.2. The knot 6 3 14
4. Proofs: twisted 1-loop invariant 16
5. Examples, continued 21
5.1. The knot 4 1 21
5.2. The knot 6 3 21
Acknowledgments 22
References 22
1. Introduction
1.1. Motivation. Ideal triangulations of 3-manifolds with torus boundary components were
introduced by Thurston [Thu77] as a convenient way to describe and eﬀectively compute [CDW]
Date: 30 August 2021.
Key words and phrases. Torsion, 1-loop invariant, adjoint Reidemeister torsion, inﬁnite cyclic cover,
twisted Alexander polynomial, ideal triangulations, knots, hyperbolic 3-manifolds, Neumann–Zagier ma-
trices, twisted Neumann–Zagier matrices, block circulant matrices.
1
arXiv:2109.00379v1  [math.GT]  1 Sep 2021
2 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
complete hyperbolic structures on 3-manifolds. To do so, one assigns a complex number dif-
ferent from 0 or 1 to each tetrahedron and a polynomial equation around each edge of the
triangulation. These so-called gluing equations have special shape that can be described by
two matrices A and B (with rows and columns indexed by the edges and by the tetrahedra,
respectively) whose entries describe the number of times (butnot the order by which) tetrahe-
dra wind around an edge. One of the main discoveries of Neumann–Zagier is that the matrix
(A|B) becomes, after some minor modiﬁcations, the upper part of a symplectic matrix with
integer entries [NZ85]. The symplectic property of the NZ matrices and of the corresponding
gluing equations deﬁne a linear symplectic structure on a vector space whose quantization
leads to a plethora of quantum invariants that include the loop invariants of Dimofte and
the ﬁrst author [DG13, DG18], the 3D-index in both the original formulation of Dimofte-
Gaiotto-Gukov [DGG14, DGG13] as well as the state-integral formulation of Kashaev and
the ﬁrst author [GK19] and Kashaev–Luo–Vartanov state-integral [KLV16, AGK]. All of
those invariants are deﬁned using the NZ matrices of a suitable ideal triangulation, and their
topological invariance follows by proving that they are unchanged under Pachner 2–3 moves.
Our original motivation was to study the behavior of the loop invariants of [DG13] under
cyclic covers. Since the latter are deﬁned in terms of NZ data of an ideal triangulation,
we were led to study the behavior of the NZ matrices under cyclic covers. By elementary
topology, each tetrahedron of an ideal triangulation lifts to n tetrahedra in the n-fold cyclic
cover, and lifting all the way to the inﬁnite cyclic cover leads to the notion of NZ matrices
which we can call equivariant or twisted (as is common in algebraic and geometric topology)
ort-deformed (as is common in physics). We will use the term “twisted”, and keep in mind
that the variable t below encodes topological information of cyclic covers.
Said diﬀerently, as the triangulation of the cyclic cover unfolds, so do its edges and the
tetrahedra that wind around them. This is the content of the twisted NZ matrices. How
can this elementary idea be nontrivial or interesting?
It turns out that the twisted NZ matrices have twisted symplectic properties which come
from topology and using them one can give twisted versions of the above mentioned invari-
ants, i.e., of the loop invariants [DG13, DG18], the 3D-index in [DGG14, DGG13] and [GK19]
and KLV state-integral [KLV16, AGK]. A key property of such a twisted invariant is that
it determines the corresponding (untwisted) invariant of all cyclic covers. For example, the
twisted 1-loop invariant of a knot complement deﬁned below satisﬁes this property.
Our goal is to deﬁne the twisted NZ matrices, describe their properties and show how to
compute them in terms of the methods developed by SnapPy [CDW]. Having done so, we can
use the twisted NZ matrices to deﬁne a twisted version of the 1-loop invariant, prove its topo-
logical invariance and conjecture that it equals to the adjoint twisted Alexander polynomial.
It is interesting to note that the twisted 1-loop invariant depends only on the combinatorics
of the NZ matrices of the inﬁnite cyclic cover (which is abelian information) whereas the
adjoint twisted Alexander polynomial depends on the complete hyperbolic structure given
as a representation of the fundamental group.
Further applications of twisted NZ matrices will be given in forthcoming work.
1.2. Torsion and its twisted version. Before discussing twisting matters further, let us
recall a key motivating example. A basic invariant of a compact 3-manifold is the order of
TWISTED NEUMANN–ZAGIER MATRICES 3
the torsion of its ﬁrst homology. The behavior of this invariant for all cyclic covers of a
knot complement is determined by a single Laurent polynomial, the Alexander polynomial.
Explicitly, we have ⏐⏐tor(H1(M (n); Z ))
⏐⏐ =
∏
ωn=1
∆K(ω) (1)
where ∆K(t) ∈ Z [t±1] is the Alexander polynomial of a knot K ⊂ S3, M (n) is the n-
fold cyclic cover of M = S3\K, and the right-hand side is the order of the torsion part
of H1(M (n); Z ). This classical result connecting the torsion of the ﬁrst homology to the
Alexander polynomial (see e.g. [Fox56, (6.3), p.417]) is deeply rooted in the idea that
the Alexander polynomial is the torsion of the inﬁnite cyclic cover of M twisted by the
abelianization map α :π1(M)→H1(M; Z ) = Z . In other words, we have
The twisted torsion determines the torsion of the cyclic covers (2)
This idea has been extended in several directions. Among them, one can deﬁne the torsion
of a 3-manifold using interesting representations of its fundamental group. For example, when
M is a cusped hyperbolic 3-manifold, one can deﬁne a torsion using a (lifted) geometric
SL2(C )-representation ρ of its complement, or a symmetric power thereof. There are some
technical diﬃculties that one must overcome, stemming from the fact that sometimes the
corresponding chain complexes are not acyclic, hence the torsion depends on a choice of
peripheral curves, as well as normalization issues, since the torsion is usually well-deﬁned
up to a sign. These issues have been addressed in detail by [Por97, DY12, DFJ12]. Among
the several torsion invariants, we will be interested in the adjoint (Reidemeister) torsion
τγ(M) of a one-cusped hyperbolic 3-manifold (such as a knot complement) using the adjoint
representation Adρ = Sym2(ρ) :π1(M)→ SL3(C ), where γ is a ﬁxed peripheral curve. The
adjoint torsion τγ(M)∈F×/± is a nonzero element of the trace ﬁeld F of M, well-deﬁned
up to a sign [Por97]. Just as in the case of the Alexander polynomial, there is a version of
the adjoint twisted Alexander polynomial τ(M,α,t )∈F [t±1]/(±tZ ) (abbreviated by τ(M,t )
when α is clear) deﬁned in [Wad94, DFJ12, DY12] using an epimorphism α : π1(M)→ Z .
Here, the ambiguity is given by multiplication by an element of ±tZ :={±tr|r∈ Z }.
Two key properties of the adjoint twisted Alexander polynomial are the behavior under
ﬁnite cyclic covers [DY12]
τ(M (n),tn) =
∏
ωn=1
τ(M,ωt ) (3)
and the relation with the adjoint torsion [Yam08], namely
τ(M, 1) = 0, d
dt
⏐⏐⏐⏐
t=1
τ(M,t ) =τλ(M) (4)
where λ is the canonical longitude, i.e., the peripheral curve satisfying α(λ) = 0.
