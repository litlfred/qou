---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-001-3-cocycles
section_title: "Cocycles"
section_number: 3
pages: 6-9
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
We will describe how to compute a representation 2 π1(T ) → PGL2(C) from an assign-
ment of parameters νe as in Theorem 2.3 using cocycles inspired by [GGZ15, Section 9]
as follows:
Deﬁnition 3.1. Let G be a group andX be a space with a polyhedral decomposition. A
G -cocycle on X is an assignment of elements inG to the oriented edges of X such that
the product around each face is the identity and such that reversing the orientation of
an edge replaces the labeling by its inverse.
All cocycles in this section are PGL2(C)-cocycles.
Given a matrix G fulﬁlling the conditions in Lemma 2.2, we will construct a cocycle on
the doubly truncated simplex ∆ coming from a simplex ∆, see Figure 2. We index a ver-
tex v of ∆ by the permutation σ ∈ S4 such that the vertex of ∆ closest to v is σ(0), the
2For consistency on how arrows in a category compose, the loop traversing the loop a ﬁrst and the
loop b second is denoted by ba in π1(T ).
7
0
1
2
3
jx
z
y
i
1
0
1
2
3
j
H2
H3
γ012 γ013
action by γ012
action by γ013
∆ in (0,1,2,3)-standard position ∆ in (0,1,3,2)-standard position
Figure 4. A simplex in different standard positions.
edge of ∆ closest to v is σ(0)σ(1), and the face of ∆ closest to v is σ(0)σ(1)σ(2). We la-
bel an oriented long, middle, or short edge of ∆ by ασ(0)σ(1)σ(2), βσ(0)σ(1)σ(2), respectively
γσ(0)σ(1)σ(2) if it starts at the vertex indexed byσ. Let us introduce the notion of standard
position to deﬁne the PGL 2(C)-matrices assigned to these edges.
We think of the upper half space model of hyperbolic 3-space as a subset H3 = {w =
z + t  : t > 0} of the quaternions. Recall that Isom +(H3) ∼= PGL2(C) ∼= PSL2(C) where the
action of a SL2(C)-matrix on H3 is given by
( a b
c d
)
7→
(
w 7→ (aw + b) · (cw + d)−1)
.
Deﬁnition 3.2. We say that a positively oriented, ﬁnite simplex ∆ is in σ-standard
position where σ ∈ S4 if vertex
• σ(0) is at ,
• σ(1) at t  with t > 1,
• σ(2) at a + t  with a > 0 and
• σ(3) at z + t  with Im(z) > 0 if σ is even and Im(z) < 0 otherwise.
An example of this is shown in Figure 4. Geometrically, the motivation for this deﬁnition
is that two faces of two (not necessarily distinct) simplices line up inH3 if the respective
edge lengths match and the two simplices are in the respective standard positions. More
precisely, let f1 ∈ {0,1,2,3} be a face of the simplex ∆1 and f2 ∈ {0,1,2,3} of ∆2. Let σ ∈
S4 \ A4 with σ(f1) = f2 be a pairing of the two faces. If the edge lengths match under
this pairing, then the faces match if each ∆k is in σk-standard position where σ1 is any
permutation with σ1(3) = f1 and σ2 = σ ◦ σ1.
8
This deﬁnition also gives us a cocycle as follows (also see Figure 4):
Deﬁnition 3.3. Consider the isometry class of a ﬁnite simplex ∆. Given an oriented
edge e of ∆, let σ and σ′ be the permutations that index the vertex where e starts and,
respectively, ends. The natural cocycle on∆ is the cocycle assigning to each edgee the
PGL2(C)-matrix taking ∆ from σ-standard position to σ′-standard position.
Note that we can identify Euclidean 3-vector space isometrically with the tangent space
of a point inH3 such that the tangents corresponding to thex-, y-, and z-axis are parallel
to the real line, the imaginary line, respectively, the line t  (see Figure 4). Thus, we can
associate a SO3-matrix to an element in Isom+(H3) ﬁxing a (ﬁnite) point of H3. Let
Rω =


cos ω −sin ω 0
sin ω cos ω 0
0 0 1


be the rotation about the z-axis by the angle ω.
Lemma 3.4. The natural cocycle on ∆ can be computed from the vertex Gram matrix
G as follows (apply even permutations σ ∈ A4 to obtain labels for all edges):
α120 = α210 = α123 = α213 =
(
0
√
v 2
12 − 1 − v12
1 0
)
,
β123 = β132 =
( −cos(η1,32/2) sin( η1,32/2)
sin(η1,32/2) cos( η1,32/2)
)
,
γ123 =
(
γ120)−1
= γ210 = (γ213)−1 =
( exp(ıθ03) 0
0 1
)
.
Note that β123 and γ123 ﬁx the point  ∈ H3 and the associated SO3-matrices are:


−cos η1,32 0 sin η1,32
0 −1 0
sin η1,32 0 cos η1,32

 and Rθ03.
Proof. α120 is an involution exchanging the points  and exp(l12) . The associated CP 1-
automorphism is of the form z 7→ x/z and exchanges 1 and exp( l12). An elementary
calculation gives the value for x.
Consider the hyperbolic plane H2 = {x + t  : x ∈ R, t > 0} ⊂ H3. β123 is the composition
of the rotation of H2 about  by η1,32 with the involution ﬁxing the line t  pointwise.
We obtain the PSL 2(R)-matrix for the rotation of H2 by conjugating the rotation of the
unit disk by η1,32 with the matrix taking the upper half plane model to the Poincare disk
model of hyperbolic 2-space:
( ı 1
1 ı
)−1
·
( exp(ıη1,32/2) 0
0 exp( −ıη1,32/2)
)
·
( ı 1
1 ı
)
9
Given an oriented triangulation T , let T be the complex obtained by replacing each
simplex ∆ by the double truncated simplex ∆. The long and short edges of T about
an edge e of T form a prism, see Figure 3. Given an assignment of edge parameters
νe for T , this prism about an edge e ∈ E(T ) is a cocycle if and only if the short edges
compose to the identity, which is equivalent to Θe being a multiple of 2π. Let ˆT denote
the complex T ∪ Prisms.
Theorem 3.5. Consider an assignment of a parameter νe < −1 to each edge of an ori-
ented, ﬁnite triangulation T .
(a) If each matrix G∆ is realized, we obtain a natural cocycle on T and, thus, a rep-
resentation π1(T ) → PGL2(C) (up to conjugation, unless we pick a vertex of T
as basepoint).
(b) If, furthermore, Θe is a multiple of 2π for every e ∈ E(T ), the cocycle extends to
ˆT and, thus, yields a representation of π1(T ) → PGL2(C).
(c) If, furthermore, Θe = 2π for every e ∈ E(T ), the representation is giving a hyper-
bolic structure on T .
Proof. Note that α and β in Lemma 3.4 are involutions and only involve the parameters
vi j on the edges of the triangle containing the respective α and β. Hence, the matri-
ces on two big hexagons on two doubly-truncated simplices are compatible and the
hexagons can be identiﬁed if the edge parameters on the respective triangles of the cor-
responding tetrahedra match. This proves (a).
(b) follows from the above comment about the prisms being cocycles and the fact that
ˆT differs from T only by a set of 3-balls which do not change π1.
(c) is just restating Theorem 2.3.
