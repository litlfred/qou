---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-004-14-results
section_title: "Results"
section_number: 1.4
pages: 6-7
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
semisimple G, including the rotation and the ﬂip. In other words, we prese nt a constructive result of the
following theorem.
6
Theorem 1.1. For a split semisimple simply-connected (or centerless) alg ebraic groupG over Q, there exists
a quiver Q, quiver mutations µrot and µﬂip , and a coordinate map M.
The map M associates coordinates of a ﬂag conﬁguration to the coordin ates on the cluster ensemble for
Q, the quiver mutation µrot describes how the coordinates change under rotation of an ord ered triangle and
µﬂip describes how the coordinates change under retriangulation.
We call this collection (Q,µ rot,µ ﬂip, M) a F ock–Goncharov coordinate structure . The construction
algorithm is presented in Section 5. First, we use the algori thm of [FZ99, Section 2], using a speciﬁc choice of
w0 (the longest word in the Weyl group) by Fact 2.10. This produc es a quiver whose A-coordinates generate
the coordinate ring for B− =H ×N−. We call this quiver Q0.
The quiver Q0 has the same mutable portion that we need for Q. However, the non-mutable portion isn’t
complete, so Q0 does not have triangulation-compatible symmetry (see Deﬁnition 4.15). We therefore
can apply the rotation µrot to Q0, and deﬁne Q to be the smallest quiver with triangulation-compatible
symmetry containing Q0.
The quiver Q and the map M allow constructing representation varieties easily given a triangulation of
a surface: a copy of Q is inscribed on each triangle and vertices along edges are id entiﬁed. The maps µrot
and µﬂip describe how the coordinate functions of the variety respon d to retriangulation, ensuring that the
variety itself is independent of triangulation choices.
Remark 1.2. The existence of cluster ensemble structures was shown non- constructively, and by diﬀerent
methods, in [GS18].
This theorem can also be used to compute representation vari eties for 3-manifolds, following work of
Zickert. In this case, quivers are drawn on each face of each i deal tetrahedron in the triangulation. The map
µﬂip describes the relation between coordinates on the four tria ngular faces of each tetrahedron. The variety
constructed is not, however, independent of triangulation . If the triangulation is suﬃciently ﬁne, however,
the variety detects all representations.
