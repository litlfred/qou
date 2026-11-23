---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-000-1-the-skein-models
section_title: "The skein models."
section_number: 1
pages: 3-4
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
The skein models.
The skein theory model of Hn is based on the framed Homﬂy skein relations,
in their simplest form
−
=
(s −s−1)
and
=
v−1
.
The Homﬂy skein S(F) of a planar surface F, with some designated input
and output boundary points, is deﬁned as linear combinations of oriented
tangles in F, modulo these two local relations, and Reidemeister moves II
and III. The coeﬃcient ring can be taken as Λ = Z[v±1, s±1] with powers of
sk −s−k in the denominators.
Every skein admits a mirror map,
: S(F) →S(F) induced by switching
all crossings in a tangle, coupled with inverting v and s in Λ.
Write Rn
n(v, s) for the skein S(F) of n-tangles, where F is a rectangle
with n inputs at the bottom and n outputs at the top. Composing n-tangles
induces a product which makes Rn
n(v, s) into an algebra. It has a linear basis
of n! elements, and is isomorphic to the Hecke algebra Hn(z). This algebra
has a presentation with generators {σi}, i = 1, . . . , n −1 satisfying the braid
relations
σiσj
=
σjσi,
|i −j| > 1,
σiσi+1σi
=
σi+1σiσi+1,
and the quadratic relations σ2
i = zσi + 1.
In Rn
n the generators are the elementary braids
σi =
i i+1
3
and the parameter z is s−s−1, giving the alternative form (σi−s)(σi+s−1) = 0
for the quadratic relations.
In the special case z = 0 the Hecke algebra reduces to C[Sn], with σi
becoming the transposition (i i + 1). For general i, j we can view the trans-
position (i j) diagrammatically
(i j) =
i
j
.
The corresponding positive permutation braid
ω(i j) =
i
j
with all crossings positive realises this transposition, as in [13]. Regarded via
Rn
n as an element of Hn(z), it becomes the transposition (i j) when we set
z = 0.
Deﬁnition. The Murphy operator M(j) ∈Rn
n, j = 2, . . . , n is deﬁned as
M(j) =
j−1
X
i=1
ω(i j).
These elements certainly project to the Jucys-Murphy elements m(j) in
C[Sn]. With a bit of algebraic work they can be shown to commute, and
their sum
M =
n
X
j=2
M(j)
=
X
i<j
ω(i j)
can be shown to lie in the centre of Rn
n. These facts are immediately obvious
from the skein representatives T(j) and T (n), discussed shortly.
