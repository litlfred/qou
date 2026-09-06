---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-024-12-gluing-equations-and-ptolemy-assignments
section_title: "Gluing equations and Ptolemy assignments"
section_number: 12
pages: 41-42
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
In this section we discuss the relation between Ptolemy assi gnments and solutions to the gluing
equations. The latter were invented by Thurston [ 27] to explicitly compute the hyperbolic structure
(and its deformations) of a triangulated hyperbolic manifo ld, and used eﬀectively in [ 22, 17, 9].
The gluing equations make sense for any 3-cycle. They are deﬁned by assigning a cross-ratio
zi ∈ C\{0, 1} to each simplex ∆ i of K. Given these, we assign cross-ratio parameters to the edges
of ∆ i as in Figure 11.
0
1
2
3
z zz′
z′
z′′
z′′
Figure 11. Assigning cross-ratio parameters to the edges of ∆ i. By deﬁnition, z′ = 1
1−z
and z′′ = 1 − 1
z .
There is a gluing equation for each edge E in K and each generator γ of the fundamental group
of each boundary component of M . These are given by
(12.1)
∏
e↦→E
z(e)ǫi(e) = 1,
∏
γ passes e
z(e)ǫi(e) = 1.
Here z(e) denotes the cross-ratio parameter assigned to e, and ǫi(e) = ǫi if e is an edge of ∆ i. It
follows that the set of assignments ∆ i ↦→zi ∈ C\{0, 1} satisfying the gluing equations ( 12.1) is an
algebraic set V (K).
Lemma 12.1. For every point {zi} ∈ V (K) there is a map D : L(0) → C ∪ {∞} such that if
~∆ i is a lift of ∆ i with vertices e1, . . . , e3 in L, the cross-ratio of the ideal simplex with vertices
D(e1), . . . , D(e3) is zi. It is unique up to multiplication by an element in PSL(2, C). Moreover,
there is a unique (up to conjugation) boundary-unipotent re presentation π1(M ) → PSL(2, C) such
that D is ρ-equivariant.
Proof. Pick a fundamental domain F for K in L. Pick a simplex ∆ in F and deﬁne D by mapping
the ﬁrst 3 vertices of ∆ to 0, ∞ and 1. The map D is now uniquely determined by the cross-ratios.
The fundamental group of M has a presentation with a generator for each face pairing of F . The
second statement thus follows from the fact that PSL(2, C) is 3-transitive. We leave the details to
the reader. □
42 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Given a Ptolemy assignment on K, we assign the cross-ratio zi = ci
03ci
12
ci
02ci
13
to ∆ i. Note that the
Ptolemy relations imply that the cross-ratio parameters ar e given by
(12.2) zi = ci
03ci
12
ci
02ci
13
, z ′
i = ci
02ci
13
ci
01ci
23
, z ′′
i = − ci
01ci
23
ci
03ci
12
.
Theorem 12.2. There is a surjective regular map
(12.3)
∐
σ∈H 2(K;Z/2Z)
P σ
2 (K) → V (K), c ↦→ {zi = ci
03ci
12
ci
02ci
13
}.
The ﬁbers are disjoint copies of (C∗)h, where h is the number of zero-cells of K.
Proof. By a simple cancellation argument (as in the proof of Zickert [ 30, Theorem 6.5]), the gluing
equations would be satisﬁed if the formula ( 12.2) for z′′
i did not have the minus sign. The minus
sign appears whenever the edge is 02 or 13. As explained in the proof of Proposition 7.7, any
curve passes these an even number of times. It thus follows th at the cross-ratios satisfy the gluing
equations. Surjectivity follows from Lemma 11.5, and the fact that ﬁbers are (C∗)h follows from
the fact that g1∞ = g2∞ if and only if g1N = g2dN for a unique diagonal matrix d. □
Remark 12.3. Gluing equation varieties for n > 2 are studied in Garoufalidis-Goerner-Zickert [ 15].
