---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-026-combinatorial-spatial-graph-floer-homology
section_title: "Combinatorial Spatial Graph Floer Homology"
section_number: null
pages: 54-58
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Shelly L. Harvey
Knot Floer homology, introduced by Ozsv´ath and Szab´o [6], and independently
by Rasmussen [8], is an invariant of knots in S3 that categoriﬁes the Alexander
polynomial. Knot Floer homology is widely studied because of its many applica-
tions in low-dimensional topology. For example, it detects the unknot [5], detects
whether a knot is ﬁbered [1, 4], and detect the genus of a knot [5]. The theory
was generalized to links in [7]. We extend their theory for balanced spatial graphs
in S3.
Originally, knot Floer homology was deﬁned as the homology of a chain complex
obtained by counting certain holomorphic disks in a 2g-dimensional symplectic
Invariants in Low-Dimensional Topology and Knot Theory
55
manifold with some boundary conditions that arose from a (doubly pointed) Hee-
gaard diagram for S3 compatible with the knot. As such, the chain groups were
combinatorial but one could not, a priori, compute the boundary map for a partic-
ular example. However, Sucharit Sarkar discovered an criterion that would ensure
that the count of certain holomorphic disks was combinatorials. This idea was
used by Manolescu, Ozsv´ath, and Sarker in [2] to give a combinatorial descrip-
tion of link Floer homology using grid diagrams. Using this description, in [3],
Manolescu, Ozsv´ath, Sz´abo, and D. Thurston gave a self-contained, combinatorial
proof that link Floer homology is an invariant.
We generalize the combinatorial description and proof in [2, 3] for certain spatial
graphs. The class of spatial graphs that we work with are embeddings of oriented
graphs with a transverse disk at each vertex splitting up the incoming and outgoing
edges. Morevoer, we require that there must be the same number of incoming edges
as outgoing edges at each vertex. We call these spatial graphs balanced.
To deﬁne the chain complex, we ﬁrst introduce the notion of a graph grid
diagram for a balanced spatial graph. Roughly, a grid diagram for a spatial graph
is an n×n grid of squares each of which is decorated with an X, an O, or is empty
and that satisﬁes some conditions. Like for links, there is precisely one O per row
and column. However, there may be many Xs in each row and column but they
must be grouped around a single O and be in L-formation. An O grouped with
multiple Xs corresponds to a vertex of the spatial graph. Note, for this deﬁnition,
we do not need to have the same number of incoming edges as outgoing edges. See
Figure 1 for an example.
O
X
X
X
O
O
O
O
X
X
X
Figure 1. Example of a graph grid diagram
We associate an oriented spatial graph to a grid diagram by connecting the
Xs to the Os vertically and the Os to the Xs horizontally.
We also use the
convention that the vertical strands go over the horizontal strands. See Figure 2
for an example.
We prove that any two representative for the same spatial graph are related by
a sequence of graph grid moves.
Theorem 1. If f : G →S3 is a balanced graph then there is grid diagram gr(f)
representing f. Moreover, if gr(f) and gr′(f) are two grid diagrams representing
56
Oberwolfach Report 28/2012
O
X
X
X
O
O
O
O
X
X
X
Figure 2. Associating a spatial graph to a graph grid diagram
f then the grid diagrams are related by a ﬁnite sequence of the following moves:
cyclic permutation, commutation’, and stabilization.
We remark that the only move that diﬀers from that of links is commutation’.
Next, we deﬁne the chain complex (C−(gr(f)), ∂−) associate to a graph grid
diagram gr(f). The chain groups consist of free modules over F[U1, . . . , UV ] where
F ∼= Z/2Z is the ring with two elements and V is the number of vertices in
the graph. Like in link Floer homology, the generators of the chain groups are
unordered tuples of intersections between the horizontal and vertical curves in the
grid. The Maslov grading is deﬁned exactly as in [3]. Note that this is possible
since it only depends on the set of Os on the grid.
For links, the Alexander
grading lives in Zm. For spatial graphs, we deﬁne an Alexander grading that has
values in H1(S3 \ f(G)) which can be identiﬁed with Zm after choosing a basis.
To deﬁne this, for each point in the lattice of the grid, we deﬁne an element of
H1(S3 \ f(G)), called the generalized winding number. It is deﬁned so that if
you can get from one point to another by passing under an edge of f(G) then
the diﬀerence between their values is the homology class of the meridian of that
edge. The Alexander grading of a generator is deﬁned by taking the sum of the
generalized winding numbers of the elements in the set. Each Ui is associated
with a vertex O and we deﬁne the Alexander grading so that multiplication by
Ui correspond to lowering the Alexander grading by the element of H1(S3 \ f(G))
represented by a meridian of the vertex corresponding to Ui.
The ∂−map is
deﬁned by counting empty rectangles in the (toroidal) grid that do not contain
an X. We show that ∂−◦∂−= 0 and hence this gives a well-deﬁned bigraded
homology group for each graph grid diagram. Moreover, one can show that the
homology is independent of the choice of grid.
Theorem 2. If gr(f) and gr′(f) are two graph grid diagrams representing
f : G →S3 then (C−(gr(f)), ∂−) and (C−(gr′(f)), ∂−) are quasi-isomorphic as
F[U1, . . . , UV ]-modules.
To prove this, we show that the quasi-isomorphism type of the chain complex
is preserved under the three graph grid moves. This gives a bigraded homology
module over F[U1, . . . , UV ] associated to each balanced spatial graph.
Invariants in Low-Dimensional Topology and Knot Theory
57
One can set all the Uis to zero and take the bigraded Euler characteristic of the
homology (or chain complex). This will give a multivariable polynomial associated
to the spatial graph. We show that this polynomial is equal to the torsion of a
certain chain complex associated to the spatial graph.
References
[1] Paolo Ghiggini, Knot Floer homology detects genus-one ﬁbred knots, Amer. J. Math. 130
(2008), no. 5, 1151–1169.
[2] Ciprian Manolescu, Peter Ozsv´ath, and Sucharit Sarkar, A combinatorial description of knot
Floer homology, Ann. of Math. (2) 169 (2009), no. 2, 633–660.
[3] Ciprian Manolescu, Peter Ozsv´ath, Zolt´an Szab´o, and Dylan Thurston, On combinatorial
link Floer homology, Geom. Topol. 11 (2007), 2339–2412.
[4] Yi Ni, Link Floer homology detects the Thurston norm, Geom. Topol. 13 (2009), no. 5,
2991–3019.
[5] Peter Ozsv´ath and Zolt´an Szab´o, Holomorphic disks and genus bounds, Geom. Topol. 8
(2004), 311–334.
[6] Peter Ozsv´ath and Zolt´an Szab´o, Holomorphic disks and knot invariants, Adv. Math. 186
(2004), no. 1, 58–116.
[7] Peter Ozsv´ath and Zolt´an Szab´o, Holomorphic disks, link invariants and the multi-variable
Alexander polynomial, Algebr. Geom. Topol. 8 (2008), no. 2, 615–692.
[8] Jacob Andrew Rasmussen, Floer homology and knot complements, Ph.D. thesis, Harvard
University, 2003.
Parity Biquandles
Aaron Kaestner
(joint work with Louis H. Kauﬀman)
We use crossing parity to construct a generalization of biquandles for virtual
knots which we call Parity Biquandles. These structures include all biquandles
as a standard example referred to as the even parity biquandle. Additionally, we
ﬁnd all Parity Biquandles arising from the Alexander Biquandle and Quaternionic
Biquandles. Examples are provided showing that using this method we can ﬁnd
examples of parity biquandles which are distinct from the associated even parity
biquandle. Furthermore we discuss some related results and additional directions
for this research.
References
[1] D. Bar-Natan, The Jones Polynomial on the Knot Atlas, http://katlas.org/wiki/The_
Jones_Polynomial.
[2] A. Bartholomew, R. Fenn, Biquandles of Small Size and some Invariants of Virtual and
Welded Knots, arXiv:1001.5127.
[3] A. Bartholomew, R. Fenn, Quaternionic Invariants of Virtual Knots and Links, J. Knot
Theory Ramiﬁcations 17 (2008), no. 2, 231–251.
[4] R. H. Crowell, R. H. Fox, Introduction to Knot Theory, Ginn and Co., 1963.
[5] H. Dye, Invariants from the Linking Number, arXiv:1007.1175.
[6] R. Fenn, M. Jordan-Santana, L. Kauﬀman, Biquandles and virtual links, Topology and its
Applications, 145 (2004), 157–175.
58
Oberwolfach Report 28/2012
[7] M.N.Goussarov, M.Polyak, O. Viro, Finite Type Invariants of Classical and Virtual Knots,
Topology 39 (2000), no. 5, 1045–1068.
[8] J. Green, A Table of Virtual Knots, http://www.math.toronto.edu/drorbn/Students/
GreenJ/.
[9] D. Hrencecin, L. Kauﬀman, Biquandles for Virtual Knots, J. Knot Theory Ramiﬁcations
16 (2007), no. 10, 1361–1382.
[10] D. P. Ilyutko, V. O. Manturov, I. M. Nikonov, Virtual Knot Invariants Arising From Par-
ities, arXiv:1102.5081.
[11] F. Jaeger, L. Kauﬀman, H. Saleur, The Conway Polynomial in R3 and in Thickened Sur-
faces: A New Determinant Formulation, J. Combin. Theory (B) 61 (1994), 237–259.
[12] A. Kaestner, L. H. Kaufmann, Parity Biquandles, arXiv:1103.2825.
[13] L. Kauﬀman, A self-linking invariant of virtual knots, Fund. Math. 184 (2004), 135–158.
[14] L. Kauﬀman, Introduction to Virtual Knot Theory, arXiv:1101.0665.
[15] Louis H. Kauﬀman, Knots and Physics, World Scientiﬁc, Singapore/New Jersey/London/
Hong Kong, 1991.
[16] L. Kauﬀman, Virtual Knot Theory, European J. Combin. 20 (1999), 663–690.
[17] L. Kauﬀman, V. O. Manturov, Virtual Biquandles, Fundamenta Mathematicae 188 (2005),
103–146.
[18] L. Kauﬀman, D. Radford, Bi-oriented Quantum Algebras, and a Generalized Alexander
Polynomial for Virtual Links, Contemp. Math. 318 (2003), 113–140.
[19] D. Yu. Krylov, V. O. Manturov, Parity and Relative Parity in Knot Theory, arXiv:
1101.0128.
[20] V. O. Manturov, A Functorial Map from Knots in Thickened Surfaces to Classical Knots
and Generalisations of Parity, arXiv:1011.4640.
[21] V. O. Manturov, On Invariants of Virtual Links, Acta Appl. Math. 72 (2002), no. 3, 295–
309.
[22] V. O. Manturov, Parity in knot theory, Sbornik: Mathematics 201 (2010), no. 5, 65–110.
[23] S. Nelson, Link invariants from ﬁnite biracks, arXiv:1002.3842.
[24] J. Sawollek,
On Alexander-Conway polynomials for virtual knots and links. arXiv:
math/9912173.
[25] D. S. Silver, S. G. Williams, Alexander Groups and Virtual Links, J. Knot Theory Ramiﬁ-
cations 10 (2001), no. 1, 151–160.
[26] V. Turaev, Cobordism of knots on surfaces, J. Topol. 1 (2008), no. 2, 285–305.
[27] M. Wada, Twisted Alexander Polynomial for ﬁnitely presentable groups, Topology 33
(1994), no. 2, 241–256.
