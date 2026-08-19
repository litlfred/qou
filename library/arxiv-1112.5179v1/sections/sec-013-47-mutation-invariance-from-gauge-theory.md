---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-013-47-mutation-invariance-from-gauge-theory
section_title: "Mutation invariance from gauge theory"
section_number: 4.7
pages: 42-46
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
In this section, we begin to test the strength of the index as a topological invariant of 3-
manifolds — i.e. its ability to distinguish 3-manifolds from one another. We will specialize to
the case of knot complements M, either in S3 or in some closed 3-manifold M, and consider
the operation of mutation [53]. To perform a mutation, the knot complement M is cut along
an S2 that is punctured exactly four times by the knot, separating M into two halves24 M1
and M2; then the halves are glued back together with a “180 ◦ rotation” along some axis of
S2, forming a new manifold Mµ. More precisely, the rotation of S2 interchanges two pairs of
punctures. This is illustrated in Figure 9 for the simplest topologically distinct mutant pair
of knot complements.
It is famously known that mutation acts trivially on colored Jones polynomials, theSU (2)
Chern-Simons wavefunctions of knot complements [54] (see also [65]). We have also mentioned
several times that the index should correspond to a complex SL(2, C) Chern-Simons wave-
function. Thus a natural expectation might be that the index is mutation invariant. We will
prove this physically below, by using the 6 d realization of theories TM, and also by argu-
ing that mutation is implemented by a 3d superpotential deformation that leaves the index
untouched. First, however, we can do a simple check. The triangulations of the KT and
24It is perfectly possible that S2 does not split M in two, but rather into a manifold ˜M with two S2
boundaries. Everything we say in this section will go through with very minor modiﬁcations in that case.
– 41 –
Conway knot complements in Figure 9 are easily found with the program SnapPy [60]. In
their simplest (non-univalent) form, they have 12 tetrahedra each, leading to an expression
for the corresponding indices as 11-dimensional sums. Then we ﬁnd, for example, that 25
IKT(0, 0;q) =ICon(0, 0;q) = 1 + 6q− 32q2 +O(q3). (4.58)
If the indices IKT andICon were to diﬀer, they could only do so by a ﬁnite number of q-
dependent normalizations — since the colored Jones polynomial determines operators ˆLM,
and these in turn ﬁx the index up to q-dependent boundary conditions. Thus, evaluating the
index even at (m,e ) = (0, 0) as in (4.58) is quite a nontrivial check of mutation invariance.
M
C
M1 M2C
Figure 10. Stretching M along C. Com-
pactiﬁcation on C gives a 4d theory T [C]
on R3×I.
Now, let us proceed to the six-dimensional ar-
gument. Consider the six-dimensional A1 theory
on a three-manifold M, and identify a two-sphere
C = S2 in M that intersects exactly four strands
of codimension 2 regular defects. We will denote as
M1 and M2 the two halves of M joined along C.
We can put a metric on M that elongates a neigh-
borhood of C into a long cylinder of cross-section
C (Figure 10). At low energy, the six-dimensional
setup admits a simple four-dimensional description,
as a four-dimensionalN = 2 gauge theory on a seg-
ment, with boundary conditions B1 andB2 at the
endpoints that are determined by the geometry of
M1 and M2. The four-dimensional theory is SU (2)
gauge theory withNf = 4 fundamental hypermulti-
plets. In the far IR, the four-dimensional setup will
ﬂow back to TM.
This cutting construction, of course, can be done for any surface C, but the four-
punctured sphere is special. While for generic C the four-dimensional theory has an SU (2)
ﬂavor symmetry for each puncture, inherited from the ﬂavor symmetry of codimension-2 de-
fects in the six-dimensional theory, the SU (2)Nf = 4 theory has an SO(8) ﬂavor symmetry.
The ﬂavor symmetries with a six-dimensional origin compose anSO(4)×SO(4) block-diagonal
subgroup ofSO(8). The remaining 16 generators of SO(8) are accidental IR symmetries that
appear in the four-dimensional limit. As TM can be deﬁned by the four-dimensional setup,
the enhanced SO(8) ﬂavor symmetry has important consequences for TM.
One important consequence is that any boundary condition B for SU (2) Nf = 4 theory
sits in an SO(8) orbit of boundary conditions g◦B , g∈ SO(8). In principle it is possible
to imagine an SO(8)-invariant boundary condition. For example: set Dirichlet boundary
conditions for the gauge ﬁelds, split the 16 chiral ﬁelds in the hypermultiplets into sets Xi,
25As per the linear/quadratic behavior of the index explained in Section 4.6, evaluating these indices to
orderqn requires summing over an 11-dimensional cube with sides approximately of length 2n. This is feasible
for low order. The computation in (4.58), done naively, required 11 7 terms and took 28 hours per knot.
– 42 –
Yi, each in a vector representation of SO(8) (Xi andYi are the top and bottom components
respectively of the 8 SU (2) doublets), and then give Dirichlet b.c. to Xi and Neumann b.c.
to Yi. However, we are not aware of a geometric realization for such a boundary condition.
Boundary conditions B obtained from a generic six-dimensional conﬁguration will typically
break SO(8) down to SU (2)4, or even a smaller subgroup HB, and hence will sit in a non-
trivial continuous family SO(8)/HB of boundary conditions.
Although it will not be too important for us, it is simple to show that these exactly
marginal deformations of anN = 2 supersymmetric boundary conditionB are actually super-
potential deformations. Indeed, they correspond to deformations of the boundary conditions
for the hypermultiplets only, and can be implemented by adding superpotential terms at the
boundary. The true space of exactly marginal deformations of B will be some complex man-
ifold that locally is the complexiﬁcation of SO(8)/HB. We do not have a good handle over
the full space of exactly marginal deformations, but for our purpose SO(8)/HB is suﬃcient.
Notice that even if B has a six-dimensional realization as some cobordism with a single
non-empty boundary C (×R3), generically the boundary condition g◦B may not have such a
realization. There is an exception, though: if g is an SO(8) rotation that permutes the four
SU (2)’s among themselves, then g◦B can be also realized by the same cobordism as B, with
the four punctures suitably permuted. There is an obvious example: the diagonal matrix
(1, 1, 1,−1, 1, 1, 1,−1) acts as a reﬂection in each SO(4), and therefore permutes the two
SU (2)’s in each SO(4). Thus we can ﬁnd an SO(8) rotation µ that simultaneously permutes
any two distinct pairs of punctures. ThenB andµ◦B are deﬁned by two possibly inequivalent
six-dimensional cobordisms, but are related by a continuous family of deformations that do
not admit a simple six-dimensional deﬁnition.
Now, we can deﬁne a deformation Tµ
M of the 3d theory TM by taking four-dimensional
SU (2) Nf = 4 gauge theory on the segment, with modiﬁed boundary conditions B1 and
µ◦B 2 at the endpoints. Clearly Tµ
M is the theory associated to a new three-manifold Mµ,
obtained by permuting the two pairs of strands across C. This is the deﬁnition of a mutation
of M. But the theories TM and Tµ
M are related by a continuous family of exactly marginal
deformations, hence must have the same index!
This is the main conclusion of this section. Next, we would like to recast it in a lan-
guage that makes use only of the deﬁnition of TM through the gluing of tetrahedra, with no
reference to the six-dimensional setup. We are after a continuous family of exactly marginal
deformations of TM, possibly including a subset HB1\SO(8)/HB2 and modeled locally on the
complexiﬁcation of that locus. If HB1 andHB2 areSU (2)4, the exactly marginal locus should
be four-dimensional. Notice that in concrete examples, such exactly marginal deformations
may be directly visible in the index, as chiral operators of R-charge 2 and speciﬁc ﬂavor
charges under the ﬂavor symmetries associated to the codimension two defects.
In order to proceed, we will assume thatM admits a triangulation that can be split along
C without cutting any tetrahedra. If we split along C, we will get triangulated versions of
– 43 –
E1
￿E1
￿E2
E2
M
C
C1 C2
M1 M2
Figure 11 . Splitting M = M1∪C M2 along a 2-sphere C to form two new geodesic boundaries,
triangulated by faces of tetrahedra.
M1 and M2, each with a triangulated C boundary component, C1 and C2; see Figure 11. 26
Clearly,C1 and C2 are triangulated in the same way, and gluing M1 and M2 back along C
can be done by imposing a standard gluing constraint for each edge in the triangulation of
C. So we can start from the theories TM1 and TM2 and implement the gluing constraints
by adding superpotential terms OE, one for each edge E of C. In a polarization where the
images E1 and E2 of E in C1 and C2 carry position edge variables, we can write
OE =OE1OE2 (4.59)
for operatorsOE1 andOE2 in the theories TM1 and TM2 respectively.
Again, this is true for a generic C, but if C is a four-punctured sphere something special
happens. Consider any of the many triangulations with the topology of a tetrahedron (not
to be confused with the tetrahedra we use for gluing!). Then any pair of opposite edges
E, ˜E have the same gauge charges, and only diﬀer by the ﬂavor charges associates with
the punctures. This means that in any polarization where the E edge coordinate and the
meridians of defects are positions, the edge coordinate of ˜E is also a position.
Thus we can simultaneously decompose
OE =OE1OE2, O ˜E =O ˜E1O ˜E2. (4.60)
Now,OE1 andO ˜E1 have the same gauge charges, and diﬀerent ﬂavor charges. The same is
true forOE2 andO ˜E2. Thus we can also build two new gauge-invariant operators
O12 =OE1O ˜E2, O21 =O ˜E1OE2. (4.61)
We can repeat the analysis for all the pairs of edges in the triangulation of C. This gives
us a total of six new gauge-invariant marginal operators of “mixed” type (4.61) in addition to
the six operators of type (4.60). It should be clear that a mutation M→Mµ simply modiﬁes
26The triangulations ofM1 andM2 contain annular cusps, and are of the “hybrid” type discussed in Section
2 of [19]. Such triangulations will be a major focus of [61].
– 44 –
the geometric gluing by permuting two opposite pairs of edges in, say, C2. In ﬁeld theory,
this corresponds to a diﬀerent choice of gluing superpotential, replacing four of the standard
operators with four of the new operators. This has no eﬀect on the index. In particular,
either conﬁguration breaks exactly the same set of global U(1) symmetries.
We can even try to see part of the space of exactly marginal deformations ofTM: consider
the most general superpotential, a linear combination of the six standard operators and the six
new operators. There is a choice of R-charges that makes all the twelve operators marginal.
The general superpotential breaks many ﬂavor symmetries of the product theory TM1×TM2.
The standard superpotential forces the meridians (puncture eigenvalues) of C1 to be equal
to the meridians of C2. The general superpotential forces all meridians to be equal . The
number of ﬂavor symmetries broken by the general superpotential is strictly smaller than 12,
but there are 12 marginal operators. By the results of [66], this indicates that at least one
linear combination of the 12 operators is exactly marginal.
We can try to be more precise. Assume thatTM1×TM2 hasSU (2)8 ﬂavor symmetry asso-
ciated to the defects, broken toSU (2)4 by the standard gluing superpotential. Then the 6 new
operators have charges ±( 1
2, 1
2,− 1
2,− 1
2),±( 1
2, 1
2,− 1
2,− 1
2),±( 1
2,− 1
2,− 1
2, 1
2),±( 1
2,− 1
2, 1
2,− 1
2)
respectively. Because of the SU (2)4 ﬂavor symmetry, the operators must really be part of a
set of 16 marginal operators in the tensor product of the four doublet representations of the
four SU (2) ﬂavor groups. By the results of [66], the space of exactly marginal deformations
is locally the K¨ ahler quotient of C16 by SU (2)4, which is indeed a local complexiﬁcation of
the expected SU (2)4\SO(8)/SU (2)4. Thus we recovered the full space of exactly marginal
deformations predicted in the UV.
