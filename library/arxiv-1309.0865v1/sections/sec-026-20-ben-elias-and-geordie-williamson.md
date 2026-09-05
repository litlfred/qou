---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-026-20-ben-elias-and-geordie-williamson
section_title: "BEN ELIAS AND GEORDIE WILLIAMSON"
section_number: 20
pages: 20-22
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
described soon) in the following matrix:
A =


2 −1 0 0 −q−1
−1 2 −1 0 0
0 −1 2 −1 0
0 0 −1 2 −q
−q 0 0 −q−1 2


.
(More precisely , this is the example when n = 4 .) This gives a realization of
W . Specializingq to an element of C \ R, one obtains a realization ofW over C
which can not be obtained by extension of scalars from a reali zation deﬁned
over R.
Given a realization (h, {α∨
s }, {αs}) of (W,S ) over k we can consider its Cartan ma-
trix (⟨α∨
s,α t⟩)s,t∈S. Clearly a realization is symmetric if and only if its Cartan matrix
is. Conversely , given a matrix (ast)s,t∈S such that ass = 2 , one can construct the free
k-module h = ⨁
s∈S kα∨
s , and deﬁne αs ∈ h∗ by ⟨α∨
s,α t⟩ = ast. When this yields a
realization of (W,S ) we call the matrix (ast) a Cartan matrix for (W,S ) over k. Any re-
alization for which {α∨
s } is a basis for h can be reconstructed from its Cartan matrix;
we call such realizations minimal.
Example 3.3. In Example 3.2 the realizations discussed in (1), (5) and (6) are minimal.
The example in (3) is minimal if and only if the root system is s imply connected and
of adjoint type (so that root lattice coincides with h). Examples (2) and (4) are not
minimal in general.
Remark 3.4. We expect that there is a rich Koszul duality theory for categ ories ob-
tained from Soergel bimodules for arbitrary Coxeter system s (generalizing Soergel’s
description [Soe90] of the algebra of category O in the case of Weyl groups). Here
one expects Koszul duality to exchange h and h∗, roots and coroots. In this setting
it seems natural to require both {α∨
s } ⊂ h and {αs} ⊂ h∗ to be linearly independent.
This explains in part why we do not assume that our realizatio ns are minimal.
It is natural to ask under which conditions a matrix (ast)s,t∈S with ass = 2 is a
Cartan matrix of (W,S ). A thorough discussion of this can be found in the appendix
to [Elib]. We provide a short discussion here.
Deﬁnition 3.5. Deﬁne the 2-colored quantum numbers [k]x and [k]y inside the ring
Z[x,y ] inductively . One has [0]x = [0] y = 0, [1]x = [1] y = 1, and [2]x =x, [2]y =y. The
other 2-colored quantum numbers are deﬁned by the rules
(3.2a) [2]x[k]y = [k + 1]x + [k − 1]x,
(3.2b) [2]y[k]x = [k + 1]y + [k − 1]y.
Whenk is odd, [k]x = [k]y and we shorten the notation to [k].
SOERGEL CALCULUS 21
Fix a pair s,t ∈ S and let x = ast andy = ats. The condition that (st) has order
exactly k is an algebraic condition on x and y. For instance, when αs and αt are
linearly independent, the action of (st) on their span has order k when [2k + 1] = 1
and [2k]x = [2k]y = 0 . In fact, this implies further that 2[k]x = 2[k]y = [2] x[k]y =
[2]y[k]x = 0. This suggests that one should set
(3.3) [mst]x = [mst]y = 0.
This is the technical condition mentioned in Deﬁnition 3.1. While (3.3) is sufﬁcient
to imply that (st) has order dividing k on the span of the roots, it is independent
of the condition that W acts on h. The reason that (3.3) is required is to ensure that
2-colored Jones-Wenzl projectors are rotation-invariant, as discussed in section 5.2.
If eitherx ory is a non-zero-divisor, then (3.3) is equivalent to the statement thatxy
satisﬁes the minimal polynomial of the algebraic integer 4 cos2( π
m). If this algebraic
integer does not exist in k then (W,S ) does not admit a realization over k. Any Cox-
eter system (of ﬁnite rank) admits a realization over some ri ng of integers. Finally ,
we introduce one other technical condition.
Deﬁnition 3.6. We call a realization balanced if for every s,t ∈S one has [mst − 1]x =
[mst − 1]y = 1 . We reﬁne this notion by calling the realization even-balanced (resp.
odd-balanced) if this property holds when mst is even (resp. odd). The opposite of
even-balanced is even-unbalanced.
The familiar Cartan matrices of Weyl groups are balanced. Ho wever, the Cartan
matrix of type A2 is not balanced when viewed as a realization of G2. The exotic
Cartan matrices for type ˜An, n ≥ 3 given in Example (6) above are not balanced,
except whenq = 1. Being balanced is equivalent to the existence of an unambig uous
notion of positive roots in h∗; when the realization is symmetric, being balanced is
similar to the condition that simple roots form an obtuse ang le. Faithful realizations
are almost always even-balanced; any minimal even-unbalan ced realization over a
domain is not faithful. Once again, a thorough discussion of these technicalities can
be found in [Elib].
Fix a realization (h, {α∨
s }, {αs}) of (W,S ) and let
R =
⨁
m≥0
Sm(h∗)
denote the symmetric algebra on h∗, which we view as a graded k-algebra with
deg h∗ = 2 . Then W acts on h∗ via the contragredient representation ( s(γ) = γ −
⟨α∨
s,γ ⟩α for allγ ∈ h∗) and this extends to an action of W on the algebraR by graded
automorphisms. We think of R as the polynomial functions on h.
We let R − Mod and R − Bim denote the category of graded R-modules and bi-
modules respectively . We viewR − Mod andR − Bim as graded categories; that is,
as categories enriched in graded k-modules. We denote the grading shift by (1): if
M = ⨁ M i is a graded (bi)module then M(1)i = M i+1. Degree 0 maps of (graded)
R-(bi)modules will be denoted by Hom0(M,N ).
