---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-002-3-the-polytope-of-angle-structures
section_title: "The polytope of angle structures"
section_number: 3
pages: 7-10
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifold M with"
---
As we have seen in the last section, the shape of a hyperbolic ideal tetrahedron
is completely determined by its dihedral angles. The notion of an angle structure
is that these dihedral angles should ﬁt together coherently.
Definition 3.1. An angle structure on an ideal triangulation τ is an assign-
ment of an (internal) dihedral angle to each edge of each tetrahedron, such that
opposite edges carry the same dihedral angle, and such that
(1) all angles lie in the range (0, π),
(2) around each ideal vertex of a tetrahedron, the dihedral angles sum to π,
(3) around each edge of M, the dihedral angles sum to 2π.
The set of all angle structures on τ is denoted A(τ).
Conditions (1) and (2) in the deﬁnition above are precisely what is needed to
specify a non-degenerate hyperbolic ideal tetrahedron up to isometry.
For con-
creteness, if the three dihedral angles meeting at a vertex of T are labeled α, β, γ
in clockwise order, then the shape parameter corresponding to α is
(3.1)
z(α) = sin γ
sin β eiα,
by the law of sines. Meanwhile, condition (3) in the deﬁnition is nothing other than
the imaginary part of the edge equation (2.3).
The notion of an angle structure can be summarized by saying that the tetra-
hedra of τ carry genuine hyperbolic shapes, but the conditions these shapes must
satisfy are much weaker than the gluing equations. The completeness equations
are discarded entirely1, and the real part of the edge equations is also discarded. If
we attempt to glue the metric tetrahedra coming from an angle structure, we can
encounter shearing singularities at the edges of τ, as in Figure 1.
One may separate the gluing equations of Deﬁnition 2.4 into a real part and
an imaginary part. The real part of the equations is non-linear, because the shape
parameters within one tetrahedron are related in a non-linear way in equation (2.1).
On the other hand, the imaginary part of the equations is linear in the dihedral
angles, and the set of angle structures A(τ) is deﬁned by a system of linear equations
and strict linear inequalities. This leads to
1There is an alternative version of an angle structure, in which the angles must also satisfy
the imaginary part of the completeness equations. This corresponds to taking a linear slice of the
polytope A(τ). We will not need this version for the main part of the paper — but see Section
6.1 for variations on this theme.
165
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
8
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
Proposition 3.2. Let τ be an ideal triangulation of M, containing n tetrahe-
dra. The set of all ways to assign a real number to each pair of opposite edges of each
tetrahedron is naturally identiﬁed with R3n. Then A(τ) is a convex, ﬁnite–sided,
bounded polytope in R3n. If A(τ)̸ = ∅, its dimension is
dim A(τ) = |τ| + |∂M|,
where |τ| = n is the number of tetrahedra and |∂M| is the number of boundary tori
in M.
Proof. Condition (1) of Deﬁnition 3.1 is a system of strict inequalities that
constrains the coordinates of A(τ) to the open cube (0, π)3n. Meanwhile, conditions
(2) and (3) impose a system of linear equations, whose solution set is an aﬃne
subspace of R3n. The intersection between this aﬃne subspace and (0, π)3n will be
a bounded, convex, ﬁnite–sided polytope.
We claim that the number of edges in the triangulation τ is n, the same as
the tetrahedra. To see this, observe that each tetrahedron gives rise to 4 boundary
triangles that lie in ∂M. Thus ∂M is subdivided into 4n boundary triangles. These
triangles have a total of 12n sides, glued in pairs; thus ∂M has 6n edges. Since
every component of ∂M is a torus,
χ(∂M) = 0 = 4n −6n + 2n,
hence there are 2n vertices on ∂M. Since every edge of τ accounts for two vertices
on ∂M, the number of edges in τ is n, as claimed. It will be convenient to think of
the tetrahedra as numbered 1 to n, and the edges as numbered n + 1 to 2n.
Deﬁnition 3.1 involves 2n equations and 3n unknowns. This system can be
encoded in a (2n × 3n) matrix A, as follows. Each column of A corresponds to a
pair of opposite edges of one tetrahedron. For 1 ≤i ≤n, the entry aij records
whether or not the ith tetrahedron contains the jth edge pair. In other words, aij
will be 1 when 3i −2 ≤j ≤3i, and 0 otherwise. For n + 1 ≤i ≤2n, the entry aij
records how many edges out of the jth edge pair become identiﬁed to the ith edge
of the glued-up manifold. Thus the entries in the bottom half of A can be 0, 1, or
2. With this setup, the system of equations is
A v = [π, . . . , π, 2π, . . . , 2π]T ,
where v ∈R3n is the vector of angles. Then dim A(τ) = 3n −rank(A).
Lemma 3.3. rank(A) = 2n −|∂M|.
This result is due to Neumann [21]. Our proof is adapted from Choi [2, Theo-
rem 3.7].
Proof. Since the matrix A has 2n rows, it suﬃces to show that the row null
space has dimension |∂M|. We will do this by constructing an explicit basis for the
row null space, with basis vectors in 1 −1 correspondence with the cusps of M.
Let c be a cusp of M. Associated to c, we construct a row vector rc ∈R2n.
For 1 ≤i ≤n, the ith entry of rc is minus the number of ideal vertices that the
ith tetrahedron has at cusp c. For n + 1 ≤i ≤2n, the ith entry of rc is plus the
number of endpoints that the ith edge has at cusp c. Thus rc records incidence,
with tetrahedra counted negatively and edges counted positively.
Claim: For every cusp c, rc A = 0.
166
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
9
Let vj be a column of A, and recall that vj corresponds to one pair of opposite
edges in one tetrahedron. Then the dot product rc · vj counts minus the number
of times that one of these edges has an endpoint at c, plus the number of times
that one of these edges is identiﬁed to an edge of M that has an endpoint at c.
Naturally the sum is 0.
Claim: The collection of vectors rc is linearly independent.
Suppose that  λcrc = 0, and let ei be the ith edge in M. The ith entry of
rc will be 0, except when c is one of the endpoints of ei.
Thus, if the edge ei
has endpoints at cusps a and b, and the ith entry of  λcrc is 0, we must have
λa + λb = 0.
Now, let Δ be an ideal triangle of τ, whose ideal vertices are at cusps a, b, and
c. The argument above, applied to the three edges of Δ, gives
λa + λb = 0,
λa + λc = 0,
λb + λc = 0.
The only way that these three equalities can hold simultaneously is if λa = λb =
λc = 0. Thus all coeﬃcients λc must vanish.
Claim: The collection of vectors rc spans the row null space of A.
Let q = [q1, . . . , q2n] be a vector such that q A = 0. Our goal is to show that
q =  λkrk. To that end, let Ti, (1 ≤i ≤n), be one tetrahedron of τ. Let a, b, c, d
be the cusps of M corresponding to the four ideal vertices of Ti. (Some of these
cusps may coincide.) A pair of letters from the collection {a, b, c, d} determines
an edge of Ti, which is identiﬁed to some edge of M. For notational convenience,
suppose that edge ab from tetrahedron Ti is identiﬁed to the edge i(ab) in M, and
similarly for the other letters.
Now, let vj be the jth column vector of A. This column of A corresponds to
a pair of opposite edges in one tetrahedron, which will be tetrahedron Ti if and
only if 3i −2 ≤j ≤3i. After relabeling {a, b, c, d}, we may assume that j = 3i −2
corresponds to opposite edges i(ab) and i(cd),
j = 3i−1 corresponds to i(ac) and
i(bd),
and j = 3i corresponds to i(ad) and i(bc). By the deﬁnition of the matrix
A, the only non-zero entries of v3i−2 are in row i (corresponding to the tetrahedron
Ti) and rows i(ab), i(cd) (corresponding to edges of M). The analogous statement
holds for j = 3i −1 and j = 3i.
Since q A = 0, we must have q · vj = 0 for every j. Applying this to 3i −2 ≤
j ≤3i gives
q · v3i−2
=
qi + qi(ab) + qi(cd)
=
0,
q · v3i−1
=
qi + qi(ac) + qi(bd)
=
0,
q · v3i
=
qi + qi(ad) + qi(bc)
=
0,
which implies
(3.2)
qi(ab) + qi(cd) = qi(ac) + qi(bd) = qi(ad) + qi(bc) = −qi.
We are now ready to ﬁnd coeﬃcients λk such that q =  λkrk. Let Δ be an
ideal triangle in Ti, whose ideal vertices are at cusps a, b, c and whose sides are at
edges i(ab), i(ac), i(bc). Deﬁne
(3.3)
λa = qi(ab)+qi(ac)−qi(bc)
2
,
λb = qi(ab)+qi(bc)−qi(ac)
2
,
λc = qi(ac)+qi(bc)−qi(ab)
2
.
A priori, this deﬁnition depends on the ideal triangle Δ. To check this is well-
deﬁned, let Δ′ be another ideal triangle of Ti, for example the triangle with ideal
167
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
10
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
vertices at b, c, d. Note that equation (3.2) implies that
qi(cd) −qi(bd) = qi(ac) −qi(ab).
Thus the deﬁnition of λc coming from Δ′ will be
λc = qi(bc) + qi(cd) −qi(bd)
2
= qi(bc) + qi(ac) −qi(ab)
2
.
Therefore, triangles Δ and Δ′ that belong to the same tetrahedron and share a
vertex at cusp c induce the same deﬁnition of λc. Since any pair of ideal triangles
that meet the cusp c are connected by a sequence of tetrahedra, it follows that λc
is well-deﬁned.
It remains to check that this deﬁnition of λc satisﬁes q =  λkrk. Recall that
for n + 1 ≤i ≤2n, the ith entry of rk is the number of endpoints that the ith edge
has at cusp k. If the ends of this edge are at cusps a and b, i.e. if this is the edge
we have referred to as i(ab), then the ith entry of  λkrk is
(3.4)
λa + λb = qi(ab),
using equation (3.3). This is exactly the ith entry of q. Similarly, for 1 ≤i ≤n, the
ith entry of rk is minus the number of ideal vertices that Ti has at cusp k. Thus, if
Ti has ideal vertices at cusps a, b, c, d (where some of these may coincide), the ith
entry of  λkrk is
−(λa + λb + λc + λd) = −qi(ab) −qi(cd) = qi,
using equations (3.4) and (3.2). Thus q =  λkrk, as desired.
This completes the proof that the vectors rc, indexed by the cusps of M, form
a basis for the row null space of A. Therefore, rank(A) = 2n −|∂M|
□
We conclude that dim A(τ) = 3n −rank(A) = n + |∂M|, completing the proof
of Proposition 3.2.
□
