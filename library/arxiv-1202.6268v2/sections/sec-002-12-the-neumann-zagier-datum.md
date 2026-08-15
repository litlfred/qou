---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-002-12-the-neumann-zagier-datum
section_title: "The Neumann-Zagier datum"
section_number: 1.2
pages: 4-5
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
per will be oriented. The volume of a hyperbolic manifold M, appearing in the Volume
Conjecture and contributing to SM, 0, is already known to have a simple expression in terms
of shape parameters of a regular ideal triangulation, i.e., one that recovers the complete
hyperbolic structure of M. (For extended discussion on regular triangulations, see Section
4.) IfT ={∆ i}N
i=1 is a regular ideal triangulation of M with shape parameters zi∈ C\{0, 1}
for i = 1,...,N , then ( cf. [
DS82, NZ85])
(1.5) Vol( M) =
N∑
i=1
D(zi),
whereD(z) := Im
(
Li2(z)
)
+ arg(1−z) log|z| is the Bloch-Wigner dilogarithm function. This
formula can also be interpreted as calculating the image of the class [ M] := ∑
i[zi]∈ Bof
M in the Bloch group B under the natural map D :B→ R. An analogous formula, using
the class of M in the “extended” Bloch group ˆB, gives the full complexiﬁed volume SM, 0
[Neu92, Neu04, GZ07, Zic09].
It is natural to ask whether the class of M inB determines not only SM, 0 but the higher
SM,n as well. This question was posed to the authors several years ago b y D. Zagier. Sub-
sequent computations [ GZ, Gar] indicated that a positive answer was not possible. For
example, there is a family of pairs of pretzel knots
(
(−2, 3, 3 + 2p), (−2, 3, 3− 2p)
)
for
p = 2, 3,... , as well as the ﬁgure-eight knot and its sister, which all have the sa me class in the
Bloch group (and classes diﬀering by 6-torsion in the extended Bloch group), but diﬀerent
invariantsSM,n for n≥ 1.
The extra information necessary to determine the SM,n can be described as follows. Recall
that ifT is a regular ideal triangulation of M withN tetrahedra, its shapes z = (z1,...,z N )
satisfy a system of polynomial equations, one equation for every e dge, and one imposing
parabolic holonomy around the meridian of the cusp [ Thu77, NZ85]. Let us set
(1.6) z′
i = (1−zi)−1, z ′′
i = 1−z−1
i .
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 5
The equations can then be written in the form
(1.7) zAz′′B :=
N∏
j=1
z
Aij
j
(
1−z−1
j
) Bij
=±1, (i = 1,...,N ),
where A and B areN×N square matrices with integer entries, which we call the Neumann-
Zagier matrices following [
NZ85].
Deﬁnition 1.1. IfT is a regular ideal triangulation of M, its Neumann-Zagier datum (resp.,
enhanced Neumann-Zagier datum ) is given by the triple
βT = (z, A, B) resp., ˆβT = (z, A, B,f ),
where z is a solution to the gluing equations and f is a combinatorial ﬂattening of T , a
collection of integers that we deﬁne in Section 2.4.
As we will discuss in detail in Section 2, implicit in the above deﬁnition is the dependence
of βT and ˆβT on the following choices:
(1) a pair of opposite edges for every oriented ideal tetrahedron (a so-called choice of
quad type),
(2) an edge of T ,
(3) a meridian loop in the boundary of M in general position with respect to T ,
(4) a combinatorial ﬂattening.
