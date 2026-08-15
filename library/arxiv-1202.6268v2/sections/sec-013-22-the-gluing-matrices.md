---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-013-22-the-gluing-matrices
section_title: "The gluing matrices"
section_number: 2.2
pages: 11-12
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
triangulations, namely the gluing and Neumann-Zagier matrices, the ir symplectic properties,
and the notion of a combinatorial ﬂattening. Although these notion s are motivated by
hyperbolic geometry (namely the gluing of ideal tetrahedra around their faces and edges
to describe a complete hyperbolic structure on a cusped manifold), we stress that these
12 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
notions make sense for arbitrary 3-manifolds with torus boundary , and for triangulations
whose gluing equations may not have solutions in C\{ 0, 1}.
Let M be an oriented one-cusped manifold with an ideal triangulation T ={∆ i}N
i=1 and
a choice of quad type.
The choice of quad, combined with the orientation of T and M allow us to attach vari-
ables (Zi,Z ′
i,Z ′′
i ) to each tetrahedron ∆ i. An Euler characteristic argument shows that the
triangulation has N edgesEI,I = 1,...,N . For each edge EI we introduce a gluing equation
of the form
(2.3) EI :
N∑
i=1
(
GIiZi + G′
IiZ ′
i + G′′
IiZ ′′
i
)
= 2πi I = 1,...,N,
where GIi∈{ 0, 1, 2} (resp., G′
Ii, G′′
Ii) is the number of times an edge of tetrahedron ∆ i with
parameter Zi (resp., Z ′
i, Z ′′
i ) is incident to the edge EI in the triangulation. In addition, we
impose the equations
(2.4) Zi +Z ′
i +Z ′′
i =iπ.
for i = 1,...,N . The Equations (
2.3) are not all independent. For a one-cusped manifold,
every edge begins and ends at the cusp, which implies ∑ N
I=1 GIi =∑ N
I=1 G′
Ii =∑ N
I=1 G′′
Ii =
2, and therefore that the sum of the left-hand sides of Equations (
2.3) equals 2πiN . This is
the only linear dependence in case of one cusp. In general, there is o ne relation per cusp of
M, as follows from [ Neu92, Thm.4.1].
An oriented peripheral simple closed curve µ (such as a meridian) on the boundary of M,
in general position with the triangulation of the boundary torus tha t comes from T , also
gives rise to a gluing equation. We assume that the curve is simple (has no self intersections),
and set the signed sum of edge parameters on the dihedral angles s ubtended by the curve
to zero. A parameter is counted with a plus sign (resp. minus sign) if a n angle is subtended
in a counterclockwise (resp. clockwise) direction as viewed from the boundary. These rules
are the same as described in [ Neu92], and demonstrated in Section 2.6 below.
Let us choose such a peripheral curve µ. We choose a meridian if M is a knot complement.
The gluing equation associated to µ then takes the form
(2.5) µ :
N∑
i=1
(
GN +1,iZi + G′
N +1,iZ ′
i + G′′
N +1,iZ ′′
i
)
= 0,
with GN +1,i, G′
N +1,i, G′′
N +1,i ∈ Z.
