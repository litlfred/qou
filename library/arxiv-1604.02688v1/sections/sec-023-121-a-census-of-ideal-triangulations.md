---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-023-121-a-census-of-ideal-triangulations
section_title: "A census of ideal triangulations"
section_number: 12.1
pages: 41-42
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
ing a list of all ideal triangulations with at most six tetrahedra using Regina’stricensus
function. Then it was determined if these triangulations were solid tori. Of the remaining
triangulations, we then (i) determined their irreducibility and (ii) checked for incompressible
tori and Klein bottles. The ﬁrst condition was checked using a light adaptation of Regina’s
isThreeSphere function and the second determined using Regina’sisSolidTorus and a
new functionisT2xI (see [Bur]). The latter function is similar to Haraway’s algorithm [Har,
Corollary 15], but instead of using an analysis of spun normal annuli, it relies on the fact
that ifM is a 2-cusped manifold with threeS1×D2 surgeries along slopes{γ1,γ 2,γ 3}, then
M is homeomorphic toT 2×I the Berge manifold [Ber91, Gab89], or is Seifert ﬁbred over the
42 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
annulus with one exceptional ﬁbre. However, all of theS1×D2 ﬁllings of the Berge manifold
are pairwise distance one from each other, and so if a manifold admitsS1×D2 ﬁllings along
slopes{ 1
0,− 1
1, 2
1} then it must beT 2×I or Seifert ﬁbred over the annulus. The latter can
be ruled out since at least one of the ﬁllings{ 1
0,− 1
1, 2
1} will result in a Seifert ﬁbred space
over the disk with two (non-trivial) exceptional ﬁbres.
This allows for a decomposition into prime and atoroidal pieces. Those pieces were then
classiﬁed by searching the Pachner graph of the corresponding triangulations and simplifying
the triangulation to that of either a SnappyOrientableCuspCensus triangulation (using
SnapPy’sidentify function) or until it was equivalent via Pachner moves to a known
triangulation of a lens space (in the case of some prime summands) or a cusped Seifert
ﬁbered space (using a dictionary of triangulations also included with the code). While a
larger library of closed triangulations would be needed for more complicated prime and JSJ
decompositions, this was suﬃcient for our purposes.
After this coarse classiﬁcation, the triangulations were then analysed for 1-eﬃciency. The
results of this census are summarised in Tables 1 and 2 below; the code used is available as
an ancillary ﬁle to the arxiv version of this paper.
n total S1×D2 T 2×I P×S1 Red. Tor. SFS Hyp. Taut 1-eﬃcient
2 10 3 0 0 0 1 4 2 7 9
3 129 65 1 0 0 15 36 12 53 102
4 1852 917 11 0 107 188 491 138 441 1082
5 26909 14324 197 1 2533 2164 6344 1346 3310 12130
6 414946 219080 2981 32 58508 29451 89933 14961 134538 28405
Table 1. This table provides information on the various types of (orientable)
ideal triangulations that can be built fromn = 2, 3, 4, 5, 6 tetrahedra. Total is
the total number of triangulations for each value ofn, S1×D2 is the number
of solid tori, similarly forT 2×I and P×S1. Red. counts the number of
reducible manifolds and Tor. counts the number of toroidal manifolds which
are not homeomorphic to SFS [D(2, 1)(2, 1)]. Instead SFS [D(2, 1)(2, 1)] is
counted in SFS which record the number of SFS over the disk or annulus with
two or one exceptional ﬁbres respectively. Finally, Hyp. counts the number
of hyperbolic manifolds observed. Note that in each case, this computation
is rigorous, in the sense that the triangulation was connected to a known
triangulation via Pachner moves. Finally, Taut records the number of trian-
gulations admitting a taut angle structure and 1-eﬃcient records the number
of 1-eﬃcient triangulations.
