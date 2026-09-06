---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-006-8-results
section_title: "Results"
section_number: 8
pages: 20-21
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
Our implementation of the algorithm in Section 7 is available at [Goe19b]. Lists of all
knots and links from Theorem 1.1 as well as the isomorphism signatures of the ﬁnite
triangulations we used are available at [Goe19a].
To produce the input to the algorithm, we used SnapPy [CDGW] to produce a ﬁnite tri-
angulation of a manifold and Orb [Hea] to ﬁnd unveriﬁed ﬂoating point edge parame-
ters. Note that there are ﬁnite triangulations that admit hyperbolic structures but Orb is
unable to ﬁnd one. However, for all examples of hyperbolic manifolds considered here,
we are always able to make Orb succeed in ﬁnding edge parameters by randomizing the
ﬁnite triangulation in SnapPy several times.
We were able to verify a hyperbolic structure on a ﬁnite triangulation of each of the
11031 orientable closed manifolds in the Hodgson-Weeks census [HW94] and the 21962
genus 2 surface bundles and 3100 genus 3 surface bundles in the census by Bell [Bel15].
In particular, we have an independent proof of [HIK+16, Theorem 5.2] that all manifolds
in SnapPy’ sOrientableClosedCensus are hyperbolic.
To prove Theorem 1.1, we went through all knots and links up to 15, respectively, 14
crossings tabulated by Hoste-Thistlethwaite4 and used SnapPy to produce the branched
double cover. We either used the above method to prove that the resulting manifold is
hyperbolic or used Regina [Bur18] to prove that it is not hyperbolic by
• ﬁnding the triangulation in Regina’ s census or
• recognizing that the triangulation has a structure ﬁtting one of Regina’ s
StandardTriangulation’ s making it, e.g., a Seifert ﬁber space, or
• ﬁnding an essential torus using normal surface theory.
Note that the ﬁrst two methods sometimes require some randomizations and simpli-
ﬁcations of the triangulation in SnapPy to work and that the last method can be quite
expensive.
The number of tetrahedra in the triangulations used to prove hyperbolicity was between
9 and 46. Most triangulations are single vertex, few have two vertices, and only one had
three vertices.
4See HTLinkExteriors, AlternatingKnotExteriors, and NonalternatingKnotExteriors in
SnapPy.
21
Testing the algorithm on the bundle census and branched double covers was suggested
by Nathan Dunﬁeld since the geodesics isotopic to the components of the branching lo-
cus tend to be long and spun triangulations spinning about one of these geodesics very
often fail to be geometric. By ﬁlling and drilling the triangulation, Dunﬁeld found geo-
metric spun triangulations (about a different geodesic) for the branched double covers
of 42367 non-alternating knots and links up to 14 crossings, missing 1593.
Remark 8.1. We also investigate how the occurrence of gimbal lock depends on the edge
partition E ∼ ∪ E = = E(T ) with |E ∼| = 3o where o is number of vertices. For this, we ﬁx a
triangulation and a hyperbolic structure and check numerically whether the derivative
Dg of the gimbal function has singular values close to zero for different partitions (ex-
hausting all partitions when o ≤ 2 and sampling otherwise). We did this for several tri-
angulations of orientable closed census manifolds including some with three and four
vertices obtained by performing 1-4 moves. This lead to Conjecture 9.1.
