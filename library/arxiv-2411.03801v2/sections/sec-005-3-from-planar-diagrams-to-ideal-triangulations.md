---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-005-3-from-planar-diagrams-to-ideal-triangulations
section_title: "From planar diagrams to ideal triangulations"
section_number: 3
pages: 9-9
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
In this section we recall a well-known connection between planar projections of (hyper-
bolic) knots and their ideal triangulations. The history of the subject predates quantum
topology, and the sought algorithm takes as input a planar projection D of a knot K, pro-
duces as an intermediate stage an octahedral cell decomposition of its complement minus
two points, and eventually produces an ideal triangulation of its complement S3\K. This
algorithm due to Thurston appears in the code of SnapPy in the original version due to
Weeks [CDGW]. It is described in detail in [Wee05], and forms the core method of SnapPy
for computing numerically (or exactly) the complete hyperbolic structure of a hyperbolic
knot (or more generally, link) complement.
Years after its discovery and its use in hyperbolic geometry, it was realized that the above
algorithm has applications to quantum topology, and more precisely to the volume conjec-
