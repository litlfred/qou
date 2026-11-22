---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution"
section_id: sec-001-front-matter-page-2
section_title: "Front matter (page 2)"
section_number: null
pages: 2-2
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
toc_source: inferred
doc_brief: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution — We establish a relation between the coeﬃcients of asymptotic expansion of the trivial"
---
Introduction
Witten’s invariant of 3d manifolds deﬁned in [1] by a path integral over the SU(2) connections
Aµ on a 3d manifold M
Z(M; k) =
Z
[DAµ]e
ik
2π SCS[Aµ],
(1.1)
SCS = 1
2 Tr ǫµνρ
Z
M d3x

Aµ∂νAρ + 2
3AµAνAρ

(1.2)
(k ∈ZZ, Tr is the trace taken in the fundamental representation of SU(2)) can also be
calculated combinatorially with the help of the surgery formula. Let M be a 3d manifold
constructed by (pj, 1) surgeries on the components Lj of an N-component link L in S3. A
(p, 1) surgery means that the meridian of the tubular neighborhood is glued to the parallel
plus p meridians on the boundary of the knot complement (in other words, a Dehn’s surgery
is performed on a knot with framing number p). The invariant of M can be expressed in
terms of the framing independent colored Jones polynomial Jα1,...,αN(L; k) of the link L:
Z(M; k)
Z(S3; k) =
 2
K
 N
2 exp

3
4πi
 2
K −1
 N
X
j=1
sign (pj)


(1.3)
×
X
0≤αj ≤K−1
(1≤j≤N)
Jα1,...,αN(L; k) exp

iπ
2K
N
X
j=1
pj(α2
j −1)


N
Y
j=1
sin
 π
K αj

,
Z(S3; k) =
s
2
K sin π
K ,
K = k + 2.
(1.4)
The Jones polynomial Jα1,...,αN(L; k) is normalized in such a way that it is multiplicative for
unlinked links and J(empty link; k) = 1, Jα(unknot; k) =
sin( π
K α)
sin( π
K) .
Although N. Reshetikhin and V. Turaev proved [2] that eq. (1.3) indeed deﬁnes an in-
variant of M (i.e. the l.h.s. of eq. (1.3) is invariant under Kirby moves), the topological
origin of this invariant remains somewhat obscure. The question is: which of the “classical”
topological invariants of M are contained inside Z(M; k)? Two distinct approaches to this
problem have been tried. The ﬁrst one is to study Z(M; k) for some particular values of
K. R. Kirby and P. Melvin discovered [3] that if K is odd, then Z(M; k) is proportional to
1
