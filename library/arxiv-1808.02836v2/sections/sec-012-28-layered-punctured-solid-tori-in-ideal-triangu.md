---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-012-28-layered-punctured-solid-tori-in-ideal-triangu
section_title: "Layered punctured solid tori in ideal triangulations"
section_number: 2.8
pages: 15-16
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low degree edges"
---
The argument for closed 3–manifolds in [22] hinged on an understanding of the intersections of maximal
layered solid tori. We now carry such an analysis out in the case of cusped hyperbolic 3–manifolds. This
requires a different approach due to the fact that the combinatorics of minimal ideal triangulations is less
restricted than the combinatorics of minimal and 0–efﬁcient (material) triangulations.
As in [22] we focus on subcomplexes in triangulations that are maximal layered ∂ –punctured solid tori (see
Section 2.4 for a brief introduction).
Lemma 12 Let T be a minimal ideal triangulation of a cusped hyperbolic 3–manifold M. Then the inter-
section of any two maximal layered ∂ –punctured solid tori is either empty, an ideal vertex, or an ideal edge
of T .
Proof Let LST a,LSTb⊂ T be two maximal ∂ –layered solid tori. If their boundaries ∂ LSTa and ∂ LSTb
meet in two faces, T must be homeomorphic to a punctured lens space. A contradiction. If LST a and LST b
share a common tetrahedron, remove the tetrahedra in the intersection from one of them and observe, that they
now meet in two faces. Again, a contradiction. Hence, we can assume that two maximal ∂ –layered solid tori
meet along a single face, three edges, or two edges.
(1) Assume that ∂ LSTa and ∂ LSTb meet along exactly two edges. It follows, that they must be identiﬁed
along a spine of each of ∂ LSTa and ∂ LSTb, referred to as their common spine. Let Da and Db be the
discs obtained by taking the interior of ∂ LSTa and ∂ LSTb after truncating their vertex and removing
their common spine. Da and Db can be glued together along sections of the exchange annuli in a
15
neighbourhood of the common spine yielding a 4–punctured sphere S properly embedded in Mc (the
truncated compact core of M) and disjoint from the two edges of the common spine.
By construction, the four boundary components of S in one of the torus boundary components T0⊂
∂Mc bound a regular neighbourhood of the intersection of the maximal layered solid tori LST a and
LSTb with T0 – a regular neighbourhood of two discs pinched along four points (the four points being
the intersection of the common spine with T0). Since this regular neighbourhood is connected, of Euler
characteristic−2, and with four boundary components, it must be a 4–punctured sphere contained inT0.
There are two cases: either all components of ∂ S are trivial in T0 (that is, S equals a disc of T0 with
three points removed), or two components of ∂ S are non-trivial (that is, S equals an annulus of T0
with two points removed).
First suppose (LSTa∪LSTb)∩ T0 is contained in a disc on T0 and hence three of its boundary compo-
nents bound discs in the complement of the intersection. Pasting these three discs of T0 into S and
pushing them slightly off T0 yields a disc properly embedded in Mc. This disc can be extended to a torus
parallel to boundary component T0 of Mc. Moreover, this torus is disjoint from the two edges of T
of the common spine, which both are incident to T0. It follows that a normalised version of this torus
cannot be equal to the vertex linking torus T0 and thus T cannot be boundary efﬁcient. A contradiction
to Theorem 4.
Hence suppose (LSTa∪LSTb)∩ T0 is contained in an annulus on T0 and hence two of its boundary
components bound discs in the complement of the intersection. Pasting these two discs ofT0 into S and
pushing them slightly off T0 yields an annulus properly embedded in Mc and disjoint from the two edges
of T of the common spine (which are both incident to T0). This annulus together with the annulus in
T0 complementary to (LSTa∪LSTb)∩ T0 extends to a boundary parallel torus since otherwise M would
contain a non-trivial Seifert ﬁbred space. Again, this boundary parallel torus leads to a contradiction to
the assumption that T is boundary efﬁcient (cf. Theorem 4).
(2) Assume that ∂ LSTa and ∂ LSTb meet along exactly three edges. Following an analogous procedure as in
the previous case, we arrive at two 3–punctured spheres S1 and S2 (instead of one 4–punctured sphere
S ), both properly embedded in Mc, both meeting the same boundary component T0⊂ ∂Mc. Again,
it follows that a regular neighbourhood of (LSTa∪LSTb)∩ T0 is connected, of Euler characteristic−4
with six boundary components and thus a 6–punctured sphere.
Pasting in some of the boundary discs of this 6–punctured sphere, analogously to the procedure carried
out in the previous case, yields a torus parallel to boundary component T0 and disjoint from three edges
of the triangulation which are all incident to T0 – and we conclude as before by using Theorem 4.
(3) Assume that ∂ LSTa and ∂ LSTb meet along a single face. Again, we argue as in the previous cases.
Here, we end up with one 3–punctured sphere S (the other one being ﬁlled in as a result of the face
identiﬁcation). A regular neighbourhood of (LSTa∪LSTb)∩T0 now is connected, of Euler characteristic
−1, has three boundary components, and thus is contained in a disc or an annulus onT0. We again obtain
a disc or an annulus that can be extended to a torus running parallel toT0 which is disjoint of three edges
of the triangulation incident to T0 and we use Theorem 4 once again to ﬁnish the proof.
This completes the proof of the lemma.
