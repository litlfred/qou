---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-006-the-observables-of-two-dimensional-yang-mills-th
section_title: "The Observables of Two-dimensional Yang-Mills Theory"
section_number: null
pages: 9-10
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
---
Two-dimensional Yang-Mills theory is invariant under area-preserving diffeomorphisms [23]
and therefore has no local observables. It is a prototypical example of an area dependent
quantum field theory [24], which is a mild generalization of a topological quantum field theory.
The observables of two-dimensional Yang-Mills theory are Wilson loops on the one hand and
on the other hand partition functions on Riemann surfaces with boundaries with prescribed
holonomies. From the point of view of topological field theories, the former corresponds to line
defects and the latter to insertions of local operators. Indeed, the boundary holonomies are
indexed by conjugacy classes of the unitary group. In a topological setting, one can proceed
to shrink the boundaries down to singular points characterized by corresponding insertions of
conjugacy classes of the unitary group. The situation is akin to the treatment of closed string
vertex operators on the world-sheet in string theory. We will adopt this same point of view
here, and treat the partition functions of Yang-Mills with boundaries as correlators of local
insertions.8 In this paper, we focus on this class of observables. We remark on Wilson loops
in section 5.5.
The correlators of pure Yang-Mills theory with gauge group U(N) and coupling constant
gYM on a Riemann surface of genus G and area A read – see e.g. [25] for a pedagogical
derivation – :
Z[MG,Ui] =
X
λ∈YN
 kY
i=1
sλ(Ui)
!
(dimWλ
N)2−2G−k exp

−g2
YMA
2N c2(λ)

, (3.1)
where the sum runs over representations Wλ
N of the unitary group which are indexed by
Young diagramsλ with at most N rows. The set of such diagrams is denoted YN. Moreover,
the partition functions are functions of the holonomy classes Ui of the gauge field on the
boundaries. We denoted by sλ(Ui) the character of an element of the conjugacy classUi in the
representation Wλ
N. Finally, c2(λ) is the quadratic Casimir of the representation Wλ
N. Note
that the coupling constant gYM and the area A always appear in the correlators (and in the
Wilson lines) in the combination g2
YMA. In other words, the dimensionless coupling constant
of the theory is g2
YMA.
It will be useful to split the sum over representations into two parts and write
X
λ∈YN
=
X
d
X
λ∈Yd
N
, (3.2)
8In particular, one can define a hole operator algebra. Holonomies U1 and U2 may be replaced in all
correlation functions by linear combinations of a single holonomy U3. This perspective is developed further at
the end of section 5.2.
8
where Yd
N is the set of Young diagrams of less than N rows and with d boxes. We refer to
the quantities obtained by only carrying out the second sum, i.e. by restricting the sum in
equation (3.1) to Young diagrams with exactly d boxes, as fixed-degree correlators. We will
denote these correlators Zd.
Let us argue that fixed-degree correlators are sensible in the whole theory – they manifestly
suffice to compute the whole theory. Indeed, the quantities Zd are observables. To prove this,
we can take a dual perspective on boundaries and associate to each boundary of the manifold
an irreducible representation of the gauge group U(N) – see e.g. [23]. The representations
must coincide to ensure that resulting correlators do not vanish [23]. We index the unique
irreducible representation at hand by a Young diagram µ and write
Zµ[Mg,k] =
Z
dU1...dU k·Z[U1,...,U k]·sµ(U−1
1 )··· sµ(U−1
k ) (3.3)
= (dimWµ
N)2−2G−k exp

−g2
YMA
2N c2(µ)

. (3.4)
The fixed-degree correlators Zd are linear combinations of the partition functions Zµ, which
implies that they are observables. This proves that these correlators are necessary and suffi-
cient ingredients to describe the full theory. From here on out, we refer to the set of partition
functions Zd of Yang-Mills correlators at fixed-degree d as the degree d sector of the theory.
