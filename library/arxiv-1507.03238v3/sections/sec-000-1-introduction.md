---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
The Ptolemy varietyPn(T ) of a topological ideal triangulationT of a compact 3-manifold
M was deﬁned by Garoufalidis, Thurston and Zickert [9]. It gives coordinates (called Ptolemy
coordinates) for boundary-unipotent SL(n, C)-representations ofπ1(M) in the sense that each
point inPn(T )determines a representation (up to conjugation). The Ptolemy variety is explicitly
computable for many census manifolds whenn = 2 or 3 (see [6, 5] for a database), and invari-
ants such as volume and Chern-Simons invariant can be explicitly computed from the Ptolemy
coordinates. The Ptolemy variety, however, depends on the triangulation and may miss several
components of representations.
Wefocusexclusivelyonthecasewhen n = 2, soweomitthesubscript nonthePtolemyvariety.
Our goal is to deﬁne a reﬁned Ptolemy varietyP (T ), which is a topological invariant ofM and is
guaranteed to detect all irreducible boundary-unipotentSL(2, C)-representations. We also deﬁne
reﬁned variants of the Ptolemy variety forPSL(2, C)-representations [9, 8], and for the enhanced
Ptolemy variety [13] forSL(2, C)-representations that are not necessarily boundary-unipotent.
The reﬁned variant of the latter detects all irreducibleSL(2, C)-representations.
A representation inSL(2, C) or PSL(2, C) is boundary-unipotent, respectivelyboundary-Borel,
if it takes each peripheral subgroup to a conjugate of the subgroupP, respectivelyB, whereB
is the group of upper triangular matrices, andP⊂B is the subgroup of matrices with1 on the
diagonal.
1.1. Motivation: Thurston’s gluing equations.In his famous notes Thurston [11] wrote
down a system of polynomial equations (calledgluing equations) for a compact 3-manifoldM
with a topological ideal triangulation. The system consists of a variable (called ashape) zi for
each simplex, and an equation for each edge. The set of solutions withzi∈ CP 1\{ 0, 1,∞} is
called thegluing equation variety, and each point in this variety determines (up to conjugation) a
C. Z. was supported by DMS-13-09088. M. G. was partially supported by DMS-11-07452.
1991 Mathematics Classiﬁcation.Primary 57N10, 57M27, 57M50. Secondary 13P10.
Key words and phrases: Ptolemy coordinates, representation variety, character variety,A-polynomial.
1
arXiv:1507.03238v3  [math.GT]  7 Dec 2017
2 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
PSL(2, C)-representation ofπ1(M). Solutions with somezi being 0, 1 or∞ are calleddegenerate,
and may not give rise to a unique representation, or to any representation at all. The gluing
equation variety and the set of representations detected depend on the triangulation and may
be empty.
In [10] Segerman considers a generalization of Thurston’s gluing equation variety, where the
shapes zi are replaced by variables in the ﬁeldC((ζ)) of Laurent series in a variableζ. He
proves the existence of a triangulation such that his generalized variety detects all irreducible
representations except those that have image in a generalized dihedral group. His approach
uses normal surfaces and it does not yield explicit deﬁning equations for the generalized variety.
Our approach focuses on Ptolemy coordinates and is completely combinatorial, and detects all
irreducible representations, even those with image in a generalized dihedral group. It is possible
that our methods could also be used to make Segerman’s generalized variety more explicit, but
we shall not pursue this idea here. Our paper does not require prior knowledge of Thurston’s
gluing equations or Segerman’s work.
1.2. Decoratedrepresentations. Aconvenientlanguageforstudyingboththegluingequation
