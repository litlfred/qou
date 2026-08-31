---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation Calvin McPhail-Snyder Duke University calvin@sl2.site"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-3
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
doc_brief: "Octahedral coordinates from the Wirtinger presentation Calvin McPhail-Snyder Duke University calvin@sl2.site — Letρ be a representation of a knot group (or more generally, the funda- mental group of"
---
[Thu02] W. Thurston, The geometry and top-
ology of three-manifolds
[Yok00] Y. Yokota,On the volume conjecture
for hyperbolic knots. arXiv
[KKY18] H. Kim, S. Kim, and S. Yoon, “Oc-
tahedral developing of knot complement. I:
Pseudo-hyperbolic structure”. arXiv doi
[KKY23] H. Kim, S. Kim, and S. Yoon, “Oc-
tahedral developing of knot complement. II:
Ptolemy coordinates and applications”. arXiv
doi
[CKK14] J. Cho, H. Kim, and S. Kim, “Opti-
mistic limits of Kashaev invariants and com-
plex volumes of hyperbolic links”. arXiv doi
[McP22] C. McPhail-Snyder, Hyperbolic struc-
tures on link complements, octahedral decom-
positions, and quantum sl2. arXiv
[MR] C. McPhail-Snyder and N. Reshetikhin,
In preparation.
[Bla+20] C. Blanchet et al., “Holonomy braid-
ings, biquandles and quantum invariants of
links with SL2(C) flat connections”. arXiv
doi
[Kas97] R. M. Kashaev, “The hyperbolic vol-
ume of knots from quantum dilogarithm”.
arXiv doi
Contents
1 Introduction 1
2 Octahedral colorings 3
3 The holonomy of an octahedral coloring 6
4 Gauge transformations 12
5 Shape parameters and the potential function 13
Bibliography 18
1. Introduction
Studying representations of knot and 3-manifold groups into SL2(C) is important in low-
dimensional topology. The isometry group of hyperbolic 3-space is PSL2(C), so this problem
is closely related to the study of hyperbolic structures [Thu02]. While one can study repre-
sentations algebraically, say via the Wirtinger presentation of the knot group, it is sometimes
better to work more geometrically. For example, for geometric invariants like the hyperbolic
volume it is usually better to work with the geometric parameters of an ideal triangulation of
the knot complement than directly withρ.
In this paper we are concerned with a particular family of ideal triangulations adapted
to knot diagrams. Given a diagramD of a knotK the octahedral decomposition decomposes
S3\K minus two points into a union of octahedra, with one for each crossing of the diagram.
By further subdividing into tetrahedra one can obtain an ideal triangulation of a standard form.
This works just as well for links and tangles. The geometric data of the tetrahedra are naturally
described by octahedral coordinates; these are implicit in work of Yokota [Yok00] and have been
studied systematically by Kim, Kim, and Yoon [KKY18; KKY23]. When studying geometric
properties of a representation the octahedral coordinates are quite useful; for example, they
enable a direct computation of the hyperbolic volume and Chern-Simons invariant [CKK14].
Our version of these coordinates is motivated by connections to the representation theory of
quantum groups [McP22; MR].
While the octahedral coordinates are geometrically natural they can be difficult to solve for
in practice. Instead we might find representations of the knot group by some other method
and then try to find the corresponding octahedral coordinates. Given a representation ρ :
π1(S3\K) → SL2(C) described by its values on Wirtinger generators one can use the
methods of Blanchet et al. [Bla+20] to find octahedral coordinates corresponding to ρ. This
gives a somewhat complicated inductive method that does not usually produce simple formulas.
In addition, some representations do not come from octahedral coordinates (one might have to
conjugate first) and there is not a simple way to check when this occurs.
In this paper we give an elementary method (Definition 2.10 and Theorem 1) for determining
the octahedral coordinates of a tangle diagram directly fromρ. As an application we give an
explicit criterion (Corollary 5.7) for whether a representation corresponds to a smooth critical
point of the potential function of a knot diagramD; this question is relevant to the saddle-point
method used in most approaches to the Volume Conjecture. Our characterization depends only
onρ andD, not the details of the triangulation.
The Volume Conjecture proposes that the asymptotics of the Kashaev invariants of a
hyperbolic knot recover geometric information like the hyperbolic volume [Kas97]. The
Kashaev invariants are naturally associated with the octahedral decomposition, and most
proofs of special cases of the conjecture proceed via studying an associated potential function
[Yok00]. The potential function is defined on a space parametrizing the geometry of the ideal
1. Introduction 2
[SY18] M. Sakuma and Y. Yokota, “An appli-
cation of non-positively curved cubings of
alternating links”. arXiv doi
[GMT16] S. Garoufalidis, I. Moffatt, and D. P.
Thurston, Non-peripheral ideal decompositions
of alternating knots. arXiv
[McP21] C. McPhail-Snyder, “ SL2(C)-
holonomy invariants of links”. arXiv
[McP] C. McPhail-Snyder, “A quantization
of the SL2(C) Chern-Simons invariant”. In
preparation.
[Cho18] J. Cho, “Quandle theory and the op-
timistic limits of the representations of link
groups”. arXiv doi
[IK14] A. Inoue and Y. Kabaya, “Quandle ho-
mology and complex volume”. arXiv doi
[McP23] C. McPhail-Snyder, Can distinct
meridians commute in a knot group?
tetrahedra: it has singularities where they are degenerate and critical points at nondegenerate
solutions of the gluing equations of the triangulation. To apply the saddle-point method to
the asymptotics of the Kashaev invariant it is important to use a diagram whose potential
function has a smooth critical point at the complete hyperbolic structure. This question has
been previously studied using other techniques [SY18; GMT16] and it is known that every
hyperbolic knot that is alternating or has at most 12 crossings has such a diagram. We show in
Theorem 3 that for knot diagrams this condition is equivalent to being arc-faithful, meaning
that the Wirtinger generators of the over and under arcs at each crossing are always distinct.
This new characterization may prove useful for showing that the potential function has smooth
critical points.
Quantum topology provides another motivation for our results. One can define [McP21;
McP] a geometrically twisted version of the Kashaev invariant that can also be understood as a
quantization of the SL2(C) Chern-Simons invariant, which includes the hyperbolic volume.
The construction of this invariant uses the octahedral coordinates in an essential way and we
expect the results of this paper to be useful for computing and studying it.
This paper began as an attempt to re-derive and generalize a formula [Cho18, Theorem 3.2]
of Cho for boundary-parabolic representations. Equation (11) is similar to but more general than
[Cho18, Theorem 3.2] and our proof is quite different. Cho’s result is more closely connected
to the quandleP of parabolic elements of PSL2(C), and in particular to a presentation of it
due to Inoue and Kabaya [IK14]. It would be interesting to better understand how our results
relate toP and if this can be generalized to the boundary non-parabolic case.
Organization
