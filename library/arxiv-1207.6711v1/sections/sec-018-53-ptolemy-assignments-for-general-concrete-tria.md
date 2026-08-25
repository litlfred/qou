---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-018-53-ptolemy-assignments-for-general-concrete-tria
section_title: "Ptolemy assignments for general concrete triangulations"
section_number: 5.3
pages: 16-17
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
triangulations the Ptolemy coordinates on faces of diﬀerent simplices must be identiﬁed by
signs given by the face pairing permutations.
Deﬁnition 5.9. A Ptolemy assignment on (M,T ) is a Ptolemy assignment for each simplex
ofT such that Ptolemy coordinates on identiﬁed faces are identiﬁed via the pullback of the
permutation matrix. More precisely, if f0⊂ ∆0 is paired with f1⊂ ∆1 via the permutation
σ, we require that
(5.9) ( σ∗c∆1)t0 = (c∆0)t0
for each t0∈ ∆3
n on face f0. Equivalently, we require that ( c∆0)t0 = det(Iσ,σ(t0))(c∆1)σ(t0).
The variety of Ptolemy assignments is denoted by Pn(T ).
0
21
3
0
21
3
+
_
_
__
+
+
+
+
_
_ +
∆0 ∆1
t0=0031
t1=0103
Figure 11. Identiﬁcation of Ptolemy coordinates.
Note that if T is an ordered triangulation, all face pairings are order preserving, so all
signs are positive, and the deﬁnition agrees with Deﬁnition 5.1.
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 17
Lemma 5.10. LetT′ be the triangulation obtained fromT by reordering the vertices of ∆i
by a permutation σi. Then{σ∗
ic∆i} is a Ptolemy cochain on T′.
Proof. We must prove that the coordinates on identiﬁed faces are identiﬁed via the pullback.
Letc∆′
i =σ∗
ic∆i. Suppose fi⊂ ∆i is glued tofj⊂ ∆j by a permutationτ. The corresponding
face pairing involving ∆′
i and ∆′
j is thenτ′ =σ−1
j τσi. Since τ∗c∆j agrees withc∆i on facef0,
it follows from the standard pullback properties that τ′∗c∆′
j and c∆′
i also agree on f0. This
proves the result. □
Corollary 5.11. Up to canonical isomorphism, the Ptolemy variety only depends on the
abstract triangulation. □
